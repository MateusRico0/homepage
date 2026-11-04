# Progresso — Supervised Learning

Estado aprovado + notações, para dar continuidade entre aulas. O histórico de correções está no git (a versão longa anterior deste arquivo foi até o commit `1d4a4fc`).

**Fontes** (`_fontes/`, symlinks; deslocamento página impressa → PDF): PRML +20, DLFC +20, ESL +19.
**Tese do curso:** todo algoritmo supervisionado = distribuição assumida + verossimilhança + regra de decisão (Aula 1, retomada na Revisão 1).
**Combinado:** aulas podem passar dos 100 min de referência.

## Estado das aulas

| Pasta | Aula | Estratégia | Dataset-fio | Estado |
|---|---|---|---|---|
| `aula01` | 1 — Dados, distribuições e detecção de anomalias | A | Beta sintética (1D, 2 classes) | publicada |
| `aula02` | 2 — Independência, Naive Bayes e teoria da decisão | A | Breast Cancer (`smoothness_mean`, `concavity_mean`) | publicada |
| `aula03` | 3 — Árvores de decisão: particionamento guloso | A | California Housing (`MedInc`, `HouseAge`) + sintéticos | publicada |
| `aula04` | 4 — Seleção de modelo, CV e Bootstrap | A | Breast Cancer (30 atributos) | publicada |
| `revisao1` | Revisão 1 — o fio probabilístico das Aulas 1–4 | B | Pima (`Glucose`, `BMI`) | publicada |
| `aula05` | 5 — Regressão linear e máxima verossimilhança | A | California Housing (`MedHouseVal` ~ `MedInc`) | publicada |
| `aula06` | 6 — Regressão logística e GLMs | A | Adult Census (idade, horas/semana) | publicada |
| `aula07` | 7 — Regularização e MAP bayesiano | B | California Housing | publicada |
| `aula08` | 8 — O tradeoff teórico viés-variância | B | Sintético ($f(x)=\sin(2\pi x)$) + California Housing | publicada |
| `aula09` | 9 — Teoria de ensembles e redução de variância | A | California Housing (8 atributos) | publicada |
| `aula10` | 10 — Gradient Boosting e otimização numérica no espaço de funções | A | California Housing (8 atributos) | publicada |
| `aula11` | 11 — Máquinas de Vetores de Suporte (SVM) | A | Breast Cancer Wisconsin (2D e 30 atributos) | publicada |

## Fio condutor (o que cada aula deixa para a seguinte)

