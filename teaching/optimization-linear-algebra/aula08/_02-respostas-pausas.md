# Respostas das Pausas Ativas — Aula 08

## Pausa Ativa 1: Soluções Analíticas vs. Iterativas

### Pergunta Aberta
**Pergunta:** Se as equações normais da Aula 3 fornecem a fórmula exata $\hat{\boldsymbol\beta} = (X^T X)^{-1} X^T \mathbf{y}$ em um único cálculo analítico, por que o treinamento de modelos modernos de Machine Learning (como redes neurais ou regressões em terabytes de dados) depende quase exclusivamente de métodos iterativos de primeira ordem como a Descida do Gradiente?

**Discussão e Condução:**
Existem dois impedimentos fundamentais para o cálculo analítico:
1. **Custo Computacional e de Memória:** O cálculo da matriz $X^T X$ para uma matriz de dados com $N$ linhas e $d$ atributos custa $O(N d^2)$ operações, e a fatoração de Cholesky ou inversão de $(X^T X)$ custa $O(d^3)$. Se $d = 100.000$ (como em modelos de linguagem ou bioinformática), armazenar $X^T X$ exige $80\text{ GB}$ de RAM e inverter exigiria $10^{15}$ operações de ponto flutuante, tornando a solução direta impraticável. Em contraste, a Descida do Gradiente avalia apenas produtos matriz-vetor que custam $O(N d)$ e exigem $O(d)$ de memória.
2. **Funções de Perda sem Solução Fechada:** Em quase todos os modelos fora dos mínimos quadrados lineares (como regressão logística, SVM com hinge loss ou redes neurais profundas), a condição de ponto crítico $\nabla f(\mathbf{w}) = \mathbf{0}$ resulta em um sistema de equações transcendentais não lineares acopladas. Não existe fórmula matemática fechada para isolar $\mathbf{w}$. A única forma de encontrar o minimizador é através de aproximações iterativas contínuas.

### Bloco V/F
1. **Afirmação:** Resolver as equações normais via fatoração de Cholesky custa $O(d^3)$ operações aritméticas, onde $d$ é a quantidade de atributos do modelo.
   - **Gabarito: V**.
   - **Justificativa:** A fatoração de Cholesky de uma matriz simétrica positiva definida $d \times d$ exige $\frac{1}{3}d^3 + O(d^2)$ multiplicações/adições.
2. **Afirmação:** O algoritmo de Descida do Gradiente exige a computação e o armazenamento explícito da matriz Hessiana $\nabla^2 f(\mathbf{x})$ a cada passo da iteração.
   - **Gabarito: F**.
   - **Justificativa:** A Descida do Gradiente é um método de **primeira ordem**: ele utiliza exclusivamente o vetor gradiente $\nabla f(\mathbf{x}) \in \mathbb{R}^d$, sem calcular a Hessiana.
3. **Afirmação:** Em qualquer função de perda com minimizador único, dar um passo de qualquer tamanho finito na direção oposta ao gradiente ($-\nabla f$) garante a diminuição estrita do valor da perda.
   - **Gabarito: F**.
   - **Justificativa:** Se o tamanho de passo $\alpha$ for excessivamente grande, o algoritmo ultrapassa o fundo da tigela (*overshooting*), podendo oscilar com amplitude crescente e divergir para o infinito.
4. **Afirmação:** Na regressão logística com perda de entropia cruzada, a condição de gradiente nulo $\nabla \mathcal{L}(\mathbf{w}) = \mathbf{0}$ não possui solução algébrica fechada para isolar o vetor de pesos $\mathbf{w}$.
   - **Gabarito: V**.
   - **Justificativa:** A não linearidade da função sigmoide $\sigma(\mathbf{w}^T \mathbf{x}_n)$ impede isolar $\mathbf{w}$ através de álgebra linear pura.

---

## Pausa Ativa 2: Suavidade de Lipschitz e o Limite do Tamanho de Passo

### Pergunta Aberta
**Pergunta:** Considere a função quadrática simples $f(x) = \frac{1}{2} L x^2$ em $\mathbb{R}$ (onde $L > 0$). Se aplicarmos a iteração da Descida do Gradiente $x_{k+1} = x_k - \alpha f'(x_k)$ iniciando em $x_0 = 1$, deduza analiticamente a relação entre $x_k$ e $x_0$. O que acontece se escolhermos $\alpha = \frac{1}{L}$, $\alpha = \frac{2}{L}$ e $\alpha = \frac{2{,}1}{L}$?

