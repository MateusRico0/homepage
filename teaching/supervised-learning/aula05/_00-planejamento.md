# Resumo — Aula 5

Primeira aula da "Parte 2: A História Linear Paramétrica". Introduz Regressão
Linear em duas camadas deliberadamente separadas: primeiro como um problema
puramente geométrico/algébrico (ajustar a reta/hiperplano que minimiza a
soma de quadrados dos resíduos — mínimos quadrados ordinários, OLS), depois
como um problema estatístico (assumir ruído gaussiano homocedástico
$Y\mid X\sim\mathcal N(\beta^T X,\sigma^2)$, construir a verossimilhança, e
maximizá-la). O núcleo matemático da aula é a prova de que essas duas
camadas coincidem: maximizar a verossimilhança gaussiana em $\beta$ é,
algebricamente, minimizar a soma de quadrados — OLS $=$ MLE sob normalidade.
Isso não é um resultado isolado: é a mesma estrutura "distribuição $\to$
verossimilhança $\to$ decisão" que a Revisão 1 revisou nas quatro primeiras
aulas, agora instanciada pela primeira vez sobre um alvo contínuo ligado
linearmente aos atributos — e o modelo a ser generalizado nas Aulas 7-9
(Bernoulli/GLM, prioris/MAP, decomposição viés-variância).

**Pré-requisitos** (conferidos contra `_progresso.md`): definição formal de
verossimilhança e MLE (Aula 3, caixa "Verossimilhança e MLE"); a estrutura
de três peças distribuição/verossimilhança/decisão (Revisão 1, Bloco 5); o
viés do MLE gaussiano de $\sigma^2$ (mencionado na Aula 3, retomado aqui
com números novos); o dataset *California Housing* e as variáveis
`MedInc`/`HouseAge`/`MedHouseVal` (já explicadas na Aula 3). Nenhuma
notação nova colide com símbolo já em uso — $\beta$ passa a denotar o vetor
de coeficientes da regressão (não confundir com o $\beta$ de precisão do
PRML, cuja notação evitamos deliberadamente no `index.qmd` em favor de
$\sigma^2$, mais comum em ESL e mais direta para quem já viu variância nas
Aulas 1-5).

**Estratégia Pedagógica:** Estratégia A (*Outside-In*) — Regressão Linear é
um modelo/algoritmo concreto, como Regressão Logística e SVM (exemplos
citados no `../CLAUDE.md`), não uma aula de fundamentação matemática pura;
a aula abre com o gráfico de dispersão real (`MedInc` × `MedHouseVal`) e a
pergunta catchy "qual é a melhor reta?", só formalizando a verossimilhança
gaussiana depois de a intuição geométrica (mínimos quadrados) já estar no
ar — prático antes do formal, a mesma lógica das Aulas 1-4. O ângulo
"MLE unifica tudo" (mais Estratégia B, "problema-fio") aparece como fio
condutor *dentro* da Estratégia A (ele é o "porquê" formal que a fase de
Teoria Formal revela), não como a estrutura macro da aula.

## Plano de aula — Aula 5 (carga horária: ~125min)

1. **Abertura** (~15 min) — Retomada da Revisão 1 (estrutura de três peças);
   ideia-ponte ("hoje a mesma estrutura, mas o alvo é contínuo e ligado
   linearmente aos atributos"); roteiro de 4 perguntas; problema motivador
   catchy — dispersão real `MedInc` × `MedHouseVal` do *California
   Housing*, "qual é a melhor reta, e o que 'melhor' quer dizer aqui?".
   Termina com Pausa Ativa 1 (testa se "melhor reta" já sugere algum
   critério, sem ainda ter dado nome a mínimos quadrados).

2. **Intuição — A Ideia Geométrica de Mínimos Quadrados** (~10 min) —
   sem matrizes ainda: resíduo $e_i=y_i-\hat y_i$, a ideia de "minimizar o
   total de erro ao quadrado", por que quadrado (penaliza desvios grandes
   mais que proporcionalmente, é diferenciável em toda parte, ao contrário
   do valor absoluto). Prepara o terreno para a formalização do Bloco 1.

3. **Bloco 1 — Formalização: RSS, Equações Normais e Projeção** (~25 min)
   — necessidade teórica → teoria formal do Outside-In. Notação matricial
   ($X$, $\beta$, $\text{RSS}(\beta)=\lVert y-X\beta\rVert^2$), derivação do
   gradiente e das equações normais, solução fechada
   $\hat\beta=(X^TX)^{-1}X^Ty$. Diagrama TikZ da geometria de projeção
   (PRML Fig. 3.2 / ESL Fig. 3.2, redesenhado). Exemplo numérico real:
   ajuste `MedInc`$\to$`MedHouseVal` no *California Housing* completo
   ($N=16\,640$), $\hat\beta=(0{,}4707,\,0{,}4076)$. Termina com Pausa
   Ativa 2 (projeção/equações normais).

