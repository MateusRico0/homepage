## Resumo — Aula 4

Esta aula fecha o trio de paradigmas de clustering já citado (ESL, p. 507)
desde a Aula 3: depois do combinatório (protótipos fixos, Aula 3 Bloco 2)
e do "mode seeking" (HDBSCAN, Aula 3 inteira), falta a **modelagem por
mistura**. A Aula 3 terminou com uma "Ponte para a Aula 4" explícita:
o HDBSCAN entrega uma partição **rígida** (cada paciente é de um cluster,
ou é ruído), o que força uma escolha artificial quando duas populações
genuinamente se sobrepõem. A Aula 4 introduz os **Modelos de Mistura
Gaussiana (GMM)** como a resposta a essa limitação: em vez de uma
atribuição única, cada ponto recebe uma probabilidade de pertencer a
cada componente (*soft clustering*). O caminho até esse resultado passa
por (i) formalizar a variável latente categórica $z$ que indica "de qual
população este ponto nasceu"; (ii) a história geradora do GMM (pesos de
mistura $\pi_k$, médias $\mu_k$, covariâncias $\Sigma_k$); (iii) a
dificuldade de maximizar a log-verossimilhança diretamente (soma dentro
do log); (iv) a derivação do algoritmo **EM** — Passo E (responsabilidades
posteriores $\gamma(z_{nk})$ via Bayes) e Passo M (atualização por MLE
ponderada de $\pi,\mu,\Sigma$); e (v) o resultado formal de que o
**KMeans é o caso limite do GMM** quando as covariâncias são esféricas,
idênticas entre componentes, e a variância compartilhada $\epsilon\to 0$.

**Pré-requisitos** (conferidos contra `../_progresso.md`): a Aula 3
já apresentou a "modelagem por mistura" como um dos três paradigmas
citados do ESL (p. 507), sem detalhar — esta aula cumpre essa promessa.
$K$-NN e KDE (Aula 2) não são pré-requisito direto, mas o vocabulário de
"densidade $p(\mathbf{x})$" e MLE (Aula 1, ajuste de Gaussiana
multivariada) são reaproveitados diretamente: o GMM generaliza a Aula 1
de uma única Gaussiana para uma soma ponderada de $K$ Gaussianas.
Nenhuma notação nova conflita com o dicionário já existente ($d_K$,
core distance, $L_\lambda$ não reaparecem nesta aula).

**Estratégia Pedagógica:** Estratégia A (*Outside-In*) — GMM é um
modelo/algoritmo concreto (como KMeans, com quem é comparado o tempo
todo), não uma fundamentação matemática de linguagem; a aula parte do
resultado visual (coloração por responsabilidade) para só depois
formalizar Bayes/MLE ponderada.

## Plano de aula — Aula 4 (carga horária: ~130min)

1. **Abertura: Revisão e Introdução** (~15 min) — Revisão da Aula 3
   (conjunto de nível, HDBSCAN, partição rígida); Ideia Central (relaxar
   atribuição rígida para probabilística); Roteiro de 4 perguntas;
   Problema motivador (pacientes na fronteira entre os dois clusters do
   Bloco 6 da Aula 3); Pausa Ativa.
2. **Intuição — Duas Nuvens Que Se Tocam** (~15 min) — sem fórmula:
   mostrar o mesmo par de atributos (`radius_worst`/`concave
   points_worst`) do Breast Cancer Wisconsin colorido por
   responsabilidade do GMM, lado a lado com a partição rígida do
   HDBSCAN (Aula 3); apontar pacientes com responsabilidade ambígua
   (perto de 50/50) que o HDBSCAN teria jogado fora como ruído ou
   forçado para um lado. Pausa ativa fecha o bloco.
3. **O Modelo de Mistura Gaussiana: Variável Latente** (~15 min) —
   premissas anunciadas (cada ponto nasce de uma, e só uma, de $K$
   populações; a identidade da população é desconhecida); construção de
   $z$ (codificação 1-de-$K$), $p(z_k=1)=\pi_k$, $p(\mathbf{x}\mid
   z_k=1)=\mathcal{N}(\mathbf{x}\mid\mu_k,\Sigma_k)$; diagrama TikZ do
   modelo gráfico ($z\to\mathbf{x}$); marginalização recupera a mistura
   $p(\mathbf{x})=\sum_k\pi_k\mathcal{N}(\mathbf{x}\mid\mu_k,\Sigma_k)$
   já teoricamente possível desde a Aula 1 (soma de gaussianas), agora
   com uma história geradora explícita.