**Discussão e Condução:**
Como $f'(x) = L x$, a iteração fica:
$$x_{k+1} = x_k - \alpha (L x_k) = (1 - \alpha L) x_k \implies x_k = (1 - \alpha L)^k x_0$$
A dinâmica é governada pela base de potência $(1 - \alpha L)$:
1. Se $\alpha = \frac{1}{L}$: $1 - \alpha L = 0$. Temos $x_1 = 0$ e o algoritmo atinge o mínimo global exato em **um único passo**!
2. Se $\alpha = \frac{2}{L}$: $1 - \alpha L = -1$. Temos $x_k = (-1)^k x_0$, oscilando indefinidamente entre $+1$ e $-1$ sem jamais convergir.
3. Se $\alpha = \frac{2{,}1}{L}$: $1 - \alpha L = -1{,}1$. Temos $|1 - \alpha L| = 1{,}1 > 1$, e $|x_k| = (1{,}1)^k \to \infty$. O algoritmo diverge exponencialmente!
Isso prova geometricamente por que a constante de Lipschitz do gradiente $L = \lambda_{\max}(\nabla^2 f)$ impõe o limite superior estrito e intransponível $\alpha < \frac{2}{L}$ para qualquer garantia de convergência.

### Bloco V/F
1. **Afirmação:** Uma função duas vezes diferenciável tem gradiente $L$-Lipschitziano se e somente se o maior autovalor de sua Hessiana é limitado superiormente por $L$ em todo o domínio ($\lambda_{\max}(\nabla^2 f(\mathbf{x})) \le L$).
   - **Gabarito: V**.
   - **Justificativa:** Pelo teorema do valor médio multivariado e pela desigualdade de Cauchy-Schwarz, a norma do operador da Hessiana limita a constante de Lipschitz do gradiente: $\|\nabla^2 f\|_2 = \lambda_{\max} \le L$.
2. **Afirmação:** Pelo Lema de Descida (*Descent Lemma*), fixar o tamanho de passo em $\alpha = \frac{1}{L}$ assegura que $f(\mathbf{x}_{k+1}) \le f(\mathbf{x}_k) - \frac{1}{2L} \|\nabla f(\mathbf{x}_k)\|^2$.
   - **Gabarito: V**.
   - **Justificativa:** Substituindo $\mathbf{y} = \mathbf{x} - \frac{1}{L}\nabla f(\mathbf{x})$ na cota quadrática superior $f(\mathbf{y}) \le f(\mathbf{x}) + \nabla f(\mathbf{x})^T(\mathbf{y}-\mathbf{x}) + \frac{L}{2}\|\mathbf{y}-\mathbf{x}\|^2$, obtemos exatamente esse decréscimo estrito.
3. **Afirmação:** Se escolhermos $\alpha = \frac{1{,}99}{L}$ em uma função convexa com gradiente $L$-Lipschitziano, o algoritmo de Descida do Gradiente divergirá para o infinito.
   - **Gabarito: F**.
   - **Justificativa:** Como $\alpha = 1{,}99/L < 2/L$, o passo permanece dentro da região de estabilidade assintótica, garantindo convergência (embora com oscilações).
4. **Afirmação:** O valor da constante de Lipschitz $L$ para a função de perda dos mínimos quadrados $f(\boldsymbol\beta) = \|X\boldsymbol\beta - \mathbf{y}\|^2$ é igual a $2 \lambda_{\max}(X^T X)$.
   - **Gabarito: V**.
   - **Justificativa:** Como $\nabla^2 f(\boldsymbol\beta) = 2 X^T X$ é constante, $L = \|\nabla^2 f\|_2 = 2 \lambda_{\max}(X^T X)$.

---

## Pausa Ativa 3: Análise Espectral de Erro e o Número de Condição

