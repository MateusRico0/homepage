## Resumo — Aula 12: Redes Neurais e Aprendizado de Representação

A Aula 11 explorou as Máquinas de Vetores de Suporte (SVM), demonstrando como fronteiras não lineares altamente sofisticadas podem ser obtidas através do Truque do Kernel no espaço de Hilbert de dimensão infinita. Contudo, a SVM e os Modelos Lineares Generalizados (GLMs) compartilham uma restrição arquitetural idêntica: **a transformação não linear dos atributos $\boldsymbol{\phi}(\mathbf{x})$ é fixada a priori pelo engenheiro** (seja via funções base polinomiais ou via um kernel de Mercer analítico como o RBF). Se o kernel escolhido não capturar a geometria intrínseca dos dados, o modelo falha em generalizar.

Esta aula encerra a disciplina conectando todos os conceitos fundamentais do curso através dos **Perceptrons Multicamadas (*Multilayer Perceptrons* - MLPs)** e da teoria do **Aprendizado de Representação (*Representation Learning*)**. Em vez de tratar redes neurais como "caixas pretas misteriosas", adotamos a perspectiva estatística rigorosa (Bishop, PRML §5; Bishop & Bishop, DLFC §3): uma rede neural profunda nada mais é do que uma **composição hierárquica e encadeada de Modelos Lineares Generalizados (GLMs)**, na qual cada camada oculta atua como um extrator adaptativo de variáveis latentes $\mathbf{z}^{(l)} = h(W^{(l)}\mathbf{z}^{(l-1)} + \mathbf{b}^{(l)})$, ajustado conjuntamente com o preditor final.

Iniciamos provando o **Teorema da Aproximação Universal** (Cybenko, 1989; Hornik, 1991), que estabelece a completude representacional de redes com uma única camada oculta, contrastando a largura exponencial exigida em redes rasas contra a eficiência parsimoniosa de representações hierárquicas profundas. Em seguida, conectamos formalmente a camada de saída à **teoria da verossimilhança estatística**: demonstramos que saídas lineares com perda $L_2$ decorrem do ruído Gaussiano, ativações sigmoides com perda de Entropia Cruzada Binária modelam a família de Bernoulli, e a ativação **Softmax** parametriza distribuições Multinomiais/Categóricas, onde a ligação canônica preserva o elegante resíduo linear $\delta_k = \hat{y}_k - y_k$. No Bloco 3, deduzimos analiticamente o algoritmo de **Retropropagação (*Backpropagation*)** a partir da regra da cadeia multivariada em notação de sensibilidades $\delta_j^{(l)}$, detalhando a propagação de erro do topo à base. No Bloco 4, investigamos as técnicas contemporâneas de regularização profunda: decaimento de pesos ($L_2$ / Weight Decay como prior Gaussiana MAP) e o **Dropout** (Srivastava et al., 2014) como um ensemble implícito exponencial de $2^D$ sub-redes com compartilhamento extremo de pesos. Concluímos com a grande síntese da disciplina, mapeando todas as 12 aulas em uma taxonomia comparativa unificada de modelos supervisionados.

**Objetivos:**
1. Formular o Perceptron Multicamadas (MLP) como uma composição encadeada de GLMs, contrastando a aprendizagem adaptativa de atributos $\boldsymbol{\phi}(\mathbf{x}; W)$ com transformações fixas a priori (polinômios e kernels de SVM).
2. Compreender as condições e o alcance do Teorema da Aproximação Universal e justificar por que representações hierárquicas profundas superam redes rasas em complexidade amostral e parsimônia paramétrica.
3. Conectar a camada de saída e a função de perda à Teoria da Máxima Verossimilhança (Gaussiana $\to$ MSE, Bernoulli $\to$ BCE, Multinomial $\to$ Softmax/Entropia Cruzada), demonstrando a propriedade de ligação canônica ($\delta_k = \hat{y}_k - y_k$).
4. Derivar analiticamente as equações da retropropagação (*backpropagation*) via regra da cadeia, implementando o passo forward, o cálculo das sensibilidades $\delta^{(l)}$ e o gradiente das matrizes de pesos.
5. Analisar o mecanismo de regularização por Dropout como um comitê implícito de $2^D$ redes compartilhando pesos e contrastá-lo com a regularização $L_2$ (Weight Decay).

