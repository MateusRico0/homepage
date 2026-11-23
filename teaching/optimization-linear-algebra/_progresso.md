# Progresso — Optimization and Linear Algebra for Machine Learning

Estado aprovado + notações, para dar continuidade entre aulas. O histórico de correções está no git (a versão longa anterior deste arquivo foi até o commit `1d4a4fc`).

**Fontes** (`_fontes/`, symlinks; deslocamento página impressa → PDF): `mathml.pdf` (Deisenroth et al.) +6; `copt.pdf` (Boyd & Vandenberghe) +14; `optml.pdf` (Wright & Recht) ainda sem uso nem deslocamento conferido.
**Problema-fio desde a Aula 2:** regressão linear múltipla no California Housing (escalas heterogêneas, multicolinearidade `AveRooms`/`AveBedrms`).
**Código compartilhado:** `src/metrics.py` (`compute_norm`, `inner_product`).
**Convenções:** gradiente como vetor-**coluna** (desde a Aula 6; o MathML usa linha) e Jacobiano *denominator layout* ($n\times m$, colunas = gradientes das componentes; o MathML usa *numerator*). A transferência de domínio nos V/F fica sempre dentro de ML: uma varredura em 2026-09-14 trocou 12 itens de física/engenharia.

## Estado das aulas

| Pasta | Aula | Estratégia | Estado |
|---|---|---|---|
| `aula01` | 1 — Espaços vetoriais, normas e métricas | B | publicada |
| `aula02` | 2 — Matrizes, sistemas lineares e independência | B | publicada |
| `aula03` | 3 — Projeções ortogonais e subespaços | B | publicada |
| `aula04` | 4 — Autovalores, autovetores e matrizes simétricas | B | publicada |
| `aula05` | 5 — SVD e aproximações de baixo posto | B | publicada |
| `aula06` | 6 — Derivadas parciais, Jacobiano e gradiente | B | publicada |
| `aula07` | 7 — Convexidade e a Hessiana | B | publicada |
| `aula08` | 8 — Otimização irrestrita e descida do gradiente | B | publicada |
| `aula09` | 9 — Funções compostas, redes neurais e diferenciação automática | B | desenvolvimento |
| `aula10` | 10 — Gradiente Descendente Estocástico (SGD) e Mini-Batching | B | publicada |
| `aula11` | 11 — Otimização de Segunda Ordem e Precondicionamento Diagonal | B | publicada |
| `aula12` | 12 — Momento, Curvatura e Métodos Acelerados (Adam & AdamW) | B | publicada |
| `aula13` | 13 — Precondicionamento Estruturado e Ortogonalização Matricial (Shampoo & Muon) | B | publicada |
| `aula14` | 14 — Otimização Não-Suave, Subgradientes e Operadores Proximais (ISTA & FISTA) | B | publicada |
| — | 15+ — Otimização Restrita, Condições KKT e Métodos de Ponto Interior | — | não iniciadas |

## Fio condutor (o que cada aula deixa para a seguinte)

