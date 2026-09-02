# Soluções — Exercícios de Verdadeiro/Falso (Aula 3)

> Arquivo de apoio, não publicado (prefixo `_`). Contém a heurística e a
> justificativa de cada item de V/F da seção "Exercícios" do `index.qmd`.
> O `index.qmd` publicado nunca tem essa resolução — é trabalho do aluno
> resolver por conta, fora do horário de aula.

### Cluster como componente conexa vs. distância a centróide — item (a)

**Heurística:** Falsa equivalência

**Afirmação:** ✗ Se um cluster verdadeiro tem formato de "U" (uma curva fechada quase se tocando nas duas pontas), uma atribuição por protótipo mais próximo com um número suficientemente grande de protótipos eventualmente recupera esse formato exato como um único cluster, só fragmentando-o internamente em pequenas células convexas que, somadas, aproximam bem o "U".

**Resposta:** Falso

**Justificativa:** Mesmo que a soma de muitas células convexas pequenas aproxime visualmente a forma do "U", essa abordagem nunca produz "um único cluster" para essa forma — a saída são tantos rótulos distintos quantos protótipos, um por célula de Voronoi, cada um tratado como um cluster separado. "Aproximar a forma via muitos fragmentos" e "recuperar como um único cluster" são coisas diferentes: a definição de cluster por atribuição a protótipo é por rótulo, não por proximidade entre fragmentos vizinhos. Juntar os fragmentos num único cluster exigiria um passo adicional que não faz parte dessa regra de atribuição.

### Cluster como componente conexa vs. distância a centróide — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ A convexidade de cada célula de Voronoi é uma consequência necessária de usar distância euclidiana ao protótipo mais próximo como regra de atribuição — não uma escolha adicional independente de qual algoritmo específico é usado para posicionar os protótipos.

**Resposta:** Verdadeiro

**Justificativa:** A célula de cada protótipo $k$ é a interseção dos semiespaços "mais perto de $k$ do que de qualquer $j$" — toda interseção de semiespaços é convexa, por definição, para qualquer métrica induzida por norma (a euclidiana inclusa). Não existe uma variante de "atribuição ao protótipo mais próximo" que produza células não-convexas; a convexidade nasce da própria regra de atribuição, não é algo escolhido além dela.

### Cluster como componente conexa vs. distância a centróide — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um cluster definido como componente conexa de um conjunto de nível $L_\lambda$ pode, em princípio, ter qualquer formato geométrico, inclusive não-convexo, desde que exista um caminho contínuo dentro de $L_\lambda$ ligando quaisquer dois de seus pontos.

**Resposta:** Verdadeiro

**Justificativa:** A definição do Bloco 3 (componente conexa) não impõe nenhuma restrição de forma — qualquer subconjunto de $L_\lambda$ que seja "percorrível" internamente conta como uma única componente, seja qual for seu contorno (espiral, forma de "U", ramificado etc.), desde que exista uma trilha inteiramente dentro de $L_\lambda$ ligando dois pontos quaisquer dela — inclusive formas nunca vistas nos exemplos da aula (luas, anéis).

### Cluster como componente conexa vs. distância a centróide — item (d)

**Heurística:** Falsa equivalência

**Afirmação:** ✗ Se dois pontos pertencem à mesma componente conexa de $L_\lambda$, isso implica que a distância euclidiana direta entre eles é menor do que a distância de qualquer um dos dois a pontos fora dessa componente.

**Resposta:** Falso

**Justificativa:** Conectividade por densidade não controla distância geométrica direta — é exatamente o ponto central da Abertura: duas pontas de uma lua podem estar geometricamente mais distantes entre si do que cada uma está de pontos do lado de fora do cluster, mas próximos em linha reta (do outro lado do vale). "Estar no mesmo cluster" (via trilha densa) e "estar geometricamente mais próximo" são propriedades independentes; confundir as duas reintroduz, pela porta de trás, a suposição de convexidade que a definição pretende evitar.

---

### Conjuntos de nível e a hierarquia indexada por $\lambda$ — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ Decrescer $\lambda$ de um valor alto para um valor baixo pode dividir uma componente conexa de $L_\lambda$ em duas, além de poder fundir componentes existentes.

**Resposta:** Falso

**Justificativa:** $L_\lambda$ só pode crescer (nunca encolher) conforme $\lambda$ diminui, porque $\{\mathbf{x}:p(\mathbf{x})\ge\lambda\}$ é um conjunto cada vez maior para $\lambda$ menor. Um conjunto que só cresce nunca separa uma região previamente conectada em duas — crescer pode conectar regiões antes separadas (fundir), mas nunca desconecta uma região já conectada. É exatamente a propriedade citada no Bloco 3: "decrescer $\lambda$... nunca separa componentes que já estavam unidas".

