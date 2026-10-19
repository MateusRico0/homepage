## Resumo — Aula 08

A Aula 7 garantiu teoricamente a existência e unicidade do minimizador em perdas convexas, mas deixou em aberto como alcançá-lo quando resolver sistemas lineares diretos ($X^T X \boldsymbol{\beta} = X^T \mathbf{y}$) é proibitivamente caro ou quando a perda não possui solução analítica em forma fechada. Esta aula desenvolve o primeiro e mais fundamental método iterativo contínuo: a **Descida do Gradiente** (*Gradient Descent* / *Steepest Descent*). Partindo da intuição geométrica da direção de maior descida ($-\nabla f$), definimos a regra de atualização e deduzimos a cota máxima do tamanho de passo ($\alpha < 2/L$) a partir da suavidade de Lipschitz do gradiente. Em seguida, realizamos a análise exata da dinâmica do erro em formas quadráticas fortemente convexas via decomposição espectral, provando rigorosamente como a taxa de contração ótima $\rho^\star = \frac{\kappa - 1}{\kappa + 1}$ é governada exclusivamente pelo número de condição $\kappa = \text{cond}(\nabla^2 f)$. Aplicamos o método ao problema-fio do California Housing, diagnosticando o ziguezague decorrente de $\kappa \approx 23.460$ e demonstrando como a padronização de atributos (*feature scaling*) restaura a convergência rápida. Por fim, estendemos a otimização para além dos mínimos quadrados com a regressão logística e a perda de entropia cruzada binária, onde a ausência de solução fechada torna a descida do gradiente indispensável.

**Objetivos:** derivar e implementar o algoritmo de Descida do Gradiente vetorizado; provar analiticamente a convergência linear em quadráticas; compreender o papel dos autovalores extremos da Hessiana no limite do passo ($\alpha < 2/\lambda_{\max}$) e do número de condição no ziguezague ($\frac{\kappa-1}{\kappa+1}$); diagnosticar e corrigir o mau condicionamento prático via padronização; derivar o gradiente da entropia cruzada na regressão logística.
**Pré-requisitos:** gradiente-coluna e derivada direcional (Aula 6); Hessiana, autovalores, positividade e convexidade (Aula 7); autodecomposição espectral e quociente de Rayleigh (Aula 4); número de condição de matrizes (Aula 5).
**Dataset-fio:** California Housing (4 atributos: `MedInc`, `HouseAge`, `AveRooms`, `Population`), demonstrando a trajetória ziguezagueante nos dados brutos versus a convergência direta após padronização.

**Estratégia Pedagógica:** B (Inside-Out com Problema-Fio) — fundamentação analítica da taxa de convergência e dinâmica espectral de 1ª ordem motivada pelas limitações da solução analítica e guiada pelo problema-fio do California Housing.

---

## Plano de aula — Aula 08 (carga horária: ~105 min)