- **1:** dados como vetores; hipótese da variedade; normas $L_1/L_2/L_\infty$, produto interno, métrica. $d_{\cos}$ **não** é métrica ($\sqrt{2d_{\cos}}$, a distância cordal, é); $k$-NN; fecha com RAG.
- **2:** matriz de design $X\in\mathbb R^{N\times d}$; $X\mathbf w=\mathbf y$ lido por linhas e por colunas; os três tipos de solução; independência e posto; multicolinearidade real. **Ponte:** $N\gg d$ torna o sistema sobredeterminado.
- **3:** melhor aproximação = projeção ortogonal em $\text{col}(X)$; complemento ortogonal; equações normais $X^TX\hat{\mathbf w}=X^T\mathbf y$.
- **4:** autovalores/autovetores, polinômio característico, teorema espectral, definitude, Rayleigh, $\text{cond}(A)$. **Ponte:** uma $X$ retangular pede a SVD.
- **5:** SVD (completa/reduzida/truncada), Eckart-Young-Mirsky, decomposição polar, $\text{cond}(X^TX)=\text{cond}(X)^2$. **Ponte:** falta como achar parâmetros que minimizam uma perda.
- **6:** derivadas parciais, gradiente, derivada direcional, Jacobiano, regra da cadeia com Jacobiano; $\nabla L=\mathbf 0$ dá só um ponto crítico. **Ponte:** mínimo, máximo ou sela? → Hessiana e convexidade.
- **7:** conjuntos e funções convexas, epígrafe, condição de 1ª ordem ($\nabla f(\mathbf{x})=\mathbf{0} \implies$ mínimo global), condição de 2ª ordem ($\nabla^2 f \succeq 0$), Hessiana da perda quadrática $2X^TX$, regularização Ridge $2(X^TX+\lambda I)$ para unicidade estrita. **Ponte:** quando $N, d$ são gigantescos ou não há solução analítica (ex: regressão logística), como encontrar o mínimo numericamente? → descida do gradiente.
- **8:** otimização irrestrita e descida do gradiente; taxa de aprendizado $\alpha$; Lema da Descida ($L$-suavidade, $\alpha < 2/L$); dinâmica espectral de erro $\mathbf{e}_{k+1} = (I - \alpha A)\mathbf{e}_k$; taxa ótima de contração de Chebyshev $\rho^\star = \frac{\kappa-1}{\kappa+1}$; diagnóstico do mau condicionamento do California Housing ($\kappa \approx 23.460{,}5 \to \rho^\star \approx 0{,}99991$); aceleração dramática por padronização $Z$-score ($\kappa \approx 12{,}9 \to \rho^\star \approx 0{,}856$); regressão logística e entropia cruzada binária (perda sem solução fechada com gradiente $\frac{1}{N}X^T(\hat{\mathbf{y}}-\mathbf{y})$ e Hessiana $\frac{1}{N}X^TSX \succ 0$). **Ponte:** modelos compostos e não-lineares (redes neurais) exigem diferenciação em cadeia e motores de execução em grafos $\to$ Funções Compostas, Redes Neurais e Diferenciação Automática.
- **9:** regra da cadeia multivariada com Jacobianos em *denominator layout*; Perceptrons Multicamadas (MLP); retropropagação analítica com vetor de sensibilidade $\boldsymbol{\delta}^{(l)} = ((W^{(l+1)})^T \boldsymbol{\delta}^{(l+1)})\odot \sigma'(\mathbf{z}^{(l)})$ e gradiente de pesos $\nabla_{W^{(l)}}\mathcal{L} = \boldsymbol{\delta}^{(l)}(\mathbf{a}^{(l-1)})^T$; colapso da diferenciação manual e simbólica; DAGs de computação; modos forward ($\dot{v}_i$) e reverse ($\bar{v}_i$); Teorema de Baur-Strassen ($C_{\text{grad}} \le 5C$); mini-autodiff orientado a objetos em Python com ordenação topológica (DFS); fita de execução (*tape*) e *activation checkpointing* ($O(L) \to O(\sqrt{L})$); fecha o Bloco 2. **Ponte:** como calcular gradientes quando $N$ é gigantesco e avaliar o grafo completo a cada iteração torna-se inviável? $\to$ Bloco 3: Gradiente Descendente Estocástico (SGD) e Mini-Batching (Aula 10). E mais adiante: séries de Taylor e modelos quadráticos de curvatura para Métodos Acelerados (Momento) e Métodos de Newton.
- **10:** formulação de somas finitas $F(\mathbf{w}) = \frac{1}{N}\sum f_i(\mathbf{w})$; gargalo do BGD ($\mathcal{O}(Nd)$ por passo); algoritmo SGD puro ($B = 1$); estimador estatístico não-enviesado ($\mathbb{E}[\mathbf{g}_k] = \nabla F(\mathbf{w})$); decomposição sinal/ruído ($\mathbf{g}_k = \nabla F + \boldsymbol{\xi}_k$ com $\mathbb{E}[\boldsymbol{\xi}_k] = \mathbf{0}$); matriz de covariância do ruído $\Sigma(\mathbf{w})$ e variância escalar $\sigma^2(\mathbf{w})$; patologia central no ótimo ($\Sigma(\mathbf{w}^\star) \succ 0$ e persistência do ruído, sem ponto fixo sob taxa constante); mini-batching e redução de variância ($\sigma^2/B$ com reposição, $\frac{N-B}{N-1}\frac{\sigma^2}{B}$ sem reposição); física do hardware moderno: operações BLAS-1 vs BLAS-3, pipelines SIMD/Tensor Cores e curva de throughput; dinâmica da bola de ruído estacionária ($\lim \mathbb{E}[\|\mathbf{w}_k - \mathbf{w}^\star\|^2] \le \frac{\alpha \sigma^2}{2\mu}$); condições de convergência de Robbins-Monro (1951) ($\sum \alpha_k = \infty, \sum \alpha_k^2 < \infty$); cronogramas práticos (*step decay*, polinomial $1/\sqrt{k}$, *cosine annealing*); o ruído como regularizador implícito (escape de pontos de sela e seleção de *flat minima* vs *sharp minima*); abre o Bloco 3. **Ponte:** o SGD utiliza uma taxa de aprendizado escalar única $\alpha$ para todos os parâmetros; em superfícies anisotrópicas, algumas coordenadas são esparsas ou possuem curvatura acentuada, exigindo passos adaptativos por coordenada; qual seria o passo ideal dado pela curvatura de 2ª ordem? $\to$ Métodos de Segunda Ordem (Newton) e Precondicionamento Diagonal (Aula 11).
- **11:** aproximação quadrática multivariada de Taylor $f(\mathbf{w}+\Delta\mathbf{w}) \approx f(\mathbf{w}) + \nabla f^T\Delta\mathbf{w} + \frac{1}{2}\Delta\mathbf{w}^T H \Delta\mathbf{w}$; minimizador do modelo quadrático e direção de Newton $\Delta\mathbf{w} = -H^{-1}\nabla f$; convergência quadrática local ($\|\mathbf{e}_{k+1}\| \le M \|\mathbf{e}_k\|^2$); patologias em ML: custo $\mathcal{O}(d^3)$, memória $\mathcal{O}(d^2)$, sensibilidade a ruído estocástico e atração por pontos de sela quando $H \not\succ 0$; Newton amortecido e regularizado ($H + \lambda I$); transição para precondicionamento: transformação de variáveis $\tilde{\mathbf{w}} = P^{1/2}\mathbf{w}$ e matriz de precondicionamento $D \approx H$; precondicionamento diagonal por coordenada; AdaGrad (Duchi et al., 2011) com acúmulo histórico $G_t = \sum g_\tau^2$ e desaceleração prematura ($\alpha / \sqrt{G_t + \epsilon}$); RMSProp (Hinton, 2012) com média móvel exponencial (EMA) $v_t = \beta_2 v_{t-1} + (1-\beta_2)g_t^2$ resolvendo o congelamento do AdaGrad; invariância a reescalonamento diagonal. **Ponte:** o RMSProp equaliza as velocidades por coordenada, mas não possui inércia temporal; em desfiladeiros estreitos com correlações cruzadas, ele ainda oscila; como incorporar memória direcional de primeira ordem e fundir momento e taxas adaptativas? $\to$ Momento, Curvatura e Métodos Acelerados (Adam) (Aula 12).
- **12:** desfiladeiros anisotrópicos e platôs com autovalores pequenos; Momento de Polyak (Heavy-ball) com oscilação ortogonal amortecida e dinâmica em espaço de estados $2\times 2$; Gradiente Acelerado de Nesterov (NAG) com look-ahead $\mathbf{w}_k + \beta \mathbf{v}_k$ e taxa ótima $\rho \approx 1 - \frac{2}{\sqrt{\kappa}}$; cota teórica ótima de Nesterov $\mathcal{O}(1/k^2)$ e polinômios de Chebyshev; Adam como síntese de 1º momento direcional $m_t$ (EMA) e 2º momento adaptativo $v_t$ (EMA de gradientes quadrados); correção de viés para inicialização em zero; patologia da regularização $L_2$ acoplada ao 2º momento no Adam e desacoplamento formal via AdamW ($w_{t+1} = (1-\gamma \lambda)w_t - \frac{\alpha}{\sqrt{v_t}+\epsilon}m_t$). **Ponte:** O Adam escala apenas a diagonal principal ($v_t \in \mathbb{R}^d$), ignorando correlações cruzadas entre neurônios de uma mesma camada matricial $W \in \mathbb{R}^{m \times n}$; como precondicionar matrizes completas sem custo cúbico ou ortogonalizar passos diretamente em hardware? $\to$ Precondicionamento Estruturado e Ortogonalização Matricial (Shampoo & Muon) (Aula 13).
- **13:** limitações do precondicionamento diagonal (Adam); tensores e matrizes de pesos $W \in \mathbb{R}^{m \times n}$; covariâncias Kronecker-factored no Shampoo ($L = \sum G G^T$, $R = \sum G^T G$) e precondicionamento bi-linear $L^{-1/4} G R^{-1/4}$; conexão com a Decomposição Polar $M = U P = U (M^T M)^{1/2}$ e o Problema de Procrustes Ortogonal ($\min_{O \in \mathcal{O}} \|M - O\|_F$); iterações polinomiais de Newton-Schulz ($X_{k+1} = \frac{1}{2} X_k (3I - X_k^T X_k)$) para ortogonalização matricial de alta performance baseada puramente em multiplicações matriciais (GEMM) em GPUs/TPUs; o otimizador Muon (Keller et al., 2024), combinando momentum de Nesterov no gradiente matricial, ortogonalização de espectro unitário via Newton-Schulz e scaling espectral/Frobenius adaptativo. **Ponte:** Todos os métodos até aqui exigiram funções suaves e diferenciáveis ($C^1$ ou $C^2$); o que acontece quando a função de perda contém termos pontiagudos ou não-diferenciáveis, como a norma $L_1$ no Lasso para induzir esparsidade estruturada? $\to$ Otimização Não-Suave, Subgradientes e Operadores Proximais (ISTA & FISTA) (Aula 14).
- **14:** falha da derivada clássica em funções não-suaves ($f(w)=|w|$); definição de subgradiente e subdiferencial convexo $\partial f(\mathbf{w}) = \{\mathbf{g} \mid f(\mathbf{u}) \ge f(\mathbf{w}) + \mathbf{g}^T(\mathbf{u}-\mathbf{w})\}$; método do subgradiente e taxa lenta $\mathcal{O}(1/\sqrt{k})$ com passos $\alpha_k \to 0$; resolução via divisão de operadores (*operator splitting*) e Operador Proximal $\text{prox}_{\gamma h}(\mathbf{w}) = \arg\min_{\mathbf{z}} \{h(\mathbf{z}) + \frac{1}{2\gamma}\|\mathbf{z}-\mathbf{w}\|_2^2\}$; derivação analítica fechada do operador de encolhimento suave (*soft-thresholding*) $\mathcal{S}_{\gamma \lambda}(w) = \text{sign}(w)\max(0, |w| - \gamma \lambda)$; Algoritmo de Limiarização Iterativa por Gradiente Proximal (ISTA) para problemas compostos $f(\mathbf{w}) = g(\mathbf{w}) + h(\mathbf{w})$ com taxa $\mathcal{O}(1/k)$; aceleração de Nesterov no domínio proximal com FISTA (Beck & Teboulle, 2009) atingindo taxa ótima $\mathcal{O}(1/k^2)$ preservando esparsidade exata dos coeficientes. **Ponte:** O operador proximal nos permitiu lidar com penalidades não-suaves; mas e quando as variáveis precisam respeitar restrições duras explícitas (ex: $\mathbf{w} \ge 0$, $\sum w_i = 1$, ou restrições de igualdade $A\mathbf{w}=\mathbf{b}$)? $\to$ Otimização Restrita, Condições KKT, Dualidade de Lagrange e Métodos de Barreira/Penalidade (Aula 15).

