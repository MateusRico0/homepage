# Respostas e Guia Docente — Pausas da Aula 12

Este documento reúne as resoluções detalhadas, as deduções analíticas completas e o gabarito comentado dos testes conceituais (Verdadeiro ou Falso) das quatro Pausas da **Aula 12: Momento, Curvatura e Métodos Acelerados**.

---

## Pausa 1: O Dilema das Oscilações Transversais e a Inércia

### 1. Resolução da Pergunta Aberta
*Cenário:* Uma partícula otimizadora está em uma ravina elíptica $f(w_1, w_2) = \frac{1}{2}(100 w_1^2 + w_2^2)$. O gradiente instantâneo no ponto inicial é $\mathbf{g}_0 = (100 w_1, w_2)^T$. Suponha que ao longo das iterações $k$, as derivadas parciais na direção transversal alternem de sinal: $g_{k, 1} \in \{+10, -10, +10, -10, \dots\}$, enquanto na calha longitudinal avancem com sinal constante: $g_{k, 2} \approx 1$.

- **Comportamento do Gradiente Descendente sem Momento:**
  Para cada passo, o GD atualiza:
  $$w_{k+1, 1} = w_{k, 1} - \alpha g_{k, 1}$$
  $$w_{k+1, 2} = w_{k, 2} - \alpha g_{k, 2}$$
  Na direção transversal ($w_1$), o ponto é arremessado alternadamente de uma borda à outra da ravina. Para evitar explosão nessa coordenada íngreme, somos forçados a fixar $\alpha < 2/100 = 0{,}02$. Com esse $\alpha$ minúsculo, o avanço longitudinal por passo é de míseros $\Delta w_2 = -0{,}02 \times 1 = -0{,}02$. O deslocamento total na coordenada útil após $K$ passos é de apenas $0{,}02 K$.

- **Ação Filtradora da Média de Inércia:**
  Com o momento $\mathbf{v}_{k+1} = \beta \mathbf{v}_k - \alpha \mathbf{g}_k$, o vetor velocidade acumula a soma exponencial ponderada dos gradientes passados:
  $$\mathbf{v}_k = -\alpha \sum_{j=0}^{k-1} \beta^{k-1-j} \mathbf{g}_j$$

  - Na coordenada transversal oscilante ($w_1$): gradientes de sinais alternados cancelam-se mutuamente:
    $$\sum_{j=0}^{k-1} \beta^{k-1-j} (\pm 10) \approx 0$$
    A velocidade transversal terminal é drasticamente amortecida, extinguindo os ziguezagues.

  - Na coordenada longitudinal constante ($w_2$): gradientes com mesmo sinal somam-se construtivamente em série geométrica:
    $$v_{k, 2} \approx -\alpha \cdot 1 \cdot \sum_{j=0}^\infty \beta^j = -\frac{\alpha}{1 - \beta} \cdot 1$$
    Para $\beta = 0{,}9$, a velocidade efetiva é amplificada por um fator de $\frac{1}{1 - 0{,}9} = 10\times$!

- **Conclusão Pedagógica:**
  A inércia mecânica atua como um **filtro passa-baixas direcional**: ela cancela ruídos de alta frequência espacial (oscilações transversais opostas) e constrói velocidade terminal de cruzeiro na direção de sinal consistente.

### 2. Gabarito Comentado dos Testes Conceituais (V/F)

*   **(A) Verdadeiro.** Na presença de gradientes oscilatórios transversais, a soma ponderada por $\beta$ cancela as amplitudes de sinais opostos, enquanto componentes consistentes somam-se até o fator $\frac{1}{1-\beta}$.
*   **(B) Falso.** O momento não altera a matriz Hessiana nem a curvatura da função; ele altera a equação diferencial do sistema dinâmico de 1ª para 2ª ordem, modificando o raio espectral do operador de iteração.
*   **(C) Falso.** Aumentar o coeficiente de momento $\beta$ sem reduzir a taxa de aprendizado $\alpha$ pode desestabilizar o sistema dinâmico e induzir oscilações caóticas ou divergência se o raio espectral da matriz de transição ultrapassar 1.
*   **(D) Verdadeiro.** Em superfícies de custo estocásticas (SGD com mini-batches), o gradiente instantâneo possui alta variância aleatória; o vetor momento atua como uma média móvel suave que atenua as flutuações amostrais.

---

## Pausa 2: Aceleração Espectral de Polyak (*Heavy-Ball*)

