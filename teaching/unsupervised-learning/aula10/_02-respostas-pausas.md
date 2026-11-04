# Respostas e Guia Docente — Pausas Ativas da Aula 10

Este documento reúne as resoluções detalhadas, a justificativa analítica de cada afirmação de Verdadeiro/Falso e diretrizes didáticas para condução das cinco Pausas Ativas da **Aula 10: Sistemas de Recomendação: Fatoração de Matrizes (SVD e NMF)**.

---

## Pausa Ativa 1: O Colapso da SVD e a Estrutura dos Vieses

### 1. Resolução da Pergunta Aberta
*Cenário:* Média global $\mu = 3{,}5$, viés de Carlos $b_u = -0{,}6$, viés do filme *Interestelar* $b_i = +0{,}8$.
Afinidade residual latente $\mathbf{p}_u^T \mathbf{q}_i = +0{,}5$.

- **Nota de Linha de Base (*Baseline Predictor*):**
  $$b_{ui} = \mu + b_u + b_i = 3{,}5 + (-0{,}6) + 0{,}8 = 3{,}7$$
  *Interpretação:* Antes de saber se Carlos gosta especificamente de ficção científica, a nota esperada para ele assistir a um filme aclamado como *Interestelar* já é de 3,7 estrelas (o otimismo do filme compensa parcialmente o pessimismo do usuário).

- **Nota Final Prevista ($\hat{r}_{ui}$):**
  $$\hat{r}_{ui} = b_{ui} + \mathbf{p}_u^T \mathbf{q}_i = 3{,}7 + 0{,}5 = 4{,}2$$
  Como Carlos aprecia especificamente os fatores temáticos presentes no filme ($\mathbf{p}_u^T \mathbf{q}_i = +0{,}5 > 0$), a predição final sobe para 4,2 estrelas.

### 2. Gabarito Comentado dos Testes Conceituais (V/F)
*   **(A) Falso.** O Teorema de Eckart-Young-Mirsky assume que todas as entradas da matriz são números reais conhecidos e finitos. Ele não se aplica a matrizes com entradas indefinidas (`NaN`) ou dados faltantes. Aplicar a SVD clássica exige preencher previamente a matriz, o que distorce a geometria do problema.
*   **(B) Verdadeiro.** Como a escala de avaliação varia tipicamente entre 1 e 5 estrelas, preencher células vazias com zero trata a ausência de observação como uma avaliação pior do que a pior nota possível (1 estrela), forçando o modelo a prever desinteresse por quase todo o catálogo.
*   **(C) Verdadeiro.** O termo $b_u$ isola o nível médio de exigência de cada usuário. Um usuário generoso terá $b_u > 0$, elevando a nota base de todos os itens avaliados por ele de forma aditiva e consistente.
*   **(D) Falso.** A regularização $L_2$ ($\frac{\lambda}{2} \|\mathbf{p}_u\|^2$) penaliza magnitudes elevadas dos pesos para evitar sobreajuste em usuários com poucas avaliações. Ela não impõe restrição de sinal e não impede coordenadas negativas nos vetores latentes. A não-negatividade é a propriedade definidora da NMF, e não da SVD regularizada.

---

## Pausa Ativa 2: Dinâmica de Otimização no Espaço Latente

### 1. Resolução da Pergunta Aberta
*Cenário:* $\gamma = 0{,}05$, $\lambda = 0{,}02$.
$\mathbf{p}_u = [0{,}8, 0{,}2]^T$, $\mathbf{q}_i = [1{,}0, 0{,}5]^T$, $r_{ui} = 5{,}0$, linha de base $= 3{,}5$.

- **Predição Atual:**
  $$\hat{r}_{ui} = 3{,}5 + \mathbf{p}_u^T \mathbf{q}_i = 3{,}5 + (0{,}8 \times 1{,}0 + 0{,}2 \times 0{,}5) = 3{,}5 + (0{,}8 + 0{,}1) = 3{,}5 + 0{,}9 = 4{,}4$$
- **Erro Residual:**
  $$e_{ui} = r_{ui} - \hat{r}_{ui} = 5{,}0 - 4{,}4 = +0{,}6$$
