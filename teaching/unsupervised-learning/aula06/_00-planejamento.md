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
de um ângulo diferente. Abre com o autoencoder linear (rede rasa,
ativação linear, gargalo de $M<D$ unidades), que torna concreto o
espaço latente: o código são coordenadas num plano de dimensão $M$
dentro do espaço dos dados, e os dados só determinam o plano, não os
eixos (invariância por $\mathbf{G}$ invertível). A pergunta "que plano
a rede aprende?" é então respondida por: (1) a Análise de Componentes Principais (PCA)
clássica, puramente algébrica, via decomposição espectral da matriz de
covariância amostral, apresentada nas suas duas formulações equivalentes
(primeiro mínimo erro de reconstrução, que é o objetivo do autoencoder;
depois máxima variância retida, ligadas por Pitágoras), o que fecha a
prova de que o autoencoder linear aprende o subespaço de PCA; (2) a PCA
Probabilística (PPCA), um modelo gerador de variável latente
linear-Gaussiana (no mesmo espírito do GMM da Aula 4, mas com $z$
contínuo em vez de categórico), cujo ajuste por máxima verossimilhança
recupera a PCA clássica como caso particular.

**Objetivos de aprendizagem:** (0) interpretar o espaço latente de um
autoencoder linear como sistema de coordenadas de um plano e reconhecer
o que é identificável (o plano) e o que não é (os eixos); (1) derivar a PCA por máxima variância e
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
   latente categórica $\to$ contínua; roteiro das 4 perguntas; problema
   motivador (mapa de correlação dos $30$ atributos: $44$ de $435$ pares
   com $|r|>0{,}8$ — quantos números bastam, e quais?); Pausa Ativa 1.
2. **Problema-Fio: Guardar Um Número, Reconstruir Dois** (~10 min) —
   par `radius_worst`/`concave points_worst`: guardar a posição ao longo
   de uma reta e reconstruir pelo ponto da reta; eixo bruto (retida
   $1{,}00$, erro $1{,}00$) vs. $45°$ (retida $1{,}79$, erro $0{,}21$).
   Motiva a aula inteira: o número guardado é um código latente
   (autoencoder), qual reta erra menos (Mecanismo I), retida $+$ erro
   $=2{,}00$ (Mecanismo II), o espalhamento em torno da reta como ruído
   (PPCA, $\sigma^2_{\mathrm{ML}}=\lambda_2=0{,}21$).
3. **O Autoencoder Linear: Comprimir, Codificar, Reconstruir** (~18 min)
   — definição (DLFC §19.1.1); codificador $\mathbf{V}$, código latente
   $\mathbf{z}_n=\mathbf{V}\mathbf{x}_n$, decodificador $\mathbf{W}$;
   reconstruções no plano $\mathcal{C}(\mathbf{W})$, código $=$
   coordenadas, colunas de $\mathbf{W}$ $=$ eixos; invariância
   $(\mathbf{G}\mathbf{V},\mathbf{W}\mathbf{G}^{-1})$: os dados fixam o
   plano, não os eixos; Teorema (Bourlard & Kamp; Baldi & Hornik)
   só anunciado como pergunta ("qual plano?"), sem citar PCA ainda;
   espaço latente do autoencoder treinado no Breast Cancer Wisconsin
   (pesos com cosseno $\approx-0{,}58$). Pausa Ativa 2 (espaço latente: o
   que os dados determinam).
4. **Mecanismo I: O Melhor Plano Pelo Erro de Reconstrução** (~15 min) —
   a partir do autoencoder: Suposição 1, pesos amarrados
   ($\mathbf{W}=\mathbf{U}$, $\mathbf{V}=\mathbf{U}^T$); Suposição 2,
   $\mathbf{U}$ com colunas ortonormais (base do plano); completar a base
   de $\mathbb{R}^D$ e reconstrução geral com $z_{ni}$ e $b_i$ (PRML
   §12.1.2). Passo 1 por Pitágoras na base: $z_{ni}=\mathbf{x}_n^T\mathbf{u}_i$
   (o codificador amarrado era ótimo), $b_i=\bar{\mathbf{x}}^T\mathbf{u}_i$,
   erro ortogonal; Passo 2, $J=\sum_{i>M}\mathbf{u}_i^T\mathbf{S}\mathbf{u}_i$;
   Passo 3, $J=\mathrm{tr}(\mathbf{S})-$ variância retida.
5. **Mecanismo II: O Melhor Plano Pela Variância Retida** (~15 min) —
   PRML §12.1.1: Lagrangeano, $\mathbf{S}\mathbf{u}_1=\lambda_1\mathbf{u}_1$;
   $\mathbf{S}$ como soma de posto 1 e indução em $M$ (ressalva Ky Fan);
   autovalores no Breast Cancer Wisconsin; Teorema do erro mínimo como
   junção ($J^\star=\sum_{i>M}\lambda_i$). Pausa Ativa 3.
6. **De Volta ao Autoencoder: a Prova** (~10 min) — Teorema (Bourlard &
   Kamp; Baldi & Hornik) enunciado agora que os componentes principais
   existem; prova por redução; ressalva do DLFC sobre não linearidade
   rasa e Pausa Ativa 4 (ativação não linear). Só nas notas: verificação
   numérica (erro $0{,}367568$ vs. $0{,}367575$; ângulos principais;
   $R^2>0{,}99999$ entre códigos), eixos canônicos da PCA e a projeção com
   os $92{,}1\%$ sem rótulo.
7. **PCA Como Gaussiana de Posto Reduzido (PPCA)** (~12 min) — Gaussiana
   com covariância livre ($\mathbf{C}=\mathbf{S}$, $465$ números) vs.
   covariância de posto $M$ mais ruído isotrópico
   ($\mathbf{WW}^T+\sigma^2\mathbf{I}$); modelo gerador (o decodificador
   com prior e ruído); resultado de Tipping & Bishop citado, lido como
   $\mathbf{C}_{\mathrm{ML}}=\sum_{i\le M}\lambda_i\mathbf{u}_i\mathbf{u}_i^T+\sigma^2_{\mathrm{ML}}\sum_{i>M}\mathbf{u}_i\mathbf{u}_i^T$
   (copia $\mathbf{S}$ em $M$ direções, achata as outras); figura dos
   espectros de $\mathbf{S}$ e $\mathbf{C}_{\mathrm{ML}}$ ($60$ números);
   $\sigma^2\to0$: Gaussiana de posto exatamente $M$ $=$ PCA. Pausa Ativa 5.
8. **Síntese, Fechamento e Ponte para a Aula 7** (~10 min) — quatro
   ângulos (neural, algébrico, geométrico, probabilístico); retomar as
   perguntas; limitação linear; ponte para autoencoders profundos e VAE.

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
(eq. 12.1–12.6), base do Mecanismo II.

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
12.11–12.18, base do Mecanismo I e da prova do autoencoder linear.

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
recuperando a PCA clássica (eq. 12.48–12.50) — base do bloco da PPCA.

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
1989), base do bloco do autoencoder — a prova em si é reconstruída nesta aula por
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
