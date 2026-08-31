# Fontes usadas — Aula 3

> Trechos literais extraídos em 2026-08-30 lendo diretamente as páginas do
> PDF nesta sessão (via `pdftotext -layout`, não reescritos de memória).
> Offset confirmado entre página impressa e página do PDF: **+6** (ex.: p. 79
> impressa = página 85 do PDF), o mesmo já usado nas Aulas 1–2 desta
> disciplina — reconfirmado aqui olhando o cabeçalho de cada página extraída
> ("79 ... Analytic Geometry" na página do PDF 85, e assim por diante).

---

### Fonte 1: MathML, §3.6 "Orthogonal Complement", p. 79
**Uso pretendido:** definição formal de complemento ortogonal $U^\perp$ e
da decomposição única $\mathbb{R}^N = U \oplus U^\perp$ — base do Bloco 3
(Subespaços e Complemento Ortogonal).

**Trecho:**
> "Consider a D-dimensional vector space V and an M-dimensional subspace
> U ⊆ V . Then its orthogonal complement U⊥ is a (D − M)-dimensional
> subspace of V and contains all vectors in V that are orthogonal to every
> vector in U. Furthermore, U ∩ U⊥ = {0} so that any vector x ∈ V can be
> uniquely decomposed into
>
> x = Σ(m=1 to M) λm bm + Σ(j=1 to D−M) ψj b⊥j , λm, ψj ∈ R,       (3.36)
>
> where (b1, . . . , bM) is a basis of U and (b⊥1 , . . . , b⊥D−M) is a basis
> of U⊥."

---

### Fonte 2: MathML, §3.6, p. 80 (normal vector, remark)
**Uso pretendido:** exemplo concreto de complemento ortogonal (o vetor
normal de um plano em $\mathbb{R}^3$) — usado no Bloco 3 para dar
intuição geométrica ao complemento ortogonal antes da definição abstrata.

**Trecho:**
> "Therefore, the orthogonal complement can also be used to describe a
> plane U (two-dimensional subspace) in a three-dimensional vector space.
> More specifically, the vector w with ∥w∥ = 1, which is orthogonal to the
> plane U, is the basis vector of U⊥. [...] All vectors that are orthogonal
> to w must (by construction) lie in the plane U. The vector w is called
> the normal vector of U."

---

### Fonte 3: MathML, §3.8 "Orthogonal Projections", Definition 3.10, p. 82
**Uso pretendido:** definição formal de projeção ($\pi^2=\pi$) — ponto de
partida do Bloco 4 (Teorema da Projeção), antes de derivar a fórmula
concreta.

**Trecho:**
> "Definition 3.10 (Projection). Let V be a vector space and U ⊆ V a
> subspace of V . A linear mapping π : V → U is called a projection if
> π² = π ◦ π = π."
>
> "Since linear mappings can be expressed by transformation matrices [...],
> the preceding definition applies equally to a special kind of
> transformation matrices, the projection matrices Pπ, which exhibit the
> property that P²π = Pπ."

---

### Fonte 4: MathML, §3.8.1 "Projection onto One-Dimensional Subspaces (Lines)", p. 82–83
**Uso pretendido:** a caracterização geométrica que abre a derivação do
Teorema da Projeção no Bloco 4 — "mais próximo" implica ortogonalidade do
resíduo ao subespaço — citada aqui no caso 1D antes de generalizar para
subespaços quaisquer (o caso que a aula usa, $U=\text{col}(X)$).

**Trecho:**
> "The projection πU(x) is closest to x, where 'closest' implies that the
> distance ∥x − πU(x)∥ is minimal. It follows that the segment πU(x) − x
> from πU(x) to x is orthogonal to U, and therefore the basis vector b of
> U. The orthogonality condition yields ⟨πU(x) − x, b⟩ = 0 since angles
> between vectors are defined via the inner product."
>
> "The projection πU(x) of x onto U must be an element of U and,
> therefore, a multiple of the basis vector b that spans U. Hence,
> πU(x) = λb, for some λ ∈ R."

---

### Fonte 5: MathML, §3.8.2 "Projection onto General Subspaces", pp. 85–86
**Uso pretendido:** a derivação passo a passo — da condição de
ortogonalidade $m$-dimensional até as **Equações Normais** — que o Bloco 4
desta aula segue de perto (adaptando a notação $B\to X$, $\lambda\to
\hat{\mathbf{w}}$, $x\to\mathbf{y}$).