## Dicionário de notações

| Símbolo/termo | Significado | Aula |
|---|---|---|
| $\lVert\mathbf x\rVert_1,\lVert\mathbf x\rVert_2,\lVert\mathbf x\rVert_\infty$ | normas $L_1$, $L_2$, $L_\infty$ | 1 |
| $\langle\mathbf x,\mathbf y\rangle$ | produto interno | 1 |
| $d(\mathbf x,\mathbf y)$, $d_{\cos}=1-\cos\theta$ | métrica; distância do cosseno (não é métrica) | 1 |
| $X\in\mathbb R^{N\times d}$ | matriz de design ($N$ observações, $d$ atributos) | 2 |
| $\text{rk}(A)$, $\text{rk}(A\mid\mathbf b)$ | posto; posto da matriz aumentada (critério de solvabilidade) | 2 |
| $\text{col}(X)$ | espaço-coluna | 2–3 |
| $U^\perp$ | complemento ortogonal | 3 |
| $\hat{\mathbf y}=X\hat{\mathbf w}$ | projeção ortogonal de $\mathbf y$ em $\text{col}(X)$ | 3 |
| $\lambda$ | autovalor | 4 (Bloco 2) |
| autovetor $\mathbf{x}$ (na equação $A\mathbf{x}=\lambda\mathbf{x}$) | direção que $A$ só estica/encolhe, nunca gira | 4 (Bloco 2) |
| $p_A(\lambda)=\det(A-\lambda I)$ | polinômio característico de $A$ | 4 (Bloco 3) |
| $E_\lambda$ | autoespaço associado ao autovalor $\lambda$ | 4 (Bloco 3) |
| multiplicidade algébrica/geométrica | grau da raiz no polinômio característico / dimensão do autoespaço | 4 (Bloco 4 (menção breve)) |
| $A=PDP^{-1}$ | decomposição em autovalores (matriz diagonalizável geral) | 4 (Bloco 4) |
| $A=Q\Lambda Q^T$ | decomposição espectral (matriz simétrica, $Q$ ortogonal) | 4 (Bloco 4) |
| $A\succ 0$ / $A\succeq 0$ | matriz (simétrica) positiva definida / semidefinida | 4 (Bloco 5) |
| quociente de Rayleigh $\mathbf{x}^TA\mathbf{x}/\mathbf{x}^T\mathbf{x}$ | média ponderada dos autovalores, limitada por $\lambda_{\min}$/$\lambda_{\max}$ | 4 (Bloco 5) |
| $\text{cond}(A)=\lambda_{\max}(A)/\lambda_{\min}(A)$ | número de condição exato (matrizes simétricas PSD) | 4 (Bloco 5) |
| $A=U\Sigma V^T$ | Decomposição em Valores Singulares (SVD) | 5 (Bloco 3) |
| $\sigma_i$ | valor singular (sempre real, $\ge0$, ordenado $\sigma_1\ge\dots\ge\sigma_r>0$) | 5 (Bloco 3) |
| $\mathbf{u}_i$ (coluna de $U$) | vetor singular à esquerda (autovetor de $AA^T$) | 5 (Bloco 3) |
| $\mathbf{v}_i$ (coluna de $V$) | vetor singular à direita (autovetor de $A^TA$) | 5 (Bloco 3) |
| SVD completa / reduzida / truncada | $U,V$ quadradas completas / $U$ recortada ao posto / soma dos $k$ primeiros termos | 5 (Bloco 3-5) |
| $\hat{A}^{(k)}=\sum_{i=1}^k\sigma_i\mathbf{u}_i\mathbf{v}_i^T$ | aproximação de posto-$k$ (SVD truncada) | 5 (Bloco 5) |
| $\|A\|_2$ | norma espectral ($=\sigma_1$, Teo. 4.24) | 5 (Bloco 5) |
| Teorema de Eckart-Young-Mirsky | $\hat{A}^{(k)}$ é a melhor aproximação de posto $k$ em norma espectral (e de Frobenius, generalização de Mirsky), erro $=\sigma_{k+1}$ | 5 (Bloco 5) |
| $A=QS$ | Decomposição Polar ($Q$ ortogonal, $S$ simétrica semidefinida positiva) | 5 (Bloco 6) |
| $\text{cond}(X)=\sigma_{\max}/\sigma_{\min}$ | número de condição via valores singulares (Boyd, já citado na Aula 4); $\text{cond}(X^TX)=\text{cond}(X)^2$ | 5 (Bloco 4) |
| $\partial f/\partial x_i$ | derivada parcial de $f$ em relação a $x_i$ (demais variáveis fixas) | 6 (Bloco 2) |
| $\nabla f$, $\nabla_{\mathbf{x}}f$, $df/d\mathbf{x}$ | gradiente de $f$ (vetor-**coluna**; o MathML usa linha) | 6 (Bloco 3) |
| $D_{\mathbf{v}}f(\mathbf{x})$ | derivada direcional de $f$ em $\mathbf{x}$, na direção unitária $\mathbf{v}$ | 6 (Bloco 4) |
| $J$, $J_f(\mathbf{x})$ | Jacobiano de $f:\mathbb{R}^n\to\mathbb{R}^m$ (matriz $n\times m$, *denominator layout*; gradiente = caso $m=1$) | 6 (Bloco 5) |
| $\mathbf{r}(\boldsymbol{\beta})=X\boldsymbol{\beta}-\mathbf{y}$ | resíduo como função vetorial de $\boldsymbol{\beta}$; $J_{\mathbf{r}}(\boldsymbol{\beta})=X^T$ | 6 (Bloco 5) |
| regra da cadeia com Jacobiano | $\nabla_{\boldsymbol{\beta}}(g\circ\mathbf{r})=J_{\mathbf{r}}(\boldsymbol{\beta})\,\nabla_{\mathbf{r}}g$ | 6 (Bloco 5) |
| ponto crítico | ponto onde $\nabla f=\mathbf{0}$ — não garante mínimo/máximo sem informação adicional | 6 (Fechamento) |
| $\mathrm{epi}\,f = \{(\mathbf{x}, t) \mid f(\mathbf{x}) \le t\}$ | epígrafe de uma função; $f$ convexa $\iff \mathrm{epi}\,f$ conjunto convexo | 7 (Bloco 1) |
| $\nabla^2 f(\mathbf{x})$ | matriz Hessiana ($d\times d$, simétrica se $C^2$); curvatura de 2ª ordem | 7 (Bloco 2) |
| $\nabla^2 f \succeq 0$ | condição necessária e suficiente de 2ª ordem para convexidade | 7 (Bloco 2) |
| $2(X^T X + \lambda I)$ | Hessiana da perda com regularização Ridge ($\lambda > 0 \implies \succ 0$) | 7 (Bloco 4) |
| $\alpha$ | taxa de aprendizado (*step size* / comprimento de passo na direção $-\nabla f$) | 8 (Bloco 1) |
| $L$ | constante de Lipschitz do gradiente ($\|\nabla f(\mathbf{x}) - \nabla f(\mathbf{y})\| \le L\|\mathbf{x}-\mathbf{y}\|$) / suavidade | 8 (Bloco 2) |
| Lema da Descida | $f(\mathbf{w} - \alpha\nabla f(\mathbf{w})) \le f(\mathbf{w}) - \alpha(1 - \frac{\alpha L}{2})\|\nabla f(\mathbf{w})\|^2$; descida garantida se $0 < \alpha < 2/L$ | 8 (Bloco 2) |
| $\mathbf{e}_k = \mathbf{w}_k - \mathbf{w}^\star$ | vetor de erro em relação ao minimizador na iteração $k$ | 8 (Bloco 3) |
| $\mathbf{e}_{k+1} = (I - \alpha A)\mathbf{e}_k$ | dinâmica espectral de contração de erro em formas quadráticas | 8 (Bloco 3) |
| $\rho^\star = \frac{\kappa-1}{\kappa+1}$ | fator de contração espectral ótimo de Chebyshev com $\alpha^\star = \frac{2}{\lambda_{\min}+\lambda_{\max}}$ | 8 (Bloco 3) |
| $\sigma(z) = \frac{1}{1 + e^{-z}}$ | função logística (sigmoide); $\sigma'(z) = \sigma(z)(1-\sigma(z))$ | 8 (Bloco 5) |
| $\mathcal{L}(\mathbf{w}) = -\frac{1}{N}\sum [y_i \ln \hat{y}_i + (1-y_i)\ln(1-\hat{y}_i)]$ | perda de entropia cruzada binária (sem solução analítica fechada) | 8 (Bloco 5) |
| $S = \text{diag}(\hat{y}_i(1-\hat{y}_i))$ | matriz diagonal de ponderação da Hessiana logística ($\nabla^2\mathcal{L} = \frac{1}{N}X^TSX \succ 0$) | 8 (Bloco 5) |
| $\boldsymbol{\delta}^{(l)} = \nabla_{\mathbf{z}^{(l)}}\mathcal{L}$ | vetor de sensibilidade pré-sináptica da camada $l$ em redes neurais | 9 (Bloco 1) |
| $\boldsymbol{\delta}^{(l)} = ((W^{(l+1)})^T \boldsymbol{\delta}^{(l+1)})\odot \sigma'(\mathbf{z}^{(l)})$ | equação canônica de retropropagação de sensibilidade | 9 (Bloco 1) |
| $\nabla_{W^{(l)}}\mathcal{L} = \boldsymbol{\delta}^{(l)}(\mathbf{a}^{(l-1)})^T$ | gradiente matricial de pesos via produto diádico erro $\times$ ativação | 9 (Bloco 1) |
| $\dot{v}_i = \partial v_i / \partial x_k$ | variável tangente no modo forward de diferenciação automática | 9 (Bloco 2) |
| $\bar{v}_i = \partial \mathcal{L} / \partial v_i$ | variável adjunta no modo reverse de diferenciação automática | 9 (Bloco 2) |
| $C_{\text{grad}} \le 5 \cdot C_{\text{eval}}$ | Teorema de Baur-Strassen / Speelpenning de complexidade temporal | 9 (Bloco 2) |
| $\mathcal{O}(\sqrt{L})$ | footprint de memória via recomputação com *activation checkpointing* | 9 (Bloco 3) |
| $\mathbf{g}_k(\mathbf{w})$ | estimador estocástico do gradiente ($\mathbb{E}[\mathbf{g}_k] = \nabla F(\mathbf{w})$) | 10 (Bloco 1-2) |
| $\boldsymbol{\xi}_k = \mathbf{g}_k - \nabla F$ | vetor de ruído estocástico de amostragem ($\mathbb{E}[\boldsymbol{\xi}_k] = \mathbf{0}$) | 10 (Bloco 2) |
| $\Sigma(\mathbf{w}) = \mathbb{E}[\boldsymbol{\xi}_k \boldsymbol{\xi}_k^T]$ | matriz de covariância do ruído estocástico ($\Sigma(\mathbf{w}^\star) \succ 0$) | 10 (Bloco 2) |
| $\sigma^2(\mathbf{w}) = \operatorname{tr}(\Sigma(\mathbf{w}))$ | variância escalar total do gradiente estocástico | 10 (Bloco 2) |
| $B$ | tamanho do mini-batch ($|\mathcal{B}| = B$) | 10 (Bloco 3) |
| $\sigma^2 / B$ | redução de variância sob amostragem com reposição | 10 (Bloco 3) |
| $\frac{N-B}{N-1}$ | fator de correção para população finita (amostragem sem reposição) | 10 (Bloco 3) |
| $\lim \mathbb{E}[\|\mathbf{w}_k - \mathbf{w}^\star\|^2] \le \frac{\alpha \sigma^2}{2\mu}$ | raio da bola de ruído estacionária sob taxa de aprendizado constante $\alpha$ | 10 (Bloco 4) |
| Condições de Robbins-Monro | $\sum \alpha_k = \infty$ (exploração) e $\sum \alpha_k^2 < \infty$ (supressão do ruído) | 10 (Bloco 4) |
| $\Delta\mathbf{w}_{\text{Newton}} = -H^{-1}\nabla f$ | passo de Newton puro via minimização do modelo quadrático | 11 (Bloco 1-2) |
| $P \succ 0$, $D = \text{diag}(s_i)$ | matriz de precondicionamento geral / diagonal | 11 (Bloco 3) |
| $G_t = \sum_{\tau=1}^t g_\tau^2$ | acúmulo histórico de gradientes quadrados (AdaGrad) | 11 (Bloco 4) |
| $v_t = \beta_2 v_{t-1} + (1-\beta_2)g_t^2$ | média móvel exponencial de gradientes quadrados / 2º momento não-central (RMSProp) | 11 (Bloco 4) |
| $\mathbf{v}_{k+1} = \beta \mathbf{v}_k - \alpha \nabla f(\mathbf{w}_k)$ | dinâmica de Momento de Polyak (Heavy-ball) | 12 (Bloco 1) |
| $\mathbf{w}_k + \beta \mathbf{v}_k$ | ponto de look-ahead no Gradiente Acelerado de Nesterov (NAG) | 12 (Bloco 2) |
| $m_t = \beta_1 m_{t-1} + (1-\beta_1)g_t$ | 1º momento / média móvel com inércia direcional (Adam) | 12 (Bloco 3) |
| $\hat{m}_t = \frac{m_t}{1-\beta_1^t}, \hat{v}_t = \frac{v_t}{1-\beta_2^t}$ | estimadores corrigidos de viés para inicialização em zero no Adam | 12 (Bloco 3) |
| $w_{t+1} = (1-\gamma \lambda)w_t - \frac{\alpha}{\sqrt{\hat{v}_t}+\epsilon}\hat{m}_t$ | atualização desacoplada do AdamW (Loshchilov & Hutter, 2019) | 12 (Bloco 4) |
| $L = \sum G G^T \in \mathbb{R}^{m\times m}, R = \sum G^T G \in \mathbb{R}^{n\times n}$ | matrizes de covariância estruturadas de linhas e colunas (Shampoo) | 13 (Bloco 1) |
| $P_{\text{shampoo}} = L^{-1/4} G R^{-1/4}$ | precondicionamento Kronecker bi-linear estruturado (Gupta et al., 2018) | 13 (Bloco 1) |
| $M = U P = U(M^TM)^{1/2}$ | fator polar ortogonal $U$ e problema de Procrustes $\min_{O \in \mathcal{O}} \|M - O\|_F$ | 13 (Bloco 2) |
| $X_{k+1} = \frac{1}{2} X_k (3I - X_k^T X_k)$ | iteração cúbica de Newton-Schulz para inversão de raiz e ortogonalização | 13 (Bloco 3) |
| Muon ($W_{t+1} = W_t - \eta \cdot \text{NS}(N_t)$) | otimizador matricial com momento de Nesterov e ortogonalização Newton-Schulz | 13 (Bloco 4) |
| $\partial f(\mathbf{w}) = \{\mathbf{g} \mid f(\mathbf{u}) \ge f(\mathbf{w}) + \mathbf{g}^T(\mathbf{u}-\mathbf{w})\}$ | subdiferencial de uma função convexa não-suave | 14 (Bloco 1) |
| $\partial |w| = \text{sign}(w)$ se $w \neq 0$, $[-1, 1]$ se $w = 0$ | subdiferencial da função valor absoluto | 14 (Bloco 1) |
| $\mathbf{w}_{k+1} = \mathbf{w}_k - \alpha_k \mathbf{g}_k$ ($\mathbf{g}_k \in \partial f$) | método do subgradiente com convergência $\mathcal{O}(1/\sqrt{k})$ sob $\alpha_k \to 0$ | 14 (Bloco 2) |
| $\text{prox}_{\gamma h}(\mathbf{w}) = \arg\min_{\mathbf{z}} \{h(\mathbf{z}) + \frac{1}{2\gamma}\|\mathbf{z}-\mathbf{w}\|_2^2\}$ | operador proximal (compromisso fidelidade ao ponto vs penalidade) | 14 (Bloco 3) |
| $\mathcal{S}_{\gamma \lambda}(w) = \text{sign}(w)\max(0, |w| - \gamma \lambda)$ | operador de encolhimento suave (*soft-thresholding*) para a norma $L_1$ | 14 (Bloco 3) |
| $\mathbf{w}_{k+1} = \text{prox}_{\alpha h}(\mathbf{w}_k - \alpha \nabla g(\mathbf{w}_k))$ | algoritmo ISTA (*Iterative Shrinkage-Thresholding Algorithm*) com taxa $\mathcal{O}(1/k)$ | 14 (Bloco 4) |
| $\mathbf{y}_{k+1} = \mathbf{w}_k + \frac{t_k - 1}{t_{k+1}}(\mathbf{w}_k - \mathbf{w}_{k-1})$ | passo de aceleração de Nesterov no FISTA com taxa ótima $\mathcal{O}(1/k^2)$ | 14 (Bloco 4) |

## Pendências

- **Aula 2:** o Bloco 1 apresenta a definição formal de matriz antes do exemplo concreto dos bairros. Inverter a ordem só com aprovação.
- **Aula 1:** o produto interno é usado no Bloco 5 sem ter sido definido formalmente no Bloco 4 (MathML §3.2.2 ainda não citado).
- **Quantidade de testes:** Aulas 2–3 têm 12 testes (a regra é 6–10).
- **Nomes legados:** `_03-respostas-pausas.md` (Aula 3) e `_00-planejamento.md`/`_01-respostas.md` (Aulas 4–6). As Aulas 1–2 não têm arquivo de respostas das pausas.

