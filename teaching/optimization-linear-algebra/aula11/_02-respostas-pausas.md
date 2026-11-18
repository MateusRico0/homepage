# Respostas e Guia Docente — Pausas da Aula 11

Este documento reúne as resoluções detalhadas, a justificativa analítica de cada item de Verdadeiro/Falso e diretrizes didáticas para condução das cinco Pausas da **Aula 11: Otimização de Segunda Ordem (Método de Newton) e Precondicionamento Diagonal**.

---

## Pausa 1: A Limitação do Passo Escalar Único

### 1. Resolução da Pergunta Aberta
*Cenário:* $f(w_1, w_2) = \frac{1}{2}(1000 w_1^2 + w_2^2)$.

- **Análise da Hessiana e Autovalores:**
  A Hessiana é constante:
  $$H = \begin{bmatrix} 1000 & 0 \\ 0 & 1 \end{bmatrix}$$
  Os autovalores são $\lambda_1 = 1000$ e $\lambda_2 = 1$. O número de condição é $\kappa = \frac{\lambda_{\max}}{\lambda_{\min}} = 1000$.

- **Teto de Estabilidade do Gradiente Descendente:**
  Pelo Lema da Descida e pela dinâmica espectral de erro ($e_{k+1, i} = (1 - \alpha \lambda_i) e_{k, i}$), para que a sequência convirja em todas as coordenadas sem divergir em $w_1$, devemos impor:
  $$|1 - \alpha \lambda_{\max}| < 1 \iff 0 < \alpha < \frac{2}{\lambda_{\max}} = \frac{2}{1000} = 0{,}002$$

- **Contração da Coordenada Suave ($w_2$):**
  Se escolhermos o passo que maximiza a velocidade em $w_1$ sem oscilar ($\alpha = 1/\lambda_{\max} = 0{,}001$), o fator de contração na coordenada $w_2$ é:
  $$\rho_2 = 1 - \alpha \lambda_2 = 1 - 0{,}001 \times 1 = 0{,}999$$
  O erro em $w_2$ evolui como $e_{k, 2} = (0{,}999)^k e_{0, 2}$.
  Para reduzir o erro por um fator de 10 ($(0{,}999)^k \le 0{,}1$):
  $$k \ge \frac{\ln(0{,}1)}{\ln(0{,}999)} \approx \frac{-2{,}3026}{-0{,}0010005} \approx 2.301\text{ iterações!}$$

- **Conclusão Pedagógica:**
  Enquanto a coordenada $w_1$ atinge o ótimo em 1 único passo sob $\alpha = 0{,}001$, a coordenada $w_2$ exige mais de 2.300 passos para avançar uma única ordem de grandeza. Um passo escalar único força o otimizador a escolher entre a instabilidade catastrófica na direção íngreme ou a paralisia exasperadora na direção suave.

### 2. Gabarito Comentado dos Testes Conceituais (V/F)
*   **(A) Verdadeiro.** A estabilidade assintótica do operador de iteração $(I - \alpha H)$ exige que seu raio espectral seja estritamente menor que 1. Como $\lambda_{\max}$ é o maior autovalor, a condição $|1 - \alpha \lambda_{\max}| < 1$ dita o limite estrito superior $\alpha < 2/\lambda_{\max}$.
*   **(B) Falso.** Ao escolher $\alpha = 1/\lambda_{\max}$, a coordenada com maior curvatura atinge contração instantânea ($1 - \alpha \lambda_{\max} = 0$). Contudo, para a coordenada com menor curvatura ($\lambda_{\min}$), o fator de contração torna-se $1 - \frac{\lambda_{\min}}{\lambda_{\max}} = 1 - \frac{1}{\kappa} \approx 1$, exigindo milhares de passos para convergir.
*   **(C) Falso.** A padronização $Z$-score ($z = (x - \mu)/\sigma$) equaliza apenas as variâncias marginais empíricas das variáveis lineares na entrada. Ela não elimina correlações cruzadas (covariâncias não-nulas fora da diagonal) e não tem poder de uniformizar a curvatura em modelos não-lineares gerais, cuja Hessiana varia a cada ponto $\mathbf{w}$.
*   **(D) Verdadeiro.** Em atributos esparsos (ex.: termos raros em vocabulários), a derivada parcial é nula na imensa maioria das observações. Se a taxa global $\alpha$ for calibrada para não divergir nas palavras frequentes (com gradientes abundantes e acumulados), os pesos das palavras raras quase não se deslocam ao longo do treinamento.

