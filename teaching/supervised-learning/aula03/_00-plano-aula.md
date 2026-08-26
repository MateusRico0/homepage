## Resumo — Aula 3: Árvores de Decisão — Particionamento Guloso

### Posição no curso

A Aula 2 fechou apontando uma limitação compartilhada por tudo que vimos
até aqui: tanto a fronteira gaussiana com covariância compartilhada quanto
o Naive Bayes decidem a **forma** da fronteira de decisão *antes* de olhar
para os dados — ela é sempre linear, por construção do modelo paramétrico
escolhido. Esta aula introduz uma família de modelos que inverte essa
lógica: árvores de decisão não assumem nenhuma forma paramétrica para
$p(\mathbf{x}\mid\mathcal{C}_k)$ — elas particionam recursivamente o
espaço de entrada em regiões, e ajustam um modelo constante (uma média,
ou uma proporção de classe) dentro de cada uma. O ponto central da aula:
o critério de split que costuma ser ensinado como pura heurística
("escolha o corte que mais reduz a impureza") é, na verdade, o mesmo
princípio que já sustentou o curso inteiro — maximização de
verossimilhança —, só que aplicado a um modelo não-paramétrico (constante
por partes) em vez de um modelo paramétrico fixo.

### Pré-requisitos

Aulas 1–2 completas: densidades condicionais por classe, regra do
posterior máximo, teoria da decisão formal, Naive Bayes e o preço da
suposição de independência. Estimação por máxima verossimilhança para
distribuições categóricas e gaussianas (usada informalmente nas Aulas
1–2; formalizada aqui). Não exige nada de Cálculo além de encontrar o
máximo de uma função de uma variável.

### Objetivos de aprendizagem

- **ML Concept:** O algoritmo CART para classificação e regressão.
- **Statistical Concept:** Estimação não-paramétrica da densidade
  condicional como função constante por partes. Medidas de impureza
  (Entropia e Gini) interpretadas como incerteza de distribuições
  categóricas, e splits entendidos como maximização gulosa de uma
  log-verossimilhança de perfil.
- **Objectives:** Reinterpretar particionamento recursivo como um
  procedimento de estimação não-paramétrica guiado por verossimilhança,
  em vez de uma heurística.
- **Expected Competencies:** Implementar CART, calcular ganhos de
  impureza, e justificar critérios de split em termos de maximização de
  log-verossimilhança.

*(fonte dos objetivos: `../index.md`, Lesson 3 — planejamento fixo do
semestre)*

### Estratégia Pedagógica