### Conjuntos de nível e a hierarquia indexada por $\lambda$ — item (b)

**Heurística:** Caso limite

**Afirmação:** ✔ Se duas regiões de alta densidade são separadas por um vale de densidade exatamente zero em pelo menos um ponto do caminho entre elas, então, para qualquer $\lambda>0$, elas nunca aparecem como uma única componente conexa de $L_\lambda$.

**Resposta:** Verdadeiro

**Justificativa:** Se existe um ponto no caminho com $p(\mathbf{x})=0$, esse ponto nunca pertence a $L_\lambda$ para nenhum $\lambda>0$ (precisaria $p(\mathbf{x})\ge\lambda>0$). Sem esse ponto, qualquer trilha entre as duas regiões que passe por ele fica quebrada dentro de $L_\lambda$ — as duas regiões nunca se tornam uma componente conexa só, para nenhum $\lambda$ positivo. Essa é a "barreira genuína" mencionada na resposta da pausa ativa do Bloco 2.

### Conjuntos de nível e a hierarquia indexada por $\lambda$ — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ A definição de cluster via $L_\lambda$ dispensa completamente a necessidade de qualquer parâmetro de escala, ao contrário de uma atribuição por protótipos fixos (que exige escolher quantos protótipos usar).

**Resposta:** Falso

**Justificativa:** $L_\lambda$ substitui a escolha de "quantos protótipos" por uma escolha diferente — o próprio $\lambda$ (ou, no HDBSCAN, `min_cluster_size`/`min_samples`) — não elimina a necessidade de uma decisão de escala. A Síntese (Bloco 7) deixa isso explícito: `min_cluster_size` "ainda é uma escolha de escala". Trocar um parâmetro por outro não é o mesmo que eliminar o parâmetro.

### Conjuntos de nível e a hierarquia indexada por $\lambda$ — item (d)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ ESL (p. 507) descreve "buscadores de moda" (*mode seekers*) como um paradigma que estima diretamente as modas da densidade e atribui cada observação à moda mais próxima — um paradigma distinto tanto do combinatório quanto da modelagem por mistura.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente o texto citado no Bloco 3 (ESL, p. 507, tradução livre): "buscadores de moda... tentando estimar diretamente as modas distintas da densidade... observações mais próximas de cada moda definem os clusters". Os três paradigmas citados ao longo da aula (combinatório, modelagem por mistura, *mode seeking*) são distintos entre si.

---

### Core distance: o mesmo $d_K$ da Aula 2, novo uso — item (a)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ $\mathrm{core}_K(\mathbf{x})$ pequeno continua significando região densa, exatamente como $d_K(\mathbf{x})$ significava na Aula 2 — a fórmula não mudou, só o papel que a quantidade desempenha (estimador de densidade vs. peso de aresta).

**Resposta:** Verdadeiro

**Justificativa:** O Bloco 4 define explicitamente $\mathrm{core}_K(\mathbf{x})=d_K(\mathbf{x})$ — é literalmente o mesmo número, sem alteração de fórmula; só o uso muda, de estimador direto de densidade (Aula 2) para peso de aresta num grafo (Aula 3, via alcançabilidade mútua).

### Core distance: o mesmo $d_K$ da Aula 2, novo uso — item (b)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Se $K$ for aumentado (por exemplo, de 5 para 50), o valor de $\mathrm{core}_K(\mathbf{x})$ para um ponto numa região densa tende a variar relativamente menos do que o mesmo aumento de $K$ produziria para um ponto numa região rara — a mesma propriedade discutida na Aula 2 para $d_K$.

**Resposta:** Verdadeiro

**Justificativa:** Numa região densa, muitos vizinhos estão a distâncias parecidas entre si, então aumentar $K$ adiciona vizinhos a distâncias próximas (baixa variação relativa); numa região rara, os vizinhos ficam espalhados, e aumentar $K$ precisa alcançar vizinhos cada vez mais distantes, produzindo maior variação relativa — a mesma sensibilidade a $K$ discutida para $d_K$ na Aula 2, herdada sem alteração porque $\mathrm{core}_K$ é literalmente $d_K$.

### Core distance: o mesmo $d_K$ da Aula 2, novo uso — item (c)

**Heurística:** Falsa equivalência

**Afirmação:** ✗ Dois pontos com o mesmo valor de $\mathrm{core}_K$, para o mesmo $K$, necessariamente moram na mesma região do espaço de atributos.

