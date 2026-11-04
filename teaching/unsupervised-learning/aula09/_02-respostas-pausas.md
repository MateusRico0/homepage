# Respostas das Pausas — Aula 09

## Pausa 1: O Espaço Binário e a Ruptura Métrica

### Pergunta Aberta
**Pergunta:** Considere três clientes em um e-commerce com catálogo de $D=10$ produtos:
- Cliente 1 comprou apenas $\{Caf\acute{e}\}$;
- Cliente 2 comprou apenas $\{Torradeira\}$;
- Cliente 3 comprou $\{Caf\acute{e}, Leite, P\tilde{a}o, Manteiga, Queijo, Biscoito, Fruta, Iogurte, Suco, Ch\acute{a}\}$ (todos os outros 9 itens, menos Torradeira).

Calcule a distância euclidiana $\|\mathbf{x}_1 - \mathbf{x}_2\|$ e compare com $\|\mathbf{x}_1 - \mathbf{x}_3\|$. O que esse resultado revela sobre a utilidade de distâncias euclidianas para comparar hábitos de compras?

**Discussão e Condução:**
Para vetores binários $\mathbf{x} \in \{0, 1\}^D$:
- $\|\mathbf{x}_1 - \mathbf{x}_2\|^2 = (1-0)^2 + (0-1)^2 + 0 = 2 \implies \|\mathbf{x}_1 - \mathbf{x}_2\| = \sqrt{2} \approx 1{,}41$.
- Para o Cliente 3, ele coincide com o Cliente 1 no item Café, mas discorda nos outros 8 itens:
  $\|\mathbf{x}_1 - \mathbf{x}_3\|^2 = (1-1)^2 + 8 \times (0-1)^2 = 8 \implies \|\mathbf{x}_1 - \mathbf{x}_3\| = \sqrt{8} \approx 2{,}83$.

Geometricamente, o Cliente 1 é considerado "muito mais próximo" do Cliente 2 ($\sqrt{2}$) do que do Cliente 3 ($\sqrt{8}$). No entanto, do ponto de vista do consumo, o Cliente 1 e o Cliente 3 compartilham a compra de itens matinais (ambos compraram Café), enquanto o Cliente 2 comprou um eletrodoméstico completamente desvinculado.
A distância euclidiana penaliza severamente o volume total da cesta (tamanho do vetor), sendo incapaz de medir afinidade ou complementaridade de consumo em dados esparsos.

### Bloco V/F
1. **Afirmação:** A distância euclidiana entre dois vetores de compra binários penaliza igualmente a ausência conjunta de um item e a presença discordante de um item.
   - **Gabarito: F**.
   - **Justificativa:** Ausência conjunta resulta em $(0-0)^2 = 0$, não somando à distância. Contudo, em catálogos grandes e esparsos, a vasta maioria dos pares de clientes tem distância euclidiana idêntica ($\sqrt{|t_1| + |t_2|}$), tornando a métrica inútil para discriminar afinidades.
2. **Afirmação:** Em um catálogo de $D=50$ produtos, o número total de possíveis cestas distintas de compras é superior a $10^{15}$.
   - **Gabarito: V**.
   - **Justificativa:** O número de subconjuntos possíveis é $2^D - 1 = 2^{50} - 1 \approx 1{,}12 \times 10^{15}$.
3. **Afirmação:** Se duas variáveis $A$ e $B$ apresentam $\text{Lift}(A \Rightarrow B) > 1$ em uma base transacional agregada, é matematicamente impossível que elas sejam condicionalmente independentes dado um terceiro fator $C$.
   - **Gabarito: F**.
   - **Justificativa:** O Paradoxo de Simpson comprova exatamente o oposto: se $C$ for uma causa comum latente ($A \leftarrow C \to B$), o Lift agregado na população pode ser expressivamente maior que $1$, enquanto o Lift estratificado em cada estrato de $C$ é rigorosamente igual a $1{,}0$.
4. **Afirmação:** Modelos baseados em gradiente contínuo e projeções ortogonais podem ser aplicados diretamente a matrizes binárias esparsas sem perdas conceituais ou semânticas.
   - **Gabarito: F**.
   - **Justificativa:** Espaços discretos $\{0, 1\}^D$ violam os pressupostos de suavidade e continuidade de variedades Riemannianas; projeções ortogonais produzem vetores de números reais contínuos que não possuem interpretação transacional válida.

---

## Pausa 2: Suporte, Confiança e a Falácia da Simetria