### 1. Resolução da Pergunta Aberta
*Cenário:* Uma forma quadrática $f(\mathbf{w}) = \frac{1}{2}\mathbf{w}^T H \mathbf{w}$ com autovalores $\lambda_{\min} \le \lambda_i \le \lambda_{\max}$ e $H \succ 0$.
Relembrando a **Aula 8**, o Gradiente Descendente clássico gerava um sistema dinâmico linear de 1ª ordem nos autovetores de $H$, desacoplado em dinâmicas escalares $e_{k+1, i} = (1 - \alpha \lambda_i) e_{k, i}$ (matriz de transição $1 \times 1$).
Com o momento de Polyak, a inércia cria dependência temporal de dois passos ($\mathbf{e}_k$ e $\mathbf{e}_{k-1}$). Aumentando o vetor de estado para $\begin{bmatrix} e_{k, i} \\ e_{k-1, i} \end{bmatrix}$, a dinâmica expressa-se através da matriz de transição $T_i \in \mathbb{R}^{2 \times 2}$ para o erro espectral na $i$-ésima direção:
$$\begin{bmatrix} e_{k+1, i} \\ e_{k, i} \end{bmatrix} = \begin{bmatrix} 1 + \beta - \alpha \lambda_i & -\beta \\ 1 & 0 \end{bmatrix} \begin{bmatrix} e_{k, i} \\ e_{k-1, i} \end{bmatrix}$$

- **Polinômio Característico:**
  $$\det(\mu I - T_i) = \det \begin{bmatrix} \mu - (1 + \beta - \alpha \lambda_i) & \beta \\ -1 & \mu \end{bmatrix} = \mu^2 - (1 + \beta - \alpha \lambda_i)\mu + \beta = 0$$

- **Condição para Raízes Complexas Conjugadas:**
  O discriminante quadrático é:
  $$\Delta(\lambda_i) = (1 + \beta - \alpha \lambda_i)^2 - 4\beta$$
  Quando $\Delta(\lambda_i) \le 0$, as duas raízes $\mu_1, \mu_2$ são complexas conjugadas da forma $a \pm ib$.
  Pelas relações de Girard, o produto das raízes de uma equação quadrática mônica com termo constante $\beta$ é:
  $$\mu_1 \mu_2 = |\mu|^2 = \beta \implies |\mu| = \sqrt{\beta}$$
  **Fato Notável:** O módulo do raio espectral é exatamente $\sqrt{\beta}$, independentemente do valor exato de $\lambda_i$, desde que o discriminante seja não-positivo!

- **A Escolha Ótima dos Hiperparâmetros de Polyak:**
  Para garantir que $\Delta(\lambda_i) \le 0$ para todos os autovalores no espectro $[\lambda_{\min}, \lambda_{\max}]$ e minimizar o raio espectral, ajustamos os extremos para que $\Delta(\lambda_{\min}) = \Delta(\lambda_{\max}) = 0$:
  $$1 + \beta - \alpha \lambda_{\min} = 2\sqrt{\beta}, \quad 1 + \beta - \alpha \lambda_{\max} = -2\sqrt{\beta}$$
  Subtraindo as equações:
  $$\alpha (\lambda_{\max} - \lambda_{\min}) = 4\sqrt{\beta}$$
  Somando as equações:
  $$2(1 + \beta) - \alpha(\lambda_{\max} + \lambda_{\min}) = 0$$
  Resolvendo o sistema algébrico obtém-se as fórmulas canônicas de Polyak (1964):
  $$\alpha^\star = \frac{4}{(\sqrt{\lambda_{\max}} + \sqrt{\lambda_{\min}})^2}, \quad \beta^\star = \left(\frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1}\right)^2$$
  onde $\kappa = \lambda_{\max}/\lambda_{\min}$.

- **A Taxa de Convergência Acelerada:**
  O raio espectral do operador de Polyak sob esses hiperparâmetros é:
  $$\rho^\star = \sqrt{\beta^\star} = \frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1} \approx 1 - \frac{2}{\sqrt{\kappa}}$$
  Comparado com o Gradiente Descendente clássico ótimo ($\rho_{\text{GD}} = \frac{\kappa - 1}{\kappa + 1} \approx 1 - \frac{2}{\kappa}$):
  Se $\kappa = 10.000$, temos:

  - $\rho_{\text{GD}} \approx 1 - \frac{2}{10.000} = 0{,}9998 \implies \approx 11.500$ iterações para reduzir o erro em $10\times$.
  - $\rho_{\text{Polyak}} \approx 1 - \frac{2}{100} = 0{,}98 \implies \approx 114$ iterações para reduzir o erro em $10\times$.
  **O ganho de aceleração é de exatamente $100\times$ ($\sqrt{\kappa}$)!**

### 2. Gabarito Comentado dos Testes Conceituais (V/F)