4. **Por Que Não Maximizar a Verossimilhança Direto** (~10 min) — a
   log-verossimilhança tem uma soma dentro do log (diferente da Aula 1,
   uma só Gaussiana); derivar por que isso impede uma solução fechada;
   menção breve às singularidades (variância colapsando sobre um ponto)
   como aviso técnico, sem aprofundar. Motiva a necessidade de um
   algoritmo iterativo.
5. **O Passo E: Responsabilidades Posteriores** (~15 min) — premissa:
   fixar os parâmetros atuais e perguntar, via Bayes, qual a
   probabilidade posterior de cada componente ter gerado cada ponto;
   derivação passo a passo de $\gamma(z_{nk})$; verificação numérica no
   dataset (os 9 pacientes com responsabilidade mais ambígua,
   $|\gamma-0{,}5|<0{,}05$). Pausa ativa.
6. **O Passo M: Atualizações Ponderadas** (~20 min) — premissa: fixar as
   responsabilidades e maximizar a verossimilhança esperada dos dados
   completos por MLE ponderada; derivação de $\mu_k$ (derivada zero),
   $\Sigma_k$ (mesma forma, ponderada), $\pi_k$ (multiplicador de
   Lagrange, restrição $\sum_k\pi_k=1$); interpretação de $N_k$ como
   "número efetivo de pontos" de cada componente.
7. **O Algoritmo EM Completo, em Ação** (~15 min) — juntar E+M num
   ciclo; convergência garantida (mencionar, sem provar em detalhe,
   que é caso do Bloco 4/9.4 do PRML); ajustar `GaussianMixture` de
   verdade no par 2D do Breast Cancer Wisconsin; números reais:
   pesos $\pi\approx(0{,}637,0{,}363)$, acurácia $94{,}55\%$ contra o
   diagnóstico (ambas as componentes usadas, sem ruído), ARI $=0{,}792$
   — comparado ao ARI do HDBSCAN da Aula 3 ($0{,}644$ excluindo ruído,
   $0{,}493$ incluindo). Pausa ativa fecha o bloco.
8. **KMeans Como Caso Limite do GMM** (~15 min) — premissas anunciadas
   (covariâncias esféricas $\epsilon I$, compartilhadas entre
   componentes, $\epsilon$ tratado como constante fixa, não
   reestimado); derivação de que, no limite $\epsilon\to 0$,
   $\gamma(z_{nk})\to r_{nk}$ (atribuição rígida ao componente mais
   próximo) e a atualização de $\mu_k$ reduz à média do KMeans;
   verificação numérica própria (não do livro): responsabilidade média
   máxima subindo de $0{,}904$ ($\epsilon=1$) para $0{,}9996$
   ($\epsilon=0{,}01$), com acurácia da atribuição rígida contra o
   KMeans de referência subindo de $95{,}78\%$ para $100\%$.
9. **Fechamento e Ponte para a Aula 5** (~10 min) — retomar as 4
   perguntas da Abertura; o que fica em aberto: como escolher $K$
   (número de componentes) e como avaliar um modelo de variável
   latente sem cair em overfitting de verossimilhança — ponte para BIC
   e Inferência Variacional (Aula 5). Pausa ativa final.

Transições: Bloco 1→2 (rígido vs. probabilístico, mostrado antes de
formalizar); 2→3 (o resultado visual pede uma história geradora
formal); 3→4 (a história geradora dá uma verossimilhança difícil de
maximizar); 4→5→6 (a saída é EM, dividido em seus dois passos);
6→7 (juntar os passos, rodar de verdade); 7→8 (pergunta puramente
teórica: e se as covariâncias fossem triviais? cai no KMeans já
conhecido); 8→9 (fechamento).

## Fontes usadas — Aula 4

### Fonte 1: PRML (Bishop, 2006), §9.2, pp. 430–432 (offset +20)
**Uso pretendido:** formulação por variável latente do GMM (Bloco 3):
introdução de $z$, $p(z)$, $p(\mathbf{x}\mid z)$, e a definição de
responsabilidade $\gamma(z_k)$ via Bayes.

