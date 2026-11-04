## Resumo — Aula 10: Gradient Boosting e Otimização Numérica no Espaço de Funções

Esta aula aprofunda a Parte 3 do curso (Modelos Avançados e Otimização), investigando a abordagem complementar ao Bagging da Aula 9. Enquanto o Bagging opera reduzindo a variância de modelos de alta capacidade (árvores profundas) por meio de agregação paralela independente, o Boosting ataca o viés de aproximação por meio de refinamento sequencial no espaço de funções. Apresentamos a evolução histórica e teórica do algoritmo pioneiro AdaBoost.M1 (Freund & Schapire, 1997) sob a ótica do modelo aditivo em estágios progressivos (*Forward Stagewise Additive Modeling*) com perda exponencial, deduzindo analiticamente a regra de reponderação de instâncias e os coeficientes ótimos de combinação $\alpha_m$. Em seguida, formalizamos a generalização seminal de Jerome Friedman (2001): o Gradient Boosting Machine (GBM). Demonstramos que o ajuste sequencial a resíduos nada mais é do que uma descida de gradiente mais íngreme (*steepest descent*) executada diretamente no espaço não paramétrico das funções de predição, onde o resíduo generalizado (pseudo-resíduo) corresponde ao gradiente negativo da função de perda avaliado no modelo corrente. Deduzimos formalmente os pseudo-resíduos e os passos de busca linear para a perda quadrática ($L_2$), valor absoluto ($L_1$), perda robusta de Huber e deviance binomial. Por fim, exploramos os mecanismos críticos de regularização — notadamente o encolhimento (*shrinkage* / taxa de aprendizado $\nu$) e a subamostragem estocástica —, o papel da profundidade das árvores ($J$ nós terminais) no controle exato da ordem de interação entre preditores, e ferramentas de interpretabilidade pós-ajuste (importância relativa de variáveis e gráficos de dependência parcial, PDP). O dataset-fio é o California Housing (`gvlassis/california_housing`), permitindo o contraste empírico direto com as árvores da Aula 3 e as Florestas Aleatórias da Aula 9.

**Estratégia Pedagógica:** A (Outside-In) — Partimos da intuição prática de comitês sequenciais que corrigem erros pregressos para reduzir o viés, formalizamos a matemática dos modelos aditivos e da otimização funcional por descida de gradiente, e sintetizamos com a parametrização de árvores, regularização por shrinkage e análise de interpretabilidade.

---

## Plano de aula — Aula 10 (carga horária: 120 min)

1. **Revisão e Introdução** (~15 min)
   - *Revisão:* A decomposição formal do EMSE da Aula 8 ($\text{EMSE} = \text{Bias}^2 + \text{Var} + \sigma^2$) e o contraste com o Bagging e Random Forests da Aula 9. Relembrar que a média de estimadores preserva a esperança ($\mathbb{E}[\bar{T}] = \mathbb{E}[T]$) e atua apenas sobre a variância ($\rho \sigma^2 + \frac{1-\rho}{B}\sigma^2$), exigindo árvores profundas de baixo viés como base.
   - *Ideia Central:* O que fazer quando dispomos de modelos excessivamente simples (*weak learners*, *decision stumps*) limitados por alto viés? Em vez de calcular médias paralelas independentes, construímos uma sequência acoplada de preditores onde cada novo membro aprende especificamente os erros cometidos pelo comitê acumulado até aquele ponto.
   - *Roteiro:* 5 perguntas fundamentais da aula:
     1. Como o Boosting inverte a estratégia do Bagging, atacando sistematicamente o viés a partir de modelos fracos?
     2. Por que o AdaBoost de Freund & Schapire (1997) equivale a um modelo aditivo em estágios progressivos minimizando a perda exponencial?
     3. Qual é o salto conceitual de Jerome Friedman (2001) ao interpretar resíduos como o gradiente negativo no espaço de funções?
     4. Como derivar os pseudo-resíduos e os valores ótimos das folhas para perdas quadrática, absoluta, Huber e deviance logística?
     5. Como a regularização por encolhimento (*shrinkage* $\nu$) e o controle da profundidade $J$ governam o tradeoff entre capacidade, taxa de convergência e ordem de interação?
   - *Problema Motivador:* No California Housing, um *decision stump* isolado (profundidade 1) possui erro de teste elevado ($\text{MSE} \approx 0{,}998$). Ao combinar sequencialmente 100 stumps via Gradient Boosting ($\nu = 0{,}1$), o erro despenca para $0{,}471$. Ao permitir árvores rasas de profundidade 3 ($J=8$), o erro atinge $0{,}279$, superando a Floresta Aleatória de 100 árvores da Aula 9 ($0{,}290$).
   - *Pausa Ativa 1:* A inversão filosófica: Bagging (paralelo, baixa variância, base complexa) vs. Boosting (sequencial, baixo viés, base simples).

