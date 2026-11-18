## Resumo — Aula 11

A Aula 10 explorou o treinamento estocástico com o SGD e o Mini-Batching, superando o gargalo de memória e tempo em Big Data ao custo de introduzir ruído amostral e flutuações em torno do ótimo. Contudo, tanto o SGD quanto o Batch Gradient Descent operam sob uma premissa restritiva: aplicam uma única taxa de aprendizado escalar global $\alpha$ para todos os parâmetros do modelo. Em problemas reais com dados tabulares ou redes profundas, variáveis exibem dispersões e importâncias desiguais, gerando superfícies de custo com vales estreitos e mau condicionamento ($\kappa = \lambda_{\max}/\lambda_{\min} \gg 1$), onde um passo escalar grande diverge nas coordenadas de alta curvatura, enquanto um passo pequeno paralisará o avanço nas coordenadas suaves.

Esta aula estuda a incorporação da **curvatura local** para construir passos ideais por coordenada. Iniciamos deduzindo o **Método de Newton Multivariado** como o minimizador exato do modelo quadrático de Taylor de 2ª ordem, provando sua taxa de convergência quadrática local e sua invariância afim. Em seguida, dissecamos as três patologias fatais que impedem o uso direto de Newton em Aprendizado de Máquina moderno: o custo temporal $\mathcal{O}(d^3)$ para resolução de sistemas lineares hessianos, o custo de memória $\mathcal{O}(d^2)$ e a atração perversa por pontos de sela quando a Hessiana perde a estrita positividade ($\nabla^2 f \not\succ 0$). Como remédio escalável, introduzimos a teoria do **Precondicionamento**, demonstrando como a restrição a matrizes diagonais desacopla as coordenadas e reduz o custo computacional para $\mathcal{O}(d)$. Por fim, deduzimos os algoritmos pioneiros de taxa de aprendizado adaptativa baseados em primeiras derivadas: o **AdaGrad** (Duchi et al., 2011), que acumula a energia histórica dos gradientes para dar passos longos em atributos esparsos, e o **RMSProp** (Tieleman & Hinton, 2012), que substitui o acúmulo infinito por uma média móvel exponencial (EMA), curando o congelamento prematuro do AdaGrad e pavimentando a base para o otimizador Adam.

**Objetivos:**
1. Derivar o passo analítico de Newton ($\Delta\mathbf{w}_{\text{nt}} = -H^{-1}\nabla f$) a partir da minimização da Série de Taylor quadrática multivariada e calcular o decremento de Newton.
2. Analisar o regime de convergência quadrática local ($\|\mathbf{e}_{k+1}\| \le M \|\mathbf{e}_k\|^2$) e demonstrar geometricamente a propriedade de invariância afim de Newton sob transformações lineares de coordenadas.
3. Quantificar as patologias computacionais do método de Newton exato em problemas de larga escala ($\mathcal{O}(d^3)$ em tempo, $\mathcal{O}(d^2)$ em espaço) e demonstrar por que ele é atraído para pontos de sela em topologias não-convexas.
4. Formalizar o precondicionamento via mudança de base e demonstrar como aproximações diagonais da Hessiana eliminam o gargalo matricial sem renunciar à normalização de escala por coordenada.
5. Derivar e implementar os otimizadores adaptativos AdaGrad e RMSProp, comparando analítica e numericamente a saturação assintótica do AdaGrad contra a adaptatividade exponencial perene do RMSProp.

**Pré-requisitos:** Hessiana, convexidade e condições de otimalidade de 2ª ordem (Aula 7); Descida do Gradiente e número de condição $\kappa$ (Aula 8); SGD e Mini-batching (Aula 10); Sistemas lineares e decomposição espectral (Aulas 2 e 4).
**Dataset-fio:** California Housing ($N = 20.640, d = 4$: `MedInc`, `HouseAge`, `AveRooms`, `AveBedrms`), demonstrando como a heterogeneidade dimensional ($\kappa \approx 23.460$) paralisa o SGD e como o precondicionamento diagonal restaura o progresso balanceado das coordenadas.
**Estratégia Pedagógica:** B (Inside-Out com Problema-Fio) — da falha do passo escalar único em variáveis de escalas discrepantes à formulação ideal do modelo quadrático de Newton, passando pelas patologias de alta dimensão até a solução pragmática do precondicionamento diagonal com AdaGrad e RMSProp.

---

## Plano de aula — Aula 11 (carga horária: ~110 min)

