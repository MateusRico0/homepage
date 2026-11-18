# Respostas e Guia Docente — Pausas da Aula 12

Este documento reúne as resoluções detalhadas, as deduções analíticas completas e o gabarito comentado dos testes conceituais (Verdadeiro ou Falso) das quatro Pausas da **Aula 12: Redes Neurais e Aprendizado de Representação**.

---

## Pausa 1: O Dilema dos Atributos Manuais e a Representação Latente

### 1. Resolução da Pergunta Aberta
*Cenário:* Considere o clássico problema do XOR ou de dois círculos concêntricos no plano $\mathbb{R}^2$. Em um modelo linear ou regressão logística clássica com atributos originais $\mathbf{x} = (x_1, x_2)^T$, é matematicamente impossível traçar uma reta que separe as duas classes.
1. Como a SVM resolve essa limitação e qual é o seu custo?
2. Como uma rede neural de duas camadas com ativação ReLU resolve o problema a partir dos dados?

- **A Abordagem da SVM:**
  A SVM contorna a não-linearidade projetando os dados em um espaço de características $\mathcal{H}$ através de uma função analítica pré-estabelecida $\boldsymbol{\phi}(\mathbf{x})$ ou um kernel de Mercer $k(\mathbf{x}, \mathbf{z}) = \langle \boldsymbol{\phi}(\mathbf{x}), \boldsymbol{\phi}(\mathbf{z}) \rangle$ (por exemplo, um kernel RBF Gaussiano com largura de banda $\gamma$).

  - *Vantagem:* A otimização dual de Wolfe é estritamente convexa, garantindo mínimo global único.
  - *Gargalo:* O kernel é estático e deve ser escolhido *a priori* pelo engenheiro humano. Ele é cego à semântica dos dados e não aprende estruturas hierárquicas. Em dados perceptuais complexos (imagens com milhões de pixels, áudio ou texto), nenhum kernel analítico simples consegue capturar as invariâncias espaciais e temporais necessárias.

- **A Abordagem do Perceptron Multicamadas (MLP):**
  A camada oculta projeta a entrada $\mathbf{x}$ em um vetor de variáveis latentes $\mathbf{z} = \text{ReLU}(W^{(1)}\mathbf{x} + \mathbf{b}^{(1)})$.

  - Geometricamente, cada neurônio $j$ define um hiperplano divisório $W_{j, :}^{(1)}\mathbf{x} + b_j = 0$ que "dobra" o espaço euclidiano através da não-linearidade da ReLU ($\max(0, a)$).
  - A combinação de múltiplos hiperplanos deforma o espaço de entrada de tal forma que, no espaço latente $\mathbf{z}$, as regiões pertencentes à classe positiva são agrupadas em um setor convexo, tornando-as **linearmente separáveis** pela camada final $W^{(2)}\mathbf{z} + b^{(2)}$.
  - *A Grande Vantagem:* Os pesos $W^{(1)}$ que definem os atributos latentes são calibrados conjuntamente por gradiente descendente para minimizar a perda final. A rede aprende automaticamente a melhor representação $\boldsymbol{\phi}(\mathbf{x}; W^{(1)})$ específica para a tarefa!

### 2. Gabarito Comentado dos Testes Conceituais (V/F)

*   **(A) Verdadeiro.** Na regressão polinomial e na SVM, a função de mapeamento $\boldsymbol{\phi}(\mathbf{x})$ é fixa a priori; no MLP, cada camada oculta atua como uma transformação adaptativa parametrizada $\mathbf{z} = h(W\mathbf{x} + \mathbf{b})$, cujos pesos são otimizados diretamente pelos dados.
*   **(B) Falso.** Se todas as funções de ativação forem lineares ($h(a) = a$), uma rede com $L$ camadas colapsa algebricamente em uma única transformação afim: $W^{(L)} W^{(L-1)} \cdots W^{(1)} \mathbf{x} = \tilde{W} \mathbf{x}$, perdendo completamente a capacidade de representar funções não lineares.
*   **(C) Verdadeiro.** Cada neurônio com ativação ReLU divide o espaço de entrada em duas regiões (ativa e inativa), e a combinação de múltiplos neurônios particiona o domínio em um poliedro de funções afins por partes (*piecewise linear*).
*   **(D) Falso.** Em redes neurais profundas, a função de custo em relação a todos os parâmetros $W^{(l)}$ é altamente **não-convexa**, possuindo múltiplos mínimos locais, pontos de sela e vales degenerados induzidos por simetrias de permutação de neurônios.

