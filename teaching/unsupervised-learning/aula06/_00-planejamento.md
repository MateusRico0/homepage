## Resumo — Aula 6

A Aula 5 fechou o assunto de variável latente **categórica** (o GMM) com
uma ferramenta geral (BIC/ELBO) para selecionar e ajustar esse tipo de
modelo. A Aula 6 muda de eixo: abre a **Parte 2** do curso (Redução de
Dimensionalidade e Auto-Supervisão) trocando a variável latente
categórica por uma variável latente **contínua** — em vez de "de qual
população este ponto veio?", a pergunta passa a ser "que posição, num
espaço de dimensão bem menor, resume este ponto sem perder o que
importa?". A aula constrói essa ideia em três camadas, cada uma
revisitando o mesmo objeto (o subespaço de maior variância dos dados)
de um ângulo diferente: (1) a Análise de Componentes Principais (PCA)
clássica, puramente algébrica, via decomposição espectral da matriz de
covariância amostral, apresentada nas suas duas formulações equivalentes
(máxima variância projetada; mínimo erro de reconstrução); (2) a PCA
Probabilística (PPCA), um modelo gerador de variável latente
linear-Gaussiana (no mesmo espírito do GMM da Aula 4, mas com $z$
contínuo em vez de categórico), cujo ajuste por máxima verossimilhança
recupera a PCA clássica como caso particular; (3) o autoencoder linear
(rede neural rasa, ativação linear, gargalo de $M<D$ unidades), provado
equivalente ao mesmo subespaço de PCA.

**Objetivos de aprendizagem:** (1) derivar a PCA por máxima variância e
por mínimo erro de reconstrução, e demonstrar a equivalência das duas
formulações; (2) formular a PPCA como modelo gerador linear-Gaussiano e
derivar sua solução de máxima verossimilhança; (3) mostrar que a PCA
clássica é o caso-limite $\sigma^2\to0$ da PPCA; (4) provar (por redução
ao problema de mínimo erro já demonstrado) que um autoencoder linear
compartilha o mesmo subespaço de projeção da PCA.

**Pré-requisitos** (checados contra o dicionário de notações e o resumo
da Aula 5 em `../_progresso.md`): nenhum pré-requisito direto do GMM/EM
é reaproveitado algebricamente aqui (a variável latente muda de natureza
por completo) — mas a **estrutura** de raciocínio "modelo gerador com
variável latente $\to$ ajuste por máxima verossimilhança" já é familiar
desde a Aula 4, e é reaproveitada explicitamente na formulação da PPCA.
Pré-requisito de álgebra linear (autovalores/autovetores de matriz
simétrica, decomposição espectral) — não coberto nesta disciplina, mas
coberto na disciplina irmã `optimization-linear-algebra` (Aula 4:
Teorema Espectral Real) — citado como pré-requisito, não redemonstrado
aqui.

