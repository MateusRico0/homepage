## Resumo — Aula 11: Máquinas de Vetores de Suporte (SVM)

Ao longo das Aulas 1 a 10, toda a formulação supervisionada foi alicerçada na **tese probabilística do curso**: assumir uma distribuição condicional de probabilidade $p(y \mid \mathbf{x})$, formular a log-verossimilhança e aplicar teoria da decisão bayesiana (minimizando o risco esperado sob uma perda $L$). Mesmo no Gradient Tree Boosting da Aula 10, a expansão aditiva de árvores foi guiada pela minimização da deviance de Bernoulli ou perdas paramétricas suaves.

Esta aula apresenta uma **ruptura deliberada e fascinante com o paradigma da máxima verossimilhança**: as **Máquinas de Vetores de Suporte (*Support Vector Machines* - SVM)**, introduzidas por Vladimir Vapnik e Corinna Cortes (1995). Em vez de tentar estimar a densidade de probabilidade $p(y \mid \mathbf{x})$ em todo o espaço de entrada — tarefa desnecessariamente complexa e vulnerável à maldição da dimensionalidade —, a SVM foca exclusivamente na busca pelo **hiperplano separador de margem máxima**.

Iniciamos formalizando a geometria do hiperplano canônico no caso linearmente separável (*Hard Margin*), provando por que maximizar a margem geométrica $2/\|\mathbf{w}\|$ equivale a minimizar a energia quadrática $\|\mathbf{w}\|^2/2$. Aplicamos o formalismo dos multiplicadores de Lagrange e deduzimos as condições KKT (*Karush-Kuhn-Tucker*), revelando a propriedade mais elegante do modelo: a **esparsidade dos vetores de suporte**, onde apenas as instâncias que repousam exatamente sobre as margens ($\alpha_i > 0$) determinam a fronteira de decisão, tornando o classificador imune a todos os outros pontos do dataset.

Em seguida, generalizamos o modelo para distribuições reais com sobreposição de classes através da introdução de variáveis de folga $\xi_i \ge 0$ (*Soft Margin*), estabelecendo a correspondência analítica exata entre o parâmetro de regularização $C$ e a **função de perda Hinge (*Hinge Loss*)** $\max(0, 1 - y f(\mathbf{x}))$. Demonstramos geometricamente por que a perda Hinge gera esparsidade exata em $\boldsymbol{\alpha}$, enquanto a perda logística da Aula 6 obriga todos os pontos a influenciarem a fronteira.

Na segunda metade da aula, transcendemos a linearidade através do célebre **Truque do Kernel (*Kernel Trick*)** fundamentado no Teorema de Mercer, demonstrando como produtos internos em espaços de Hilbert de dimensão infinita (Kernel RBF Gaussiano) são avaliados com custo computacional baixo no espaço original. Por fim, resolvemos o dilema estatístico da SVM: como ela gera apenas escores de margem não calibrados $f(\mathbf{x}) \in \mathbb{R}$, deduzimos o método de **Platt Scaling (1999)** para recuperar probabilidades a posteriori bem calibradas via regressão logística out-of-fold, e estendemos o arcabouço para regressão através da perda $\varepsilon$-insensível (SVR). O dataset-fio é o clássico Breast Cancer Wisconsin (`load_breast_cancer`), combinando projeções 2D didáticas e avaliação nos 30 atributos diagnósticos.

**Objetivos:**
1. Formular algebricamente o hiperplano de separação, deduzir a distância ortogonal euclidiana de um ponto e provar a equivalência entre maximização de margem e minimização de $\|\mathbf{w}\|^2/2$.
2. Aplicar a teoria da dualidade de Lagrange e as condições KKT para deduzir a forma dual de Wolfe e provar a esparsidade dos vetores de suporte.
3. Formular o classificador de margem suave (*Soft Margin*), analisar o papel do hiperparâmetro $C$ no tradeoff viés-variância e deduzir a equivalência com a perda Hinge regularizada.
4. Compreender o Truque do Kernel via Teorema de Mercer e comparar a geometria de kernels lineares, polinomiais e RBF gaussianos.
5. Implementar e calibrar probabilisticamente os escores de margem da SVM via Platt Scaling, evitando vazamento de dados (*data leakage*).

