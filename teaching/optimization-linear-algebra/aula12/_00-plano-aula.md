## Resumo — Aula 12

A Aula 11 estabeleceu a teoria do precondicionamento diagonal e deduziu as regras de taxas de aprendizado adaptativas (AdaGrad e RMSProp), capazes de equalizar as ordens de grandeza das coordenadas em paisagens com mau condicionamento ($\kappa \gg 1$) sem o custo inviável de inverter matrizes Hessianas completas ($\mathcal{O}(d^3)$). No entanto, o RMSProp opera sem memória direcional: suas atualizações dependem unicamente da derivada instantânea, deixando o algoritmo vulnerável a ziguezagues em vales cujos eixos principais não estão alinhados às coordenadas cartesianas, além de ficar vulnerável a desacelerações em platôs e pontos de sela.

Esta aula estuda a incorporação da **Inércia Mecânica e do Momento** na otimização de primeira ordem e culmina na grande síntese dos otimizadores modernos: o **Adam** e o **AdamW**. Iniciamos com a física da esfera pesada rolando sob atrito viscoso, deduzindo o **Momento de Polyak (*Heavy-Ball*)** e analisando sua dinâmica espectral em formas quadráticas, provando a aceleração de Chebyshev que reduz o fator de contração assintótico de $\mathcal{O}(1 - 1/\kappa)$ para $\mathcal{O}(1 - 2/\sqrt{\kappa})$. Em seguida, examinamos o **Gradiente Acelerado de Nesterov (NAG)**, introduzindo o conceito de gradiente antecipado (*look-ahead gradient*) como um sistema inteligente de frenagem que evita o *overshoot* do momento clássico e atinge a cota inferior de complexidade $\mathcal{O}(1/k^2)$ para métodos de primeira ordem em funções convexas gerais. No Bloco 3, unificamos a inércia de primeira ordem com o precondicionamento de segunda ordem, deduzindo rigorosamente o **Adam** (Kingma & Ba, 2014) e provando a necessidade da correção analítica de viés de inicialização nos passos transitórios iniciais. Por fim, no Bloco 4, dissecamos a histórica patologia da interação entre regularização $L_2$ e taxas adaptativas, deduzindo a correção do **AdamW** (Loshchilov & Hutter, 2019) via desacoplamento do *weight decay*, padrão indispensável no treinamento contemporâneo de Large Language Models (LLMs) e Transformers.

**Objetivos:**
1. Formular a analogia física do momento como um sistema dinâmico de 2ª ordem discretizado e deduzir a regra de atualização do Momento de Polyak (*Heavy-Ball*).
2. Analisar o operador de transição linear $2 \times 2$ do momento clássico no espaço espectral da Hessiana, deduzindo o ganho assintótico de taxa de convergência de $\kappa$ para $\sqrt{\kappa}$.
3. Contrastar o momento clássico com o Gradiente Acelerado de Nesterov (NAG), explicando a mecânica do vetor de antecipação (*look-ahead*) e seu efeito amortecedor de oscilações.
4. Derivar a formulação matemática do otimizador Adam, provando passo a passo a dedução das correções de viés de 1º e 2º momentos ($\frac{1}{1-\beta_1^t}$ e $\frac{1}{1-\beta_2^t}$).
5. Demonstrar analiticamente por que a regularização $L_2$ padrão distorce a escala de contração em otimizadores adaptativos e implementar a regra desacoplada do AdamW.

**Pré-requisitos:**

- Gradiente Descendente e número de condição $\kappa$ (Aula 8).
- Otimização Estocástica e Mini-Batching (Aula 10).
- Métodos de Newton, Precondicionamento Diagonal e RMSProp (Aula 11).
- Álgebra Linear: Teorema Espectral, raio espectral de matrizes, polinômio característico de sistemas dinâmicos $2 \times 2$.

**Dataset-fio / Problema-fio:** Bacia elíptica altamente mal-condicionada ($\kappa = 100$ a $1.000$) e superfície de regressão não-estacionária, ilustrando o amortecimento de oscilações transversais, a aceleração ao longo da calha plana, a correção de viés inicial do Adam e a preservação do decaimento uniforme de pesos no AdamW.

