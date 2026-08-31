# Fontes usadas — Aula 3

> Trechos literais extraídos lendo diretamente as páginas do PDF (não
> reescritos de memória).
>
> - `../_fontes/esl.pdf` (Hastie, Tibshirani & Friedman, ESL, 2009):
>   offset **+19** confirmado nesta sessão (mesmo valor já usado nas
>   Aulas 1 e 2) — página impressa 507 = página 526 do PDF; página
>   impressa 520 = página 539 do PDF (`pdftotext -f <pdf> -l <pdf>`
>   confere o cabeçalho "520   14. Unsupervised Learning" na página
>   impressa 520).
> - `../_fontes/prml.pdf` (Bishop, PRML, 2006): offset **+20**
>   confirmado nesta sessão (mesmo valor já usado nas Aulas 1 e 2) —
>   página impressa 424 = página 444 do PDF.

---

### Fonte 1: ESL, §14.3.4 "Clustering Algorithms", p. 507
**Uso pretendido:** a taxonomia de três paradigmas de clustering —
combinatório (K-means/K-medoids), modelagem por mistura, e "mode
seeking"/densidade — usada na Abertura (Bloco 1) para situar o
contraste Outside-In (K-means, o "de fora") e no Bloco 3 (Conjuntos de
Nível de Densidade) para justificar a definição de cluster como região
de densidade alta ("mode seeking"), a tese central desta aula.

**Trecho:**
> "The goal of cluster analysis is to partition the observations into
> groups ('clusters') so that the pairwise dissimilarities between
> those assigned to the same cluster tend to be smaller than those in
> different clusters. Clustering algorithms fall into three distinct
> types: combinatorial algorithms, mixture modeling, and mode seeking.
> Combinatorial algorithms work directly on the observed data with no
> direct reference to an underlying probability model. Mixture
> modeling supposes that the data is an i.i.d sample from some
> population described by a probability density function. [...] Mode
> seekers ('bump hunters') take a nonparametric perspective, attempting
> to directly estimate distinct modes of the probability density
> function. Observations 'closest' to each respective mode then define
> the individual clusters." (p. 507)

---

### Fonte 2: ESL, §14.3.6 "K-means", pp. 509–510
**Uso pretendido:** a definição formal de K-means como algoritmo
combinatório baseado em distância euclidiana ao centróide, e a
Voronoi tessellation resultante da partição — o fato matemático
central que explica *por que* K-means corta uma lua/anel ao meio: toda
célula de Voronoi é convexa, então qualquer cluster não-convexo é
necessariamente fatiado por essas fronteiras retas. Usado na Abertura
(Bloco 1) e na Intuição (Bloco 2).