1. **Revisão e Introdução** (~12 min)
   - *Revisão:* Da Aula 8 (Lema da Descida e taxa de contração proporcional a $\frac{\kappa-1}{\kappa+1}$) e Aula 10 (SGD e a persistência da bola de ruído sob passo fixo).
   - *Ideia Central:* O gradiente indica a direção de maior inclinação local, mas é cego à taxa de variação dessa inclinação; conhecer a curvatura (Hessiana) permite predizer exatamente onde está o fundo de uma bacia parabólica em um único passo.
   - *Problema Motivador:* Regressão linear no California Housing sem padronização: `MedInc` varia em dezenas de milhares de dólares, enquanto `AveBedrms` oscila em frações unitárias. Um passo de SGD que estabiliza `MedInc` exige milhares de iterações para atualizar `AveBedrms`.
   - *Roteiro (4 Perguntas Centrais):*
     1. Como a aproximação quadrática de Taylor multivariada deduz o passo ideal de Newton e por que ele é imune a transformações afins?
     2. Por que o Método de Newton exato, apesar de sua convergência quadrática, torna-se computacionalmente impraticável e patológico em aprendizado profundo?
     3. Como a teoria do precondicionamento transforma o espaço paramétrico e por que matrizes diagonais oferecem o compromisso perfeito de complexidade $\mathcal{O}(d)$?
     4. Como o AdaGrad e o RMSProp constroem estimativas de curvatura coordenada a coordenada usando unicamente o histórico de gradientes de 1ª ordem?
   - *Pausa 1.*

2. **Intuição — A Bacia Elíptica e a Normalização Métrica** (~8 min)
   - O relevo em forma de vale estreito e comprido: descer ao longo do gradiente é como deslizar perpendicularmente às paredes íngremes sem avançar no comprimento do vale.
   - O Método de Newton como uma "lente métrica distorcida": ele transforma elipses concêntricas em círculos perfeitamente esféricos, onde o gradiente aponta diretamente para o centro.
   - O precondicionamento diagonal como uma aproximação axis-aligned: esticar e comprimir os eixos coordenados individualmente sem girá-los, eliminando as disparidades de escala bruta.

3. **Bloco 1: A Aproximação Quadrática de Taylor e o Método de Newton** (~25 min)
   - Expansão de Taylor multivariada em torno de $\mathbf{w}_k$:
     $$f(\mathbf{w}_k + \Delta\mathbf{w}) \approx q(\Delta\mathbf{w}) = f(\mathbf{w}_k) + \nabla f(\mathbf{w}_k)^T \Delta\mathbf{w} + \frac{1}{2}\Delta\mathbf{w}^T \nabla^2 f(\mathbf{w}_k) \Delta\mathbf{w}$$
   - Minimização do modelo substituto $q(\Delta\mathbf{w})$:
     $$\nabla_{\Delta\mathbf{w}} q(\Delta\mathbf{w}) = \nabla f(\mathbf{w}_k) + \nabla^2 f(\mathbf{w}_k)\Delta\mathbf{w} = \mathbf{0} \implies \Delta\mathbf{w}_{\text{nt}} = -[\nabla^2 f(\mathbf{w}_k)]^{-1} \nabla f(\mathbf{w}_k)$$
   - O Decremento de Newton como medida invariante de proximidade ao mínimo:
     $$\lambda(\mathbf{w})^2 = \nabla f(\mathbf{w})^T [\nabla^2 f(\mathbf{w})]^{-1} \nabla f(\mathbf{w}) = 2 [f(\mathbf{w}) - \min_{\Delta\mathbf{w}} q(\Delta\mathbf{w})]$$
   - Teorema da Invariância Afim: Seja $\tilde{\mathbf{w}} = A \mathbf{w}$ com $A$ inversível. O passo de Newton computado em $\tilde{\mathbf{w}}$ satisfaz $\Delta\tilde{\mathbf{w}} = A \Delta\mathbf{w}$. O algoritmo não depende da escolha de unidades de medida dos dados!
   - Teorema da Convergência Quadrática Local: sob $H$ fortemente convexa e Lipschitz contínua, para $\mathbf{w}_k$ suficientemente próximo de $\mathbf{w}^\star$, existe $M > 0$ tal que:
     $$\|\mathbf{w}_{k+1} - \mathbf{w}^\star\| \le M \|\mathbf{w}_k - \mathbf{w}^\star\|^2$$
     (o número de dígitos significativos corretos dobra a cada iteração!).
   - *Transição:* Se Newton é tão matematicamente perfeito, por que quase nenhuma rede neural de produção é treinada com ele?
   - *Pausa 2.*

