# Respostas das Pausas Ativas — Aula 09

## Pausa Ativa 1: Regras de Associação e Antimonotonicidade

### Pergunta Aberta
**Pergunta:** Se um itemset composto por 3 produtos $\{Caf\acute{e}, Leite, P\tilde{a}o\}$ possui suporte de $15\%$ em uma base de 1 milhão de transações de supermercado, o que podemos afirmar matematicamente sobre o suporte do par $\{Caf\acute{e}, P\tilde{a}o\}$ e do itemset de 4 produtos $\{Caf\acute{e}, Leite, P\tilde{a}o, Manteiga\}$? Como essa propriedade geométrica permite ao algoritmo Apriori podar o espaço de busca exponencial?

**Discussão e Condução:**
O suporte de um conjunto de itens $I$ é a probabilidade empírica da interseção de eventos: $s(I) = P(\bigcap_{j \in I} X_j = 1)$.
Como a interseção de mais eventos nunca aumenta a probabilidade de ocorrência, temos a propriedade fundamental de **antimonotonicidade**: se $A \subseteq B$, então $s(A) \ge s(B)$.
Assim:
1. Para o subconjunto $\{Caf\acute{e}, P\tilde{a}o\} \subset \{Caf\acute{e}, Leite, P\tilde{a}o\}$, o suporte deve ser **pelo menos $15\%$** ($s \ge 0{,}15$).
2. Para o superconjunto $\{Caf\acute{e}, Leite, P\tilde{a}o, Manteiga\} \supset \{Caf\acute{e}, Leite, P\tilde{a}o\}$, o suporte pode ser **no máximo $15\%$** ($s \le 0{,}15$).
Essa assimetria é a espinha dorsal da poda do Apriori: se um conjunto de tamanho $k$ falha em atingir o limiar mínimo de suporte $s_{\min}$, **nenhum** de seus superconjuntos de tamanho $k+1, k+2, \dots$ poderá jamais atingir $s_{\min}$. Isso permite podar ramos inteiros da árvore de combinações ($2^D$ possíveis itemsets) sem precisar consultar o banco de dados.

### Bloco V/F
1. **Afirmação:** Se o itemset $\{A, B\}$ tem suporte de $0{,}05$, é matematicamente impossível que o item isolado $\{A\}$ tenha suporte inferior a $0{,}05$.
   - **Gabarito: V**.
   - **Justificativa:** Pela antimonotonicidade do suporte, $\{A\} \subset \{A, B\} \implies s(\{A\}) \ge s(\{A, B\}) = 0{,}05$.
2. **Afirmação:** Uma regra de associação com confiança de $100\%$ ($c(A \Rightarrow B) = 1{,}0$) garante que a compra do produto $A$ é a causa direta da compra do produto $B$.
   - **Gabarito: F**.
   - **Justificativa:** Confiança mede apenas a probabilidade condicional empírica $P(B \mid A)$. Se todos os clientes da loja compram $B$ (ex.: sacola plástica, $P(B) = 1{,}0$), a confiança $c(A \Rightarrow B)$ será $1{,}0$ mesmo que $A$ e $B$ sejam completamente independentes ou que $B$ não tenha relação causal alguma com $A$.
3. **Afirmação:** O espaço total de possíveis itemsets que podem ser formados a partir de um catálogo contendo $D$ produtos distintos escala linearmente com $D$.
   - **Gabarito: F**.
   - **Justificativa:** O espaço de subconjuntos é o conjunto das partes menos o conjunto vazio, que possui cardinalidade $2^D - 1$, escalando exponencialmente com $D$.
4. **Afirmação:** A métrica de suporte mede a probabilidade conjunta $P(A \cap B)$, enquanto a métrica de confiança mede a probabilidade condicional $P(B \mid A)$.
   - **Gabarito: V**.
   - **Justificativa:** Pela definição clássica de Agrawal et al. (1993), $s(A \Rightarrow B) = P(A \cap B)$ e $c(A \Rightarrow B) = P(A \cap B) / P(A) = P(B \mid A)$.

---

## Pausa Ativa 2: A Simetria do Lift e o Confounding

### Pergunta Aberta
**Pergunta:** Uma rede de drogarias constata que a regra $\{Fraldas\} \Rightarrow \{Cerveja\}$ apresenta $\text{Lift} = 2{,}5$, e a regra $\{Cerveja\} \Rightarrow \{Fraldas\}$ também apresenta exatamente $\text{Lift} = 2{,}5$. O que a igualdade estrita entre esses dois valores revela sobre a capacidade do *Lift* de indicar direcionalidade ou dependência causal? Se a variável oculta $\{Sexta\text{-}feira\ \grave{a}\ tarde\}$ duplicar as vendas de ambos os itens de forma independente, o que acontece com a dependência real entre eles?

