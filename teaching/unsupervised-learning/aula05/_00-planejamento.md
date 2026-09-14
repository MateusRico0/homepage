## Resumo — Aula 5

A Aula 4 fechou com uma pergunta explícita, deixada sem resposta: mais
componentes ($K=10$ vs. $K=2$) sempre aumenta (ou nunca piora) a
log-verossimilhança de treino de um GMM? Esta aula responde essa
pergunta de forma rigorosa (sim — e prova/verifica numericamente por
quê), mostra por que isso torna a log-verossimilhança pura inútil como
critério de seleção de $K$, e introduz o **BIC** como aproximação
assintótica da evidência do modelo via aproximação de Laplace. Na
segunda metade, a aula generaliza o problema: a evidência do modelo
$p(\mathcal{D})$ é intratável em geral (não só para GMM), e a aula
introduz a **divergência KL** e a decomposição
$\ln p(\mathbf{X}) = \mathcal{L}(q) + \mathrm{KL}(q\|p)$, culminando no
**ELBO** ($\mathcal{L}(q)$) como cota inferior sempre válida da
evidência. O fechamento amarra essa ferramenta de volta ao Algoritmo EM
da Aula 4: o Passo E e o Passo M da Aula 4 são, precisamente, subida de
coordenadas no ELBO (E: maximiza $\mathcal{L}$ sobre $q$ com $\theta$
fixo; M: maximiza $\mathcal{L}$ sobre $\theta$ com $q$ fixo) — o EM não
é um truque isolado, é um caso particular do framework geral que esta
aula introduz.

**Objetivos de aprendizagem:** (1) explicar por que a log-verossimilhança
de treino não serve para escolher $K$; (2) derivar o BIC a partir da
aproximação de Laplace da evidência e aplicá-lo à seleção de $K$ num
GMM; (3) definir formalmente a divergência KL e provar sua
não-negatividade; (4) derivar a decomposição
$\ln p(\mathbf{X}) = \mathcal{L}(q) + \mathrm{KL}(q\|p)$ e identificar o
ELBO como cota inferior; (5) reconhecer o EM da Aula 4 como caso
particular de subida de coordenadas no ELBO.

**Pré-requisitos** (checados contra o dicionário de notações e o
resumo da Aula 4 em `../_progresso.md`): GMM com variável latente $z$
1-de-$K$ e prior $\pi_k$; responsabilidade $\gamma(z_{nk})$; Passo E e
Passo M; log-verossimilhança $\ln p(\mathbf{X}|\boldsymbol\theta)$;
verossimilhança marginalizada sobre $z$. Nada disso muda de notação
nesta aula — só se acrescenta a ela.

**Estratégia Pedagógica:** Estratégia A (*Outside-In*) — o "modelo
mental catchy" é a tentação óbvia e errada ("escolher $K$ que maximiza
a verossimilhança de treino"), que a aula desmonta antes de introduzir
a teoria formal (BIC, depois KL/ELBO) e fechar com síntese e limitação
(ELBO como critério geral, mas ainda exige posterior exata ou tratável
— limitação que motiva a Aula 7/VAE).

## Plano de aula — Aula 5 (carga horária: ~120 min)

1. **Abertura — Revisão e Introdução** (~12 min) — revisão cuidadosa do
   GMM/EM da Aula 4 (variável latente, responsabilidade, Passo E/M,
   KMeans como caso limite); Ideia Central (Ausubel): "ajustamos o
   modelo — mas nunca perguntamos se o modelo, ou o $K$ escolhido, era
   bom"; roteiro explícito das 4 perguntas da aula; problema motivador
   (o próprio gráfico log-verossimilhança vs. $K$ no Breast Cancer
   Wisconsin, $K=1,\dots,10$, mostrando crescimento monótono); Pausa
   Ativa 1.
2. **Intuição** (~10 min) — sem equações: por que a log-verossimilhança
   de treino "recompensa" complexidade por construção (mais componentes
   $\Rightarrow$ mais liberdade para encaixar cada ponto); mostrar lado
   a lado o gráfico de log-verossimilhança (sempre subindo) e uma
   prévia do gráfico de BIC (com pico interior) — o aluno já vê a forma
   final do argumento antes de qualquer fórmula.
