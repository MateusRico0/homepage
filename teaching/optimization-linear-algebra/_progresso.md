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
| `aula09` | 9 — Séries de Taylor e a Regra da Cadeia Multivariada | B | publicada |
| `aula10` | 10 — Diferenciação Automática e Grafos de Computação | B | publicada |
| — | 11+ — Gradiente Descendente Estocástico (SGD), ... | — | não iniciadas |

## Fio condutor (o que cada aula deixa para a seguinte)

- **1:** dados como vetores; hipótese da variedade; normas $L_1/L_2/L_\infty$, produto interno, métrica. $d_{\cos}$ **não** é métrica ($\sqrt{2d_{\cos}}$, a distância cordal, é); $k$-NN; fecha com RAG.
- **2:** matriz de design $X\in\mathbb R^{N\times d}$; $X\mathbf w=\mathbf y$ lido por linhas e por colunas; os três tipos de solução; independência e posto; multicolinearidade real. **Ponte:** $N\gg d$ torna o sistema sobredeterminado.
- **3:** melhor aproximação = projeção ortogonal em $\text{col}(X)$; complemento ortogonal; equações normais $X^TX\hat{\mathbf w}=X^T\mathbf y$.
- **4:** autovalores/autovetores, polinômio característico, teorema espectral, definitude, Rayleigh, $\text{cond}(A)$. **Ponte:** uma $X$ retangular pede a SVD.
- **5:** SVD (completa/reduzida/truncada), Eckart-Young-Mirsky, decomposição polar, $\text{cond}(X^TX)=\text{cond}(X)^2$. **Ponte:** falta como achar parâmetros que minimizam uma perda.
- **6:** derivadas parciais, gradiente, derivada direcional, Jacobiano, regra da cadeia com Jacobiano; $\nabla L=\mathbf 0$ dá só um ponto crítico. **Ponte:** mínimo, máximo ou sela? → Hessiana e convexidade.
- **7:** conjuntos e funções convexas, epígrafe, condição de 1ª ordem ($\nabla f(\mathbf{x})=\mathbf{0} \implies$ mínimo global), condição de 2ª ordem ($\nabla^2 f \succeq 0$), Hessiana da perda quadrática $2X^TX$, regularização Ridge $2(X^TX+\lambda I)$ para unicidade estrita. **Ponte:** quando $N, d$ são gigantescos ou não há solução analítica (ex: regressão logística), como encontrar o mínimo numericamente? → descida do gradiente.
- **8:** otimização irrestrita e descida do gradiente; taxa de aprendizado $\alpha$; Lema da Descida ($L$-suavidade, $\alpha < 2/L$); dinâmica espectral de erro $\mathbf{e}_{k+1} = (I - \alpha A)\mathbf{e}_k$; taxa ótima de contração de Chebyshev $\rho^\star = \frac{\kappa-1}{\kappa+1}$; diagnóstico do mau condicionamento do California Housing ($\kappa \approx 23.460{,}5 \to \rho^\star \approx 0{,}99991$); aceleração dramática por padronização $Z$-score ($\kappa \approx 12{,}9 \to \rho^\star \approx 0{,}856$); regressão logística e entropia cruzada binária (perda sem solução fechada com gradiente $\frac{1}{N}X^T(\hat{\mathbf{y}}-\mathbf{y})$ e Hessiana $\frac{1}{N}X^TSX \succ 0$). **Ponte:** modelos compostos e não-lineares (redes neurais) exigem aproximações locais e diferenciação em cadeia $\to$ Séries de Taylor e Regra da Cadeia Multivariada.
- **9:** aproximações multivariadas de Taylor ($T_1, T_2$); restos de Lagrange e cotas $|R_1|\le \frac{L}{2}\|\mathbf{h}\|^2$, $|R_2|\le \frac{M}{6}\|\mathbf{h}\|^3$; Gradient Descent como minimizador proximal de $T_1$; regra da cadeia matricial em *denominator layout* $\nabla_{\mathbf{x}}(g \circ \mathbf{f}) = J_{\mathbf{f}}\nabla_{\mathbf{u}}g$; propagação retrógrada de sensibilidade $\boldsymbol{\delta}^{(l)} = ((W^{(l+1)})^T \boldsymbol{\delta}^{(l+1)})\odot \sigma'(\mathbf{z}^{(l)})$ e gradiente de pesos $\nabla_{W^{(l)}}\mathcal{L} = \boldsymbol{\delta}^{(l)}(\mathbf{a}^{(l-1)})^T$ em MLPs; validação no California Housing. **Ponte:** a derivação manual no papel torna-se intratável para grafos com ramificações e a expansão simbólica sofre de *expression swell* $\to$ Grafos de computação e Diferenciação Automática (modo reverso e Teorema de Baur-Strassen).
- **10:** os quatro paradigmas da diferenciação (manual, numérica, simbólica e automática); instabilidade de diferenças finitas (truncamento vs cancelamento subtrativo); inchaço de expressões simbólicas; formalização de programas como Grafos Acíclicos Direcionados (DAGs); modo forward (tangente/pushforward, $\dot{v}_i$, $O(d_{\text{in}}\cdot C)$); modo reverse (adjunto/pullback, $\bar{v}_i$, $O(d_{\text{out}}\cdot C)$); Teorema de Baur-Strassen ($C_{\text{grad}} \le 5C$); implementação de mini-autograd com ordenação topológica (DFS); footprint de memória e activation checkpointing ($O(L) \to O(\sqrt{L})$); fecha o Bloco 2. **Ponte:** como calcular gradientes quando $N$ é gigantesco (Big Data) e avaliar todas as amostras a cada passo torna-se intratável? $\to$ Bloco 3: Gradiente Descendente Estocástico (SGD) e Mini-Batching (Aula 11).

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
| $T_1(\mathbf{x}_0+\mathbf{h}) = f(\mathbf{x}_0) + \nabla f(\mathbf{x}_0)^T\mathbf{h}$ | polinômio de Taylor de grau 1 (aproximação afim / hiperplano tangente) | 9 (Bloco 1) |
| $T_2(\mathbf{x}_0+\mathbf{h}) = T_1 + \frac{1}{2}\mathbf{h}^T\nabla^2 f(\mathbf{x}_0)\mathbf{h}$ | polinômio de Taylor de grau 2 (aproximação quadrática / paraboloide osculador) | 9 (Bloco 1) |
| $R_1(\mathbf{h}) \le \frac{L}{2}\|\mathbf{h}\|^2, R_2(\mathbf{h}) \le \frac{M}{6}\|\mathbf{h}\|^3$ | cotas assintóticas dos restos de Taylor sob suavidade de Lipschitz | 9 (Bloco 1) |
| $\boldsymbol{\delta}^{(l)} = \nabla_{\mathbf{z}^{(l)}}\mathcal{L}$ | vetor de sensibilidade pré-sináptica da camada $l$ em redes neurais | 9 (Bloco 3) |
| $\boldsymbol{\delta}^{(l)} = ((W^{(l+1)})^T \boldsymbol{\delta}^{(l+1)})\odot \sigma'(\mathbf{z}^{(l)})$ | equação canônica de retropropagação de sensibilidade | 9 (Bloco 3) |
| $\nabla_{W^{(l)}}\mathcal{L} = \boldsymbol{\delta}^{(l)}(\mathbf{a}^{(l-1)})^T$ | gradiente matricial de pesos via produto diádico erro $\times$ ativação | 9 (Bloco 3) |
| $\dot{v}_i = \partial v_i / \partial x_k$ | variável tangente no modo forward de diferenciação automática | 10 (Bloco 2) |
| $\bar{v}_i = \partial \mathcal{L} / \partial v_i$ | variável adjunta no modo reverse de diferenciação automática | 10 (Bloco 2) |
| $C_{\text{grad}} \le 5 \cdot C_{\text{eval}}$ | Teorema de Baur-Strassen / Speelpenning de complexidade temporal | 10 (Bloco 2) |
| $\mathcal{O}(\sqrt{L})$ | footprint de memória via recomputação com *activation checkpointing* | 10 (Bloco 4) |

## Pendências

- **Aula 2:** o Bloco 1 apresenta a definição formal de matriz antes do exemplo concreto dos bairros. Inverter a ordem só com aprovação.
- **Aula 1:** o produto interno é usado no Bloco 5 sem ter sido definido formalmente no Bloco 4 (MathML §3.2.2 ainda não citado).
- **Quantidade de testes:** Aulas 2–3 têm 12 testes (a regra é 6–10).
- **Nomes legados:** `_03-respostas-pausas.md` (Aula 3) e `_00-planejamento.md`/`_01-respostas.md` (Aulas 4–6). As Aulas 1–2 não têm arquivo de respostas das pausas.