**Resposta:** Falso

**Justificativa:** $\mathrm{core}_K$ é um escalar — dois pontos podem ter exatamente o mesmo valor estando em regiões completamente diferentes do espaço (ex.: duas montanhas distintas, cada uma com densidade local parecida, mas geometricamente distantes uma da outra). "Mesmo valor de uma estatística de densidade local" não implica "mesma localização" — $\mathrm{core}_K$ descarta toda informação posicional, guardando só uma medida de escala local.

### Core distance: o mesmo $d_K$ da Aula 2, novo uso — item (d)

**Heurística:** Contrafactual

**Afirmação:** ✗ $\mathrm{core}_K(\mathbf{x})$, como usado nesta aula, não depende em nada da escolha de $K$ — é uma propriedade fixa de cada ponto, independente de qualquer parâmetro.

**Resposta:** Falso

**Justificativa:** $\mathrm{core}_K(\mathbf{x})=d_K(\mathbf{x})$ é, por definição, a distância ao $K$-ésimo vizinho mais próximo — depende diretamente da escolha de $K$ ($K$ diferente, vizinho diferente, distância diferente). É exatamente o parâmetro de escala mencionado na Síntese (Bloco 7): `min_samples`, "que desempenha o papel de $K$ no *core distance*".

---

### Distância de alcançabilidade mútua — item (a)

**Heurística:** Caso limite

**Afirmação:** ✔ $d_{\mathrm{mreach}}(a,b) \ge d(a,b)$ vale sempre, para quaisquer $a,b$ e qualquer $K$ — a alcançabilidade mútua nunca aproxima dois pontos além de sua distância bruta.

**Resposta:** Verdadeiro

**Justificativa:** Por definição, $d_{\mathrm{mreach}}(a,b) = \max(\mathrm{core}_K(a), \mathrm{core}_K(b), d(a,b))$ — o máximo de um conjunto que inclui $d(a,b)$ é, por definição, sempre maior ou igual a $d(a,b)$. É exatamente a propriedade "nunca aproxima, só afasta" destacada no Bloco 4.

### Distância de alcançabilidade mútua — item (b)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Se $a$ e $b$ estão ambos em regiões muito densas (ambos os *core distances* pequenos), $d_{\mathrm{mreach}}(a,b)$ é, em geral, determinado pela distância bruta $d(a,b)$, não pelos núcleos.

**Resposta:** Verdadeiro

**Justificativa:** Quando $\mathrm{core}_K(a)$ e $\mathrm{core}_K(b)$ são pequenos (menores que $d(a,b)$, o caso comum dentro de uma mesma região densa), o máximo é dominado pelo terceiro termo, $d(a,b)$ — exatamente o comportamento "a distância bruta domina o máximo" descrito no Bloco 4 para pontos que moram na mesma montanha.

### Distância de alcançabilidade mútua — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Num cenário em que $a$ está numa região densa e $b$ está isolado bem longe de qualquer vizinho, $d_{\mathrm{mreach}}(a,b)$ é necessariamente igual a $d(a,b)$, porque o núcleo de $a$ (pequeno) domina o máximo.

**Resposta:** Falso

**Justificativa:** O máximo é dominado pelo termo MAIOR, não pelo menor — um núcleo pequeno (de $a$) nunca "domina" o máximo. É o núcleo grande de $b$ (o ponto isolado) que domina, forçando $d_{\mathrm{mreach}}(a,b) \ge \mathrm{core}_K(b)$, tipicamente maior que $d(a,b)$. O item inverte a lógica do máximo: confundir "qual termo é pequeno" com "qual termo decide o resultado" é o erro central.

### Distância de alcançabilidade mútua — item (d)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Trocar a distância bruta $d$ por $d_{\mathrm{mreach}}$ em todo o grafo pode mudar quais arestas pertencem à MST, comparado à MST construída sobre a distância bruta original.

**Resposta:** Verdadeiro

**Justificativa:** $d_{\mathrm{mreach}}$ reordena e infla pesos de forma não-uniforme (afasta seletivamente pontos isolados, mantém pontos densos praticamente inalterados) — a ordenação relativa de arestas pode mudar: uma aresta que era a mais barata sob distância bruta pode deixar de ser sob $d_{\mathrm{mreach}}$ (se um dos extremos tiver *core distance* grande), alterando quais arestas entram na árvore geradora mínima.

---

### MST e a equivalência com ligação simples — item (a)

**Heurística:** Caso limite

