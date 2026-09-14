# Respostas da Aula 4 — Pausas Ativas

> Arquivo de apoio, não publicado (prefixo `_`). Discussão em prosa das
> 5 pausas ativas do `index.qmd` (a pergunta motivadora + a resolução
> do V/F, que no `index.qmd` só aparece nos slides RevealJS, nunca nas
> notas HTML).
>
> (O gabarito dos 7 blocos de V/F da seção Exercícios **não** é
> discutido aqui — vive em `exercicios.qmd`/`soluções.qmd`, páginas
> públicas e separadas desta aula.)

### Pausa 1 — Ruído do HDBSCAN vs. ambiguidade do GMM

A pergunta pergunta se um paciente marcado como ruído pelo HDBSCAN é
necessariamente "igualmente parecido" com as duas populações. Não é: o
HDBSCAN mede densidade **local geométrica** (o paciente não tem vizinhos
suficientes por perto, na escala de `min_samples`/`min_cluster_size`),
enquanto o GMM mede probabilidade **sob um modelo global** ajustado a
todos os dados. As duas noções podem discordar — um paciente pode
escapar do limiar de densidade local do HDBSCAN e, ainda assim, cair
claramente dentro da elipse de um único componente do GMM, com
responsabilidade próxima de $1$. A responsabilidade $50/50$ também não
depende só de distância euclidiana bruta às médias: como a fórmula de
Bayes pondera pela densidade completa (incluindo covariância e peso de
mistura), duas médias diferentes com formas/pesos diferentes podem
deslocar o ponto de equilíbrio para longe do ponto médio geométrico. No
caso degenerado em que os dois componentes têm exatamente a mesma média
e covariância, a densidade cancela na razão de Bayes e sobra só
$\gamma(z_k)=\pi_k$, independente de onde o ponto está — um bom
lembrete de que a responsabilidade é sempre uma função dos parâmetros
inteiros do modelo, não só da posição do ponto.

- ✔ Um paciente marcado como ruído pode receber responsabilidade
  próxima de $1$ sob um GMM — "vale geométrico local" e "ambiguidade
  probabilística global" não são a mesma coisa.
- ✗ Responsabilidade $0{,}5/0{,}5$ não implica equidistância euclidiana
  bruta — depende de $\pi_k$ e $\Sigma_k$ também.
- ✔ Com densidades idênticas nos componentes, a razão de Bayes cancela
  o termo de densidade, sobrando só $\pi_k$, para qualquer ponto.
- ✔ A mesma lógica (sobreposição contínua pede resposta contínua)
  transfere para qualquer domínio com segmentos que se misturam.

### Pausa 2 — O que significa responsabilidade 50/50

A pergunta contrasta a incerteza de uma moeda (evento futuro, ainda não
decidido) com a incerteza sobre a origem de um paciente (fato já
determinado, mas desconhecido para nós). A responsabilidade $50/50$ é a
melhor estimativa do modelo sobre um fato fixo — o paciente realmente
nasceu de uma única população, o GMM só não tem evidência suficiente
nos dois atributos usados para decidir qual. Mais atributos não reduz
automaticamente essa ambiguidade: pode até piorar (maldição da
dimensionalidade, Aula 2) ou simplesmente confirmar que a sobreposição
é real também em mais dimensões. No Passo M (Bloco 6), um paciente
$50/50$ não é descartado nem ignorado — ele contribui com metade do seu
peso para a reestimação de **cada** um dos dois componentes,
exatamente como fração. E se o modelo verdadeiro tivesse só $1$
componente, esperaríamos ver muito mais gente perto de $50/50$ (na
verdade, todo mundo perto de $\pi_k$ para $K=1$ isso seria trivialmente
$1$, mas a intuição geral é: quanto menos separação real, mais gente na
faixa ambígua) do que os $9$ casos observados, que são a exceção, não a
regra, entre os $569$ pacientes.

- ✔ É incerteza sobre um fato já determinado, não sobre um evento
  aleatório futuro.
- ✗ Mais atributos não garante menos ambiguidade para pontos
  específicos.
- ✔ Responsabilidade fracionária = peso fracionário no Passo M, nunca
  descartado.
- ✔ Com um único componente verdadeiro, a ambiguidade tenderia a ser
  muito mais disseminada do que os $9$ casos raros observados.

### Pausa 3 — Responsabilidade muda com os parâmetros

