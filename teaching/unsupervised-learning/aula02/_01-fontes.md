# Fontes usadas — Aula 2

> Trechos literais extraídos lendo diretamente as páginas do PDF (não
> reescritos de memória).
>
> - `../fontes/prml.pdf` (Bishop, PRML, 2006): offset **+20** confirmado
>   nesta sessão (mesmo valor já usado na Aula 1 e nas fontes de
>   `supervised-learning`) — página impressa 121 = página 141 do PDF.
> - `../fontes/esl.pdf` (Hastie, Tibshirani & Friedman, ESL, 2009):
>   offset **+19** confirmado nesta sessão — página impressa 21 = página
>   40 do PDF (`pdftotext -f 40` retorna "21" como primeira linha).

---

### Fonte 1: Bishop, PRML (2006), §1.4 "The Curse of Dimensionality", pp. 33–37
**Uso pretendido:** a maldição da dimensionalidade, geometricamente — concentração de volume numa hiperesfera e de massa numa gaussiana em alta dimensão (Bloco 2).

**Trecho:**
> "There are numerous problems with this naive approach, but one of the
> most severe becomes apparent when we consider its extension to
> problems having larger numbers of input variables [...] if we divide a
> region of a space into regular cells, then the number of such cells
> grows exponentially with the dimensionality of the space." (p. 35)
>
> "As a simple example, consider a sphere of radius r = 1 in a space of
> D dimensions, and ask what is the fraction of the volume of the sphere
> that lies between radius r = 1 − ε and r = 1. [...] the volume of a
> sphere of radius r in D dimensions must scale as r^D, and so we write
> V_D(r) = K_D r^D [...] Thus the required fraction is given by
> [V_D(1) − V_D(1 − ε)] / V_D(1) = 1 − (1 − ε)^D [...] We see that, for
> large D, this fraction tends to 1 even for small values of ε. Thus, in
> spaces of high dimensionality, most of the volume of a sphere is
> concentrated in a thin shell near the surface!" (pp. 36–37)
>
> "As a further example, of direct relevance to pattern recognition,
> consider the behaviour of a Gaussian distribution in a high-dimensional
> space. [...] we see that for large D the probability mass of the
> Gaussian is concentrated in a thin shell. [...] The severe difficulty
> that can arise in spaces of many dimensions is sometimes called the
> curse of dimensionality (Bellman, 1961)." (p. 37)

---

### Fonte 2: Bishop, PRML (2006), §2.5 "Nonparametric Methods", pp. 120–123
**Uso pretendido:** as lições do histograma, e o resultado geral $p(\mathbf{x})=K/(NV)$ que unifica k-NN e KDE (Bloco 3).

**Trecho:**
> "Another major limitation of the histogram approach is its scaling
> with dimensionality. If we divide each variable in a D-dimensional
> space into M bins, then the total number of bins will be M^D. This
> exponential scaling with D is an example of the curse of
> dimensionality." (p. 121)
>
> "First, to estimate the probability density at a particular location,
> we should consider the data points that lie within some local
> neighbourhood of that point. [...] Second, the value of the smoothing
> parameter should be neither too large nor too small in order to obtain
> good results." (pp. 121–122)
>
> "Now suppose that we have collected a data set comprising N
> observations drawn from p(x). Because each data point has a
> probability P of falling within R, the total number K of points that
> lie inside R will be distributed according to the binomial
> distribution [...] For large N, this distribution will be sharply
> peaked around the mean and so K ≃ NP. If, however, we also assume that
> the region R is sufficiently small that the probability density p(x)
> is roughly constant over the region, then we have P ≃ p(x)V [...]
> Combining [...] we obtain our density estimate in the form p(x) =
> K/(NV)." (p. 122)
>
> "We can exploit this result in two different ways. Either we can fix K
> and determine the value of V from the data, which gives rise to the
> K-nearest-neighbour technique [...], or we can fix V and determine K
> from the data, giving rise to the kernel approach." (p. 123)

---

### Fonte 3: Bishop, PRML (2006), §2.5.1 "Kernel density estimators", pp. 123–124
**Uso pretendido:** a janela de Parzen (hipercubo) e a passagem para o kernel gaussiano suave — KDE (Bloco 5).

**Trecho:**
> "[...] we take the region R to be a small hypercube centred on the
> point x [...] k(u) = 1 if |u_i| ≤ 1/2 for i = 1,...,D, 0 otherwise [...]
> The total number of data points lying inside this cube will therefore
> be K = Σ_n k((x − x_n)/h). Substituting this expression [...] gives [...]
> p(x) = (1/N) Σ_n (1/h^D) k((x − x_n)/h)." (p. 123)
>
> "As it stands, the kernel density estimator will suffer from one of the
> same problems that the histogram method suffered from, namely the
> presence of artificial discontinuities, in this case at the boundaries
> of the cubes. We can obtain a smoother density model if we choose a
> smoother kernel function, and a common choice is the Gaussian [...]
> p(x) = (1/N) Σ_n 1/(2πh²)^(1/2) exp(−‖x − x_n‖²/2h²) [...] where h
> represents the standard deviation of the Gaussian components." (p. 124)
>
> "We see that, as expected, the parameter h plays the role of a
> smoothing parameter, and there is a trade-off between sensitivity to
> noise at small h and over-smoothing at large h." (p. 124)

---