---

## Pausa 2: O Passo de Newton e a Invariância Afim

### 1. Resolução da Pergunta Aberta
*Cenário:* $f(\mathbf{w}) = \frac{1}{2}\mathbf{w}^T A \mathbf{w} - \mathbf{b}^T \mathbf{w}$, com $A \succ 0$.

- **Gradiente e Hessiana Analíticos:**
  $$\nabla f(\mathbf{w}) = A\mathbf{w} - \mathbf{b}, \quad \nabla^2 f(\mathbf{w}) = A$$
- **Aplicação da Fórmula de Newton:**
  $$\mathbf{w}_1 = \mathbf{w}_0 - [\nabla^2 f(\mathbf{w}_0)]^{-1} \nabla f(\mathbf{w}_0) = \mathbf{w}_0 - A^{-1}(A\mathbf{w}_0 - \mathbf{b}) = \mathbf{w}_0 - \mathbf{w}_0 + A^{-1}\mathbf{b} = A^{-1}\mathbf{b}$$
  Como a solução exata das Equações Normais é $\mathbf{w}^\star = A^{-1}\mathbf{b}$, temos $\mathbf{w}_1 = \mathbf{w}^\star$ em exatamente 1 iteração, a partir de qualquer $\mathbf{w}_0 \in \mathbb{R}^d$.
- **Significado Geométrico do Decremento de Newton:**
  $$\lambda(\mathbf{w})^2 = \nabla f(\mathbf{w})^T [\nabla^2 f(\mathbf{w})]^{-1} \nabla f(\mathbf{w})$$
  Ele mede o dobro da queda prevista pela melhor aproximação quadrática local: $f(\mathbf{w}) - \min_{\Delta\mathbf{w}} q(\Delta\mathbf{w}) = \frac{1}{2}\lambda(\mathbf{w})^2$. É uma métrica intrínseca de subotimalidade: quando $\lambda(\mathbf{w}) \le \eta$ (com $\eta$ pequeno), o algoritmo entra no regime quadrático puro.

### 2. Gabarito Comentado dos Testes Conceituais (V/F)
*   **(A) Verdadeiro.** Para uma forma quadrática, a derivada de ordem 3 e todas as subsequentes são identicamente nulas ($\nabla^3 f \equiv \mathbf{0}$). A expansão de Taylor de segunda ordem trunca sem nenhum erro de resíduo, coincidindo exatamente com a função original.
*   **(B) Verdadeiro.** Em termos de análise dimensional, se $w$ possui dimensão $[\text{parâmetro}]$ e $f$ possui unidade $[\text{custo}]$, o gradiente $\nabla f$ possui unidade $[\text{custo}]/[\text{parâmetro}]$ e a Hessiana $H$ tem unidade $[\text{custo}]/[\text{parâmetro}]^2$. Portanto, $H^{-1} \nabla f$ tem unidade $[\text{parâmetro}]^2/[\text{custo}] \times [\text{custo}]/[\text{parâmetro}] = [\text{parâmetro}]$, exatamente a mesma unidade de $w$. O gradiente puro, por outro lado, requer uma taxa $\alpha$ com dimensão artificial para balancear as unidades.
*   **(C) Falso.** O Gradiente Descendente euclidiano depende da métrica adotada. Se fizermos uma mudança de escala $\tilde{\mathbf{w}} = c \mathbf{w}$, o gradiente na nova variável é $\nabla_{\tilde{\mathbf{w}}} f = \frac{1}{c}\nabla_{\mathbf{w}} f$. A trajetória geométrica percorrida pelo GD é alterada (as curvas de nível mudam de excentricidade). Somente o Método de Newton é rigorosamente invariante a qualquer transformação afim inversível.
*   **(D) Verdadeiro.** Como $H \succ 0$, sua inversa também é estritamente definida positiva ($H^{-1} \succ 0$). Pela definição de positividade estrita, $\mathbf{v}^T H^{-1} \mathbf{v} \ge 0$ para todo $\mathbf{v}$, anulando-se apenas se $\mathbf{v} = \mathbf{0}$. Logo, $\lambda(\mathbf{w})^2 = 0 \iff \nabla f(\mathbf{w}) = \mathbf{0}$.