- **Atualização de $\mathbf{p}_u$:**
  $$\mathbf{p}_u^{\text{novo}} = \mathbf{p}_u + \gamma (e_{ui} \mathbf{q}_i - \lambda \mathbf{p}_u)$$
  Calculando os termos:
  $$e_{ui} \mathbf{q}_i = 0{,}6 \times \begin{bmatrix} 1{,}0 \\ 0{,}5 \end{bmatrix} = \begin{bmatrix} 0{,}60 \\ 0{,}30 \end{bmatrix}$$
  $$\lambda \mathbf{p}_u = 0{,}02 \times \begin{bmatrix} 0{,}8 \\ 0{,}2 \end{bmatrix} = \begin{bmatrix} 0{,}016 \\ 0{,}004 \end{bmatrix}$$
  $$e_{ui} \mathbf{q}_i - \lambda \mathbf{p}_u = \begin{bmatrix} 0{,}584 \\ 0{,}296 \end{bmatrix}$$
  $$\mathbf{p}_u^{\text{novo}} = \begin{bmatrix} 0{,}80 \\ 0{,}20 \end{bmatrix} + 0{,}05 \times \begin{bmatrix} 0{,}584 \\ 0{,}296 \end{bmatrix} = \begin{bmatrix} 0{,}80 \\ 0{,}20 \end{bmatrix} + \begin{bmatrix} 0{,}0292 \\ 0{,}0148 \end{bmatrix} = \begin{bmatrix} 0{,}8292 \\ 0{,}2148 \end{bmatrix}$$
- *Conclusão:* Como o usuário deu nota 5,0 (acima do previsto), o vetor $\mathbf{p}_u$ cresce em ambas as dimensões, com maior incremento na primeira coordenada ($+0{,}0292$ vs $+0{,}0148$), que é justamente o fator mais forte do filme ($q_{i1} = 1{,}0$). O modelo "aprende" que Carlos aprecia ainda mais esse atributo.

### 2. Gabarito Comentado dos Testes Conceituais (V/F)
*   **(A) Falso.** A presença do termo bilinear $\mathbf{p}_u^T \mathbf{q}_i$ torna a função de perda não-convexa conjuntamente no espaço das matrizes $P$ e $Q$. Ela admite múltiplos mínimos locais e pontos de sela.
*   **(B) Verdadeiro.** Como cada passo do ALS resolve analiticamente uma regressão Ridge ótima em relação a uma das matrizes mantendo a outra fixa, o erro quadrático regularizado não pode aumentar a cada iteração, garantindo convergência monotônica para um ponto crítico estacionário.
*   **(C) Falso.** Se $e_{ui} = 0$, a derivada do erro anula-se, mas o termo de penalização de regularização $-\lambda \mathbf{p}_u$ permanece ativo: $\mathbf{p}_u \leftarrow \mathbf{p}_u - \gamma \lambda \mathbf{p}_u = (1 - \gamma \lambda)\mathbf{p}_u$. Logo, o vetor sofre uma pequena contração de encolhimento (*shrinkage*).
*   **(D) Verdadeiro.** No ALS, cada vetor de usuário $\mathbf{p}_u$ depende unicamente dos itens avaliados por ele e das características desses itens em $Q$. A otimização para $M$ usuários desacopla-se em $M$ problemas de regressão independentes, facilmente distribuíveis entre centenas de nós de um cluster (como no Apache Spark).

---

## Pausa Ativa 3: A Geometria da Não-Negatividade

### 1. Resolução da Pergunta Aberta
*Cenário:* Matriz termo-documento com frequências de palavras.
- Na PCA clássica, a projeção de um documento é reconstruída por uma combinação linear arbitrária de autovetores que contêm pesos positivos e negativos. Para um documento que discute "culinária", a combinação de autovetores pode gerar um valor estimado negativo (ex.: $-4{,}2$) para termos não correlacionados (como "ciência"). Isso é um absurdo físico, pois contagens de ocorrências não podem ser negativas.
- A NMF impõe $W \ge 0$ e $H \ge 0$. Como a reconstrução é dada por $\hat{\mathbf{v}}_j = \sum_k H_{kj} \mathbf{w}_k$, a soma de produtos de números não-negativos é obrigatoriamente não-negativa ($\hat{v}_{ij} \ge 0$). O modelo garante que nenhuma palavra tenha frequência prevista menor que zero.

### 2. Gabarito Comentado dos Testes Conceituais (V/F)
*   **(A) Falso.** Truncar os autovetores negativos da PCA para zero destrói a ortogonalidade, invalida as propriedades de máxima variância e não minimiza o erro de reconstrução sob a restrição de positividade. A NMF é formulada como um problema de otimização restrita resolvido do zero.
*   **(B) Falso.** As colunas de $W$ na NMF formam as arestas de um cone convexo gerador e não precisam ser ortogonais entre si. Fatores com sobreposição parcial (ex.: palavras que aparecem em tópicos correlacionados) são permitidos e frequentes.
*   **(C) Verdadeiro.** Como a NMF proíbe cancelamentos subtrativos, um fator não pode apagar o excesso gerado por outro fator. Para representar eficientemente os dados, cada fator latente é forçado a modelar componentes compactos e espacialmente localizados.
*   **(D) Falso.** A formulação padrão da NMF assume e exige que todos os elementos da matriz original $V$ sejam não-negativos ($v_{ij} \ge 0$). Se houver números negativos, as regras multiplicativas tornam-se indefinidas ou matematicamente inválidas.