**Pré-requisitos:** Regressão Logística, entropia cruzada e GLMs (Aula 6); Regularização $L_2$ e MAP (Aula 7); Teoria de Ensembles e Bagging (Aula 9); Regra da cadeia multivariada e diferenciação (Aula 9 de Álgebra/Otimização).
**Dataset-fio:** Breast Cancer Wisconsin ($N = 569, d = 30$), utilizando projeção 2D (`mean radius` $\times$ `mean texture`) para visualização contínua das fronteiras de decisão não lineares e do espaço latente oculto $\boldsymbol{\phi}(\mathbf{x})$, e validação comparativa nos 30 atributos contra Regressão Logística, Random Forest, Gradient Boosting e SVM.
**Estratégia Pedagógica:** A (Outside-In) — Da limitação de kernels fixos na SVM $\to$ Arquitetura do MLP como encadeamento de GLMs $\to$ Saídas probabilísticas e Máxima Verossimilhança $\to$ Derivação matemática da Retropropagação $\to$ Regularização (Weight Decay e Dropout) $\to$ Síntese terminal do curso de Aprendizado Supervisionado.

---

## Plano de aula — Aula 12 (carga horária: ~110 min)

1. **Revisão e Introdução** (~12 min)
   - *Revisão:* Da Aula 6 (Regressão Logística como GLM de Bernoulli) e Aula 11 (SVM e o Truque do Kernel para fronteiras não-lineares com kernel analítico fixado a priori).
   - *Ideia Central:* Na SVM ou na regressão polinomial, o engenheiro precisa "adivinhar" o kernel ou a base de expansão correta; em redes neurais, as transformações não lineares intermediárias são parametrizadas e **aprendidas conjuntamente a partir dos próprios dados**.
   - *Problema Motivador:* Em conjuntos de dados com manifolds não-lineares intricados, kernels analíticos padrão (como RBF com $\gamma$ fixo) exigem ajuste fino manual exaustivo ou falham em capturar simetrias locais; uma rede com 2 camadas ocultas deforma o espaço para tornar as classes perfeitamente separáveis por um hiperplano linear.
   - *Roteiro (4 Perguntas Centrais):*
     1. Como interpretar uma rede neural como uma hierarquia encadeada de GLMs e por que isso resolve o gargalo de engenharia manual de atributos (*feature engineering*)?
     2. Como a Teoria da Verossimilhança fundamenta a escolha da camada de saída (Linear, Sigmoide e Softmax) e unifica as funções de custo (MSE e Entropia Cruzada)?
     3. Como a regra da cadeia multivariada deduz o algoritmo de retropropagação e por que a ligação canônica preserva o resíduo linear $\hat{y}_k - y_k$?
     4. Como técnicas contemporâneas de regularização profunda ($L_2$ e Dropout) previnem o sobreajuste em arquiteturas massivamente superparametrizadas?
   - *Pausa Ativa 1.*

2. **Intuição — Deformação do Espaço e Aprendizado de Representação** (~8 min)
   - A metáfora da folha de papel amassada: duas cores de tinta espalhadas em uma folha amassada não podem ser separadas por uma tesoura reta (plano linear). A camada oculta desamassa e estica a folha no espaço latente $\mathbf{z} \in \mathbb{R}^h$, permitindo que a camada final corte as classes com um corte plano trivial.
   - A transição histórica:
     $$\mathbf{x} \xrightarrow{\text{Manual / Fixo}} \boldsymbol{\phi}(\mathbf{x}) \xrightarrow{\text{Linear}} \hat{y} \quad \implies \quad \mathbf{x} \xrightarrow{\text{Aprendido via } W^{(1)}} \mathbf{z} \xrightarrow{\text{Linear via } W^{(2)}} \hat{y}$$

