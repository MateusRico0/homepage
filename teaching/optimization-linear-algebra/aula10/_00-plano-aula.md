## Resumo — Aula 10

A Aula 9 estabeleceu a Diferenciação Automática e o Teorema de Baur-Strassen, capacitando o cálculo eficiente de gradientes exatos de perdas escalares em grafos computacionais arbitrários. No entanto, todos os algoritmos estudados até aqui — desde as Equações Normais e a SVD (Aulas 3 e 5) até a Descida do Gradiente em Lote (*Batch Gradient Descent* - BGD, Aula 8) — operam sob a hipótese de que o conjunto de dados completo de tamanho $N$ pode ser processado a cada passo de iteração. Em cenários reais de Aprendizado de Máquina moderno, onde $N$ atinge de milhões a trilhões de exemplos, avaliar $\nabla F(\mathbf{w}) = \frac{1}{N}\sum_{i=1}^N \nabla f_i(\mathbf{w})$ tem custo $\mathcal{O}(Nd)$ por passo. Uma única iteração pode exigir horas de computação e exceder a memória disponível, tornando o BGD inviável.

Esta aula inaugura o **Bloco 3: Otimização Estocástica e em Larga Escala**, introduzindo a fundamentação teórica e prática do **Gradiente Descendente Estocástico** (*Stochastic Gradient Descent* - SGD) e do **Mini-Batching**. 

Iniciamos formulando o problema de aprendizado supervisionado como minimização de **somas finitas** e estabelecemos o Gradiente Estocástico como um **estimador estatístico não-enviesado** do gradiente populacional/empírico: $\mathbb{E}_{i}[\nabla f_i(\mathbf{w})] = \nabla F(\mathbf{w})$. Analisamos rigorosamente a decomposição do gradiente estocástico $\mathbf{g}_k = \nabla F(\mathbf{w}_k) + \boldsymbol{\xi}_k$, demonstrando a patologia central do SGD: no minimizador exato $\mathbf{w}^\star$, embora o gradiente médio se anule ($\nabla F(\mathbf{w}^\star) = \mathbf{0}$), a covariância do ruído amostral permanece estritamente positiva ($\Sigma(\mathbf{w}^\star) \succ 0$). Esse fenômeno impede que o SGD convirja para um ponto fixo sob taxa de aprendizado constante $\alpha$, aprisionando os parâmetros em uma "bola de ruído" (*noise ball*) de raio proporcional a $\alpha \sigma^2 / \mu$.

Para sanar esse impasse, deduzimos as históricas **Condições de Convergência de Robbins-Monro (1951)** ($\sum \alpha_k = \infty$ e $\sum \alpha_k^2 < \infty$) e analisamos cronogramas práticos de decaimento de taxa de aprendizado (*step decay*, decaimento polinomial $1/\sqrt{k}$ e decaimento cosseno). Em seguida, formulamos o compromisso do **Mini-Batching**, provando que um lote de tamanho $B$ reduz a variância do gradiente por um fator de $1/B$ ($\frac{\sigma^2}{B}$ com reposição, ou $\frac{N-B}{N-1}\frac{\sigma^2}{B}$ sem reposição), enquanto explora a paralelização massiva de hardware moderno (operações BLAS-3, hierarquia de memória cache e Tensor Cores em GPUs). Por fim, desmistificamos a "bênção oculta" da estocasticidade: longe de ser um mero defeito de aproximação, o ruído estocástico atua como uma flutuação térmica (análoga à dinâmica de difusão de Langevin) que permite ao otimizador escapar de vales estreitos e pontos de sela, direcionando o modelo para mínimos planos (*flat minima*) dotados de superior capacidade de generalização.