*   **(A) Verdadeiro.** A matriz de transição $2 \times 2$ possui determinante igual a $\beta$. Quando as raízes do polinômio característico são complexas conjugadas, o produto dos autovalores é $|\mu|^2 = \det(T) = \beta$, garantindo que todas as direções espectrais dentro do intervalo amortecido decaiam com taxa $\sqrt{\beta}$.
*   **(B) Falso.** Em problemas mal-condicionados ($\kappa \gg 1$), a taxa de contração de Polyak escala com $1 - \frac{2}{\sqrt{\kappa}}$, e não $1 - \frac{2}{\kappa}$. A dependência da raiz quadrada de $\kappa$ representa uma aceleração quadrática de velocidade assintótica.
*   **(C) Verdadeiro.** A taxa assintótica $\frac{\sqrt{\kappa}-1}{\sqrt{\kappa}+1}$ deduzida por Polyak para funções quadráticas atinge o limite inferior teórico derivado por Chebyshev para polinômios ótimos de iteração de 1ª ordem.
*   **(D) Falso.** O método Heavy-Ball de Polyak com parâmetros fixos não possui garantia global de convergência para funções convexas gerais não-quadráticas, podendo oscilar ou divergir em funções estritamente convexas com curvaturas variantes se o amortecimento não for calibrado dinamicamente (daí a necessidade do método de Nesterov).

---

## Pausa 3: Gradiente Acelerado de Nesterov (NAG) vs. Momento Clássico

### 1. Resolução da Pergunta Aberta
*Cenário:* Uma partícula está em $\mathbf{w}_k = 2$ em uma bacia parabólica 1D $f(w) = \frac{1}{2}w^2$, com velocidade herdada $v_k = -3$ (apontando fortemente em direção à origem). Seja $\alpha = 0{,}5$ e $\beta = 0{,}9$.

- **Atualização do Momento Clássico (Polyak):**
  1. Gradiente avaliado no ponto presente: $g_k = f'(w_k) = f'(2) = 2$.
  2. Nova velocidade:
     $$v_{k+1} = \beta v_k - \alpha g_k = 0{,}9 \times (-3) - 0{,}5 \times 2 = -2{,}7 - 1{,}0 = -3{,}7$$
  3. Nova posição:
     $$w_{k+1} = w_k + v_{k+1} = 2 - 3{,}7 = -1{,}7$$
  A partícula foi arremessada para o outro lado do vale ($w = -1{,}7$) com velocidade ainda maior no sentido negativo ($v = -3{,}7$), gerando um violento *overshoot*!

- **Atualização do Momento de Nesterov (NAG):**
  1. Ponto antecipado (*look-ahead*):
     $$w_{\text{ahead}} = w_k + \beta v_k = 2 + 0{,}9 \times (-3) = 2 - 2{,}7 = -0{,}7$$
     Observe que o salto antecipado pela inércia já levou a partícula para o outro lado do vale ($w_{\text{ahead}} = -0{,}7 < 0$)!
  2. Gradiente avaliado no ponto antecipado:
     $$g_{\text{ahead}} = f'(w_{\text{ahead}}) = -0{,}7$$
     Como a encosta oposta sobe para valores menores, a derivada lá é negativa!
  3. Nova velocidade:
     $$v_{k+1} = \beta v_k - \alpha g_{\text{ahead}} = -2{,}7 - 0{,}5 \times (-0{,}7) = -2{,}7 + 0{,}35 = -2{,}35$$
  4. Nova posição:
     $$w_{k+1} = w_k + v_{k+1} = 2 - 2{,}35 = -0{,}35$$

- **Conclusão Pedagógica:**
  O gradiente de Nesterov percebeu preventivamente que a inércia estava subindo a encosta oposta e aplicou uma força corretiva contrária ($+0{,}35$), freando a partícula. O ponto resultante $w_{k+1} = -0{,}35$ está muito mais próximo da origem ($w^\star = 0$) do que o ponto gerado por Polyak ($w_{k+1} = -1{,}7$). Nesterov atua como um sistema de freios inteligente antes da curva.

### 2. Gabarito Comentado dos Testes Conceituais (V/F)

*   **(A) Verdadeiro.** A avaliação do gradiente no ponto adiantado pela inércia $\mathbf{w}_k + \beta \mathbf{v}_k$ detecta a subida de potenciais antes que ela ocorra fisicamente, adicionando uma força contrária que atua como amortecedor ativo de oscilações.
*   **(B) Verdadeiro.** Para funções convexas $L$-suaves gerais, Nesterov provou que a taxa teórica ótima inultrapassável para qualquer método de primeira ordem é $\mathcal{O}(1/k^2)$. Enquanto o GD clássico atinge apenas $\mathcal{O}(1/k)$, o NAG atinge essa cota ótima teórica.
*   **(C) Falso.** O cálculo do gradiente em $\mathbf{w}_k + \beta \mathbf{v}_k$ exige exatamente uma única avaliação de gradiente por iteração, possuindo exatamente o mesmo custo assintótico $\mathcal{O}(d)$ por passo que o Gradiente Descendente e o Momento de Polyak.
*   **(D) Falso.** Em funções não-convexas e com ruído estocástico acentuado (SGD), estimar o gradiente no ponto antecipado em mini-batches pequenos pode adicionar ruído e instabilidade adicional, razão pela qual o Momento de Polyak padrão é mais frequentemente adotado como base para o Adam em redes profundas.