**Estratégia A (Outside-In)** — Árvores de Decisão é o exemplo
explicitamente citado em `../../CLAUDE.md` para esta estratégia. A aula
já abre pelo modelo mental informal que o aluno provavelmente já tem
("corte até ficar homogêneo", tratado como pura heurística por "a
maioria dos cursos") e usa exatamente esse senso comum como gancho para
a necessidade teórica ("por baixo do capô, é o mesmo princípio de MLE
de sempre"), antes de formalizar Gini/entropia/verossimilhança de
perfil, fechando com síntese e limitações (preço da liberdade
não-paramétrica). **Adicionado nesta revisão (2026-08-26)** para
conformidade com a nova política de `../../CLAUDE.md`; sem mudança de
conteúdo no `index.qmd`.

### Sobre as fontes

O tratamento de árvores de decisão desta aula é conceitualmente padrão
(particionamento recursivo, ajuste de constante por folha, critérios de
impureza, poda por custo-complexidade) — a exposição abaixo é nossa, e a
citação literal específica (equações, números de página) fica reservada
para `01-fontes.md`, na Etapa 3, onde cada trecho é conferido
diretamente contra o PDF antes de ser usado.

**Achado técnico verificado nesta sessão, antes de escrever a aula:** a
conexão entre impureza e log-verossimilhança de perfil (o ponto central
desta aula) não é uma citação de nenhum livro — é uma reformulação
estatística nossa, **derivada e verificada numericamente** (script
Python, à parte da aula) antes de ser incorporada:

1. **Classificação:** o estimador de máxima verossimilhança de uma
   distribuição categórica numa folha, com contagens $n_{\tau k}$, é a
   proporção empírica $\hat p_{\tau k} = n_{\tau k}/N_\tau$ — verificado
   testando a log-verossimilhança contra várias distribuições
   candidatas. A log-verossimilhança maximizada é
   $\ell_\tau(\hat p_\tau) = N_\tau \sum_k \hat p_{\tau k}\ln\hat p_{\tau k} = -N_\tau H(\hat p_\tau)$,
   onde $H(p) = -\sum_k p_k\ln p_k$ é a entropia (convenção padrão, com o
   sinal negativo). Logo, **maximizar a log-verossimilhança equivale a
   minimizar a entropia** — exatamente o critério de crescimento da
   árvore.
2. **Regressão:** sob um modelo gaussiano com média constante por folha
   e variância compartilhada, o estimador de máxima verossimilhança da
   média é a média amostral, e maximizar a log-verossimilhança equivale
   a minimizar a soma de quadrados residuais — verificado numericamente
   com dados simulados.

::: {.callout-warning}
**Inconsistência encontrada numa fonte, ao verificar a matemática.** Uma
formulação de "cross-entropy" comum na literatura de árvores omite o
sinal negativo padrão da entropia e ainda assim descreve, em prosa, um
comportamento (valor mínimo nas bordas $p=0,1$, máximo em $p=0{,}5$) que
só é verdadeiro **com** o sinal. Verificado numericamente: a fórmula sem
o sinal tem esse comportamento invertido. Usamos a convenção padrão (com
o sinal), que é a que faz a conexão com log-verossimilhança funcionar e
a que bate com a descrição em prosa da fonte — o trecho citado em
`01-fontes.md` preserva a formulação exatamente como impressa, sem
"corrigi-la" ali.
:::

### Exercícios (quotas fixas do `CLAUDE.md`)

- **Notas (HTML):** seção de Exercícios ao final, com **exatamente 3
  questões discursivas/conceituais** e **12 questões de V/F** (12 blocos
  de 4 itens cada, um tema por bloco), cada bloco em `::: {.callout-tip}`
  titulado com o tema.
- **Slides (RevealJS):** **no mínimo 3 exercícios de checagem** (V/F de 4
  itens), espalhados ao longo dos slides, cada um em seu próprio slide
  com título real (`##` fora da caixa), seguido imediatamente por um
  slide de resposta separado.
- **Pausas ativas** entre blocos: pergunta direta como título real do
  slide, caixa `callout-tip` abaixo com a instrução de escrever/comparar.

## Plano de aula — Aula 3 (carga horária estimada: ~110–120min)

### Bloco 0 — Abertura (5 min)

Recapitular a ponte da Aula 2: fronteiras gaussianas e Naive Bayes são
sempre lineares — a forma é decidida antes de ver os dados. Pergunta que
abre a aula: e se deixássemos os próprios dados decidirem a forma da
fronteira, sem suposição paramétrica alguma?

### Bloco 1 — Árvores como estimação não-paramétrica (15 min)

Particionamento recursivo do espaço de entrada em regiões cuboides,
alinhadas aos eixos; cada região recebe um modelo constante. Um exemplo
visual simples (poucas regiões, árvore binária correspondente) ilustra a
ideia antes de qualquer fórmula. Interpretação central do bloco: isto é
uma estimativa não-paramétrica de $p(\mathbf{x}\mid\mathcal{C}_k)$ (ou de
$\mathbb{E}[t\mid\mathbf{x}]$) como função constante por partes — o
oposto do que Naive Bayes e a gaussiana faziam. O preço dessa liberdade é
o assunto dos Blocos 4–5.

### Bloco 2 — Árvores de regressão: verossimilhança gaussiana (20 min)

Critério: a predição em cada folha é a média dos alvos que caem nela, e
o erro de ajuste é a soma de quadrados residuais. Núcleo estatístico do
bloco: mostrar (com a verificação já feita) que isso é exatamente o
estimador de máxima verossimilhança de um modelo gaussiano com média
constante por folha — a mesma equivalência entre mínimos quadrados e
máxima verossimilhança que a Aula 5 vai formalizar para hiperplanos,
aqui aplicada a um modelo constante por partes. Crescimento guloso: busca
exaustiva sobre variável de split e limiar, porque otimizar a estrutura
inteira de uma vez é combinatorialmente inviável.

### Bloco 3 — Árvores de classificação: verossimilhança categórica, entropia e Gini (25 min)

Núcleo estatístico da aula. Mostrar (com a verificação já feita) que o
estimador de máxima verossimilhança categórico numa folha é a proporção
empírica de cada classe, e que maximizar a log-verossimilhança resultante
equivale a **minimizar a entropia** da distribuição de classes na folha
— a reformulação estatística do critério de impureza mais comum.
Apresentar o **índice de Gini** como alternativa, com sua própria
interpretação (a taxa de erro esperada de um classificador que sorteia
rótulos ao acaso segundo as proporções da folha), sem forçar a mesma
conexão de verossimilhança — Gini não é um MLE de forma tão direta quanto
a entropia. Comparar com a taxa de erro de classificação bruta: por que
ela não serve para *crescer* a árvore (não é diferenciável, é pouco
sensível a mudanças nas probabilidades) mas é a preferida para *podar*.

### Bloco 4 — Poda e o critério de custo-complexidade (20 min)

Por que não parar de crescer a árvore cedo, mesmo quando um split não
reduz o erro: empiricamente, um split "inútil" isolado pode habilitar um
split seguinte muito bom — a busca gulosa é míope demais para enxergar
isso na hora. Prática recomendada: crescer uma árvore grande, depois
podar. O critério de poda soma o erro residual de todas as folhas a uma
penalidade proporcional ao número de folhas; o peso dessa penalidade é
escolhido por validação cruzada — ponte direta com a Aula 4 (Model
Selection and Resampling), que formaliza exatamente esse tipo de escolha.

### Bloco 5 — Limites e fechamento (10–15 min)

Três limitações estruturais das árvores: (1) splits alinhados aos eixos
podem ser muito subótimos para fronteiras que não se alinham a eles — uma
fronteira a 45° (o próprio caso de covariância compartilhada não-diagonal
da Aula 2!) precisaria de muitos splits para ser aproximada, enquanto a
gaussiana da Aula 2 a captura numa única direção; (2) instabilidade —
pequenas mudanças nos dados de treino podem produzir uma estrutura de
árvore bem diferente; (3) partição rígida — cada ponto pertence a
exatamente uma folha, produzindo previsões descontínuas, particularmente
ruim para alvos de regressão suaves. Fechamento: a mesma liberdade que
permite à árvore capturar qualquer fronteira também a torna instável e
gulosamente míope — nenhum dos dois extremos (sempre linear vs.
totalmente livre) é gratuito. Ponte para a Aula 4: escolher a
complexidade certa é uma instância do problema geral de seleção de
modelo e validação cruzada — e ponte de mais longo alcance para a Aula 9
(Ensemble Theory): a instabilidade que aqui é fraqueza da árvore isolada
é exatamente o que torna o *bagging* eficaz mais adiante no curso.