2. **Intuição — Descida de Gradiente no Espaço de Funções** (~15 min)
   - A analogia do golfista ou arqueiro: cada tacada corrige o erro residual da tacada anterior.
   - Descida de gradiente tradicional (espaço Euclidiano): atualiza-se um vetor paramétrico finito $\mathbf{w}^{(m)} = \mathbf{w}^{(m-1)} - \eta \nabla_{\mathbf{w}} L$.
   - Descida de gradiente funcional: o vetor de predições no conjunto de treino $\mathbf{f} = [f(\mathbf{x}_1), \dots, f(\mathbf{x}_N)]^T \in \mathbb{R}^N$ é o "parâmetro" a ser otimizado. O vetor de descida mais íngreme aponta na direção de $-\nabla_{\mathbf{f}} L$.
   - A barreira da generalização: o vetor $-\nabla_{\mathbf{f}} L$ só fornece direções de correção nos pontos observados de treino. Para generalizar para novos pontos $\mathbf{x} \notin \mathcal{D}$, projetamos essa direção de descida sobre uma classe restrita de hipóteses estruturadas (árvores de regressão $h_m(\mathbf{x})$) ajustadas aos pseudo-resíduos por mínimos quadrados.
   - Diagrama TikZ contrastando o vetor gradiente irrestrito em $\mathbb{R}^N$ com a projeção ortogonal na superfície das árvores de decisão.
   - *Pausa Ativa 2:* O papel da classe base como projeção do gradiente irrestrito.

3. **Bloco 1: Modelos Aditivos em Estágios e AdaBoost** (~25 min)
   - A formulação geral de Modelos Aditivos: $f_M(\mathbf{x}) = \sum_{m=1}^M \beta_m b(\mathbf{x}; \gamma_m)$.
   - O algoritmo de Modelos Aditivos em Estágios Progressivos (*Forward Stagewise Additive Modeling - FSAM*): em vez de otimizar todos os termos simultaneamente, fixa-se $f_{m-1}(\mathbf{x})$ e resolve-se:
     $$(\beta_m, \gamma_m) = \arg\min_{\beta, \gamma} \sum_{i=1}^N L(y_i, f_{m-1}(\mathbf{x}_i) + \beta b(\mathbf{x}_i; \gamma))$$
   - Dedução analítica rigorosa: equivalência exata entre FSAM com perda exponencial $L(y, f) = e^{-yf}$ ($y \in \{-1, +1\}$) e o algoritmo AdaBoost.M1 (Freund & Schapire, 1997).
     - Fatoração do erro: $e^{-y_i(f_{m-1}(\mathbf{x}_i) + \beta h(\mathbf{x}_i))} = w_i^{(m)} e^{-\beta y_i h(\mathbf{x}_i)}$.
     - Prova de que o classificador base ótimo $h_m$ minimiza o erro ponderado $\sum_{i=1}^N w_i^{(m)} \mathbb{I}(y_i \neq h(\mathbf{x}_i))$.
     - Derivação em relação a $\beta$ gerando o multiplicador analítico $\alpha_m = \frac{1}{2}\ln\left(\frac{1 - \text{err}_m}{\text{err}_m}\right)$.
     - Atualização dos pesos das instâncias: $w_i^{(m+1)} = w_i^{(m)} e^{-\alpha_m y_i h_m(\mathbf{x}_i)}$.
   - Propriedade populacional da perda exponencial: o minimizador populacional $f^*(\mathbf{x}) = \arg\min_{f(\mathbf{x})} \mathbb{E}_{Y\mid\mathbf{x}}[e^{-Yf(\mathbf{x})}]$ é exatamente a metade do log-odds de Bayes:
     $$f^*(\mathbf{x}) = \frac{1}{2} \ln \frac{P(Y=1\mid\mathbf{x})}{P(Y=-1\mid\mathbf{x})}$$
   - Patologias e limitações da perda exponencial: crescimento exponencial assimétrico para valores negativos $yf \ll 0$. Em dados ruidosos ou com rótulos incorretos, o AdaBoost concentra quase todo o peso em outliers intransponíveis, deteriorando a generalização.
   - *Pausa Ativa 3:* A mecânica da perda exponencial e a vulnerabilidade a outliers.

