## Resumo — Aula 7

A Aula 6 terminou com a ressalva de que $\nabla L=\mathbf{0}$ identifica um ponto crítico, não necessariamente um mínimo. Esta aula passa à segunda ordem: define formalmente conjunto, conjunto convexo, função, função convexa e epígrafe, prova que $f$ é convexa se e somente se $\mathrm{epi}\,f$ é convexo, prova a condição de primeira ordem, introduz a Hessiana como matriz simétrica de curvatura e prova a condição de segunda ordem ($f$ convexa $\iff\nabla^2f\succeq0$). Aplica tudo à perda do problema-fio: $\nabla^2L=2X^TX$ e curvatura $2\|X\mathbf{v}\|^2$, com unicidade do minimizador se e somente se o posto coluna é completo. Fecha com a Ridge, que desloca os autovalores em $\lambda$ e garante existência e unicidade.

**Objetivos:** reconhecer quando um ponto crítico é mínimo global; ler convexidade nos autovalores da Hessiana; provar a convexidade da perda quadrática e da Ridge.
**Pré-requisitos:** gradiente-linha, regra da cadeia e $J_{\mathbf r}=X$ (Aula 6); $A\succeq0$, teorema espectral, Rayleigh (Aula 4); posto e núcleo (Aula 2); equações normais (Aula 3); $\text{cond}(X^TX)\approx23\,460{,}5$ (Aula 5).
**Dataset-fio:** California Housing, o mesmo $X$ de 4 colunas da Aula 6. Acrescenta-se a coluna derivada `AveOtherRooms = AveRooms − AveBedrms` para produzir um vale plano real: posto 4, núcleo gerado por $(0,0,-1,1,1)$.

**Estratégia Pedagógica:** B (Inside-Out com Problema-Fio) — aula de fundamentação matemática (convexidade, Hessiana) guiada pela pergunta que a Aula 6 deixou aberta.

## Plano de aula — Aula 7 (carga horária: ~110 min)

1. **Revisão e Introdução** (~12 min) — gradiente e ponto crítico (Aula 6), PSD e Rayleigh (Aula 4), posto e cond (Aulas 2, 3 e 5). Problema motivador: com `AveOtherRooms`, infinitos $\boldsymbol\beta$ com a mesma perda, e `np.linalg.solve` "resolve" sem erro. Pausa Ativa.
2. **Intuição — tigela, sela e vale plano** (~8 min) — três quadráticas 2D que diferem só no sinal dos autovalores.
3. **Bloco 1: convexidade e condição de 1ª ordem** (~30 min) — conjunto, segmento e combinação convexa; conjunto convexo e não convexo ("para todo" × "existe"), com semiespaço e bola provados convexos e anel e união refutados por contraexemplo; interseção preserva convexidade. Função (domínio + regra), gráfico, função convexa e não convexa ($x^2$ pela identidade $\theta(1-\theta)(x-y)^2$, $x^3$ por contraexemplo), fechamento por soma. Epígrafe e teorema "$f$ convexa $\iff$ $\mathrm{epi}\,f$ convexo" com prova nos dois sentidos; consequência: máximo de convexas ($|x|$, *hinge*). Teorema de 1ª ordem com prova, leitura pela epígrafe (hiperplano suporte), corolário "gradiente nulo ⇒ mínimo global". Pausa Ativa.
4. **Bloco 2: Hessiana e condição de 2ª ordem** (~22 min) — definição e simetria, curvatura ao longo de uma reta, teorema de 2ª ordem com prova (Taylor com resto de Lagrange), $x^4$ e $1/x^2$, quadráticas com Taylor exata e classificação de pontos críticos. Pausa Ativa.
5. **Bloco 3: a perda quadrática** (~18 min) — Hessiana $2X^TX$ por duas rotas, proposição de unicidade e conjunto de minimizadores, autovalores no dataset, figura do vale plano. Pausa Ativa.
6. **Bloco 4: Ridge** (~15 min) — Hessiana $2(X^TX+\lambda I)$, autovalores deslocados, lema de unicidade, existência, tabela no dataset. Pausa Ativa.
7. **Fechamento** (~5 min) — quatro perguntas; não convexidade e custo computacional em aberto. Ponte para a Aula 8 (descida do gradiente; autovalores da Hessiana e número de condição controlam o passo e a velocidade).

## Fontes usadas — Aula 7

Deslocamentos página impressa → PDF: `copt.pdf` +14; `mathml.pdf` +6 (conferidos nesta sessão).

