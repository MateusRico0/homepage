## Resumo — Aula 10

A Aula 9 explorou a mineração não supervisionada de regras de associação e a modelagem gráfica probabilística através de Redes Bayesianas direcionadas para variáveis categóricas e discretas. Contudo, em problemas industriais massivos de personalização e comércio eletrônico — como plataformas de streaming de vídeo (Netflix), música (Spotify) e catálogos de e-commerce (Amazon) —, as interações entre usuários e itens manifestam-se na forma de matrizes de avaliação (*ratings*) ou consumo. Essas matrizes possuem duas propriedades definidoras: **dimensionalidade colossal** ($10^6$ a $10^9$ usuários e itens) e **esparsidade extrema**, onde tipicamente mais de $99\%$ das entradas são desconhecidas e não observadas.

Esta aula aprofunda a **Parte 3: Descoberta de Informação e Estruturas em Grande Escala**, formalizando os fundamentos matemáticos e estatísticos dos **Sistemas de Recomendação baseados em Fatoração de Matrizes: SVD Regularizada e Fatoração de Matrizes Não-Negativa (NMF)**.

Iniciamos demonstrando por que a Decomposição em Valores Singulares clássica (SVD truncada via Teorema de Eckart-Young-Mirsky, Aula 5 de Álgebra Linear) colapsa diante de matrizes de recomendação reais: a SVD clássica exige matrizes densas e preenchidas, e a imputação ingênua de zeros ou médias distorce irremediavelmente a geometria dos fatores latentes. A partir do célebre avanço do *Netflix Prize* (Koren, Bell & Volinsky, 2009; Funk, 2006), reformulamos a aproximação de baixo posto como um problema de otimização contínua restrito estritamente ao conjunto de **entradas observadas**, incorporando regularização $L_2$ e termos de viés (*baseline predictors*) para capturar idiossincrasias sistemáticas de usuários e itens.

Em seguida, contrastamos as duas principais estratégias de treinamento: o **SGD Estocástico por Entrada**, que atualiza vetores latentes em tempo real a cada observação, e os **Mínimos Quadrados Alternados (*Alternating Least Squares* - ALS)**, que exploram a biconvexidade do problema para desacoplar a otimização em sistemas lineares independentes, ideais para computação distribuída. 

Na segunda metade da aula, investigamos uma das restrições geométricas mais profundas do aprendizado não supervisionado: a **Fatoração de Matrizes Não-Negativa (NMF)** (Lee & Seung, 1999; ESL §14.6). Revelamos que a PCA/SVD clássica gera fatores latentes com coeficientes positivos e negativos arbitrários, cujas reconstruções dependem de complexos cancelamentos subtrativos sem correspondência física ("combinações holísticas"). Em contrapartida, ao impor que $W \ge 0$ e $H \ge 0$, a NMF proíbe subtrações e força o modelo a aprender uma **representação baseada em partes puramente aditivas** (*parts-based representation*), onde os fatores latentes atuam como blocos construtivos semanticamente interpretáveis (tópicos de texto, partes de rostos, gêneros musicais puros). Deduzimos as célebres **Regras de Atualização Multiplicativas de Lee & Seung (2001)** baseadas em divergência de Kullback-Leibler e perda de Frobenius, e encerramos analisando o dilema da não-unicidade da NMF identificado por Donoho & Stodden (2004).

**Objetivos:**
1. Formular matematicamente o problema de filtragem colaborativa como a aproximação de baixo posto de matrizes esparsas com dados faltantes, demonstrando as falhas da SVD clássica e da imputação de médias.
2. Dedução do modelo de fatores latentes regularizado com preditores de linha de base (vieses de usuário, item e média global) e derivação das regras de gradiente descendente estocástico (SGD de Funk).
3. Compreender a propriedade de biconvexidade da perda quadrática e a mecânica dos Mínimos Quadrados Alternados (ALS) para paralelização em larga escala.
4. Comparar a geometria dos fatores latentes da SVD/PCA (espaço ortogonal com cancelamentos) com a geometria cônica da NMF (combinações convexas/cônicas não-negativas e partes aditivas).
5. Deduzir analiticamente as Regras de Atualização Multiplicativas de Lee & Seung (2001) para NMF sob distância euclidiana e divergência de Kullback-Leibler, e avaliar o problema de identificabilidade e não-unicidade (Donoho & Stodden, 2004).