4. **Bloco 2: As Três Patologias de Newton em Aprendizado de Máquina** (~20 min)
   - **Patologia 1 (Complexidade $\mathcal{O}(d^3)$ e Memória $\mathcal{O}(d^2)$):**
     - Em um modelo com $d = 10^6$ parâmetros (minúsculo para os padrões atuais), armazenar a Hessiana requer $10^{12}$ floats $\approx 4$ Terabytes de RAM.
     - Resolver o sistema linear $H \Delta\mathbf{w} = -\mathbf{g}$ custa $\approx \frac{1}{3}d^3$ FLOPs $\approx 3{,}3 \times 10^{17}$ operações por iteração.
   - **Patologia 2 (Atração por Pontos de Sela e Máximos Locais):**
     - A condição $\nabla q(\Delta\mathbf{w}) = \mathbf{0}$ encontra pontos estacionários do modelo quadrático.
     - Se $H$ possuir autovalores negativos ($\lambda_i < 0$), o passo de Newton move-se no sentido de maximizar a função ao longo desse autoespaço!
     - Em superfícies não-convexas de alta dimensão, pontos de sela superam mínimos locais por razões combinatórias exponenciais.
   - **Patologia 3 (Fragilidade ao Ruído Estocástico):**
     - Inverter uma estimativa ruidosa de mini-batch da Hessiana amplia violentamente o erro nas direções com autovalores pequenos.
   - Regularização de Levenberg-Marquardt / Newton Amortecido: $(H + \lambda I)^{-1}\nabla f$, interpolando suavemente entre Newton puro ($\lambda \to 0$) e Gradiente Descendente ($\lambda \to \infty$).
   - *Transição:* Não podemos arcar com $\mathcal{O}(d^3)$, mas não queremos a lentidão do passo escalar de $\mathcal{O}(d)$. Como extrair o melhor dos dois mundos?
   - *Pausa 3.*

5. **Bloco 3: A Geometria do Precondicionamento e a Matriz Diagonal** (~22 min)
   - Mudança de variáveis linear: considere a transformação $\tilde{\mathbf{w}} = P^{1/2} \mathbf{w}$, onde $P \succ 0$ é a matriz de precondicionamento.
   - O gradiente na nova base: $\nabla_{\tilde{\mathbf{w}}} f = P^{-1/2} \nabla_{\mathbf{w}} f$.
   - A atualização de gradiente descendente em $\tilde{\mathbf{w}}$:
     $$\tilde{\mathbf{w}}_{k+1} = \tilde{\mathbf{w}}_k - \alpha \nabla_{\tilde{\mathbf{w}}} f \iff \mathbf{w}_{k+1} = \mathbf{w}_k - \alpha P^{-1} \nabla_{\mathbf{w}} f(\mathbf{w}_k)$$
   - Conexão: se $P = \nabla^2 f$, recuperamos Newton. Se $P = I$, temos o GD padrão.
   - O compromisso da **Aproximação Diagonal**: restringir $P$ a ser uma matriz diagonal positiva $D = \text{diag}(s_1, \dots, s_d) \succ 0$.
     - Inversão trivial em tempo linear $\mathcal{O}(d)$: $D^{-1} = \text{diag}(1/s_1, \dots, 1/s_d)$.
     - Atualização desacoplada por coordenada:
       $$w_{i, k+1} = w_{i, k} - \frac{\alpha}{s_{i, k}} \frac{\partial f}{\partial w_i}$$
     - Cada parâmetro recebe um passo inversamente proporcional à sua escala de curvatura estimada.
   - *Transição:* Como obter esses coeficientes de escala $s_i$ sem precisar calcular nem mesmo a diagonal analítica da Hessiana?
   - *Pausa 4.*

6. **Bloco 4: Escalas Adaptativas na Prática: AdaGrad e RMSProp** (~15 min)
   - A intuição das primeiras derivadas como substituto da curvatura: se uma coordenada exibe gradientes de grande magnitude ao longo das iterações, sua bacia é íngreme; se os gradientes são raros ou diminutos, a direção é suave ou esparsa.
   - **AdaGrad (Duchi, Hazan & Singer, 2011):**
     - Acúmulo de quadrados de gradientes passados:
       $$G_{t, i} = G_{t-1, i} + g_{t, i}^2 = \sum_{\tau=1}^t g_{\tau, i}^2$$
     - Atualização vetorial:
       $$\mathbf{w}_{t+1} = \mathbf{w}_t - \frac{\alpha}{\sqrt{G_t} + \epsilon} \odot \mathbf{g}_t$$
     - *Sucesso:* Avanço veloz em coordenadas esparsas (como vocabulário raro em NLP ou IDs em sistemas de recomendação).
     - *A Patologia do Congelamento:* Como $g_{\tau, i}^2 \ge 0$, a soma $G_t$ cresce monotonamente. A taxa de aprendizado efetiva $\alpha / \sqrt{G_t}$ decai inexoravelmente para $0$, paralisando o treinamento precocemente em redes profundas.
   - **RMSProp (Tieleman & Hinton, 2012):**
     - Cura do congelamento: substituir a soma infinita por uma Média Móvel Exponencial (*Exponential Moving Average* - EMA):
       $$v_{t, i} = \beta_2 v_{t-1, i} + (1 - \beta_2) g_{t, i}^2, \quad \text{com } \beta_2 \in [0{,}9, 0{,}999]$$
     - Atualização vetorial:
       $$\mathbf{w}_{t+1} = \mathbf{w}_t - \frac{\alpha}{\sqrt{v_t} + \epsilon} \odot \mathbf{g}_t$$
     - A taxa de aprendizado efetiva reflete a variabilidade das últimas $\approx \frac{1}{1-\beta_2}$ iterações, permitindo adaptação perene em paisagens não-estacionárias.
   - *Pausa 5.*

