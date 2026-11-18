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
| `aula07` | 7 — Autoencoders profundos e VAE | A | Breast Cancer + MNIST | publicada |
| `aula08` | 8 — Redução para visualização: MDS e t-SNE | A | Breast Cancer + MNIST | publicada |
| `aula09` | 9 — Redes Bayesianas e Modelos Gráficos Probabilísticos (PGMs) para Mineração de Itens Frequentes | A | Cestas de compras sintético controlado + Adult Census | publicada |
| `aula10` | 10 — Sistemas de Recomendação: Fatoração de Matrizes (SVD e NMF) | A | MovieLens (núcleo 2000×1000) + MNIST | publicada |
| `aula11` | 11 — Detecção de drift e alinhamento de distribuições: teste de duas amostras e MMD | A | Gas Sensor Array Drift (UCI) + sintéticos 2D + duas luas | pronta, aguardando publicação |

## Fio condutor (o que cada aula deixa para a seguinte)

- **1:** Gaussiana multivariada por MLE; anomalia via $D_M^2\sim\chi^2_d$. Ressalva: $\hat\Sigma$ só é invertível com $N>d$. **Ponte:** abandonar a forma paramétrica.
- **2:** maldição da dimensionalidade e concentração de medida; $p(\mathbf x)=K/(NV)$ → $k$-NN (fixa $K$) e KDE (fixa $V$). **Ponte:** $d_K(\mathbf x)$ vira peso de aresta num grafo.
- **3:** cluster = componente conexa de $L_\lambda$; $d_{\mathrm{mreach}}$, MST com a hierarquia inteira, HDBSCAN e persistência. Trio de paradigmas (ESL p. 507): combinatório, *mode seeking* e mistura. **Ponte:** a partição rígida força uma escolha em populações sobrepostas.
- **4:** GMM com latente categórica $z$, responsabilidades, EM (E/M), K-Means como caso-limite. **Ponte:** a verossimilhança de treino sempre prefere $K$ maior; sem priori em $\theta$, não há como penalizar a complexidade.
- **5:** seleção bayesiana de modelos (evidência = Occam), KL e decomposição da evidência, GMM bayesiano completo (Normal-Wishart + Dirichlet, $\alpha_0$ fixo), ELBO dissecado, ELPD e *double-dipping*, Silhueta + Dunn (inclusive DBSCAN via $k$-NN) e PPC quantitativo (KS em projeções, MMD). **Ponte:** a latente foi sempre categórica; a Aula 6 passa a uma latente contínua.
- **6:** latente contínua. Ordem: Problema-Fio 2D (guardar um número, reconstruir dois) → autoencoder linear (código latente = coordenadas num plano; invariância por $\mathbf{G}$: os dados fixam o plano, não os eixos) → Mecanismo I (erro mínimo, com pesos amarrados e base ortonormal; erro $=\mathrm{tr}\,\mathbf{S}-$ variância retida) → Mecanismo II (máxima variância, Lagrange, indução) → prova por redução do teorema do autoencoder → PPCA como Gaussiana de posto reduzido ($\sigma^2\to0$ recupera a PCA). Resultados: $\lambda_1$ explica 44,27%; um limiar no PC1 dá 92,1% sem rótulo. **Ponte:** *deep autoencoder* e VAE; a posterior perde a forma fechada, e o ELBO da Aula 5 volta com o *reparameterization trick*.
- **7:** *Deep autoencoder* e VAE. Proposição (nossa): decoder afim $\Rightarrow$ reconstruções num subespaço afim de dim. $\le M$ (explica DLFC p. 565: AE raso = PCA); profundo curva (arco 2D), ganha no MNIST, sobreajusta no Breast Cancer (treino $\div3$, teste pior). Gap generativo (invariância por reparametrização do latente). VAE = PPCA com $\mathbf{g}(\mathbf{z},\mathbf{w})$; posterior intratável $\to$ inferência amortizada; $\mathcal{L}_n=\mathbb{E}_q[\ln p(\mathbf{x}_n\mid\mathbf{z})]-\mathrm{KL}(q\|p(\mathbf{z}))$ derivado da Aula 5, KL Gaussiana fechada, minimizadores dependem de $\beta\sigma^2$; folga ELBO medida por amostragem por importância; reparametrização vs. *score function* (variância medida). **Ponte:** mapas 2D do AE/VAE são subprodutos da reconstrução; para visualizar, otimizar posições diretamente (MDS, t-SNE) $\to$ *crowding problem*.
- **8:** Redução para visualização. Geometria de hiperesferas e o *crowding problem* ($r^D$ vs $r^2$). MDS métrico e o viés do *Stress* em favor de distâncias longas. SNE probabilístico, busca binária de $\sigma_i$ via Perplexidade $2^{H(P_i)}$ e assimetria da divergência KL ($p_{ij} \parallel q_{ij}$). t-SNE: quebra de simetria de famílias de densidade adotando a cauda pesada de Student-$t$ ($\nu=1$ / Cauchy) no mapa 2D, aliviando a pressão de volume. Dinâmica de forças (mola atrativa e repulsão eletrostática). As 4 armadilhas de interpretação: distâncias inter-cluster espúrias, áreas sem relação com densidade/variância original, alucinação em ruído e ausência de projeção paramétrica. **Ponte:** encerramento da Parte 2 (espaço latente); início da Parte 3 com Modelos Gráficos Probabilísticos (PGMs) e mineração de itens frequentes (Aula 9).
- **9:** Início da Parte 3 (dados categóricos/esparsos). Ruptura epistemológica em relação ao espaço contínuo métrico $\mathbb{R}^D$ (onde distâncias perdem o sentido físico). Mineração de itens frequentes e regras de associação: Suporte $s(I)$, Confiança $c(A \Rightarrow B)$ e *Lift*. Antimonotonicidade do suporte ($A \subseteq B \implies s(B) \le s(A)$) e mecânica completa do algoritmo Apriori (geração $L_{k-1} \bowtie L_{k-1}$, poda em RAM por subconjuntos infrequentes e mineração prática de regras de mercado). Limitações do *Lift*: comutatividade estrita ($\text{Lift}(A \Rightarrow B) \equiv \text{Lift}(B \Rightarrow A)$) e vulnerabilidade ao Paradoxo de Simpson por causas comuns latentes. Redes Bayesianas (DAGs) e fatoração conjunta $p(\mathbf{x}) = \prod_k p(x_k \mid \text{pa}_k)$ como filtro de regras. As 3 estruturas canônicas: cadeia ($A \to B \to C$) para poda de transitividade e causa comum ($A \leftarrow B \to C$) para descarte de espúrios (ambas bloqueadas dado $B$); colisor ($A \to C \leftarrow B$) aberto por condicionamento (*explaining away*) alertando contra viés de seleção. Construção do grafo por montagem de componentes locais (esqueleto via Apriori $\to$ testes locais de independência $\to$ colisores unívocos gerando o CPDAG). Limite observacional: classes de equivalência de Markov (I-equivalência: mesmo esqueleto e v-structures) e impossibilidade de inferir causalidade estrita sem intervenção experimental ($do(x)$, teste A/B). **Ponte:** de grafos discretos para recomendação em matrizes esparsas massivas via SVD e NMF (Aula 10).
- **10:** Matrizes esparsas massivas ($>99\%$ ausente) e filtragem colaborativa; colapso da SVD clássica e patologia da imputação de zeros/médias; formulação de fatores latentes regularizados do *Netflix Prize* (Funk-SVD, Koren et al., 2009) restrita aos dados observados $\Omega$; preditores de linha de base (vieses $\mu + b_u + b_i$); otimização biconvexa: SGD por amostra ($\mathcal{O}(|\Omega|K)$) e Mínimos Quadrados Alternados (ALS) com solução analítica por usuário ($\sum \mathbf{q}_i \mathbf{q}_i^T + \lambda I)^{-1}$; transição para Fatoração de Matrizes Não-Negativa (NMF, Lee & Seung 1999; ESL §14.6); colapso semântico da PCA/SVD (cancelamentos subtrativos holísticos) vs. princípio aditivo da NMF ($W \ge 0, H \ge 0$, representação por partes); funções de custo: Frobenius (gaussiano) e Divergência KL generalizada (modelo de Poisson); dedução das Regras Multiplicativas de Atualização de Lee & Seung (2001); dilema da não-unicidade e cones geradores (Donoho & Stodden, 2004); encerra a Parte 3. Em dados reais: média 0,98, SVD com zeros 2,42, vieses 0,77, ALS 0,73, Funk-SVD 0,73; NMF dá partes só com zeros reais no ajuste (feedback implícito, MNIST). Leitura do espaço latente (eixo é hipótese, direção é semelhança, norma é sinal, usuário novo é uma etapa do ALS) e suposições (posto baixo, bilinear, MNAR, estabilidade). **Ponte:** como monitorar se as matrizes e distribuições em produção continuam alinhadas ou se sofreram mutações estocásticas não supervisionadas? $\to$ **Aula 11: Alinhamento de Distribuições e Detecção de Domain Shift (Data Drift)** via Maximum Mean Discrepancy (MMD).
- **11:** Detecção de *drift* sem rótulos como teste de duas amostras ($H_0: P=Q$); teste de permutação com nível $\alpha$ garantido para qualquer estatística; MMD como supremo de diferenças de médias, igual a $\|\boldsymbol\mu_P-\boldsymbol\mu_Q\|_{\mathcal{H}}$ e a $\mathbb{E}k(\mathbf{x},\mathbf{x}')-2\mathbb{E}k(\mathbf{x},\mathbf{y})+\mathbb{E}k(\mathbf{y},\mathbf{y}')$; testemunha como diferença de dois KDEs; estimador não viesado, heurística da mediana, queda do poder com a dimensão; tipos de mudança e alinhamento por padronização do lote. Dataset fora do HF: o setup baixa o `.zip` da UCI para `~/.cache/mc847/`. Aula dimensionada para 60 min (4 blocos). **Ponte:** o kernel fixa o espaço de atributos; o teste por classificador aprende a função a partir da tarefa de distinguir as amostras $\to$ **Aula 12: aprendizado contrastivo e InfoNCE**.

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
| $\mathbf{f}(\cdot,\boldsymbol\phi)$, $\mathbf{g}(\cdot,\mathbf{w})$ | Encoder ($\mathbb{R}^D\to\mathbb{R}^M$) e decoder ($\mathbb{R}^M\to\mathbb{R}^D$) do autoencoder; $\boldsymbol\phi$ e $\mathbf{w}$ separados como no DLFC | 7 |
| $q(\mathbf{z}\mid\mathbf{x},\boldsymbol\phi)$ | Encoder do VAE: Gaussiana diagonal $\prod_j\mathcal{N}(\mu_j(\mathbf{x}),\sigma_j^2(\mathbf{x}))$, posterior aproximada amortizada | 7 |
| $\sigma^2$ vs. $\sigma_{nj}$ | **Atenção:** $\sigma^2$ sem índice = variância do ruído do decoder (como na PPCA); $\sigma_{nj}$ = desvio-padrão do encoder (ponto $n$, coordenada $j$) | 7 |
| $\mathcal{L}_n(\mathbf{w},\boldsymbol\phi)$ | ELBO por ponto do VAE, $\mathbb{E}_q[\ln p(\mathbf{x}_n\mid\mathbf{z},\mathbf{w})]-\mathrm{KL}(q\|p(\mathbf{z}))$ (DLFC 19.14) | 7 |
| $\beta$ | Peso do termo KL ($\beta$-VAE); só o produto $\beta\sigma^2$ afeta os minimizadores | 7 |
| $\boldsymbol\epsilon$, reparametrização | $\mathbf{z}=\boldsymbol\mu+\boldsymbol\sigma\odot\boldsymbol\epsilon$, $\boldsymbol\epsilon\sim\mathcal{N}(\mathbf{0},\mathbf{I})$; contraste: estimador *score function* $f\,\nabla_{\boldsymbol\phi}\ln q$ | 7 |
| $\sigma_M(\mathbf{Y})$, *Stress* | Função de perda do MDS (discrepância quadrática entre distâncias originais e no mapa) | 8 |
| $p_{j|i}$, $p_{ij}$ | Probabilidade de vizinhança na alta dimensão (condicional via kernel gaussiano com $\sigma_i$ local / conjunta simetrizada) | 8 |
| $\text{Perp}(P_i) = 2^{H(P_i)}$ | Perplexidade da distribuição condicional $P_i$ (número efetivo de vizinhos por ponto) | 8 |
| $q_{ij}$ | Probabilidade conjunta no mapa 2D do t-SNE (kernel Student-$t$ com 1 grau de liberdade / Cauchy) | 8 |
| *Crowding problem* | Confinamento e colapso de pontos no centro de mapas 2D devido ao gargalo volumétrico entre $r^D$ e $r^2$ | 8 |
| $s(I)$ | Suporte do itemset $I$: frequência conjunta empírica $P(\bigwedge_{j \in I} x_j = 1)$ | 9 |
| $c(A \Rightarrow B)$ | Confiança da regra de associação: probabilidade condicional empírica $P(B \mid A)$ | 9 |
| $\text{Lift}(A \Rightarrow B)$ | Razão de associação $\frac{P(A \cap B)}{P(A)P(B)}$; métrica estritamente simétrica e comutativa | 9 |
| $\text{pa}_k$ | Conjunto de nós pais da variável $x_k$ em um Grafo Acíclico Direcionado (DAG) | 9 |
| Fatoração DAG: $\prod_k p(x_k \mid \text{pa}_k)$ | Fatoração da probabilidade conjunta sob uma Rede Bayesiana direcionada (PRML §8.1) | 9 |
| $A \perp\!\!\!\perp B \mid C$ | Independência condicional: $p(A, B \mid C) = p(A \mid C)p(B \mid C)$ | 9 |
| Cadeia, Causa Comum, Colisor | As 3 geometrias canônicas: cadeia e causa comum são bloqueadas pelo intermediário; colisor é aberto | 9 |
| *Explaining away* | Fenômeno no colisor ($A \to C \leftarrow B$) onde condicionar no efeito comum $C$ induz dependência negativa entre as causas | 9 |
| $d$-separação | Critério gráfico geral de bloqueio de caminhos em DAGs (Pearl, 1988; PRML §8.2.2) | 9 |
| $\text{MB}(X_i)$ | Cobertura de Markov (*Markov Blanket*): $\text{pa} \cup \text{ch} \cup \text{co-pais}$, menor conjunto que isola $X_i$ do restante | 9 |
| I-equivalência, CPDAG | Classes de equivalência de Markov (mesmo esqueleto e v-structures) e grafo misto essencial | 9 |
| $R \in \mathbb{R}^{M \times N}$, $\Omega$ | Matriz de interações usuário-item e conjunto de pares $(u, i)$ com avaliações observadas | 10 |
| $\mathbf{p}_u, \mathbf{q}_i \in \mathbb{R}^K$ | Vetores latentes de preferências do usuário e atributos do item | 10 |
| $\hat{r}_{ui} = \mu + b_u + b_i + \mathbf{p}_u^T \mathbf{q}_i$ | Preditor de linha de base com interação residual bilinear (Funk-SVD / Koren et al., 2009) | 10 |
| ALS (*Alternating Least Squares*) | Otimização biconvexa alternada resolvendo sistemas lineares de Ridge desacoplados | 10 |
| $V \approx W H$ ($W \ge 0, H \ge 0$) | Fatoração de Matrizes Não-Negativa (NMF, Lee & Seung 1999; ESL §14.6) | 10 |
| Representação por partes | Decomposição puramente aditiva sem cancelamentos subtrativos decorrente da não-negatividade | 10 |
| $\mathcal{D}_{KL}(V \parallel WH)$ | Divergência de Kullback-Leibler generalizada (modelo de contagens de Poisson) | 10 |
| Regras multiplicativas | Atualização de Lee & Seung que preserva não-negatividade de forma nativa sem projeção | 10 |
| Matriz monomial | Produto de matriz de permutação por diagonal positiva ($A \ge 0, A^{-1} \ge 0$), ambiguidade trivial da NMF | 10 |
| Atenção: $M$, $N$, $\lambda$, $H$ na Aula 10 | $M$ usuários, $N$ itens, $\lambda$ regularização e $H$ fator da NMF; colidem com $M$ latente e $N$ pontos (Aula 6), $\lambda_i$ autovalor (Aula 6) e $\mathbf{H}$ genérico (Aula 5) | 10 |
| MNAR | Falta não aleatória: a ausência de uma nota depende do valor; "avaliou" é um colisor (Aula 9) | 10 |
| Hit@10 | Fração dos usuários com ao menos um item de teste bem avaliado entre os 10 recomendados | 10 |
| $P$, $Q$; $X=\{\mathbf{x}_i\}_{i=1}^n$, $Y=\{\mathbf{y}_j\}_{j=1}^m$ | Distribuições e amostras de referência e de produção; $\mathbf{y}_j$ é um ponto, não um rótulo (o rótulo é $c$) | 11 |
| $H_0$, nível $\alpha$, poder, $\hat p$, $B$ | Teste de duas amostras; p-valor de permutação $\hat p=(1+\#\{T_b\ge T_0\})/(B+1)$ com $B$ permutações. **Atenção:** $\alpha$ colide com $\alpha_0$ da Dirichlet (Aula 5) | 11 |
| $k(\mathbf{x},\mathbf{x}')$, $\phi$, $\mathcal{H}$, $\sigma$ | Kernel como produto interno no espaço de atributos; kernel Gaussiano de largura $\sigma$, com $\gamma=1/(2\sigma^2)$ (Aula 5). **Atenção:** $\sigma$ colide com o ruído do decoder (Aulas 6–7); "kernel" na Aula 2 é a janela do KDE | 11 |
| $\mathrm{MMD}[\mathcal{F},P,Q]$, $\boldsymbol\mu_P$, $f^\star$ | Supremo de diferenças de médias em $\mathcal{F}$; *mean embedding* $\mathbb{E}_P[\phi(\mathbf{x})]$; função testemunha $\propto\mathbb{E}_Pk(\mathbf{x},\cdot)-\mathbb{E}_Qk(\mathbf{y},\cdot)$ | 11 |
| $\widehat{\mathrm{MMD}}_u^2$, $\widehat{\mathrm{MMD}}_b^2$ | Estimadores não viesado (sem pares $i=i'$, pode ser negativo) e viesado | 11 |
| *Covariate*, *label*, *concept shift* | $q(\mathbf{x},c)=q(\mathbf{x})p(c\mid\mathbf{x})$; $q(\mathbf{x},c)=q(c)p(\mathbf{x}\mid c)$; mudança em $p(c\mid\mathbf{x})$ | 11 |

## Pendências

- **Aula 2:** uma nota antiga diz que restaram citações de PRML/ESL em inglês sem tradução. Conferir.
- **Aula 1:** falta o par DLFC para as fontes (só PRML).
- **Quantidade de testes:** Aulas 1–3 têm 12 testes (a regra é 6–10).
- **Nomes legados:** `_03-respostas-pausas.md` (Aulas 2 e 3) e `_00-planejamento.md`/`_01-respostas.md` (Aulas 4–6).
- **Vírgula decimal em `$`{python} brl(x)`$`:** a saída inline do Quarto escapa a vírgula (`0\,998`, que o MathJax mostra como espaço). Afeta pelo menos a Aula 6. Corrigido na Aula 7: número isolado fica fora de `$…$`; expressão mista usa o *helper* `mm()` (Markdown gerado em Python, vírgula como `{,}`).