---

## Pausa Ativa 4: Regras Multiplicativas e Não-Unicidade

### 1. Resolução da Pergunta Aberta
*Cenário:* Atualização multiplicativa com $(WH)_{ij} < v_{ij}$.
- A regra de atualização de Frobenius para $W$ é $W_{ik} \leftarrow W_{ik} \frac{(V H^T)_{ik}}{(W H H^T)_{ik}}$.
- Se a reconstrução atual subestima a matriz original ($(WH)_{ij} < v_{ij}$), o termo $(V H^T)_{ik} = \sum_j v_{ij} H_{kj}$ será estritamente maior que $(WH H^T)_{ik} = \sum_j (WH)_{ij} H_{kj}$.
- A razão multiplicativa será maior que 1 ($\frac{(VH^T)_{ik}}{(WHH^T)_{ik}} > 1$).
- Consequentemente, o novo valor de $W_{ik}$ aumentará na próxima iteração, elevando a magnitude da reconstrução $(WH)_{ij}$ para aproximá-la do valor real $v_{ij}$. O mecanismo atua como um sistema de controle com realimentação corretiva automática.

### 2. Gabarito Comentado dos Testes Conceituais (V/F)
*   **(A) Verdadeiro.** A regra de atualização tem a forma $W_{ik} \leftarrow W_{ik} \cdot R_{ik}$. Se $W_{ik} = 0$, qualquer que seja o valor do multiplicador $R_{ik}$, o produto será $0 \cdot R_{ik} = 0$. O zero é um ponto absorvente estrito das regras multiplicativas de Lee & Seung.
*   **(B) Verdadeiro.** Conforme demonstrado no ESL (§14.6), minimizar a divergência de Kullback-Leibler generalizada equivale matematicamente a maximizar a log-verossimilhança de variáveis de Poisson independentes com média $(WH)_{ij}$.
*   **(C) Falso.** O Teorema de Donoho & Stodden (2004) provou exatamente o oposto: na ausência de restrições adicionais (como esparsidade ou independência simplicial), a decomposição NMF não é única e admite infinitas rotações cônicas válidas.
*   **(D) Verdadeiro.** Seja $A = \operatorname{diag}(c, 1, \dots, 1)$ e $A^{-1} = \operatorname{diag}(1/c, 1, \dots, 1)$. Temos $(W A)(A^{-1} H) = W (A A^{-1}) H = W I H = WH$. Essa ambiguidade de escala é inerente à bilinearidade da fatoração.

---

## Pausa Ativa 5: Síntese e Comparação Arquitetural

### 1. Resolução da Pergunta Aberta
*Cenário:* Streaming musical com matriz de contagens de reproduções esparsa.
- **Quando usar Funk-SVD:** Se o objetivo primário for a **predição de notas ou preferências implícitas em entradas faltantes** com foco em métricas de erro de predição (RMSE), onde a interpretabilidade das dimensões individuais não é essencial e a velocidade de inferência bilinear com vieses é prioritária.
- **Quando usar NMF:** Se o objetivo for a **descoberta não supervisionada de perfis de gosto e agrupamento interpretável de artistas** (ex.: identificar que o Fator 1 é "Bossa Nova clássica" e o Fator 2 é "Heavy Metal progressivo"). A não-negatividade garante que cada usuário seja representado como uma soma puramente aditiva de gêneros musicais, viabilizando interfaces explicáveis de recomendação ("Recomendamos porque você ouve 70% de Rock e 30% de Blues").

### 2. Gabarito Comentado dos Testes Conceituais (V/F)
*   **(A) Verdadeiro.** Quando a matriz de dados é densa, completa (sem NaNs) e a perda de Frobenius é minimizada sem termos de regularização $L_2$, o minimizador global de posto $K$ coincide exatamente com a projeção fornecida pela SVD truncada clássica de Eckart-Young-Mirsky.
*   **(B) Falso.** A Funk-SVD atua sobre notas reais e desvios em relação à média. Os fatores latentes $\mathbf{p}_u$ e $\mathbf{q}_i$ podem assumir valores positivos e negativos livremente.
*   **(C) Verdadeiro.** A PCA impõe ortogonalidade estrita entre os eixos de projeção, permitindo números negativos. A NMF abandona a exigência de ortogonalidade e impõe a não-negatividade, obtendo como contrapartida a interpretabilidade semântica por partes aditivas.
*   **(D) Verdadeiro.** O algoritmo Non-Negative Alternating Least Squares (NNALS) atualiza alternadamente $W$ e $H$ resolvendo subproblemas de mínimos quadrados restritos à não-negatividade ($\min_{H \ge 0} \|V - WH\|_F^2$), sendo uma alternativa eficiente às regras multiplicativas.