3. **Bloco 1: A Arquitetura do MLP como Composição de GLMs e Teorema de Cybenko** (~25 min)
   - A anatomia de um neurônio artificial:
     $$a_j = \sum_{i=1}^d W_{ji} x_i + b_j = \mathbf{w}_j^T \mathbf{x} + b_j$$
     $$z_j = h(a_j)$$
     onde $a_j$ é a ativação linear pré-sináptica e $h(\cdot)$ é a função de ativação não-linear pós-sináptica.

   - O catálogo de ativações ocultas:
     - Sigmoide Logística $\sigma(a) = \frac{1}{1 + e^{-a}}$ (histórica, saturação bilateral, gradiente evanescente).
     - Tangente Hiperbólica $\tanh(a) = \frac{e^a - e^{-a}}{e^a + e^{-a}}$ (centrada em zero, saturação nos extremos).
     - ReLU (*Rectified Linear Unit*, Nair & Hinton, 2010): $\text{ReLU}(a) = \max(0, a)$ (gradiente não-saturante $\frac{\partial}{\partial a} = 1$ para $a > 0$, esparsidade induzida, computação instantânea).
   - O Teorema da Aproximação Universal (Cybenko, 1989; Hornik, 1991):
     - Seja $h(\cdot)$ uma função contínua não-constante, limitada e sigmoidal (estendida posteriormente para qualquer ativação contínua não-polinomial, incluindo ReLU).
     - Para qualquer função contínua $f: K \to \mathbb{R}$ definida sobre um compacto $K \subset \mathbb{R}^d$ e qualquer tolerância $\epsilon > 0$, existe uma rede com uma única camada oculta com $M < \infty$ neurônios:
       $$F(\mathbf{x}) = \sum_{j=1}^M v_j h(\mathbf{w}_j^T \mathbf{x} + b_j)$$
       tal que $|F(\mathbf{x}) - f(\mathbf{x})| < \epsilon$ para todo $\mathbf{x} \in K$.

   - A armadilha do teorema raso vs. a virtude da profundidade:
     - O teorema garante *existência*, mas não diz se $M$ é computacionalmente viável (em muitos casos, $M$ escala exponencialmente com $d$, $\mathcal{O}(2^d)$).
     - Redes profundas (camadas em cascata) criam composições hierárquicas de funções $f(g(h(\mathbf{x})))$ que particionam o espaço em um número exponencial de regiões lineares por partes com número polinomial de parâmetros (Montúfar et al., 2014).
   - *Pausa Ativa 2.*

4. **Bloco 2: A Camada de Saída sob a Ótica da Verossimilhança Estatística** (~20 min)
   - A tese probabilística aplicada ao preditor final:
     1. **Regressão Real Multivariada:**
        - Ativação linear na saída: $y_k = a_k$.
        - Modelo de ruído: $p(y \mid \mathbf{x}) = \mathcal{N}(y \mid a(\mathbf{x}), \sigma^2 I)$.
        - Máxima Verossimilhança $\implies$ Perda de Erro Quadrático Médio (MSE):
          $$\mathcal{L}(\mathbf{w}) = \frac{1}{2}\sum_{n=1}^N \|y_n - a(\mathbf{x}_n)\|^2$$
     2. **Classificação Binária:**
        - Ativação sigmoide: $\hat{y} = \sigma(a) = \frac{1}{1 + e^{-a}}$.
        - Modelo: $p(y \mid \mathbf{x}) = \text{Bernoulli}(y \mid \hat{y})$.
        - Máxima Verossimilhança $\implies$ Entropia Cruzada Binária (BCE / Log-Loss):
          $$\mathcal{L}(\mathbf{w}) = -\sum_{n=1}^N \left[ y_n \ln \hat{y}_n + (1 - y_n) \ln(1 - \hat{y}_n) \right]$$
     3. **Classificação Multiclasse ($K \ge 3$):**
        - Ativação **Softmax**:
          $$\hat{y}_k = p(y = k \mid \mathbf{x}) = \frac{e^{a_k}}{\sum_{j=1}^K e^{a_j}}$$

        - Modelo: Distribuição Categórica / Multinomial com codificação *one-hot* $\mathbf{y} \in \{0, 1\}^K$.
        - Log-verossimilhança conjunta e Perda de Entropia Cruzada Categórica:
          $$\mathcal{L}(\mathbf{w}) = -\sum_{n=1}^N \sum_{k=1}^K y_{nk} \ln \hat{y}_{nk}$$

   - A Propriedade da Ligação Canônica:
     - Em todos os três casos fundamentais da família exponencial, a derivada da perda em relação à ativação pré-sináptica da saída reduz-se ao **resíduo linear puro**:
       $$\delta_k = \frac{\partial \mathcal{L}}{\partial a_k} = \hat{y}_k - y_k$$
       Essa elegância matemática evita saturações de gradiente quando o erro é grande!

   - *Pausa Ativa 3.*