### Pergunta Aberta
**Pergunta:** Em uma grande loja de departamentos, descobriu-se que a regra $\{Tablet\} \Rightarrow \{Sacola\ Pl\acute{a}stica\}$ possui confiança $c = 1{,}0$ ($100\%$) e $\text{Lift} = 1{,}05$. Por outro lado, a regra $\{Sacola\ Pl\acute{a}stica\} \Rightarrow \{Tablet\}$ possui o mesmo $\text{Lift} = 1{,}05$, mas confiança de apenas $0{,}002$ ($0{,}2\%$).
Como o mesmo Lift pode coexistir com confianças tão radicalmente opostas? O que aconteceria se a loja decidisse dar desconto em sacolas plásticas esperando alavancar a venda de tablets?

**Discussão e Condução:**
Por definição analítica:
$$c(A \Rightarrow B) = \frac{P(A \cap B)}{P(A)} = \text{Lift}(A \Rightarrow B) \times P(B)$$
O *Lift* é uma métrica estritamente simétrica:
$$\text{Lift}(A \Rightarrow B) = \frac{P(A \cap B)}{P(A)P(B)} = \text{Lift}(B \Rightarrow A)$$
No entanto, a confiança depende da probabilidade marginal do consequente. Como a sacola plástica é comprada por quase todos os clientes da loja ($P(Sacola) \approx 0{,}95$), qualquer produto $A$ terá $c(A \Rightarrow Sacola) \approx 1{,}00$. 
Por outro lado, tablets são itens raros ($P(Tablet) \approx 0{,}002$), resultando em uma confiança ínfima no sentido inverso.
A política de dar desconto em sacolas esperando atrair compradores de tablets fracassará por completo: a associação é assimétrica e o Lift próximo de $1{,}0$ atesta que sacolas e tablets são marginalmente quase independentes.

### Bloco V/F
1. **Afirmação:** Pela propriedade de antimonotonicidade, se o itemset $\{P\tilde{a}o, Caf\acute{e}\}$ tem suporte de $0{,}30$, o item isolado $\{P\tilde{a}o\}$ tem suporte maior ou igual a $0{,}30$.
   - **Gabarito: V**.
   - **Justificativa:** Teorema 1 ($A \subseteq B \implies s(B) \le s(A)$). Como $\{P\tilde{a}o\} \subset \{P\tilde{a}o, Caf\acute{e}\}$, seu suporte é no mínimo $0{,}30$.
2. **Afirmação:** A confiança $c(A \Rightarrow B)$ é uma métrica simétrica, satisfazendo sempre $c(A \Rightarrow B) = c(B \Rightarrow A)$.
   - **Gabarito: F**.
   - **Justificativa:** Confiança mede probabilidades condicionais direcionadas $P(B \mid A)$ e $P(A \mid B)$, que diferem pela razão das probabilidades marginais $P(B)/P(A)$.
3. **Afirmação:** Se um produto $B$ for comprado em $90\%$ de todas as transações de uma loja, qualquer regra $A \Rightarrow B$ terá confiança mínima de $90\%$, mesmo que $A$ e $B$ sejam completamente independentes.
   - **Gabarito: V**.
   - **Justificativa:** Se $A \perp\!\!\!\perp B$, então $c(A \Rightarrow B) = P(B \mid A) = P(B) = 0{,}90$. A confiança elevada é um artefato da popularidade de $B$.
4. **Afirmação:** Um valor de $\text{Lift}(A \Rightarrow B) = 3{,}0$ prova que comprar $A$ causa diretamente um aumento de $300\%$ nas vendas de $B$.
   - **Gabarito: F**.
   - **Justificativa:** O Lift quantifica apenas a co-ocorrência observada relativa à independência na base agregada; ele não estabelece causalidade e é vulnerável a causas comuns latentes.

---

## Pausa 3: A Poda do Apriori e a Mineração Prática

### Pergunta Aberta
**Pergunta:** Suponha que no nível 2 o algoritmo Apriori identificou como frequentes os seguintes pares:
$L_2 = \{\{A, B\}, \{A, C\}, \{A, D\}, \{B, C\}, \{B, D\}\}$.
Note que o par $\{C, D\}$ **não** atingiu o suporte mínimo e foi descartado.

No nível 3, o passo de junção gera o candidato $\{A, B, C, D\}$? Se sim ou se não, quais candidatos de tamanho 3 sobrevivem ao passo de poda?