### Pergunta Aberta
**Pergunta:** Considere a minimização de uma função quadrática $f(\mathbf{x}) = \frac{1}{2}\mathbf{x}^T A \mathbf{x}$ em $\mathbb{R}^2$, onde a matriz Hessiana $A = \text{diag}(\lambda_1, \lambda_2)$ possui autovalores $\lambda_1 = 100$ e $\lambda_2 = 1$. Se usarmos o passo ótimo $\alpha^\star = \frac{2}{\lambda_1 + \lambda_2} \approx 0{,}0198$, qual é o fator de redução do erro na coordenada $x_1$ e na coordenada $x_2$ a cada iteração? Por que a coordenada mais lenta dita o ritmo de convergência de todo o algoritmo?

**Discussão e Condução:**
Como a matriz é diagonal, as coordenadas desacoplam-se:
$$e_{k+1, i} = (1 - \alpha \lambda_i) e_{k, i}$$
Substituindo $\alpha^\star = \frac{2}{100 + 1} = \frac{2}{101} \approx 0{,}0198$:
1. Na coordenada 1 (eixo de alta curvatura):
   $$1 - \alpha^\star \lambda_1 = 1 - \frac{2 \times 100}{101} = 1 - \frac{200}{101} = -\frac{99}{101} \approx -0{,}9802$$
   O erro inverte de sinal a cada passo (ziguezague) e é multiplicado em magnitude por $0{,}9802$.
2. Na coordenada 2 (eixo de baixa curvatura, vale quase plano):
   $$1 - \alpha^\star \lambda_2 = 1 - \frac{2 \times 1}{101} = 1 - \frac{2}{101} = +\frac{99}{101} \approx +0{,}9802$$
   O erro decai monotonamente, sendo multiplicado exatamente pelo mesmo fator $0{,}9802$.
O fator de contração máximo é:
$$\rho^\star = \frac{\lambda_{\max} - \lambda_{\min}}{\lambda_{\max} + \lambda_{\min}} = \frac{100 - 1}{100 + 1} = \frac{99}{101} \approx 0{,}9802$$
Mesmo no passo matematicamente ótimo, a cada iteração o erro total diminui apenas cerca de $2\%$. Para reduzir o erro em $10^4$ vezes, precisamos de centenas de passos.
Se tentarmos aumentar o passo para acelerar a coordenada 2, desestabilizamos a coordenada 1 ($|1 - \alpha \lambda_1| > 1$), causando explosão numérica. O eixo de menor curvatura impede o progresso rápido, enquanto o eixo de maior curvatura limita o tamanho do passo. Esse impasse é a essência do mau condicionamento.

### Bloco V/F
1. **Afirmação:** Em uma forma quadrática com $A \succ 0$, o fator de contração ótimo do erro no Gradient Descent é dado rigorosamente por $\frac{\kappa - 1}{\kappa + 1}$, onde $\kappa = \text{cond}(A) = \frac{\lambda_{\max}}{\lambda_{\min}}$.
   - **Gabarito: V**.
   - **Justificativa:** É a taxa de convergência exata de Chebyshev deduzida por Boyd & Vandenberghe (§9.3.2).
2. **Afirmação:** Se a matriz Hessiana for um múltiplo da identidade ($\nabla^2 f = c I$, logo $\kappa = 1$), a Descida do Gradiente com passo $\alpha = 1/c$ atinge o mínimo global exato em uma única iteração.
   - **Gabarito: V**.
   - **Justificativa:** Com $\kappa = 1$, $\rho^\star = \frac{1-1}{1+1} = 0$, e a contração é total em um único passo.
3. **Afirmação:** O número de condição de uma matriz simétrica definida positiva pode assumir valores estritamente menores do que 1.
   - **Gabarito: F**.
   - **Justificativa:** Por definição, $\kappa = \lambda_{\max}/\lambda_{\min}$; como $\lambda_{\max} \ge \lambda_{\min} > 0$, temos sempre $\kappa \ge 1$.
4. **Afirmação:** O fenômeno de ziguezague na Descida do Gradiente ocorre preferencialmente ao longo do autovetor associado ao menor autovalor da Hessiana.
   - **Gabarito: F**.
   - **Justificativa:** O ziguezague (oscilação com inversão de sinal $(1 - \alpha \lambda_i) < 0$) ocorre no autovetor de **maior autovalor** ($\lambda_{\max}$), onde a curvatura é excessivamente íngreme.