1. **Revisão e Introdução** (~12 min) — Revisão cuidadosa da Aula 7: ponto crítico com gradiente nulo é mínimo global sob convexidade. Problema motivador: por que não podemos simplesmente inverter $(X^T X)$ quando $N, d \gg 1$ ou quando a perda é transcendental? O que acontece ao dar passos na direção oposta ao gradiente? Pausa Ativa 1.
2. **Intuição — A Descida na Neblina e a Tigela Alongada** (~8 min) — O alpinista que só enxerga a declividade sob os pés ($-\nabla f$). A geometria da tigela esférica ($\kappa = 1$, gradiente aponta para o centro) versus a tigela alongada ($\kappa \gg 1$, gradiente quase ortogonal ao eixo ótimo).
3. **Bloco 1: O Algoritmo de Descida do Gradiente e o Tamanho de Passo** (~20 min) — Formulação da iteração $\mathbf{x}_{k+1} = \mathbf{x}_k - \alpha \nabla f(\mathbf{x}_k)$. Suavidade de Lipschitz do gradiente ($\|\nabla f(\mathbf{x}) - \nabla f(\mathbf{y})\| \le L \|\mathbf{x} - \mathbf{y}\|$). O lema do limitante superior quadrático (*Descent Lemma*). Teorema do passo máximo: descida estrita garantida para $0 < \alpha < 2/L$. O que ocorre quando $\alpha \ge 2/L$: oscilação e explosão numérica. Pausa Ativa 2.
4. **Bloco 2: Análise Espectral de Convergência em Quadráticas** (~25 min) — Forma quadrática $f(\mathbf{x}) = \frac{1}{2}\mathbf{x}^T A \mathbf{x} - \mathbf{b}^T \mathbf{x}$ com $A \succ 0$. Equação dinâmica do vetor de erro $\mathbf{e}_{k+1} = (I - \alpha A)\mathbf{e}_k$. Desacoplamento modal via autovetores de $A$: $\tilde{e}_{k+1, i} = (1 - \alpha \lambda_i)\tilde{e}_{k, i}$. Estabilidade absoluta e o raio espectral $\rho(I - \alpha A)$. Passo ótimo de Chebyshev $\alpha^\star = \frac{2}{\lambda_{\max} + \lambda_{\min}}$. Dedução da taxa de convergência $\rho^\star = \frac{\kappa - 1}{\kappa + 1}$, onde $\kappa = \lambda_{\max}/\lambda_{\min} = \text{cond}(A)$. Interpretação: por que $\kappa \approx 23.460$ torna a convergência centenas de vezes mais lenta. Pausa Ativa 3.
5. **Bloco 3: O Problema-Fio no California Housing e a Padronização** (~20 min) — Implementação vetorizada do Gradient Descent em Python. Execução nos dados brutos do California Housing: visualização da trajetória de ziguezague. A disparidade de escalas (`MedInc` $\sim 3$ vs `Population` $\sim 1400$) como causa do mau condicionamento da Hessiana. A padronização $Z$-score ($\tilde{x} = (x - \mu)/\sigma$) e seu efeito algébrico na homogeneização dos autovalores de $X^T X$. Reexecução com convergência rápida em poucas iterações. Pausa Ativa 4.
6. **Bloco 4: Extensão para Além dos Mínimos Quadrados — Regressão Logística** (~15 min) — Modelagem probabilística de classificação binária $P(y=1 \mid \mathbf{x}) = \sigma(\mathbf{w}^T \mathbf{x})$. A perda de Entropia Cruzada Binária (*Cross-Entropy*). Derivação do vetor gradiente $\nabla \mathcal{L}(\mathbf{w}) = \frac{1}{N}X^T(\hat{\mathbf{y}} - \mathbf{y})$. Hessiana $\nabla^2 \mathcal{L}(\mathbf{w}) = \frac{1}{N}X^T S X$ com $S$ diagonal positiva. Prova de convexidade estrita. A ausência de solução fechada para $\nabla \mathcal{L} = \mathbf{0}$ e o papel indispensável da descida do gradiente. Pausa Ativa 5.
7. **Fechamento** (~5 min) — Retomada das 5 perguntas da aula. O que fica em aberto: funções locais complexas e redes multicamadas. Ponte para a Aula 9 (Aproximações de Taylor e a Regra da Cadeia Multivariada).

---

## Fontes usadas — Aula 08

Deslocamentos página impressa → PDF: `copt.pdf` +14; `mathml.pdf` +6.

