# Respostas e Guia Docente — Pausas da Aula 13

Este documento reúne as resoluções detalhadas, as deduções analíticas completas e o gabarito comentado dos testes conceituais (Verdadeiro ou Falso) das quatro Pausas da **Aula 13: Precondicionamento Estruturado e Ortogonalização Matricial (Shampoo & Muon)**.

---

## Pausa 1: A Limitação da Diagonalização e o Custo do Hessiano Completo

### 1. Resolução da Pergunta Aberta
*Cenário:* Uma matriz de pesos de projeção de atenção em um Transformer moderno possui dimensões $W \in \mathbb{R}^{m \times n}$ com $m = n = 4.096$.
1. **Número de parâmetros:** $d = m \times n = 4.096 \times 4.096 = 16.777.216 \approx 1{,}68 \times 10^7$ parâmetros (16,8M de pesos).
2. **Dimensão do Hessiano completo:**
   $$\dim(H) = d \times d = (mn) \times (mn) \approx (1{,}68 \times 10^7) \times (1{,}68 \times 10^7) \approx 2{,}8 \times 10^{14} \text{ entradas!}$$
   Armazenar essa matriz em precisão simples FP32 (4 bytes por elemento) exigiria:
   $$\text{Memória} = 2{,}8 \times 10^{14} \times 4 \text{ bytes} \approx 1{,}12 \times 10^{15} \text{ bytes} \approx 1.120 \text{ Terabytes (1,12 Petabytes!)}$$
   Em uma GPU H100 com 80 GB de VRAM, seriam necessárias mais de **14.000 GPUs** apenas para guardar o Hessiano de uma única camada de pesos!
3. **Custo de Inversão:** Inverter essa matriz requer $\mathcal{O}(d^3) = \mathcal{O}((mn)^3) \approx (1{,}68 \times 10^7)^3 \approx 4{,}7 \times 10^{21}$ operações de ponto flutuante (FLOPs), tornando o método de Newton completo absolutamente impossível.
4. **O Compromisso do AdamW:** O AdamW contorna essa barreira guardando apenas a diagonal principal ($d = 16,8 \times 10^6$ números $\approx 67 \text{ MB}$). O preço pago é severo: o AdamW descarta $99{,}999994\%$ da geometria de curvatura cruzada, assumindo que as interações entre neurônios são completamente nulas.

### 2. Gabarito Comentado dos Testes Conceituais (V/F)

*   **(A) Verdadeiro.** Ao estimar a curvatura via $v_{ij} \approx (\nabla_{W_{ij}} \mathcal{L})^2$ elemento a elemento, o AdamW assume que o Hessiano é puramente diagonal ($H \approx \text{diag}(\mathbf{v})$), ignorando correlações cruzadas entre pesos distintos.
*   **(B) Falso.** A matriz Hessiana completa do vetor de pesos achatado tem dimensão $(mn) \times (mn)$. Sua inversão consome $\mathcal{O}((mn)^3) = \mathcal{O}(m^3 n^3)$ operações, e não $\mathcal{O}(m^3 + n^3)$.
*   **(C) Verdadeiro.** Pesos localizados na mesma linha $i$ de $W$ conectam-se às mesmas entradas $\mathbf{x}$; as derivadas parciais $\frac{\partial \mathcal{L}}{\partial W_{ij}}$ compartilham o sinal de erro $\delta_i$ e as ativações $x_j$, gerando forte covariância estruturada não-diagonal.
*   **(D) Falso.** Achatar $W$ em um vetor $\text{vec}(W)$ destrói as propriedades matriciais de posto, autovalores e normas de operadores lineares, tratando $W$ como uma coleção desordenada de coeficientes sem estrutura geométrica.

---

## Pausa 2: Precondicionamento Estruturado via Fatoração de Kronecker (Shampoo)

### 1. Resolução da Pergunta Aberta
*Cenário:* Para mitigar o custo intratável do Hessiano completo sem cair na simplificação excessiva da diagonalização, o algoritmo Shampoo propõe o modelo de Kronecker $H \approx L \otimes R$.
1. **Dimensão e Armazenamento das Covariâncias:**
   - Covariância esquerda (entre saídas): $L = \mathbb{E}[G G^T] \in \mathbb{R}^{m \times m} = 4.096 \times 4.096 \implies 16{,}8 \times 10^6 \text{ entradas} \approx 67 \text{ MB}$.
   - Covariância direita (entre entradas): $R = \mathbb{E}[G^T G] \in \mathbb{R}^{n \times n} = 4.096 \times 4.096 \implies 16{,}8 \times 10^6 \text{ entradas} \approx 67 \text{ MB}$.
   - **Armazenamento total do Shampoo:** $67 + 67 = 134 \text{ MB}$ (perfeitamente viável em qualquer GPU moderna, contra 1,12 Petabytes do Hessiano completo!).
