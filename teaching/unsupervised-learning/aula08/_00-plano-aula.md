## Resumo — Aula 08

A aula aborda a redução de dimensionalidade estritamente voltada para **visualização em 2D/3D**. Partindo da limitação dos métodos focados em reconstrução métrica global (PCA, Autoencoders e MDS), analisamos o **dilema do volume** e o **crowding problem** decorrentes da geometria de altas dimensões. A partir disso, examinamos o MDS e o critério de *Stress*, avançamos para o *Stochastic Neighbor Embedding* (SNE) com formalização de vizinhanças probabilísticas e divergência KL assimétrica, e culminamos no **t-SNE** de van der Maaten & Hinton (2008), demonstrando por que a substituição da distribuição gaussiana pela $t$-Student de 1 grau de liberdade (Cauchy) no mapa latente resolve o *crowding problem*. A aula fecha com uma análise crítica rigorosa das 4 armadilhas de interpretação do t-SNE e o efeito da perplexidade.

**Estratégia Pedagógica:** A (Outside-In) — Problema perceptivo/geométrico (colapso no 2D) $\to$ Preservação métrica global (MDS) $\to$ Formulação probabilística (SNE e assimetria da KL) $\to$ Teoria formal da cauda pesada (t-SNE) $\to$ Cuidados metodológicos e armadilhas interpretativas.

**Datasets-fio:**
1. *Breast Cancer Wisconsin* (30 atributos, fio do curso): comparação de PCA, MDS e t-SNE na separação não supervisionada das lesões.
2. *MNIST* (subconjunto de $N=1.500$ imagens de dígitos 0–9): demonstração visual do colapso de classes em projeções lineares/métricas versus a separação topológica no t-SNE.

---

## Plano de aula — Aula 08 (carga horária: 90–100 min)

1. **Revisão e Introdução** (~10 min) — Reconstrução (Aulas 6 e 7) versus Visualização topológica. O que a alta dimensão esconde. Problema motivador no MNIST e Breast Cancer. Pausa Ativa 1.
2. **Intuição — O Dilema do Volume e o *Crowding Problem*** (~10 min) — Geometria de esferas em $\mathbb{R}^D$ vs $\mathbb{R}^2$. O colapso forçado no centro.
3. **Bloco 1: Preservando Distâncias Métricas — MDS e a Perda *Stress*** (~15 min) — Formulação clássica do MDS. Minimização do *Stress*. Por que distâncias longas sufocam a estrutura local. Pausa Ativa 2.
4. **Bloco 2: Vizinhanças Probabilísticas — SNE e Divergência KL** (~15 min) — Probabilidades condicionais gaussianas $p_{j|i}$. Entropia e o hiperparâmetro Perplexidade $\text{Perp}(P_i) = 2^{H(P_i)}$. Simetrização $p_{ij}$. A assimetria de $\mathrm{KL}(P \parallel Q)$: por que falsos afastamentos custam caro e falsas aproximações são toleradas. Pausa Ativa 3.
5. **Bloco 3: A Solução da Cauda Pesada — t-SNE** (~20 min) — Por que o SNE gaussiano ainda falhava em 2D. A distribuição $t$-Student ($1$ grau de liberdade / Cauchy). Alívio da pressão de volume. Dinâmica de forças: atração por mola e repulsão eletrostática. Pausa Ativa 4.
6. **Bloco 4: Cuidados Práticos e as 4 Armadilhas de Interpretação** (~15 min) — Calibração da Perplexidade. As falácias: distâncias inter-cluster, tamanho aparente dos clusters, alucinação de clusters a partir de ruído, e a ausência de mapa paramétrico indutivo. Pausa Ativa 5.
7. **Fechamento** (~5 min) — Retomada das 5 perguntas centrais. O que fica em aberto. Ponte para a Parte 3 (Modelos Gráficos Probabilísticos e grafos de dependência).

---

## Fontes usadas — Aula 08

### Fonte 1: van der Maaten, L. & Hinton, G. (2008), "Visualizing Data using t-SNE", JMLR 9, 2579–2605
**Uso pretendido:** Definição do SNE simétrico, formulação do t-SNE com kernel $t$-Student, análise do *crowding problem* e cálculo do gradiente da divergência KL.
**Trecho:**
> "In high-dimensional space, we can have many data points that are all mutually equidistant. In two dimensions, this is impossible... The heavy tails of the Student-t distribution allow points that are only moderately distant in the high-dimensional space to be placed much farther apart in the low-dimensional map."

### Fonte 2: Hastie, T., Tibshirani, R., & Friedman, J. (2009), "The Elements of Statistical Learning" (ESL), Cap. 14 (§14.8 e §14.9)
**Uso pretendido:** Formulação matemática do Multidimensional Scaling (MDS), definição de *Stress* e contraste entre métodos métricos globais e abordagens não métricas/locais.
**Trecho:**
> "Multidimensional scaling attempts to preserve pairwise distances between data points... In doing so, large distances dominate the stress function, often obscuring subtle local clustering."

### Fonte 3: Wattenberg, M., Viégas, F., & Johnson, I. (2016), "How to Use t-SNE Effectively", Distill
**Uso pretendido:** Sistematização das armadilhas práticas de interpretação (perplexidade, distâncias entre aglomerados, densidade aparente e ausência de projeção paramétrica).