**Estratégia Pedagógica:** B (Inside-Out com Problema-Fio) — da falha da bússola cega instantânea em ravinas elípticas à formulação de inércia da física newtoniana, passando pelo refinamento preditivo de Nesterov até a síntese adaptativa contemporânea do Adam e sua correção definitiva no AdamW.

---

## Plano de aula — Aula 12 (carga horária: ~110 min)

1. **Revisão e Introdução** (~12 min)
   - *Revisão:* Da Aula 11 (RMSProp e o precondicionamento diagonal $v_t = \beta_2 v_{t-1} + (1-\beta_2)g_t^2$).
   - *Ideia Central:* O RMSProp equaliza as velocidades individuais por eixo, mas ainda sofre de oscilações transversais se o gradiente instantâneo apontar para os lados; na física, uma bola pesada que desce uma canaleta estreita não ziguezagueia, pois sua inércia cancela forças laterais opostas e soma o avanço longitudinal.
   - *Problema Motivador:* Vale elíptico estreito com curvatura desalinhada dos eixos coordenados ($\kappa = 100$): GD e RMSProp demoram centenas de passos devido à oscilação; um mecanismo de inércia corta esse tempo por uma ordem de grandeza.
   - *Roteiro (4 Perguntas Centrais):*
     1. Como a analogia mecânica de uma esfera com massa e atrito deduz o Momento de Polyak e reduz a taxa de convergência de $\kappa$ para $\sqrt{\kappa}$?
     2. Por que o salto antecipatório do Gradiente Acelerado de Nesterov (NAG) age como um sistema de freio inteligente e atinge a cota teórica ótima $\mathcal{O}(1/k^2)$?
     3. Como a síntese do Adam unifica inércia de primeira ordem com escalas adaptativas de segunda ordem, e por que a correção de viés inicial é indispensável?
     4. Por que a regularização $L_2$ clássica falha dentro de otimizadores adaptativos e por que o desacoplamento do AdamW revolucionou o treinamento de Transformers?
   - *Pausa 1.*

2. **Intuição — A Esfera Pesada no Vale Estreito** (~8 min)
   - Visualização física: uma partícula puntual sem massa (GD) segue instantaneamente o vetor força local; uma esfera com massa $m$ (Momento) acumula velocidade e quantidade de movimento linear.
   - Forças laterais oscilantes possuem média temporal próxima de zero ($\sum g_{\perp} \approx \mathbf{0}$): a inércia anula as oscilações transversais.
   - Forças longitudinais ao longo do vale apontam consistentemente na mesma direção ($\sum g_{\parallel} > 0$): a velocidade acelera até atingir a velocidade terminal de equilíbrio viscoso.