**Pré-requisitos:** Projeção ortogonal e hiperplanos (Aula 3 de Álgebra Linear); Otimização convexa, gradientes e Hessiana (Aulas 6 e 7 de Otimização); Regressão logística e perda de entropia cruzada (Aula 6 de Aprendizado Supervisionado).
**Estratégia Pedagógica:** A (Outside-In) — Da intuição geométrica de margem de segurança entre duas classes $\to$ Formulação do primal quadrático $\to$ Dualidade de Lagrange e condições KKT $\to$ Margem suave e perda Hinge $\to$ Truque do Kernel $\to$ Calibração de Platt e SVR.
**Dataset-fio:** Breast Cancer Wisconsin ($N = 569, d = 30$), utilizando o par 2D (`mean radius` $\times$ `mean texture`) para visualização analítica dos hiperplanos, margens e vetores de suporte, e validação cruzada nos 30 atributos.

---

## Plano de aula — Aula 11 (carga horária: ~110 min)

1. **Revisão e Introdução** (~12 min)
   - *Revisão:* Da Aula 6 (Regressão Logística probabilística minimizando a perda de entropia cruzada sobre todos os pontos) e Aula 10 (Gradient Boosting aditivo).
   - *Ideia Central:* Por que gastar capacidade matemática modelando a probabilidade condicional precisa $p(y \mid \mathbf{x})$ no interior das nuvens de dados se a única decisão que importa para classificar ocorre **na fronteira entre as classes**?
   - *Problema Motivador:* Em um conjunto linearmente separável, existem infinitos hiperplanos que separam perfeitamente os dados com erro zero de treino. Qual deles é o melhor?
   - *Roteiro (5 Perguntas Centrais):*
     1. O que é a margem geométrica de separação e por que maximizá-la minimiza a capacidade e o erro de generalização?
     2. Como a dualidade de Lagrange e as condições KKT isolam os vetores de suporte?
     3. Como a introdução de variáveis de folga $\xi_i$ (*Soft Margin*) conecta a SVM à perda Hinge?
     4. Como o Truque do Kernel projeta dados não-lineares em espaços de dimensão infinita operando apenas com produtos internos locais?
     5. Como transformar o escore geométrico determinístico da SVM em probabilidades estatisticamente válidas via calibração de Platt?
   - *Pausa Ativa 1.*

2. **Intuição — A Autoestrada de Separação e a Imunidade ao Interior** (~8 min)
   - A metáfora da rodovia: em vez de traçar uma linha infinitesimal que passa raspando nos pontos, construímos a rodovia mais larga possível entre as duas cidades (classes). A linha divisória central é a fronteira; os acostamentos são as margens.
   - O princípio da irrelevância do interior: se movermos ou adicionarmos milhares de novos pontos bem dentro de seu próprio território, a rodovia não se move um milímetro. Apenas os pontos que encostam no acostamento (os **vetores de suporte**) sustentam o asfalto.

