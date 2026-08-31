## Resumo — Aula 3: Topografia de Densidade e Grafos — Clustering Hierárquico e HDBSCAN

Esta aula muda o objeto de estudo de "estimar quão comum um ponto é"
(Aula 2) para "agrupar pontos parecidos, sem saber de antemão quantos
grupos existem nem que forma eles têm". A tese central: um **cluster**
é uma componente conexa de uma região de alta densidade — um "conjunto
de nível" $\{\mathbf{x} : p(\mathbf{x}) \ge \lambda\}$ — e não uma bola
em torno de um centróide. Essa mudança de definição é o que permite
clusters de forma arbitrária, e é também o que conecta clustering a
teoria de grafos: a distância ao $K$-ésimo vizinho $d_K(\mathbf{x})$,
já construída na Aula 2 como estimador de densidade, reaparece aqui
como peso de aresta num grafo, e a Árvore Geradora Mínima (MST) desse
grafo contém, ao mesmo tempo, toda a hierarquia de clusters possível em
qualquer limiar $\lambda$. O HDBSCAN soma a essa construção uma ideia
nova — **persistência estatística** — para decidir quais clusters da
hierarquia são estruturas reais dos dados, e quais são apenas flutuação
amostral, sem exigir que o usuário escolha $\lambda$ (ou $K$) a priori.

**Pré-requisitos:** Aula 2 completa — em particular, $d_K(\mathbf{x})$
como medida de densidade local (inversamente relacionada: $d_K$ pequeno
= região densa), e o aviso de que $k$-NN/KDE não escapam da maldição da
dimensionalidade, só trocam sua forma.

**Estratégia Pedagógica:** Estratégia A (Outside-In) — HDBSCAN é um
algoritmo concreto (como Árvores de Decisão, citado no `CLAUDE.md` como
exemplo canônico de Estratégia A), e a aula é guiada por um gancho
prático (clusters de forma arbitrária que métodos baseados em centróide
não capturam) antes da formalização em teoria de grafos.

**Dataset-fio:** Breast Cancer Wisconsin (o mesmo da Aula 2), agora
usado sem os rótulos de diagnóstico durante o clustering — o rótulo
benigno/maligno só reaparece no final, para conferir se a estrutura
encontrada de forma não supervisionada corresponde a algo real.
Complementado por um contraexemplo sintético controlado (duas luas ou
dois anéis concêntricos) — uso explicitamente permitido pelo
`CLAUDE.md` para isolar um ponto matemático específico: aqui, o ponto é
"forma arbitrária, não convexa", que o próprio Breast Cancer Wisconsin
(clusters aproximadamente convexos) não ilustraria bem.

## Plano de aula — Aula 3 (carga horária: ~120min)

1. **Abertura — O que "cluster" deveria significar** (~15 min) —
   Organizador prévio: a Aula 2 estimou densidade ponto a ponto; hoje
   perguntamos o que fazer com essa densidade — como transformá-la em
   grupos. Revisão rápida de $d_K(\mathbf{x})$. Roteiro explícito: (i)
   por que "distância ao centróide" falha para formas arbitrárias; (ii)
   o que é um cluster como conjunto de nível de densidade; (iii) como
   construir isso com um grafo, sem escolher o número de clusters de
   antemão; (iv) como decidir quais clusters são reais. Problema
   motivador: mostrar (sem resolver ainda) um exemplo em que agrupar
   pelos $k$ centróides mais próximos visivelmente corta um cluster
   verdadeiro em pedaços errados. Pausa ativa fechando o bloco.

2. **Intuição — Vales e Montanhas, Não Bolas** (~12 min) — Preview
   gráfico e conceitual, antes de qualquer formalismo: densidade como
   uma "paisagem" (montanhas = regiões densas, vales = regiões raras);
   um cluster é uma montanha inteira, não importa a forma do seu
   contorno. Mostrar lado a lado, no exemplo sintético de duas
   lu­as/anéis: agrupamento por centróide (falha, corta ao meio) vs.
   "andar sempre por terreno alto" (sucesso, cada lua/anel é um cluster
   inteiro). Isso já entrega o resultado final; falta só nomear os
   passos.

3. **Conjuntos de Nível de Densidade** (~10 min) — Formalizar
   $\{\mathbf{x} : p(\mathbf{x}) \ge \lambda\}$: para $\lambda$ alto,
   poucas regiões pequenas e bem separadas (picos); conforme $\lambda$
   cai, as regiões crescem e podem se fundir. Isso já é, em germe, uma
   hierarquia de clusters indexada por $\lambda$ — o objeto que o resto
   da aula vai construir de forma computável.

4. **Da Densidade ao Grafo: Distância de Alcançabilidade Mútua**
   (~18 min) — Premissas + passo a passo: por que $d_K(\mathbf{x})$
   (já construído na Aula 2) serve como "distância ao vale mais
   próximo" (*core distance*); por que a distância bruta entre dois
   pontos não é suficiente para construir o grafo (dois pontos podem
   estar próximos em distância bruta mas em regiões de densidade muito
   diferentes); derivação da distância de alcançabilidade mútua
   $d_{\text{mreach}}(a,b) = \max(\text{core}(a), \text{core}(b),
   d(a,b))$ e por que ela "acalma" pontos em regiões raras.

5. **A Árvore Geradora Mínima e o Clustering Hierárquico Clássico**
   (~15 min) — Construir o grafo completo com pesos
   $d_{\text{mreach}}$; a MST desse grafo. Resultado citado e verificado
   num exemplo pequeno: cortar as $k-1$ arestas mais pesadas da MST
   reproduz exatamente o clustering hierárquico por ligação simples
   (*single linkage*) com $k$ clusters — a MST comprime a hierarquia
   inteira numa única estrutura, sem refazer o cálculo para cada
   $\lambda$.

6. **Condensando a Árvore e Medindo Persistência** (~20 min) — O
   problema do corte único: um $\lambda$ (ou $k$) fixo não serve para
   um dataset com clusters de densidades bem diferentes entre si.
   Construir a árvore condensada (fundir ramos menores que
   `min_cluster_size`); definir **persistência** de um cluster como a
   integral de quanto tempo ele "sobrevive" como componente distinta ao
   longo da faixa de $\lambda$ (excesso de massa); extrair os clusters
   de maior persistência, possivelmente em níveis diferentes da
   hierarquia. Aplicar ao Breast Cancer Wisconsin (sem rótulos) e só
   então comparar a partição encontrada com o diagnóstico real.

7. **Síntese: o Que o HDBSCAN Compra, e o Que Ainda Custa** (~10 min)
   — Recapitular o algoritmo de ponta a ponta. Não exige escolher $K$
   nem $\lambda$ globalmente — mas exige `min_cluster_size`/
   `min_samples`, que ainda é uma escolha de escala. Herda a mesma
   maldição da dimensionalidade da Aula 2: em muitas dimensões, $d_K$
   (e portanto a alcançabilidade mútua) perde poder discriminativo.

8. **Fechamento e Ponte para a Aula 4** (~10 min) — Retomar as quatro
   perguntas da abertura, uma frase cada. O que fica em aberto: HDBSCAN
   dá uma partição **rígida** (cada ponto pertence a um cluster, ou é
   ruído) — a Aula 4 (Gaussian Mixture Models e EM) relaxa isso para
   atribuição **probabilística**, útil quando os clusters genuinamente
   se sobrepõem.

**Nota de dados (verificado nesta sessão):** `sklearn.cluster.HDBSCAN`
está disponível no kernel `sensibleml-moo` (scikit-learn 1.8.0) — usar
essa implementação, não o pacote `hdbscan` externo (não instalado).