---

## Pausa Ativa 4: Padronização e a Homogeneização da Hessiana

### Pergunta Aberta
**Pergunta:** No conjunto de dados California Housing, a renda média (`MedInc`) varia na escala de $0{,}5$ a $15$, enquanto a população do distrito (`Population`) varia de $3$ a $35.000$. O que acontece geometricamente com as curvas de nível da função de perda quadrática quando combinamos variáveis com escalas tão discrepantes? De que maneira a transformação linear de padronização ($Z$-score) altera a matriz Hessiana $X^T X$?

**Discussão e Condução:**
Como a perda é $L(\boldsymbol\beta) = \|X\boldsymbol\beta - \mathbf{y}\|^2$, a derivada parcial em relação ao coeficiente de uma variável de grande magnitude (como `Population`) é multiplicada por valores da ordem de $10^3$ a $10^4$, enquanto a derivada em relação a `MedInc` envolve valores da ordem de $10^0$.
A Hessiana $2 X^T X$ tem elementos diagonais proporcionais a $\sum_n x_{nj}^2$. Uma variável com escala $1000$ vezes maior gera um elemento diagonal $10^6$ vezes maior na matriz de Gram.
Isso estica brutalmente a tigela quadrática, transformando-a em uma fenda hiperalongada com $\text{cond}(X^T X) \approx 23.460$.
A padronização $Z$-score transforma cada coluna para ter média zero e variância amostral unitária: $\tilde{x}_{nj} = \frac{x_{nj} - \mu_j}{\sigma_j}$.
Algebricamente, isso equivale a multiplicar $X$ por uma matriz diagonal de escalonamento $D^{-1}$: $\tilde{X} = X D^{-1}$.
Na matriz transformada $\tilde{X}^T \tilde{X}$, todos os elementos diagonais tornam-se rigorosamente iguais a $N$. Os autovalores tornam-se muito mais homogêneos (governados apenas pelas correlações lineares entre atributos, e não pela unidade física de medida), derrubando o número de condição de dezenas de milhares para dezenas e eliminando o ziguezague patológico do otimizador.

### Bloco V/F
1. **Afirmação:** A padronização de atributos via $Z$-score altera o valor preditivo final ótimo de um modelo de regressão linear regularizado via mínimos quadrados comuns (OLS sem penalização).
   - **Gabarito: F**.
   - **Justificativa:** A transformação é invertível; no OLS clássico, os coeficientes padronizados podem ser mapeados de volta exatamente aos coeficientes originais, produzindo predições $\hat{\mathbf{y}}$ matematicamente idênticas.
2. **Afirmação:** Aplicar padronização às colunas da matriz de dados $X$ garante que todos os elementos da diagonal principal da matriz de covariância amostral sejam iguais a 1.
   - **Gabarito: V**.
   - **Justificativa:** Por definição, a variância de cada coluna padronizada é $\frac{1}{N}\sum_n \tilde{x}_{nj}^2 = 1$.
3. **Afirmação:** A Descida do Gradiente é um algoritmo invariante a transformações afins de escala nos atributos de entrada.
   - **Gabarito: F**.
   - **Justificativa:** A Descida do Gradiente é altamente sensível à escala dos atributos; a direção $-\nabla f$ muda dependendo do sistema de coordenadas métrico utilizado (o método de Newton é invariante afim, mas o gradiente não é).
4. **Afirmação:** Reduzir o número de condição de $X^T X$ de $20.000$ para $50$ diminui o número de iterações necessárias para atingir uma tolerância fixa de erro em ordens de magnitude.
   - **Gabarito: V**.
   - **Justificativa:** A taxa de contração $\frac{\kappa - 1}{\kappa + 1}$ cai de $\approx 0{,}9999$ para $\approx 0{,}96$, acelerando drasticamente o decaimento exponencial do erro.

---

## Pausa Ativa 5: Regressão Logística e a Ausência de Solução Fechada