4. **Bloco 2: Gradient Tree Boosting e Pseudo-Resíduos Genéricos** (~25 min)
   - A formulação canônica de Jerome Friedman (2001) para perdas arbitrárias diferenciáveis.
   - Definição formal do vetor gradiente negativo no espaço de dados:
     $$r_{im} = -\left[\frac{\partial L(y_i, f(\mathbf{x}_i))}{\partial f(\mathbf{x}_i)}\right]_{f(\mathbf{x}) = f_{m-1}(\mathbf{x})}$$
   - Dedução passo a passo dos pseudo-resíduos para as quatro funções de perda fundamentais:
     1. **Perda Quadrática ($L_2$):** $L(y, f) = \frac{1}{2}(y - f)^2 \implies r_{im} = y_i - f_{m-1}(\mathbf{x}_i)$ (o resíduo clássico!).
     2. **Perda Absoluta ($L_1$ / MAE):** $L(y, f) = |y - f| \implies r_{im} = \text{sign}(y_i - f_{m-1}(\mathbf{x}_i))$ (independe da magnitude do erro, blindando a direção contra discrepâncias extremas).
     3. **Perda de Huber:** transição suave entre $L_2$ (para $|y - f| \le \delta$) e $L_1$ (para $|y - f| > \delta$), combinando a suavidade do mínimos quadrados próximo ao ótimo com a robustez do $L_1$ nas caudas.
     4. **Deviance Binomial (Log-Loss):** $L(y, f) = \ln(1 + e^{-2yf})$ para $y \in \{-1, +1\}$ ou $L(y, p) = -[y\ln p + (1-y)\ln(1-p)]$ para $y \in \{0, 1\}$. Pseudo-resíduo: $r_{im} = y_i - p_{m-1}(\mathbf{x}_i)$, onde $p_{m-1}(\mathbf{x}_i) = \sigma(f_{m-1}(\mathbf{x}_i))$.
   - O algoritmo Gradient Tree Boosting (Algoritmo 10.3 do ESL / Friedman, 2001):
     - Inicialização com a constante ótima $f_0(\mathbf{x}) = \arg\min_\gamma \sum_{i=1}^N L(y_i, \gamma)$.
     - Indução da árvore de regressão $T_m(\mathbf{x})$ com $J_m$ regiões terminais $R_{jm}$ ajustada aos pseudo-resíduos $r_{im}$ por mínimos quadrados.
     - Otimização da busca linear (*Line Search*) específica para cada folha terminal:
       $$\gamma_{jm} = \arg\min_\gamma \sum_{\mathbf{x}_i \in R_{jm}} L(y_i, f_{m-1}(\mathbf{x}_i) + \gamma)$$
     - Demonstração dos valores de $\gamma_{jm}$: média dos resíduos ($L_2$), mediana dos resíduos ($L_1$), e aproximação de Newton-Raphson de passo único para a deviance: $\gamma_{jm} = \frac{\sum_{i \in R_{jm}} (y_i - p_i)}{\sum_{i \in R_{jm}} p_i(1 - p_i)}$.
   - *Pausa Ativa 4:* Pseudo-resíduos de perdas robustas e a busca linear nas folhas.