### Fonte 1: Boyd & Vandenberghe, *Convex Optimization*, §2.1.4, p. 23
**Uso pretendido:** definição de conjunto convexo.

**Trecho:**
> "A set C is convex if the line segment between any two points in C lies in C, i.e., if for any x1, x2 ∈ C and any θ with 0 ≤ θ ≤ 1, we have θx1 + (1 − θ)x2 ∈ C."

### Fonte 1b: Boyd & Vandenberghe, §2.1.4 (Fig. 2.2), p. 24; §2.2.1, p. 27; §2.2.2, p. 30; §2.3.1, p. 36
**Uso pretendido:** exemplos de conjuntos convexos e não convexos; semiespaço e bola convexos; interseção preserva convexidade.

**Trechos:**
> "Figure 2.2 Some simple convex and nonconvex sets. Left. The hexagon, which includes its boundary (shown darker), is convex. Middle. The kidney shaped set is not convex, since the line segment between the two points in the set shown as dots is not contained in the set."

> "A (closed) halfspace is a set of the form {x | aT x ≤ b}, (2.1) where a ≠ 0, i.e., the solution set of one (nontrivial) linear inequality. Halfspaces are convex, but not affine."

> "A Euclidean ball is a convex set: if ‖x1 − xc‖2 ≤ r, ‖x2 − xc‖2 ≤ r, and 0 ≤ θ ≤ 1, then ‖θx1 + (1 − θ)x2 − xc‖2 = ‖θ(x1 − xc) + (1 − θ)(x2 − xc)‖2 ≤ θ‖x1 − xc‖2 + (1 − θ)‖x2 − xc‖2 ≤ r."

> "Convexity is preserved under intersection: if S1 and S2 are convex, then S1 ∩ S2 is convex."

### Fonte 1c: Deisenroth, Faisal & Ong, *Mathematics for Machine Learning*, §5 (introdução), pp. 139–140
**Uso pretendido:** definição de função.

**Trecho:**
> "We often write f : RD → R (5.1a) x ↦ f (x) (5.1b) to specify a function, where (5.1a) specifies that f is a mapping from RD to R and (5.1b) specifies the explicit assignment of an input x to a function value f (x). A function f assigns every input x exactly one function value f (x)."

### Fonte 1d: Boyd & Vandenberghe, §3.1.7, pp. 75–76; §3.2.3, pp. 80–81
**Uso pretendido:** gráfico e epígrafe; enunciado (sem prova no livro) de "$f$ convexa ⟺ epígrafe convexa"; hiperplano suporte; máximo de convexas via interseção de epígrafes.

**Trechos:**
> "The graph of a function f : Rn → R is defined as {(x, f (x)) | x ∈ dom f }, which is a subset of Rn+1 . The epigraph of a function f : Rn → R is defined as epi f = {(x, t) | x ∈ dom f, f (x) ≤ t}, which is a subset of Rn+1 . (‘Epi’ means ‘above’ so epigraph means ‘above the graph’.) [...] The link between convex sets and convex functions is via the epigraph: A function is convex if and only if its epigraph is a convex set."

> "This means that the hyperplane defined by (∇f (x), −1) supports epi f at the boundary point (x, f (x)); see figure 3.6."

> "If f1 and f2 are convex functions then their pointwise maximum f , defined by f (x) = max{f1 (x), f2 (x)}, with dom f = dom f1 ∩ dom f2 , is also convex."

### Fonte 2: Boyd & Vandenberghe, §3.1.1, p. 67
**Uso pretendido:** definição de função convexa, estrita e côncava; afins são convexas e côncavas.

**Trecho:**
> "A function f : Rn → R is convex if dom f is a convex set and if for all x, y ∈ dom f , and θ with 0 ≤ θ ≤ 1, we have f (θx + (1 − θ)y) ≤ θf (x) + (1 − θ)f (y). (3.1) Geometrically, this inequality means that the line segment between (x, f (x)) and (y, f (y)), which is the chord from x to y, lies above the graph of f (figure 3.1). A function f is strictly convex if strict inequality holds in (3.1) whenever x ≠ y and 0 < θ < 1. We say f is concave if −f is convex, and strictly concave if −f is strictly convex. For an affine function we always have equality in (3.1), so all affine (and therefore also linear) functions are both convex and concave."

### Fonte 3: Boyd & Vandenberghe, §3.1.3, pp. 69–70
**Uso pretendido:** teorema de 1ª ordem, sua prova e o corolário do gradiente nulo.