3. **Bloco 1: A Física da Inércia e o Momento de Polyak (*Heavy-Ball*)** (~25 min)
   - Formulação discreta da equação diferencial de amortecimento viscoso:
     $$m \ddot{\mathbf{w}}(t) + \gamma \dot{\mathbf{w}}(t) + \nabla f(\mathbf{w}(t)) = \mathbf{0}$$

   - Discretização de Euler com passo $\Delta t$:
     $$\mathbf{v}_{k+1} = \beta \mathbf{v}_k - \alpha \nabla f(\mathbf{w}_k)$$
     $$\mathbf{w}_{k+1} = \mathbf{w}_k + \mathbf{v}_{k+1} = \mathbf{w}_k - \alpha \nabla f(\mathbf{w}_k) + \beta (\mathbf{w}_k - \mathbf{w}_{k-1})$$

   - Análise Espectral em Formas Quadráticas $f(\mathbf{w}) = \frac{1}{2}\mathbf{w}^T H \mathbf{w}$:
     - Relembrando a Aula 8: no GD, o erro evoluía como sistema dinâmico linear de 1ª ordem desacoplado nos autovetores de $H$, gerando dinâmicas escalares 1D $e_{k+1, i} = (1 - \alpha \lambda_i) e_{k, i}$ (matriz de transição $1 \times 1$).
     - Com o momento de Polyak, a dependência temporal de dois passos ($\mathbf{e}_k$ e $\mathbf{e}_{k-1}$) gera uma equação de diferenças de 2ª ordem.
     - Aumento do espaço de estados: definindo o vetor conjunto $\begin{bmatrix} e_{k, i} \\ e_{k-1, i} \end{bmatrix} \in \mathbb{R}^2$ (posição e memória), convertemos a recorrência de 2ª ordem em um sistema matricial de 1ª ordem em dimensão 2:
       $$\begin{bmatrix} e_{k+1, i} \\ e_{k, i} \end{bmatrix} = \begin{bmatrix} 1 + \beta - \alpha \lambda_i & -\beta \\ 1 & 0 \end{bmatrix} \begin{bmatrix} e_{k, i} \\ e_{k-1, i} \end{bmatrix}$$

     - Polinômio característico: $\mu^2 - (1 + \beta - \alpha \lambda_i)\mu + \beta = 0$.
     - Raízes complexas conjugadas: quando o discriminante é não-positivo, o módulo das raízes é identicamente $|\mu| = \sqrt{\beta}$ para todos os autovalores no intervalo!
     - Escolha ótima dos hiperparâmetros (Polyak, 1964):
       $$\alpha^\star = \frac{4}{(\sqrt{\lambda_{\max}} + \sqrt{\lambda_{\min}})^2}, \quad \beta^\star = \left(\frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1}\right)^2$$

     - Fator assintótico de contração:
       $$\rho_{\text{Polyak}} = \frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1} \approx 1 - \frac{2}{\sqrt{\kappa}}$$
       (Contraste com o GD puro: $\rho_{\text{GD}} \approx 1 - \frac{2}{\kappa}$).

   - *Transição:* Se a esfera desce veloz pelo vale, o que acontece quando o terreno faz uma curva fechada ou quando ela chega perto do fundo? Ela passa direto (*overshoot*). Como remediar isso?
   - *Pausa 2.*

4. **Bloco 2: O Gradiente Acelerado de Nesterov (NAG) e a Cota Ótima** (~22 min)
   - O problema do momento clássico: acúmulo de velocidade cega baseado na inclinação do ponto atual $\mathbf{w}_k$.
   - A ideia visionária de Yurii Nesterov (1983): primeiro saltar na direção da inércia até o ponto antecipado $\mathbf{w}_k + \beta \mathbf{v}_k$ (*look-ahead*), e avaliar a derivada **lá na frente**:
     $$\mathbf{v}_{k+1} = \beta \mathbf{v}_k - \alpha \nabla f(\mathbf{w}_k + \beta \mathbf{v}_k)$$
     $$\mathbf{w}_{k+1} = \mathbf{w}_k + \mathbf{v}_{k+1}$$

   - Interpretação geométrica:
     - Se o ponto antecipado já começou a subir a encosta oposta do vale, o gradiente $\nabla f(\mathbf{w}_k + \beta \mathbf{v}_k)$ apontará contra a velocidade atual, atuando como um freio preventivo.
   - Cota inferior de complexidade para otimização de primeira ordem de funções convexas $L$-suaves:
     - Teorema de Nesterov: Nenhum método de gradiente de 1ª ordem pode convergir mais rápido que $\mathcal{O}(1/k^2)$.
     - O Gradiente Descendente atinge apenas $\mathcal{O}(1/k)$.
     - O NAG atinge a cota ótima teórica $\mathcal{O}(1/k^2)$ com sequência dinâmica de momento $\beta_k = \frac{k-1}{k+2}$.
   - *Transição:* Temos agora duas ferramentas poderosas: escalas adaptativas de 2ª ordem (RMSProp) e inércia aceleradora de 1ª ordem (Polyak/Nesterov). Como fundir ambas de forma matematicamente consistente?
   - *Pausa 3.*

