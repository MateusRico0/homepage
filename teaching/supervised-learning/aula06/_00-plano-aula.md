# Resumo — Aula 6

Segunda aula da "Parte 2: A História Linear Paramétrica". Enquanto a Aula 5
introduziu a predição linear contínua sob ruído gaussiano ($Y\mid X\sim\mathcal N(\mathbf{w}^T\mathbf{x},\sigma^2)$),
a Aula 6 estende a mesma lógica de Máxima Verossimilhança para classificação binária paramétrica:
o modelo de **Regressão Logística** e o arcabouço de **Modelos Lineares Generalizados (GLMs)**.

O ponto de partida é o contraste com a Aula 5: um hiperplano linear $\mathbf{w}^T\mathbf{x}$ mapeia
$\mathbb R^D \to \mathbb R$, mas para classificar precisamos modelar a probabilidade condicional de classe
$p(C_1\mid\mathbf{x}) \in [0, 1]$. Assumindo que a resposta $y_n \in \{0, 1\}$ segue uma distribuição
de Bernoulli $Y\mid X=\mathbf{x} \sim \text{Bernoulli}(\mu(\mathbf{x}))$, a função de ligação canônica (*logit*)
$\ln\frac{\mu}{1-\mu} = \mathbf{w}^T\mathbf{x}$ induz a função sigmoide logística $\mu(\mathbf{x}) = \sigma(\mathbf{w}^T\mathbf{x}) = \frac{1}{1 + e^{-\mathbf{w}^T\mathbf{x}}}$.

Ao construir a verossimilhança conjunta sob observações independentes e tomar o logaritmo negativo,
a função de perda resultante é a **Entropia Cruzada Binária** (cross-entropy error).
Diferente da regressão linear gaussiana (que possui solução fechada via equações normais OLS),
a não-linearidade da sigmoide impede uma solução analítica para $\nabla E(\mathbf{w}) = \mathbf{0}$.
Entretanto, o gradiente preserva a mesma forma intuitiva "erro $\times$ vetor de atributos" da regressão linear:
$\nabla E(\mathbf{w}) = \sum_n (\mu_n - y_n)\mathbf{x}_n = X^T(\boldsymbol\mu - \mathbf{y})$.
A Hessiana $H = X^T R X$ é estritamente semidefinida positiva (com $R_{nn} = \mu_n(1-\mu_n) > 0$), garantindo
que a superfície de perda é estritamente convexa e possui um único mínimo global, resolvido de maneira
elegante pelo algoritmo **IRLS (Iteratively Reweighted Least Squares)** via Newton-Raphson.

Por fim, o fechamento da aula enquadra a regressão linear e a regressão logística como duas instâncias
do mesmo arcabouço unificador: a **Família Exponencial** e os **Modelos Lineares Generalizados (GLMs)**
(Nelder & Wedderburn, 1972; PRML §4.3.6), onde a função de ligação canônica garante sempre que
o gradiente da perda seja o resíduo multiplicado pela base. Discute-se também a separabilidade perfeita
(onde o MLE diverge para $\lVert\mathbf{w}\rVert \to \infty$), servindo de ponte direta para a regularização
(Ridge/Lasso e MAP) da Aula 7.

**Pré-requisitos** (conferidos contra `_progresso.md`):
- Definição formal de Máxima Verossimilhança (Aula 3 e Aula 5);
- OLS como MLE gaussiano (Aula 5);
- Teoria da decisão e probabilidade a posteriori $p(C_1\mid\mathbf{x})$ (Aulas 1, 2 e Revisão 1);
- Entropia e teoria da informação (Aula 3);
- Notação de gradiente e hessiana.

**Estratégia Pedagógica:** Estratégia A (*Outside-In*) — Regressão Logística é o modelo paramétrico de
classificação por excelência. A aula abre com a provocação prática: "o que acontece se tentarmos usar
a regressão linear da Aula 5 diretamente para classificar rótulos 0 e 1?". Mostra-se o fracasso geométrico
e probabilístico da reta (previsões $<0$ ou $>1$, sensibilidade extrema a outliers), motivando a necessidade
de esmagar $\mathbb R$ em $[0, 1]$ via sigmoide. O rigor matemático desenvolve passo a passo a verossimilhança
de Bernoulli, a entropia cruzada, a derivação do gradiente e a convergência do IRLS sobre o dataset real
**Adult Census Income** (`scikit-learn/adult-census-income`), terminando com a síntese conceitual via GLM.

---

## Plano de aula — Aula 6 (carga horária: ~130min)

1. **Abertura e Revisão** (~15 min)
   - Revisão cuidadosa da Aula 5: regressão linear, ruído gaussiano homocedástico $Y\mid X\sim\mathcal N(\mathbf{w}^Tx, \sigma^2)$, e a identidade $\hat\beta_{\text{OLS}} = \hat\beta_{\text{MLE}}$.
   - Problema motivador: classificação de renda (Adult Census Income, $>50\text{K}$). Por que não usar regressão linear ordinária diretamente em $y \in \{0, 1\}$?
   - Roteiro explícito de 4 perguntas que a aula responderá.
   - **Pausa Ativa 1:** Pergunta provocadora e V/F sobre as falhas da regressão linear para classificação de probabilidades.