**Afirmação:** ✔ Para um conjunto de $N$ pontos, a MST sobre a matriz de distâncias brutas tem sempre exatamente $N-1$ arestas, independente de quantos clusters "verdadeiros" existam nos dados.

**Resposta:** Verdadeiro

**Justificativa:** É uma propriedade de teoria de grafos, não dos dados: qualquer árvore geradora de um grafo conexo com $N$ vértices tem exatamente $N-1$ arestas, por definição de árvore — independentemente de quantos "clusters verdadeiros" (um conceito estatístico, não estrutural) existam.

### MST e a equivalência com ligação simples — item (b)

**Heurística:** Caso limite

**Afirmação:** ✔ Cortar as $k-1$ arestas mais pesadas da MST produz sempre uma partição em exatamente $k$ componentes conexas, para qualquer $1\le k\le N$.

**Resposta:** Verdadeiro

**Justificativa:** Remover uma aresta de uma árvore sempre a desconecta em exatamente dois pedaços (árvores não têm ciclos, então cada aresta é uma "ponte"); remover $k-1$ arestas de uma árvore de $N-1$ arestas, uma por vez, produz exatamente $k$ componentes — vale para qualquer $k$ entre $1$ (nenhuma removida) e $N$ (todas as $N-1$ removidas).

### MST e a equivalência com ligação simples — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Se a MST inteira for reconstruída usando $d_{\mathrm{mreach}}$ em vez da distância bruta, o resultado de "cortar as $k-1$ arestas mais pesadas" ainda corresponde ao clustering de ligação simples — mas agora sobre as distâncias de alcançabilidade mútua, não sobre as distâncias brutas originais.

**Resposta:** Verdadeiro

**Justificativa:** O resultado clássico (MST-corte = ligação simples) é uma propriedade puramente de teoria de grafos, válida para qualquer matriz de pesos simétrica não-negativa — não depende de a matriz ser distância bruta especificamente. Trocar por $d_{\mathrm{mreach}}$ (ainda uma matriz de pesos válida) preserva a equivalência, só sobre a métrica nova.

### MST e a equivalência com ligação simples — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ No exemplo numérico do Bloco 5 (7 pontos, grupos A, B e o ponto isolado 6), o fato de A e B se fundirem antes de 6 se juntar a qualquer um deles (no corte $k=2$) é uma inconsistência do algoritmo de ligação simples, não uma consequência esperada da definição $d_{SL}(G,H)=\min_{i\in G,i'\in H}d_{ii'}$.

**Resposta:** Falso

**Justificativa:** É uma consequência direta e correta da definição — a distância mínima entre A e B ($6{,}14$) é, por pouco, menor que a distância mínima entre qualquer um dos dois grupos e o ponto 6 ($6{,}22$); ligação simples funde sempre o par de menor dissimilaridade primeiro, então A-B se fundem antes por definição, não por erro. O próprio Bloco 5 sinaliza isso: "correto pela definição de ligação simples", mesmo sendo contraintuitivo à primeira vista.

---

### O defeito do encadeamento (*chaining*) — item (a)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ O encadeamento citado do ESL ocorre porque a ligação simples define a proximidade entre dois grupos pelo par mais próximo entre eles, ignorando todos os outros pares — uma única cadeia de pontos intermediários basta para acionar uma fusão.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente a definição de $d_{SL}$ (mínimo entre pares) e a explicação do ESL citada no Bloco 5: como só uma dissimilaridade pequena entre um par já basta, uma série de pontos intermediários próximos entre si (mesmo que os extremos da cadeia estejam distantes) já é suficiente para encadear uma fusão de baixo nível.

### O defeito do encadeamento (*chaining*) — item (b)

**Heurística:** Falsa equivalência

**Afirmação:** ✗ Ligação completa (*complete linkage*, que usa a distância máxima entre pares, não a mínima) sofreria exatamente do mesmo defeito de encadeamento que a ligação simples, pela mesma razão matemática.

**Resposta:** Falso

**Justificativa:** Ligação completa usa o MÁXIMO entre pares — para fundir dois grupos, todos os pares precisam estar relativamente próximos, não só um. Isso é o oposto do mecanismo do encadeamento (que explora um único par próximo ignorando os demais); ligação completa tende, ao contrário, a produzir clusters compactos, não encadeados — o defeito citado é específico à regra do mínimo, não generaliza para o máximo.

### O defeito do encadeamento (*chaining*) — item (c)

**Heurística:** Contrafactual

**Afirmação:** ✔ Um único ponto de ruído inserido bem no meio do vale entre dois clusters genuinamente distintos pode, por si só, fazer a ligação simples fundir os dois num nível de dissimilaridade artificialmente baixo.