**Discussão e Condução:**
Por definição, $\text{Lift}(A \Rightarrow B) = \frac{P(A \cap B)}{P(A)P(B)} = \frac{P(B \cap A)}{P(B)P(A)} = \text{Lift}(B \Rightarrow A)$. O *Lift* é uma métrica puramente comutativa e simétrica: ele quantifica o quanto a co-ocorrência observada se desvia da independência estatística global, mas é intrinsecamente incapaz de estabelecer qualquer direcionalidade ($A \to B$ vs. $B \to A$).
Além disso, se existe uma terceira variável contextual $C$ (como o horário de pico da sexta-feira) que atua como **causa comum** elevando as probabilidades marginais de ambos os itens de forma não correlacionada dentro de cada estrato, a agregação ingênua dos dados produz uma correlação espúria global ($\text{Lift} > 1$). Ao condicionar em $C$, a independência condicional pode ser restaurada: $P(A \cap B \mid C) = P(A \mid C) P(B \mid C)$, revelando que a associação empírica era puramente um artefato de confusão (*confounding*).

### Bloco V/F
1. **Afirmação:** Um valor de $\text{Lift}(A \Rightarrow B) = 1{,}0$ indica que a ocorrência de $A$ e a ocorrência de $B$ são estatisticamente independentes na base de dados.
   - **Gabarito: V**.
   - **Justificativa:** $\text{Lift} = \frac{P(A \cap B)}{P(A)P(B)} = 1{,}0 \iff P(A \cap B) = P(A)P(B)$, que é a definição clássica de independência estocástica.
2. **Afirmação:** Se $\text{Lift}(A \Rightarrow B) = 3{,}0$, então necessariamente a confiança da regra $c(A \Rightarrow B)$ é três vezes maior do que a confiança inversa $c(B \Rightarrow A)$.
   - **Gabarito: F**.
   - **Justificativa:** O Lift é simétrico ($\text{Lift}(A \Rightarrow B) = \text{Lift}(B \Rightarrow A) = 3{,}0$). As confianças dependem das probabilidades marginais: $c(A \Rightarrow B) = \text{Lift} \times P(B)$ e $c(B \Rightarrow A) = \text{Lift} \times P(A)$; se $P(A) = P(B)$, as duas confianças são idênticas.
3. **Afirmação:** O paradoxo de Simpson ocorre quando uma associação estatística observada em uma população agregada se inverte ou desaparece quando os dados são estratificados por uma variável confundidora.
   - **Gabarito: V**.
   - **Justificativa:** É a definição formal do paradoxo de Simpson: a correlação marginal entre duas variáveis pode ter sinal oposto à correlação condicional dentro de cada subgrupo definido por uma terceira variável.
4. **Afirmação:** Uma regra de associação com alto Lift e alta Confiança é imune a variáveis de confusão latentes, pois foi validada em toda a base de dados.
   - **Gabarito: F**.
   - **Justificativa:** Métricas baseadas em frequências marginais agregadas são especialmente vulneráveis a confundidores latentes; sem modelar a estrutura condicional, uma causa comum latente pode inflar arbitrariamente tanto o Lift quanto a Confiança.

---

## Pausa Ativa 3: Redes Bayesianas e Fatoração

### Pergunta Aberta
**Pergunta:** Considere um conjunto de $K=10$ variáveis binárias (por exemplo, 10 itens de um catálogo de compras). Quantos parâmetros de probabilidade independentes seriam necessários para especificar a distribuição conjunta completa $p(x_1, \dots, x_{10})$ sem nenhuma hipótese de independência? Se organizarmos essas variáveis em uma Rede Bayesiana onde cada nó tem no máximo 2 pais, quantos parâmetros tornam-se suficientes?

**Discussão e Condução:**
Sem simplificações, o espaço de estados de $10$ variáveis binárias possui $2^{10} = 1024$ configurações possíveis. Como a soma de todas as probabilidades deve ser igual a $1$, a distribuição conjunta completa exige $2^{10} - 1 = 1023$ parâmetros numéricos livres.
Sob uma Rede Bayesiana, a distribuição conjunta fatora como $p(x_1, \dots, x_{10}) = \prod_{k=1}^{10} p(x_k \mid \text{pa}_k)$.
Para cada nó $k$ que possui $m_k \le 2$ pais binários, a tabela de probabilidade condicional (CPT) exige especificar $P(x_k = 1 \mid \text{pa}_k)$ para cada uma das $2^{m_k} \le 4$ configurações dos pais.
Portanto, cada nó exige no máximo $2^2 = 4$ parâmetros livres. Para os $10$ nós juntos, precisamos de no máximo $10 \times 4 = 40$ parâmetros (na verdade, nós sem pais exigem apenas 1 parâmetro, e nós com 1 pai exigem 2).
A economia paramétrica é esmagadora: de $1023$ para no máximo $40$ números. Essa redução exponencial viabiliza a inferência e a estimativa estatística não supervisionada a partir de amostras de tamanho finito.