3. **Bloco 1: Margem Máxima e o Problema Primal/Dual (Hard Margin)** (~25 min)
   - Equação do hiperplano: $\mathbf{w}^T \mathbf{x} + b = 0$.
   - Distância ortogonal de um ponto $\mathbf{x}_i$ ao hiperplano: $\frac{y_i(\mathbf{w}^T \mathbf{x}_i + b)}{\|\mathbf{w}\|}$ com $y_i \in \{-1, +1\}$.
   - Fixação da escala canônica: $\min_i y_i(\mathbf{w}^T \mathbf{x}_i + b) = 1$.
   - A margem geométrica entre as classes é $\gamma = \frac{2}{\|\mathbf{w}\|}$.
   - O Problema Primal de Otimização Convexa:
     $$\min_{\mathbf{w}, b} \frac{1}{2}\|\mathbf{w}\|^2 \quad \text{sujeito a } y_i(\mathbf{w}^T \mathbf{x}_i + b) \ge 1, \quad \forall i=1, \dots, N$$
   - A Função Lagrangeana Primal:
     $$\mathcal{L}(\mathbf{w}, b, \boldsymbol{\alpha}) = \frac{1}{2}\|\mathbf{w}\|^2 - \sum_{i=1}^N \alpha_i [y_i(\mathbf{w}^T \mathbf{x}_i + b) - 1], \quad \alpha_i \ge 0$$
   - Derivadas e condições de ponto de sela:
     $$\nabla_{\mathbf{w}} \mathcal{L} = \mathbf{w} - \sum_{i=1}^N \alpha_i y_i \mathbf{x}_i = \mathbf{0} \implies \mathbf{w} = \sum_{i=1}^N \alpha_i y_i \mathbf{x}_i$$
     $$\frac{\partial \mathcal{L}}{\partial b} = -\sum_{i=1}^N \alpha_i y_i = 0 \implies \sum_{i=1}^N \alpha_i y_i = 0$$
   - O Problema Dual de Wolfe:
     $$\max_{\boldsymbol{\alpha}} \sum_{i=1}^N \alpha_i - \frac{1}{2}\sum_{i=1}^N \sum_{j=1}^N \alpha_i \alpha_j y_i y_j \langle \mathbf{x}_i, \mathbf{x}_j \rangle \quad \text{s.a. } \alpha_i \ge 0, \, \sum_{i=1}^N \alpha_i y_i = 0$$
   - As Condições KKT e a Folga Complementar:
     $$\alpha_i [y_i(\mathbf{w}^T \mathbf{x}_i + b) - 1] = 0$$
     - Se $y_i(\mathbf{w}^T \mathbf{x}_i + b) > 1$ (ponto além da margem) $\implies \alpha_i = 0$.
     - Se $\alpha_i > 0 \implies y_i(\mathbf{w}^T \mathbf{x}_i + b) = 1$ (o ponto é um **Vetor de Suporte**!).
   - *Pausa Ativa 2.*

4. **Bloco 2: Margem Suave (Soft Margin) e a Perda Hinge** (~22 min)
   - A realidade dos dados ruidosos e sobreposição de classes.
   - Variáveis de folga (*slack variables*) $\xi_i \ge 0$:
     $$y_i(\mathbf{w}^T \mathbf{x}_i + b) \ge 1 - \xi_i$$
     - $\xi_i = 0$: classificado corretamente além da margem;
     - $0 < \xi_i \le 1$: classificado corretamente, mas dentro da margem;
     - $\xi_i > 1$: classificado incorretamente (cruzou a fronteira de decisão).
   - O Problema Primal Soft Margin:
     $$\min_{\mathbf{w}, b, \boldsymbol{\xi}} \frac{1}{2}\|\mathbf{w}\|^2 + C \sum_{i=1}^N \xi_i \quad \text{s.a. } y_i(\mathbf{w}^T \mathbf{x}_i + b) \ge 1 - \xi_i, \, \xi_i \ge 0$$
     - O parâmetro $C > 0$: tradeoff entre tamanho da margem e violações.
     - $C \to \infty$: penalização rígida (Hard Margin);
     - $C \to 0$: margens largas e tolerantes.
   - O Dual com Restrições em Caixa (*Box Constraints*):
     $$\max_{\boldsymbol{\alpha}} \sum_{i=1}^N \alpha_i - \frac{1}{2}\sum_{i=1}^N \sum_{j=1}^N \alpha_i \alpha_j y_i y_j \langle \mathbf{x}_i, \mathbf{x}_j \rangle \quad \text{s.a. } 0 \le \alpha_i \le C, \, \sum_{i=1}^N \alpha_i y_i = 0$$
   - A Conexão com a Perda Hinge (*Hinge Loss*):
     $$\min_{\mathbf{w}, b} \sum_{i=1}^N \max(0, 1 - y_i(\mathbf{w}^T \mathbf{x}_i + b)) + \frac{1}{2C} \|\mathbf{w}\|^2$$
     - Comparação gráfica: Perda Hinge vs. Perda Logística vs. Erro 0-1.
     - Por que a perda Hinge é plana (derivada zero) para $y f(\mathbf{x}) \ge 1$, gerando esparsidade exata, enquanto a logística nunca zera sua inclinação.
   - *Pausa Ativa 3.*

