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
| `aula07` | 7 — Regularização e MAP bayesiano | B | California Housing | publicada no index; não commitada |
| — | 8 — Viés-variância (teórico) | — | — | não iniciada |

## Fio condutor (o que cada aula deixa para a seguinte)

- **1:** classificar = comparar densidades ponderadas pela priori. Limiar $T_{CONJ}$ no cruzamento das conjuntas, erros Tipo I/II como áreas, custo assimétrico, ROC, rejeição. **Ponte:** em $d$ dimensões, $p(\mathbf{x}\mid\mathcal C_k)$ não é estimável sem estrutura.
- **2:** Naive Bayes (independência condicional) e teoria da decisão geral (perda $L$, risco posterior, risco de Bayes). Com $\Sigma$ compartilhada, o log-razão é linear. **Ponte:** os modelos até aqui fixam a forma da fronteira antes de ver os dados.
- **3:** CART como MLE não paramétrico (folha gaussiana → soma de quadrados; folha categórica → entropia). Teoria da informação ($H$, $I(X;Y)$, ganho de informação = informação mútua). Poda por custo-complexidade. **Ponte:** $\lambda$ foi escolhido "olhando o gráfico".
- **4:** $\hat R(\theta)$ é um estimador otimista de $R(\theta)$. CV como simulação de amostragem, a escolha de $k$ (viés × variância do estimador), regra de 1 desvio-padrão, Bootstrap (reamostrar o teste × reamostrar e reajustar), vazamento de dados. **Ponte:** viés-variância formal na Aula 8; regressão linear na Aula 5.
- **Revisão 1:** as Aulas 1–4 como instâncias de distribuição → verossimilhança → decisão/risco. Alerta de colisão: $k$ (classe × *fold*); $\lambda$ (custo assimétrico × custo-complexidade).
- **5:** OLS geométrico (RSS, equações normais, projeção em $\mathcal S=\mathrm{span}(\varphi_1,\varphi_2)$) = MLE sob ruído gaussiano homocedástico. Viés de $\hat\sigma^2_{\text{MLE}}$. Limitações: heterocedasticidade, censura de `MedHouseVal` em $5{,}00001$. **Ponte:** trocar a Gaussiana por Bernoulli.
- **6:** logit/sigmoide, entropia cruzada = $-\ln L$, gradiente $X^T(\boldsymbol\mu-\mathbf y)$, Hessiana $X^TRX$ (convexa), IRLS, GLM e ligação canônica. **Ponte:** a separação perfeita faz $\lVert\mathbf w\rVert\to\infty$, o que motiva a regularização.
- **7:** Ridge (forma fechada $(X^TX+\lambda I)^{-1}X^T\mathbf y$), Lasso e soft-thresholding, MAP (priori gaussiana → Ridge com $\lambda=\sigma^2/\tau^2$; Laplace → Lasso com $\lambda=\sigma^2/b$). **Ponte:** como escolher $\lambda$ → decomposição viés-variância (Aula 8).

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

## Pendências

- **Numeração pós-Revisão 1:** a Ponte da `aula05` ainda anuncia a regressão logística como "Aula 7" (hoje é a Aula 6).
- **`aula07`:** no link de Soluções, a classe está como `.soluções-link`, mas a correta é `.solucoes-link` (sem ela, o link fica sem ícone).
- **`aula04`:** a seção "Resumo — Aula 4" / "Conteúdo da Aula" adicionada ao `index.qmd` está sem commit, e há um link de Exercícios no topo que duplica o do Fechamento.
- **Quantidade de testes:** Aulas 2–4 e Revisão 1 têm 12 testes (a regra é 6–10). Revisar só se o usuário pedir.
- **Nomes legados:** `_03-respostas-pausas.md` (Aulas 1, 2, 4 e Revisão 1) e `_00-planejamento.md`/`_01-respostas.md` (Aula 5).