### Bloco V/F
1. **Afirmação:** Pela regra do produto da probabilidade, qualquer distribuição conjunta pode ser expressa como $p(x_1, \dots, x_K) = \prod_{k=1}^K p(x_k \mid x_1, \dots, x_{k-1})$ sem perda de generalidade.
   - **Gabarito: V**.
   - **Justificativa:** É a regra da cadeia da probabilidade (PRML eq. 8.1–8.2), válida para qualquer conjunto de variáveis aleatórias sem exigir nenhuma hipótese de independência.
2. **Afirmação:** Em uma Rede Bayesiana, a ausência de uma aresta direcionada entre dois nós nunca expressa uma restrição probabilística; trata-se apenas de uma conveniência visual.
   - **Gabarito: F**.
   - **Justificativa:** É exatamente a **ausência** de arestas que codifica as hipóteses de independência condicional que tornam o modelo tratável e reduzem a quantidade de parâmetros.
3. **Afirmação:** Um Grafo Acíclico Direcionado (DAG) permite ciclos direcionados desde que a probabilidade ao longo do ciclo seja menor que 1.
   - **Gabarito: F**.
   - **Justificativa:** A própria definição de DAG (*Directed Acyclic Graph*) proíbe rigorosamente qualquer ciclo direcionado ($A \to B \to \dots \to A$), pois ciclos violariam a ordenação topológica necessária para a regra da cadeia.
4. **Afirmação:** Para um nó binário $X$ com $m$ pais binários, o número de parâmetros independentes necessários na sua tabela de probabilidade condicional é $2^m$.
   - **Gabarito: V**.
   - **Justificativa:** Existem $2^m$ combinações possíveis dos valores dos pais; para cada combinação, especificar $P(X=1 \mid \text{pais})$ fixa automaticamente $P(X=0 \mid \text{pais}) = 1 - P(X=1 \mid \text{pais})$.

---

## Pausa Ativa 4: As Três Estruturas Canônicas e o Colisor

### Pergunta Aberta
**Pergunta:** Considere três variáveis binárias: $A$ (Choveu), $B$ (O regador automático de grama ligou) e $C$ (A grama está molhada). A física do problema dita que $A$ e $B$ ocorrem de forma independente ($A \perp\!\!\!\perp B$). No entanto, se você olhar pela janela e observar que a grama está molhada ($C=1$), e logo em seguida seu vizinho informar que o regador automático ligou com certeza ($B=1$), o que acontece com a sua crença a posteriori de que choveu ($A=1$)? Como esse fenômeno (conhecido como *explaining away*) distingue os colisores das cadeias e bifurcações?

**Discussão e Condução:**
Este é o clássico exemplo de **colisor (head-to-head / v-structure)**: $A \to C \leftarrow B$.
Marginalmente, $A$ e $B$ são independentes: saber que o regador ligou não altera em nada a probabilidade meteorológica de chuva ($P(A \mid B) = P(A)$).
Contudo, quando condicionamos no efeito comum observado $C=1$ (a grama está molhada), as duas causas disputam a explicação do fato. Se ficamos sabendo que $B=1$ (o regador ligou e já é suficiente para explicar a grama molhada), a necessidade de invocar a hipótese alternativa $A=1$ diminui consideravelmente: $P(A=1 \mid C=1, B=1) < P(A=1 \mid C=1)$.
Esse efeito é denominado **explaining away** (uma causa "explica e afasta" a outra).
Em cadeias ($A \to B \to C$) e bifurcações ($A \leftarrow B \to C$), condicionar no nó intermediário **bloqueia** o fluxo de informação e torna as pontas independentes. No colisor, ocorre exatamente o oposto: os nós nas pontas são independentes inicialmente, e condicionar no nó central **abre o canal e induz dependência**!

### Bloco V/F
1. **Afirmação:** Na estrutura em cadeia $A \to B \to C$, as variáveis $A$ e $C$ são marginalmente dependentes, mas tornam-se condicionalmente independentes dado $B$ ($A \perp\!\!\!\perp C \mid B$).
   - **Gabarito: V**.
   - **Justificativa:** Pelo PRML §8.2, $p(a, c \mid b) = p(a \mid b) p(c \mid b)$, o que prova que condicionar em $B$ bloqueia o caminho head-to-tail.
2. **Afirmação:** Na estrutura de causa comum $A \leftarrow B \to C$, condicionar em $B$ induz dependência espúria entre $A$ e $C$.
   - **Gabarito: F**.
   - **Justificativa:** É o oposto: $A$ e $C$ eram marginalmente dependentes devido à causa comum $B$; condicionar em $B$ bloqueia o caminho tail-to-tail e torna $A$ e $C$ independentes ($A \perp\!\!\!\perp C \mid B$).