---

## Pausa 2: Teorema da Aproximação Universal e Redes Profundas

### 1. Resolução da Pergunta Aberta
*Cenário:* O Teorema da Aproximação Universal (Cybenko, 1989; Hornik, 1991) prova que uma rede neural com **apenas uma única camada oculta** e número finito de neurônios não lineares consegue aproximar qualquer função contínua em compactos de $\mathbb{R}^d$ com precisão arbitrariamente alta $\epsilon > 0$.
Por que, então, a indústria e a pesquisa abandonaram redes rasas de uma única camada oculta em favor de **redes neurais profundas** (*Deep Neural Networks*) com dezenas ou centenas de camadas?

- **A Distinção entre Existência Teórica e Viabilidade Computacional:**
  O teorema é um resultado puramente de existência não-construtivo: ele afirma que existe um número finito $M$ de neurônios que aproxima $f$, mas não estabelece limites práticos sobre o tamanho de $M$. Em muitas funções elementares (como paridade de $d$ bits ou funções com simetrias combinatórias), para que uma rede rasa de 1 camada oculta atinja erro $\epsilon$, o número de neurônios necessários escala exponencialmente com a dimensão de entrada: $M \sim \mathcal{O}(2^d)$. Para $d = 100$, $2^{100} \approx 10^{30}$ neurônios, exigindo mais parâmetros e amostras do que átomos no universo visível.

- **A Vantagem Combinatória da Profundidade:**
  Montúfar et al. (2014) demonstraram que, enquanto uma rede rasa com $M$ neurônios particiona o espaço em no máximo $\mathcal{O}(M^d)$ regiões lineares, uma rede profunda com $L$ camadas e $n$ neurônios por camada consegue gerar até $\mathcal{O}((n/d)^{(L-1)d} n^d)$ regiões lineares distintas — um crescimento **exponencial com a profundidade $L$** utilizando apenas $\mathcal{O}(L \cdot n^2)$ parâmetros!

- **Composição Hierárquica de Conceitos:**
  Redes profundas constroem representações distribuídas e hierárquicas: em imagens, a camada 1 detecta bordas e gradientes de luminância; a camada 2 combina bordas em texturas e contornos; a camada 3 agrupa contornos em partes anatômicas (olhos, narizes); e a camada de topo reconhece objetos completos. Essa decomposição reflete a estrutura composicional do mundo físico.

### 2. Gabarito Comentado dos Testes Conceituais (V/F)

