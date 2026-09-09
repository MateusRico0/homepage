## Resumo — Aula 4

A Aula 3 fechou com uma promessa explícita: o número de condição de
$X^TX$ — usado ali de forma só empírica (perturbar os dados, medir o
efeito no peso estimado) — teria, na Aula 4, "a ferramenta exata para
medi-lo diretamente a partir da estrutura de $X^TX$ (seus autovalores e
autovetores), sem precisar perturbar nada". Esta aula cumpre exatamente
essa promessa: introduz autovalores e autovetores do zero (intuição
geométrica → polinômio característico → cálculo à mão), prova o Teorema
Espectral Real para matrizes simétricas (autovalores reais, autobase
ortonormal), define definitude positiva via o sinal dos autovalores
(conectando com a forma quadrática $x^TAx$ já vista na Aula 1), e fecha
recalculando — agora exatamente, via autovalores — os mesmos números de
condição que a Aula 3 só tinha estimado por perturbação (23.460,5 para
$X^TX$ completo; 419,8 para o par quase-colinear
`AveRooms`/`AveBedrms`; 169,1 para o par bem-condicionado
`MedInc`/`HouseAge`). Pré-requisitos: matriz de design $X$, posto,
produto interno/forma quadrática $x^TAx$ (Aula 1), subespaços,
complemento ortogonal $U^\perp$, projeção ortogonal e Equações Normais
$X^TX\hat{\mathbf{w}}=X^T\mathbf{y}$ (Aula 3) — todos reutilizados
diretamente, nenhuma notação nova incompatível introduzida.

**Notação nova introduzida nesta aula** (para o dicionário de
`_progresso.md`): autovalor $\lambda$, autovetor $\mathbf{x}$ (equação
$A\mathbf{x}=\lambda\mathbf{x}$), polinômio característico
$p_A(\lambda)=\det(A-\lambda I)$, autoespaço $E_\lambda$, multiplicidade
algébrica/geométrica, matriz diagonalizável $A=PDP^{-1}$, decomposição
espectral de matriz simétrica $A=Q\Lambda Q^T$ ($Q$ ortogonal), matriz
positiva (semi)definida $A\succ 0$/$A\succeq 0$, quociente de Rayleigh
$\mathbf{x}^TA\mathbf{x}/\mathbf{x}^T\mathbf{x}$, número de condição
$\text{cond}(A)=\lambda_{\max}(A)/\lambda_{\min}(A)$ (matrizes simétricas
PSD).

**Estratégia Pedagógica:** Estratégia B (Inside-Out com Problema-Fio) —
é uma aula de fundação matemática de linguagem/representação
(autovalores/autovetores como uma nova forma de caracterizar uma matriz
e sua transformação linear associada), na mesma família de Aulas 1-3;
o problema-fio (o número de condição deixado em aberto na Aula 3) guia
a aula do início ao fim, com a "necessidade do idioma matemático"
vindo antes do formalismo em cada bloco.

## Plano de aula — Aula 4 (carga horária real da turma: ~100min)