4. **Bloco 2 — O Modelo de Ruído Gaussiano Homocedástico** (~25 min) —
   anunciar as premissas explicitamente antes de usá-las: $Y\mid
   X=x\sim\mathcal N(\beta^Tx,\sigma^2)$, $\sigma^2$ constante (não
   depende de $x$ — homocedástico), erros independentes entre observações.
   Construção passo a passo da verossimilhança conjunta (produto de
   densidades $\to$ log $\to$ soma), chegando à log-verossimilhança
   $\ell(\beta,\sigma^2)$. Contraste conceitual com heterocedasticidade
   (antecipando a Seção de Limitações). Termina com Pausa Ativa 3.

5. **Bloco 3 — O Teorema Central: OLS $=$ MLE Sob Normalidade** (~30 min)
   — o pagamento matemático da aula: isolar, na log-verossimilhança, o
   único termo que depende de $\beta$ (a soma de quadrados negativa),
   concluir que maximizar em $\beta$ $\equiv$ minimizar RSS $\equiv$
   $\hat\beta_{\text{MLE}}=\hat\beta_{\text{OLS}}$; depois maximizar em
   $\sigma^2$, obtendo $\hat\sigma^2_{\text{MLE}}=\text{RSS}/N$ (viesado
   para baixo — callback à Aula 3). Verificação numérica: `scipy.optimize`
   maximizando a log-verossimilhança sobre $(\beta_0,\beta_1,\log\sigma)$
   bate com a forma fechada a $10^{-8}$; grade de log-verossimilhança
   sobre $(\beta_0,\beta_1)$ confirma visualmente o máximo no ponto
   fechado. Termina com Pausa Ativa 4.

6. **Síntese e Limitações** (~10 min) — quarta fase do Outside-In: o que
   quebra se as premissas falharem. Achado real nos próprios dados:
   `MedHouseVal` é censurado em $5{,}00001$ ($4{,}49\%$ das observações no
   teto) e a variância dos resíduos cresce com `MedInc` (heterocedasticidade
   real, não hipotética: $\text{Var}(\text{resíduo})$ vai de $0{,}486$ no
   1º quartil de renda a $0{,}849$ no 3º) — ambos violam premissas do
   Bloco 2. Ponte para a Aula 7: trocar a Gaussiana por uma Bernoulli
   recupera a mesma estrutura (distribuição $\to$ verossimilhança $\to$
   decisão) para alvos binários, e a "soma de quadrados" vira
   "entropia cruzada" pela mesma lógica de hoje.

7. **Fechamento** (~10 min) — retomar as 4 perguntas do roteiro, uma
   frase cada; nomear o que fica em aberto (regularização/MAP na Aula 8,
   decomposição viés-variância na Aula 9).

**Exercícios:** 3 discursivas + 8 blocos de V/F (32 itens), cobrindo:
geometria/projeção, RSS/equações normais, premissas do modelo gaussiano,
construção da verossimilhança, o teorema central (OLS=MLE), viés do MLE de
$\sigma^2$, verificação numérica/otimização, e limitações
(heterocedasticidade/censura/não-linearidade).

## Fontes usadas — Aula 5

### Fonte 1: PRML, §3, p. 137 (introdução do capítulo)
**Uso pretendido:** definição do problema de regressão, usada na Abertura/
Intuição para situar o alvo contínuo $t$ (aqui $y$) e o vetor de entrada
$D$-dimensional.

**Trecho:**
> "The goal of regression is to predict the value of one or more continuous
> target variables t given the value of a D-dimensional vector x of input
> variables."

---

### Fonte 2: PRML, §3.1.1, p. 140
**Uso pretendido:** anúncio explícito das premissas do modelo de ruído
gaussiano (Bloco 2) — citado quase literalmente na estrutura de
"anunciar premissas antes de usá-las" do `../CLAUDE.md`.

**Trecho:**
> "As before, we assume that the target variable t is given by a
> deterministic function y(x, w) with additive Gaussian noise so that
> t = y(x, w) + ϵ where ϵ is a zero mean Gaussian random variable with
> precision (inverse variance) β. Thus we can write
> p(t|x, w, β) = N (t|y(x, w), β⁻¹)."

---

### Fonte 3: PRML, §3.1.1, pp. 141-142
**Uso pretendido:** construção passo a passo da verossimilhança conjunta
(produto de gaussianas $\to$ log-verossimilhança), e o resultado central —
maximizar a verossimilhança gaussiana $\equiv$ minimizar soma de
quadrados — usado no Bloco 3 como a prova principal da aula.