**Trecho (p. 430–431):**
> "Let us introduce a K-dimensional binary random variable z having a
> 1-of-K representation in which a particular element zk is equal to 1
> and allother elements are equal to 0. [...] The marginal distribution
> over z is specified in terms of the mixing coefficients πk, such that
> p(zk = 1) = πk"

**Trecho (p. 432, definição de responsabilidade):**
> "γ(zk) ≡ p(zk = 1|x) = [πk N (x|µk, Σk)] / [Σj πj N (x|µj, Σj)] ...
> γ(zk) can also be viewed as the responsibility that component k takes
> for 'explaining' the observation x."

---

### Fonte 2: PRML (Bishop, 2006), §9.2.1, pp. 433–435 (offset +20)
**Uso pretendido:** log-verossimilhança do GMM (Bloco 4) e o aviso sobre
singularidades (variância colapsando sobre um ponto).

**Trecho (p. 433, log-verossimilhança):**
> "ln p(X|π, µ, Σ) = ΣNn=1 ln{ΣKk=1 πk N (xn|µk, Σk)}."

**Trecho (p. 433–434, dificuldade da soma dentro do log):**
> "The difficulty arises from the presence of the summation over k that
> appears inside the logarithm in (9.14), so that the logarithm function
> no longer acts directly on the Gaussian. If we set the derivatives of
> the log likelihood to zero, we will no longer obtain a closed form
> solution."

**Trecho (p. 434, singularidade):**
> "If we consider the limit σj → 0, then we see that this term goes to
> infinity and so the log likelihood function will also go to infinity.
> Thus the maximization of the log likelihood function is not a well
> posed problem because such singularities will always be present."

---

### Fonte 3: PRML (Bishop, 2006), §9.2.2, pp. 435–437 (offset +20)
**Uso pretendido:** derivação completa do Passo M (Bloco 6) — $\mu_k$,
$\Sigma_k$, $\pi_k$ via multiplicador de Lagrange, e a definição de
$N_k$.

**Trecho (p. 435, atualização de $\mu_k$):**
> "µk = (1/Nk) ΣNn=1 γ(znk)xn where we have defined Nk = ΣNn=1 γ(znk).
> We can interpret Nk as the effective number of points assigned to
> cluster k."

**Trecho (p. 436, atualização de $\Sigma_k$):**
> "Σk = (1/Nk) ΣNn=1 γ(znk)(xn − µk)(xn − µk)^T which has the same form
> as the corresponding result for a single Gaussian fitted to the data
> set, but again with each data point weighted by the corresponding
> posterior probability."

**Trecho (p. 436, atualização de $\pi_k$):**
> "πk = Nk/N so that the mixing coefficient for the kth component is
> given by the average responsibility which that component takes for
> explaining the data points."

**Trecho (p. 437, resumo do ciclo E/M):**
> "In the expectation step, or E step, we use the current values for the
> parameters to evaluate the posterior probabilities, or responsibilities
> [...] We then use these probabilities in the maximization step, or M
> step, to re-estimate the means, covariances, and mixing coefficients."

---

### Fonte 4: PRML (Bishop, 2006), §9.3.2, pp. 443–444 (offset +20)
**Uso pretendido:** o resultado central do Bloco 8 — KMeans como caso
limite do GMM.

**Trecho (p. 443, setup do limite):**
> "Consider a Gaussian mixture model in which the covariance matrices of
> the mixture components are given by εI, where ε is a variance
> parameter that is shared by all of the components [...] We now
> consider the EM algorithm for a mixture of K Gaussians of this form in
> which we treat ε as a fixed constant, instead of a parameter to be
> re-estimated."

**Trecho (p. 444, o limite ε→0):**
> "If we consider the limit ε → 0, we see that in the denominator the
> term for which ‖xn − µj‖² is smallest will go to zero most slowly, and
> hence the responsibilities γ(znk) for the data point xn all go to zero
> except for term j, for which the responsibility γ(znj) will go to
> unity. [...] Thus, in this limit, we obtain a hard assignment of data
> points to clusters, just as in the K-means algorithm."