**Resposta:** Verdadeiro

**Justificativa:** Um ponto no meio do vale cria dois pares de distâncias curtas (ponto-a-A e ponto-a-B), cada uma menor que a distância direta A-B — a ligação simples usa o mínimo entre pares, então essas novas distâncias curtas fazem a fusão ocorrer num nível de dissimilaridade bem mais baixo do que sem o ponto extra.

### O defeito do encadeamento (*chaining*) — item (d)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ $d_{\mathrm{mreach}}$ reduz a chance de encadeamento causado por pontos isolados de baixa densidade, mas não elimina, por si só, todo encadeamento possível — daí a necessidade adicional de `min_cluster_size` no HDBSCAN.

**Resposta:** Verdadeiro

**Justificativa:** $d_{\mathrm{mreach}}$ penaliza pontos com *core distance* grande (isolados), reduzindo o caso mais comum de encadeamento por pontos raros — mas uma cadeia de pontos moderadamente densos (não isolados o bastante para ter *core distance* alto) ainda pode encadear via distância bruta dominando o máximo; por isso o HDBSCAN precisa da defesa adicional de `min_cluster_size` (Bloco 6).

---

### Árvore condensada — item (a)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Na árvore condensada, um ramo com menos que `min_cluster_size` pontos, ao se separar do seu ramo-pai, é tratado como "pontos perdidos" do pai, não como um cluster novo — mesmo que, na hierarquia completa (não condensada), esse ramo aparecesse como uma divisão legítima.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente o Passo 1 do algoritmo descrito no Bloco 6: ramos pequenos (abaixo de `min_cluster_size`) são tratados como "pontos que se perderam do cluster pai", não como novos ramos — independentemente de a hierarquia completa (sem condensamento) já registrar essa divisão como um evento válido.

### Árvore condensada — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Condensar a árvore usando `min_cluster_size` elimina completamente a necessidade de qualquer outro parâmetro de escala no HDBSCAN, já que a persistência decide tudo o mais automaticamente.

**Resposta:** Falso

