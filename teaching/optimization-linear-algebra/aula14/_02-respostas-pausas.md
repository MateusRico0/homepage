# Respostas e Guia Docente — Pausas da Aula 14

Este documento reúne as resoluções detalhadas, as deduções analíticas completas e o gabarito comentado dos testes conceituais (Verdadeiro ou Falso) das quatro Pausas da **Aula 14: Otimização Não-Suave, Subgradientes e Operadores Proximais**.

---

## Pausa 1: A Falha do Gradiente em Bicos e o Subdiferencial

### 1. Resolução da Pergunta Aberta
*Cenário:* Seja a função convexa 1D $f(w) = |w|$ em $w_0 = 0$.
1. **Por que o limite clássico da derivada não existe?**
   O limite pela direita é:
   $$\lim_{h \to 0^+} \frac{|0 + h| - |0|}{h} = \lim_{h \to 0^+} \frac{h}{h} = +1$$
   O limite pela esquerda é:
   $$\lim_{h \to 0^-} \frac{|0 + h| - |0|}{h} = \lim_{h \to 0^-} \frac{-h}{h} = -1$$
   Como os limites laterais são diferentes ($+1 \neq -1$), a função não possui derivada no sentido clássico em $w = 0$.
2. **Definição de Subgradiente:**
   Um número $g \in \mathbb{R}$ é um subgradiente de $f$ em $w = 0$ se satisfaz a desigualdade de suporte global para todo $u \in \mathbb{R}$:
   $$f(u) \ge f(0) + g(u - 0) \implies |u| \ge g \cdot u$$
   - Se $u > 0$: $|u| = u \ge g u \implies g \le 1$.
   - Se $u < 0$: $|u| = -u \ge g u \implies -1 \ge g$ (dividindo por $u < 0$, inverte o sinal: $g \ge -1$).
   Portanto, a desigualdade é satisfeita se e somente se:
   $$-1 \le g \le 1$$
   O subdiferencial em zero é o intervalo fechado:
   $$\partial |0| = [-1, 1]$$
   Existem infinitos subgradientes válidos em $w = 0$, cada um correspondendo à inclinação de uma reta suporte que passa por $(0, 0)$ sem jamais cruzar a função por cima!
3. **Condição de Fermat Generalizada:**
   O ponto $w = 0$ é minimizador global de $f(w) = |w|$ porque $0 \in [-1, 1]$, ou seja, $\mathbf{0} \in \partial f(0)$!

### 2. Gabarito Comentado dos Testes Conceituais (V/F)

*   **(A) Verdadeiro.** A definição de subgradiente estabelece exatamente que a reta ou hiperplano afim $h(\mathbf{u}) = f(\mathbf{w}) + \mathbf{g}^T(\mathbf{u} - \mathbf{w})$ é um limitante inferior global da função convexa $f$.
*   **(B) Verdadeiro.** Se $f$ for diferenciável em $\mathbf{w}$, o hiperplano suporte é único e coincide com o plano tangente, de modo que $\partial f(\mathbf{w}) = \{\nabla f(\mathbf{w})\}$.
*   **(C) Falso.** O subdiferencial da norma $L_1$ em $\mathbf{w} = \mathbf{0} \in \mathbb{R}^d$ é o produto cartesiano $[-1, 1]^d$, e não uma bola euclidiana de raio 1 (que seria a norma dual $L_2$).
*   **(D) Verdadeiro.** A condição $\mathbf{0} \in \partial f(\mathbf{w}^\star)$ é necessária e suficiente para otimalidade global em funções convexas irrestritas.

---

## Pausa 2: As Limitações do Método do Subgradiente

### 1. Resolução da Pergunta Aberta
*Cenário:* Minimização da função 1D $f(w) = |w|$ pelo Método do Subgradiente com passo constante $\alpha = 0{,}1$, partindo de $w_0 = 0{,}05$.
1. **Evolução das iterações:**
   - Em $w_0 = 0{,}05 > 0$: o único subgradiente é $g_0 = +1$.
     $$w_1 = w_0 - \alpha g_0 = 0{,}05 - 0{,}1 \times 1 = -0{,}05$$
     Valor da função: $f(w_0) = 0{,}05 \to f(w_1) = |-0{,}05| = 0{,}05$ (nenhum decrescimento!).
   - Em $w_1 = -0{,}05 < 0$: o único subgradiente é $g_1 = -1$.
     $$w_2 = w_1 - \alpha g_1 = -0{,}05 - 0{,}1 \times (-1) = -0{,}05 + 0{,}1 = +0{,}05$$
     Valor da função: $f(w_2) = 0{,}05$.
2. **Ciclo Limite Oscilatório:**
   O algoritmo fica preso eternamente no ciclo de período 2:
   $$w_0 = 0{,}05 \to w_1 = -0{,}05 \to w_2 = 0{,}05 \to w_3 = -0{,}05 \dots$$
   Ele **jamais atinge o mínimo ótimo $w^\star = 0$**! Isso ocorre porque em um ponto não-suave, a magnitude do subgradiente não tende a zero conforme nos aproximamos do ótimo ($|g| = 1$ em todos os pontos exceto exatamente em zero).