### Fonte 1: Boyd & Vandenberghe, *Convex Optimization*, §9.3 e §9.3.1, pp. 466–469 (PDF pp. 480–483)
**Uso pretendido:** Definição formal do algoritmo de Descida do Gradiente, critério de parada, lema de descida quadrática (*Descent Lemma*) sob gradiente Lipschitziano e análise de convergência linear para funções fortemente convexas.
**Trecho:**
> "Algorithm 9.3 Gradient descent method.
> given a starting point $x \in \mathbf{dom}\,f$.
> repeat
> 1. $\Delta x := -\nabla f(x)$.
> 2. Line search. Choose step size $t$ via exact or backtracking line search.
> 3. Update. $x := x + t \Delta x$.
> until stopping criterion is satisfied." (§9.3, p. 466)
> "quadratic upper bound on $\tilde{f}$: $\tilde{f}(t) \le f(x) - t \|\nabla f(x)\|_2^2 + \frac{M t^2}{2} \|\nabla f(x)\|_2^2$." (§9.3.1, eq. 9.17, p. 466)

### Fonte 2: Boyd & Vandenberghe, §9.3.2, pp. 469–470 (PDF pp. 483–484)
**Uso pretendido:** Exemplo analítico de forma quadrática 2D com autovalores $1$ e $\gamma$, dedução fechada da taxa de convergência $(\frac{\gamma-1}{\gamma+1})^{2k}$ e explicação geométrica do ziguezague associado ao número de condição da Hessiana.
**Trecho:**
> "We consider the quadratic objective function on $\mathbf{R}^2$: $f(x) = \frac{1}{2}(x_1^2 + \gamma x_2^2)$, where $\gamma > 0$... The condition numbers of the sublevel sets of $f$ are all exactly $\text{cond} = \max\{\gamma, 1/\gamma\}$. In this case we can derive the following closed-form expressions for the iterates... $f(x^{(k)}) = \left(\frac{\gamma - 1}{\gamma + 1}\right)^{2k} f(x^{(0)})$. This formula shows that the convergence is very slow if $\gamma$ is very large or very small, i.e., if the condition number of the Hessian is very large... The iterates zigzag back and forth across the narrow valley..." (§9.3.2, pp. 469–470)

### Fonte 3: Deisenroth, Faisal & Ong, *Mathematics for Machine Learning*, §7.1, pp. 225–231 (PDF pp. 231–237)
**Uso pretendido:** Definição da Descida do Gradiente em aprendizado de máquina, taxa de aprendizado $\gamma$, análise do efeito do tamanho de passo (subamortecido, crítico e divergente) e interpretação geométrica das curvas de nível.
**Trecho:**
> "Gradient descent is a first-order optimization algorithm. To find a local minimum of a function, we take steps proportional to the negative of the gradient of the function at the current point: $\mathbf{x}_{k+1} = \mathbf{x}_k - \gamma \nabla f(\mathbf{x}_k)$... If the step size is too small, gradient descent can be slow. If the step size is too large, gradient descent can overshoot the minimum and even diverge." (§7.1, p. 226)

### Fonte 4: Bishop, C. M., *Pattern Recognition and Machine Learning* (PRML), §4.3.2 e §4.3.3, pp. 205–207
**Uso pretendido:** Formulação da regressão logística, função sigmoide $\sigma(a)$, perda de entropia cruzada negativa, derivação do gradiente $\nabla \mathcal{L} = \frac{1}{N}X^T(\hat{\mathbf{y}} - \mathbf{y})$ e da Hessiana $\nabla^2 \mathcal{L} = \frac{1}{N}X^T S X$.
**Trecho:**
> "For a data set of independent observations, the cross-entropy error function is given by $E(\mathbf{w}) = -\sum \{t_n \ln y_n + (1 - t_n) \ln(1 - y_n)\}...$ Taking the gradient with respect to $\mathbf{w}$ gives $\nabla E(\mathbf{w}) = \sum (y_n - t_n) \mathbf{x}_n...$ The Hessian matrix is $H = \nabla \nabla E(\mathbf{w}) = \sum y_n(1 - y_n)\mathbf{x}_n \mathbf{x}_n^T = \mathbf{\Phi}^T \mathbf{R} \mathbf{\Phi}$, which is positive definite, so the error function is a convex function of $\mathbf{w}$." (§4.3.2 e §4.3.3, pp. 206–207)