**Pré-requisitos:** Decomposição em Valores Singulares (SVD) e projeções de baixo posto (Aula 5/6); Descida do gradiente e estocasticidade (Aula 8/10 de Otimização); Conceitos básicos de álgebra matricial e normas de Frobenius.
**Estratégia Pedagógica:** A (Outside-In) — Do desafio prático do *Netflix Prize* e do colapso da SVD em dados esparsos $\to$ Formulação de fatores latentes regularizados $\to$ Dinâmica algorítmica (SGD vs ALS) $\to$ A virada geométrica da não-negatividade na NMF $\to$ Regras multiplicativas e interpretabilidade por partes.

**Datasets e Cenários-Fio:**
1. *Matriz de Avaliações de Filmes (Estilo MovieLens)*: Matriz controlada $M \times N$ de usuários e filmes com esparsidade intencional de $80\%$, contrastando a predição da SVD clássica com imputação versus o modelo de fatores latentes regularizado com vieses.
2. *Decomposição de Imagens de Faces e Tópicos de Texto (Lee & Seung / Olivetti)*: Demonstração da emergência de partes semânticas locais (olhos, narizes, bocas ou vocabulário temático não-negativo) na NMF contra os autovetores globais e fantasmagóricos da PCA.

---

## Plano de aula — Aula 10 (carga horária: ~95–100 min)

1. **Revisão e Introdução** (~10 min)
   - *Revisão:* Da Aula 9 (grafos discretos de dependência e regras de associação) para o problema contínuo/latente de predição em matrizes massivas com dados faltantes.
   - *Ideia Central:* O que um usuário não avaliou não é "nota zero"; é uma variável latente não observada que deve ser inferida pela correlação cruzada de preferências de baixo posto.
   - *Problema Motivador:* Uma matriz de streaming com $10^6$ usuários e $10^4$ filmes, onde cada usuário assistiu em média a apenas 50 títulos ($99{,}5\%$ de entradas vazias). Como recomendar novos itens?
   - *Roteiro (4 Perguntas Centrais):*
     1. Por que a SVD clássica falha diante de dados faltantes e como reformular o problema como otimização restrita às entradas observadas?
     2. Como decompor avaliações em um espaço latente compartilhado de usuários e itens enriquecido por vieses estruturais?
     3. Como o SGD estocástico e o ALS resolvem a não-convexidade da fatoração matricial?
     4. Por que a restrição de não-negatividade na NMF transforma combinações matemáticas abstratas em partes físicas aditivas e interpretáveis?
   - *Pausa Ativa 1.*

2. **Intuição — O Espaço dos Gostos Ocultos e os Blocos de Montar** (~8 min)
   - *Os Fatores Latentes:* Filmes e usuários não habitam mundos separados; ambos podem ser projetados em um mesmo espaço vetorial de "dimensões conceituais ocultas" (ex.: grau de ação, teor de comédia, sofisticação dramática). A nota prevista é o produto interno entre o perfil de gosto do usuário e a assinatura do filme.
   - *A Metáfora da NMF (Lego vs Massinha):* A PCA mistura dimensões como massinha de modelar colorida que se misturam e cancelam (adicionando azul e subtraindo vermelho). A NMF funciona como blocos de Lego: só podemos construir um castelo adicionando blocos (peças não-negativas), garantindo que cada bloco continue reconhecível individualmente.

