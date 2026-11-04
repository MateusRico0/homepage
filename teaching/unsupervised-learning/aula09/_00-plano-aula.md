## Resumo — Aula 09

A aula inaugura a **Parte 3: Descoberta de Informação e Estruturas em Grande Escala**, estabelecendo uma **ruptura epistemológica** em relação à Parte 2: abandonamos os espaços contínuos e métricos $\mathbb{R}^D$ (onde distâncias e projeções operavam) e adentramos o universo de dados discretos, categóricos e transações binárias esparsas $\mathbf{x} \in \{0, 1\}^D$. Nesses domínios, distâncias euclidianas perdem o sentido físico e o objetivo passa a ser a **descoberta de estruturas de dependência e co-ocorrência**.

Apresentamos formal e praticamente a mineração clássica de itens frequentes e regras de associação (*market basket analysis*): definimos Suporte, Confiança e *Lift*, demonstramos a propriedade de antimonotonicidade do suporte e detalhamos o **algoritmo Apriori completo** (passo de junção $L_{k-1} \bowtie L_{k-1}$, passo de poda por subconjuntos e geração de regras com confiança mínima), executando-o em dados reais.

Em seguida, revelamos as graves limitações dessas heurísticas empíricas: a simetria comutativa do *Lift* ($\text{Lift}(A \Rightarrow B) \equiv \text{Lift}(B \Rightarrow A)$) e sua incapacidade de distinguir relações diretas de correlações espúrias geradas por variáveis de confusão latentes (Paradoxo de Simpson). Para superar esse teto, introduzimos os **Modelos Gráficos Probabilísticos Direcionados (Redes Bayesianas)**, provando como a topologia de um DAG fatora a distribuição conjunta $p(\mathbf{x}) = \prod_k p(x_k \mid \text{pa}_k)$ gerando economia paramétrica exponencial. Dissecamos as três estruturas canônicas de 3 nós (cadeia, bifurcação e colisor com *explaining away*), deduzimos o critério geral de **$d$-separação** de Pearl (1988) e a Cobertura de Markov (*Markov Blanket*). Encerramos estabelecendo o limite epistemológico da inferência puramente observacional: classes de equivalência de Markov (I-equivalência), provando por que dados passivos não determinam causalidade sem intervenções experimentais.

**Estratégia Pedagógica:** A (Outside-In) — Ruptura do espaço contínuo $\to$ Algoritmo Apriori e mineração prática de regras $\to$ Limitações do *Lift* e o Paradoxo de Simpson $\to$ Teoria formal de Redes Bayesianas e fatoração conjunta $\to$ Critério de $d$-separação e estruturas canônicas $\to$ Síntese dos limites da inferência observacional e I-equivalência.

**Datasets e Cenários-Fio:**
1. *Transações de Varejo (Market Basket)*: base esparsa de compras com itens de supermercado ($\{P\tilde{a}o, Leite, Caf\acute{e}, Manteiga, Cerveja, Fralda\}$) minerada pelo Apriori, cruzada com variável de confusão $\{Perfil\}$ para evidenciar analítica e graficamente a quebra do *Lift*.
2. *Adult Census Income* (`scikit-learn/adult-census-income`): dados categóricos socioeconômicos para ilustrar a fatoração de dependências em DAGs discretos.

---

## Plano de aula — Aula 09 (carga horária: 90–100 min)

1. **Revisão e Introdução** (~10 min) — A Ruptura de Paradigma: o fracasso do espaço contínuo $\mathbb{R}^D$ em dados categóricos e transações esparsas $\{0, 1\}^D$. Por que distâncias euclidianas não funcionam para compras. Ideia Central em 4 passos: (1) Mineração de co-ocorrências, (2) O problema da validade dos padrões empíricos, (3) O teste da probabilidade condicional, (4) O DAG de dependências com exemplo concreto no varejo. Problema motivador: a regra ilusória do Café e da Torradeira com alto Lift ($2{,}69$). Pausa 1.
2. **Intuição — O Mercado, a Cesta e a Explosão Combinatória** (~10 min) — Espaço de busca exponencial $2^D - 1$. A imagem mental do funil de frequências e a necessidade de podas inteligentes.
3. **Bloco 1: Mineração de Itens Frequentes — Suporte, Confiança e Antimonotonicidade** (~15 min) — Formalização de itens e transações como vetores binários. Definição formal de Suporte $s(I)$. Teorema da Antimonotonicidade do suporte ($A \subseteq B \implies s(B) \le s(A)$) e demonstração analítica. Definição de Confiança e *Lift*. A falácia da comutatividade do Lift ($\text{Lift}(A \Rightarrow B) \equiv \text{Lift}(B \Rightarrow A)$). Pausa 2.
4. **Bloco 2: O Algoritmo Apriori na Prática** (~15 min) — Rastreamento passo a passo com uma mini-base de 5 transações logo na abertura: contagem em $L_1$ eliminando a Cerveja na raiz; geração de pares $C_2 \to L_2$; o passo de junção de candidatos de 3 itens com prefixo comum ($L_2 \bowtie L_2$); o passo de poda (*pruning*) descartando $\{Leite, Manteiga, Pão\}$ em memória RAM antes de tocar o disco; e critério de parada ($L_3 = \emptyset$). Geração de regras de associação e filtro de confiança mínima. Aplicação prática em Python com extração da tabela real de regras. Pausa 3.
5. **Bloco 3: Redes Bayesianas como Filtro Estrutural de Regras** (~20 min) — O DAG como mapa de dependências e a fatoração conjunta $p(\mathbf{x}) = \prod_k p(x_k \mid \text{pa}_k)$. As três geometrias canônicas do fluxo de informação como filtros estruturais práticos para regras do Apriori:
   - *Causa Comum (Tail-to-tail):* $A \leftarrow B \to C \implies A \perp\!\!\!\perp C \mid B$. Descarte de regras diretas espúrias (resolução do Paradoxo de Simpson).
   - *Cadeia (Head-to-tail):* $A \to B \to C \implies A \perp\!\!\!\perp C \mid B$. Poda de atalhos transitivos redundantes.
   - *Colisor (Head-to-head):* $A \to C \leftarrow B$. Marginalmente independentes ($A \perp\!\!\!\perp B$), mas dependentes dado $C$ (*explaining away*). Alerta contra viés de seleção ao condicionar em subamostras. Pausa 4.