### Pergunta Aberta
**Pergunta:** Na regressão linear, igualamos o gradiente a zero ($\nabla L = 2X^T(X\boldsymbol\beta - \mathbf{y}) = \mathbf{0}$) e isolamos $\boldsymbol\beta = (X^TX)^{-1}X^T\mathbf{y}$ usando apenas álgebra linear elementar. Na regressão logística, o gradiente tem a forma quase idêntica $\nabla \mathcal{L}(\mathbf{w}) = \frac{1}{N}X^T(\boldsymbol\sigma(X\mathbf{w}) - \mathbf{y}) = \mathbf{0}$. Por que não é possível usar álgebra de matrizes para isolar $\mathbf{w}$ nessa segunda equação?

**Discussão e Condução:**
Na regressão linear, a predição é linear nos parâmetros: $\hat{\mathbf{y}} = X\boldsymbol\beta$. A equação $X^TX\boldsymbol\beta = X^T\mathbf{y}$ é um sistema linear de equações algébricas, que admite inversão via matrizes.
Na regressão logística, a predição é não linear: $\hat{y}_n = \sigma(\mathbf{w}^T \mathbf{x}_n) = \frac{1}{1 + \exp(-\mathbf{w}^T \mathbf{x}_n)}$.
A equação de ponto crítico é:
$$\sum_{n=1}^N \left( \frac{1}{1 + \exp(-\mathbf{w}^T \mathbf{x}_n)} - y_n \right) \mathbf{x}_n = \mathbf{0}$$
O vetor de incógnitas $\mathbf{w}$ encontra-se "preso" dentro do expoente de funções sigmoides somadas sobre todas as $N$ observações. Não existe operação de álgebra linear (nem matriz inversa) capaz de desmembrar essa soma transcendental e isolar $\mathbf{w}$.
Por outro lado, provamos na aula que a Hessiana $\nabla^2 \mathcal{L} = \frac{1}{N}X^T S X$ é estritamente positiva definida se $X$ tem posto completo, o que garante que a função é estritamente convexa e possui um único mínimo global. Como não temos fórmula analítica para a raiz, a **Descida do Gradiente** torna-se o veículo matemático perfeito para navegar a superfície e convergir assintoticamente ao valor ótimo $\mathbf{w}^\star$.

### Bloco V/F
1. **Afirmação:** A função sigmoide $\sigma(a) = \frac{1}{1 + \exp(-a)}$ tem derivada dada elegantemente por $\sigma'(a) = \sigma(a)(1 - \sigma(a))$.
   - **Gabarito: V**.
   - **Justificativa:** Pela regra do quociente/cadeia: $\frac{d}{da}(1 + e^{-a})^{-1} = -(1+e^{-a})^{-2}(-e^{-a}) = \frac{1}{1+e^{-a}}\frac{e^{-a}}{1+e^{-a}} = \sigma(a)(1 - \sigma(a))$.
2. **Afirmação:** A matriz Hessiana da regressão logística $\nabla^2 \mathcal{L}(\mathbf{w}) = \frac{1}{N}X^T S X$ é constante e independe do vetor de parâmetros $\mathbf{w}$.
   - **Gabarito: F**.
   - **Justificativa:** Os elementos da matriz diagonal $S$ são $s_{nn} = \hat{y}_n(1 - \hat{y}_n)$, que dependem explicitamente de $\mathbf{w}$ através de $\hat{y}_n = \sigma(\mathbf{w}^T \mathbf{x}_n)$. A curvatura muda a cada ponto do espaço!
3. **Afirmação:** Como $0 < \sigma(a) < 1$ para todo $a \in \mathbb{R}$, todos os elementos diagonais da matriz de ponderação $S$ na regressão logística são estritamente positivos.
   - **Gabarito: V**.
   - **Justificativa:** Como $\hat{y}_n \in (0, 1)$, o produto $\hat{y}_n(1 - \hat{y}_n)$ é estritamente positivo (atingindo o máximo de $0{,}25$ quando $\mathbf{w}^T\mathbf{x}_n = 0$).
4. **Afirmação:** A ausência de solução analítica fechada na regressão logística implica que o problema de otimização pode ter múltiplos mínimos locais indesejados.
   - **Gabarito: F**.
   - **Justificativa:** Ausência de solução fechada não tem relação com não convexidade. A perda de entropia cruzada é estritamente convexa ($X^T S X \succ 0$), garantindo um único mínimo global; ela apenas não pode ser calculada por uma fórmula direta.