### Fonte 4: Bishop, PRML (2006), §2.5.2 "Nearest-neighbour methods", pp. 124–127
**Uso pretendido:** k-NN para densidade, $p(\mathbf{x})\propto 1/d_K(\mathbf{x})^D$, e a nota honesta de que não é uma densidade de verdade (Bloco 4); custo de armazenamento (Bloco 7).

**Trecho:**
> "[...] instead of fixing V and determining the value of K from the
> data, we consider a fixed value of K and use the data to find an
> appropriate value for V. To do this, we consider a small sphere centred
> on the point x [...] and we allow the radius of the sphere to grow
> until it contains precisely K data points. The estimate of the density
> p(x) is then given by [K/(NV)] with V set to the volume of the
> resulting sphere. This technique is known as K nearest neighbours."
> (pp. 124–125)
>
> "Note that the model produced by K nearest neighbours is not a true
> density model because the integral over all space diverges." (p. 125)
>
> "As discussed so far, both the K-nearest-neighbour method, and the
> kernel density estimator, require the entire training data set to be
> stored, leading to expensive computation if the data set is large."
> (p. 127)

---

### Fonte 5 (livro-texto adicional, primeira vez usado nesta disciplina): Hastie, Tibshirani & Friedman, ESL (2009), §2.5 "Local Methods in High Dimensions", pp. 22–24
**Uso pretendido:** a maldição da dimensionalidade especificamente para métodos locais/k-NN — fórmulas concretas de comprimento de aresta e distância ao vizinho mais próximo, complementando o PRML (duplo registro, Bloco 2).

**Sinalização de fonte:** ESL já está em `_fontes/` (link simbólico
compartilhado com `supervised-learning`), mas nunca havia sido citado
nas aulas já publicadas desta disciplina — primeiro uso aqui.

**Trecho:**
> "Consider the nearest-neighbor procedure for inputs uniformly
> distributed in a p-dimensional unit hypercube [...]. Suppose we send
> out a hypercubical neighborhood about a target point to capture a
> fraction r of the observations. [...] the expected edge length will be
> e_p(r) = r^(1/p). In ten dimensions e_10(0.01) = 0.63 and e_10(0.1) =
> 0.80, while the entire range for each input is only 1.0. So to capture
> 1% or 10% of the data to form a local average, we must cover 63% or
> 80% of the range of each input variable. Such neighborhoods are no
> longer 'local.'" (p. 22)
>
> "Another consequence of the sparse sampling in high dimensions is that
> all sample points are close to an edge of the sample. [...] The median
> distance from the origin to the closest data point is given by the
> expression d(p, N) = (1 − (1/2)^(1/N))^(1/p) [...]. For N = 500, p =
> 10, d(p, N) ≈ 0.52, more than halfway to the boundary. Hence most data
> points are closer to the boundary of the sample space than to any
> other data point." (pp. 22–23)
>
> "Another manifestation of the curse is that the sampling density is
> proportional to N^(1/p) [...]. Thus, if N_1 = 100 represents a dense
> sample for a single input problem, then N_10 = 100^10 is the sample
> size required for the same sampling density with 10 inputs." (p. 23)

---

## Achado sem citação de livro — sinalizado explicitamente

**Comparação L1/L2/Cosseno e "contraste relativo" como medida de
concentração:** não encontrado em PRML, ESL nem DLFC (busca feita nesta
sessão nos três PDFs por "cosine similarity/distance", "L1 norm",
"Manhattan distance", "curse of dimensionality", "concentration of
measure"). Tratado como **demonstração numérica nossa** — a mesma
prática já usada na Aula 1 para a distribuição $\chi^2_d$ da distância
de Mahalanobis. Métrica de contraste relativo,
$(\text{dist}_{\max}-\text{dist}_{\min})/\text{dist}_{\min}$, no
estilo de Beyer et al. (1999) / Aggarwal et al. (2001) sobre o
significado de "vizinho mais próximo" em alta dimensão — citação de
autor mencionada na aula como atribuição de origem da ideia, não como
citação literal de um texto lido nesta sessão (não tínhamos esses
artigos em `_fontes/`; sinalizado como tal).

Valores verificados nesta sessão com script Python, no próprio Breast
Cancer Wisconsin, 30 sorteios aleatórios de subconjuntos de colunas por
$d$, ponto de consulta aleatório, features padronizadas ($z$-score),
distância Euclidiana:

| $d$ | Contraste relativo médio |
|---|---|
| 2 | $\approx 221$ |
| 5 | $\approx 28$ |
| 10 | $\approx 14$ |
| 20 | $\approx 11$ |
| 30 | $\approx 10$ |

## Pendências e notas

- **DLFC (Bishop & Bishop, 2024)** foi buscado nesta sessão para o
  mesmo conteúdo — só menciona "curse of dimensionality" de forma
  passageira (Cap. 6, sem o mesmo desenvolvimento de PRML/ESL) e usa
  "cosine similarity" só no contexto de aprendizado contrastivo (fora
  do escopo desta aula). Não usado.
- Os valores de $d_K$/densidade por $k$-NN e os picos de KDE citados no
  plano de aula (`_00-plano-aula.md`) foram verificados por script antes
  de escrever `index.qmd` — números reais do dataset, não inventados;
  reproduzidos com o mesmo `rng` (seed) dentro do `.qmd` para
  consistência entre o texto e as figuras geradas.
