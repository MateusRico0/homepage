## Resumo — Aula 13

A Aula 12 concluiu a linhagem dos métodos acelerados de primeira ordem baseados em coordenadas escalares, culminando na síntese do **Adam** e na correção do **AdamW**. Tanto o RMSProp quanto o Adam e o AdamW operam sob uma premissa simplificadora radical: **o precondicionamento diagonal**, que trata cada um dos milhões ou bilhões de parâmetros de uma rede neural profunda como um escalar independente em um vetor unidimensional $\mathbf{w} \in \mathbb{R}^d$.

No entanto, em redes neurais modernas (especialmente camadas densas, convoluções e projeções de atenção em Transformers), os parâmetros não são grandezas escalares isoladas: eles organizam-se naturalmente como **matrizes de pesos e operadores lineares** $W \in \mathbb{R}^{m \times n}$. Achatar $W$ em um vetor $\text{vec}(W) \in \mathbb{R}^{mn}$ descarta sumariamente toda a correlação cruzada entre as linhas (espaço de ativações de saída) e colunas (espaço de representações de entrada). Um precondicionador completo de segunda ordem exigiria uma matriz Hessiana de dimensão $(mn) \times (mn)$, cuja inversão custaria catastróficos $\mathcal{O}((mn)^3) = \mathcal{O}(m^3 n^3)$ — absolutamente inviável quando $m, n \approx 4.096$ ou $8.192$.

Esta aula investiga a fronteira mais moderna da otimização para Aprendizado Profundo: o **Precondicionamento Estruturado e a Ortogonalização Matricial**. No Bloco 1, examinamos a geometria de operadores matriciais e a aproximação de segunda ordem via produtos de Kronecker, deduzindo o algoritmo **Shampoo** (Gupta et al., 2018; Anil et al., 2020), que desacopla a curvatura em covariâncias esquerdas $L = \mathbb{E}[G G^T] \in \mathbb{R}^{m \times m}$ e direitas $R = \mathbb{E}[G^T G] \in \mathbb{R}^{n \times n}$, atualizando a matriz via $L^{-1/4} G R^{-1/4}$ e reduzindo o custo de inversão de $(mn)^3$ para meros $m^3 + n^3$. No Bloco 2, resgatamos a **Decomposição Polar** (desenvolvida na Aula 5) sob uma nova ótica geométrica: a projeção da matriz de gradientes no grupo das matrizes ortogonais $\mathcal{O}(n)$, provando sua otimalidade no problema de Procrustes e seu papel em limitar a norma espectral das atualizações. No Bloco 3, enfrentamos o gargalo computacional das GPUs: calcular SVDs a cada iteração é inviável no hardware moderno; deduzimos então os **Polinômios de Newton-Schulz**, que calculam a decomposição polar a velocidade extrema utilizando exclusivamente multiplicações matriciais puras (GEMM). Por fim, no Bloco 4, dissecamos a arquitetura do otimizador **Muon** (Jordan et al., 2024), que une momento matricial de Nesterov com ortogonalização por Newton-Schulz, explicando por que ele quebrou recordes recentes de eficiência no pré-treinamento de Transformers.

**Objetivos:**
1. Compreender as limitações teóricas do precondicionamento diagonal em tensores de pesos e analisar o custo intratável do Hessiano completo de operadores matriciais.
2. Derivar analiticamente a estrutura de covariância bilinear do algoritmo Shampoo e a atualização via raízes quartas matriciais $L^{-1/4} G R^{-1/4}$ sob produtos de Kronecker.
3. Conectar a projeção no grupo ortogonal à Decomposição Polar da Aula 5, formulando o problema de Procrustes ortogonal e seu impacto no controle da norma espectral.
4. Derivar a recorrência polinomial de Newton-Schulz ($X_{k+1} = \frac{1}{2}X_k(3I - X_k^T X_k)$) e provar sua convergência cúbica/química para o fator ortogonal da decomposição polar.
5. Analisar a mecânica algorítmica do otimizador Muon, contrastando sua eficiência de hardware (Tensor Cores) e sua velocidade de aprendizado em relação ao AdamW em Large Language Models (LLMs).

**Pré-requisitos:**
- SVD, Decomposição Polar e normas matriciais (Aula 5).
- Pré-condicionamento Diagonal e RMSProp (Aula 11).
- Momento, Adam e AdamW (Aula 12).
- Álgebra Linear: Produtos de Kronecker, traço, produto interno de Frobenius, matrizes ortogonais.

**Problema-fio:** Treinamento de uma camada de projeção linear de Transformer ($W \in \mathbb{R}^{m \times n}$) sob gradientes de covariância anisotrópica cruzada, comparando o colapso espectral do SGD, a ineficiência estrutural do AdamW e a convergência acelerada do Muon via ortogonalização por Newton-Schulz.

**Estratégia Pedagógica:** B (Inside-Out com Problema-Fio) — da falha da diagonalização escalar em capturar correlações entre neurônios ao precondicionamento estruturado de Kronecker (Shampoo), transicionando para a geometria pura da ortogonalização polar e sua computação ultra-rápida via Newton-Schulz no otimizador Muon.

---

## Plano de aula — Aula 13 (carga horária: ~110 min)