5. **Bloco 3: O Algoritmo de Retropropagação (*Backpropagation*)** (~25 min)
   - Notação vetorial de camadas:
     - Entrada: $\mathbf{z}^{(0)} = \mathbf{x}$.
     - Camada oculta $l \in \{1, \dots, L-1\}$:
       $$\mathbf{a}^{(l)} = W^{(l)} \mathbf{z}^{(l-1)} + \mathbf{b}^{(l)}, \quad \mathbf{z}^{(l)} = h(\mathbf{a}^{(l)})$$

     - Camada de saída $L$:
       $$\mathbf{a}^{(L)} = W^{(L)} \mathbf{z}^{(L-1)} + \mathbf{b}^{(L)}, \quad \hat{\mathbf{y}} = g(\mathbf{a}^{(L)})$$

   - Definição formal das sensibilidades de erro (*error signals*):
     $$\delta_j^{(l)} = \frac{\partial \mathcal{L}}{\partial a_j^{(l)}}$$

   - Dedução da recorrência via Regra da Cadeia:
     $$\delta_j^{(l)} = \sum_{k=1}^{n_{l+1}} \frac{\partial \mathcal{L}}{\partial a_k^{(l+1)}} \frac{\partial a_k^{(l+1)}}{\partial z_j^{(l)}} \frac{\partial z_j^{(l)}}{\partial a_j^{(l)}} = \left(\sum_{k=1}^{n_{l+1}} \delta_k^{(l+1)} W_{kj}^{(l+1)}\right) h'(a_j^{(l)})$$
     Em notação matricial vetorizada:
     $$\boldsymbol{\delta}^{(l)} = \left( (W^{(l+1)})^T \boldsymbol{\delta}^{(l+1)} \right) \odot h'(\mathbf{a}^{(l)})$$

   - Gradientes das matrizes de parâmetros:
     $$\frac{\partial \mathcal{L}}{\partial W_{ji}^{(l)}} = \delta_j^{(l)} z_i^{(l-1)} \implies \nabla_{W^{(l)}} \mathcal{L} = \boldsymbol{\delta}^{(l)} (\mathbf{z}^{(l-1)})^T$$
     $$\frac{\partial \mathcal{L}}{\partial \mathbf{b}^{(l)}} = \boldsymbol{\delta}^{(l)}$$

   - Análise de Complexidade Computacional:
     - A passagem direta (*forward pass*) avalia a perda em $\mathcal{O}(|W|)$.
     - A passagem reversa (*backward pass*) propaga os gradientes em tempo linear $\mathcal{O}(|W|)$ (Teorema de Baur-Strassen).
   - *Pausa Ativa 4.*

6. **Bloco 4: Regularização Profunda: Weight Decay e Dropout** (~12 min)
   - Redes neurais modernas frequentemente operam no regime superparametrizado ($P \gg N$). Por que não colapsam em sobreajuste catastrófico?
   - **Weight Decay ($L_2$ Regularization):**
     - Penalidade $\frac{\lambda}{2}\sum_l \|W^{(l)}\|_F^2$.
     - Equivalência bayesiana: Máximo A Posteriori (MAP) sob priori Gaussiana independente com variância $\sigma_w^2 = 1/\lambda$ em cada peso.
     - Efeito no gradiente: $W^{(l)} \leftarrow (1 - \alpha \lambda) W^{(l)} - \alpha \nabla \mathcal{L}$.
   - **Dropout (Srivastava, Hinton, Krizhevsky, Sutskever & Salakhutdinov, 2014):**
     - Mecânica no treino: a cada iteração de mini-batch, cada neurônio oculto é zerado temporariamente com probabilidade $p_{\text{drop}}$ através de uma máscara de Bernoulli $\mathbf{m} \sim \text{Bernoulli}(1 - p_{\text{drop}})$:
       $$\tilde{\mathbf{z}}^{(l)} = \mathbf{z}^{(l)} \odot \mathbf{m}^{(l)}$$

     - Mecânica no teste: todos os neurônios são mantidos e as ativações são multiplicadas por $(1 - p_{\text{drop}})$ (ou *Inverted Dropout* durante o treino).
     - Interpretação como Ensemble Exponencial: em uma rede com $D$ neurônios ocultos, existem $2^D$ sub-redes possíveis. O Dropout treina um comitê massivo de $2^D$ arquiteturas ralas que compartilham todos os parâmetros, cancelando co-adaptações espúrias entre detectores de atributos.

7. **Fechamento e Grande Síntese do Curso de Aprendizado Supervisionado** (~8 min)
   - *Retomando as 4 Perguntas:* Síntese das respostas consolidadas na aula.
   - *O Mapa Completo do Aprendizado Supervisionado:*
     - Modelos Lineares e GLMs (Aulas 5–7): alta interpretabilidade, baixo custo computacional, viés estrutural rígido.
     - Árvores e Ensembles (Aulas 3, 9, 10): estado da arte incontestável para dados tabulares heterogêneos; Bagging reduz variância e Boosting reduz viés.
     - Máquinas de Vetores de Suporte (Aula 11): margem máxima robusta e formulação dual elegante para problemas de alta dimensão com poucos exemplos.
     - Redes Neurais e Deep Learning (Aula 12): supremacia em dados perceptuais não-estruturados (imagens, áudio, texto) graças à capacidade de aprender representações latentes hierárquicas diretamente dos dados brutos.
   - Encerramento do ciclo letivo da disciplina.