5. **Bloco 3: O Truque do Kernel (Kernel Trick) e Não-Linearidade** (~23 min)
   - A limitação de fronteiras hiperplanares em problemas não-lineares (ex.: anéis concêntricos, XOR, duas luas).
   - Mapeamento para espaço de atributos de alta dimensão: $\phi(\mathbf{x}) \in \mathcal{H}$.
   - O Teorema de Mercer e o Truque do Kernel:
     - No problema dual, os dados aparecem **exclusivamente como produtos internos**: $\langle \phi(\mathbf{x}_i), \phi(\mathbf{x}_j) \rangle$.
     - Se definirmos uma função kernel $k(\mathbf{x}, \mathbf{z}) = \langle \phi(\mathbf{x}), \phi(\mathbf{z}) \rangle$, podemos avaliar a similaridade no espaço de Hilbert diretamente sem calcular $\phi(\mathbf{x})$ explicitamente!
   - Catálogo de Kernels:
     1. Linear: $k(\mathbf{x}, \mathbf{z}) = \mathbf{x}^T \mathbf{z}$;
     2. Polinomial: $k(\mathbf{x}, \mathbf{z}) = (\mathbf{x}^T \mathbf{z} + c)^d$;
     3. RBF Gaussiano (*Radial Basis Function*):
        $$k(\mathbf{x}, \mathbf{z}) = \exp(-\gamma \|\mathbf{x} - \mathbf{z}\|^2)$$
        - Demonstração: a RBF projeta dados em um espaço de Hilbert de **dimensão infinita** via expansão da função exponencial em série de potências.
        - O hiperparâmetro $\gamma = \frac{1}{2\sigma^2}$: raio de influência dos vetores de suporte. $\gamma$ excessivo gera ilhas isoladas em torno de cada amostra (sobreajuste severo).
   - *Pausa Ativa 4.*

6. **Bloco 4: Calibração de Platt e Support Vector Regression (SVR)** (~15 min)
   - A saída determinística da SVM: $f(\mathbf{x}) = \sum_{i \in \text{SV}} \alpha_i y_i k(\mathbf{x}_i, \mathbf{x}) + b$.
   - O problema da ausência de probabilidades e o método de **Platt Scaling (1999)**:
     - Ajuste de uma sigmoide univariada sobre o escore: $P(Y = 1 \mid \mathbf{x}) = \frac{1}{1 + \exp(A f(\mathbf{x}) + B)}$.
     - Procedimento correto via validação cruzada out-of-fold para impedir sobreajuste na calibração.
   - Extensão para Regressão: Support Vector Regression ($\varepsilon$-SVR):
     - A perda $\varepsilon$-insensível: erros menores que $\varepsilon$ custam exatamente zero.
     - Tubo de tolerância ao redor da função: gera esparsidade nos dados para regressão.
   - *Pausa Ativa 5.*

7. **Fechamento** (~7 min)
   - *Retomando as 5 Perguntas:* Síntese conceitual das respostas estruturadas ao longo da aula.
   - *Quadro Comparativo:* Regressão Logística vs. Gradient Boosting vs. SVM Linear vs. Kernel RBF.
   - *Ponte para a Aula 12:* A SVM usa kernels fixos pré-programados para projetar em alta dimensão. Como aprender representações e transformações de forma adaptativa e profunda a partir dos próprios dados? $\to$ **Aula 12: Redes Neurais e Aprendizado de Representações**.
   - Links para Exercícios e Soluções.