A pergunta testa se $\gamma(z_{nk})$ é uma propriedade fixa do ponto ou
uma função dos parâmetros correntes do modelo. É a segunda: a cada
rodada do EM, os parâmetros mudam (Passo M) e a responsabilidade é
recalculada do zero a partir deles (novo Passo E) — não existe
"responsabilidade permanente" de um paciente. Sobre o efeito de dobrar
a covariância do componente maligno: o raciocínio "gaussiana mais
espalhada sempre atribui mais densidade a todo ponto" é uma falsa
generalização — a densidade gaussiana se normaliza a integral $1$, então
espalhar a covariância **reduz o pico** e aumenta a cauda; o efeito
líquido sobre a responsabilidade de um ponto específico depende de
onde ele está (perto do pico ou na cauda), não é uniformemente "mais
densidade". Dois pacientes idênticos em atributos, com a mesma
responsabilidade hoje, podem divergir depois de uma rodada de
reestimação porque o Passo M usa a soma sobre **todos** os pontos —
qualquer assimetria em como os dois entram nessa soma agregada (por
exemplo, se um deles aparece duplicado no dataset) muda o resultado
para ambos de forma diferente. Com $K=1$, não há termo concorrente no
denominador de Bayes — a razão degenera trivialmente em $1$.

- ✔ $\gamma(z_{nk})$ é recalculada a cada rodada — função corrente dos
  parâmetros, nunca fixa ao ponto.
- ✗ Covariância maior reduz o pico da densidade (normalização) — o
  efeito sobre $\gamma$ depende da posição do ponto, não é sempre
  "aumenta".
- ✔ Dois pacientes idênticos podem divergir se entrarem de forma
  assimétrica nas somas agregadas do Passo M.
- ✔ Com $K=1$, a razão de Bayes degenera em $1$ para o único
  componente, sempre.

### Pausa 4 — GMM completo é sempre melhor que o KMeans?

A pergunta pede para não tratar "o GMM generaliza matematicamente o
KMeans" como "o GMM é sempre a escolha prática melhor". As quatro
afirmações exploram por que não: (1) mais parâmetros (covariância livre
por componente) exige mais dados para estimar sem overfitar — com
poucos pontos por cluster, o KMeans, mais restrito, generaliza melhor;
(2) se os clusters verdadeiros já são esféricos e homogêneos entre si,
o GMM convergiria para algo parecido com a suposição do KMeans, e a
vantagem prática se estreita; (3) um cluster alongado é exatamente o
caso em que a liberdade de covariância do GMM compensa — o KMeans,
travado em bolas circulares do mesmo tamanho, cortaria esse cluster de
forma artificial perto da fronteira com outro; (4) "caso particular
matemático" (um limite formal) não implica nada sobre velocidade de
convergência prática — o KMeans, com menos parâmetros e uma atualização
mais simples por iteração, tipicamente converge em menos iterações, não
mais.

- ✔ Mais parâmetros com poucos dados por cluster pode overfitar —
  KMeans generaliza melhor nesse regime.
- ✔ Com covariâncias verdadeiramente esféricas e idênticas, a vantagem
  prática do GMM sobre o KMeans encolhe.
- ✔ Cluster alongado: GMM orienta/estica a elipse; KMeans corta
  artificialmente na fronteira.
- ✗ "Caso particular" é relação de limite matemático, não de
  velocidade — KMeans tipicamente converge em menos iterações.

### Pausa 5 — Mais componentes, mais verossimilhança? (fechamento)

A pergunta antecipa o problema central da Aula 5: por que a
log-verossimilhança de treino não serve, sozinha, para escolher $K$.
Qualquer solução com $K=2$ pode ser "imitada" por uma solução com
$K=10$ simplesmente zerando o peso $\pi_k$ dos $8$ componentes extras —
logo, o ótimo com $K=10$ nunca é pior que o ótimo com $K=2$ no mesmo
conjunto de treino. Isso é exatamente por que escolher $K$ maximizando
a verossimilhança de treino não é confiável: o critério empurra sempre
para mais componentes, não para o número real. A mesma lógica de "mais
flexibilidade sempre ajusta melhor o treino, sem necessariamente
generalizar" já apareceu nesta disciplina antes (por exemplo, ajustar
formas cada vez mais flexíveis aos dados de treino sem controle de
complexidade). E colapsar a covariância de um dos $10$ componentes
sobre um único ponto não dá uma verossimilhança "artificialmente
baixa" — dá uma verossimilhança tendendo a **infinito** (a
singularidade do Bloco 4), o oposto do que a afirmação sugere.

- ✔ $K=10$ nunca fica pior que $K=2$ no treino — pode sempre "imitar" a
  solução menor.
- ✗ Por isso mesmo não é um critério confiável — sempre favorece mais
  componentes.
- ✔ É a mesma lógica de overfitting já vista antes nesta disciplina.
- ✗ Colapsar sobre um ponto dá verossimilhança tendendo a infinito, não
  "baixa".