7. **Fechamento** (~8 min)
   - *Retomando as 4 Perguntas:* Síntese concisa das respostas construídas na aula.
   - *O Que Fica em Aberto:* O RMSProp equaliza com perfeição as velocidades individuais de cada coordenada. Mas ele opera sem memória vetorial de direção: em vales com inclinação transversal mista, ele ainda sofre de ziguezagues porque cada passo depende unicamente do gradiente instantâneo $\mathbf{g}_t$.
   - *Ponte para a Aula 12:* Como dotar as atualizações de inércia mecânica e momento direcional? $\to$ **Aula 12: Momento, Curvatura e Métodos Acelerados (e a síntese definitiva no Adam e AdamW)**.
   - Links para Exercícios e Soluções.

---

## Fontes usadas — Aula 11

### Fonte 1: Boyd & Vandenberghe (2004), *Convex Optimization*, §9.5, pp. 484–492
**Uso pretendido:** Definição formal do passo de Newton, dedução via minimização do modelo quadrático de Taylor, decremento de Newton e Teorema de Invariância Afim.
**Trecho:**
> "The step $\Delta x_{\mathrm{nt}} = -\nabla^2 f(x)^{-1}\nabla f(x)$ is called the Newton step (for $f$, at $x$). Positive definiteness of $\nabla^2 f(x)$ implies that $\nabla f(x)^T \Delta x_{\mathrm{nt}} = -\nabla f(x)^T \nabla^2 f(x)^{-1}\nabla f(x) < 0$ unless $\nabla f(x) = 0$, so the Newton step is a descent direction [...] The quantity $\lambda(x) = (\nabla f(x)^T \nabla^2 f(x)^{-1}\nabla f(x))^{1/2}$ is called the Newton decrement for $f$ at $x$ [...] A very important property of the Newton step and decrement is that they are independent of affine changes of coordinates."

### Fonte 2: Wright & Recht (2022), *Optimization for Data Analysis*, §3.1–3.3 e §5.3, pp. 62–75, 114–118
**Uso pretendido:** Análise da convergência quadrática local de Newton, regularização de Levenberg-Marquardt para matrizes mal-condicionadas e precondicionamento diagonal.
**Trecho:**
> "Newton's method achieves quadratic convergence when the current iterate is sufficiently close to a strictly convex local minimum: $\|\mathbf{x}_{k+1} - \mathbf{x}^\star\| \le M \|\mathbf{x}_k - \mathbf{x}^\star\|^2$ [...] In large-scale data settings, evaluating and factoring the Hessian matrix $H_k$ has complexity $\mathcal{O}(d^3)$, which is completely prohibitive when $d$ is in the millions. Diagonal scaling replaces $H_k$ with a positive diagonal matrix $D_k$, yielding coordinate-wise step sizes that scale linearly in dimension."

### Fonte 3: Deisenroth, Faisal & Ong (2020), *Mathematics for Machine Learning*, §7.1–7.2, pp. 235–241
**Uso pretendido:** Comparação entre gradiente descendente de primeira ordem e métodos de segunda ordem, e as patologias de não-convexidade e atração por pontos de sela.
**Trecho:**
> "Newton's method uses second-order curvature information to find the minimum of a function. However, if the Hessian is not positive definite, the Newton step may point towards a saddle point or a local maximum [...] Furthermore, computing the Hessian requires $\mathcal{O}(D^2)$ memory and $\mathcal{O}(D^3)$ computation, making exact Newton updates impractical for high-dimensional models."

### Fonte 4: Duchi, Hazan & Singer (2011), *Adaptive Subgradient Methods for Online Learning and Stochastic Optimization*, JMLR
**Uso pretendido:** Formulação do AdaGrad, justificativa geométrica de acumulação de gradientes por coordenada e desaceleração do aprendizado em atributos frequentes vs raros.
**Trecho:**
> "Our algorithms dynamically incorporate knowledge of the geometry of the data observed in earlier iterations [...] Informally, our procedures give frequently occurring features very low learning rates and infrequent features high learning rates."