2. **Custo Computacional da Inversão:**
   A inversão das matrizes estruturadas requer inverter $L$ e $R$ separadamente:
   $$\text{Custo} = \mathcal{O}(m^3 + n^3) = 2 \times (4.096)^3 \approx 2 \times 6{,}87 \times 10^{10} \approx 1{,}37 \times 10^{11} \text{ FLOPs}$$
   Isso representa uma redução de mais de **10 ordens de grandeza** em relação aos $4{,}7 \times 10^{21}$ FLOPs do método de Newton clássico!
3. **Por que a Raiz Quarta $L^{-1/4}$ e $R^{-1/4}$?**
   Pelas propriedades do produto de Kronecker: $(L \otimes R)^{-1/2} = L^{-1/2} \otimes R^{-1/2}$. Ao aplicar esse operador linear bidimensional sobre a matriz de gradiente $G$, a identidade de vetorização estabelece que:
   $$(L^{-1/2} \otimes R^{-1/2})\text{vec}(G) = \text{vec}\left( R^{-1/4} G L^{-1/4} \right) \quad \text{ou na convenção padrão} \quad L^{-1/4} G R^{-1/4}$$
   A raiz quarta nas matrizes marginais garante que o operador conjunto no espaço completo atue com a raiz quadrada inversa correta do precondicionamento de segunda ordem!

### 2. Gabarito Comentado dos Testes Conceituais (V/F)

*   **(A) Verdadeiro.** O algoritmo Shampoo assume que a curvatura de segunda ordem da transformação bilinear pode ser aproximada pelo produto de Kronecker das covariâncias marginais $H \approx L \otimes R$.
*   **(B) Verdadeiro.** Aplicar a raiz quarta inversa $L^{-1/4}$ decompõe $L$ espectralmente ($L = V \Lambda V^T$) e calcula $\Lambda^{-1/4}$ em seus autovalores positivos.
*   **(C) Falso.** Inverter matrizes a cada passo ainda seria custoso em GPUs. Na prática, o Shampoo atualiza a decomposição e as raízes quartas apenas uma vez a cada $K$ passos (e.g., $K = 50$ ou $100$), amortizando o custo computacional para menos de $1\%$ do tempo total de treino.
*   **(D) Verdadeiro.** $L = \mathbb{E}[G G^T]$ mensura a correlação espacial entre as linhas (espaço de ativações de saída), enquanto $R = \mathbb{E}[G^T G]$ mensura a correlação entre as colunas (espaço de representações de entrada).

---

## Pausa 3: Decomposição Polar e Projeção no Grupo Ortogonal

### 1. Resolução da Pergunta Aberta
*Cenário:* Uma matriz de gradiente $G \in \mathbb{R}^{m \times n}$ possui valores singulares heterogêneos $\boldsymbol{\sigma}(G) = [100{,}0; \, 10{,}0; \, 0{,}1]$.
1. **Problema de Procrustes Ortogonal:**
   O problema de encontrar a matriz ortogonal $U \in \mathbb{R}^{m \times n}$ ($U^T U = I$) mais próxima de $G$ na norma de Frobenius:
   $$\min_{U^T U = I} \|U - G\|_F^2$$
   possui solução analítica única dada pelo fator ortogonal da **Decomposição Polar** de $G$ (Aula 5):
   $$U = G (G^T G)^{-1/2}$$
2. **Espectro de Valores Singulares de $U$:**
   Se $G = V_1 \Sigma V_2^T$ é a SVD de $G$, então $U = V_1 V_2^T$. Portanto:
   $$\boldsymbol{\sigma}(U) = [1{,}0; \, 1{,}0; \, 1{,}0]$$
   Todos os valores singulares da atualização são rigorosamente unitários!
3. **Efeito Estabilizador em Redes Profundas:**
   Em Transformers com dezenas de camadas residuais ($x_{l+1} = x_l + f(W_l x_l)$), se uma matriz de atualização tiver valor singular $\sigma_{\max} = 100$, ela amplifica brutalmente certas direções de ativação, provocando explosão de ativações (*activation blowup*). Se $\sigma_{\min} = 0{,}1$, outras direções são amortecidas excessivamente.
   Ao projetar $G \to U$, a norma espectral da atualização fica estritamente limitada: $\|U\|_2 = 1$. Nenhuma direção é superaquecida e nenhuma direção colapsa, garantindo fluxo homogêneo de sinal por todas as camadas!

### 2. Gabarito Comentado dos Testes Conceituais (V/F)