2. **Intuição — A Transformação Sigmoide e a Razão de Chances (*Odds*)** (~15 min)
   - Modelo mental: do espaço não limitado $\mathbf{w}^T\mathbf{x} \in (-\infty, +\infty)$ para a probabilidade $\mu \in (0, 1)$.
   - A razão de chances (*odds ratio*): $\frac{p}{1-p}$. O logaritmo das chances (*logit*) como a ponte linear natural.
   - Propriedades fundamentais da sigmoide logística $\sigma(a) = \frac{1}{1 + e^{-a}}$: simetria $\sigma(-a) = 1 - \sigma(a)$ e a elegante derivada $\sigma'(a) = \sigma(a)(1 - \sigma(a))$.
   - O hiperplano de decisão $\mathbf{w}^T\mathbf{x} = 0 \iff p = 0{,}5$.

3. **Bloco 1 — A Verossimilhança de Bernoulli e a Entropia Cruzada** (~25 min)
   - Premissas explícitas: rótulos binários $y_n \in \{0, 1\}$, variáveis independentes condicionadas a $\mathbf{x}_n$, $Y_n\mid\mathbf{x}_n \sim \text{Bernoulli}(\mu_n)$.
   - Densidade de Bernoulli escrita na forma compacta: $p(y_n\mid\mathbf{w}) = \mu_n^{y_n}(1 - \mu_n)^{1 - y_n}$.
   - Verossimilhança conjunta: produto sobre as $N$ observações.
   - A perda de Entropia Cruzada Negativa (NLL): $E(\mathbf{w}) = -\sum_{n=1}^N [y_n \ln \mu_n + (1 - y_n)\ln(1 - \mu_n)]$.
   - Conexão formal com a Teoria da Informação (Aula 3): por que chamamos de entropia cruzada?
   - **Pausa Ativa 2:** Pergunta provocadora e V/F sobre a construção da verossimilhança de Bernoulli e a perda logarítmica.

4. **Bloco 2 — Otimização: Gradiente, Convexidade e IRLS** (~30 min)
   - O gradiente passo a passo: usando a regra da cadeia e o cancelamento da derivada da sigmoide, chega-se a $\nabla E(\mathbf{w}) = \sum_n (\mu_n - y_n)\mathbf{x}_n = X^T(\boldsymbol\mu - \mathbf{y})$.
   - Comparação formal com o gradiente da regressão linear da Aula 5: mesma estrutura "erro $\times$ atributo".
   - Ausência de solução fechada: por que $\nabla E(\mathbf{w}) = \mathbf{0}$ é um sistema transcendental não-linear.
   - A matriz Hessiana $H = \nabla^2 E(\mathbf{w}) = X^T R X$, onde $R = \text{diag}(\mu_n(1-\mu_n))$. Prova de estrita convexidade.
   - O método de Newton-Raphson e a reinterpretação como Mínimos Quadrados Ponderados Iterativos (IRLS).
   - Demonstração prática e verificação numérica no dataset Adult Census Income: convergência quadrática rápida (6 iterações).
   - **Pausa Ativa 3:** Pergunta provocadora e V/F sobre otimização convexa, Hessiana e o algoritmo IRLS.

5. **Bloco 3 — O Arcabouço dos Modelos Lineares Generalizados (GLMs)** (~25 min)
   - A Família Exponencial unificadora: $p(y\mid \eta) = h(y)g(\eta)\exp(\eta y)$.
   - Caso Gaussiano com variância fixa $\to$ Regressão Linear (função de ligação identidade $\eta = \mu$).
   - Caso Bernoulli $\to$ Regressão Logística (função de ligação logit $\eta = \ln\frac{\mu}{1-\mu}$).
   - O teorema da ligação canônica (PRML §4.3.6): quando o parâmetro natural é a combinação linear dos atributos, o gradiente da log-verossimilhança é sempre $X^T(\boldsymbol\mu - \mathbf{y})$.
   - Generalização multiclasse: a função Softmax como ligação canônica da distribuição Categórica/Multinomial.
   - **Pausa Ativa 4:** Pergunta provocadora e V/F sobre a Família Exponencial e GLMs.

6. **Síntese, Limitações e Fechamento** (~20 min)
   - A patologia da separabilidade linear perfeita: quando as classes são perfeitamente separáveis, $\lVert\mathbf{w}\rVert \to \infty$ e as probabilidades colapsam para 0 ou 1.
   - A necessidade de regularização: ponte para a Aula 7 (Ridge, Lasso e MAP).
   - Retomada das 4 perguntas de abertura respondidas em uma frase cada.
   - **Pausa Ativa 5:** Pergunta provocadora e V/F sobre separabilidade perfeita e transição para regularização.
   - Direcionamento para `exercicios.qmd` e `soluções.qmd`.

---

## Fontes usadas — Aula 6