---

## Pausa 3: Patologias de Newton em Alta Dimensão

### 1. Resolução da Pergunta Aberta
*Cenário:* $f(w_1, w_2) = w_1^2 - w_2^2$ a partir de $\mathbf{w}_0 = (1, 1)^T$.

- **Gradiente e Hessiana:**
  $$\nabla f(\mathbf{w}) = \begin{bmatrix} 2w_1 \\ -2w_2 \end{bmatrix} \implies \nabla f(\mathbf{w}_0) = \begin{bmatrix} 2 \\ -2 \end{bmatrix}$$
  $$\nabla^2 f(\mathbf{w}) = \begin{bmatrix} 2 & 0 \\ 0 & -2 \end{bmatrix} \implies [\nabla^2 f(\mathbf{w}_0)]^{-1} = \begin{bmatrix} 1/2 & 0 \\ 0 & -1/2 \end{bmatrix}$$
- **Passo de Newton:**
  $$\Delta\mathbf{w}_{\text{nt}} = -H^{-1}\nabla f(\mathbf{w}_0) = -\begin{bmatrix} 1/2 & 0 \\ 0 & -1/2 \end{bmatrix} \begin{bmatrix} 2 \\ -2 \end{bmatrix} = -\begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} -1 \\ -1 \end{bmatrix}$$
- **Novo Ponto:**
  $$\mathbf{w}_1 = \mathbf{w}_0 + \Delta\mathbf{w}_{\text{nt}} = \begin{bmatrix} 1 \\ 1 \end{bmatrix} + \begin{bmatrix} -1 \\ -1 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$
- **O que aconteceu:**
  $\mathbf{w}_1 = (0, 0)^T$ é o ponto estacionário exato ($\nabla f = \mathbf{0}$), mas este ponto é um **ponto de sela**! Na direção $w_2$, a perda original era $f(1, 1) = 0$. Em $(0, 0)$, $f(0, 0) = 0$. Mas se o ponto inicial fosse $\mathbf{w}_0 = (0, 1)^T$, com $f(0, 1) = -1$, o passo de Newton saltaria para $(0, 0)$ onde $f(0, 0) = 0$, **aumentando a perda** e maximizando a função ao longo da direção de curvatura negativa! Newton é cego à diferença entre mínimos, máximos e selas; ele busca meramente pontos estacionários do modelo quadrático.

