## Resumo — Aula 5

A Aula 5 resolve a pendência explícita deixada pelo Fechamento da Aula 4:
autovalores/autovetores reais, na forma garantida pelo Teorema Espectral
Real, só existem incondicionalmente para matrizes **quadradas
simétricas** — $X^TX$ sempre se encaixa aí, mas $X$ em si (a matriz de
design, $N\ne d$) não. A Decomposição em Valores Singulares (SVD)
generaliza a decomposição espectral para **qualquer** matriz retangular,
constrói-se diretamente a partir do Teorema Espectral aplicado a $X^TX$ e
$XX^T$ (ferramenta já disponível desde a Aula 4), e abre duas aplicações
centrais de ML: (1) aproximação de matrizes por outras de posto menor,
com garantia de otimalidade (Teorema de Eckart-Young-Mirsky) — a
matemática por trás de PCA (Aprendizado Não Supervisionado) e de sistemas
de recomendação/filtragem colaborativa; e (2) a Decomposição Polar, que
nasce "de graça" rearranjando os três fatores da SVD, e reaparece como
peça central da Aula 14 (ortogonalização de matrizes de atualização via
iteração de Newton-Schulz, Shampoo/Muon).

**Objetivos de aprendizagem:** (a) enunciar e justificar por que a SVD
existe para qualquer matriz retangular; (b) construir a SVD a partir do
Teorema Espectral aplicado a $A^TA$/$AA^T$; (c) calcular e interpretar
aproximações de posto-$k$, com o Teorema de Eckart-Young-Mirsky como
garantia de otimalidade; (d) derivar a Decomposição Polar a partir dos
três fatores da SVD e explicar a relação entre as duas decomposições.

**Pré-requisitos** (dicionário de notações, Aula 4): Teorema Espectral
Real ($A=Q\Lambda Q^T$ para $A$ simétrica), definitude
positiva/semidefinida, $X^TX$ como matriz simétrica PSD para qualquer
$X$, número de condição $\text{cond}(A)=\lambda_{\max}/\lambda_{\min}$
(caso simétrico). Também usa posto/independência linear (Aula 2),
produto interno/norma e a desigualdade de Cauchy-Schwarz (Aula 1), e o
dataset-fio California Housing ($X\in\mathbb{R}^{16\,640\times 4}$,
colunas `MedInc`, `HouseAge`, `AveRooms`, `AveBedrms`) usado desde a
Aula 1.

**Estratégia Pedagógica:** Estratégia B (Inside-Out com Problema-Fio) —
aula de fundamentação matemática/decomposição matricial, exatamente o
caso de uso que o `CLAUDE.md` lista para a Estratégia B
("Representações Matriciais [...] SVD/Decomposição").

## Plano de aula — Aula 5 (carga horária real da turma: ~100min)

1. **Revisão e Introdução** (~12 min) — Revisão rápida do Teorema
   Espectral Real e por que ele não se aplica a $X$ diretamente (retomando
   o TikZ de fechamento da Aula 4); Ideia Central: tudo que sabemos sobre
   autovalores de matrizes simétricas pode ser reciclado, aplicando-o a
   $X^TX$ e $XX^T$ em vez de a $X$; Roteiro explícito (4 perguntas);
   Problema motivador com a matriz pequena de notas de filmes (3
   espectadores, 4 filmes — MathML Exemplo 4.14, traduzida) perguntando
   "existe uma estrutura escondida (gêneros/perfis) por trás dessas
   notas?"; Pausa Ativa 1.

2. **Intuição Geométrica da SVD** (~10 min) — a SVD como composição de
   três transformações sequenciais (rotação $V^T$ no domínio, escala
   $\Sigma$, rotação $U$ no codomínio), com figura de grade de vetores em
   $\mathbb{R}^2\to\mathbb{R}^2$ (reaproveitando a mesma lógica visual da
   Aula 4, Bloco 2, agora sem exigir simetria); TikZ do "pipeline"
   $V^T\to\Sigma\to U$. Pausa Ativa 2.

3. **Construção Formal da SVD a partir do Teorema Espectral** (~18 min) —
   sobe o rigor: Premissas ($A^TA$ e $AA^T$ são simétricas PSD, Aula 4);
   passo a passo (autovetores de $A^TA$ como $V$, autovalores
   $\sigma_i^2=\lambda_i$, vetores singulares à esquerda como imagem
   normalizada $u_i=Av_i/\sigma_i$, prova de ortogonalidade de $Av_i$
   usando a relação de autovalor, equação de valor singular
   $Av_i=\sigma_i u_i$); Teorema da SVD (MathML Teo. 4.22) enunciado
   formalmente; exemplo numérico resolvido à mão ($2\times 3$, MathML
   Exemplo 4.13), verificado com `np.linalg.svd`. Pausa Ativa 3.