5. **Bloco 3: Regularização, Arquitetura de Árvores e Interpretabilidade** (~25 min)
   - **Regularização por Encolhimento (*Shrinkage* / Taxa de Aprendizado $\nu$):**
     $$f_m(\mathbf{x}) = f_{m-1}(\mathbf{x}) + \nu \sum_{j=1}^J \gamma_{jm} \mathbb{I}(\mathbf{x} \in R_{jm}), \quad 0 < \nu \le 1$$
     - A analogia com regularização por penalidade ($L_2$ / Ridge): passos curtos forçam o comitê a explorar direções ortogonais de melhoria, evitando que as primeiras árvores dominem toda a predição.
     - O tradeoff $(\nu, M)$: diminuir $\nu$ para $\nu \le 0{,}1$ melhora consistentemente o erro de teste, ao custo de exigir um número proporcionalmente maior de iterações $M$.
     - Comprovação empírica no California Housing: sem encolhimento ($\nu = 1{,}0$), o modelo sofre sobreajuste rápido ($\text{MSE}_{\text{test}} = 0{,}452$); com encolhimento ($\nu = 0{,}1$), o erro atinge o mínimo global em $0{,}279$.
   - **Subamostragem Estocástica (*Stochastic Gradient Boosting*):** Amostragem sem reposição de uma fração $\eta \in (0, 1)$ das instâncias a cada iteração, combinando a redução de variância do Bagging com a aceleração do treino.
   - **Tamanho Ideal das Árvores (*Right-Sized Trees*) e Ordem de Interação:**
     - Uma árvore com $J$ folhas possui no máximo $J-1$ divisões internas.
     - Teorema estrutural de Friedman (2001): uma árvore com $J$ nós terminais é capaz de representar interações entre no máximo $J-1$ variáveis.
     - $J = 2$ (*decision stumps*): o modelo resultante é puramente aditivo (GAM, sem efeitos de interação cruzada): $f(\mathbf{x}) = \sum_{k=1}^p f_k(x_k)$.
     - Prática estatística: valores moderados $4 \le J \le 8$ (profundidade 2 a 3) são suficientes para modelar interações dominantes na quase totalidade dos datasets tabulares.
   - **Ferramentas de Interpretabilidade (Friedman, 2001):**
     - *Importância Relativa de Variáveis ($I_j^2$):* acúmulo da melhoria quadrática média proporcionada pelos cortes atribuídos à variável $j$, agregada sobre todas as $M$ árvores.
     - *Gráficos de Dependência Parcial (PDP):* isolamento visual do efeito marginal de uma variável $X_S$ integrando as variáveis complementares $X_C$:
       $$\bar{f}_S(\mathbf{x}_S) = \frac{1}{N} \sum_{i=1}^N f(\mathbf{x}_S, \mathbf{x}_{i, C})$$
   - **Modelos Intrinsecamente Explicáveis (EBM / $GA^2M$, Lou et al., 2012; Nori et al., 2019):**
     - O boosting cíclico (*round-robin*) sobre atributos individuais com micro-passos ($\nu \approx 0{,}01$).
     - Funções 1D $f_j(x_j)$ e interações 2D $f_{jk}(x_j, x_k)$ exatas (*glassbox*), sem necessidade de aproximações post-hoc (como PDP/SHAP).
     - Atribuição local exata por soma escalar e editabilidade de curvas para depuração de modelos em produção (*model debugging*).
   - *Pausa Ativa 5:* Regularização por encolhimento vs. subamostragem e interpretação de interações.

6. **Fechamento** (~15 min)
   - *Retomando as 5 Perguntas da Aula:* Síntese concisa das 5 respostas técnicas fundamentais.
   - *Tabela Comparativa Completa:* Bagging vs. Boosting (Objetivo central, capacidade dos estimadores base, agregação, comportamento assintótico perante $B / M \to \infty$, suscetibilidade a ruído).
   - *O Que Fica em Aberto:* Como otimizar árvores diretamente via aproximação quadrática de Taylor de 2ª ordem sobre a função de perda? (O surgimento dos modernos frameworks: XGBoost de Chen & Guestrin 2016, LightGBM de Ke et al. 2017, e CatBoost).
   - *Ponte para a Aula 11:* Máquinas de Vetores de Suporte (SVM). Enquanto o Boosting ataca o viés compondo milhares de hiperplanos ortogonais locais no espaço de funções, o SVM ataca a separação ótima no espaço Euclidiano original projetando pontos via *kernel trick* para encontrar o hiperplano de margem geométrica máxima.
   - Links para `exercicios.qmd` e `soluções.qmd`.

---

## Fontes usadas — Aula 10