### 2. Gabarito Comentado dos Testes Conceituais (V/F)
*   **(A) Verdadeiro.** Se $H$ tem um autovalor $\lambda_i < 0$ com autovetor $\mathbf{u}_i$, e o gradiente possui componente nessa direção, o produto interno é $\nabla f^T \Delta\mathbf{w}_{\text{nt}} = -\nabla f^T H^{-1} \nabla f$. Se a componente na direção negativa dominar, essa quantidade torna-se estritamente positiva, de modo que o passo de Newton aponta na direção de subida da função.
*   **(B) Falso.** A resolução de um sistema linear simétrico de dimensão $d$ via fatoração de Cholesky requer $\frac{1}{3}d^3$ operações de ponto flutuante (tempo $\mathcal{O}(d^3)$) e exige armazenar os $\frac{d(d+1)}{2}$ elementos da matriz triangular (memória $\mathcal{O}(d^2)$).
*   **(C) Verdadeiro.** Pelo Teorema Espectral, se $H = Q\Lambda Q^T$, então $H + \lambda I = Q(\Lambda + \lambda I)Q^T$. Os novos autovalores são $\lambda_i + \lambda$. Se escolhermos $\lambda > |\min_i \lambda_i|$, todos os autovalores tornam-se estritamente positivos, garantindo que a matriz modificada seja positiva definida e invertível.
*   **(D) Falso.** Uma matriz Hessiana densa para $d = 7 \times 10^{10}$ parâmetros conteria $d^2 \approx 4{,}9 \times 10^{21}$ floats. Em float32 (4 bytes), isso totaliza $\approx 1{,}96 \times 10^{22}$ bytes $\approx 19{,}6$ Zetabytes de memória RAM, superando em muitas ordens de grandeza a capacidade de todos os supercomputadores somados.

---

## Pausa 4: Precondicionamento Diagonal

### 1. Resolução da Pergunta Aberta
*Cenário:* Mostrar por que a inversão de $D = \text{diag}(d_1, \dots, d_n)$ custa $\mathcal{O}(d)$ e desacopla a atualização.

- **Inversão de Matriz Diagonal:**
  A inversa de uma matriz diagonal com elementos diagonais não-nulos $d_i \neq 0$ é simplesmente a matriz diagonal com os inversos recíprocos:
  $$D^{-1} = \begin{bmatrix} 1/d_1 & 0 & \dots & 0 \\ 0 & 1/d_2 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & 1/d_n \end{bmatrix}$$
  Calcular os $d$ recíprocos requer exatamente $d$ divisões escalares: complexidade temporal estrita $\mathcal{O}(d)$, sem necessidade de fatoração LU, Cholesky ou eliminações gaussianas.
- **Desacoplamento da Atualização:**
  A multiplicação matriz-vetor $D^{-1}\mathbf{g}$ reduz-se ao produto elemento a elemento (Hadamard):
  $$[D^{-1}\mathbf{g}]_i = \frac{1}{d_i} g_i$$
  Assim, a atualização do parâmetro $w_i$ depende única e exclusivamente do gradiente parcial da sua própria coordenada $g_i$ e do seu fator de escala $d_i$:
  $$w_{i, k+1} = w_{i, k} - \alpha \frac{g_{i, k}}{d_{i, k}}$$
  Nenhuma informação das outras coordenadas $j \neq i$ precisa ser transmitida ou comunicada entre os registradores ou threads de execução.

### 2. Gabarito Comentado dos Testes Conceituais (V/F)
*   **(A) Verdadeiro.** Definindo $\tilde{\mathbf{w}} = D^{1/2}\mathbf{w}$, temos $\tilde{w}_i = \sqrt{D_{ii}} w_i$. O gradiente em relação à nova variável é $\frac{\partial f}{\partial \tilde{w}_i} = \frac{1}{\sqrt{D_{ii}}} \frac{\partial f}{\partial w_i}$. Aplicando o GD na variável $\tilde{\mathbf{w}}$ e convertendo de volta para $\mathbf{w}$, obtém-se exatamente o passo desacoplado $w_{i, k+1} = w_{i, k} - \frac{\alpha}{D_{ii}} \frac{\partial f}{\partial w_i}$.
*   **(B) Falso.** Matrizes diagonais realizam apenas dilatações e contrações paralelas aos eixos canônicos de coordenadas. Como seus termos fora da diagonal são identicamente nulos ($D_{ij} = 0$ para $i \neq j$), elas são absolutamente incapazes de induzir rotações de eixos ou desacoplar variáveis com forte correlação linear mista (Hessianas densas).
*   **(C) Verdadeiro.** Trata-se da chamada *Diagonal Newton / Diagonal Hessian approximation*: adota-se $D = \text{diag}(\nabla^2 f)$. Cada coordenada recebe um passo de Newton unidimensional exato, ignorando termos de curvatura cruzada $\frac{\partial^2 f}{\partial w_i \partial w_j}$.
*   **(D) Falso.** Uma matriz diagonal $d \times d$ possui apenas $d$ elementos não-nulos. Seu armazenamento requer um simples vetor de dimensão $d$, ou seja, espaço de memória linear $\mathcal{O}(d)$, e não quadrático.