*   **(A) Verdadeiro.** O Teorema de Cybenko garante a densidade do espaço de hipóteses gerado por redes com 1 camada oculta no espaço das funções contínuas sobre compactos, desde que a função de ativação seja contínua e não-polinomial.
*   **(B) Falso.** O Teorema da Aproximação Universal garante apenas a *capacidade de representação* (existência de pesos que aproximam $f$); ele não garante que algoritmos de otimização estocástica baseados em gradiente (como SGD ou Adam) conseguirão encontrar esses pesos a partir de dados finitos em tempo polinomial.
*   **(C) Verdadeiro.** A profundidade permite reutilizar recursivamente detectores de atributos intermediários, particionando o espaço em um número exponencial de regiões lineares com um número linear de camadas.
*   **(D) Falso.** A ativação ReLU $\max(0, a)$ supera a sigmoide justamente porque sua derivada na região positiva é constante e unitária ($h'(a) = 1$ para $a > 0$), eliminando o problema do gradiente evanescente (*vanishing gradient*) que paralisa o aprendizado em redes profundas sigmoides.

---

## Pausa 3: Camada de Saída, Família Exponencial e a Ligação Canônica

### 1. Resolução da Pergunta Aberta
*Cenário:* Considere um problema de classificação multiclasse com $K \ge 3$ classes mutualmente exclusivas, onde o alvo $\mathbf{y} \in \{0, 1\}^K$ é um vetor *one-hot* ($\sum_{k=1}^K y_k = 1$). A camada de saída aplica a função de ativação Softmax sobre as ativações pré-sinápticas $\mathbf{a} \in \mathbb{R}^K$:
$$\hat{y}_k = p(y = k \mid \mathbf{x}) = \frac{e^{a_k}}{\sum_{j=1}^K e^{a_j}}$$
A função de perda é a Entropia Cruzada Categórica (negativo da log-verossimilhança):
$$\mathcal{L} = -\sum_{k=1}^K y_k \ln \hat{y}_k$$
Demonstre analiticamente que a derivada da perda em relação à ativação pré-sináptica $a_i$ reduz-se ao resíduo linear exato:
$$\frac{\partial \mathcal{L}}{\partial a_i} = \hat{y}_i - y_i$$

- **Dedução da Derivada da Softmax:**
  Aplicando a regra do quociente para derivar $\hat{y}_k$ em relação a $a_i$:

  - Caso 1: $k = i$:
    $$\frac{\partial \hat{y}_i}{\partial a_i} = \frac{e^{a_i} \sum_j e^{a_j} - e^{a_i} e^{a_i}}{\left(\sum_j e^{a_j}\right)^2} = \frac{e^{a_i}}{\sum_j e^{a_j}} - \left(\frac{e^{a_i}}{\sum_j e^{a_j}}\right)^2 = \hat{y}_i(1 - \hat{y}_i)$$

  - Caso 2: $k \neq i$:
    $$\frac{\partial \hat{y}_k}{\partial a_i} = \frac{0 \cdot \sum_j e^{a_j} - e^{a_k} e^{a_i}}{\left(\sum_j e^{a_j}\right)^2} = -\frac{e^{a_k}}{\sum_j e^{a_j}} \frac{e^{a_i}}{\sum_j e^{a_j}} = -\hat{y}_k \hat{y}_i$$
  Em forma compacta via Delta de Kronecker $\delta_{ki}$:
  $$\frac{\partial \hat{y}_k}{\partial a_i} = \hat{y}_k (\delta_{ki} - \hat{y}_i)$$

- **Dedução da Derivada da Perda $\mathcal{L}$:**
  Pela regra da cadeia:
  $$\frac{\partial \mathcal{L}}{\partial a_i} = -\sum_{k=1}^K y_k \frac{1}{\hat{y}_k} \frac{\partial \hat{y}_k}{\partial a_i} = -\sum_{k=1}^K \frac{y_k}{\hat{y}_k} \left[ \hat{y}_k (\delta_{ki} - \hat{y}_i) \right]$$
  Cancelando o termo $\hat{y}_k$:
  $$\frac{\partial \mathcal{L}}{\partial a_i} = -\sum_{k=1}^K y_k (\delta_{ki} - \hat{y}_i) = -\sum_{k=1}^K y_k \delta_{ki} + \sum_{k=1}^K y_k \hat{y}_i$$
  Como $\delta_{ki} = 1$ apenas quando $k = i$, o primeiro somatório resulta em $-y_i$. Como $\mathbf{y}$ é *one-hot*, $\sum_{k=1}^K y_k = 1$, de modo que o segundo somatório resulta em $\hat{y}_i \sum_{k=1}^K y_k = \hat{y}_i \cdot 1 = \hat{y}_i$.
  Portanto:
  $$\frac{\partial \mathcal{L}}{\partial a_i} = \hat{y}_i - y_i \quad \blacksquare$$

- **Significado Pedagógico:**
  Assim como na Regressão Logística (Aula 6), o casamento entre a distribuição da família exponencial (Multinomial) e sua função de ligação canônica (Softmax) cancela perfeitamente os termos não lineares da derivada, fazendo com que o gradiente seja puramente proporcional à magnitude do erro de predição linear!

### 2. Gabarito Comentado dos Testes Conceituais (V/F)

*   **(A) Verdadeiro.** A minimização da perda quadrática média (MSE) decorre estritamente da máxima verossimilhança sob a premissa de ruído gaussiano homocedástico com média dada pela ativação linear da saída.
*   **(B) Verdadeiro.** A função Softmax atua como uma generalização multivariada da sigmoide logística, garantindo que as saídas $\hat{y}_k$ sejam estritamente positivas e somem 1 ($\sum_k \hat{y}_k = 1$), parametrizando uma distribuição Categórica válida.
*   **(C) Falso.** Sob a ligação canônica (Softmax com Entropia Cruzada), o gradiente na saída é o resíduo linear $\hat{y}_k - y_k$. Quando o modelo comete um erro grave (por exemplo, prediz $\hat{y}_k \approx 0$ quando $y_k = 1$), a magnitude do gradiente atinge seu valor máximo ($|0 - 1| = 1$), fornecendo um sinal de correção vigoroso sem sofrer de saturação.
*   **(D) Verdadeiro.** Em problemas multirrótulo (*multi-label*), onde uma instância pode pertencer a múltiplas classes independentes simultaneamente, a camada final deve empregar $K$ ativações sigmoides independentes (modelando $K$ distribuições de Bernoulli separadas), e não a Softmax (que impõe competição e soma unitária estrita).

---

## Pausa 4: Retropropagação de Erro e Regularização por Dropout

### 1. Resolução da Pergunta Aberta
*Cenário:* Considere uma rede com arquitetura 2-2-1: duas entradas $\mathbf{x} = (x_1, x_2)^T$, uma camada oculta com 2 neurônios com ativação $\text{ReLU}(a) = \max(0, a)$, e uma saída escalar linear $\hat{y} = w_{1}^{(2)} z_1 + w_{2}^{(2)} z_2 + b^{(2)}$ treinada com perda quadrática $\mathcal{L} = \frac{1}{2}(\hat{y} - y)^2$.
Suponha que para um dado exemplo tenhamos resíduo de saída $\delta^{(2)} = \frac{\partial \mathcal{L}}{\partial a^{(2)}} = \hat{y} - y = 4{,}0$. Os pesos da camada de saída são $W^{(2)} = [3{,}0, \, -2{,}0]$ e as ativações pré-sinápticas da camada oculta são $a_1^{(1)} = 1{,}5$ e $a_2^{(1)} = -0{,}8$.
1. Quais são as sensibilidades de erro $\delta_1^{(1)}$ e $\delta_2^{(1)}$ nos neurônios da camada oculta?
2. Como o gradiente do peso $W_{11}^{(1)}$ é calculado se a entrada for $x_1 = 2{,}0$?

- **Cálculo das Sensibilidades Ocultas:**
  A equação da retropropagação é:
  $$\delta_j^{(1)} = h'(a_j^{(1)}) \left( \delta^{(2)} W_j^{(2)} \right)$$
  Para a função de ativação ReLU, $h'(a) = 1$ se $a > 0$ e $h'(a) = 0$ se $a < 0$.

  - Para o neurônio 1: $a_1^{(1)} = 1{,}5 > 0 \implies h'(a_1^{(1)}) = 1$.
    $$\delta_1^{(1)} = 1 \cdot (4{,}0 \times 3{,}0) = \mathbf{12{,}0}$$

  - Para o neurônio 2: $a_2^{(1)} = -0{,}8 < 0 \implies h'(a_2^{(1)}) = 0$.
    $$\delta_2^{(1)} = 0 \cdot (4{,}0 \times (-2{,}0)) = \mathbf{0{,}0}$$
  O neurônio 2 está inativo (na região zero da ReLU); portanto, nenhum gradiente de erro é retropropagado através dele!

- **Cálculo do Gradiente do Peso:**
  Pela regra da cadeia:
  $$\frac{\partial \mathcal{L}}{\partial W_{11}^{(1)}} = \delta_1^{(1)} x_1 = 12{,}0 \times 2{,}0 = \mathbf{24{,}0}$$

### 2. Gabarito Comentado dos Testes Conceituais (V/F)

*   **(A) Verdadeiro.** A sensibilidade de cada camada $\boldsymbol{\delta}^{(l)}$ é obtida multiplicando o vetor de sensibilidade da camada seguinte pelo transposto da matriz de pesos e pelo vetor de derivadas das ativações locais: $\boldsymbol{\delta}^{(l)} = ((W^{(l+1)})^T \boldsymbol{\delta}^{(l+1)}) \odot h'(\mathbf{a}^{(l)})$.
*   **(B) Falso.** O custo computacional da retropropagação de gradientes é proporcional ao número de conexões sinápticas (pesos), escalando linearmente com o tamanho da rede $\mathcal{O}(|W|)$, o que torna o treinamento viável mesmo em modelos com bilhões de parâmetros (Teorema de Baur-Strassen).
*   **(C) Verdadeiro.** Em uma camada com $D$ neurônios, a cada iteração de treino o Dropout sorteia uma máscara binária entre $2^D$ combinações possíveis. Como os parâmetros são compartilhados, o procedimento emula o treinamento de um ensemble massivo de $2^D$ sub-redes esparsas.
*   **(D) Falso.** No momento da inferência/teste, o Dropout é desativado para garantir predições determinísticas sem ruído amostral; para compensar a presença de todos os neurônios, as ativações são multiplicadas pelo fator de escala $(1 - p_{\text{drop}})$ (ou utiliza-se a técnica de *Inverted Dropout* durante o próprio treinamento).