---

## Fontes usadas — Aula 11

Deslocamentos página impressa → PDF: `prml.pdf` +20; `esl.pdf` +19.

### Fonte 1: Bishop, C. M. (2006), *Pattern Recognition and Machine Learning* (PRML), Cap. 7 (§7.1, pp. 325–345, PDF pp. 345–365)
**Uso pretendido:** Formulação geométrica da margem máxima, dual de Lagrange, condições KKT e esparsidade dos vetores de suporte, margem suave com variáveis de folga $\xi_n$ e relação com a perda Hinge.
**Trechos:**
> "We now consider a class of classification, regression and other algorithms that are linear combinations of fixed basis functions... A central property of these models is that the parameter values are found by solving a quadratic programming problem... The margin is defined as the perpendicular distance between the decision boundary and the closest of the data points. Maximizing the margin leads to a particular choice of decision boundary that has good generalization properties... The points for which $\alpha_n > 0$ are called support vectors... If a data point satisfies $y_n y(\mathbf{x}_n) > 1$, then $\alpha_n = 0$ and this point has no role in determining the boundary." (§7.1.1, pp. 327–330)
> "We can interpret the soft-margin support vector machine as the minimization of an error function with a regularizer: $\sum_{n=1}^N E_{SV}(y_n f(\mathbf{x}_n)) + \lambda \|\mathbf{w}\|^2$ where $E_{SV}$ is the hinge error function." (§7.1.3, p. 337)

### Fonte 2: Hastie, T., Tibshirani, R., & Friedman, J. (2009), *The Elements of Statistical Learning* (ESL), Cap. 12 (§12.1–§12.3, pp. 417–438, PDF pp. 436–457)
**Uso pretendido:** The Support Vector Classifier, formulação primal e dual com restrições em caixa ($0 \le \alpha_i \le C$), o truque do kernel, perda Hinge e comparação detalhada com a perda de entropia cruzada da regressão logística.
**Trechos:**
> "The support vector machine produces non-linear boundaries by constructing a linear boundary in a large, transformed version of the feature space... The Lagrange dual problem is $\max_\alpha \sum \alpha_i - \frac{1}{2}\sum \alpha_i \alpha_j y_i y_j \langle \mathbf{x}_i, \mathbf{x}_j \rangle$ subject to $0 \le \alpha_i \le C$... Notice that the solution has the form $\hat{f}(x) = \sum \hat{\alpha}_i y_i K(x, x_i) + \hat{\beta}_0$. Only the points with $\hat{\alpha}_i > 0$ (the support vectors) define the boundary." (§12.2 e §12.3, pp. 420–424)

### Fonte 3: Cortes, C. & Vapnik, V. (1995), "Support-vector networks", *Machine Learning*, 20(3): 273–297
**Uso pretendido:** A formulação seminal do classificador de margem suave (*Soft Margin*) com variáveis de folga $\xi_i$ e penalização $C$.
**Trecho:**
> "The support-vector network implements the following idea: it maps the input vectors into some high-dimensional feature space through a non-linear mapping chosen a priori. In this space, a linear decision surface is constructed with special properties that ensure high generalization ability... An optimal hyperplane is defined as the unique hyperplane characterized by maximum margin." (p. 273)

### Fonte 4: Platt, J. (1999), "Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods", *Advances in Large Margin Classifiers*
**Uso pretendido:** Fundamentação estatística do método de Platt Scaling para calibração de probabilidades a posteriori a partir de margens de decisão determinísticas da SVM.
**Trecho:**
> "Standard Support Vector Machines produce an uncalibrated real-valued output that is not a probability. We propose an algorithm that trains a parametric sigmoid model $P(y=1\mid f) = \frac{1}{1 + \exp(Af + B)}$ to map the SVM outputs into posterior probabilities using an out-of-fold maximum likelihood formulation." (p. 61)