3. **Por que a verossimilhança pura falha** (~12 min) — desenvolvimento
   principled: liga explicitamente ao Bloco 4 da Aula 4 (singularidade
   quando um componente colapsa sobre um único ponto,
   $\Sigma_k\to\mathbf{0}$, log-verossimilhança $\to\infty$); argumento
   geral de que aumentar $K$ nunca pode reduzir o máximo da
   verossimilhança de treino (um modelo com $K$ componentes é replicável
   por um com $K+1$, fixando o peso do novo componente a $0^+$); Pausa
   Ativa 2.
4. **A evidência do modelo e o BIC** (~20 min) — desenvolvimento
   principled com premissas explícitas: evidência
   $p(\mathcal{D})=\int p(\mathcal{D}|\boldsymbol\theta)p(\boldsymbol\theta)\,\mathrm{d}\boldsymbol\theta$
   como o objeto que realmente queremos (não a verossimilhança pura);
   por que a integral é intratável em geral; aproximação de Laplace
   (retomando a intuição de "moda + curvatura" já vista em outras
   disciplinas do curso, mas formal aqui) $\to$ eq. (4.137) $\to$
   BIC eq. (4.139) sob as premissas de prior largo e Hessiana de posto
   completo; aplicação ao GMM (contagem de parâmetros $M(K,d)$); cálculo
   real no Breast Cancer Wisconsin, $K=1,\dots,10$: BIC atinge o máximo
   em $K=2$ mesmo com a log-verossimilhança subindo até $K=10$. Pausa
   Ativa 3.
5. **KL e a decomposição geral $\ln p(\mathbf{X})=\mathcal{L}(q)+\mathrm{KL}(q\|p)$**
   (~25 min) — motivação: BIC só funciona sob as premissas de Laplace
   (posterior aproximadamente Gaussiana, Hessiana de posto completo) —
   nem sempre válidas; precisamos de uma ferramenta mais geral.
   Definição formal de divergência KL (callout formal), prova da
   não-negatividade via desigualdade de Jensen (Gibbs); decomposição via
   regra do produto (PRML §10.1, com $\theta$ absorvido em $Z$, mais
   geral que o caso do EM); ELBO $\mathcal{L}(q)$ como cota inferior
   sempre válida, com igualdade sse $q(\mathbf{Z})=p(\mathbf{Z}|\mathbf{X})$.
   Exemplo numérico concreto reaproveitando o GMM $K=2$ já ajustado na
   Aula 4: $\mathcal{L}(q=\text{posterior})=\ln p(\mathbf{X}|\boldsymbol\theta)$
   exatamente (KL $=0$), $\mathcal{L}(q=\text{uniforme})$ e
   $\mathcal{L}(q=\text{de um }\theta\text{ errado})$ ambos estritamente
   menores, com a diferença batendo exatamente com $\mathrm{KL}(q\|p)$
   calculado independentemente. Pausa Ativa 4.
6. **O EM da Aula 4 é subida de coordenadas no ELBO** (~15 min) —
   especialização da decomposição para $\theta$ não-Bayesiano (PRML
   §9.4, eq. 9.69–9.74): Passo E = $\arg\max_q\mathcal{L}(q,\theta^{\text{old}})$
   com $\theta$ fixo $\Rightarrow q=p(\mathbf{Z}|\mathbf{X},\theta^{\text{old}})$
   (fecha o KL); Passo M = $\arg\max_\theta\mathcal{L}(q,\theta)$ com $q$
   fixo. Ligação explícita com os nomes exatos usados na Aula 4
   (responsabilidade $\gamma(z_{nk})$ = a distribuição $q$ ótima do
   Passo E). Diagrama TikZ da decomposição (barra
   $\ln p(\mathbf{X})=\mathcal{L}+\mathrm{KL}$) e um segundo diagrama
   mostrando o Passo E fechando o KL. Pausa Ativa 5.