3. **Bloco 1: O Colapso da SVD Clássica e o Modelo de Fatores Latentes** (~20 min)
   - A SVD clássica de Mínimos Quadrados: $R = U \Sigma V^T \approx P Q^T$.
     - O Teorema de Eckart-Young-Mirsky assume matriz completamente conhecida.
     - A cilada da imputação: preencher valores não observados com zero distorce os autovetores (assume que o usuário detesta todos os filmes não vistos); preencher com a média global destrói a variância discriminativa.
   - A Formulação do *Netflix Prize* (Koren et al., 2009; Funk, 2006):
     - Otimização estritamente restrita ao conjunto de pares observados $\Omega = \{(u, i) \mid r_{ui} \text{ é observado}\}$:
       $$\min_{P, Q} \frac{1}{2}\sum_{(u, i) \in \Omega} (r_{ui} - \mathbf{p}_u^T \mathbf{q}_i)^2 + \frac{\lambda}{2} \sum_u \|\mathbf{p}_u\|_2^2 + \frac{\lambda}{2} \sum_i \|\mathbf{q}_i\|_2^2$$
     - Interpretação geométrica: $\mathbf{p}_u \in \mathbb{R}^K$ (afinidade do usuário pelos $K$ fatores) e $\mathbf{q}_i \in \mathbb{R}^K$ (presença dos $K$ fatores no item).
   - O Modelo com Preditores de Linha de Base (*Baseline Predictors*):
     - A maior parte da variação nas notas não decorre de preferências sutis, mas de efeitos principais sistemáticos:
       $$\hat{r}_{ui} = \mu + b_u + b_i + \mathbf{p}_u^T \mathbf{q}_i$$
     - $\mu$: média global de todas as avaliações do catálogo;
     - $b_u$: viés do usuário $u$ (usuários sistematicamente críticos vs generosos);
     - $b_i$: viés do item $i$ (obras-primas aclamadas vs produções fracas).
   - *Pausa Ativa 2.*

4. **Bloco 2: Algoritmos de Otimização: SGD de Funk vs. Mínimos Quadrados Alternados (ALS)** (~18 min)
   - Não-Convexidade Conjunta: A função de custo é quadrática separadamente em $P$ e em $Q$, mas é **não-convexa conjuntamente** devido ao termo bilinear $\mathbf{p}_u^T \mathbf{q}_i$.
   - Algoritmo 1: Stochastic Gradient Descent por Amostra Observada (Funk-SVD):
     - Para cada par $(u, i) \in \Omega$ sorteado aleatoriamente:
       $$e_{ui} = r_{ui} - \hat{r}_{ui}$$
       $$b_u \leftarrow b_u + \gamma (e_{ui} - \lambda b_u), \quad b_i \leftarrow b_i + \gamma (e_{ui} - \lambda b_i)$$
       $$\mathbf{p}_u \leftarrow \mathbf{p}_u + \gamma (e_{ui} \mathbf{q}_i - \lambda \mathbf{p}_u)$$
       $$\mathbf{q}_i \leftarrow \mathbf{q}_i + \gamma (e_{ui} \mathbf{p}_u - \lambda \mathbf{q}_i)$$
     - Custo por época: $\mathcal{O}(|\Omega| \cdot K)$, perfeitamente linear no número de avaliações observadas!
   - Algoritmo 2: Alternating Least Squares (ALS):
     - Fixando $Q$, o problema divide-se em $M$ problemas independentes de Ridge Regression:
       $$\mathbf{p}_u = \left(\sum_{i \in \mathcal{I}_u} \mathbf{q}_i \mathbf{q}_i^T + \lambda I\right)^{-1} \sum_{i \in \mathcal{I}_u} r_{ui} \mathbf{q}_i$$
     - Fixando $P$, atualizam-se os vetores $\mathbf{q}_i$ de forma análoga.
     - Vantagem: Paralelização maciça em clusters de computação distribuída (ex.: Apache Spark).
   - *Pausa Ativa 3.*