- **1:** classificar = comparar densidades ponderadas pela priori. Limiar $T_{CONJ}$ no cruzamento das conjuntas, erros Tipo I/II como áreas, custo assimétrico, ROC, rejeição. **Ponte:** em $d$ dimensões, $p(\mathbf{x}\mid\mathcal C_k)$ não é estimável sem estrutura.
- **2:** Naive Bayes (independência condicional) e teoria da decisão geral (perda $L$, risco posterior, risco de Bayes). Com $\Sigma$ compartilhada, o log-razão é linear. **Ponte:** os modelos até aqui fixam a forma da fronteira antes de ver os dados.
- **3:** CART como MLE não paramétrico (folha gaussiana → soma de quadrados; folha categórica → entropia). Teoria da informação ($H$, $I(X;Y)$, ganho de informação = informação mútua). Poda por custo-complexidade. **Ponte:** $\lambda$ foi escolhido "olhando o gráfico".
- **4:** $\hat R(\theta)$ é um estimador otimista de $R(\theta)$. CV como simulação de amostragem, a escolha de $k$ (viés × variância do estimador), regra de 1 desvio-padrão, Bootstrap (reamostrar o teste × reamostrar e reajustar), vazamento de dados. **Ponte:** viés-variância formal na Aula 8; regressão linear na Aula 5.
- **Revisão 1:** as Aulas 1–4 como instâncias de distribuição → verossimilhança → decisão/risco. Alerta de colisão: $k$ (classe × *fold*); $\lambda$ (custo assimétrico × custo-complexidade).
- **5:** OLS geométrico (RSS, equações normais, projeção em $\mathcal S=\mathrm{span}(\varphi_1,\varphi_2)$) = MLE sob ruído gaussiano homocedástico. Viés de $\hat\sigma^2_{\text{MLE}}$. Limitações: heterocedasticidade, censura de `MedHouseVal` em $5{,}00001$. **Ponte:** trocar a Gaussiana por Bernoulli.
- **6:** logit/sigmoide, entropia cruzada = $-\ln L$, gradiente $X^T(\boldsymbol\mu-\mathbf y)$, Hessiana $X^TRX$ (convexa), IRLS, GLM e ligação canônica. **Ponte:** a separação perfeita faz $\lVert\mathbf w\rVert\to\infty$, o que motiva a regularização.
- **7:** Ridge (forma fechada $(X^TX+\lambda I)^{-1}X^T\mathbf y$), Lasso e soft-thresholding, MAP (priori gaussiana → Ridge com $\lambda=\sigma^2/\tau^2$; Laplace → Lasso com $\lambda=\sigma^2/b$). **Ponte:** como escolher $\lambda$ → decomposição viés-variância (Aula 8).
- **8:** Decomposição formal $\text{EMSE} = \text{Bias}^2 + \text{Var} + \sigma^2$; estimador como variável aleatória sobre $\mathcal{D}$; ortogonalidade e cancelamento do termo cruzado; Teorema de Hoerl & Kennard (1970) provando a existência de $\lambda > 0$ com $\text{MSE}(\hat{\boldsymbol\beta}_{\text{Ridge}}) < \text{MSE}(\hat{\boldsymbol\beta}_{\text{OLS}})$; curvas de aprendizado para diagnóstico de alto viés vs. alta variância. **Ponte:** encerramento da Parte 2; a Parte 3 ataca o tradeoff por Ensembles (Bagging reduz variância na Aula 9; Boosting reduz viés na Aula 10).
- **9:** Bagging como média bootstrap; preservação de viés ($\mathbb{E}[\bar{T}] = \mathbb{E}[T]$); derivação da variância correlacionada $\rho \sigma^2 + \frac{1-\rho}{B}\sigma^2$; Random Forests (Breiman, 2001) e descorrelação via subamostragem de $m \le p$ variáveis por nó; avaliação Out-of-Bag ($(1 - 1/N)^N \to 1/e \approx 36{,}8\%$); MDI (viés de alta cardinalidade) vs. MDA (permutação OOB). **Ponte:** Bagging reduz variância partindo de árvores profundas; a Aula 10 ataca o viés via Boosting sequencial no espaço de funções.
- **10:** AdaBoost como FSAM sob perda exponencial ($L=e^{-yf}$); dedução de $\alpha_m$ e pesos; Friedman (2001) e Gradient Boosting Machine: resíduos como gradiente negativo no espaço de funções ($r_{im} = -\frac{\partial L}{\partial f}$); pseudo-resíduos para $L_2$, $L_1$ (mediana), Huber e Deviance binária ($y - p$); busca linear na folha terminal ($\gamma_{jm}$); encolhimento $\nu \le 0{,}1$ (*shrinkage*); teorema de ordem de interação de árvores ($K \le J - 1$); interpretabilidade pós-ajuste (importância relativa e PDP) e modelos intrinsecamente explicáveis (EBM / $GA^2M$). **Ponte:** de comitês aditivos de milhares de regras ortogonais locais para a busca de um único hiperplano ótimo de margem máxima via formulação dual e truque do kernel nas Máquinas de Vetores de Suporte (SVM, Aula 11).
- **11:** Ruptura com a modelagem global de $p(y \mid \mathbf{x})$; hiperplano afim e margem geométrica canônica $\gamma = \frac{2}{\|\mathbf{w}\|}$; formulação primal quadrática e dual de Wolfe; condições KKT e folga complementar provando a esparsidade dos vetores de suporte ($\alpha_i > 0$); margem suave (*Soft Margin*) com variáveis de folga $\xi_i \ge 0$, restrições em caixa $0 \le \alpha_i \le C$ e equivalência analítica com a minimização da perda Hinge regularizada; Truque do Kernel (*Kernel Trick*) via Teorema de Mercer e catálogo de kernels (Linear, Polinomial, RBF Gaussiano com projeção em espaço de Hilbert de dimensão infinita $\ell^2$); Calibração de Platt (1999) via regressão logística out-of-fold para escores de margem e Support Vector Regression ($\varepsilon$-SVR) com tubo de tolerância. **Ponte:** a SVM utiliza kernels analíticos fixados a priori pelo engenheiro; a Aula 12 introduz a aprendizagem profunda de representações não lineares a partir dos próprios dados via Redes Neurais Artificiais e Backpropagation.