**Discussão e Condução:**
No nível 3, o Apriori une pares de $L_2$ que compartilham o primeiro item:
- $\{A, B\}$ e $\{A, C\} \implies \{A, B, C\}$. Subconjuntos de tamanho 2: $\{A, B\}, \{A, C\}, \{B, C\}$. Todos pertencem a $L_2$. O candidato $\{A, B, C\}$ **sobrevive à poda**.
- $\{A, B\}$ e $\{A, D\} \implies \{A, B, D\}$. Subconjuntos: $\{A, B\}, \{A, D\}, \{B, D\}$. Todos pertencem a $L_2$. O candidato $\{A, B, D\}$ **sobrevive à poda**.
- $\{A, C\}$ e $\{A, D\} \implies \{A, C, D\}$. Subconjuntos: $\{A, C\}, \{A, D\}, \{C, D\}$. Como $\{C, D\} \notin L_2$, o candidato $\{A, C, D\}$ é **imediatamente descartado no passo de poda**, sem necessidade de ler nenhuma transação do disco!
- $\{B, C\}$ e $\{B, D\} \implies \{B, C, D\}$. Subconjuntos: $\{B, C\}, \{B, D\}, \{C, D\}$. Como $\{C, D\} \notin L_2$, é **descartado**.
O candidato $\{A, B, C, D\}$ tem tamanho 4 e sequer é avaliado no nível 3; se fosse gerado no nível 4, conteria $\{C, D\}$ e seria podado instantaneamente.

### Bloco V/F
1. **Afirmação:** No algoritmo Apriori, o passo de poda (*prune step*) exige varrer novamente o banco de dados em disco para checar a frequência dos subconjuntos.
   - **Gabarito: F**.
   - **Justificativa:** O passo de poda consulta exclusivamente a tabela $L_{k-1}$ já carregada na memória principal (RAM); não há nenhuma operação de I/O em disco.
2. **Afirmação:** Se um candidato de tamanho 3 tem um subconjunto de tamanho 2 que não está em $L_2$, ele é descartado imediatamente pela antimonotonicidade.
   - **Gabarito: V**.
   - **Justificativa:** Pela antimonotonicidade, se um subconjunto é infrequente, o superconjunto obrigatoriamente será infrequente.
3. **Afirmação:** O algoritmo Apriori garante encontrar todos os itemsets frequentes da base de dados para o limiar $s_{\min}$ escolhido.
   - **Gabarito: V**.
   - **Justificativa:** O Apriori é um algoritmo exato e completo: a propriedade de poda descarta apenas candidatos que matematicamente não poderiam ser frequentes.
4. **Afirmação:** Se uma base transacional contiver $1$ milhão de compras, o Apriori realizará $1$ milhão de varreduras na base de dados.
   - **Gabarito: F**.
   - **Justificativa:** O número de passadas pelo banco de dados é igual ao tamanho do maior itemset frequente mais um ($k_{\max} + 1$), tipicamente entre 3 e 6 varreduras completas.

---

## Pausa 4: As Geometrias Canônicas como Filtro de Regras

### Pergunta Aberta
**Pergunta:** Considere três variáveis: $A$ (Ocorreu um terremoto), $B$ (Houve uma tentativa de assalto) e $C$ (O alarme da casa tocou). Terremotos e assaltos são independentes na natureza ($A \perp\!\!\!\perp B$).
Se você estiver viajando e receber uma notificação de que o alarme tocou ($C=1$), e dez segundos depois ouvir no rádio que um terremoto acabou de ocorrer na sua cidade ($A=1$), o que acontece com a probabilidade de que sua casa tenha sido assaltada ($B=1$)?

**Discussão e Condução:**
Esta estrutura forma um **colisor (head-to-head)**: $A \to C \leftarrow B$.
Marginalmente, $A$ e $B$ são independentes ($P(B \mid A) = P(B)$).
Quando recebemos a informação de que o alarme tocou ($C=1$), a probabilidade a posteriori de um assalto sobe substancialmente ($P(B=1 \mid C=1) > P(B=1)$).
No entanto, ao descobrirmos que ocorreu um terremoto ($A=1$), o terremoto explica de forma convincente o disparo do alarme. Essa confirmação "explica e afasta" a hipótese concorrente, fazendo com que a probabilidade de assalto despenque:
$$P(B=1 \mid C=1, A=1) < P(B=1 \mid C=1)$$
Esse é o fenômeno de **explaining away**: condicionar em um efeito comum observado introduz uma correlação estatística entre suas causas independentes. Em mineração de dados, condicionar em subamostras filtradas por um efeito comum induz regras artificiais espúrias entre variáveis não correlacionadas.