**Objetivos:**
1. Formular o problema de aprendizado supervisionado como a minimização de uma soma finita e quantificar o gargalo temporal $\mathcal{O}(Nd)$ e de memória do Batch Gradient Descent em larga escala.
2. Demonstrar formalmente a propriedade de estimador não-enviesado do gradiente estocástico ($\mathbb{E}[\mathbf{g}_k] = \nabla F(\mathbf{w})$) e calcular o tensor de covariância do ruído estocástico $\Sigma(\mathbf{w})$.
3. Provar por que o SGD com taxa de aprendizado constante não atinge o minimizador exato, deduzir o raio da "bola de confusão" e aplicar as Condições de Robbins-Monro ($\sum \alpha_k = \infty, \sum \alpha_k^2 < \infty$) para garantir convergência assintótica quase certa.
4. Demonstrar a redução de variância $\sigma^2/B$ propiciada pelo Mini-Batching e explicar o compromisso físico entre tamanho do lote, saturação de largura de banda de memória e throughput em hardware moderno (SIMD/GPU).
5. Analisar o papel do ruído estocástico como regularizador implícito que viabiliza o escape de pontos de sela e induz a seleção de mínimos planos com melhor generalização.

**Pré-requisitos:** Descida do Gradiente, Lema da Descida, $L$-suavidade e taxa de contração espectral (Aula 8); Diferenciação reversa e retropropagação em grafos (Aula 9); Esperança, covariância e propriedades de variáveis aleatórias vetoriais (revisão de estatística/probabilidade).
**Dataset-fio:** California Housing ($N = 20.640, d = 4$), comparando o progresso da perda, o tempo de parede (*wall-clock time*) e a trajetória no espaço de parâmetros entre BGD ($B = N$), SGD puro ($B = 1$) e Mini-batch SGD ($B = 32$).
**Estratégia Pedagógica:** B (Inside-Out com Problema-Fio) — da limitação computacional da descida em lote com $N$ massivo à modelagem estatística do gradiente estocástico, culminando na parametrização ótima de mini-batches em hardware real.

---

## Plano de aula — Aula 10 (carga horária: ~110 min)

1. **Revisão e Introdução** (~12 min)
   - *Revisão:* Da Aula 8 (Gradient Descent em lote e convergência linear sob convexidade forte) e Aula 9 (cálculo de gradiente via autodiff em tempo linear por amostra).
   - *Ideia Central:* Avaliar o gradiente exato sobre $N$ amostras a cada passo é um luxo proibitivo em larga escala; uma amostragem aleatória de tamanho $B \ll N$ fornece uma bússola ruidosa, mas correta em média, com custo computacional ordens de grandeza inferior.
   - *Problema Motivador:* No California Housing ($N = 20.640$), cada iteração do BGD exige acumular mais de 20 mil gradientes. Em redes modernas (ImageNet com $1{,}3 \times 10^6$ imagens ou LLMs com trilhões de tokens), dar um único passo de BGD levaria horas ou dias.
   - *Roteiro (4 Perguntas Centrais):*
     1. Por que podemos substituir a soma de $N$ gradientes por uma amostra aleatória de tamanho $B \ll N$ sem desviar o modelo do minimizador?
     2. Qual é a estrutura matemática do ruído estocástico e por que ele impede a convergência para um ponto fixo sob taxa de aprendizado constante?
     3. Como o Mini-Batching governa a variância do gradiente e qual é o ponto de equilíbrio ótimo com a arquitetura do hardware?
     4. Como as condições de Robbins-Monro asseguram a convergência e como o ruído estocástico atua beneficamente no escape de selas e na generalização?
   - *Pausa 1.*

2. **Intuição — O Alpinista no Nevoeiro e a Partícula Browniana** (~8 min)
   - A descida em lote como um alpinista com visão telescópica perfeita de todo o relevo montanhoso: passos perfeitamente alinhados, porém extremamente lentos para planejar.
   - O SGD como um alpinista imerso em nevoeiro denso segurando uma bússola ruidosa que vibra aleatoriamente a cada instante: cada passo é tomado quase instantaneamente; embora o caminho ziguezagueie de modo caótico, a tendência média aponta persistentemente para o fundo do vale.
   - A física da estocasticidade: o gradiente ruidoso como uma força de atrito combinada a um banho térmico browniano (Dinâmica de Langevin).