1. **Revisão e Introdução** (~12 min)
   - *Revisão:* Da Aula 12 (Adam e AdamW). O precondicionamento diagonal escala cada peso por $\frac{1}{\sqrt{v_{ij}}+\epsilon}$.
   - *A Pergunta Crítica:* Pesos de uma camada de rede neural atuam em conjunto como uma transformação linear $W\mathbf{x}$. Será que tratar $W_{ij}$ e $W_{ik}$ como escalares sem correlação faz sentido quando ambos operam sobre as mesmas ativações de entrada?
   - *Problema Motivador:* Camada linear $W \in \mathbb{R}^{1024 \times 1024}$. O Hessiano completo possui dimensão $10^6 \times 10^6$ ($10^{12}$ entradas). O AdamW aproxima essa matriz gigante por sua diagonal ($10^6$ entradas), ignorando 99,9999% da informação de curvatura cruzada!
   - *Roteiro (4 Perguntas Centrais):*
     1. Por que a diagonalização escalar falha em redes profundas e como o produto de Kronecker permite aproximar o Hessiano completo a custo linear no número de parâmetros?
     2. Como o algoritmo Shampoo utiliza matrizes de covariância esquerda e direita ($L$ e $R$) para precondicionar tensores de pesos?
     3. Qual é a justificativa matemática para projetar atualizações no grupo das matrizes ortogonais via Decomposição Polar?
     4. Como a iteração polinomial de Newton-Schulz permite calcular a decomposição polar em GPUs sem jamais rodar uma SVD, e como o otimizador Muon supera o AdamW?
   - *Pausa 1.*

2. **Intuição — A Geometria de Matrizes vs. Vetores Achatados** (~8 min)
   - Visualização: uma transformação linear estica e rotaciona o espaço. Achatar uma matriz em vetor perde a noção de linha (neurônio receptor) e coluna (canal transmissor).
   - O que significa precondicionar uma matriz? Em vez de esticar cada pixel isoladamente, corrigimos as deformações no espaço de entrada e no espaço de saída.
   - A Decomposição Polar $G = U P$: $P$ contém as deformações e estiramentos de escala; $U$ contém a rotação pura rígida de energia uniforme.

3. **Bloco 1: O Precondicionamento Estruturado de Kronecker e o Algoritmo Shampoo** (~25 min)
   - O gradiente matricial $G = \nabla_W \mathcal{L} \in \mathbb{R}^{m \times n}$.
   - Covariâncias de segunda ordem por dimensão:
     - Covariância entre linhas (espaço de saída): $L = \mathbb{E}[G G^T] \in \mathbb{R}^{m \times m}$.
     - Covariância entre colunas (espaço de entrada): $R = \mathbb{E}[G^T G] \in \mathbb{R}^{n \times n}$.
   - O modelo de Kronecker para o Hessiano: $H \approx L \otimes R$.
   - A regra de atualização do Shampoo:
     $$\Delta W = - \alpha L^{-1/4} G R^{-1/4}$$
   - Redução exponencial de complexidade: inversão de $(mn)^3$ cai para $m^3 + n^3$.

4. **Bloco 2: Ortogonalização Matricial e a Decomposição Polar** (~25 min)
   - Revisitando a Aula 5: Teorema da Decomposição Polar $M = U P$.
   - O Problema de Procrustes Ortogonal:
     $$\min_{U \in \mathcal{O}(m, n)} \|U - G\|_F^2 \implies U = G (G^T G)^{-1/2}$$
   - Propriedades de $U$: todos os valores singulares são unitários ($\sigma_i(U) = 1$).
   - Controle da norma espectral: $\|U\|_2 = 1$, prevenindo explosão ou colapso da magnitude das atualizações nos blocos residuais de Transformers.
   - Por que o SVD clássico é um gargalo intratável em aceleradores modernos (GPUs/TPUs).

5. **Bloco 3: Computação Hardware-Friendly — As Iterações de Newton-Schulz** (~20 min)
   - O objetivo: aproximar $G(G^T G)^{-1/2}$ sem autovalores e sem divisões escalares, usando apenas produtos matriciais (GEMM).
   - A recorrência clássica de Newton-Schulz de 3ª ordem:
     $$X_0 = \frac{G}{\|G\|_F}, \quad X_{k+1} = \frac{1}{2} X_k (3I - X_k^T X_k)$$
   - Dedução da convergência cúbica dos valores singulares em direção a $1$:
     $$\sigma_{k+1} = \frac{1}{2} \sigma_k (3 - \sigma_k^2)$$
   - Polinômios de ordem superior (5ª ordem) e estabilização de ponto flutuante (BF16/FP16) para execução em Tensor Cores.

6. **Bloco 4: A Arquitetura do Otimizador Muon** (~12 min)
   - A anatomia do Muon (Momentum Orthogonalized by Newton-Schulz):
     1. Acúmulo de momento de Nesterov sobre o gradiente matricial: $M_t = \beta M_{t-1} + G_t$.
     2. Ortogonalização rápida via 5 a 6 passos de Newton-Schulz: $O_t = \text{NewtonSchulz}(M_t)$.
     3. Escalonamento dimensional: $\Delta W_t = -\alpha \cdot \max(1, \sqrt{m/n}) \cdot O_t$.
   - Eficiência de treinamento: por que o Muon treina modelos de linguagem na metade dos FLOPs do AdamW.
   - Quando usar AdamW (embeddings e vetores 1D) versus Muon (matrizes densas e projeções de atenção).

7. **Fechamento e Próximos Passos** (~8 min)
   - Síntese da genealogia dos precondicionadores: de Newton exato ($\mathcal{O}(d^3)$) para Diagonal/AdamW ($\mathcal{O}(d)$) até Estruturado/Muon ($\mathcal{O}(mn \min(m, n))$).
   - O que fica em aberto: todos os métodos até aqui assumiram funções de perda diferenciáveis e suaves ($L$-suaves). E quando a perda ou a regularização introduz bicos e não-diferenciabilidade (como a norma $L_1$ no Lasso)?
   - Ponte para a Aula 14: **Otimização Não-Suave, Subgradientes e Operadores Proximais (ISTA/FISTA)**.