### Fonte 1: ESL (Hastie, Tibshirani & Friedman, 2009), §10.1–10.4, pp. 337–345
**Uso pretendido:** Definição formal do algoritmo AdaBoost.M1, modelo aditivo em estágios progressivos (*Forward Stagewise Additive Modeling*) e equivalência analítica com a minimização da perda exponencial.
**Trecho:**
> "The motivation for boosting was a procedure that combines the outputs of many 'weak' classifiers to produce a powerful 'committee.' From this perspective boosting bears a resemblance to bagging and other committee-based approaches (Section 8.8). However we shall see that the connection is at best superficial and that boosting is fundamentally different... Forward stagewise modeling approximates the solution to (10.8) by sequentially adding new basis functions to the expansion without adjusting the parameters and coefficients of those that have already been added... We now show that AdaBoost.M1 (Algorithm 10.1) is equivalent to forward stagewise additive modeling using the exponential loss function $L(y, f(x)) = e^{-y f(x)}$."

### Fonte 2: ESL (Hastie, Tibshirani & Friedman, 2009), §10.10, pp. 358–361
**Uso pretendido:** Formulação da otimização numérica no espaço de funções via descida de gradiente mais íngreme, definição dos pseudo-resíduos e apresentação do Algoritmo 10.3 (Gradient Tree Boosting).
**Trecho:**
> "Fast approximate algorithms for solving (10.29) with any differentiable loss criterion can be derived by analogy to numerical optimization. The loss in using $f(x)$ to predict $y$ on the training data is $L(f) = \sum_{i=1}^N L(y_i, f(x_i))$. The goal is to minimize $L(f)$ with respect to $f$, where here $f(x)$ is constrained to be a sum of trees... Minimizing (10.33) can be viewed as a numerical optimization $\hat{\mathbf{f}} = \arg\min_{\mathbf{f}} L(\mathbf{f})$, where the 'parameters' $\mathbf{f} \in \mathbb{R}^N$ are the values of the approximating function $f(x_i)$ at each of the $N$ data points... Steepest descent chooses $\mathbf{h}_m = -\rho_m \mathbf{g}_m$ where $\rho_m$ is a scalar and $\mathbf{g}_m \in \mathbb{R}^N$ is the gradient of $L(\mathbf{f})$ evaluated at $\mathbf{f}_{m-1}$."

### Fonte 3: Friedman, Jerome H. (2001). "Greedy Function Approximation: A Gradient Boosting Machine", *Annals of Statistics*, 29(5), pp. 1189–1195
**Uso pretendido:** Proposição teórica original da aproximação gulosa de funções, dedução dos pseudo-resíduos e projeção do gradiente não paramétrico sobre modelos base estruturados.
**Trecho:**
> "Function estimation/approximation is a fundamental task in data analysis... When the function is to be represented as an expansion of parameterized base functions, non-linear optimization methods are often required. Here we develop a general gradient descent and Newton-like descent boosting paradigm for arbitrary loss functions. The base hypothesis at each iteration is fit to the negative gradient of the loss evaluated at the current model predictions, known as pseudo-residuals. A line search is then performed to calculate the step multiplier."

### Fonte 4: ESL (Hastie, Tibshirani & Friedman, 2009), §10.11–10.13, pp. 361–369
**Uso pretendido:** Relação entre o número de nós terminais $J$ e a ordem de interação de variáveis, mecanismo de regularização por encolhimento (*shrinkage* $\nu$) e métricas de interpretabilidade pós-ajuste (importância relativa e gráficos de dependência parcial).
**Trecho:**
> "A tree with $J$ terminal nodes can model at most $(J - 1)$-way interactions among the predictor variables... Although in many applications $J = 2$ will be insufficient, it is unlikely that $J > 10$ will be required. Experience so far indicates that $4 \le J \le 8$ works well in the context of boosting... That is, line 2(d) of Algorithm 10.3 is replaced by $f_m(x) = f_{m-1}(x) + \nu \cdot \sum_{j=1}^J \gamma_{jm} I(x \in R_{jm})$. The parameter $\nu$ can be regarded as controlling the learning rate of the boosting procedure. Smaller values of $\nu$ (more shrinkage) result in larger training risk for the same number of iterations $M$... Empirically it has been found (Friedman, 2001) that smaller values of $\nu$ favor better test error, and require correspondingly larger values of $M$."