3. **Bloco 1: O Gargalo do Lote Completo e o Gradiente Estocástico** (~25 min)
   - O problema de soma finita em Aprendizado de Máquina:
     $$F(\mathbf{w}) = \frac{1}{N}\sum_{i=1}^N f_i(\mathbf{w}), \quad \text{onde } f_i(\mathbf{w}) = \ell(h(\mathbf{x}_i; \mathbf{w}), y_i)$$
   - Complexidade temporal e de memória do Batch Gradient Descent (BGD):
     $$\mathbf{w}_{k+1} = \mathbf{w}_k - \alpha \nabla F(\mathbf{w}_k) = \mathbf{w}_k - \frac{\alpha}{N}\sum_{i=1}^N \nabla f_i(\mathbf{w}_k)$$
     Custo por iteração: $\mathcal{O}(Nd)$. Para atingir erro $\epsilon$, o BGD requer $\mathcal{O}(d \cdot N \log(1/\epsilon))$ operações de ponto flutuante.
   - O Algoritmo Stochastic Gradient Descent (SGD puro, $B = 1$):
     - Sorteio uniforme de um índice aleatório $i_k \sim \text{Uniforme}\{1, \dots, N\}$ a cada iteração $k$.
     - Regra de atualização: $\mathbf{w}_{k+1} = \mathbf{w}_k - \alpha_k \nabla f_{i_k}(\mathbf{w}_k)$.
     - Custo por iteração: $\mathcal{O}(d)$ — independente de $N$!
   - Comparação fundamental: em uma única "época" computacional ($N$ avaliações de gradiente individual), o BGD realiza **1 única atualização** de parâmetros, enquanto o SGD realiza **$N$ atualizações consecutivas**.
   - Ilustração empírica no California Housing: trajetória suave vs trajetória errática.
   - *Transição:* O SGD é ordens de grandeza mais rápido por passo, mas como temos certeza de que essa sequência de passos aleatórios realmente caminha em direção ao mínimo da função global $F(\mathbf{w})$?
   - *Pausa 2.*

4. **Bloco 2: Propriedades Estatísticas do Gradiente Estocástico** (~25 min)
   - Demonstração formal do estimador não-enviesado:
     $$\mathbb{E}_{i_k}[\nabla f_{i_k}(\mathbf{w})] = \sum_{i=1}^N P(i_k = i) \nabla f_i(\mathbf{w}) = \frac{1}{N}\sum_{i=1}^N \nabla f_i(\mathbf{w}) = \nabla F(\mathbf{w})$$
   - Decomposição canônica: Gradiente Estocástico = Gradiente Verdadeiro + Ruído de Amostragem:
     $$\mathbf{g}_k(\mathbf{w}_k) := \nabla f_{i_k}(\mathbf{w}_k) = \nabla F(\mathbf{w}_k) + \boldsymbol{\xi}_k$$
     onde $\mathbb{E}[\boldsymbol{\xi}_k \mid \mathbf{w}_k] = \mathbf{0}$.
   - O Tensor de Covariância do Ruído Estocástico:
     $$\Sigma(\mathbf{w}) := \text{Cov}(\boldsymbol{\xi}_k) = \mathbb{E}[(\mathbf{g}_k - \nabla F(\mathbf{w}))(\mathbf{g}_k - \nabla F(\mathbf{w}))^T] = \frac{1}{N}\sum_{i=1}^N \nabla f_i(\mathbf{w})\nabla f_i(\mathbf{w})^T - \nabla F(\mathbf{w})\nabla F(\mathbf{w})^T$$
   - A patologia central do SGD: o que ocorre no ponto ótimo $\mathbf{w}^\star$?
     - No BGD: $\nabla F(\mathbf{w}^\star) = \mathbf{0} \implies$ os passos se anulam e o algoritmo estagna exatamente em $\mathbf{w}^\star$.
     - No SGD: Embora $\nabla F(\mathbf{w}^\star) = \mathbf{0}$, os gradientes individuais $\nabla f_i(\mathbf{w}^\star) \neq \mathbf{0}$ para amostras individuais (a menos que haja ajuste perfeito com resíduo zero para todas as amostras — condição de interpolação).
     - Consequência: $\Sigma(\mathbf{w}^\star) = \frac{1}{N}\sum_{i=1}^N \nabla f_i(\mathbf{w}^\star)\nabla f_i(\mathbf{w}^\star)^T \succ 0$.
     - O ruído **não se anula** no minimizador! Sob taxa fixa $\alpha$, os parâmetros flutuam eternamente em torno de $\mathbf{w}^\star$.
   - *Transição:* Se uma única amostra produz ruído persistente, o que acontece se agregarmos um subconjunto de amostras a cada iteração?
   - *Pausa 3.*