4. **A SVD do Dataset-Fio: $X$ do California Housing** (~12 min) — SVD
   completa de $X$ ($16\,640\times 4$), conexão explícita
   $\sigma_i^2=\lambda_i(X^TX)$ com os autovalores já calculados na
   Aula 4 (valores idênticos, verificado numericamente); número de
   condição de $X$ ($\sigma_{\max}/\sigma_{\min}$) vs. de $X^TX$
   ($\sigma_{\max}^2/\sigma_{\min}^2$) — fecha o ciclo aberto no
   Fechamento da Aula 4 (a definição do Boyd usava $\sigma$, não
   $\lambda$). Pausa Ativa 4.

5. **Aproximação de Baixo Posto e o Teorema de Eckart-Young-Mirsky**
   (~18 min) — matrizes de posto 1 $A_i=\sigma_iu_iv_i^T$, soma
   $A=\sum\sigma_iA_i$, aproximação de posto-$k$ truncada
   $\hat{A}^{(k)}$; norma espectral (MathML Def. 4.23) e Teorema 4.24
   ($\|A\|_2=\sigma_1$); Teorema de Eckart-Young-Mirsky (MathML Teo.
   4.25) enunciado com hipótese e tese completas, prova (via
   Cauchy-Schwarz — Aula 1 — e o Teorema do Núcleo e da Imagem, citado);
   aplicado a $X$ (erro de aproximação $=\sigma_{k+1}$, verificado
   numericamente para $k=1,2,3$) e ao exemplo de notas de filmes
   (retomando o Problema Motivador — interpretação de filtragem
   colaborativa: $u_i$ como "filme estereotípico", $v_i$ como
   "espectador estereotípico"). Pausa Ativa 5.

6. **Decomposição Polar** (~10 min) — a partir de $A=U\Sigma V^T$,
   definir $Q:=UV^T$ (ortogonal — prova direta) e $S:=V\Sigma V^T$
   (simétrica semidefinida positiva — prova direta), mostrando
   $A=QS$; interpretação geométrica (rotação/reflexão pura $Q$, depois
   escala ao longo de eixos ortogonais $S$ — generalização do módulo e
   fase de um número complexo); ponte breve, sem desenvolver, para a
   Aula 14 (ortogonalização de matrizes de atualização via iteração de
   Newton-Schulz, Shampoo/Muon).

7. **Fechamento e Ponte para a Aula 6** (~10 min) — retomar as 4
   perguntas do Roteiro; nomear o que fica aberto: a SVD decompõe uma
   matriz estática, mas o problema central de otimização em ML é
   encontrar os parâmetros $\beta$ que minimizam uma função de perda —
   isso exige poder medir *como* a perda muda quando $\beta$ muda, o que
   pede um objeto novo (derivada em várias variáveis), tema da Aula 6.

**Fontes usadas — Aula 5**

### Fonte 1 — MathML, Teorema 4.22 (SVD Theorem), p. 119 (PDF p. 125)
**Uso pretendido:** enunciado formal do Teorema da SVD (Bloco 3).

**Trecho:**
> "Theorem 4.22 (SVD Theorem). Let A ∈ Rm×n be a rectangular matrix of
> rank r ∈ [0, min(m, n)]. The SVD of A is a decomposition of the form
> [...] with an orthogonal matrix U ∈ Rm×m with column vectors ui,
> i = 1, . . . , m, and an orthogonal matrix V ∈ Rn×n with column vectors
> vj , j = 1, . . . , n. Moreover, Σ is an m × n matrix with Σii = σi ⩾ 0
> and Σij = 0, i ≠ j."
>
> "Remark. The SVD exists for any matrix A ∈ Rm×n."

### Fonte 2 — MathML, §4.5.2 "Construction of the SVD", pp. 122-125 (PDF pp. 128-131)
**Uso pretendido:** derivação passo a passo da SVD a partir do Teorema
Espectral aplicado a $A^TA$/$AA^T$ (Bloco 3).

**Trecho:**
> "The spectral theorem (Theorem 4.15) tells us that the eigenvectors of
> a symmetric matrix form an ONB, which also means it can be
> diagonalized. Moreover, from Theorem 4.14 we can always construct a
> symmetric, positive semidefinite matrix A⊤A ∈ Rn×n from any
> rectangular matrix A ∈ Rm×n."
>
> "For any two orthogonal eigenvectors vi, vj , i ≠ j, it holds that
> (Avi)⊤(Avj) = vi⊤(A⊤A)vj = vi⊤(λjvj) = λjvi⊤vj = 0."
>
> "ui := Avi/∥Avi∥ = (1/√λi)Avi = (1/σi)Avi [...] Let us rearrange (4.78)
> to obtain the singular value equation Avi = σiui, i = 1, . . . , r."

### Fonte 3 — MathML, Exemplo 4.13 "Computing the SVD", pp. 125-126 (PDF pp. 131-132)
**Uso pretendido:** exemplo numérico resolvido à mão, $A\in\mathbb{R}^{2
\times 3}$ (Bloco 3), verificado com `np.linalg.svd`.