### Bloco V/F
1. **Afirmação:** Na cadeia $A \to B \to C$, condicionar no nó intermediário $B$ torna $A$ e $C$ condicionalmente independentes ($A \perp\!\!\!\perp C \mid B$).
   - **Gabarito: V**.
   - **Justificativa:** Condicionar no intermediário bloqueia o canal *head-to-tail*.
2. **Afirmação:** Na causa comum $A \leftarrow B \to C$, condicionar em $B$ induz dependência espúria entre $A$ e $C$.
   - **Gabarito: F**.
   - **Justificativa:** Condicionar na causa comum $B$ elimina a correlação espúria e restaura a independência condicional ($A \perp\!\!\!\perp C \mid B$).
3. **Afirmação:** No colisor $A \to C \leftarrow B$, as causas $A$ e $B$ são marginalmente independentes sem nenhum condicionamento ($A \perp\!\!\!\perp B$).
   - **Gabarito: V**.
   - **Justificativa:** Sem condicionar no colisor $C$, o caminho está naturalmente bloqueado e as causas são independentes.
4. **Afirmação:** Se $C$ for um colisor entre $A$ e $B$, condicionar no nó $C$ (ou em qualquer de seus descendentes) mantém o caminho bloqueado.
   - **Gabarito: F**.
   - **Justificativa:** Condicionar no colisor **ou em qualquer de seus descendentes** abre o canal e induz dependência estatística entre $A$ e $B$.

---

## Pausa 5: Componentes do Grafo e o Teto Observacional

### Pergunta Aberta
**Pergunta:** Suponha que, analisando 500 mil transações de varejo com os produtos $A$, $B$ e $C$, seus testes estatísticos comprovem rigorosamente que $A \perp\!\!\!\perp C \mid B$, e nenhuma outra independência exista. É possível afirmar apenas com esses dados se $A$ causa $B$ ou se $B$ causa $A$? O que seria necessário fazer na loja para desvendar a seta com certeza científica?

**Discussão e Condução:**
Os DAGs $A \to B \to C$, $A \leftarrow B \leftarrow C$ e $A \leftarrow B \to C$ codificam exatamente a mesma e única declaração de independência condicional: $A \perp\!\!\!\perp C \mid B$.
Pelo Teorema de Verma & Pearl (1990), essas três estruturas compartilham o mesmo esqueleto ($A - B - C$) e nenhuma possui v-structures, pertencendo à mesma **classe de equivalência de Markov (I-equivalência)**. Suas distribuições conjuntas observadas são matematicamente indistinguíveis.
Portanto, é impossível orientar a seta apenas com dados observacionais passivos.
Para determinar a relação causal com certeza científica, é indispensável uma **intervenção ativa**: por exemplo, alterar artificialmente o preço ou a oferta do item $B$ (aplicando o operador $do(B)$ via teste A/B) e medir se essa intervenção altera a distribuição de compra de $A$ e de $C$.

### Bloco V/F
1. **Afirmação:** O Apriori fornece o esqueleto inicial de conexões frequentes, enquanto os testes locais de independência condicional podam regras espúrias e atalhos transitivos.
   - **Gabarito: V**.
   - **Justificativa:** Essa é a estratégia computacionalmente tratável de aprendizado de estrutura baseada em restrições (como no algoritmo PC).
2. **Afirmação:** Dois DAGs com o mesmo esqueleto e as mesmas v-structures pertencem à mesma classe de equivalência de Markov e são indistinguíveis por dados puramente observacionais.
   - **Gabarito: V**.
   - **Justificativa:** Teorema de Verma & Pearl (1990); ambos produzem exatamente as mesmas independências condicionais.
3. **Afirmação:** O grafo de colisor $A \to B \leftarrow C$ gera a mesma distribuição de independência condicional que a cadeia $A \to B \to C$.
   - **Gabarito: F**.
   - **Justificativa:** O colisor é observacionalmente único: ele gera independência marginal ($A \perp\!\!\!\perp C$) e dependência condicional ($A \not\perp\!\!\!\perp C \mid B$), ao passo que a cadeia gera o oposto.
4. **Afirmação:** Apenas com dados passivos de compras de supermercado, sem qualquer experimento ativo ($do(x)$), é sempre possível determinar a direção de causa e efeito de todas as arestas do grafo.
   - **Gabarito: F**.
   - **Justificativa:** Dados puramente observacionais identificam apenas o Grafo Essencial (CPDAG); a orientação causal de arestas reversíveis exige intervenção ativa ou premissas temporais externas.