5. **Bloco 3: Mini-Batching e a Física do Hardware** (~25 min)
   - O Estimador por Mini-Batch:
     $$\mathbf{g}_{\mathcal{B}}(\mathbf{w}) = \frac{1}{B}\sum_{i \in \mathcal{B}} \nabla f_i(\mathbf{w}), \quad \text{onde } \mathcal{B} \subset \{1, \dots, N\}, \, |\mathcal{B}| = B$$
   - Redução da variância pelo Teorema do Limite Central:
     - Amostragem i.i.d. com reposição:
       $$\mathbb{E}[\|\mathbf{g}_{\mathcal{B}}(\mathbf{w}) - \nabla F(\mathbf{w})\|^2] = \frac{1}{B} \sigma^2(\mathbf{w})$$
       onde $\sigma^2(\mathbf{w}) = \mathbb{E}[\|\nabla f_i(\mathbf{w}) - \nabla F(\mathbf{w})\|^2]$.
     - Amostragem sem reposição (particionamento em épocas):
       $$\mathbb{E}[\|\mathbf{g}_{\mathcal{B}}(\mathbf{w}) - \nabla F(\mathbf{w})\|^2] = \frac{N - B}{N - 1} \frac{\sigma^2(\mathbf{w})}{B}$$
       (quando $B = N$, o fator de população finita zera o ruído, recuperando o BGD exato).
   - A Física da Computação Moderna e o Tradeoff de Hardware:
     - Por que $B = 1$ é ineficiente em GPUs/CPUs modernas: gargalo de comunicação e latência de despacho (*kernel launch overhead*). Operações Vetor-Vetor (BLAS Nível 1) são limitadas por largura de banda de memória (*memory-bound*).
     - Por que $B \in [32, 256]$ atinge máxima eficiência computacional: operações Matriz-Matriz (BLAS Nível 3) aproveitam pipelines SIMD, caches L1/L2 e Tensor Cores (*compute-bound*).
     - A Curva de Throughput: número de amostras processadas por segundo vs tamanho do lote $B$. O ponto de inflexão (*sweet spot*) do hardware.
   - Tradeoff Estatístico vs Computacional:
     - Dobrar $B$ dobra o custo computacional por passo, mas reduz a variância apenas por $\sqrt{2}$ na norma do ruído ($\frac{1}{2}$ na variância escalar). A partir de um limiar crítico de lote $B_{\text{crit}}$, aumentar $B$ traz retornos decrescentes de convergência por época.
   - *Transição:* Seja com $B=1$ ou $B=64$, o ruído ainda existe enquanto $B < N$. Como controlar a taxa de aprendizado para forçar o algoritmo a convergir exatamente para o minimizador?
   - *Pausa 4.*