3. **Por que passos decrescentes são obrigatórios?**
   Para amortecer a oscilação, devemos adotar $\alpha_k \to 0$ satisfazendo as condições de Robbins-Monro ($\sum \alpha_k = \infty$ e $\sum \alpha_k^2 < \infty$), como $\alpha_k = \frac{1}{\sqrt{k}}$. O preço pago é uma convergência extremamente lenta: $\mathcal{O}(1/\sqrt{k})$ no valor de função, necessitando de $\mathcal{O}(1/\epsilon^2)$ iterações para atingir erro $\epsilon$ (contra $\mathcal{O}(1/\epsilon)$ do GD suave e $\mathcal{O}(1/\sqrt{\epsilon})$ do NAG).

### 2. Gabarito Comentado dos Testes Conceituais (V/F)

*   **(A) Falso.** Ao contrário do gradiente negativo de funções suaves, o vetor subgradiente negativo $-\mathbf{g}$ **não é** necessariamente uma direção de descida local; passos arbitrários podem aumentar o valor da função.
*   **(B) Verdadeiro.** Sob passo fixo $\alpha$, o método do subgradiente não converge para a solução exata, mas apenas para uma vizinhança de raio proporcional a $\alpha$ ao redor do mínimo.
*   **(C) Verdadeiro.** A prova de convergência do subgradiente garante apenas taxa de decaimento do melhor valor encontrado $\mathcal{O}(1/\sqrt{k})$, muito inferior a métodos de gradiente suave.
*   **(D) Falso.** Em problemas não-suaves, aplicar momento ingênuo sobre subgradientes frequentemente amplifica as oscilações transversais em torno dos bicos, piorando a instabilidade.

---

## Pausa 3: Operadores Proximais e o Soft-Thresholding ($L_1$)

### 1. Resolução da Pergunta Aberta
*Cenário:* Dedução analítica do Operador Proximal para a função $h(z) = \lambda |z|$ em $\mathbb{R}$:
$$\text{prox}_{\gamma h}(w) = \arg\min_{z \in \mathbb{R}} \left\{ \lambda |z| + \frac{1}{2\gamma} (z - w)^2 \right\}$$
1. **Condição de Otimalidade de Primeira Ordem:**
   Como a função objetivo é estritamente convexa e coerciva, existe um minimizador único $z^\star$ que satisfaz a condição de Fermat generalizada:
   $$0 \in \partial \left( \lambda |z| + \frac{1}{2\gamma}(z - w)^2 \right) \implies 0 \in \lambda \partial |z| + \frac{1}{\gamma}(z - w) \implies w - z \in \gamma \lambda \partial |z|$$
2. **Análise de Casos:**
   - **Caso 1 ($z > 0$):** Então $\partial |z| = \{+1\}$. A equação torna-se:
     $$w - z = \gamma \lambda \implies z = w - \gamma \lambda$$
     Para que a hipótese $z > 0$ seja consistente, devemos ter $w - \gamma \lambda > 0 \implies w > \gamma \lambda$.
   - **Caso 2 ($z < 0$):** Então $\partial |z| = \{-1\}$. A equação torna-se:
     $$w - z = -\gamma \lambda \implies z = w + \gamma \lambda$$
     Para que a hipótese $z < 0$ seja consistente, devemos ter $w + \gamma \lambda < 0 \implies w < -\gamma \lambda$.
   - **Caso 3 ($z = 0$):** Então $\partial |z| = [-1, 1]$. A equação torna-se:
     $$w - 0 \in \gamma \lambda [-1, 1] \implies w \in [-\gamma \lambda, \gamma \lambda] \iff |w| \le \gamma \lambda$$
3. **Unificação na Fórmula do Soft-Thresholding:**
   Combinando os três casos:
   $$\text{prox}_{\gamma \lambda |\cdot|}(w) = \mathcal{S}_{\gamma \lambda}(w) \triangleq \begin{cases} w - \gamma \lambda, & w > \gamma \lambda \\ 0, & |w| \le \gamma \lambda \\ w + \gamma \lambda, & w < -\gamma \lambda \end{cases} = \text{sign}(w) \max(|w| - \gamma \lambda, 0)$$
4. **Por que o $L_1$ induz esparsidade exata e o $L_2$ não?**
   - O operador proximal do $L_2$ ($\frac{\lambda}{2} z^2$) é uma contração linear suave: $\text{prox}_{\gamma \lambda (\cdot)^2}(w) = \frac{1}{1 + \gamma \lambda} w$. Se $w \neq 0$, o resultado é sempre diferente de zero ($z \neq 0$); ele apenas encolhe o número sem nunca zerá-lo!
   - O operador proximal do $L_1$ possui uma **zona morta não-linear** de largura $2\gamma\lambda$: qualquer coordenada cujo valor absoluto seja menor ou igual a $\gamma\lambda$ é projetada **exatamente em zero** ($z = 0$), induzindo esparsidade estrutural estrita!