**Justificativa:** O HDBSCAN ainda depende de `min_samples` (o $K$ do *core distance*), além de `min_cluster_size` — a persistência decide QUAIS ramos sobrevivem dada a árvore condensada, mas não decide, por si só, o que conta como "denso" em primeiro lugar (isso vem de `min_samples`/*core distance*) nem o tamanho mínimo de ramo (`min_cluster_size`). Dois parâmetros de escala continuam presentes.

### Árvore condensada — item (c)

**Heurística:** Caso limite

**Afirmação:** ✔ Aumentar `min_cluster_size` tende a reduzir o número de ramos que sobrevivem como clusters candidatos na árvore condensada, comparado a um `min_cluster_size` menor sobre a mesma hierarquia completa.

**Resposta:** Verdadeiro

**Justificativa:** Um `min_cluster_size` maior exige que mais ramos sejam fundidos ao pai (só ramos suficientemente grandes contam como cluster candidato) — isso reduz o número total de ramos candidatos sobreviventes, comparado a um limiar menor sobre a mesma hierarquia.

### Árvore condensada — item (d)

**Heurística:** Contrafactual

**Afirmação:** ✔ A árvore condensada de um conjunto de dados sem nenhuma estrutura de cluster real (por exemplo, uma única Gaussiana multivariada bem comportada) pode, ainda assim, ter ramos que sobrevivem ao condensamento, dependendo de `min_cluster_size` escolhido.

**Resposta:** Verdadeiro

**Justificativa:** Mesmo numa única Gaussiana (sem clusters verdadeiros), flutuações amostrais locais produzem sub-regiões de densidade ligeiramente mais alta/mais baixa; se `min_cluster_size` for pequeno o suficiente, algumas dessas flutuações podem, por acaso, ter tamanho suficiente para sobreviver ao condensamento — um cluster espúrio. É por isso que a persistência (não só o condensamento) é necessária para distinguir estrutura real de flutuação amostral.

---

### Persistência por excesso de massa — item (a)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ A persistência de um cluster candidato é definida somando, para cada ponto do ramo, o intervalo de $\lambda$ (ou de $1/d_{\mathrm{mreach}}$) em que esse ponto pertenceu a esse cluster específico antes de ser absorvido pelo pai ou virar ruído.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente a definição dada no Passo 2 do Bloco 6 — persistência (excesso de massa) é a soma, por ponto, do intervalo de sobrevivência daquele ponto como membro daquele cluster específico, ao longo da faixa de $\lambda$.

### Persistência por excesso de massa — item (b)

**Heurística:** Caso limite

**Afirmação:** ✔ Um cluster que aparece por uma faixa muito curta de $\lambda$ antes de se fundir com outro tem, em geral, persistência mais baixa do que um cluster de tamanho comparável que sobrevive por uma faixa longa de $\lambda$.

**Resposta:** Verdadeiro

**Justificativa:** Persistência é, por definição, uma soma sobre o intervalo de sobrevivência — para tamanho de ramo comparável, uma faixa mais curta de $\lambda$ produz uma soma menor do que uma faixa mais longa; é diretamente a definição de "excesso de massa" (mais tempo sobrevivendo = mais massa acumulada).

### Persistência por excesso de massa — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ A extração final por persistência, em cada ramificação da árvore condensada, escolhe sempre "dividir nos dois filhos" em vez de "manter o pai inteiro", porque dois clusters específicos têm, por definição, mais persistência somada do que um cluster genérico.

**Resposta:** Falso

**Justificativa:** A extração (Passo 3) escolhe o lado de MAIOR persistência total entre as duas opções — não há garantia de que "dividir" sempre vença; se o pai (antes de dividir) já acumulou muita massa sozinho e os dois filhos, individualmente, têm persistências pequenas, manter o pai inteiro pode ter persistência total maior. Não existe uma regra fixa "dividir sempre vence" — é decidido caso a caso por programação dinâmica.

### Persistência por excesso de massa — item (d)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se dois clusters candidatos tivessem exatamente o mesmo tamanho (mesmo número de pontos), eles teriam, necessariamente, a mesma persistência, independente de quanto tempo cada um sobreviveu na hierarquia.

**Resposta:** Falso

**Justificativa:** Persistência depende do tamanho do ramo E de quanto tempo sobrevive (soma por ponto do intervalo de $\lambda$), não só do tamanho — dois clusters com o mesmo número de pontos, mas um sobrevivendo por uma faixa de $\lambda$ muito mais longa que o outro antes de se fundir ou virar ruído, têm persistências diferentes. Confundir "mesmo tamanho" com "mesma persistência" ignora a dimensão de faixa de $\lambda$ da definição.

---

### O resultado no Breast Cancer Wisconsin — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ O cluster de 54 pacientes encontrado no Bloco 6, sendo 100% malignos, é uma evidência de que HDBSCAN funcionou como um classificador treinado no rótulo `diagnosis` — o rótulo foi usado apenas para conferir o resultado depois, não durante o clustering.

**Resposta:** Falso

**Justificativa:** O item afirma duas coisas incompatíveis ao mesmo tempo. "Funcionar como um classificador treinado no rótulo" implicaria que o rótulo influenciou o ajuste — o que é falso: o HDBSCAN nunca viu `diagnosis` durante o clustering (só os dois atributos numéricos). O rótulo ter sido usado só para conferência posterior é justamente o que torna o resultado notável (estrutura real encontrada sem supervisão), não evidência de que funcionou "como classificador treinado" — a frase, como um todo, é falsa por misturar as duas ideias de forma incorreta.

### O resultado no Breast Cancer Wisconsin — item (b)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ O fato de 126 dos 212 pacientes malignos totais caírem em ruído (não em nenhum dos dois clusters) é consistente com a ideia de que tumores malignos variam mais em apresentação clínica do que tumores benignos, formando uma "montanha" de densidade menos coesa nesses dois atributos.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente a explicação dada no texto do Bloco 6 — tumores malignos têm múltiplos subtipos/estágios, então sua densidade nesses dois atributos é mais espalhada/menos coesa, formando uma "montanha" mais baixa e irregular que não sobrevive inteira como cluster de alta persistência; boa parte cai no "vale" entre o núcleo denso e a massa benigna, virando ruído.

### O resultado no Breast Cancer Wisconsin — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ O ARI de $0{,}644$ (excluindo ruído) sendo maior que o ARI de $0{,}493$ (incluindo ruído como rótulo) é esperado, porque excluir os pontos mais ambíguos (o ruído) da comparação tende a aumentar a concordância medida nos pontos restantes.

**Resposta:** Verdadeiro

**Justificativa:** Os pontos marcados como ruído são justamente os mais ambíguos/difíceis de classificar por densidade — excluí-los da comparação deixa só os pacientes que o HDBSCAN atribuiu com confiança a um dos dois clusters, que tendem a concordar mais fortemente com o diagnóstico real; incluir o ruído como uma "terceira categoria" reintroduz essa ambiguidade na métrica, reduzindo a concordância medida.

### O resultado no Breast Cancer Wisconsin — item (d)

**Heurística:** Caso limite

**Afirmação:** ✗ Se o HDBSCAN tivesse encontrado só ruído (nenhum cluster) nesses dois atributos, o ARI (incluindo ruído como rótulo) seria necessariamente próximo de $1$, já que todos os pontos receberiam o mesmo tratamento.

**Resposta:** Falso

**Justificativa:** Um ARI próximo de $1$ exige que a partição encontrada corresponda fortemente à partição verdadeira; "todos os pontos em ruído" é uma partição trivial (todo mundo no mesmo grupo) comparada contra duas categorias reais de diagnóstico bem distribuídas — o ARI para essa comparação seria próximo de ZERO (ausência total de estrutura descoberta), não próximo de $1$. "Tratar todos igual" não é o mesmo que "concordar com o rótulo real".

---

### Hiperparâmetros: `min_cluster_size` e `min_samples` — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Trocar a escolha de um valor de $\lambda$ global (nos métodos de corte único do Bloco 3) por uma escolha de `min_cluster_size` no HDBSCAN elimina, por completo, qualquer decisão de escala que o usuário precise tomar.

**Resposta:** Falso

**Justificativa:** Já discutido na Síntese (Bloco 7): `min_cluster_size` (e `min_samples`) ainda são escolhas de escala — o HDBSCAN troca uma decisão ($\lambda$) por outra (tamanho mínimo de cluster / $K$ do *core distance*), não elimina a necessidade de decisão alguma.

### Hiperparâmetros: `min_cluster_size` e `min_samples` — item (b)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Reduzir `min_cluster_size` para um valor muito pequeno (como 2) tende a reintroduzir uma versão do problema de encadeamento discutido para a ligação simples pura.

**Resposta:** Verdadeiro

**Justificativa:** Já verificado na pausa ativa do Bloco 6 — com `min_cluster_size=2`, cadeias finas de poucos pontos passam a contar como clusters válidos por si mesmas, reintroduzindo o mesmo mecanismo de encadeamento (fusões via par único próximo) que a ligação simples pura já sofria (Bloco 5).

### Hiperparâmetros: `min_cluster_size` e `min_samples` — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ `min_samples` desempenha, no HDBSCAN, um papel análogo ao de $K$ no *core distance* $\mathrm{core}_K(\mathbf{x})$ — ambos controlam quantos vizinhos definem a escala local de densidade.

**Resposta:** Verdadeiro

**Justificativa:** O Bloco 6 nomeia explicitamente `min_samples` como "o análogo de $K$ do *core distance*" — ambos determinam quantos vizinhos entram no cálculo da distância que define "quão densa" é a vizinhança de um ponto.

### Hiperparâmetros: `min_cluster_size` e `min_samples` — item (d)

**Heurística:** Falsa equivalência

**Afirmação:** ✗ Um cluster que só aparece ao forçar `min_cluster_size` bem mais alto do que o valor originalmente usado é, por esse único motivo, necessariamente tão confiável estatisticamente quanto um cluster que aparece de forma estável numa faixa ampla de valores testados.

**Resposta:** Falso

**Justificativa:** Aparecer só sob um ajuste forçado do parâmetro (e não numa faixa estável de valores) é evidência de sensibilidade ao limiar escolhido — um sinal de possível artefato, não de robustez. Um cluster que aparece de forma estável através de vários valores de `min_cluster_size` é evidência mais forte de estrutura real (mesma lógica discutida na pausa ativa do Bloco 7 sobre "resolver" a maldição da dimensionalidade forçando o parâmetro).

---

### Maldição da dimensionalidade herdada da Aula 2 — item (a)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ A queda de $70{,}5\%$ dos pacientes em algum cluster (com 2 atributos) para $100\%$ de ruído (com 30 atributos, `min_cluster_size≥10`) ocorre porque $\mathrm{core}_K$ é literalmente o mesmo $d_K(\mathbf{x})$ da Aula 2 — herda o mesmo mecanismo pelo qual distâncias perdem poder discriminativo em alta dimensão.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente a explicação do Bloco 7 — como $\mathrm{core}_K(\mathbf{x})=d_K(\mathbf{x})$ e $d_{\mathrm{mreach}}$ depende de $\mathrm{core}_K$ e da distância bruta, ambas herdam a perda de poder discriminativo de distâncias em alta dimensão (o mesmo mecanismo da maldição da Aula 2), fazendo a árvore condensada não encontrar ramo estável o bastante para sobreviver como cluster.

### Maldição da dimensionalidade herdada da Aula 2 — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Aumentar `min_cluster_size` até encontrar algum cluster de novo em 30 dimensões resolve a causa raiz da maldição da dimensionalidade para esse dataset, não só o sintoma de "nenhum cluster apareceu".

**Resposta:** Falso

**Justificativa:** Já resolvido na pausa ativa do Bloco 7 — forçar `min_cluster_size` mais alto ataca o sintoma (falta de clusters aparentes), não a causa (perda de poder discriminativo das distâncias em alta dimensão); um cluster que aparece só por esse ajuste não é necessariamente confiável.

### Maldição da dimensionalidade herdada da Aula 2 — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Uma atribuição por protótipos fixos (distância euclidiana a centros) aplicada aos mesmos 30 atributos padronizados está, em algum grau, imune à maldição da dimensionalidade, porque não usa nenhum estimador de densidade baseado em vizinhos como $\mathrm{core}_K$.

**Resposta:** Falso

**Justificativa:** Distância euclidiana a um protótipo fixo sofre sua própria versão da maldição (distâncias entre pontos e protótipos também perdem significado geométrico relativo em alta dimensão) — já apontado na resposta da pausa ativa do Bloco 7: "nenhum método baseado em distância escapa por completo". Não usar $\mathrm{core}_K$ especificamente não é o mesmo que estar imune à maldição em geral.

### Maldição da dimensionalidade herdada da Aula 2 — item (d)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Reduzir a dimensionalidade (por exemplo, escolher um subconjunto pequeno de atributos informativos, como feito no Bloco 6) antes de rodar HDBSCAN ataca a causa do problema, não só o sintoma.

**Resposta:** Verdadeiro

**Justificativa:** Reduzir dimensionalidade ataca diretamente a causa (distâncias perdendo poder discriminativo por excesso de dimensões, muitas delas pouco informativas) — é a mesma lição herdada da Aula 2 e explicitamente citada como a "rota mais direta" na resposta da pausa ativa do Bloco 7.

---

### Partição rígida vs. probabilística — ponte para a Aula 4 — item (a)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ A saída do HDBSCAN atribui cada ponto a exatamente um cluster, ou a ruído — nunca uma probabilidade de pertencimento a mais de um cluster ao mesmo tempo.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente a definição de partição "rígida" citada no Fechamento — cada paciente recebe um rótulo único (um dos clusters, ou ruído/$-1$), nunca uma distribuição de probabilidade entre múltiplos clusters simultaneamente.

### Partição rígida vs. probabilística — ponte para a Aula 4 — item (b)

**Heurística:** Contrafactual

**Afirmação:** ✗ Um paciente exatamente na fronteira entre o núcleo maligno denso e a massa benigna do Bloco 6, sob uma atribuição probabilística (Aula 4), receberia tipicamente uma probabilidade bem definida e próxima de $1$ para um único cluster, e próxima de $0$ para o outro — igual ao HDBSCAN, sem diferença prática nesse caso.

**Resposta:** Falso

**Justificativa:** É exatamente o caso em que a atribuição probabilística DIFERE do HDBSCAN — um ponto genuinamente na fronteira (onde os clusters se sobrepõem) receberia, sob GMM/EM, probabilidades intermediárias (não próximas de $0$ ou $1$) para os dois clusters, refletindo a ambiguidade real; forçar $0$/$1$ nesse caso seria o comportamento do HDBSCAN, não a diferença que a Aula 4 pretende introduzir.

### Partição rígida vs. probabilística — ponte para a Aula 4 — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ O ESL (p. 507) cita "modelagem por mistura" como um paradigma de clustering distinto tanto do combinatório (protótipos fixos) quanto do "*mode seeking*" (HDBSCAN) — os três paradigmas citados ao longo desta aula.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente a taxonomia de três paradigmas citada do ESL (Blocos 1 e 3): combinatório, modelagem por mistura, *mode seeking* — cada um distinto dos outros dois, com a modelagem por mistura reservada para a Aula 4.

### Partição rígida vs. probabilística — ponte para a Aula 4 — item (d)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ A escolha entre uma partição rígida (HDBSCAN) e uma probabilística (Aula 4) é, em essência, uma escolha sobre o quanto se acredita que os clusters verdadeiros se sobrepõem genuinamente, não uma escolha puramente de conveniência computacional.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente a conclusão da pausa ativa do Bloco 8 — a escolha reflete uma hipótese sobre a estrutura real dos dados (existe ou não um vale de densidade genuíno separando os grupos), não é uma questão de conveniência de implementação.