5. **Bloco 3: A Grande Síntese — O Otimizador Adam** (~25 min)
   - A arquitetura do Adam (*Adaptive Moment Estimation*, Kingma & Ba, 2014):
     - $m_t$: média móvel exponencial dos gradientes (1º momento — velocidade/inércia).
     - $v_t$: média móvel exponencial dos quadrados dos gradientes (2º momento — curvatura diagonal).
   - Equações fundamentais:
     $$m_t = \beta_1 m_{t-1} + (1 - \beta_1) g_t$$
     $$v_t = \beta_2 v_{t-1} + (1 - \beta_2) g_t^2$$

   - Dedução rigorosa da **Correção de Viés de Inicialização**:
     - Como $m_0 = \mathbf{0}$, expandindo recursivamente:
       $$m_t = (1 - \beta_1) \sum_{i=1}^t \beta_1^{t-i} g_i$$

     - Tomando a esperança sob a premissa de distribuição estacionária $\mathbb{E}[g_i] \approx \mathbb{E}[g_t]$:
       $$\mathbb{E}[m_t] = \mathbb{E}[g_t] (1 - \beta_1) \sum_{i=1}^t \beta_1^{t-i} = \mathbb{E}[g_t] (1 - \beta_1) \frac{1 - \beta_1^t}{1 - \beta_1} = \mathbb{E}[g_t] (1 - \beta_1^t)$$

     - Portanto, o estimador não viesado é:
       $$\hat{m}_t = \frac{m_t}{1 - \beta_1^t}, \quad \hat{v}_t = \frac{v_t}{1 - \beta_2^t}$$

     - O perigo sem a correção: para $\beta_2 = 0{,}999$ e $t=1$, $v_1 = 0{,}001 g_1^2 \implies \sqrt{v_1} \approx 0{,}031 |g_1|$. O passo seria multiplicado artificialmente por $\approx 31$, provocando explosão ou instabilidade nos passos iniciais!
   - Atualização final do Adam:
     $$\mathbf{w}_{t+1} = \mathbf{w}_t - \frac{\alpha}{\sqrt{\hat{v}_t} + \epsilon} \hat{m}_t$$

   - Hiperparâmetros canônicos recomendados na literatura: $\alpha = 10^{-3}, \beta_1 = 0{,}9, \beta_2 = 0{,}999, \epsilon = 10^{-8}$.
   - *Pausa 4.*

6. **Bloco 4: A Correção Crítica — Do $L_2$ Regularization ao AdamW** (~12 min)
   - A armadilha do $L_2$ em otimizadores adaptativos:
     - Adicionar penalidade $\frac{\lambda}{2}\|\mathbf{w}\|^2$ à perda altera o gradiente para $\tilde{g}_t = g_t + \lambda \mathbf{w}_t$.
     - No GD clássico, isso equivale a subtrair $\alpha \lambda \mathbf{w}_t$ (*weight decay* puro).
     - No Adam, o termo regularizado entra no cálculo de $v_t$ e é dividido por $\sqrt{\hat{v}_t} + \epsilon$:
       $$\mathbf{w}_{t+1} = \mathbf{w}_t - \frac{\alpha}{\sqrt{\hat{v}_t} + \epsilon} \left(\hat{m}_t + \frac{\lambda \mathbf{w}_t}{1 - \beta_1^t}\right)$$

     - Parâmetros com gradientes frequentes e volumosos ($\hat{v}_t$ grande) sofrem regularização praticamente nula!
     - Parâmetros esparsos ou com gradientes pequenos sofrem penalidade desproporcional.
   - A formulação do AdamW (Loshchilov & Hutter, 2019):
     - Desacoplamento estrito do decaimento de peso da atualização adaptativa:
       $$\mathbf{w}_{t+1} = \mathbf{w}_t - \alpha \lambda \mathbf{w}_t - \frac{\alpha}{\sqrt{\hat{v}_t} + \epsilon} \hat{m}_t$$

     - Cada parâmetro decai proporcionalmente à sua magnitude original, restaurando a semântica da regularização Euclidiana.
     - Por que todo modelo moderno de IA (GPT, LLaMA, ResNet) usa AdamW e não Adam com $L_2$.

7. **Fechamento** (~6 min)
   - *Retomando as 4 Perguntas:* Quadro-resumo comparativo (GD vs. Polyak vs. Nesterov vs. RMSProp vs. Adam vs. AdamW).
   - *O Que Fica em Aberto:* O AdamW domina o treinamento de parâmetros de pesos e biases, mas trata cada peso como um escalar independente na diagonal. Em redes neurais, os pesos são matrizes e tensores com correlações estruturadas ricas entre linhas e colunas.
   - *Ponte para a Aula 13:* Como construir precondicionadores estruturados que capturam a geometria matricial dos pesos sem explodir a complexidade? $\to$ **Aula 13: Precondicionamento Estruturado e Ortogonalização Matricial (Shampoo & Muon)**.

