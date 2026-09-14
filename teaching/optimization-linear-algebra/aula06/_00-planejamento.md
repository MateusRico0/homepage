## Resumo — Aula 6

A Aula 6 abre a **Parte 2** do curso ("Cálculo da Otimização
Diferenciável"), uma mudança real de eixo em relação às cinco aulas
anteriores, todas de Álgebra Linear pura. A Abertura reconhece esse
corte explicitamente: por que o curso precisa de Cálculo agora, depois
de cinco aulas inteiras sem derivar nada? A resposta, motivada em
retrospecto: a própria derivação das Equações Normais (Aula 3,
$X^T X\hat{\mathbf{w}}=X^T\mathbf{y}$) já usou, implicitamente, a ideia
de "achar o ponto onde a perda para de diminuir" — mas em nenhum
momento o curso definiu, formalmente, o que "parar de diminuir"
significa para uma função de várias variáveis. A Aula 6 fecha essa
lacuna: derivada parcial, gradiente (como vetor-linha, convenção do
MathML), derivada direcional (com prova própria de que o gradiente
aponta na direção de subida mais íngreme, via desigualdade de
Cauchy-Schwarz da Aula 1) e Jacobiano (generalização para funções
vetoriais) — aplicados de ponta a ponta ao mesmo problema-fio
($L(\boldsymbol{\beta})=\|X\boldsymbol{\beta}-\mathbf{y}\|^2$,
California Housing), recuperando as Equações Normais como o caso
$\nabla L=\mathbf{0}$.

**Objetivos de aprendizagem:** (a) definir formalmente derivada
parcial e gradiente (como vetor-linha), aplicando regras de
diferenciação (soma, produto, cadeia); (b) derivar o gradiente de uma
perda quadrática por extenso, recuperando as Equações Normais; (c)
definir derivada direcional e provar que o gradiente aponta na direção
de subida mais íngreme; (d) generalizar para o Jacobiano de uma função
vetorial, com um exemplo concreto ($J$ do resíduo $=X$); (e) verificar
numericamente gradiente e Jacobiano por diferença finita.

**Pré-requisitos** (dicionário de notações, Aulas 1-5): produto interno
e desigualdade de Cauchy-Schwarz (Aula 1); Equações Normais
$X^TX\hat{\mathbf{w}}=X^T\mathbf{y}$ e resíduo (Aula 3); quociente de
Rayleigh (Aula 4); SVD, valores singulares (Aula 5). Dataset-fio:
California Housing ($X\in\mathbb{R}^{16\,640\times4}$, mesmas 4 colunas
desde a Aula 1).

**Estratégia Pedagógica:** Estratégia B (Inside-Out com
Problema-Fio) — aula de fundamentação matemática/linguagem
(derivadas/gradiente), exatamente o caso de uso que o `CLAUDE.md` lista
para a Estratégia B.

## Plano de aula — Aula 6 (carga horária real da turma: ~100min)

1. **Revisão e Introdução** (~14 min) — Revisão rápida da Aula 5 (SVD,
   aproximação de baixo posto, decomposição polar); reconhecimento
   explícito da virada Parte 1 $\to$ Parte 2 (por que Cálculo agora);
   gancho retrospectivo: as Equações Normais (Aula 3) já usaram "parar
   de diminuir" sem nunca defini-lo; Roteiro explícito (4 perguntas);
   Problema Motivador (ajustar $\boldsymbol{\beta}$ para reduzir a perda
   mais rápido possível, sem resolver o sistema $4\times4$ exato); Pausa
   Ativa 1.

2. **Derivada Parcial** (~14 min) — definição formal (MathML, Def. 5.5,
   primeira metade — derivada mantendo as demais variáveis fixas),
   exemplo bivariado resolvido à mão, aplicado a uma perda de $2$
   parâmetros (versão simplificada de $L(\boldsymbol{\beta})=\|X
   \boldsymbol{\beta}-\mathbf{y}\|^2$ com só 2 atributos) calculada via
   limite diretamente. Pausa Ativa 2.

3. **O Gradiente como Vetor e as Regras de Derivação** (~18 min) —
   gradiente como vetor-linha (MathML, Def. 5.5 completa + Remark da
   convenção linha-vs-coluna); regras de soma/produto/cadeia (MathML
   §5.2.1); desenvolvimento *principled* completo do gradiente da perda
   quadrática, $\nabla_{\boldsymbol{\beta}}\|X\boldsymbol{\beta}-
   \mathbf{y}\|^2=2(X\boldsymbol{\beta}-\mathbf{y})^TX$, recuperando as
   Equações Normais como a condição $\nabla L=\mathbf{0}$. Pausa
   Ativa 3.

4. **Derivada Direcional e a Direção de Subida Mais Íngreme** (~16 min)
   — motivação (o gradiente só dá a taxa de variação ao longo dos eixos
   — e nas outras direções?); definição própria de derivada direcional
   (nenhuma das 3 fontes da disciplina define isso formalmente no MathML
   — só `optml.pdf`/`copt.pdf`, reservados para aulas posteriores);
   derivação via regra da cadeia ($g(h)=f(\mathbf{x}+h\mathbf{v})$,
   $g'(0)=\nabla f(\mathbf{x})\cdot\mathbf{v}$); prova própria (via
   Cauchy-Schwarz, Aula 1) de que o gradiente aponta na direção de
   subida mais íngreme — o MathML só afirma isso como observação, sem
   provar (Def. 5.2, p.141; recorrência no Cap. 7, p.227-228). Pausa
   Ativa 4.

5. **O Jacobiano: Generalizando para Funções Vetoriais** (~14 min) —
   definição formal (MathML, Def. 5.6, convenção *numerator layout*);
   exemplo concreto e conectado ao problema-fio: o resíduo
   $\mathbf{r}(\boldsymbol{\beta})=X\boldsymbol{\beta}-\mathbf{y}$ como
   função vetorial $\mathbb{R}^4\to\mathbb{R}^{16\,640}$, cujo Jacobiano
   é exatamente $X$ — a própria matriz de design já usada desde a
   Aula 1; regra da cadeia com Jacobiano recupera o gradiente do
   Bloco 3 ($\nabla_{\boldsymbol{\beta}}L=2\mathbf{r}^TJ_{\mathbf{r}}=
   2\mathbf{r}^TX$). Pausa Ativa 5.

6. **Verificação Numérica** (~10 min) — gradiente e Jacobiano
   analíticos vs. diferença finita central, no dado real (California
   Housing); aviso sobre o compromisso passo-pequeno-vs-arredondamento
   na escolha do $h$ da diferença finita. Sem pausa ativa (mesmo padrão
   do bloco de "aplicação no dado real" da Aula 4).

7. **Fechamento e Ponte para a Aula 7** (~14 min) — retomar as 4
   perguntas do Roteiro; nomear o que fica em aberto: $\nabla L=
   \mathbf{0}$ identifica um ponto crítico, mas não diz se é mínimo,
   máximo ou sela — para a perda quadrática do problema-fio isso
   funciona porque $X^TX$ é semidefinida positiva (Aula 4), mas essa
   garantia não vem do gradiente sozinho. Tema da Aula 7: convexidade e
   a Hessiana.

**Fontes usadas — Aula 6**

### Fonte 1 — MathML, Definição 5.5 (Partial Derivative), p. 146 (PDF p. 152)
**Uso pretendido:** definição formal de derivada parcial e do gradiente
como vetor-linha (Blocos 2-3).

**Trecho:**
> "Definition 5.5 (Partial Derivative). For a function f : Rn → R, x 7→
> f (x), x ∈ Rn of n variables x1 , . . . , xn we define the partial
> derivatives as [...] and collect them in the row vector
> ∇x f = gradf = df/dx = [∂f(x)/∂x1 ∂f(x)/∂x2 · · · ∂f(x)/∂xn] ∈ R^{1×n},
> where n is the number of variables and 1 is the dimension of the
> image/range/codomain of f. [...] The row vector [...] is called the
> gradient of f or the Jacobian and is the generalization of the
> derivative from Section 5.1."

### Fonte 2 — MathML, Remark (Gradient as a Row Vector), p. 147 (PDF p. 153)
**Uso pretendido:** justificar a convenção de gradiente como vetor-linha
(Bloco 3), citada explicitamente para não parecer arbitrária.

**Trecho:**
> "It is not uncommon in the literature to define the gradient vector as
> a column vector, following the convention that vectors are generally
> column vectors. The reason why we define the gradient vector as a row
> vector is twofold: First, we can consistently generalize the gradient
> to vector-valued functions f : Rn → Rm (then the gradient becomes a
> matrix). Second, we can immediately apply the multi-variate chain
> rule without paying attention to the dimension of the gradient."

### Fonte 3 — MathML, §5.2.1 "Basic Rules of Partial Differentiation", p. 147-148 (PDF p. 153-154)
**Uso pretendido:** regras de soma/produto/cadeia usadas na derivação do
gradiente da perda quadrática (Bloco 3).

**Trecho:**
> "Here are the general product rule, sum rule, and chain rule:
> Product rule: ∂/∂x (f(x)g(x)) = (∂f/∂x)g(x) + f(x)(∂g/∂x); Sum rule:
> ∂/∂x (f(x) + g(x)) = ∂f/∂x + ∂g/∂x; Chain rule: ∂/∂x (g◦f)(x) =
> ∂/∂x g(f(x)) = (∂g/∂f)(∂f/∂x)."

### Fonte 4 — MathML, Definição 5.6 (Jacobian) e Remark (numerator layout), p. 150-151 (PDF p. 156-157)
**Uso pretendido:** definição formal do Jacobiano e da convenção de
*numerator layout* (Bloco 5).

**Trecho:**
> "Definition 5.6 (Jacobian). The collection of all first-order partial
> derivatives of a vector-valued function f : Rn → Rm is called the
> Jacobian. The Jacobian J is an m × n matrix [...] As a special case of
> (5.58), a function f : Rn → R1 [...] possesses a Jacobian that is a
> row vector."
>
> "Remark. In this book, we use the numerator layout of the derivative,
> i.e., the derivative df/dx of f ∈ Rm with respect to x ∈ Rn is an
> m × n matrix, where the elements of f define the rows and the
> elements of x define the columns [...] There exists also the
> denominator layout, which is the transpose of the numerator layout."

### Fonte 5 — MathML, Definição 5.2 (Derivative) e observação, p. 141 (PDF p. 147)
**Uso pretendido:** motivação para a Aula (Bloco 4) — o MathML afirma,
sem provar, que a derivada aponta na direção de subida mais íngreme; a
Aula 6 fornece a prova (via Cauchy-Schwarz, Aula 1).

**Trecho:**
> "The derivative of f points in the direction of steepest ascent of
> f."

### Fonte 6 — MathML, §7.1 "Optimization Using Gradient Descent", p. 227-228 (PDF p. 233-234)
**Uso pretendido:** reforço, com mais contexto, da afirmação da Fonte 5
— ainda sem prova no MathML, usada no Bloco 4 como motivação adicional
e no Fechamento como ponte para a Aula 8 (Gradiente Descendente).

**Trecho:**
> "Recall from Section 5.1 that the gradient points in the direction of
> the steepest ascent. Another useful intuition is to consider the set
> of lines where the function is at a certain value [...] The gradient
> points in a direction that is orthogonal to the contour lines of the
> function we wish to optimize. [...] Gradient descent exploits the
> fact that f (x0 ) decreases fastest if one moves from x0 in the
> direction of the negative gradient −((∇f )(x0 ))⊤ of f at x0 ."

**Nota de exposição própria (Bloco 4 — Derivada Direcional):** nenhuma
das 3 fontes da disciplina define formalmente derivada direcional no
material já coberto por este curso — o MathML não usa o termo em
nenhum lugar (verificado por busca no texto completo); `optml.pdf`
(Wright & Recht, §8.2, "The Subdifferential and Directional
Derivatives", p. 137) e `copt.pdf` definem o termo, mas ambos os livros
estão reservados para aulas posteriores (otimização, Lições 6+ em
sentido amplo, mas especificamente Wright & Recht para tópicos de
otimização não-suave/subgradientes, fora do escopo linear desta aula).
A definição e a prova de que o gradiente maximiza a derivada direcional
apresentadas no Bloco 4 são, portanto, construção nossa — usando só a
regra da cadeia (Fonte 3) e a desigualdade de Cauchy-Schwarz (Aula 1),
ambas já disponíveis.

### Fonte 7 — MathML, Exemplo 5.11 (Gradient of a Least-Squares Loss in a Linear Model), p. 153-154 (PDF p. 159-160)
**Uso pretendido:** achado durante a escrita do Bloco 5 — o MathML
resolve **exatamente** o problema desta aula (perda de mínimos
quadrados de um modelo linear) como exemplo de regra da cadeia com
Jacobiano, usando $\mathbf{e}(\boldsymbol{\theta})=\mathbf{y}-\Phi
\boldsymbol{\theta}$ (sinal oposto ao nosso
$\mathbf{r}=X\boldsymbol{\beta}-\mathbf{y}=-\mathbf{e}$) e
$L(\mathbf{e})=\|\mathbf{e}\|^2$. Substitui a nota de exposição própria
originalmente planejada para $J_{\mathbf{r}}(\boldsymbol{\beta})=X$ —
a identificação continua sendo observação nossa (o MathML não nomeia o
Jacobiano do resíduo como "a matriz de design"), mas a regra da cadeia
com Jacobiano que a envolve tem citação direta e precisa.

**Trecho:**
> "Let us consider the linear model y = Φθ [...] We define the
> functions L(e) := ∥e∥², e(θ) := y − Φθ. We seek ∂L/∂θ, and we will
> use the chain rule for this purpose. [...] The chain rule allows us
> to compute the gradient as ∂L/∂θ = (∂L/∂e)(∂e/∂θ) [...] ∂L/∂e = 2e⊤
> ∈ R^{1×N}. Furthermore, we obtain ∂e/∂θ = −Φ ∈ R^{N×D} [...] Remark.
> We would have obtained the same result without using the chain rule
> by immediately looking at the function L2(θ) := ∥y − Φθ∥² [...] This
> approach is still practical for simple functions like L2 but becomes
> impractical for deep function compositions."