6. **Bloco 4: Teoria de Convergência e Taxas de Aprendizado** (~25 min)
   - O Paradoxo da Taxa de Aprendizado Constante:
     - Análise em formas quadráticas fortemente convexas: $\mathbb{E}[\|\mathbf{w}_k - \mathbf{w}^\star\|^2] \le (1 - 2\alpha \mu)^k \|\mathbf{w}_0 - \mathbf{w}^\star\|^2 + \frac{\alpha \sigma^2}{2\mu}$.
     - A "bola de confusão" (*noise ball*): quando $k \to \infty$, o erro estagna em $\mathcal{O}(\alpha \sigma^2 / \mu)$.
   - O Teorema Histórico de Robbins e Monro (1951):
     - Para garantir convergência estocástica quase certa ($\mathbf{w}_k \xrightarrow{\text{q.c.}} \mathbf{w}^\star$), a sequência de passos $\{\alpha_k\}$ deve satisfazer:
       $$\sum_{k=1}^\infty \alpha_k = \infty \quad \text{(Capacidade de Exploração: permite atingir o mínimo a partir de qualquer ponto inicial)}$$
       $$\sum_{k=1}^\infty \alpha_k^2 < \infty \quad \text{(Supressão do Ruído: a variância acumulada é finita, eliminando flutuações)}$$
     - Exemplo canônico: $\alpha_k = \frac{\alpha_0}{k}$ ou $\alpha_k = \frac{\alpha_0}{\sqrt{k}}$.
   - Cronogramas Práticos de Decaimento (*Learning Rate Schedules*):
     - Decaimento em Degraus (*Step Decay*): divide $\alpha$ por $\gamma \approx 2$ ou $10$ a cada $E$ épocas.
     - Decaimento Polinomial: $\alpha_k = \frac{\alpha_0}{(1 + \gamma k)^p}$ com $p \in [0.5, 1.0]$.
     - Decaimento Cosseno (*Cosine Annealing*): $\alpha_t = \alpha_{\min} + \frac{1}{2}(\alpha_{\max} - \alpha_{\min})\left(1 + \cos\left(\frac{t}{T}\pi\right)\right)$.
   - A Bênção Oculta do Ruído Estocástico em Paisagens Não-Convexas:
     - Em redes neurais profundas, o ruído atua como regularizador implícito.
     - Escape de pontos de sela e mínimos locais estreitos (*sharp minima*): a covariância do ruído $\Sigma(\mathbf{w})$ tem maior energia nas direções de maior curvatura, empurrando os parâmetros para fora de vales pontiagudos em direção a mínimos planos (*flat minima*).
     - Conexão com generalização: mínimos planos são mais tolerantes a desvios entre a distribuição de treino e a distribuição de teste.
   - *Transição:* O ruído auxilia na generalização, mas o passo escalar global $\alpha$ trata todas as coordenadas de maneira uniforme. Como incorporar a curvatura local para dar passos ótimos por coordenada? $\to$ Métodos de Segunda Ordem e Precondicionamento (Aula 11).
   - *Pausa 5.*

7. **Fechamento** (~7 min)
   - *Retomando as 4 Perguntas:* Síntese concisa das respostas construídas na aula.
   - *Fechamento do Bloco 3 (Abertura):* O SGD e o Mini-Batching constituem o coração do treinamento moderno de aprendizado de máquina em grande escala.
   - *Ponte para a Aula 11:* A aproximação quadrática de Taylor multivariada, o passo ideal de Newton ($H^{-1}\nabla f$), o colapso cúbico em alta dimensão e as taxas de aprendizado adaptativas por coordenada via precondicionamento diagonal $\to$ **Aula 11: Otimização de Segunda Ordem e Precondicionamento Diagonal (AdaGrad e RMSProp)**.
   - Links para Exercícios e Soluções.

---

## Fontes usadas — Aula 10

Deslocamentos página impressa → PDF: `mathml.pdf` +6; `copt.pdf` +14; `optml.pdf` +12.

### Fonte 1: Wright & Recht, *Optimization for Data Analysis*, Cap. 5, §5.1, pp. 75–78 (PDF pp. 87–90)
**Uso pretendido:** Formulação de somas finitas, gradiente incremental/estocástico e propriedade fundamental de estimador não-enviesado.
**Trecho:**
> "The stochastic gradient (SG) method is one of the most popular algorithms in modern data analysis and machine learning... Here we assume that $f$ has the form of a finite sum; that is, $f(x) = \frac{1}{N}\sum_{i=1}^N f_i(x)$, where $N$ is usually very large. Computing a full gradient $\nabla f$ generally requires computation of $\nabla f_i, i = 1, 2, \dots, N$ — a computation that scales proportionally to $N$ in general... Alternatively, we could choose $i_k$ according to some random procedure at each iteration, which would be an SG approach... The unbiasedness property holds, since $\mathbb{E}_{\xi}(g(x, \xi)) = \frac{1}{N}\sum_{i=1}^N \nabla f_i(x) = \nabla f(x)$." (§5.1, pp. 75–77)