7. **Síntese** (~8 min) — ELBO unifica seleção (BIC como aproximação
   assintótica/pontual do mesmo problema de evidência) e ajuste
   (EM como caso do ELBO com posterior exata tratável); nomear a
   limitação central: e quando a posterior $p(\mathbf{Z}|\mathbf{X})$
   não é tratável nem para o Passo E? (gancho para inferência
   variacional plena/VAE na Aula 7).
8. **Fechamento e Ponte para a Aula 6** (~8 min) — retomar as 4
   perguntas da abertura, uma frase cada; nomear o que fica em aberto
   (posterior intratável em modelos mais ricos); ponte para a Aula 6 —
   mudança de tema, não só de método: a partir daqui a disciplina
   troca a variável latente **categórica** (GMM) pela variável latente
   **contínua** (PCA/PPCA), abrindo a Parte 2 do curso
   (Redução de Dimensionalidade e Auto-Supervisão).

**Exercícios finais:** 3 discursivas + 7 blocos de V/F (28 itens) —
densidade um pouco menor que a Aula 4 (28 itens) porque esta aula tem
menos blocos de conteúdo numérico-aplicado e mais teoria unificadora;
7 blocos cobrem: verossimilhança vs. complexidade; evidência e
aproximação de Laplace; BIC aplicado a GMM; definição e propriedades da
divergência KL; a decomposição $\mathcal{L}+\mathrm{KL}$; EM como
subida de coordenadas; síntese/limitações e ponte para a Aula 6.

## Fontes usadas — Aula 5

### Fonte 1: PRML, §4.4.1 "Model comparison and BIC", pp. 216–217 (PDF pp. 236–237, offset +20 confirmado nesta sessão comparando o cabeçalho de página)

**Uso pretendido:** derivação da aproximação de Laplace da evidência do
modelo e do BIC (eq. 4.137–4.139), base do Bloco 4.

**Trecho (p. 216):**
> "4.4.1 Model comparison and BIC
> As well as approximating the distribution p(z) we can also obtain an approxi-
> mation to the normalization constant Z. Using the approximation (4.133) we have
>
> Z ≃ f(z0) (2π)^{M/2} / |A|^{1/2}                                              (4.135)
>
> where we have noted that the integrand is Gaussian and made use of the standard
> result (2.43) for a normalized Gaussian distribution. We can use the result (4.135) to
> obtain an approximation to the model evidence which, as discussed in Section 3.4,
> plays a central role in Bayesian model comparison.
> Consider a data set D and a set of models {Mi} having parameters {θi}. For
> each model we define a likelihood function p(D|θi, Mi). If we introduce a prior
> p(θi|Mi) over the parameters, then we are interested in computing the model evi-
> dence p(D|Mi) for the various models. [...] From Bayes' theorem the model evidence is
> given by
>
> p(D) = ∫ p(D|θ)p(θ) dθ.                                                        (4.136)
>
> Identifying f(θ) = p(D|θ)p(θ) and Z = p(D), and applying the result (4.135), we
> obtain
>
> ln p(D) ≃ ln p(D|θ_MAP) + ln p(θ_MAP) + (M/2) ln(2π) − (1/2) ln|A|            (4.137)
>                                          \_____________ Occam factor ____________/"

**Trecho (p. 217):**
> "If we assume that the Gaussian prior distribution over parameters is broad, and
> that the Hessian has full rank, then we can approximate (4.137) very roughly using
>
> ln p(D) ≃ ln p(D|θ_MAP) − (1/2) M ln N                                        (4.139)
>
> where N is the number of data points, M is the number of parameters in θ and
> we have omitted additive constants. This is known as the Bayesian Information
> Criterion (BIC) or the Schwarz criterion (Schwarz, 1978). Note that, compared to
> AIC given by (1.73), this penalizes model complexity more heavily."

---

### Fonte 2: PRML, §1.6.1 "Relative entropy and mutual information", pp. 55–56 (PDF pp. 75–76)

**Uso pretendido:** definição formal da divergência KL (eq. 1.113) e
prova da não-negatividade via desigualdade de Jensen/convexidade
(eq. 1.113–1.118), base do Bloco 5.