---

## Pausa 5: AdaGrad vs RMSProp

### 1. Resolução da Pergunta Aberta
*Cenário:* Por que o AdaGrad é ótimo em dados esparsos mas congela em redes profundas? Como o RMSProp resolve isso?

- **Comportamento do AdaGrad em Dados Esparsos:**
  Em atributos esparsos (ex.: uma palavra rara em processamento de texto), o gradiente associado $g_{t, i}$ é nulo em quase todas as iterações. Portanto, seu acumulador $G_{t, i} = \sum_{\tau=1}^t g_{\tau, i}^2$ permanece muito pequeno. Quando essa palavra rara finalmente aparece no lote, o denominador $\sqrt{G_{t, i}} + \epsilon$ é minúsculo, gerando um passo de aprendizado proporcionalmente muito grande e eficaz para atualizar esse parâmetro raro.
- **A Patologia do Congelamento Precoce:**
  Como cada termo somado é estritamente não-negativo ($g_{\tau, i}^2 \ge 0$), a sequência $G_t$ cresce monotonamente a cada iteração ($G_{t} \ge G_{t-1}$). Em problemas não-convexos e de longa duração (redes neurais profundas com $10^5$ passos), $G_t$ atinge valores enormes mesmo em regiões planas distantes do mínimo. Consequentemente, a taxa efetiva de aprendizado decai assintoticamente para zero ($\frac{\alpha}{\sqrt{G_t}} \to 0$): os parâmetros "congelam" prematuramente no espaço antes de alcançar a bacia do minimizador.
- **A Solução do RMSProp:**
  O RMSProp substitui a soma cumulativa por uma média móvel ponderada exponencialmente:
  $$v_{t, i} = \beta_2 v_{t-1, i} + (1 - \beta_2) g_{t, i}^2$$
  Os gradientes ocorridos há mais de $\approx \frac{1}{1-\beta_2}$ passos são esquecidos exponencialmente. Dessa forma, $v_t$ não cresce indefinidamente; ele rastreia a variância local recente da perda, permitindo que a taxa de aprendizado permaneça ativa e se expanda caso o modelo entre em um vale plano.

### 2. Gabarito Comentado dos Testes Conceituais (V/F)
*   **(A) Verdadeiro.** Por definição, $G_{t, i} = G_{t-1, i} + g_{t, i}^2$. Como o quadrado de qualquer número real é não-negativo ($g^2 \ge 0$), segue diretamente que $G_{t, i} \ge G_{t-1, i}$ para todo $t$ e todo $i$.
*   **(B) Verdadeiro.** Se o gradiente não for identicamente nulo, a série $\sum_{\tau=1}^\infty g_{\tau, i}^2$ diverge para o infinito em trajetórias gerais que não estacionaram, fazendo o denominador tender a infinito e o passo efetivo tender a zero.
*   **(C) Verdadeiro.** Expandindo a recursão da EMA, $v_t = (1-\beta_2)\sum_{k=0}^t \beta_2^k g_{t-k}^2$. A base de decaimento exponencial tem meia-vida correspondente a uma janela temporal efetiva de aproximadamente $\frac{1}{1-\beta_2}$ iterações (para $\beta_2 = 0{,}99$, a memória foca nos últimos 100 passos).
*   **(D) Falso.** O RMSProp é um algoritmo estritamente de primeira ordem. Ele nunca avalia a segunda derivada nem computa aproximações por diferenças finitas; ele utiliza exclusivamente os gradientes de primeira ordem estocásticos $g_t$ obtidos diretamente via retropropagação reversa.