### Fonte 2: Wright & Recht, Cap. 5, §5.5.2, pp. 94–95 (PDF pp. 106–107)
**Uso pretendido:** Dedução da redução de variância via Mini-Batching, compromisso computacional e implementação prática.
**Trecho:**
> "When applying SG to the finite-sum objective, steps are often not based just on the gradient on a single term in this sum but rather on a minibatch of terms, usually of a given size (say $p$). That is, at iteration $k$, we select a subset $S_k \subset \{1, 2, \dots, n\}$, with $|S_k| = p$, and set $x^{k+1} = x^k - \alpha_k \frac{1}{p}\sum_{i \in S_k} \nabla f_i(x^k)$... The idea is that the minibatch has lower variance as an estimate of $\nabla f(x^k)$ than does the estimate based on a single term, namely $\nabla f_{i_k}(x^k)$, so more rapid convergence can be expected. Of course, it is also typically $p$ times more expensive to obtain this estimate! Still, when we account for the cost of performing the update to the vector $x$ and possibly communicating this update to the nodes in a parallel processing architecture, the minibatching approach makes sense. It is used almost universally in practical implementations of SG." (§5.5.2, p. 94)

### Fonte 3: Deisenroth, Faisal & Ong, *Mathematics for Machine Learning*, §7.1.3, pp. 231–233 (PDF pp. 237–239)
**Uso pretendido:** Estimador empírico da esperança, compromissos práticos de memória de hardware (CPU/GPU) e o papel do ruído no escape de ótimos locais.
**Trecho:**
> "Evaluating the sum gradient may require expensive evaluations of the gradients from all individual functions $L_n$. When the training set is enormous and/or no simple formulas exist, evaluating the sums of gradients becomes very expensive... In contrast to batch gradient descent, which uses all $L_n$ for $n = 1, \dots, N$, we randomly choose a subset of $L_n$ for mini-batch gradient descent. In the extreme case, we randomly select only a single $L_n$ to estimate the gradient. The key insight about why taking a subset of data is sensible is to realize that for gradient descent to converge, we only require that the gradient is an unbiased estimate of the true gradient... A major reason is practical implementation constraints, such as the size of central processing unit (CPU)/graphics processing unit (GPU) memory or limits on computational time... In contrast, small mini-batches are quick to estimate. If we keep the mini-batch size small, the noise in our gradient estimate will allow us to get out of some bad local optima, which we may otherwise get stuck in." (§7.1.3, pp. 231–233)

### Fonte 4: Robbins & Monro, "A Stochastic Approximation Method", *The Annals of Mathematical Statistics*, 22(3): 400–407 (1951)
**Uso pretendido:** Condições canônicas de convergência para aproximação estocástica com ruído amostral persistente.
**Trecho:**
> "Let $\alpha_n$ be a sequence of positive numbers such that $\sum_{n=1}^\infty \alpha_n = \infty$ and $\sum_{n=1}^\infty \alpha_n^2 < \infty$. Then the sequence $x_n$ defined by $x_{n+1} = x_n - \alpha_n y_n$, where $y_n$ is an unbiased observation of the regression function, converges in probability to the root $\theta$."

### Fonte 5: Bottou, Curtis & Nocedal, "Optimization Methods for Large-Scale Machine Learning", *SIAM Review*, 60(2): 223–311 (2018), §4.1–§4.3
**Uso pretendido:** Análise rigorosa do efeito de taxa de aprendizado constante versus decrescente, e a dinâmica da bola de ruído estacionária.
**Trecho:**
> "A fundamental difference between batch gradient descent and stochastic gradient methods is that in the latter, the variance of the stochastic gradient estimator does not vanish as the iterates approach a minimizer $w_*$... With a fixed stepsize $\alpha$, the iterates will not converge to the minimizer, but will wander in a region whose diameter is proportional to the stepsize $\alpha$ and the variance of the gradient estimates." (§4.2, p. 248)