**Trecho (p. 55):**
> "Consider some unknown distribution p(x), and suppose that we have modelled
> this using an approximating distribution q(x). If we use q(x) to construct a coding
> scheme for the purpose of transmitting values of x to a receiver, then the average
> additional amount of information (in nats) required to specify the value of x
> (assuming we choose an efficient coding scheme) as a result of using q(x) instead of
> the true distribution p(x) is given by
>
> KL(p‖q) = − ∫ p(x) ln q(x) dx − ( − ∫ p(x) ln p(x) dx )
>          = − ∫ p(x) ln { q(x)/p(x) } dx.                                       (1.113)
>
> This is known as the relative entropy or Kullback-Leibler divergence, or KL diver-
> gence (Kullback and Leibler, 1951), between the distributions p(x) and q(x). Note
> that it is not a symmetrical quantity, that is to say KL(p‖q) ≢ KL(q‖p).
> We now show that the Kullback-Leibler divergence satisfies KL(p‖q) ⩾ 0 with
> equality if, and only if, p(x) = q(x)."

**Trecho (p. 56):**
> "We can apply Jensen's inequality in the form (1.117) to the Kullback-Leibler
> divergence (1.113) to give
>
> KL(p‖q) = − ∫ p(x) ln { q(x)/p(x) } dx ⩾ − ln ∫ q(x) dx = 0                    (1.118)"

---

### Fonte 3: PRML, §9.4 "The EM Algorithm in General", pp. 450–452 (PDF pp. 470–472)

**Uso pretendido:** decomposição $\ln p(\mathbf{X}|\boldsymbol\theta) =
\mathcal{L}(q,\boldsymbol\theta) + \mathrm{KL}(q\|p)$ com $\theta$
como parâmetro (não Bayesiano pleno) e a releitura do Passo E/Passo M
da Aula 4 como subida de coordenadas nesse funcional — base do Bloco 6,
o elo de fechamento com a Aula 4.

**Trecho (p. 450):**
> "The expectation maximization algorithm, or EM algorithm, is a general technique for
> finding maximum likelihood solutions for probabilistic models having latent vari-
> ables [...] Here we give a very
> general treatment of the EM algorithm and in the process provide a proof that the
> EM algorithm derived heuristically in Sections 9.2 and 9.3 for Gaussian mixtures
> does indeed maximize the likelihood function [...]
> Consider a probabilistic model in which we collectively denote all of the ob-
> served variables by X and all of the hidden variables by Z. [...] Our goal
> is to maximize the likelihood function that is given by
>
> p(X|θ) = Σ_Z p(X, Z|θ).                                                        (9.69)
>
> [...] we introduce a distribution q(Z) defined over the latent variables, and we ob-
> serve that, for any choice of q(Z), the following decomposition holds
>
> ln p(X|θ) = L(q, θ) + KL(q‖p)                                                  (9.70)
>
> where we have defined
>
> L(q, θ) = Σ_Z q(Z) ln { p(X, Z|θ) / q(Z) }                                     (9.71)
>
> KL(q‖p) = − Σ_Z q(Z) ln { p(Z|X, θ) / q(Z) }.                                  (9.72)"

**Trecho (p. 451):**
> "The EM algorithm is a two-stage iterative optimization technique for finding
> maximum likelihood solutions. We can use the decomposition (9.70) to define the
> EM algorithm and to demonstrate that it does indeed maximize the log likelihood.
> Suppose that the current value of the parameter vector is θ^old. In the E step, the
> lower bound L(q, θ^old) is maximized with respect to q(Z) while holding θ^old fixed.
> The solution to this maximization problem is easily seen by noting that the value
> of ln p(X|θ^old) does not depend on q(Z) and so the largest value of L(q, θ^old)
> will occur when the Kullback-Leibler divergence vanishes, in other words when
> q(Z) is equal to the posterior distribution p(Z|X, θ^old). [...]
> In the subsequent M step, the distribution q(Z) is held fixed and the lower bound
> L(q, θ) is maximized with respect to θ to give some new value θ^new."

---

### Fonte 4: PRML, §10.1 "Variational Inference", pp. 462–463 (PDF pp. 482–483)