6. **Bloco 4: Montando o Grafo e os Limites dos Dados Observacionais** (~15 min) — Construção do Grafo Essencial (CPDAG) via validação e montagem de componentes locais (esqueleto via Apriori $\to$ testes locais de independência condicional $\to$ orientação de colisores unívocos). Exemplo prático rastreando 6 regras brutas do Apriori ($R, C, T, P, M$), podando a causa comum espúria ($C-T$) e a transitividade redundante ($P-C$) para montar o DAG limpo de 4 dependências essenciais. Limites epistemológicos: Teorema de I-Equivalência de Markov (Verma & Pearl, 1990). Por que dados puramente observacionais passivos não provam causalidade sem intervenções experimentais ativas ($do(x)$, teste A/B). Pausa 5.
7. **Fechamento** (~5 min) — Síntese: Apriori como gerador de candidatos + PGMs como filtro e validador de componentes. Retomada das 4 perguntas da aula. O que fica em aberto (aprendizado de estrutura global NP-difícil, variáveis latentes não observadas). Ponte para a Aula 10 (Sistemas de Recomendação: Fatoração de Matrizes com SVD e NMF).

---

## Fontes usadas — Aula 09

### Fonte 1: Bishop, C. M. (2006), "Pattern Recognition and Machine Learning" (PRML), Cap. 8 (§8.1 e §8.2, pp. 360–383)
**Uso pretendido:** Definição formal de Redes Bayesianas direcionadas, fatoração da probabilidade conjunta sob grafos acíclicos direcionados (DAGs), independência condicional, demonstração analítica das 3 estruturas canônicas e o critério de $d$-separação geral (Pearl, 1988).
**Trecho:**
> "Indeed, one of the powerful aspects of graphical models is that a specific graph can make probabilistic statements for a broad class of distributions... In general, the joint distribution is given by the product of these conditional distributions over all nodes in the graph: $p(\mathbf{x}) = \prod_{k=1}^K p(x_k \mid \text{pa}_k)$." (§8.1, p. 362)
> "A path is said to be blocked if it includes a node such that either (a) the arrows on the path meet either head-to-tail or tail-to-tail at the node, and the node is in the set C, or (b) the arrows meet head-to-head at the node, and neither the node, nor any of its descendants, is in the set C. If all paths are blocked, then A is said to be d-separated from B by C..." (§8.2.2, p. 378)

### Fonte 2: Hastie, T., Tibshirani, R., & Friedman, J. (2009), "The Elements of Statistical Learning" (ESL), Cap. 14 (§14.2, pp. 487–493)
**Uso pretendido:** Formalização de regras de associação, dados de cestas de compras (*market basket analysis*), métricas de Suporte e Confiança, e a propriedade de antimonotonicidade do suporte no algoritmo Apriori.
**Trecho:**
> "Association rule analysis has emerged as a popular tool for mining commercial data bases. The goal is to find joint values of the variables $X = (X_1, \dots, X_p)$ that appear most frequently in the data base... Any item set $L$ consisting of a subset of the items in $K$ must have support greater than or equal to that of $K$, $L \subseteq K \implies T(L) \ge T(K)$." (§14.2 e §14.2.2, pp. 487, 490)

### Fonte 3: Agrawal, R., & Srikant, R. (1994), "Fast Algorithms for Mining Association Rules in Large Databases", VLDB, pp. 487–499
**Uso pretendido:** Formalização do algoritmo Apriori, etapas de Candidate Generation ($C_k = L_{k-1} \bowtie L_{k-1}$), passo de poda de subconjuntos (*Apriori pruning*) e geração sistemática de regras.
**Trecho:**
> "Apriori algorithm generates the candidate itemsets to be counted in a pass by using only the itemsets found large in the previous pass—without considering the transactions in the database... In the join step, $L_{k-1}$ is joined with $L_{k-1}$ to generate candidate itemsets $C_k$... In the prune step, any candidate itemset $c \in C_k$ that has a subset of size $k-1$ that is not in $L_{k-1}$ is deleted."

### Fonte 4: Pearl, J. (1988 / 2000), "Probabilistic Reasoning in Intelligent Systems" e "Causality"
**Uso pretendido:** O conceito de *explaining away* em colisores, formalização da semântica de $d$-separação e limites da equivalência observacional de Markov (I-equivalência e Verma & Pearl, 1990).
**Trecho:**
> "Two events tend to become conditionally dependent given their common effect, even though they are marginally independent... Conditioning on a common consequence creates a spurious dependency between its otherwise independent causes."
