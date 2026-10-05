# Progresso — Optimization and Linear Algebra for Machine Learning

Estado aprovado + notações, para dar continuidade entre aulas. O histórico de correções está no git (a versão longa anterior deste arquivo foi até o commit `1d4a4fc`).

**Fontes** (`_fontes/`, symlinks; deslocamento página impressa → PDF): `mathml.pdf` (Deisenroth et al.) +6; `copt.pdf` (Boyd & Vandenberghe) +14; `optml.pdf` (Wright & Recht) ainda sem uso nem deslocamento conferido.
**Problema-fio desde a Aula 2:** regressão linear múltipla no California Housing (escalas heterogêneas, multicolinearidade `AveRooms`/`AveBedrms`).
**Código compartilhado:** `src/metrics.py` (`compute_norm`, `inner_product`).
**Convenções:** gradiente como vetor-**linha** e Jacobiano *numerator layout* (MathML). A transferência de domínio nos V/F fica sempre dentro de ML: uma varredura em 2026-09-14 trocou 12 itens de física/engenharia.

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
| — | 8+ — Descida do gradiente, ... | — | não iniciadas |

## Fio condutor (o que cada aula deixa para a seguinte)

- **1:** dados como vetores; hipótese da variedade; normas $L_1/L_2/L_\infty$, produto interno, métrica. $d_{\cos}$ **não** é métrica ($\sqrt{2d_{\cos}}$, a distância cordal, é); $k$-NN; fecha com RAG.
- **2:** matriz de design $X\in\mathbb R^{N\times d}$; $X\mathbf w=\mathbf y$ lido por linhas e por colunas; os três tipos de solução; independência e posto; multicolinearidade real. **Ponte:** $N\gg d$ torna o sistema sobredeterminado.
- **3:** melhor aproximação = projeção ortogonal em $\text{col}(X)$; complemento ortogonal; equações normais $X^TX\hat{\mathbf w}=X^T\mathbf y$.
- **4:** autovalores/autovetores, polinômio característico, teorema espectral, definitude, Rayleigh, $\text{cond}(A)$. **Ponte:** uma $X$ retangular pede a SVD.
- **5:** SVD (completa/reduzida/truncada), Eckart-Young-Mirsky, decomposição polar, $\text{cond}(X^TX)=\text{cond}(X)^2$. **Ponte:** falta como achar parâmetros que minimizam uma perda.
- **6:** derivadas parciais, gradiente, derivada direcional, Jacobiano, regra da cadeia com Jacobiano; $\nabla L=\mathbf 0$ dá só um ponto crítico. **Ponte:** mínimo, máximo ou sela? → Hessiana e convexidade.

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
| $\nabla f$, $\nabla_{\mathbf{x}}f$, $df/d\mathbf{x}$ | gradiente de $f$ (vetor-**linha**, convenção MathML) | 6 (Bloco 3) |
| $D_{\mathbf{v}}f(\mathbf{x})$ | derivada direcional de $f$ em $\mathbf{x}$, na direção unitária $\mathbf{v}$ | 6 (Bloco 4) |
| $J$, $J_f(\mathbf{x})$ | Jacobiano de $f:\mathbb{R}^n\to\mathbb{R}^m$ (matriz $m\times n$, *numerator layout*; gradiente = caso $m=1$) | 6 (Bloco 5) |
| $\mathbf{r}(\boldsymbol{\beta})=X\boldsymbol{\beta}-\mathbf{y}$ | resíduo como função vetorial de $\boldsymbol{\beta}$; $J_{\mathbf{r}}(\boldsymbol{\beta})=X$ | 6 (Bloco 5) |
| regra da cadeia com Jacobiano | $\nabla_{\boldsymbol{\beta}}(g\circ\mathbf{r})=\nabla_{\mathbf{r}}g\cdot J_{\mathbf{r}}(\boldsymbol{\beta})$ | 6 (Bloco 5) |
| ponto crítico | ponto onde $\nabla f=\mathbf{0}$ — não garante mínimo/máximo sem informação adicional | 6 (Fechamento) |

## Pendências

- **Aula 7:** alinhar ao esqueleto do `CLAUDE.md` (Revisão/Intuição/Blocos/Fechamento, Pausas Ativas) e gerar exercícios e soluções antes de publicar. O plano indica 70 min de carga horária; confirmar.
- **Aula 2:** o Bloco 1 apresenta a definição formal de matriz antes do exemplo concreto dos bairros. Inverter a ordem só com aprovação.
- **Aula 1:** o produto interno é usado no Bloco 5 sem ter sido definido formalmente no Bloco 4 (MathML §3.2.2 ainda não citado).
- **Quantidade de testes:** Aulas 2–3 têm 12 testes (a regra é 6–10).
- **Nomes legados:** `_03-respostas-pausas.md` (Aula 3) e `_00-planejamento.md`/`_01-respostas.md` (Aulas 4–6). As Aulas 1–2 não têm arquivo de respostas das pausas.
