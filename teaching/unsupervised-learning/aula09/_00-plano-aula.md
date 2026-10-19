## Resumo — Aula 09

A aula inaugura a **Parte 3: Descoberta de Informação e Estruturas em Grande Escala**, estabelecendo a transição de espaços contínuos e métricos (Parte 2) para a descoberta não supervisionada de estruturas de dependência em dados discretos, categóricos e esparsos. Iniciamos pela mineração clássica de itens frequentes e regras de associação (*market basket analysis*), formalizando analiticamente as métricas de Suporte, Confiança e *Lift*, bem como o princípio de antimonotonicidade do algoritmo Apriori. Em seguida, revelamos as graves limitações dessas heurísticas: a simetria ingênua do *Lift* e sua cegueira perante variáveis de confusão latentes (causas comuns e paradoxo de Simpson). Para resolver essa deficiência teórica, introduzimos os **Modelos Gráficos Probabilísticos Direcionados (Redes Bayesianas)**, provando como a topologia do grafo fatora a distribuição conjunta $p(\mathbf{x}) = \prod_k p(x_k \mid \text{pa}_k)$. Dissecamos as três estruturas canônicas de 3 nós (cadeia, bifurcação e colisor), deduzimos o critério geral de **$d$-separação** de Pearl (1988) e o conceito de Cobertura de Markov (*Markov Blanket*), e encerramos com os limites epistemológicos da inferência puramente observacional: classes de equivalência de Markov (I-equivalência).

**Estratégia Pedagógica:** A (Outside-In) — Modelo mental prático de transações e regras de associação $\to$ Falha do *Lift* em discernir direcionalidade e correlações espúrias $\to$ Teoria formal de Redes Bayesianas e fatoração conjunta $\to$ Critério de $d$-separação e estruturas canônicas $\to$ Síntese de limites observacionais e I-equivalência.

**Datasets e Cenários-Fio:**
1. *Transações de Cesta de Compras (Market Basket)*: conjunto esparso binário $\{Caf\acute{e}, Leite, P\tilde{a}o, Filtro, Ch\acute{a}\}$ cruzado com variável temporal/contextual $\{Manh\tilde{a}\}$ para demonstrar empiricamente a quebra de regras espúrias sob estratificação condicional.
2. *Adult Census Income* (`scikit-learn/adult-census-income`): dados categóricos socioeconômicos para ilustrar como atributos binários e discretos se estruturam em grafos direcionados de dependência condicional.

---

## Plano de aula — Aula 09 (carga horária: 90–100 min)

1. **Revisão e Introdução** (~10 min) — Transição do espaço contínuo/latente (t-SNE, VAE) para variáveis categóricas e dados transacionais esparsos. Por que contar co-ocorrências não basta. Problema motivador: a regra ilusória com alto *Lift*. Pausa Ativa 1.
2. **Intuição — O Mercado, as Cestas e a Ilusão da Associação Direta** (~10 min) — A intuição de regras de associação no varejo. Co-ocorrência como reflexo de hábitos e horários, e não de atração causal mútua.
3. **Bloco 1: Mineração de Itens Frequentes — Suporte, Confiança e Lift** (~15 min) — Formalização de itens e transações como vetores binários $\mathbf{x} \in \{0, 1\}^D$. Definição formal de Suporte, Confiança e *Lift*. A propriedade de antimonotonicidade do suporte ($A \subseteq B \implies s(A) \ge s(B)$) e a poda do Apriori. A falácia da simetria: por que $\text{Lift}(A \Rightarrow B) = \text{Lift}(B \Rightarrow A)$ falha em indicar direção. Pausa Ativa 2.
4. **Bloco 2: Redes Bayesianas e a Fatoração da Distribuição Conjunta** (~15 min) — Grafos Acíclicos Direcionados (DAGs) como modelos generativos para variáveis discretas. A regra do produto e a simplificação por pais: $p(x_1, \dots, x_K) = \prod_{k=1}^K p(x_k \mid \text{pa}_k)$. Economia paramétrica exponencial: de $2^K - 1$ probabilidades livres para somas locais limitadas pelos graus de entrada. Pausa Ativa 3.
5. **Bloco 3: Independência Condicional e as Três Estruturas Canônicas** (~20 min) — As três geometrias fundamentais de fluxo de probabilidade:
   - *Cadeia (Head-to-tail):* $A \to B \to C \implies A \perp\!\!\!\perp C \mid B$. O intermediário bloqueia o canal.
   - *Bifurcação / Causa Comum (Tail-to-tail):* $A \leftarrow B \to C \implies A \perp\!\!\!\perp C \mid B$. O condicionamento na causa comum dissipa a correlação espúria.
   - *Colisor / Efeito Comum (Head-to-head):* $A \to C \leftarrow B$. Marginalmente independentes ($A \perp\!\!\!\perp B$), mas condicionalmente dependentes dado $C$ (*explaining away*). Pausa Ativa 4.
6. **Bloco 4: d-Separação Geral, Cobertura de Markov e Equivalência de Markov** (~15 min) — O critério formal de $d$-separação (Pearl, 1988) para conjuntos arbitrários de nós. Definição da Cobertura de Markov (*Markov Blanket*): pais, filhos e outros pais dos filhos. O que dados observacionais conseguem e não conseguem revelar: I-equivalência (classes de equivalência de Markov que compartilham o mesmo esqueleto e as mesmas v-structures não blindadas). Pausa Ativa 5.
7. **Fechamento** (~5 min) — Retomada das 5 perguntas da aula. O que fica em aberto (aprendizado de estrutura NP-difícil, inferência causal sem intervenção). Ponte para a Aula 10 (Fatoração de Matrizes: SVD e NMF para Sistemas de Recomendação).

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

### Fonte 3: Pearl, J. (1988 / 2000), "Probabilistic Reasoning in Intelligent Systems" e "Causality"
**Uso pretendido:** O conceito de *explaining away* em colisores, formalização da semântica de $d$-separação e limites da equivalência observacional de Markov (I-equivalência).
**Trecho:**
> "Two event tend to become conditionally dependent given their common effect, even though they are marginally independent... Conditioning on a common consequence creates a spurious dependency between its otherwise independent causes."