**Trecho:**
> "Assume that (b1, . . . , bm) is an ordered basis of U. Any projection
> πU(x) onto U is necessarily an element of U. Therefore, they can be
> represented as linear combinations of the basis vectors b1, . . . , bm of
> U, such that πU(x) = Σ(i=1 to m) λi bi."
>
> "As in the 1D case, 'closest' means 'minimum distance', which implies
> that the vector connecting πU(x) ∈ U and x ∈ Rn must be orthogonal to
> all basis vectors of U. Therefore, we obtain m simultaneous conditions
> (assuming the dot product as the inner product)
>
> ⟨b1, x − πU(x)⟩ = b1ᵗ(x − πU(x)) = 0
> ...
> ⟨bm, x − πU(x)⟩ = bmᵗ(x − πU(x)) = 0"
>
> "which, with πU(x) = Bλ, can be written as [...] such that we obtain a
> homogeneous linear equation system
>
> b1ᵗ
> ...  (x − Bλ) = 0 ⇐⇒ Bᵗ(x − Bλ) = 0
> bmᵗ
>
> ⇐⇒ Bᵗ Bλ = Bᵗ x.
>
> The last expression is called normal equation. Since b1, . . . , bm are a
> basis of U and, therefore, linearly independent, BᵗB ∈ Rm×m is regular
> and can be inverted. This allows us to solve for the coefficients/
> coordinates
>
> λ = (BᵗB)⁻¹ Bᵗ x."

---

### Fonte 6: MathML, §3.8.2, p. 86–87 (projeção e matriz de projeção)
**Uso pretendido:** fecha a derivação do Bloco 4 — a partir de $\lambda$,
obter $\pi_U(x)=B\lambda$ e a matriz de projeção $P_\pi$ — usada para
nomear $\hat{\mathbf{y}}=X\hat{\mathbf{w}}$ como a projeção de
$\mathbf{y}$ sobre o espaço-coluna de $X$.

**Trecho:**
> "2. Find the projection πU(x) ∈ U. We already established that
> πU(x) = Bλ. Therefore, with (3.57)
>
> πU(x) = B(BᵗB)⁻¹ Bᵗ x.
>
> 3. Find the projection matrix Pπ. From (3.58), we can immediately see
> that the projection matrix that solves Pπx = πU(x) must be
>
> Pπ = B(BᵗB)⁻¹ Bᵗ."

---

### Fonte 7: MathML, §3.8.2, p. 88 (projeções e sistemas sem solução — a ponte para regressão)
**Uso pretendido:** a ponte explícita, no próprio livro, entre "sistema
$A\mathbf{x}=\mathbf{b}$ sem solução" (Aula 2 desta disciplina) e "projeção
ortogonal como melhor aproximação" — usada na Abertura (Bloco 1) e no
Fechamento (Bloco 7) para justificar por que este é exatamente o problema
que a Aula 2 deixou aberto.

**Trecho:**
> "Projections allow us to look at situations where we have a linear
> system Ax = b without a solution. Recall that this means that b does not
> lie in the span of A, i.e., the vector b does not lie in the subspace
> spanned by the columns of A. Given that the linear equation cannot be
> solved exactly, we can find an approximate solution. The idea is to find
> the vector in the subspace spanned by the columns of A that is closest to
> b, i.e., we compute the orthogonal projection of b onto the subspace
> spanned by the columns of A. This problem arises often in practice, and
> the solution is called the least-squares solution (assuming the dot
> product as the inner product) of an overdetermined system."

---

## Pendências e notas

- A Fonte 5/6 usa a notação do livro ($B$, $\lambda$, $x$) para o caso
  geral de um subespaço $U$ com base $(b_1,\dots,b_m)$; no `index.qmd`
  desta aula, adaptamos essa mesma derivação para o caso específico da
  regressão ($B\to X$ a matriz de design, $\lambda\to\hat{\mathbf{w}}$ os
  pesos, $x\to\mathbf{y}$ o alvo observado) — é a mesma matemática, exposta
  com os nomes de variável já introduzidos nas Aulas 1–2 desta disciplina,
  não uma citação separada.
- O livro chama $(B^TB)^{-1}B^T$ de "pseudo-inversa" de $B$ (p. 86) — menção
  breve nossa no `index.qmd`, sem aprofundar (pseudo-inversa via SVD é
  assunto de aula futura, quando o curso chegar a decomposições).
- `copt.pdf` e `optml.pdf` seguem reservados para a Parte 2/3 do curso
  (Aulas 6+), não usados nesta aula.
- Os exemplos numéricos do livro (Example 3.10, 3.11 — projeção sobre uma
  reta e sobre um subespaço 2D em $\mathbb{R}^3$) não são citados
  literalmente aqui; são substituídos, no `index.qmd`, pelo exemplo real do
  California Housing (Bloco 5), seguindo a diretriz do projeto de preferir
  dados reais a exemplos de brinquedo.
