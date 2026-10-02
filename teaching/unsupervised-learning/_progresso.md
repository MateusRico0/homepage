# Progresso — Unsupervised Learning

Estado aprovado + notações, para dar continuidade entre aulas. O histórico de correções está no git (a versão longa anterior deste arquivo foi até o commit `1d4a4fc`).

**Fontes** (`_fontes/`, symlinks; deslocamento página impressa → PDF): PRML +20, DLFC +11, ESL (usado pontualmente, p. ex. a p. 507 na Aula 3).
**Dataset-fio desde a Aula 2:** Breast Cancer Wisconsin sem o rótulo (`diagnosis` só aparece para conferir o resultado). O par 2D `radius_worst` × `concave points_worst` (padronizado) é o mesmo nas Aulas 3–5; a Aula 6 usa os 30 atributos. Duas luas sintéticas servem de contraexemplo de forma não convexa.

## Estado das aulas

| Pasta | Aula | Estratégia | Dataset-fio | Estado |
|---|---|---|---|---|
| `aula01` | 1 — Modelos generativos paramétricos e anomalias | — | sintético (dois sensores: temperatura × vibração) | publicada |
| `aula02` | 2 — k-NN, maldição da dimensionalidade e KDE | B | Breast Cancer | publicada |
| `aula03` | 3 — Topografia de densidade: hierárquico e HDBSCAN | A | Breast Cancer 2D + duas luas | publicada |
| `aula04` | 4 — GMM e o algoritmo EM | A | Breast Cancer 2D | publicada |
| `aula05` | 5 — Modelos variacionais, GMM bayesiano e seleção de modelos | A | Breast Cancer 2D + duas luas | publicada |
| `aula06` | 6 — PCA, PPCA e autoencoders lineares | B | Breast Cancer (30 atributos) | publicada |
| — | 7 — Autoencoders não lineares e VAE | — | — | não iniciada |

## Fio condutor (o que cada aula deixa para a seguinte)

- **1:** Gaussiana multivariada por MLE; anomalia via $D_M^2\sim\chi^2_d$. Ressalva: $\hat\Sigma$ só é invertível com $N>d$. **Ponte:** abandonar a forma paramétrica.
- **2:** maldição da dimensionalidade e concentração de medida; $p(\mathbf x)=K/(NV)$ → $k$-NN (fixa $K$) e KDE (fixa $V$). **Ponte:** $d_K(\mathbf x)$ vira peso de aresta num grafo.
- **3:** cluster = componente conexa de $L_\lambda$; $d_{\mathrm{mreach}}$, MST com a hierarquia inteira, HDBSCAN e persistência. Trio de paradigmas (ESL p. 507): combinatório, *mode seeking* e mistura. **Ponte:** a partição rígida força uma escolha em populações sobrepostas.
- **4:** GMM com latente categórica $z$, responsabilidades, EM (E/M), K-Means como caso-limite. **Ponte:** a verossimilhança de treino sempre prefere $K$ maior; sem priori em $\theta$, não há como penalizar a complexidade.
- **5:** seleção bayesiana de modelos (evidência = Occam), KL e decomposição da evidência, GMM bayesiano completo (Normal-Wishart + Dirichlet, $\alpha_0$ fixo), ELBO dissecado, ELPD e *double-dipping*, Silhueta + Dunn (inclusive DBSCAN via $k$-NN) e PPC quantitativo (KS em projeções, MMD). **Ponte:** a latente foi sempre categórica; a Aula 6 passa a uma latente contínua.
- **6:** latente contínua. Ordem: Problema-Fio 2D (guardar um número, reconstruir dois) → autoencoder linear (código latente = coordenadas num plano; invariância por $\mathbf{G}$: os dados fixam o plano, não os eixos) → Mecanismo I (erro mínimo, com pesos amarrados e base ortonormal; erro $=\mathrm{tr}\,\mathbf{S}-$ variância retida) → Mecanismo II (máxima variância, Lagrange, indução) → prova por redução do teorema do autoencoder → PPCA como Gaussiana de posto reduzido ($\sigma^2\to0$ recupera a PCA). Resultados: $\lambda_1$ explica 44,27%; um limiar no PC1 dá 92,1% sem rótulo. **Ponte:** *deep autoencoder* e VAE; a posterior perde a forma fechada, e o ELBO da Aula 5 volta com o *reparameterization trick*.

## Dicionário de notações