**Trecho (p. 444, redução do Passo M ao KMeans):**
> "The EM re-estimation equation for the µk, given by (9.17), then
> reduces to the K-means result (9.4). [...] in this limit, maximizing
> the expected complete-data log likelihood is equivalent to minimizing
> the distortion measure J for the K-means algorithm."

---

### Fonte 5: PRML (Bishop, 2006), §9.1, pp. 424, 427 (offset +20)
**Uso pretendido:** relembrar a definição do KMeans (medida de
distorção $J$, atribuição rígida $r_{nk}$, atualização de $\mu_k$) —
necessária para o Bloco 8 comparar termo a termo com o GMM.

**Trecho (p. 424, medida de distorção):**
> "J = ΣNn=1 ΣKk=1 rnk ‖xn − µk‖². [...] Our goal is to find values for
> the {rnk} and the {µk} so as to minimize J."

**Trecho (p. 427, atribuição rígida e atualização):**
> "rnk = 1 if k = argminj ‖xn − µj‖², 0 otherwise. [...] µk =
> (Σn rnk xn)/(Σn rnk)."

---

### Fonte 6: ESL (Hastie, Tibshirani & Friedman, 2009), §8.5–8.5.1, pp. 272–274 (offset +19)
**Uso pretendido:** framing alternativo e mais informal da variável
latente (Bloco 3, como reforço complementar ao PRML) — o exemplo de
duas componentes com $\Delta_i\in\{0,1\}$ ajuda a explicar a mesma ideia
com notação mais simples (mistura de 2 ao invés de $K$).

**Trecho (p. 272–273, formulação generativa):**
> "Y1 ∼ N(µ1, σ1²), Y2 ∼ N(µ2, σ2²), Y = (1 − ∆) · Y1 + ∆ · Y2, where
> ∆ ∈ {0, 1} with Pr(∆ = 1) = π. This generative representation is
> explicit: generate a ∆ ∈ {0, 1} with probability π, and then depending
> on the outcome, deliver either Y1 or Y2."

**Trecho (p. 274, motivação do EM via verossimilhança inatingível):**
> "Direct maximization of ℓ(θ; Z) is quite difficult numerically, because
> of the sum of terms inside the logarithm. There is, however, a simpler
> approach. We consider unobserved latent variables ∆i [...] Since the
> values of the ∆i's are actually unknown, we proceed in an iterative
> fashion, substituting for each ∆i in (8.40) its expected value γi(θ) =
> E(∆i|θ, Z) [...] also called the responsibility of model 2 for
> observation i."

---

### Notas sobre as fontes

- Todos os trechos foram extraídos literalmente do PDF via
  `pdftotext -layout`, com offset de página confirmado por inspeção
  direta do cabeçalho de página impresso versus a página do PDF (PRML:
  +20, mesmo offset já usado nas Aulas 1–3; ESL: +19, mesmo offset já
  registrado na Aula 2).
- DLFC (Bishop & Bishop, 2024) não foi localizado com um tratamento de
  GMM/EM diferente o suficiente do PRML para justificar uma citação
  própria nesta aula — os dois autores compartilham a mesma notação e
  desenvolvimento; fica como nota, não como pendência (o PRML sozinho
  já cobre tudo o que a aula precisa, com offset já validado em aulas
  anteriores).
- O resultado do Bloco 8 (verificação numérica de que a responsabilidade
  média máxima sobe de $0{,}904$ para $0{,}9996$, e a concordância com o
  KMeans de $95{,}78\%$ para $100\%$, variando $\epsilon$ de $1$ a
  $0{,}01$) **não vem de nenhum livro** — é uma verificação numérica
  nossa, construída para tornar tangível o resultado teórico do PRML
  (Fonte 4), mesmo tratamento dado a verificações numéricas nas Aulas
  1–3 (sinalizado como tal no `index.qmd`).
- Todos os números do Bloco 2 e do Bloco 7 (pesos $\pi$, acurácia,
  ARI, contagem de pacientes ambíguos) foram computados por script
  Python antes de escrever a aula, reaproveitando exatamente o mesmo
  carregamento/pré-processamento do Breast Cancer Wisconsin já usado na
  Aula 3 (`radius_worst`/`concave points_worst`, padronizado).