### 2. Gabarito Comentado dos Testes Conceituais (V/F)

*   **(A) Verdadeiro.** A definição do operador proximal adiciona uma penalidade quadrática euclidiana ao termo não-suave, garantindo solução única por estrita convexidade.
*   **(B) Verdadeiro.** A condição $|w| \le \gamma\lambda$ mapeia todas as magnitudes inferiores ao limiar exatamente para o zero absoluto.
*   **(C) Falso.** O operador proximal da penalidade quadrática $L_2$ é o escalonador linear $\frac{1}{1 + \gamma\lambda} \mathbf{w}$, que nunca zera entradas não-nulas.
*   **(D) Verdadeiro.** O operador proximal é uma contração não-expansiva ($\|\text{prox}(x) - \text{prox}(y)\| \le \|x - y\|$), garantindo estabilidade numérica estrita.

---

## Pausa 4: Otimização Composta com ISTA e FISTA

### 1. Resolução da Pergunta Aberta
*Cenário:* Regressão Lasso com perda de Mínimos Quadrados e penalidade $L_1$:
$$\min_{\mathbf{w}} F(\mathbf{w}) = \underbrace{\frac{1}{2}\|X\mathbf{w} - \mathbf{y}\|_2^2}_{g(\mathbf{w})} + \underbrace{\lambda \|\mathbf{w}\|_1}_{h(\mathbf{w})}$$
onde $g(\mathbf{w})$ é suave com constante de Lipschitz $L = \lambda_{\max}(X^T X)$ e $h(\mathbf{w})$ é convexa não-diferenciável.
1. **Passo do ISTA:**
   Com taxa de aprendizado $\alpha = 1/L$:
   $$\mathbf{w}_{k+1} = \text{prox}_{\alpha h}\left( \mathbf{w}_k - \alpha \nabla g(\mathbf{w}_k) \right) = \mathcal{S}_{\alpha \lambda}\left( \mathbf{w}_k - \alpha X^T (X\mathbf{w}_k - \mathbf{y}) \right)$$
   O algoritmo executa uma descida de gradiente usual na perda de dados e em seguida aplica o *Soft-Thresholding* componente a componente, zerando coordenadas ruidosas.
   **Taxa de Convergência do ISTA:** $\mathcal{O}(1/k)$, idêntica à do Gradiente Descendente clássico suave.
2. **Aceleração do FISTA (Fast ISTA):**
   Beck e Teboulle (2009) provaram que é possível incorporar o momentum dinâmico de Nesterov $\beta_k = \frac{k-1}{k+2}$ antes da aplicação do operador proximal:
   $$\mathbf{y}_k = \mathbf{w}_k + \frac{k-1}{k+2}(\mathbf{w}_k - \mathbf{w}_{k-1})$$
   $$\mathbf{w}_{k+1} = \mathcal{S}_{\alpha \lambda}\left( \mathbf{y}_k - \alpha \nabla g(\mathbf{y}_k) \right)$$
   **Taxa de Convergência do FISTA:** $\mathcal{O}(1/k^2)$!
3. **Comparativo Numérico para Precisão $\epsilon = 10^{-4}$:**
   - Subgradiente clássico: $\mathcal{O}(1/\epsilon^2) \approx (10^4)^2 = \mathbf{100.000.000}$ iterações!
   - ISTA: $\mathcal{O}(1/\epsilon) \approx 10^4 = \mathbf{10.000}$ iterações!
   - FISTA: $\mathcal{O}(1/\sqrt{\epsilon}) \approx \sqrt{10^4} = \mathbf{100}$ iterações!
   O FISTA reduz o esforço computacional em 100 vezes em relação ao ISTA e em 1 milhão de vezes em relação ao método do subgradiente, provando o poder da união entre operadores proximais e aceleração de Nesterov!

### 2. Gabarito Comentado dos Testes Conceituais (V/F)

*   **(A) Verdadeiro.** O ISTA decompõe a iteração em um passo de gradiente na parte suave seguido pela aplicação do operador proximal na parte não-suave.
*   **(B) Verdadeiro.** O ISTA atinge a taxa $\mathcal{O}(1/k)$, idêntica à do Gradiente Descendente em problemas suaves.
*   **(C) Verdadeiro.** O FISTA introduz o momentum dinâmico de Nesterov no ponto de avaliação, acelerando a taxa para $\mathcal{O}(1/k^2)$.
*   **(D) Falso.** O FISTA é extremamente simples e eficiente: exige exatamente uma avaliação de gradiente e uma aplicação de *Soft-Thresholding* por passo, com custo assintótico por iteração idêntico ao do ISTA.