3. **Afirmação:** Na estrutura de colisor $A \to C \leftarrow B$, as variáveis $A$ e $B$ são marginalmente independentes quando $C$ não é observado ($A \perp\!\!\!\perp B$).
   - **Gabarito: V**.
   - **Justificativa:** Como não há condicionamento em $C$ nem em seus descendentes, o caminho head-to-head está bloqueado, preservando a independência marginal $p(a, b) = p(a)p(b)$.
4. **Afirmação:** Se $C$ é um colisor no caminho entre $A$ e $B$, condicionar em um **descendente** de $C$ mantém o caminho bloqueado e preserva a independência de $A$ e $B$.
   - **Gabarito: F**.
   - **Justificativa:** Pelo critério de $d$-separação de Pearl (1988), condicionar em $C$ **ou em qualquer de seus descendentes** abre o colisor e torna $A$ e $B$ dependentes.

---

## Pausa Ativa 5: d-Separação e Equivalência de Markov

### Pergunta Aberta
**Pergunta:** Suponha que você possua um banco de dados transacional com 100 mil compras contendo três itens $A$, $B$ e $C$. Após testes estatísticos exaustivos de independência, você descobre que $A \perp\!\!\!\perp C \mid B$, e nenhuma outra independência existe. É possível determinar, apenas com esses dados observacionais e sem realizar intervenções no mercado, se a estrutura verdadeira do mundo é $A \to B \to C$, $A \leftarrow B \leftarrow C$ ou $A \leftarrow B \to C$? O que isso implica para a descoberta causal não supervisionada?

**Discussão e Condução:**
Essas três estruturas compartilham exatamente o mesmo esqueleto (as arestas não direcionadas $A - B - C$) e nenhuma delas possui colisores (v-structures).
Pelo teorema de Verma & Pearl (1990), dois DAGs pertencem à mesma **classe de equivalência de Markov (I-equivalência)** se e somente se:
1. Possuem o mesmo esqueleto não direcionado.
2. Possuem exatamente o mesmo conjunto de v-structures não blindadas (colisores onde os pais não possuem aresta direta entre si).
Como $A \to B \to C$, $A \leftarrow B \leftarrow C$ e $A \leftarrow B \to C$ codificam a mesmíssima declaração de independência condicional ($A \perp\!\!\!\perp C \mid B$), **nenhum algoritmo estatístico baseado puramente em dados observacionais passivos consegue diferenciá-las**.
Elas formam uma classe de equivalência de Markov que pode ser representada por um grafo misto essencial (CPDAG: $A - B - C$).
Isso demonstra um limite epistemológico formal do aprendizado não supervisionado: dados observacionais passivos conseguem identificar independências e correlações, mas a orientação das flechas causais sem colisores exige ou suposições a priori (como ordem temporal) ou intervenções ativas ($do$-calculus de Pearl).

### Bloco V/F
1. **Afirmação:** O critério de $d$-separação garante que, se todos os caminhos entre o conjunto de nós $A$ e o conjunto de nós $B$ estiverem bloqueados dado $C$, então $A$ e $B$ são condicionalmente independentes dado $C$ em qualquer distribuição que fature de acordo com o grafo.
   - **Gabarito: V**.
   - **Justificativa:** É o teorema fundamental da $d$-separação demonstrado por Pearl (1988) e detalhado em PRML §8.2.2.
2. **Afirmação:** A Cobertura de Markov (*Markov Blanket*) de um nó $X$ é composta exclusivamente pelo conjunto dos seus nós pais imediatos.
   - **Gabarito: F**.
   - **Justificativa:** A Cobertura de Markov $MB(X)$ é composta pelos pais de $X$, pelos filhos de $X$ e por todos os **outros pais dos filhos de $X$** (co-pais), que são necessários para bloquear os colisores induzidos pelos filhos.
3. **Afirmação:** Dois DAGs que possuem o mesmo esqueleto não direcionado e as mesmas v-structures geram o mesmo conjunto de independências condicionais.
   - **Gabarito: V**.
   - **Justificativa:** É o critério formal de classes de equivalência de Markov (I-equivalência) demonstrado por Verma & Pearl (1990).
4. **Afirmação:** A estrutura de colisor $A \to B \leftarrow C$ pertence à mesma classe de equivalência de Markov que a cadeia $A \to B \to C$.
   - **Gabarito: F**.
   - **Justificativa:** O colisor introduz uma v-structure que codifica a independência marginal $A \perp\!\!\!\perp C$ e dependência condicional $A \not\!\perp\!\!\!\perp C \mid B$, enquanto a cadeia codifica o oposto ($A \not\!\perp\!\!\!\perp C$ e $A \perp\!\!\!\perp C \mid B$). Elas são observacionalmente distinguíveis em dados.