---

## Pausa 4: A Síntese do Adam e a Cirurgia do AdamW

### 1. Resolução da Pergunta Aberta
*Cenário:* Inicializamos o otimizador Adam com hiperparâmetros padrão $\beta_1 = 0{,}9$, $\beta_2 = 0{,}999$, $\epsilon = 10^{-8}$ e inicializadores zerados $m_0 = 0$ e $v_0 = 0$. Suponha que no passo $t=1$ o gradiente seja constante $g_1 = 5{,}0$.

- **Cálculo sem Correção de Viés:**
  $$m_1 = (1 - 0{,}9) g_1 = 0{,}1 \times 5{,}0 = 0{,}5$$
  $$v_1 = (1 - 0{,}999) g_1^2 = 0{,}001 \times 25{,}0 = 0{,}025$$
  O passo de atualização sem correção seria:
  $$\Delta w_1 = -\alpha \frac{m_1}{\sqrt{v_1} + \epsilon} = -\alpha \frac{0{,}5}{\sqrt{0{,}025}} = -\alpha \frac{0{,}5}{0{,}1581} \approx -3{,}16 \alpha$$

- **Cálculo com a Correção de Viés Teórica:**
  Fatores de correção para $t=1$:
  $$1 - \beta_1^1 = 1 - 0{,}9 = 0{,}1 \implies \hat{m}_1 = \frac{m_1}{0{,}1} = \frac{0{,}5}{0{,}1} = 5{,}0$$
  $$1 - \beta_2^1 = 1 - 0{,}999 = 0{,}001 \implies \hat{v}_1 = \frac{v_1}{0{,}001} = \frac{0{,}025}{0{,}001} = 25{,}0$$
  O passo de atualização rigorosamente corrigido é:
  $$\Delta w_1^{\text{corrigido}} = -\alpha \frac{\hat{m}_1}{\sqrt{\hat{v}_1} + \epsilon} = -\alpha \frac{5{,}0}{\sqrt{25{,}0}} = -\alpha \frac{5{,}0}{5{,}0} = -\alpha \cdot 1{,}0$$

- **O Que Teria Acontecido se o Gradiente Fosse Menor ($g_1 = 0{,}1$)?**
  Sem correção de viés:
  $$v_1 = 0{,}001 \times (0{,}1)^2 = 10^{-5} \implies \sqrt{v_1} = 0{,}00316$$
  $$m_1 = 0{,}1 \times 0{,}1 = 0{,}01$$
  $$\frac{m_1}{\sqrt{v_1}} = \frac{0{,}01}{0{,}00316} \approx 3{,}16$$
  Novamente, o passo é distorcido. Pior: se $t$ avança lentamente para valores pequenos, a ausência de correção de viés faz com que $\sqrt{v_t}$ permaneça minúsculo por centenas de iterações (já que $1 - \beta_2 \approx 10^{-3}$), provocando passos gigantestos e instabilidade severa durante a fase de partida do modelo!

### 2. Gabarito Comentado dos Testes Conceituais (V/F)

*   **(A) Verdadeiro.** A expansão geométrica da média exponencial inicializada em zero gera $\mathbb{E}[m_t] = \mathbb{E}[g_t](1 - \beta_1^t)$ e $\mathbb{E}[v_t] = \mathbb{E}[g_t^2](1 - \beta_2^t)$. Dividir por $1 - \beta^t$ anula esse viés estocástico exatamente para qualquer $t \ge 1$.
*   **(B) Falso.** Quando $t \to \infty$, como $\beta_1, \beta_2 \in (0, 1)$, temos $\beta_1^t \to 0$ e $\beta_2^t \to 0$. Os denominadores $1 - \beta^t$ convergem rapidamente para 1, tornando a correção irrelevante em iterações avançadas e crucial apenas no período transitório inicial.
*   **(C) Verdadeiro.** No Adam com regularização $L_2$ adicionada à perda, o termo regularizador $\lambda w$ é dividido por $\sqrt{\hat{v}_t} + \epsilon$. Parâmetros com gradientes volumosos ($\hat{v}_t$ grande) sofrem regularização suprimida, enquanto pesos esparsos com $\hat{v}_t$ minúsculo sofrem penalidade inflacionada.
*   **(D) Verdadeiro.** O algoritmo AdamW (Loshchilov & Hutter, 2019) restaura a integridade da penalidade Euclidiana ao subtrair diretamente $\alpha \lambda \mathbf{w}_t$ fora da fração adaptativa, garantindo que o decaimento de pesos ocorra a uma taxa constante por época independente da escala do gradiente.