**Uso pretendido:** versão totalmente geral (Bayesiana, $\theta$
absorvido em $\mathbf{Z}$) da mesma decomposição, para deixar claro que
o resultado do Bloco 6 (EM) é um caso particular de um framework ainda
mais geral — usado no Bloco 5 para apresentar a decomposição pela
primeira vez, antes de especializar para o EM no Bloco 6.

**Trecho (p. 463):**
> "Now let us consider in more detail how the concept of variational optimization
> can be applied to the inference problem. Suppose we have a fully Bayesian model in
> which all parameters are given prior distributions. The model may also have latent
> variables as well as parameters, and we shall denote the set of all latent variables
> and parameters by Z. Similarly, we denote the set of all observed variables by X.
> [...] As in our discussion of EM, we can decompose the log marginal probability using
>
> ln p(X) = L(q) + KL(q‖p)                                                       (10.2)
>
> where we have defined
>
> L(q) = ∫ q(Z) ln { p(X, Z) / q(Z) } dZ                                         (10.3)
>
> KL(q‖p) = − ∫ q(Z) ln { p(Z|X) / q(Z) } dZ.                                    (10.4)
>
> This differs from our discussion of EM only in that the parameter vector θ no longer
> appears, because the parameters are now stochastic variables and are absorbed into
> Z. [...] we
> can maximize the lower bound L(q) by optimization with respect to the distribution
> q(Z), which is equivalent to minimizing the KL divergence. If we allow any possible
> choice for q(Z), then the maximum of the lower bound occurs when the KL diver-
> gence vanishes, which occurs when q(Z) equals the posterior distribution p(Z|X)."

---

**Números verificados nesta sessão, por script independente** (não
inventados, ver `verify_bic.py` e `verify_elbo.py` gerados no diretório
de trabalho da sessão — reproduzíveis a partir do `.qmd` final, cujo
código é o mesmo usado nos scripts de verificação):

- GMM ajustado (`GaussianMixture`, `covariance_type="full"`, múltiplos
  reinícios) em `radius_worst`/`concave points_worst` padronizados
  (mesmas duas colunas da Aula 4), $K=1,\dots,10$: log-verossimilhança
  total estritamente não-decrescente em $K$ (confirmado), de
  $-1339{,}45$ ($K=1$) a $-1169{,}66$ ($K=10$). Contagem de parâmetros
  $M(K,d{=}2)=6K-1$ (médias $2K$ + covariâncias $3K$ + pesos $K-1$).
  BIC no sentido do PRML (eq. 4.139, a **maximizar**) atinge o pico em
  $K=2$ ($-1238{,}98$), caindo monotonicamente depois — mesmo com a
  log-verossimilhança ainda subindo. **Atenção de convenção:**
  bibliotecas como o `scikit-learn` (`GaussianMixture.bic()`) reportam
  $-2\ln p(\mathcal{D}|\theta_{\mathrm{ML}}) + M\ln N$ (a
  **minimizar**) — o mesmo critério, sinal invertido; a aula usa a
  convenção do PRML (maximizar) e sinaliza essa diferença de convenção
  explicitamente para não confundir quem for usar `scikit-learn` depois.
- Exemplo numérico do ELBO reaproveitando o GMM $K=2$ da Aula 4: com
  $q=$ responsabilidades verdadeiras, $\mathcal{L}(q,\theta)=
  \ln p(\mathbf{X}|\theta)=-1204{,}0898$ exatamente (diferença
  $2{,}3\times10^{-13}$, arredondamento de ponto flutuante). Com
  $q=$ uniforme $50/50$ (ignorando os dados), $\mathcal{L}(q)=
  -2474{,}67$, gap $=1270{,}58$, batendo exatamente com
  $\mathrm{KL}(q_{\text{unif}}\|p)$ calculado de forma independente
  ($1270{,}585$). Com $q$ vindo das responsabilidades de um
  $\theta$ "errado" (médias trocadas e encolhidas), $\mathcal{L}(q)=
  -3644{,}54$, gap $=2440{,}45$, de novo batendo exatamente com o KL
  calculado à parte.