5. **Bloco 3: Fatoração de Matrizes Não-Negativa (NMF) e a Decomposição em Partes** (~20 min)
   - A Limitação Semântica da SVD/PCA:
     - As colunas de $U$ e $V$ contêm números negativos. Na reconstrução de uma imagem ou perfil, partes com sinal oposto cancelam-se destrutivamente. Um autovetor de PCA ("eigenface") representa uma variação global indistinta.
   - A Formulação da NMF (Lee & Seung, 1999; ESL §14.6):
     $$V \approx W H, \quad \text{sujeito a } W \in \mathbb{R}_{\ge 0}^{M \times K}, \, H \in \mathbb{R}_{\ge 0}^{K \times N}$$
     - $V$: matriz de dados estritamente não-negativos (intensidades de pixel, contagens de palavras, frequências de consumo);
     - $W$: matriz de fatores/partes básicas ($K$ protótipos não-negativos);
     - $H$: matriz de coeficientes de ativação não-negativos.
   - O Princípio Aditivo (*Parts-Based Representation*):
     - Como $W_{ik} \ge 0$ e $H_{kj} \ge 0$, cada dado $\mathbf{v}_j \approx \sum_{k=1}^K H_{kj} \mathbf{w}_k$ é uma **combinação cônica estritamente aditiva** dos protótipos. É impossível subtrair atributos.
     - Consequência: a NMF aprende partes localizadas e esparsas (olhos, bocas, tópicos focados).
   - *Pausa Ativa 4.*

6. **Bloco 4: Funções de Perda, Regras Multiplicativas de Lee & Seung e Não-Unicidade** (~17 min)
   - Funções de Custo para NMF:
     1. Distância Euclidiana de Frobenius: $\|V - WH\|_F^2 = \sum_{ij} (v_{ij} - (WH)_{ij})^2$.
     2. Divergência de Kullback-Leibler Generalizada / I-Divergence (Modelo de Poisson):
        $$D_{KL}(V \parallel WH) = \sum_{i,j} \left[ v_{ij} \ln \frac{v_{ij}}{(WH)_{ij}} - v_{ij} + (WH)_{ij} \right]$$
   - As Regras de Atualização Multiplicativas (Lee & Seung, 2001):
     - Para perda de Frobenius:
       $$H_{kj} \leftarrow H_{kj} \frac{(W^T V)_{kj}}{(W^T W H)_{kj}}, \quad W_{ik} \leftarrow W_{ik} \frac{(V H^T)_{ik}}{(W H H^T)_{ik}}$$
     - Elegância matemática: se a inicialização for estritamente positiva, os fatores multiplicativos são não-negativos, **preservando a não-negatividade automaticamente sem exigir projeção**.
   - O Dilema da Não-Unicidade e Identificabilidade (Donoho & Stodden, 2004; ESL §14.6):
     - Para qualquer matriz invertível $A$ tal que $A \ge 0$ e $A^{-1} \ge 0$ (matrizes monomiais: permutação e escalonamento diagonal), temos $V \approx (W A)(A^{-1} H)$.
     - Além disso, na presença de espaço aberto entre o cone dos dados e os eixos coordenados, existem múltiplos cones convexos geradores igualmente válidos.
   - *Pausa Ativa 5.*

7. **Fechamento** (~5 min)
   - *Retomando as 4 Perguntas:* Síntese conceitual das respostas estruturadas ao longo da aula.
   - *Quadro Comparativo:* SVD Clássica vs. Fatores Latentes Regularizados (Funk) vs. NMF.
   - *Ponte para a Aula 11:* Matrizes e representações em grande escala são sensíveis a mudanças na distribuição dos dados de produção $\to$ **Aula 11: Alinhamento de Distribuições e Detecção de Domain Shift (Data Drift)**.
   - Links para Exercícios e Soluções.

---

## Fontes usadas — Aula 10

Deslocamentos página impressa → PDF: `esl.pdf` +19; `prml.pdf` +20.