**Trecho:**
> "Suppose f is differentiable (i.e., its gradient ∇f exists at each point in dom f , which is open). Then f is convex if and only if dom f is convex and f (y) ≥ f (x) + ∇f (x)T (y − x) (3.2) holds for all x, y ∈ dom f . [...] The inequality (3.2) states that for a convex function, the first-order Taylor approximation is in fact a global underestimator of the function. [...] This is perhaps the most important property of convex functions [...]. As one simple example, the inequality (3.2) shows that if ∇f (x) = 0, then for all y ∈ dom f , f (y) ≥ f (x), i.e., x is a global minimizer of the function f ."

### Fonte 4: Boyd & Vandenberghe, §3.1.4, p. 71
**Uso pretendido:** teorema de 2ª ordem (prova deixada como exercício; a da aula é nossa), convexidade estrita parcial, contraexemplos $x^4$ e $1/x^2$, Exemplo 3.2 (quadráticas).

**Trecho:**
> "We now assume that f is twice differentiable, that is, its Hessian or second derivative ∇2 f exists at each point in dom f , which is open. Then f is convex if and only if dom f is convex and its Hessian is positive semidefinite: for all x ∈ dom f , ∇2 f (x) ⪰ 0. [...] We leave the proof of the second-order condition as an exercise (exercise 3.8). [...] If ∇2 f (x) ≻ 0 for all x ∈ dom f , then f is strictly convex. The converse, however, is not true: for example, the function f : R → R given by f (x) = x4 is strictly convex but has zero second derivative at x = 0. [...] Example 3.2 Quadratic functions. [...] f (x) = (1/2)xT P x + q T x + r, with P ∈ Sn [...]. Since ∇2 f (x) = P for all x, f is convex if and only if P ⪰ 0 [...]. f is strictly convex if and only if P ≻ 0 [...]. Remark 3.1 [...] the function f (x) = 1/x2 , with dom f = {x ∈ R | x ≠ 0}, satisfies f ′′ (x) > 0 for all x ∈ dom f , but is not a convex function."

### Fonte 5: Boyd & Vandenberghe, §3.1.8, p. 77; §3.2.1, p. 79; §4.2.2, p. 138
**Uso pretendido:** nome "desigualdade de Jensen"; soma de convexas; ótimo local é global.

**Trechos:**
> "The basic inequality (3.1), i.e., f (θx + (1 − θ)y) ≤ θf (x) + (1 − θ)f (y), is sometimes called Jensen's inequality."

> "If f1 and f2 are both convex functions, then so is their sum f1 + f2 ."

> "A fundamental property of convex optimization problems is that any locally optimal point is also (globally) optimal."

### Fonte 6: Deisenroth, Faisal & Ong, *Mathematics for Machine Learning*, §5.7, pp. 164–165
**Uso pretendido:** definição de Hessiana e simetria.

**Trecho:**
> "The Hessian is the collection of all second-order partial derivatives. If f (x, y) is a twice (continuously) differentiable function, then ∂2f/∂x∂y = ∂2f/∂y∂x, (5.146) i.e., the order of differentiation does not matter, and the corresponding Hessian matrix [...] is symmetric. [...] Generally, for x ∈ Rn and f : Rn → R, the Hessian is an n × n matrix. The Hessian measures the curvature of the function locally around (x, y)."

### Fonte 7: Deisenroth, Faisal & Ong, §7.3, pp. 236–237
**Uso pretendido:** definições de conjunto e função convexos (Defs. 7.2 e 7.3) e as condições de 1ª e 2ª ordem na notação do livro-texto.

**Trecho:**
> "Definition 7.2. A set C is a convex set if for any x, y ∈ C and for any scalar θ with 0 ⩽ θ ⩽ 1, we have θx + (1 − θ)y ∈ C . [...] If we further know that a function f (x) is twice differentiable, that is, the Hessian (5.147) exists for all values in the domain of x, then the function f (x) is convex if and only if ∇2x f (x) is positive semidefinite (Boyd and Vandenberghe, 2004)."

**Contribuições nossas (sinalizadas no texto):** definição de conjunto (noção usual, não axiomática); prova de "$f$ convexa ⟺ $\mathrm{epi}\,f$ convexo" (o Boyd só enuncia); exemplos $x^2$, $x^3$, anel e união; prova da condição de 2ª ordem; proposição sobre o conjunto de minimizadores $\boldsymbol\beta^\star+\mathcal{N}(X)$; lema de unicidade e existência da solução Ridge; o exemplo `AveOtherRooms`. O teste da segunda derivada para $f$ não quadrática é citado sem prova.