**Estratégia Pedagógica:** Estratégia B (*Inside-Out com Problema-Fio*)
— o `CLAUDE.md` lista explicitamente "SVD/Decomposição" como caso de uso
da Estratégia B, e a PCA é, na sua essência, exatamente isso: uma técnica
de decomposição algébrica (autovalores/autovetores da matriz de
covariância). O problema-fio geométrico ("como resumir um paciente de
$30$ atributos em $2$ números sem perder o que importa clinicamente?")
organiza a progressão Mecanismo (decomposição espectral) $\to$
Diagnóstico Teórico (o que a PPCA revela sobre esse mecanismo — que ele
é, na verdade, uma solução de máxima verossimilhança de um modelo
gerador, e que a mesma solução emerge de uma rede neural rasa) $\to$
Ponte (limitação: só captura estrutura **linear** — motivando a extensão
não linear da Aula 7).

## Plano de aula — Aula 6 (carga horária: ~120 min)

1. **Abertura — Revisão e Introdução** (~12 min) — revisão cuidadosa do
   que a Aula 5 deixou pronto (BIC, ELBO, EM como subida de
   coordenadas); Ideia Central (Ausubel): a mudança de eixo, variável
   latente categórica $\to$ contínua, anunciada no fechamento da Aula 5;
   roteiro explícito das 4 perguntas; problema motivador (o Breast
   Cancer Wisconsin tem $30$ atributos — impossível visualizar
   diretamente; como resumir cada paciente em $2$ números escolhidos
   "corretamente", não arbitrariamente?); Pausa Ativa 1.
2. **Problema-Fio: Qual Direção Resume Melhor?** (~10 min) — Inside-Out:
   ilustração geométrica 2D (mesmo par `radius_worst`/`concave
   points_worst` das Aulas 3–5, ambos padronizados), comparando a
   variância dos dados projetados em duas direções candidatas (o eixo
   bruto de um atributo vs. a direção a $45°$) — sem fórmula ainda, só a
   pergunta geométrica que o Bloco 3 formaliza.
3. **Mecanismo I: Formulação de Máxima Variância** (~15 min) —
   desenvolvimento *principled*: premissas explícitas, Lagrangeano,
   $Su_1=\lambda_1u_1$ — a direção ótima é o autovetor de maior
   autovalor de $S$. Generalização para $M$ componentes por indução.
   Aplicação ao Breast Cancer Wisconsin completo ($D=30$): autovalores,
   variância explicada. Pausa Ativa 2.
4. **Mecanismo II: Formulação de Erro Mínimo, e Sua Equivalência com a Anterior** (~15 min) —
   segunda derivação (minimizar $J=\frac1N\sum_n\|\mathbf{x}_n-
   \tilde{\mathbf{x}}_n\|^2$), chegando à mesma equação de autovetores —
   Teorema de equivalência das duas formulações. Projeção real nos 2
   primeiros componentes, mostrando que a estrutura benigno/maligno
   (nunca usada no ajuste) emerge visualmente. Pausa Ativa 3.
5. **Diagnóstico Teórico: PCA Probabilística (PPCA)** (~20 min) —
   formulação do modelo gerador linear-Gaussiano
   ($p(\mathbf{z})=\mathcal{N}(\mathbf{0},I)$,
   $p(\mathbf{x}\mid\mathbf{z})=\mathcal{N}(\mathbf{Wz}+\boldsymbol\mu,
   \sigma^2I)$), no mesmo espírito da variável latente da Aula 4;
   solução de máxima verossimilhança
   ($\mathbf{W}_{\mathrm{ML}}=\mathbf{U}_M(\mathbf{L}_M-\sigma^2I)^{1/2}
   \mathbf{R}$); verificação numérica de que $\sigma^2_{\mathrm{ML}}$ é
   a média dos autovalores descartados; caso-limite $\sigma^2\to0$
   recupera a projeção ortogonal da PCA clássica. Pausa Ativa 4.
6. **O Autoencoder Linear Compartilha o Mesmo Subespaço** (~15 min) —
   Teorema (Bourlard & Kamp, 1988; Baldi & Hornik, 1989, via DLFC
   §19.1.1), demonstrado por redução ao problema de erro mínimo já
   provado no Bloco 4 (o objetivo de reconstrução do autoencoder linear
   é, literalmente, o mesmo $J$); verificação numérica (autoencoder
   linear via `MLPRegressor(activation="identity")`) comparando o erro
   de reconstrução obtido com o ótimo teórico da PCA. Pausa Ativa 5.
7. **Síntese, Fechamento e Ponte para a Aula 7** (~10 min) — as quatro
   respostas convergem para o mesmo subespaço, vistas de quatro ângulos
   (geométrico, algébrico, probabilístico, neural); retomar as perguntas
   da Abertura; nomear a limitação central (só estrutura **linear**) —
   ponte explícita para a Aula 7 (autoencoders não lineares e VAE,
   retomando o ELBO da Aula 5 no cenário não linear).

**Exercícios finais:** 3 discursivas + 6 blocos de V/F (24 itens) —
densidade um pouco menor que a Aula 5 (28 itens) porque esta aula, apesar
de densa em derivações, tem menos blocos de conteúdo numérico-aplicado
distintos (a mesma ideia — o subespaço de maior variância — é revisitada
sob quatro ângulos, não quatro tópicos independentes); 6 blocos cobrem:
formulação de máxima variância; formulação de erro mínimo e sua
equivalência; PPCA como modelo gerador; MLE da PPCA e o caso-limite
clássico; o autoencoder linear; síntese/limitações e ponte para a
Aula 7.

## Fontes usadas — Aula 6

### Fonte 1: PRML, §12.1.1 "Maximum variance formulation", pp. 561–562 (PDF pp. 581–582, offset +20 confirmado nesta sessão comparando o cabeçalho de página)

**Uso pretendido:** derivação da PCA por máxima variância projetada
(eq. 12.1–12.6), base do Bloco 3.

**Trecho (p. 561):**
> "Consider a data set of observations {xn} where n = 1, . . . , N, and xn
> is a Euclidean variable with dimensionality D. Our goal is to project
> the data onto a space having dimensionality M < D while maximizing the
> variance of the projected data. [...]
> To begin with, consider the projection onto a one-dimensional space
> (M = 1). We can define the direction of this space using a
> D-dimensional vector u1, which for convenience (and without loss of
> generality) we shall choose to be a unit vector so that u1^T u1 = 1
> [...] The mean of the projected data is u1^T x̄ where x̄ is the sample
> set mean [...] and the variance of the projected data is given by
>
> (1/N) Σn {u1^T xn − u1^T x̄}^2 = u1^T S u1                              (12.2)
>
> where S is the data covariance matrix defined by
>
> S = (1/N) Σn (xn − x̄)(xn − x̄)^T.                                       (12.3)"

**Trecho (p. 562):**
> "We now maximize the projected variance u1^T S u1 with respect to u1.
> [...] To enforce this constraint, we introduce a Lagrange multiplier
> that we shall denote by λ1, and then make an unconstrained maximization
> of
>
> u1^T S u1 + λ1 (1 − u1^T u1).                                          (12.4)
>
> By setting the derivative with respect to u1 equal to zero, we see that
> this will have a stationary point when
>
> S u1 = λ1 u1                                                          (12.5)
>
> which says that u1 must be an eigenvector of S. [...] the variance will
> be a maximum when we set u1 equal to the eigenvector having the largest
> eigenvalue λ1. This eigenvector is known as the first principal
> component."

---

### Fonte 2: PRML, §12.1.2 "Minimum-error formulation", pp. 563–565 (PDF pp. 583–585)

**Uso pretendido:** segunda derivação (erro de reconstrução), eq.
12.11–12.18, base do Bloco 4 e da ponte ao autoencoder linear (Bloco 6).

**Trecho (p. 564):**
> "As our distortion measure, we shall use the squared distance between
> the original data point xn and its approximation x̃n, averaged over the
> data set, so that our goal is to minimize
>
> J = (1/N) Σn ‖xn − x̃n‖^2.                                              (12.11)"

**Trecho (p. 565):**
> "The general solution to the minimization of J for arbitrary D and
> arbitrary M < D is obtained by choosing the {ui} to be eigenvectors of
> the covariance matrix given by
>
> S ui = λi ui,                                                          (12.17)
>
> [...] and hence the eigenvectors defining the principal subspace are
> those corresponding to the M largest eigenvalues."

---

### Fonte 3: PRML, §12.2 "Probabilistic PCA", pp. 570–576 (PDF pp. 590–596)

**Uso pretendido:** formulação do modelo gerador linear-Gaussiano
(eq. 12.31–12.33), covariância marginal (eq. 12.35–12.36), solução de
máxima verossimilhança (eq. 12.43–12.47), e o caso-limite $\sigma^2\to0$
recuperando a PCA clássica (eq. 12.48–12.50) — base do Bloco 5.

**Trecho (p. 571):**
> "We can formulate probabilistic PCA by first introducing an explicit
> latent variable z corresponding to the principal-component subspace.
> Next we define a Gaussian prior distribution p(z) over the latent
> variable, together with a Gaussian conditional distribution p(x|z) for
> the observed variable x conditioned on the value of the latent
> variable. Specifically, the prior distribution over z is given by a
> zero-mean unit-covariance Gaussian
>
> p(z) = N(z|0, I).                                                      (12.31)
>
> Similarly, the conditional distribution of the observed variable x,
> conditioned on the value of the latent variable z, is again Gaussian,
> of the form
>
> p(x|z) = N(x|Wz + μ, σ^2 I)                                            (12.32)
>
> in which the mean of x is a general linear function of z governed by
> the D × M matrix W and the D-dimensional vector μ."

**Trecho (p. 573):**
> "where the D × D covariance matrix C is defined by
>
> C = WW^T + σ^2 I.                                                      (12.36)"

**Trecho (p. 574, eq. 12.45):**
> "W_ML = U_M (L_M − σ^2 I)^{1/2} R
>
> where U_M is a D × M matrix whose columns are given by any subset (of
> size M) of the eigenvectors of the data covariance matrix S, the M × M
> diagonal matrix L_M has elements given by the corresponding
> eigenvalues, and R is an arbitrary M × M orthogonal matrix."

**Trecho (p. 575, eq. 12.46):**
> "σ_ML^2 = (1/(D − M)) Σ_{i=M+1}^{D} λi
>
> so that σ_ML^2 is the average variance associated with the discarded
> dimensions."

**Trecho (p. 576, sobre o limite $\sigma^2\to0$):**
> "If we take the limit σ^2 → 0, then the posterior mean reduces to
>
> (W_ML^T W_ML)^{−1} W_ML^T (x − x̄)                                     (12.50)
>
> which represents an orthogonal projection of the data point onto the
> latent space, and so we recover the standard PCA model."

---

### Fonte 4: DLFC (Bishop & Bishop, 2024), §19.1.1 "Linear autoencoders", pp. 564–565 (PDF pp. 575–576, offset **−12** confirmado nesta sessão — este PDF não é digitalizado, a paginação impressa fica **atrás** da paginação do arquivo, ao contrário do PRML)

**Uso pretendido:** enunciado do teorema de equivalência
autoencoder-linear/PCA (citando Bourlard & Kamp, 1988; Baldi & Hornik,
1989), base do Bloco 6 — a prova em si é reconstruída nesta aula por
redução ao problema de erro mínimo já demonstrado (Fonte 2), não copiada
do livro (o DLFC enuncia o resultado sem demonstrá-lo: "it can be shown
that...").

**Trecho (p. 564):**
> "Consider first a multilayer perceptron of the form shown in Figure
> 19.1, having D inputs, D output units, and M hidden units, with M < D.
> The targets used to train the network are simply the input vectors
> themselves, so that the network attempts to map each input vector onto
> itself. [...] We therefore determine the network parameters w by
> minimizing an error function that captures the degree of mismatch
> between the input vectors and their reconstructions. In particular, we
> choose a sum-of-squares error of the form
>
> E(w) = (1/2) Σ_{n=1}^{N} ‖y(xn, w) − xn‖^2.                            (19.1)
>
> If the hidden units have linear activation functions, then it can be
> shown that the error function has a unique global minimum and that at
> this minimum the network..."

**Trecho (p. 565):**
> "...performs a projection onto the M-dimensional subspace that is
> spanned by the first M principal components of the data (Bourlard and
> Kamp, 1988; Baldi and Hornik, 1989). Thus, the vectors of weights that
> lead into the hidden units in Figure 19.1 form a basis set that spans
> the principal subspace. Note, however, that these vectors need not be
> orthogonal or normalized."

---

**Números verificados nesta sessão, por script independente**
(reproduzíveis a partir do código do `.qmd`, mesma metodologia):

- Ilustração 2D (`radius_worst`/`concave points_worst` padronizados,
  mesmo par das Aulas 3–5): os dois atributos têm correlação positiva
  forte o bastante para que o autovetor principal $u_1$ fique
  exatamente a $45°$ do eixo bruto, com variância projetada
  $\lambda_1=1{,}7874$ (contra variância $1{,}0$ ao longo de qualquer
  eixo bruto isolado) e $\lambda_2=0{,}2126$ na direção ortogonal.
- PCA completa no Breast Cancer Wisconsin ($D=30$, padronizado): 5
  maiores autovalores $13{,}2816$, $5{,}6914$, $2{,}8179$, $1{,}9806$,
  $1{,}6487$; variância explicada pelos 2 primeiros componentes
  $\approx63{,}24\%$ ($44{,}27\%+18{,}97\%$).
- PPCA ($M=2$): $\sigma^2_{\mathrm{ML}}=0{,}39382$, confirmado
  numericamente igual à média dos $28$ autovalores descartados;
  verificado que $\mathbf{v}^T\mathbf{C}\mathbf{v}=\lambda_1$ para
  $\mathbf{v}=u_1$ e $=\sigma^2_{\mathrm{ML}}$ para um autovetor
  descartado, exatamente como a eq. 12.36 prevê.
- Projeção real nos 2 primeiros componentes principais (rótulo
  `diagnosis` nunca usado no ajuste): um único limiar ao longo do
  primeiro componente já separa benigno/maligno com $92{,}1\%$ de
  acurácia — estrutura clínica real emergindo de um critério puramente
  de variância.
- Autoencoder linear (`MLPRegressor(activation="identity")`, $M=2$):
  erro quadrático médio de reconstrução $0{,}367575$ contra o ótimo
  teórico da PCA, $0{,}367568$ — coincidência a $5$ algarismos
  significativos. Os vetores de peso do autoencoder **não** ficaram
  alinhados (nem ortonormais) com os autovetores da PCA (cossenos dos
  ângulos principais $\approx0{,}98$ e $\approx0{,}93$, não exatamente
  $1$) — consistente com a observação do próprio DLFC de que "esses
  vetores não precisam ser ortogonais nem normalizados": o teorema
  garante o mesmo **subespaço ótimo** (mesmo erro de reconstrução), não
  que o otimizador numérico encontre a mesma base ortonormal; o pequeno
  desvio residual nos ângulos principais é atribuído à convergência
  finita do otimizador (Adam/L-BFGS), não a uma falha do teorema —
  sinalizado explicitamente como tal na aula.