### Fonte 1: Hastie, T., Tibshirani, R., & Friedman, J. (2009), *The Elements of Statistical Learning* (ESL), Cap. 14 (§14.6, pp. 553–558, PDF pp. 572–577)
**Uso pretendido:** Definição formal da Fatoração de Matrizes Não-Negativa (NMF), modelo de Poisson / verossimilhança de contagens, algoritmo de regras multiplicativas de Lee & Seung (2001), comparação de representações por partes (faces) e o teorema da não-unicidade de Donoho & Stodden (2004).
**Trechos:**
> "Non-negative matrix factorization (Lee and Seung, 1999) is a recent alternative approach to principal components analysis, in which the data and components are assumed to be non-negative. The $N \times p$ data matrix $X$ is approximated by $X \approx W H$ where $W$ is $N \times r$ and $H$ is $r \times p$, with $x_{ij}, w_{ik}, h_{kj} \ge 0$... The authors point out that unlike VQ and PCA, NMF learns to represent faces with a set of basis images resembling parts of faces." (§14.6, pp. 553–554)
> "Donoho and Stodden (2004) point out a potentially serious problem with non-negative matrix factorization. Even in situations where $X = W H$ holds exactly, the decomposition may not be unique... The data points lie in $p = 2$ dimensions, and there is 'open space' between the data and the coordinate axes. We can choose the basis vectors $h_1$ and $h_2$ anywhere in this open space, and represent each data point exactly with a nonnegative linear combination of these vectors." (§14.6, p. 554)

### Fonte 2: Bishop, C. M. (2006), *Pattern Recognition and Machine Learning* (PRML), Cap. 12 (§12.1 e §12.2, pp. 559–580, PDF pp. 579–600)
**Uso pretendido:** A formulação da PCA clássica, reconstrução linear ótima em dados completos, e a extensão de Probabilistic PCA (PPCA) com inferência via EM para matrizes contendo dados faltantes.
**Trechos:**
> "One of the major advantages of probabilistic PCA is that it can handle missing data in a natural way using the EM algorithm. Suppose some of the entries in the data matrix $X$ are unobserved... The EM algorithm allows the parameters of the model to be estimated directly from the incomplete data without having to perform prior imputation." (§12.2.2, pp. 579–580)

### Fonte 3: Koren, Y., Bell, R., & Volinsky, C. (2009), "Matrix Factorization Techniques for Recommender Systems", *IEEE Computer*, 42(8): 30–37
**Uso pretendido:** A formulação canônica do modelo de fatores latentes do Netflix Prize, regularização $L_2$ sobre entradas observadas $\Omega$, preditores de linha de base (vieses de usuário e item) e otimização por SGD e ALS.
**Trechos:**
> "Matrix factorization models map both users and items to a joint latent factor space of dimensionality $f$. The user-item interaction is modeled by inner products in that space... Conventional SVD is undefined when knowledge about the matrix is incomplete. Moreover, carelessly addressing only the relatively few known entries is highly prone to overfitting... We minimize the regularized squared error on the set of known ratings: $\min_{q*, p*} \sum_{(u, i) \in \kappa} (r_{ui} - q_i^T p_u)^2 + \lambda(\|q_i\|^2 + \|p_u\|^2)$." (pp. 31–32)
> "The rating $\hat{r}_{ui}$ is predicted by $\hat{r}_{ui} = \mu + b_i + b_u + q_i^T p_u$. The parameters $\mu, b_i, b_u$ account for the baseline predictors, capturing data tendencies that are independent of user-item interactions." (p. 33)

### Fonte 4: Lee, D. D. & Seung, H. S. (1999), "Learning the parts of objects by non-negative matrix factorization", *Nature*, 401: 788–791; e Lee & Seung (2001), "Algorithms for Non-negative Matrix Factorization", *NeurIPS*
**Uso pretendido:** Prova das regras multiplicativas de atualização para NMF e demonstração de convergência monotônica não-crescente sob funções de perda de Frobenius e Divergência KL generalizada.
**Trechos:**
> "Non-negative matrix factorization is distinguished from other methods by its use of non-negativity constraints. These constraints lead to a parts-based representation because they allow only additive, not subtractive, combinations... We prove that the Euclidean distance $\|V - WH\|$ and the divergence $D(V \parallel WH)$ are non-increasing under the multiplicative update rules." (1999 / 2001)