**Trecho:**
> "The K-means algorithm is one of the most popular iterative descent
> clustering methods. It is intended for situations in which all
> variables are of the quantitative type, and squared Euclidean
> distance $d(x_i,x_{i'}) = \sum_{j=1}^p (x_{ij}-x_{i'j})^2 =
> ||x_i-x_{i'}||^2$ is chosen as the dissimilarity measure." (p. 509)
>
> "Figure 14.6 shows some of the K-means iterations for the simulated
> data of Figure 14.4. The centroids are depicted by 'O's. The straight
> lines show the partitioning of points, each sector being the set of
> points closest to each centroid. This partitioning is called the
> *Voronoi tessellation*. After 20 iterations the procedure has
> converged." (p. 510)

---

### Fonte 3: PRML (Bishop, 2006), §9.1 "K-means Clustering", pp. 424–425
**Uso pretendido:** duplo registro com a Fonte 2 — a mesma regra de
atribuição (ponto vai para o centróide mais próximo), formalizada como
minimização da distorção $J$, Eq. (9.1)–(9.2). Usado na Abertura
(Bloco 1) para nomear com precisão o que "distância ao centróide"
significa antes de mostrar onde isso falha.

**Trecho:**
> "Our goal is to find an assignment of data points to clusters, as
> well as a set of vectors $\{\boldsymbol\mu_k\}$, such that the sum of
> the squares of the distances of each data point to its closest
> vector $\boldsymbol\mu_k$, is a minimum." (p. 424)
>
> "$$J = \sum_{n=1}^N \sum_{k=1}^K r_{nk} ||\mathbf{x}_n -
> \boldsymbol\mu_k||^2 \quad (9.1)$$ which represents the sum of the
> squares of the distances of each data point to its assigned vector
> $\boldsymbol\mu_k$." (p. 424)
>
> "$$r_{nk} = \begin{cases} 1 & \text{if } k = \arg\min_j
> ||\mathbf{x}_n - \boldsymbol\mu_j||^2 \\ 0 & \text{otherwise}
> \end{cases} \quad (9.2)$$ In other words, we simply assign the $n$th
> data point to the closest cluster centre." (p. 425)

---

### Fonte 4: ESL, §14.3.12 "Hierarchical Clustering", pp. 520–525
**Uso pretendido:** a definição de *single linkage* (Eq. 14.41), a
estrutura de dendrograma com $N-1$ níveis, o defeito de *chaining*, e
o argumento assintótico sobre single linkage não depender das
densidades $p_G, p_H$ — usados no Bloco 5 (MST e Clustering
Hierárquico Clássico) para introduzir single linkage antes de
conectá-lo à MST, e no Bloco 4 (alcançabilidade mútua) como contraste
("distância bruta" vs. distância que respeita densidade local).

**Trecho:**
> "Hierarchical clustering methods do not require [...] specifications
> [of the number of clusters and a starting configuration]. Instead,
> they require the user to specify a measure of dissimilarity between
> (disjoint) *groups* of observations, based on the pairwise
> dissimilarities among the observations in the two groups. [...] At
> the lowest level, each cluster contains a single observation. At the
> highest level there is only one cluster containing all of the data."
> (p. 520)
>
> "Agglomerative strategies start at the bottom and at each level
> recursively merge a selected pair of clusters into a single cluster.
> [...] The pair chosen for merging consist of the two groups with the
> smallest intergroup dissimilarity. [...] With both paradigms there
> are $N-1$ levels in the hierarchy." (pp. 520–521)
>
> "*Single linkage* (SL) agglomerative clustering takes the intergroup
> dissimilarity to be that of the closest (least dissimilar) pair
> $$d_{SL}(G,H) = \min_{i\in G, i'\in H} d_{ii'}. \quad (14.41)$$ This
> is also often called the *nearest-neighbor* technique." (p. 523)
>
> "Single linkage (14.41) only requires that a single dissimilarity
> $d_{ii'}$, $i\in G$ and $i'\in H$, be small for two groups $G$ and $H$
> to be considered close together, irrespective of the other
> observation dissimilarities between the groups. It will therefore
> have a tendency to combine, at relatively low thresholds, observations
> linked by a series of close intermediate observations. This
> phenomenon, referred to as *chaining*, is often considered a defect of
> the method." (p. 524)
>
> "As the sample size $N$ approaches infinity $d_{GA}(G,H)$ (14.43)
> approaches (14.45), which is a characteristic of the relationship
> between the two densities $p_G(x)$ and $p_H(x)$. For single linkage,
> $d_{SL}(G,H)$ (14.41) approaches zero as $N\to\infty$ independent of
> $p_G(x)$ and $p_H(x)$. [...] Thus, it is not clear what aspects of the
> population distribution are being estimated by $d_{SL}(G,H)$ and
> $d_{CL}(G,H)$." (p. 525)

---

## Achado sem citação de livro — sinalizado explicitamente

**HDBSCAN (Campello, Moulavi & Sander, 2013) e seus componentes —
*core distance*, *mutual reachability distance*, árvore condensada,
persistência por excesso de massa (*excess of mass*):** não coberto em
ESL, PRML nem DLFC (busca feita nesta sessão nos três PDFs por
"HDBSCAN", "mutual reachability", "condensed tree", "excess of mass",
"core distance" — nenhum resultado; os três livros antecedem a
publicação do algoritmo em 2013, ESL 2009/PRML 2006, e DLFC 2024 não o
inclui). Tratado como **síntese nossa, apoiada na descrição algorítmica
pública e amplamente documentada do método** — não uma citação literal
de um livro-texto que não discute o assunto. Onde útil, referenciamos a
descrição do algoritmo na documentação do scikit-learn
(`sklearn.cluster.HDBSCAN`, seção "How HDBSCAN Works" da documentação
oficial), citada como fonte não-livro, claramente identificada como
tal no `index.qmd`, nunca apresentada como trecho de PRML/ESL/DLFC.

A ligação entre "cortar as $k-1$ arestas mais pesadas da MST" e
"single linkage com $k$ clusters" é um resultado clássico de teoria de
grafos/clustering (não específico do HDBSCAN) — verificado
computacionalmente nesta sessão com um exemplo numérico pequeno (ver
`index.qmd`, Bloco 5), não extraído de nenhum PDF.

## Pendências e notas

- **DLFC (Bishop & Bishop, 2024)** foi buscado nesta sessão para
  "hierarchical clustering", "single linkage", "HDBSCAN", "mutual
  reachability" — sem cobertura substancial do assunto (o livro foca
  em deep learning; clustering clássico não é tratado em capítulo
  próprio). Não usado nesta aula.
- $d_K(\mathbf{x})$ (distância ao $K$-ésimo vizinho), reaproveitada
  aqui como *core distance*, já foi construída e citada como fonte na
  Aula 2 (PRML §2.5.2, pp. 124–127) — não recitada aqui; ver
  `../aula02/_01-fontes.md`.
- Os números do exemplo numérico da MST (Bloco 5) e da aplicação do
  HDBSCAN ao Breast Cancer Wisconsin (Bloco 6) foram verificados por
  script Python antes de escrever `index.qmd` — reproduzidos com o
  mesmo `rng` (seed) dentro do `.qmd` para consistência entre o texto e
  as figuras/números citados.