*   **(A) Verdadeiro.** Pelo Teorema da Decomposição Polar (Aula 5), qualquer matriz real retangular com $m \ge n$ pode ser fatorada unicamente como $G = U P$, onde $U$ possui colunas ortonormais ($U^T U = I$) e $P = (G^T G)^{1/2}$ é simétrica semidefinida positiva.
*   **(B) Verdadeiro.** A fórmula explícita do fator polar é $U = G P^{-1} = G(G^T G)^{-1/2}$.
*   **(C) Verdadeiro.** Como $U = V_1 V_2^T$, a multiplicação de matrizes ortogonais preserva as normas e comprimentos euclidianos, fixando todos os valores singulares em $\sigma_i = 1$.
*   **(D) Falso.** A computação da SVD clássica exige rotinas iterativas de autovalores (algoritmos de QR/bidiagonalização de Golub-Kahan) com branches condicionais e acessos aleatórios à memória, incompatíveis com o paralelismo massivo e determinístico das Tensor Cores de GPUs.

---

## Pausa 4: Iterações de Newton-Schulz e o Otimizador Muon

### 1. Resolução da Pergunta Aberta
*Cenário:* Iteração polinomial de Newton-Schulz para calcular o fator polar ortogonal sem recorrer à SVD:
$$X_{k+1} = \frac{1}{2} X_k (3I - X_k^T X_k)$$
1. **Dinâmica Escalar nos Valores Singulares:**
   Como $X_k = V_1 \Sigma_k V_2^T$, a iteração desacopla diagonalmente para cada valor singular $\sigma_k$:
   $$\sigma_{k+1} = \frac{1}{2} \sigma_k (3 - \sigma_k^2)$$
   - Seja $\sigma_0 = 0{,}5$:
     $$\sigma_1 = \frac{1}{2}(0{,}5)(3 - 0{,}25) = 0{,}25 \times 2{,}75 = 0{,}6875$$
     $$\sigma_2 = \frac{1}{2}(0{,}6875)(3 - (0{,}6875)^2) = 0{,}34375 \times (3 - 0{,}47265) = 0{,}34375 \times 2{,}52734 \approx 0{,}8687$$
     $$\sigma_3 = \frac{1}{2}(0{,}8687)(3 - 0{,}7546) = 0{,}43435 \times 2{,}2454 \approx 0{,}9753$$
     $$\sigma_4 \approx 0{,}9990, \quad \sigma_5 \approx 0{,}999999$$
   Com apenas 5 iterações, o valor singular converge para $1{,}0$ com precisão quase exata!
2. **Convergência Cúbica:** O ponto fixo $\sigma = 1$ possui derivada primeira e segunda nulas para o resíduo $e_k = 1 - \sigma_k$: $e_{k+1} \approx \frac{3}{2} e_k^2$ ou ordem cúbica $e_{k+1} \approx \mathcal{O}(e_k^3)$. O número de dígitos de precisão triplica a cada passo!
3. **Por que roda na velocidade nativa do hardware?** A equação de Newton-Schulz consiste exclusivamente em:
   - Uma multiplicação matricial $A = X_k^T X_k$;
   - Uma subtração escalar $B = 3I - A$;
   - Uma multiplicação matricial $X_{k+1} = \frac{1}{2} X_k B$.
   Toda a computação resume-se a operações de multiplicação matricial densa (GEMM), executadas a centenas de teraflops em FP16/BF16 nas Tensor Cores sem transferências de memória nem dependências seriais!

### 2. Gabarito Comentado dos Testes Conceituais (V/F)

*   **(A) Verdadeiro.** A iteração de Newton-Schulz elimina qualquer necessidade de cálculo explícito de autovalores ou inversão matricial, expressando a projeção ortogonal estritamente por multiplicações de matrizes (GEMM).
*   **(B) Verdadeiro.** A função cúbica $f(\sigma) = \frac{1}{2}\sigma(3-\sigma^2)$ é estável se e somente se o valor singular inicial pertencer ao intervalo aberto $(0, \sqrt{3})$. Para $\sigma \ge \sqrt{3}$, a iteração diverge. Daí a necessidade de normalizar $X_0 = G / \|G\|_F$.
*   **(C) Falso.** O Muon é projetado especificamente para tensores de pesos bidimensionais ($W \in \mathbb{R}^{m \times n}$); vetores unidimensionais (como biases, parâmetros de LayerNorm e matrizes de embedding) não possuem estrutura de linha/coluna equivalente e continuam sendo otimizados com AdamW padrão.
*   **(D) Verdadeiro.** Em testes extensivos (como no NanoGPT e benchmarks de Transformers), o Muon alcança a mesma perplexidade de validação consumindo entre $1{,}5\times$ e $2\times$ menos iterações de treino do que o AdamW sob a mesma taxa de transferência de hardware.