1. **Revisão e Introdução** (~12 min) — Revisão rápida da Aula 3
   (projeção, Equações Normais, o número de condição medido só
   empiricamente no Bloco 6); Organizador Prévio ("de perturbar os
   dados para olhar direto para dentro de $X^TX$"); Roteiro explícito
   (4 perguntas); Problema Motivador (os mesmos dois pares de atributos
   do California Housing, quase-colinear vs. bem-condicionado — dá para
   prever a fragilidade sem perturbar nada?); Pausa Ativa 1.

2. **Intuição: Autovetores como Direções que Não Giram** (~13 min) —
   sem fórmula ainda: uma matriz $2\times 2$ agindo sobre um círculo
   unitário/grade de vetores, a maioria dos vetores gira de direção, mas
   duas direções especiais só esticam/encolhem (nunca giram) — construído
   visualmente primeiro (matplotlib, matriz $A=\begin{bmatrix}4&2\\1&3
   \end{bmatrix}$ do MathML Exemplo 4.5, reaproveitada no Bloco 3 para o
   cálculo à mão). Nomeando informalmente "autovetor"/"autovalor" antes
   da equação formal. Observação plantada (não resolvida ainda): as duas
   direções não são perpendiculares uma à outra — isso muda para
   matrizes simétricas (gancho para o Bloco 4). Termina com a equação
   formal $A\mathbf{x}=\lambda\mathbf{x}$ (Definição 4.6, MathML).
   Pausa Ativa 2.

3. **O Polinômio Característico: Achando Autovalores e Autovetores à
   Mão** (~15 min) — Premissas → passo a passo: por que
   $A\mathbf{x}=\lambda\mathbf{x}$ vira $\det(A-\lambda I)=0$
   (Definição 4.5); exemplo resolvido completo à mão, a mesma matriz
   $A=\begin{bmatrix}4&2\\1&3\end{bmatrix}$ do Bloco 2 (MathML Exemplo
   4.5: polinômio, raízes $\lambda=2,5$, autovetores $(2,1)$ e
   $(1,-1)$, confirmando visualmente as duas direções do Bloco 2);
   verificação numérica com `numpy.linalg.eig`. Observação de não-
   unicidade do autovetor (qualquer múltiplo escalar serve). Pausa
   Ativa 3.

4. **O Teorema Espectral Real para Matrizes Simétricas** (~18 min) —
   Premissa central: $X^TX$ (Aula 3) é sempre simétrica — e o Teorema
   4.14 do MathML garante que é sempre semidefinida positiva também.
   Prova curta e própria (não do livro, sinalizada como nossa) de que
   autovetores de autovalores distintos de uma matriz simétrica são
   automaticamente ortogonais (usando $\mathbf{x}_1^TA\mathbf{x}_2$ dos
   dois lados); enunciado do Teorema Espectral Real (MathML Teorema
   4.15 + Boyd Apêndice A.5.2, $A=Q\Lambda Q^T$, $Q$ ortogonal);
   contraste direto com o Bloco 3 (a matriz não-simétrica tinha
   autovetores não-ortogonais; a simétrica, sim) via exemplo resolvido
   à mão (MathML Exemplo 4.11, $A=\frac12\begin{bmatrix}5&-2\\-2&5
   \end{bmatrix}$, autovalores $7/2,3/2$, autovetores ortonormais).
   Menção breve (sem aprofundar) ao caso de autovalores repetidos
   precisando de Gram-Schmidt (MathML Exemplo 4.8). Decomposição
   espectral geral $A=PDP^{-1}$ (Teorema 4.20) especializada para o caso
   ortogonal simétrico. Pausa Ativa 4.

5. **Definitude Positiva: o Sinal dos Autovalores** (~15 min) —
   Retomando a forma quadrática $x^TAx$ da Aula 1: definição de matriz
   positiva (semi)definida via o sinal de $x^TAx$ (MathML Definição
   3.4, com os dois exemplos resolvidos $A_1$/$A_2$ da própria fonte);
   ponte para a caracterização equivalente via autovalores (Boyd
   Apêndice A.5.2: $A\succ 0 \iff \lambda_{\min}(A)>0$), verificada
   numericamente nos mesmos $A_1$/$A_2$; quociente de Rayleigh
   ($\lambda_{\min}(A)\mathbf{x}^T\mathbf{x}\le\mathbf{x}^TA\mathbf{x}
   \le\lambda_{\max}(A)\mathbf{x}^T\mathbf{x}$, Boyd) como a peça que
   finalmente define o número de condição
   $\text{cond}(A)=\lambda_{\max}(A)/\lambda_{\min}(A)$ de forma exata
   — fechando o ciclo aberto na Aula 3. Ponte explícita (sem
   aprofundar) para Hessiana/convexidade, tema da Aula 7. Pausa Ativa 5.

6. **Aplicação e Verificação no Dado Real** (~20 min) — Reaproveitando
   $X^TX$ da Aula 3 (mesmos 4 atributos e os dois pares de 20 bairros):
   calcular os autovalores exatos de cada $X^TX$ via
   `numpy.linalg.eigh` e confirmar que a razão $\lambda_{\max}/
   \lambda_{\min}$ reproduz, número por número, os condicionamentos que
   a Aula 3 só tinha medido via `np.linalg.cond` e perturbação — fecha
   o ciclo prometido. Em seguida, uma segunda matriz simétrica PSD, de
   natureza diferente: a matriz de covariância empírica de
   `AveRooms`/`AveBedrms` (não mais $X^TX$ bruta, mas centrada) —
   verificar simetria, autodecompor via `eigh`, confirmar ortogonalidade
   dos autovetores, e interpretar o autovetor principal geometricamente
   sobre o dispersão real das duas variáveis (a direção de maior
   variância dos dados) — semente explícita, sem aprofundar, para PCA
   (Aula 5/disciplina de Aprendizado Não Supervisionado). Aviso honesto
   sobre sensibilidade de escala (a covariância dos 4 atributos brutos é
   dominada por `HouseAge`, de maior variância numérica bruta — motiva
   padronização antes de PCA, sem ensinar PCA aqui).

7. **Fechamento e Ponte para a Aula 5** (~7 min) — Retomando as 4
   perguntas de abertura; o que fica em aberto: autovalores/autovetores
   só existem (na forma real) garantidamente para matrizes quadradas
   simétricas — o que fazer com uma matriz de design $X$ retangular,
   não-quadrada? Ponte para a Decomposição em Valores Singulares (SVD),
   Aula 5.

## Fontes usadas — Aula 4

### Fonte 1: MathML, §3.2.3, Definição 3.4 e Exemplo 3.4, p. 74
**Uso pretendido:** definição de matriz simétrica positiva (semi)definida
via a forma quadrática $x^TAx$, com os dois exemplos resolvidos usados
no Bloco 5.

**Trecho:**
> "Definition 3.4 (Symmetric, Positive Definite Matrix). A symmetric
> matrix A ∈ R^(n×n) that satisfies (3.11) is called symmetric, positive
> definite, or just positive definite. If only ⩾ holds in (3.11), then A
> is called symmetric, positive semidefinite."
>
> "Example 3.4 (Symmetric, Positive Definite Matrices) Consider the
> matrices A1 = [[9,6],[6,5]], A2 = [[9,6],[6,3]]. A1 is positive
> definite because it is symmetric and x^T A1 x = 9x1^2+12x1x2+5x2^2 =
> (3x1+2x2)^2+x2^2 > 0 for all x ∈ V\{0}. In contrast, A2 is symmetric
> but not positive definite because x^T A2 x = 9x1^2+12x1x2+3x2^2 =
> (3x1+2x2)^2−x2^2 can be less than 0, e.g., for x = [2,−3]^T."

---

### Fonte 2: MathML, §4.1, Definição 4.5 (Characteristic Polynomial), p. 104
**Uso pretendido:** definição formal do polinômio característico, base
da derivação do Bloco 3.

**Trecho:**
> "Definition 4.5 (Characteristic Polynomial). For λ ∈ R and a square
> matrix A ∈ R^(n×n) p_A(λ) := det(A − λI) = c0 + c1λ + c2λ^2 + ··· +
> c_(n−1)λ^(n−1) + (−1)^n λ^n, c0, . . . , c_(n−1) ∈ R, is the
> characteristic polynomial of A."

---

### Fonte 3: MathML, §4.2, Definição 4.6 e observação de não-unicidade, p. 105
**Uso pretendido:** equação de autovalor, formalização da intuição do
Bloco 2, e a observação de que qualquer múltiplo escalar de um
autovetor também é autovetor.

**Trecho:**
> "Definition 4.6. Let A ∈ R^(n×n) be a square matrix. Then λ ∈ R is an
> eigenvalue of A and x ∈ R^n\{0} is the corresponding eigenvector of A
> if Ax = λx. We call (4.25) the eigenvalue equation."
>
> "Remark (Non-uniqueness of eigenvectors). If x is an eigenvector of A
> associated with eigenvalue λ, then for any c ∈ R\{0} it holds that cx
> is an eigenvector of A with the same eigenvalue since A(cx) = cAx =
> cλx = λ(cx). Thus, all vectors that are collinear to x are also
> eigenvectors of A."

---

### Fonte 4: MathML, §4.2, Teorema 4.8 e observação geométrica, p. 106
**Uso pretendido:** equivalência entre autovalor e raiz do polinômio
característico; a leitura geométrica de "esticar" e "inverter direção"
usada na Intuição do Bloco 2; menção de que matrizes simétricas positivas
definidas sempre têm autovalores reais e positivos (ponte para o Bloco 5).

**Trecho:**
> "Theorem 4.8. λ ∈ R is an eigenvalue of A ∈ R^(n×n) if and only if λ
> is a root of the characteristic polynomial p_A(λ) of A."
>
> "Geometrically, the eigenvector corresponding to a nonzero eigenvalue
> points in a direction that is stretched by the linear mapping. The
> eigenvalue is the factor by which it is stretched. If the eigenvalue
> is negative, the direction of the stretching is flipped."
>
> "Symmetric, positive definite matrices always have positive, real
> eigenvalues."

---

### Fonte 5: MathML, §4.2, Exemplo 4.5 (Computing Eigenvalues, Eigenvectors, and Eigenspaces), p. 107
**Uso pretendido:** exemplo resolvido à mão, passo a passo, reaproveitado
tanto na Intuição visual (Bloco 2) quanto no cálculo formal (Bloco 3).

**Trecho:**
> "Let us find the eigenvalues and eigenvectors of the 2 × 2 matrix A =
> [[4,2],[1,3]]. [...] The characteristic polynomial is p_A(λ) =
> det(A − λI) = (4 − λ)(3 − λ) − 2 · 1. We factorize the characteristic
> polynomial and obtain p(λ) = (4−λ)(3−λ)−2·1 = 10−7λ+λ^2 = (2−λ)(5−λ)
> giving the roots λ1 = 2 and λ2 = 5. [...] For λ = 5 we obtain [...] a
> solution space E5 = span([2,1])."

---

### Fonte 6: MathML, §4.2, Figura 4.4 e discussão geométrica, p. 108-110
**Uso pretendido:** inspiração direta para a figura da Intuição (Bloco
2) — matriz agindo sobre uma grade/círculo de pontos, eigenvetores como
as direções que só esticam/comprimem.

**Trecho:**
> "Let us gain some intuition for determinants, eigenvectors, and
> eigenvalues using five different transformation matrices A1, . . . ,
> A5 and their impact on a square grid of points, centered at the
> origin: A1 = [[1/2,0],[0,2]]. The direction of the two eigenvectors
> correspond to the canonical basis vectors in R^2, i.e., to two
> cardinal axes. The vertical axis is extended by a factor of 2
> (eigenvalue λ1 = 2), and the horizontal axis is compressed by factor
> 1/2 (eigenvalue λ2 = 1/2)."

---

### Fonte 7: MathML, §4.2, Teorema 4.14 e Teorema 4.15 (Spectral Theorem), p. 111
**Uso pretendido:** a peça que conecta diretamente com $X^TX$ da Aula
3 (Teorema 4.14) e o enunciado formal do Teorema Espectral Real (Teorema
4.15), núcleo do Bloco 4.

**Trecho:**
> "Theorem 4.14. Given a matrix A ∈ R^(m×n), we can always obtain a
> symmetric, positive semidefinite matrix S ∈ R^(n×n) by defining S :=
> A^T A. Remark. If rk(A) = n, then S := A^T A is symmetric, positive
> definite."
>
> "Theorem 4.15 (Spectral Theorem). If A ∈ R^(n×n) is symmetric, there
> exists an orthonormal basis of the corresponding vector space V
> consisting of eigenvectors of A, and each eigenvalue is real."

---

### Fonte 8: MathML, §4.2, Exemplo 4.11 (Eigendecomposition), p. 117-118
**Uso pretendido:** exemplo resolvido de decomposição espectral de uma
matriz simétrica, contrastado no Bloco 4 com o Exemplo 4.5 (não-simétrico,
Fonte 5) — autovetores ortonormais.

**Trecho:**
> "Let us compute the eigendecomposition of A = (1/2)[[5,−2],[−2,5]].
> [...] the eigenvalues of A are λ1 = 7/2 and λ2 = 3/2 [...] p1 =
> (1/√2)[1,−1], p2 = (1/√2)[1,1]."

---

### Fonte 9: MathML, §4.4, Teorema 4.20 (Eigendecomposition) e Teorema 4.21, p. 116-117
**Uso pretendido:** decomposição espectral geral $A=PDP^{-1}$ e o caso
especial (sempre possível) para matrizes simétricas, base formal do
Bloco 4.

**Trecho:**
> "Theorem 4.20 (Eigendecomposition). A square matrix A ∈ R^(n×n) can
> be factored into A = PDP^(−1), where P ∈ R^(n×n) and D is a diagonal
> matrix whose diagonal entries are the eigenvalues of A, if and only if
> the eigenvectors of A form a basis of R^n."
>
> "Theorem 4.21. A symmetric matrix S ∈ R^(n×n) can always be
> diagonalized. [...] the spectral theorem states that we can find an
> ONB of eigenvectors of R^n. This makes P an orthogonal matrix so that
> D = P^T AP."

---

### Fonte 10: Boyd & Vandenberghe (Convex Optimization), §2.2.2, p. 30
**Uso pretendido:** a elipse/elipsoide com semieixos iguais à raiz
quadrada dos autovalores — ligação direta entre autovalor e a figura
"círculo vira elipse" da Intuição/Aplicação (Blocos 2 e 6).

**Trecho:**
> "A related family of convex sets is the ellipsoids, which have the
> form E = {x | (x − xc)^T P^(−1) (x − xc) ≤ 1}, where P = P^T ≻ 0,
> i.e., P is symmetric and positive definite. [...] The matrix P
> determines how far the ellipsoid extends in every direction from xc;
> the lengths of the semi-axes of E are given by √λi, where λi are the
> eigenvalues of P."

---

### Fonte 11: Boyd & Vandenberghe, Apêndice A.5.2 (Symmetric eigenvalue decomposition) e "Definiteness and matrix inequalities", p. 646-647
**Uso pretendido:** segunda formulação (independente do MathML) do
Teorema Espectral, mais a caracterização exata de definitude positiva via
autovalores e o quociente de Rayleigh — a peça central do Bloco 5 que
fecha o ciclo do número de condição aberto na Aula 3.

**Trecho:**
> "Suppose A ∈ S^n, i.e., A is a real symmetric n × n matrix. Then A can
> be factored as A = QΛQ^T, where Q ∈ R^(n×n) is orthogonal [...] and
> Λ = diag(λ1, . . . , λn)."
>
> "The largest and smallest eigenvalues satisfy λmax(A) = sup_(x≠0)
> x^T Ax / x^T x, λmin(A) = inf_(x≠0) x^T Ax / x^T x. In particular, for
> any x, we have λmin(A) x^T x ≤ x^T Ax ≤ λmax(A) x^T x [...] A matrix
> A ∈ S^n is called positive definite if for all x ≠ 0, x^T Ax > 0. [...]
> we see that A ≻ 0 if and only all its eigenvalues are positive, i.e.,
> λmin(A) > 0."

---

### Fonte 12: Boyd & Vandenberghe, Apêndice A.5.2, "condition number", p. 649
**Uso pretendido:** definição formal do número de condição, fechando
exatamente a promessa deixada em aberto pela Aula 3.

**Trecho:**
> "The condition number of a nonsingular A ∈ R^(n×n), denoted cond(A) or
> κ(A), is defined as cond(A) = ‖A‖2‖A^(−1)‖2 = σmax(A)/σmin(A)."

## Observações de precisão

- A prova de que autovetores de autovalores distintos de uma matriz
  simétrica são ortogonais (usada no Bloco 4) é **exposição nossa**,
  não uma citação literal do MathML ou do Boyd — ambos enunciam o
  Teorema Espectral diretamente, sem provar esse passo intermediário em
  detalhe no nível que este curso quer mostrar. A prova em si é padrão
  (manipulação de $\mathbf{x}_1^TA\mathbf{x}_2$ dos dois lados), mas
  sinalizada como nossa, não copiada.
- Os números do Bloco 6 (autovalores de $X^TX$, condicionamentos) foram
  todos calculados via script Python antes de escrever a aula, não
  fabricados — ver `_01-respostas.md`/registro em `_progresso.md` para
  os valores exatos.