**Trecho:**
> "Now consider a data set of inputs X = {x1, . . . , xN} with
> corresponding target values t1, . . . , tN. [...] Making the assumption
> that these data points are drawn independently from the distribution
> (3.8), we obtain the following expression for the likelihood function,
> which is a function of the adjustable parameters w and β, in the form
> p(t|X, w, β) = ∏[n=1 to N] N(tn|w^T φ(xn), β⁻¹)."
>
> "Having written down the likelihood function, we can use maximum
> likelihood to determine w and β. Consider first the maximization with
> respect to w. [...] we see that maximization of the likelihood function
> under a conditional Gaussian noise distribution for a linear model is
> equivalent to minimizing a sum-of-squares error function given by
> ED(w)."
>
> "Setting this gradient to zero gives [...] Solving for w we obtain
> wML = (Φ^T Φ)^{−1} Φ^T t which are known as the normal equations for the
> least squares problem."

---

### Fonte 4: PRML, §3.1.2, p. 143
**Uso pretendido:** interpretação geométrica da solução de mínimos
quadrados como projeção ortogonal — base do diagrama TikZ do Bloco 1.

**Trecho:**
> "At this point, it is instructive to consider the geometrical
> interpretation of the least-squares solution. [...] Thus the
> least-squares solution for w corresponds to that choice of y that lies
> in subspace S that is closest to t. [...] we anticipate that this
> solution corresponds to the orthogonal projection of t onto the
> subspace S."

---

### Fonte 5: ESL, §3.2, p. 44
**Uso pretendido:** definição alternativa (notação $\beta$, RSS) do
critério de mínimos quadrados, usada no Bloco 1 junto com PRML para dar
duas notações equivalentes que o aluno vai encontrar na literatura.

**Trecho:**
> "The most popular estimation method is least squares, in which we pick
> the coefficients β = (β0, β1, . . . , βp)^T to minimize the residual
> sum of squares RSS(β) = ∑[i=1 to N](yi − f(xi))²."

---

### Fonte 6: ESL, §3.2, p. 45
**Uso pretendido:** derivação alternativa das equações normais via
diferenciação direta de RSS (complementa a derivação via gradiente da
log-verossimilhança do PRML) — usada no Bloco 1.

**Trecho:**
> "Differentiating with respect to β we obtain ∂RSS/∂β = −2X^T(y − Xβ)
> [...] Assuming (for the moment) that X has full column rank, and hence
> X^T X is positive definite, we set the first derivative to zero
> X^T(y − Xβ) = 0 to obtain the unique solution β̂ = (X^T X)^{−1} X^T y."

---

### Fonte 7: ESL, §3.2, p. 46
**Uso pretendido:** segunda formulação da geometria de projeção (espaço
$\mathbb R^N$, hat matrix), complementando a Fonte 4 (PRML) no diagrama
TikZ do Bloco 1.

**Trecho:**
> "The N-dimensional geometry of least squares regression with two
> predictors. The outcome vector y is orthogonally projected onto the
> hyperplane spanned by the input vectors x1 and x2. [...] This
> orthogonality is expressed in (3.5), and the resulting estimate ŷ is
> hence the orthogonal projection of y onto this subspace."

## Dataset escolhido e justificativa

A Revisão 1 usou *Pima Indians Diabetes* como fio condutor, mas seu alvo
(`y`, diabético/não) é binário — não serve para uma aula de regressão, que
precisa de um alvo genuinamente contínuo. Também não é pedagogicamente
natural forçar uma coluna do Pima (ex.: `Glucose` ou `BMI`) a virar alvo de
regressão só por continuidade de dataset: `Glucose` já foi usada há uma
aula como variável de entrada para um limiar de classificação (Revisão 1,
Bloco 1) — reciclá-la agora como *alvo* de regressão inverteria seu papel
sem nenhum ganho pedagógico, só confusão.

Optamos por **California Housing** (`gvlassis/california_housing`, tabela
curada do `../CLAUDE.md`), que já apareceu na Aula 3 (`MedInc`/`HouseAge`
como atributos de uma árvore de regressão) — portanto não é um dataset
novo para a disciplina, só um retorno com um alvo contínuo genuíno
(`MedHouseVal`, preço mediano de imóvel em US\$100 mil) e um encaixe
direto com "regressão linear" (é literalmente o exemplo canônico da
tabela para essa técnica). Usamos o conjunto de treino completo
($N=16\,640$, sem subamostragem — a regressão simples de 2 parâmetros não
exige reduzir o tamanho da amostra como as árvores/Naive Bayes de aulas
anteriores exigiram para visualização).