## Dicionário de notações

| Símbolo/termo | Significado | Aula |
|---|---|---|
| $\mathcal C_k$, $\pi_k$ | classe $k$; priori $p(\mathcal C_k)$ | 1 |
| $p(x\mid\mathcal C_k)$ | densidade condicional de classe | 1 |
| $\mathrm{Beta}(a,b)$ | família para dados em $[0,1]$ | 1 |
| $T_{CONJ}$ | limiar no cruzamento das conjuntas $p(x,\mathcal C_k)$ | 1 |
| $\mathcal R_k$ | região de decisão da classe $k$ | 1 |
| Tipo I / Tipo II | falso positivo / falso negativo | 1 |
| $L$, $\rho(a\mid\mathbf x)$ | matriz de perda; risco posterior da ação $a$ | 2 |
| $\Sigma$ compartilhada / diagonal | Gaussiana plena com $\Sigma$ comum (fronteira linear) / Naive Bayes gaussiano | 2 |
| $\mathcal R_\tau$, $Q_\tau$ | região da folha $\tau$; soma de quadrados na folha | 3 |
| $H(\hat p_\tau)$, Gini | impurezas da folha (nats) | 3 |
| $I(X;Y)$, $IG(\tau,s)$ | informação mútua; ganho de informação do corte $s$ (= $I(S;\mathcal C)$ local) | 3 |
| $\sum_\tau Q_\tau(T)+\lambda\lvert T\rvert$ | critério de custo-complexidade da poda | 3 |
| $\hat R(\theta)$, $R(\theta)$ | risco empírico (treino); risco esperado | 4 |
| $k$ (CV), $B$ | número de *folds*; número de réplicas de Bootstrap | 4 |
| $\boldsymbol\beta$ | coeficientes da regressão (não o $\beta$ de precisão do PRML; usamos $\sigma^2$) | 5 |
| RSS, $\hat{\mathbf y}=X\hat{\boldsymbol\beta}$, $\mathcal S$ | soma de quadrados dos resíduos; projeção no espaço-coluna | 5 |
| $\hat\sigma^2_{\text{MLE}}$ | MLE da variância do ruído (enviesado) | 5 |
| $a=\mathbf w^T\mathbf x$, $\sigma(a)$, $\mu_n$ | ativação; sigmoide; $p(\mathcal C_1\mid\mathbf x_n)$ | 6 |
| $E(\mathbf w)$ | entropia cruzada binária | 6 |
| $R$ ($R_{nn}=\mu_n(1-\mu_n)$) | pesos do IRLS | 6 |
| $\eta=g(\mu)$ | parâmetro natural e função de ligação (GLM) | 6 |
| $\lambda$ (Ridge/Lasso), $\tau^2$, $b$ | força da regularização; variância da priori gaussiana; escala da Laplace | 7 |
| $\hat{\boldsymbol\beta}_{\text{Ridge}}$, $\hat{\boldsymbol\beta}_{\text{MLE}}$ | estimadores regularizado / não regularizado | 7 |
| $\text{EMSE}(\mathbf{x})$ | Erro Quadrático Médio Esperado $\mathbb{E}_{\mathcal{D},\epsilon}[(y - \hat{f}(\mathbf{x}))^2]$ | 8 |
| $\bar{f}(\mathbf{x})$ | estimador médio $\mathbb{E}_{\mathcal{D}}[\hat{f}(\mathbf{x};\mathcal{D})]$ sobre conjuntos de treino | 8 |
| $\text{Bias}^2(\mathbf{x}), \text{Var}(\mathbf{x}), \sigma^2$ | viés ao quadrado, variância do estimador e erro irredutível | 8 |
| $\hat{f}_{\text{bag}}, \hat{f}_{\text{rf}}$ | estimadores Bagging e Random Forest | 9 |
| $\rho$ (ensemble) | correlação par-a-par entre estimadores do ensemble | 9 |
| $m$ (RF) | número de variáveis candidatas sorteadas por divisão de nó | 9 |
| $\text{OOB}, \mathcal{B}_i$ | Out-of-Bag; conjunto de árvores onde $\mathbf{z}_i$ não participou do treino | 9 |
| $\text{MDI}, \text{MDA}$ | Mean Decrease Impurity / Mean Decrease Accuracy (Permutação) | 9 |
| $M$ | número total de iterações/árvores na expansão aditiva de Boosting | 10 |
| $h_m(\mathbf{x})$ | modelo base / hipótese fraca (*weak learner*) ajustada na iteração $m$ | 10 |
| $\alpha_m$ | coeficiente analítico do classificador base no AdaBoost | 10 |
| $r_{im}, g_{im}$ | pseudo-resíduo e gradiente da perda na observação $i$ e iteração $m$ | 10 |
| $\gamma_{jm}$ | valor ótimo por busca linear (*line search*) na região terminal $R_{jm}$ | 10 |
| $\nu$ (shrinkage) | taxa de aprendizado / fator de encolhimento no Gradient Tree Boosting | 10 |
| $J$ | número de nós terminais (folhas) de cada árvore constituinte | 10 |
| $I_k^2, \bar{f}_S$ | Importância Relativa de Friedman e Gráfico de Dependência Parcial (PDP) | 10 |
| $\mathbf{w}, b$ | vetor normal e deslocamento do hiperplano de separação afim | 11 |
| $\gamma$ | margem geométrica de separação canônica $\frac{2}{\|\mathbf{w}\|}$ | 11 |
| $\alpha_i$ | multiplicador de Lagrange no problema dual de Wolfe ($\alpha_i > 0 \implies$ Vetor de Suporte) | 11 |
| $\xi_i$ | variável de folga (*slack variable*) na formulação de margem suave | 11 |
| $C$ | hiperparâmetro de penalização e teto da caixa dual ($0 \le \alpha_i \le C$) | 11 |
| $L_{\text{hinge}}(z)$ | função de perda Hinge $\max(0, 1 - z)$ | 11 |
| $k(\mathbf{x}, \mathbf{z}), \mathcal{H}$ | função kernel e espaço de Hilbert de projeção implícita | 11 |
| $\gamma$ (RBF) | largura de banda do Kernel Gaussiano $\frac{1}{2\sigma^2}$ | 11 |
| $\varepsilon$ (SVR) | raio do tubo de insensibilidade da Support Vector Regression | 11 |

## Pendências

- **Numeração pós-Revisão 1:** a Ponte da `aula05` ainda anuncia a regressão logística como "Aula 7" (hoje é a Aula 6).
- **`aula07`:** no link de Soluções, a classe está como `.soluções-link`, mas a correta é `.solucoes-link` (sem ela, o link fica sem ícone).
- **`aula04`:** a seção "Resumo — Aula 4" / "Conteúdo da Aula" adicionada ao `index.qmd` está sem commit, e há um link de Exercícios no topo que duplica o do Fechamento.
- **Quantidade de testes:** Aulas 2–4 e Revisão 1 têm 12 testes (a regra é 6–10). Revisar só se o usuário pedir.
- **Nomes legados:** `_03-respostas-pausas.md` (Aulas 1, 2, 4 e Revisão 1) e `_00-planejamento.md`/`_01-respostas.md` (Aula 5).