| Símbolo/termo | Significado | Introduzido em |
|---|---|---|
| $\hat{\boldsymbol\mu}$, $\hat\Sigma$ | Média e covariância amostrais (estimadores de máxima verossimilhança) | 1 |
| $D_M(\mathbf{x})^2$ | Distância de Mahalanobis ao quadrado, $(\mathbf{x}-\hat{\boldsymbol\mu})^T\hat\Sigma^{-1}(\mathbf{x}-\hat{\boldsymbol\mu})$ | 1 |
| $\chi^2_d$ | Distribuição de $D_M(\mathbf{x})^2$ sob o modelo ajustado; base do $p$-valor de anomalia | 1 |
| $d_K(\mathbf{x})$ | Distância ao $K$-ésimo vizinho mais próximo | 2 |
| $p(\mathbf{x})=K/(NV)$ | Estimador geral de densidade (fixa $K$ e acha $V$, ou vice-versa) — dá origem a $k$-NN e KDE | 2 |
| $h$ | Parâmetro de suavização (largura de banda) do KDE | 2 |
| $L_\lambda=\{\mathbf{x}:p(\mathbf{x})\ge\lambda\}$ | Conjunto de nível de densidade; cluster = componente conexa de $L_\lambda$ | 3 |
| $d_{\mathrm{mreach}}(a,b)$ | Distância de alcançabilidade mútua, $\max(\mathrm{core}_K(a),\mathrm{core}_K(b),d(a,b))$ | 3 |
| MST, persistência | Árvore Geradora Mínima; critério de robustez de um cluster na árvore condensada (HDBSCAN) | 3 |
| $z_n$, $\pi_k$ | Variável latente categórica 1-de-$K$ (origem do ponto $n$); prior de mistura, $\sum_k\pi_k=1$ | 4 |
| $\gamma(z_{nk})$ | Responsabilidade — $p(z_{nk}=1\mid\mathbf{x}_n,\theta)$, posterior via Bayes | 4 |
| Passo E / Passo M | As duas etapas alternadas do Algoritmo EM | 4 |
| $\mathbf{H}$ | Variável não observada genérica na decomposição do ELBO ($\mathbf{Z}$, $\theta$ ou ambos). Não usar $\mathbf{Z}$ genérico nem $\mathbf{W}$, que colidem com a Aula 6 | 5 |
| $\mathrm{KL}(q\|p)$ | Divergência de Kullback-Leibler, $-\int q\ln\{p/q\}$; $\ge0$, não simétrica | 5 |
| $\mathcal{L}(q)$, $\mathcal{L}(q,\theta)$ | ELBO (*Evidence Lower Bound*) — cota inferior de $\ln p(\mathbf{X})$ (ou $\ln p(\mathbf{X}\mid\theta)$), igual à evidência sse $q$ = posterior exata | 5 |
| Decomposição $\ln p(\mathbf{X})=\mathcal{L}(q)+\mathrm{KL}(q\|p(\mathbf{H}\mid\mathbf{X}))$ | Identidade central da Aula 5, para qualquer $\mathbf{H}$ e $q(\mathbf{H})$ normalizada | 5 |
| $q(\mathbf{Z},\theta)\approx q(\mathbf{Z})q(\theta)$ | Aproximação de campo médio (*mean field*) — fatoração usada para tornar o ELBO com $\theta$ dentro do tratamento variacional tratável | 5 |
| $\alpha_0$ | Parâmetro de concentração da priori de Dirichlet sobre os pesos de mistura $\pi$ num GMM Bayesiano — mantido fixo e neutro na Aula 5; quem escolhe $K$ é a comparação de ELBOs, não a variação de $\alpha_0$ | 5 |
| Inferência Bayesiana Variacional (*Variational Bayes*) | Procedimento que otimiza $q(\mathbf{Z})$ **e** $q(\theta)$ (com $\theta$ tendo uma priori $p(\theta)$) — diferente do EM clássico, que trata $\theta$ como ponto fixo, sem prior | 5 |
| $s(i)$ | Coeficiente de Silhueta de um ponto (Rousseeuw, 1987): $\frac{b(i)-a(i)}{\max\{a(i),b(i)\}}\in[-1,1]$, maior é melhor | 5 |
| PPC (*Posterior Predictive Check*) | Amostrar $\theta$ aprendido, gerar $\mathbf{X}_{\text{sim}}$ do modelo generativo, comparar contra $\mathbf{X}_{\text{real}}$ — único teste desta aula que compara **forma**, não só um número agregado (Gelman & Rubin, 1996) | 5 |
| $\mathbf{S}$ | Matriz de covariância amostral, $\frac1N\sum_n(\mathbf{x}_n-\bar{\mathbf{x}})(\mathbf{x}_n-\bar{\mathbf{x}})^T$ — simétrica e semidefinida positiva | 6 |
| $\mathbf{u}_i$, subespaço principal | Autovetores de $\mathbf{S}$ associados aos $M$ maiores autovalores; direções/base da PCA | 6 |
| $J$ | Distorção média de reconstrução da PCA, $\frac1N\sum_n\|\mathbf{x}_n-\tilde{\mathbf{x}}_n\|^2$ (mesma letra do $J$ de distorção do KMeans, Aula 4 — família de significado análoga, não coincidência de símbolo) | 6 |
| $\mathbf{z}\in\mathbb{R}^M$ | **Atenção — reuso de símbolo:** variável latente **contínua** da PPCA (Gaussiana, $\mathcal{N}(\mathbf{0},\mathbf{I})$); não confundir com $z_n$/$z_{nk}$ da Aula 4, que é a variável latente **categórica** (1-de-$K$) do GMM, nem com o $\mathbf{H}$ genérico da Aula 5 | 6 |
| $\mathbf{W}$, $\sigma^2$ | Parâmetros da PPCA: matriz de carregamento ($D\times M$) e variância do ruído isotrópico — **não confundir** com o $\mathbf{H}$ genérico da Aula 5 (renomeado de propósito para não colidir com este $\mathbf{W}$) | 6 |
| $\mathbf{C}=\mathbf{WW}^T+\sigma^2\mathbf{I}$ | Covariância marginal de $\mathbf{x}$ no modelo PPCA | 6 |
| $M$ (dimensão latente/subespaço) | Dimensão do subespaço/variável latente contínua da PPCA | 6 |
| $\mathcal{M}_m$ | Estrutura/modelo candidato (ex.: "GMM com $K=m$"), tratado como variável na seleção Bayesiana de modelos | 5 |
| $p(\mathbf{X}\mid\mathcal{M}_m)$ (evidência) | Verossimilhança marginal de $\mathcal{M}_m$, $\int p(\mathbf{X},\mathbf{H}\mid\mathcal{M}_m)\,\mathrm{d}\mathbf{H}$ — já embute Navalha de Occam antes de qualquer aproximação | 5 |
| $\mathcal{L}_m(q)$ | ELBO da estrutura $\mathcal{M}_m$ — cota inferior tratável para a evidência, usada como *proxy* de ranqueamento | 5 |
| $N_k$ | Contagem esperada de pontos no componente $k$ sob $q(\mathbf{Z})$, $\sum_n\gamma(z_{nk})$ — real, não necessariamente inteira | 5 |
| Normal-Wishart, $\Lambda_k=\Sigma_k^{-1}$, $(m_0,\beta_0,W_0,\nu_0)$ | Priori conjugada sobre $(\mu_k,\Sigma_k)$ no GMM Bayesiano — impede analiticamente o colapso $\Sigma_k\to\mathbf{0}$, via $W_k^{-1}\succeq W_0^{-1}\succ0$ | 5 |
| CAVI (*Coordinate Ascent Variational Inference*) | Resultado geral que otimiza um fator de $q$ por vez, $\ln q_j^\star=\mathbb{E}_{i\ne j}[\ln p(\mathbf{X},\mathbf{H})]+\text{const}$ (citado de PRML §10.1.1, não rederivado) | 5 |
| ELPD (*Expected Log Predictive Density*) | $\mathbb{E}_{\mathbf{x}\sim p_{\text{true}}}[\ln p(\mathbf{x}\mid\mathbf{X}_{\text{train}})]$ — alvo estatístico verdadeiro da validação preditiva | 5 |
| *Double-dipping* / viés de otimismo | Viés de estimar o ELPD usando os próprios dados de treino — reutilizar pontos de ajuste na avaliação | 5 |
| Índice de Dunn | $\min$ distância inter-cluster / $\max$ diâmetro intra-cluster (Dunn, 1974) — geométrico, livre de distribuição, sensível a extremos | 5 |
| PPC quantitativo, MMD, teste *sliced* | Checagem preditiva a posteriori com números: projeções aleatórias + KS (Massey, 1951) e *Maximum Mean Discrepancy* com kernel RBF (Gretton et al., 2012) | 5 |

## Pendências

- **Aula 2:** uma nota antiga diz que restaram citações de PRML/ESL em inglês sem tradução. Conferir.
- **Aula 1:** falta o par DLFC para as fontes (só PRML).
- **Quantidade de testes:** Aulas 1–3 têm 12 testes (a regra é 6–10).
- **Nomes legados:** `_03-respostas-pausas.md` (Aulas 2 e 3) e `_00-planejamento.md`/`_01-respostas.md` (Aulas 4–6).