### Fonte 1: PRML (Bishop, 2006), §4.3.1–§4.3.2, pp. 204–207
**Uso pretendido:** Definição da regressão logística discriminativa, função sigmoide, verossimilhança de Bernoulli, função de erro cross-entropy e derivação analítica do gradiente.

**Trechos literais:**
> "For a data set $\{\phi_n, t_n\}$, where $t_n \in \{0, 1\}$ and $\phi_n = \phi(\mathbf{x}_n)$, with $n = 1, \ldots, N$, the likelihood function can be written
> $$p(\mathbf{t}|\mathbf{w}) = \prod_{n=1}^N y_n^{t_n} \{1 - y_n\}^{1 - t_n}$$
> where $\mathbf{t} = (t_1, \ldots, t_N)^T$ and $y_n = p(C_1|\phi_n)$. As usual, we can define an error function by taking the negative logarithm of the likelihood, which gives the cross-entropy error function in the form
> $$E(\mathbf{w}) = -\ln p(\mathbf{t}|\mathbf{w}) = -\sum_{n=1}^N \{t_n \ln y_n + (1 - t_n)\ln(1 - y_n)\}$$
> where $y_n = \sigma(a_n)$ and $a_n = \mathbf{w}^T\phi_n$." (PRML, p. 206)

> "Taking the gradient of the error function with respect to $\mathbf{w}$, we obtain
> $$\nabla E(\mathbf{w}) = \sum_{n=1}^N (y_n - t_n)\phi_n$$
> ... Furthermore, comparison with (3.13) shows that this takes precisely the same form as the gradient of the sum-of-squares error function for the linear regression model." (PRML, p. 206)

---

### Fonte 2: PRML (Bishop, 2006), §4.3.3, pp. 207–209
**Uso pretendido:** Algoritmo Newton-Raphson, matriz Hessiana, curvatura convexa e formulação de Iterative Reweighted Least Squares (IRLS).

**Trechos literais:**
> "The Newton-Raphson update, for minimizing a function $E(\mathbf{w})$, takes the form
> $$\mathbf{w}^{(\text{new})} = \mathbf{w}^{(\text{old})} - \mathbf{H}^{-1}\nabla E(\mathbf{w})$$
> where $\mathbf{H}$ is the Hessian matrix whose elements comprise the second derivatives of $E(\mathbf{w})$ with respect to the components of $\mathbf{w}$." (PRML, p. 207)

> "The Hessian matrix is given by
> $$\mathbf{H} = \nabla\nabla E(\mathbf{w}) = \sum_{n=1}^N y_n (1 - y_n)\phi_n \phi_n^T = \boldsymbol\Phi^T \mathbf{R} \boldsymbol\Phi$$
> where we have introduced the $N \times N$ diagonal matrix $\mathbf{R}$ with elements $R_{nn} = y_n (1 - y_n)$." (PRML, p. 207)

---

### Fonte 3: PRML (Bishop, 2006), §4.3.2, p. 206–207 & §4.3.6, pp. 212–213
**Uso pretendido:** Separação linear perfeita (overfitting do MLE) e o arcabouço unificador de Modelos Lineares Generalizados (GLMs) com ligação canônica.

**Trechos literais:**
> "It is worth noting that maximum likelihood can exhibit severe over-fitting for data sets that are linearly separable. This arises because the maximum likelihood solution occurs when the hyperplane corresponding to $\sigma = 0.5$, equivalent to $\mathbf{w}^T\phi = 0$, separates the two classes and the magnitude of $\mathbf{w}$ goes to infinity." (PRML, p. 206)

> "Following Nelder and Wedderburn (1972), we define a generalized linear model to be one for which $y$ is a nonlinear function of a linear combination of the input (or feature) variables, so that $y = f(\mathbf{w}^T\phi)$. The function $f(\cdot)$ is known as the activation function in the machine learning literature, and its inverse is called the link function in statistics." (PRML, p. 213)

> "...we obtain the canonical link function for which $\eta = \psi(y) = \mathbf{w}^T\phi$. ... If we take the derivative of the log likelihood with respect to the parameter vector $\mathbf{w}$, we find that the gradient takes the form $\nabla E(\mathbf{w}) = \sum_n (y_n - t_n)\phi_n$." (PRML, p. 213)

---

### Fonte 4: ESL (Hastie, Tibshirani & Friedman, 2009), §4.4, pp. 119–124
**Uso pretendido:** Relação com as odds (*razão de chances*), interpretação dos coeficientes como log-odds ratio, e multiclasse via softmax.

**Trechos literais:**
> "The logistic regression model arises from the desire to model the posterior probabilities of the $K$ classes via linear functions in $x$, while at the same time ensuring that they sum to one and remain in $[0, 1]$. The model has the form
> $$\log \frac{\Pr(G=1|X=x)}{\Pr(G=K|X=x)} = \beta_{10} + \beta_1^T x$$
> ... Logistic regression models are used extensively in medical and social sciences, where the odds ratio $\exp(\beta_j)$ has a direct and natural interpretation." (ESL, p. 119)