**Trecho:**
> "Let us find the singular value decomposition of A = [[1,0,1],[-2,1,0]]
> [...] Step 1: Right-singular vectors as the eigenbasis of A⊤A. [...]
> Step 2: Singular-value matrix. [...] since rk(A) = 2, there are only
> two nonzero singular values: σ1 = √6 and σ2 = 1."

### Fonte 4 — MathML, Definição 4.23 (Spectral Norm) e Teorema 4.24, p. 131 (PDF p. 137)
**Uso pretendido:** norma espectral e sua caracterização via maior valor
singular (Bloco 5, base para o Teorema de Eckart-Young).

**Trecho:**
> "Definition 4.23 (Spectral Norm of a Matrix). For x ∈ Rn\{0}, the
> spectral norm of a matrix A ∈ Rm×n is defined as ∥A∥2 := maxx
> ∥Ax∥2/∥x∥2."
>
> "Theorem 4.24. The spectral norm of A is its largest singular value σ1.
> We leave the proof of this theorem as an exercise."

### Fonte 5 — MathML, Teorema 4.25 (Eckart-Young Theorem), pp. 131-132 (PDF pp. 137-138)
**Uso pretendido:** enunciado e prova do Teorema de Eckart-Young-Mirsky
(Bloco 5) — hipótese e tese completas, mais o esboço de prova via
Cauchy-Schwarz e o Teorema do Núcleo e da Imagem.

**Trecho:**
> "Theorem 4.25 (Eckart-Young Theorem (Eckart and Young, 1936)). Consider
> a matrix A ∈ Rm×n of rank r and let B ∈ Rm×n be a matrix of rank k. For
> any k ⩽ r with Â(k) = Σi=1..k σiuivi⊤ it holds that Â(k) =
> argminrk(B)=k∥A − B∥2, ∥A − Â(k)∥2 = σk+1."
>
> "[...] by using a version of the Cauchy-Schwartz inequality (3.17) [...]
> ∥Ax∥2 ⩽ ∥A − B∥2∥x∥2 < σk+1∥x∥2. However, there exists a
> (k + 1)-dimensional subspace where ∥Ax∥2 ⩾ σk+1∥x∥2 [...] Adding up
> dimensions of these two spaces yields a number greater than n [...]
> This is a contradiction of the rank-nullity theorem (Theorem 2.24)."

### Fonte 6 — MathML, Exemplos 4.14-4.15 "Finding Structure in Movie Ratings and Consumers", pp. 127-128 e 132 (PDF pp. 133-134, 138)
**Uso pretendido:** Problema Motivador da Abertura e retomada no Bloco 5
(interpretação de filtragem colaborativa — $u_i$/$v_i$ como "filme
estereotípico"/"espectador estereotípico").

**Trecho:**
> "Consider three viewers (Ali, Beatrix, Chandra) rating four different
> movies (Star Wars, Blade Runner, Amelie, Delicatessen). [...] We
> interpret the left-singular vectors ui as stereotypical movies and the
> right-singular vectors vj as stereotypical viewers."
>
> "[...] by using only the first singular value term in a rank-1
> decomposition of the movie-rating matrix [...] This first rank-1
> approximation A1 is insightful: it tells us that Ali and Beatrix like
> science fiction movies [...] but fails to capture the ratings of the
> other movies by Chandra."

### Fonte 7 — MathML, "full SVD"/"reduced SVD"/"truncated SVD", p. 128-129 (PDF p. 134-135)
**Uso pretendido:** vocabulário (SVD completa vs. reduzida vs. truncada)
usado ao longo dos Blocos 3-5.

**Trecho:**
> "Our definition (4.64) for the SVD is sometimes called the full SVD.
> [...] Sometimes this formulation is called the reduced SVD [...] In
> Section 4.6, we will learn about matrix approximation techniques using
> the SVD, which is also called the truncated SVD."

**Nota de exposição própria (Bloco 6 — Decomposição Polar):** nenhuma
das três fontes desta disciplina (`mathml.pdf`, `copt.pdf`, `optml.pdf`)
contém uma seção dedicada à Decomposição Polar — buscado
explicitamente, sem ocorrência. O Bloco 6 é, portanto, uma derivação
nossa (não uma citação), construída diretamente a partir do Teorema 4.22
já estabelecido: dado $A=U\Sigma V^T$, definimos $Q:=UV^T$ e
$S:=V\Sigma V^T$, e provamos por conta própria que $Q$ é ortogonal e $S$
é simétrica semidefinida positiva — sinalizado explicitamente como tal
no `index.qmd`.

**Nota de exposição própria (Bloco 4 — derivada direcional não se
aplica aqui, mas registrada para a Aula 6):** não há pendência de fonte
para a Aula 5.
