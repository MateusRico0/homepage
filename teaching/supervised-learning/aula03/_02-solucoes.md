# Soluções — Questões de Verdadeiro/Falso (Aula 3)

> Arquivo de apoio, não publicado (prefixo `_`). Contém a resposta e a
> justificativa de cada item das 12 questões de V/F do `index.qmd`. O
> `index.qmd` publicado continua sem solução — este arquivo existe só
> para conferência do professor/monitor, seguindo a metodologia de
> criação de questões definida em `../../CLAUDE.md`.

### Árvores como estimação não-paramétrica — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se, em vez de cortes alinhados aos eixos, uma árvore pudesse usar cortes ao longo de qualquer direção linear (hiperplanos oblíquos), mantendo a mesma lógica gulosa de escolher o corte que mais reduz $Q$, ela deixaria de ser um modelo não-paramétrico.

**Resposta:** Falso

**Justificativa:** O status de "não-paramétrico" não depende de os cortes serem alinhados aos eixos ou oblíquos — depende só de o número de parâmetros efetivos (regiões) crescer com $N$ em vez de ser fixado a priori. Uma árvore com cortes oblíquos, buscados gulosamente do mesmo jeito, ainda cresce região por região conforme os dados permitem; o aluno que marca Verdadeiro confunde uma propriedade estrutural incidental (geometria do corte) com a propriedade que de fato define paramétrico vs. não-paramétrico (dimensão de $\theta$ fixa vs. crescente).

### Árvores como estimação não-paramétrica — item (b)

**Heurística:** Limite

**Afirmação:** ✔ Se o número mínimo de pontos por folha for reduzido a $1$ e a profundidade máxima não for limitada, o número de parâmetros efetivos de uma árvore pode crescer até se igualar ao número de pontos de treino $N$.

**Resposta:** Verdadeiro

**Justificativa:** No extremo sem restrição nenhuma, a árvore pode isolar cada ponto de treino em sua própria folha — $N$ folhas, $N$ "parâmetros" (uma constante por folha). É exatamente esse extremo que caracteriza a árvore como não-paramétrica: nada no procedimento impede esse crescimento até o limite $N$.

### Árvores como estimação não-paramétrica — item (c)

**Heurística:** Transferência

**Afirmação:** ✗ Suponha que se queira usar uma árvore para modelar a distribuição conjunta completa $p(\mathbf{x}, y)$, não só a fronteira de decisão. Isso é possível diretamente com o mesmo procedimento de ajuste desta aula, sem nenhuma modificação.

**Resposta:** Falso

**Justificativa:** O procedimento desta aula nunca modela uma densidade de $\mathbf{x}$ — cada folha estima diretamente $p(\mathcal{C}_k\mid\mathbf{x})$ (ou $\mathbb{E}[t\mid\mathbf{x}]$), nunca $p(\mathbf{x})$ nem $p(\mathbf{x},y)$. Modelar a conjunta completa exigiria uma abordagem generativa (como as das Aulas 1–2), não uma adaptação trivial do algoritmo guloso. O aluno que marca Verdadeiro ignora a distinção generativo/preditivo estabelecida na Seção 2.

### Árvores como estimação não-paramétrica — item (d)

**Heurística:** Limite

**Afirmação:** ✔ Numa árvore com uma única folha (nenhum corte realizado), a estimativa em classificação se reduz à priori marginal $\hat\pi_k$ da amostra de treino, ignorando completamente $\mathbf{x}$.

**Resposta:** Verdadeiro

**Justificativa:** Com zero cortes, todo o conjunto de treino é uma única região; a proporção empírica de classes nessa região é, por definição, a priori marginal da amostra — não há dependência de $\mathbf{x}$ nesse caso degenerado. É o extremo oposto do item (b): a árvore mais simples possível já revela que a estimativa de folha é sempre "proporção dentro da região", que no caso trivial vira a marginal inteira.

### O estimador ótimo numa folha de regressão — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se, em vez de uma verossimilhança gaussiana, assumíssemos uma verossimilhança de Laplace (dupla exponencial) para os alvos de uma folha, o estimador de máxima verossimilhança de $y_\tau$ deixaria de ser a média amostral e passaria a ser a mediana amostral.

**Resposta:** Verdadeiro

**Justificativa:** A log-verossimilhança de Laplace é proporcional a $-\sum_n|t_n-y_\tau|/b$; maximizá-la equivale a minimizar $\sum_n|t_n-y_\tau|$, cujo minimizador é a mediana, não a média. Isso confirma que a escolha "prever a média" não é uma convenção universal — é uma consequência direta de ter assumido gaussiana; trocar a verossimilhança muda a métrica que está sendo minimizada, e portanto muda o estimador ótimo.

### O estimador ótimo numa folha de regressão — item (b)

**Heurística:** Limite

**Afirmação:** ✔ Se todos os $N_\tau$ alvos de uma folha forem idênticos entre si (variância zero), o valor mínimo de $Q_\tau$ é zero, e a log-verossimilhança gaussiana correspondente, no limite $\sigma^2\to 0$, tende a $+\infty$.

**Resposta:** Verdadeiro

**Justificativa:** Com $Q_\tau=0$, o termo $-\frac{1}{2\sigma^2}Q_\tau$ vale $0$ para qualquer $\sigma^2$, e a log-verossimilhança se reduz a $-\frac{N_\tau}{2}\ln(2\pi\sigma^2)$, que diverge para $+\infty$ quando $\sigma^2\to0^+$. É uma degenerescência real e conhecida da verossimilhança gaussiana em ajuste perfeito — o aluno que marca Falso provavelmente não testou o que acontece com a fórmula quando o segundo termo desaparece.

### O estimador ótimo numa folha de regressão — item (c)

**Heurística:** Limite

**Afirmação:** ✔ Uma folha com $N_\tau=1$ ainda define um $Q_\tau$ mínimo bem definido e igual a zero, mas a variância amostral desse único ponto não pode ser estimada de forma não-enviesada (o denominador $N_\tau - 1$ seria zero).

**Resposta:** Verdadeiro

**Justificativa:** Com um único ponto, $y_\tau=t_1$ e $Q_\tau=(t_1-t_1)^2=0$ — bem definido. Mas o estimador não-enviesado de variância, com denominador $N_\tau-1$, dá $0/0$, indefinido. Esse é o mesmo fato do viés do MLE de $\sigma^2$ (Seção 2) levado ao seu caso-limite mais extremo: com $N=1$ nem a versão enviesada nem a não-enviesada fazem sentido pleno.

### O estimador ótimo numa folha de regressão — item (d)

**Heurística:** Falsa equivalência

**Afirmação:** ✗ Como $Q_\tau$ e a variância amostral $\hat\sigma^2_\tau = Q_\tau/N_\tau$ diferem apenas por uma constante multiplicativa, qualquer corte que minimize $Q_\tau$ nas duas folhas geradas também minimiza, necessariamente, a variância combinada dessas folhas.

**Resposta:** Falso

**Justificativa:** A equivalência "$Q=N\cdot\text{variância}$" só vale para uma ÚNICA região de tamanho $N$ fixo — é exatamente o que a pausa ativa da Seção 3 estabeleceu para duas folhas de mesmo $N_\tau$. Mas cortes candidatos diferentes produzem folhas com $N_{\text{esq}}$ e $N_{\text{dir}}$ diferentes entre si; a "constante" que liga $Q$ e variância muda de candidato para candidato, então minimizar a soma de $Q$ (que já é ponderada implicitamente pelo tamanho de cada folha) não é o mesmo problema que minimizar alguma variância combinada não-ponderada. O erro é generalizar um fato válido para tamanhos fixos para uma comparação entre partições de tamanhos distintos.

### Crescimento guloso e sua miopia — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se o critério fosse "sempre aprofundar a folha mais numerosa" em vez de "maior redução de $Q$", o resultado seria idêntico ao crescimento guloso descrito na aula, já que a folha mais numerosa tende a ter o maior $Q$.

**Resposta:** Falso

**Justificativa:** O próprio quarto corte do exemplo de California Housing contradiz isso: entre as quatro folhas abertas, `LL` (132 pontos) e `LR` (255 pontos) eram maiores que `RL` (113 pontos), mas foi `RL` quem venceu, por oferecer a maior *redução* de $Q$ (${\approx}20{,}0$), não o maior tamanho. "Tende a" não é "sempre", e a aula já mostrou um contraexemplo concreto dentro do próprio material.

### Crescimento guloso e sua miopia — item (b)

**Heurística:** Limite

**Afirmação:** ✔ No limite em que o número mínimo de pontos por folha tende a zero, a busca exaustiva de limiares dentro de uma folha com $N_\tau$ pontos distintos passa a testar até $N_\tau - 1$ limiares candidatos.

**Resposta:** Verdadeiro

**Justificativa:** Os limiares candidatos são os pontos médios entre valores consecutivos distintos; com $N_\tau$ valores distintos há $N_\tau - 1$ desses intervalos. Sem um mínimo de pontos por folha filtrando candidatos inválidos, todos esses $N_\tau-1$ limiares tornam-se testáveis — é exatamente o que o código `melhor_corte` faz ao remover a checagem de `MIN_POR_FOLHA`.

### Crescimento guloso e sua miopia — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Se, em vez de um único alvo, tivéssemos alvos multivariados $\mathbf{t}\in\mathbb{R}^p$ e definíssemos $Q_\tau$ como a soma das somas de quadrados de cada componente, o mesmo algoritmo de busca exaustiva continuaria bem definido, sem alteração na lógica do Passo 2.

**Resposta:** Verdadeiro

**Justificativa:** O algoritmo do Passo 2 só precisa que $Q$ seja um número escalar comparável entre candidatos — de onde esse número vem (uma dimensão ou a soma de $p$ dimensões) é irrelevante para a lógica de "teste tudo, escolha o menor". Árvores de regressão multi-saída em bibliotecas reais funcionam exatamente assim, sem qualquer mudança estrutural no algoritmo de busca.

### Crescimento guloso e sua miopia — item (d)

**Heurística:** Falsa equivalência

**Afirmação:** ✗ Como a busca escolhe sempre o corte de menor $Q$ entre as duas folhas geradas, a árvore final construída por esse processo guloso é, necessariamente, a de menor $Q$ total entre todas as árvores com o mesmo número de folhas.

**Resposta:** Falso

**Justificativa:** Esta é a miopia do título do bloco, em forma de armadilha: otimizar cada passo localmente não garante o ótimo global entre todas as árvores com aquele número de folhas — um corte "ruim" agora pode ser o único caminho até uma árvore melhor lá na frente (é literalmente o argumento do Bloco 4/Seção de poda, "por que crescer grande e depois podar"). O aluno que marca Verdadeiro confunde "melhor decisão a cada passo" com "melhor resultado final".

### Entropia e informação mútua — item (a)

**Heurística:** Limite

**Afirmação:** ✔ Se uma variável $X$ tem $K$ resultados possíveis e é uniforme entre eles, sua entropia tende a $\ln K$ nats — e, no limite em que $K\to\infty$ mantendo a uniformidade, $H(X)\to\infty$.

**Resposta:** Verdadeiro

**Justificativa:** Para $p_k=1/K$ em todos os $K$ resultados, $H=-\sum_k \frac1K\ln\frac1K = \ln K$, que cresce sem limite conforme $K$ cresce. É um fato direto da fórmula, mas revela algo importante: ao contrário do índice de Gini (ver bloco seguinte), a entropia não tem teto — quanto mais categorias equiprováveis, maior a incerteza, sem limite superior.

### Entropia e informação mútua — item (b)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se $Y$ fosse uma função determinística e invertível de $X$ (conhecer $Y$ permite recuperar $X$ exatamente, e vice-versa), então $I(X;Y) = H(X) = H(Y)$.

**Resposta:** Verdadeiro

**Justificativa:** Invertibilidade determinística implica $H(Y\mid X)=0$ e $H(X\mid Y)=0$ (conhecer um determina o outro sem incerteza residual), logo $I(X;Y)=H(X)-H(X\mid Y)=H(X)$ e, simetricamente, $=H(Y)$. Como a transformação é bijetora, $H(X)=H(Y)$ também vale (entropia é invariante por relabeling). O caso extremo mostra que $I(X;Y)$ satura no maior valor possível exatamente quando a dependência é total e sem perdas — o oposto do caso de independência ($I=0$).

### Entropia e informação mútua — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Considere duas moedas honestas lançadas de forma totalmente independente, sem qualquer relação causal entre elas. Mesmo assim, numa amostra finita de $N$ lançamentos, a informação mútua empírica calculada a partir das frequências observadas dificilmente será exatamente zero, mesmo que a informação mútua populacional verdadeira seja zero.

**Resposta:** Verdadeiro

**Justificativa:** $I(X;Y)=0$ é uma propriedade da distribuição populacional verdadeira; as frequências observadas numa amostra finita quase certamente têm pequenos desvios amostrais em relação às proporções exatas de independência, e esses desvios se traduzem em informação mútua empírica estritamente positiva (ainda que pequena). É um lembrete importante e frequentemente ignorado: "$I=0$ na população" e "$I=0$ calculado numa amostra" não são a mesma afirmação.

### Entropia e informação mútua — item (d)

**Heurística:** Falsa equivalência

**Afirmação:** ✗ Como $I(X;Y)$ é sempre não-negativa e vale zero exatamente na independência, uma informação mútua alta necessariamente implica que $X$ causa $Y$ (ou vice-versa).

**Resposta:** Falso

**Justificativa:** Informação mútua mede associação estatística, não causalidade — é a mesma armadilha de "correlação não implica causação", vestida com o jargão certo da aula. O próprio exemplo de "grátis"/"ganhador" ilustra isso: as duas palavras são dependentes ($I>0$) por terem uma causa comum (a classe), sem que uma cause a outra diretamente.

### Ganho de informação e a conexão MLE categórico–entropia — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se, em vez de comparar $H(\hat p_\tau)$ com a **média ponderada** das entropias dos filhos, comparássemos com a MAIOR das duas entropias, o valor resultante ainda seria igual à informação mútua $I(S;\mathcal{C})$.

**Resposta:** Falso

**Justificativa:** A identidade $IG(\tau,s)=I(S;\mathcal{C})$ depende especificamente de o termo subtraído ser a entropia condicional $H(\mathcal{C}\mid S)$, que é, por definição, a **média ponderada** das entropias dos filhos (pelos tamanhos $N_{\text{esq}}/N_\tau$ e $N_{\text{dir}}/N_\tau$) — não o máximo, nem qualquer outra combinação. Trocar a média pelo máximo produz uma fórmula diferente, sem essa interpretação de informação mútua; o aluno que marca Verdadeiro não rastreou de onde vem a igualdade.

### Ganho de informação e a conexão MLE categórico–entropia — item (b)

**Heurística:** Limite

**Afirmação:** ✔ No caso extremo em que um corte separa perfeitamente as duas classes (ambas as folhas filhas ficam com $H=0$), o ganho de informação desse corte é exatamente igual a $H(\hat p_\tau)$ — o maior valor possível para aquele nó.

**Resposta:** Verdadeiro

**Justificativa:** Com os dois filhos puros, a média ponderada das entropias é $0$ (zero vezes qualquer peso é zero), então $IG=H(\hat p_\tau)-0=H(\hat p_\tau)$. Como entropia nunca é negativa, a média ponderada dos filhos nunca pode ser menor que $0$, então $H(\hat p_\tau)$ é de fato o teto de $IG$ para aquele nó — atingido exatamente na separação perfeita.

### Ganho de informação e a conexão MLE categórico–entropia — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Numa folha com 3 classes, em contagens $(10,10,10)$, o MLE categórico dessa folha ainda seria a proporção empírica $(1/3,1/3,1/3)$, com entropia dada pela mesma fórmula, agora somando sobre 3 termos.

**Resposta:** Verdadeiro

**Justificativa:** Nada na derivação do MLE categórico (Seção 5) é específico de duas classes — o argumento de maximização de $\ell_\tau$ vale para $K$ classes quaisquer, e o máximo continua sendo a proporção empírica de cada uma. A fórmula $H(p)=-\sum_k p_k\ln p_k$ já está escrita para $K$ genérico desde a Seção 4; o exemplo binário da aula foi só uma escolha de ilustração, não uma restrição do resultado.

### Ganho de informação e a conexão MLE categórico–entropia — item (d)

**Heurística:** Falsa equivalência

**Afirmação:** ✗ Como maximizar a log-verossimilhança categórica equivale a minimizar a entropia da folha, um corte que reduz a entropia de AMBAS as folhas filhas em relação à do pai necessariamente maximiza o ganho de informação entre todos os cortes candidatos disponíveis naquele nó.

**Resposta:** Falso

**Justificativa:** Reduzir a entropia em relação ao pai é uma melhoria em relação a NÃO cortar — mas não garante ser a *melhor* melhoria entre todos os candidatos testados. Pode existir outro corte, variável ou limiar, com uma redução (ponderada) ainda maior. Confundir "esse corte ajuda" com "esse corte é o argmax da busca" é o mesmo erro do item (a) do bloco de miopia, agora do lado da classificação.

### Entropia e Gini: forma e interpretação — item (a)

**Heurística:** Limite

**Afirmação:** ✗ À medida que o número de classes $K$ numa folha cresce, sempre mantendo a distribuição uniforme entre elas, tanto a entropia máxima $H=\ln K$ quanto o valor máximo do índice de Gini, $G=1-1/K$, crescem sem limite.

**Resposta:** Falso

**Justificativa:** $H=\ln K$ de fato cresce sem limite, mas $G=1-1/K$ é **limitado**: à medida que $K\to\infty$, $G\to 1$ e nunca ultrapassa esse teto. É uma diferença estrutural real entre as duas medidas (uma ilimitada, outra limitada em $[0,1)$) que a "mesma forma geral" no caso binário esconde — o aluno que marca Verdadeiro generalizou incorretamente uma semelhança válida só para $K=2$.

### Entropia e Gini: forma e interpretação — item (b)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se, em vez do índice de Gini, usássemos $G'(p)=\max_k p_k$ (a proporção da classe majoritária) como critério de impureza, um corte que produz duas folhas com $\max_k p_k$ idêntico teria impureza ponderada igual, mesmo que as distribuições internas das duas folhas fossem completamente diferentes fora da classe majoritária.

**Resposta:** Verdadeiro

**Justificativa:** Por definição, $G'$ só olha a proporção da classe majoritária — é cega a como as classes restantes se distribuem entre si. Duas folhas com a mesma "classe majoritária a 60%", por exemplo, podem ter o resto dividido de formas bem diferentes entre as demais classes, e $G'$ não capta essa diferença. É a mesma crítica que a aula faz à taxa de erro bruta, agora transferida para uma métrica hipotética com o mesmo ponto cego.

### Entropia e Gini: forma e interpretação — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Num problema de detecção de fraude com 99% de transações legítimas e 1% fraudulentas, uma folha que reproduz exatamente essa proporção tem entropia próxima do mínimo possível, mesmo antes de qualquer corte ser feito.

**Resposta:** Verdadeiro

**Justificativa:** $H(0{,}99)\approx 0{,}056$ nats — muito próximo de $0$ e longe do máximo $\ln 2\approx0{,}693$ em $p=0{,}5$. A entropia baixa aqui não vem de a árvore já ter cortado nada; vem só do desbalanceamento natural das classes. É um lembrete prático importante: entropia baixa numa folha grande e não cortada não significa "sem informação" — significa "já bastante previsível por composição".

### Entropia e Gini: forma e interpretação — item (d)

**Heurística:** Falsa equivalência

**Afirmação:** ✗ Como entropia e Gini se anulam numa folha pura e atingem o máximo em $p=0{,}5$ (caso binário), as duas medidas sempre concordam sobre qual, entre dois cortes candidatos, produz a maior redução de impureza.

**Resposta:** Falso

**Justificativa:** Compartilhar os mesmos extremos (zero na pureza, máximo em $p=0{,}5$) não implica concordar em toda a curva entre os extremos. Verificado numericamente: com contagens de pai $(20,20)$, o split $(17,13)\,|\,(3,7)$ tem Gini ponderado $0{,}4733$ e entropia ponderada $0{,}6659$, enquanto o split $(0,2)\,|\,(20,18)$ tem Gini $0{,}4737$ (pior, por pouco) e entropia $0{,}6572$ (melhor) — Gini prefere o primeiro, entropia prefere o segundo. As duas métricas usualmente concordam, mas "usualmente" não é "sempre".

### Por que não usar a taxa de erro bruta para crescer a árvore — item (a)

**Heurística:** Limite

**Afirmação:** ✔ Num nó com duas classes empatadas em número de pontos (proporção $50/50$), a taxa de erro do classificador majoritário é $0{,}5$ — o valor máximo possível dessa métrica, coincidindo com o ponto de máxima entropia e máximo Gini.

**Resposta:** Verdadeiro

**Justificativa:** Em $p=0{,}5$: taxa de erro $=1-\max(p,1-p)=0{,}5$ (seu teto, já que nunca se erra mais que metade prevendo a maioria); $H(0{,}5)=\ln2$ (seu máximo); $\text{Gini}(0{,}5)=0{,}5$ (seu máximo). As três métricas, que discordam em pontos intermediários (ver bloco anterior), coincidem exatamente nesse extremo — todas concordam que $p=0{,}5$ é o pior caso possível.

### Por que não usar a taxa de erro bruta para crescer a árvore — item (b)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se a taxa de erro bruta fosse o único critério de crescimento, e dois cortes candidatos produzissem a mesma taxa de erro ponderada, o algoritmo não teria como preferir um corte ao outro, nem mesmo quando um deles produz uma folha perfeitamente pura.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente o que o contraexemplo Split 1 vs. Split 2 desta aula demonstra numericamente: ambos empatam em erro ponderado $0{,}25$, mas só entropia e Gini enxergam que o Split 2 produz uma folha pura. Um critério de crescimento baseado só em erro bruto trataria os dois splits como equivalentes, perdendo a chance de crescer em direção à folha pura mais cedo.

### Por que não usar a taxa de erro bruta para crescer a árvore — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Considere um nó com 3 classes e contagens $(50,49,1)$. O classificador que sempre prevê a classe majoritária nesse nó erra em $50\%$ dos casos, mesmo a folha estando longe de ser uniformemente distribuída entre as 3 classes.

**Resposta:** Verdadeiro

**Justificativa:** Total $=100$, majoritária $=50$, erro $=1-50/100=0{,}5$. A taxa de erro não diferencia esse nó (bem desbalanceado, quase binário na prática, já que a terceira classe quase não existe) de um nó verdadeiramente equilibrado entre 3 classes — ela só enxerga "quem ganha e por quanto o resto perde", nunca a forma completa da distribuição. Generaliza para $K>2$ o mesmo ponto cego discutido no caso binário.

### Por que não usar a taxa de erro bruta para crescer a árvore — item (d)

**Heurística:** Falsa equivalência

**Afirmação:** ✗ Como a validação, na escolha de $\lambda$, usa a acurácia (equivalente à taxa de erro), conclui-se que entropia e Gini deixam de ter qualquer papel na fase de poda por custo-complexidade.

**Resposta:** Falso

**Justificativa:** São dois passos diferentes: o termo $Q_\tau(T)$ dentro de $C(T)=\sum_\tau Q_\tau(T)+\lambda|T|$, tal como calculado por `cost_complexity_pruning_path` do scikit-learn, usa a MESMA impureza (Gini, o critério padrão da árvore) usada para crescer — não a taxa de erro bruta. É só o passo externo de *escolher o valor de $\lambda$* que usa acurácia de validação. Confundir o critério interno de custo com o critério externo de seleção de hiperparâmetro é o erro deste item.

### Custo vs. complexidade e a poda — item (a)

**Heurística:** Limite

**Afirmação:** ✔ No limite em que $\lambda\to\infty$, o critério $C(T) = \sum_\tau Q_\tau(T) + \lambda|T|$ é minimizado por uma árvore com uma única folha.

**Resposta:** Verdadeiro

**Justificativa:** Conforme $\lambda\to\infty$, qualquer folha adicional além da primeira acrescenta uma penalidade que cresce sem limite, dominando qualquer redução possível em $\sum_\tau Q_\tau(T)$ (que é limitada inferiormente por $0$). O mínimo degenera para $|T|=1$: a raiz, sem nenhum corte.

### Custo vs. complexidade e a poda — item (b)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se a penalidade de complexidade fosse proporcional à profundidade da árvore em vez de ao número de folhas, duas árvores com o mesmo número de folhas mas formatos diferentes (uma bem desbalanceada, outra balanceada) poderiam receber penalidades diferentes sob esse critério alternativo, ao contrário do critério $C(T)$ usado na aula.

**Resposta:** Verdadeiro

**Justificativa:** $C(T)$, como definido na aula, depende só de $|T|$ (número de folhas) — duas árvores com o mesmo número de folhas recebem exatamente a mesma penalidade $\lambda|T|$, não importa o formato. Uma penalidade baseada em profundidade discriminaria entre elas (uma árvore desbalanceada pode ter profundidade maior que uma balanceada com o mesmo número de folhas), mostrando que a escolha de "o que penalizar" não é neutra.

### Custo vs. complexidade e a poda — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Numa tarefa de regressão em que os alvos $t$ passam a ser medidos numa escala muito maior (ex.: milhões em vez de milhares de dólares), o mesmo valor de $\lambda$ usado na escala original não produz, em geral, a mesma árvore podada na nova escala.

**Resposta:** Verdadeiro

**Justificativa:** $Q_\tau=\sum(t_n-y_\tau)^2$ escala quadraticamente com a unidade de $t$; multiplicar os alvos por $1000$ multiplica cada $Q_\tau$ por $10^6$, enquanto $\lambda|T|$ não muda. O mesmo $\lambda$ que antes competia de forma equilibrada com o custo passa a ser irrelevante (ou dominante, se a escala diminuir) na nova escala — $\lambda$ não é livre de unidade, um detalhe prático que a fórmula não deixa óbvio.

### Custo vs. complexidade e a poda — item (d)

**Heurística:** Falsa equivalência

**Afirmação:** ✗ Como $\sum_\tau Q_\tau(T)$ só pode diminuir (ou manter-se) conforme se adicionam folhas, e $\lambda|T|$ só pode aumentar, conclui-se que $C(T)$ é uma função estritamente convexa do número de folhas, com um único mínimo global bem definido.

**Resposta:** Falso

**Justificativa:** As duas premissas (custo não-crescente, penalidade crescente) estão corretas, mas a conclusão não segue: $C(T)$ não é sequer uma função de "número de folhas" isoladamente — várias árvores diferentes podem ter o mesmo $|T|$ com $Q_\tau(T)$ totais diferentes, então o domínio da minimização é o conjunto discreto de subárvores podáveis, não um eixo escalar contínuo. Somar uma sequência não-crescente com uma sequência crescente não produz automaticamente convexidade nem unicidade de mínimo sem hipóteses adicionais que não foram estabelecidas.

### Treino vs. validação: por que separar os dados — item (a)

**Heurística:** Limite

**Afirmação:** ✔ Se o conjunto de validação tivesse exatamente $0\%$ dos dados (todo o conjunto fosse usado como treino), a acurácia medida no que sobrasse para "validação" seria, no limite, idêntica à acurácia de treino.

**Resposta:** Verdadeiro

**Justificativa:** Com $0\%$ separado, o conjunto de "validação" coincide com o próprio conjunto de treino — medir desempenho nele é, por construção, medir desempenho nos mesmos dados usados para ajustar o modelo, o caso mais otimista possível descrito na caixa da aula.

### Treino vs. validação: por que separar os dados — item (b)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se a escolha do melhor $\lambda$ fosse feita usando a acurácia de TREINO em vez da de validação, o $\lambda$ escolhido tenderia a ser sistematicamente menor (menos poda) do que o escolhido por validação.

**Resposta:** Verdadeiro

**Justificativa:** A acurácia de treino é monotonicamente não-crescente à medida que $\lambda$ aumenta (a árvore encolhe e perde capacidade de memorizar o próprio treino) — o próprio gráfico da aula mostra isso. Otimizar só a acurácia de treino, portanto, empurraria a escolha para o menor $\lambda$ possível (a árvore mais completa, menos podada), sistematicamente diferente do ponto ótimo de validação, que aparece no meio da curva.

### Treino vs. validação: por que separar os dados — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Num cenário com apenas 40 pontos de treino disponíveis, reservar $40\%$ deles só para validação tem um custo prático mais sério do que reservar a mesma proporção de um conjunto de 40.000 pontos.

**Resposta:** Verdadeiro

**Justificativa:** Com 40 pontos, reservar $40\%$ deixa só 24 pontos para ajustar a árvore — pouquíssimo para estimar cortes e proporções de folha de forma confiável. Com 40.000 pontos, a mesma proporção ainda deixa 24.000 para o ajuste, mais do que suficiente na prática. O "custo de separar dados" mencionado na aula não é fixo — depende de quanto dado sobra depois do corte, e isso pesa muito mais em regimes de amostra pequena.

### Treino vs. validação: por que separar os dados — item (d)

**Heurística:** Falsa equivalência

**Afirmação:** ✗ Como o conjunto de validação nunca é usado para ajustar os cortes da árvore, o desempenho medido nele é uma estimativa não-enviesada do erro de generalização, mesmo que o próprio valor de $\lambda$ tenha sido escolhido observando exatamente esse mesmo conjunto.

**Resposta:** Falso

**Justificativa:** "Nunca usado para ajustar os cortes" garante só que a ÁRVORE em si não foi montada olhando a validação — mas se $\lambda$ foi escolhido justamente por maximizar a acurácia nesse conjunto, o par (árvore, $\lambda$) final foi, sim, otimizado em função dele, ainda que indiretamente. A acurácia de validação no $\lambda$ vencedor tende a ser levemente otimista por essa mesma razão — é por isso que a Aula 4 trata a escolha de hiperparâmetro e a estimativa final de erro como problemas relacionados, mas distintos.

### Splits alinhados aos eixos — item (a)

**Heurística:** Limite

**Afirmação:** ✔ No limite em que a profundidade tende a infinito, o erro de aproximação de uma fronteira diagonal por cortes alinhados aos eixos tende a zero, mas o número de folhas necessário para um erro menor que $\epsilon$ cresce sem limite à medida que $\epsilon\to0$.

**Resposta:** Verdadeiro

**Justificativa:** Uma escada de degraus cada vez menores pode se aproximar arbitrariamente de uma reta diagonal, mas nunca a alcança com um número finito de degraus — e o número de degraus necessário para uma tolerância $\epsilon$ cada vez menor cresce sem limite. É uma versão quantitativa do "nunca alcança exatamente" já discutido qualitativamente na aula.

### Splits alinhados aos eixos — item (b)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se a fronteira de decisão ótima entre duas classes fosse alinhada a um dos eixos originais (dependendo só de $x_1$, por exemplo), uma árvore poderia representá-la exatamente com um único corte, ao contrário do caso diagonal.

**Resposta:** Verdadeiro

**Justificativa:** É o espelho exato do argumento da aula: a limitação de "splits alinhados aos eixos" só aparece quando a fronteira verdadeira NÃO é alinhada aos eixos. Numa fronteira vertical ou horizontal, um único corte na variável certa reproduz a fronteira ótima sem qualquer erro de aproximação — o problema é específico da geometria do caso diagonal, não das árvores em geral.

### Splits alinhados aos eixos — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Considere um problema em que a fronteira ótima é um círculo centrado na origem. Uma árvore com cortes alinhados aos eixos pode aproximar essa fronteira com uma sequência de retângulos, mas nunca a representa exatamente com um número finito de cortes.

**Resposta:** Verdadeiro

**Justificativa:** A mesma limitação estrutural do caso diagonal (retas não alinhadas aos eixos) se aplica a qualquer fronteira curva: uma união finita de retângulos alinhados aos eixos nunca reproduz exatamente um círculo, só o aproxima cada vez melhor com mais cortes. O exemplo generaliza a lição da aula (só testada com uma reta) para uma fronteira não-linear.

### Splits alinhados aos eixos — item (d)

**Heurística:** Falsa equivalência

**Afirmação:** ✗ Como uma árvore com profundidade suficiente aproxima arbitrariamente bem qualquer fronteira, o número de folhas necessário para uma boa aproximação não depende da complexidade geométrica da fronteira verdadeira, só da profundidade escolhida.

**Resposta:** Falso

**Justificativa:** "Aproxima arbitrariamente bem, em princípio" não é o mesmo que "custa igual, na prática". Uma fronteira mais "enrugada" (mais curvatura, mais mudanças de direção) exige muito mais cortes para atingir a mesma tolerância de erro do que uma fronteira simples como uma única diagonal — a complexidade geométrica da fronteira verdadeira afeta diretamente o custo (número de folhas) da aproximação, não é irrelevante.

### Instabilidade estrutural — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se, em vez de escolher deterministicamente o corte de maior $IG$ (ou menor $Q$), o algoritmo escolhesse aleatoriamente entre os $k$ melhores cortes candidatos a cada rodada, a instabilidade da estrutura de uma árvore individual a pequenas mudanças no treino tenderia a diminuir.

**Resposta:** Falso

**Justificativa:** Injetar aleatoriedade na escolha do corte tende a tornar cada árvore individual **mais** variável, não menos — é exatamente o mecanismo por trás de florestas aleatórias (Aula 9), em que árvores individuais deliberadamente instáveis/decorrelacionadas são construídas para que a MÉDIA do conjunto (não uma árvore isolada) tenha variância menor. O aluno que marca Verdadeiro confunde "o ensemble fica mais estável" com "a árvore individual fica mais estável" — são afirmações diferentes.

### Instabilidade estrutural — item (b)

**Heurística:** Limite

**Afirmação:** ✔ No limite em que o conjunto de treino tem um número muito grande de pontos amostrados da mesma distribuição geradora, o corte escolhido na raiz se aproxima de um valor estável, e pequenas remoções de pontos deixam de mudar esse corte de forma perceptível.

**Resposta:** Verdadeiro

**Justificativa:** É um argumento assintótico razoável (não uma prova formal dada na aula, mas uma extrapolação natural): à medida que $N$ cresce, a estimativa empírica do melhor corte se aproxima do corte ótimo populacional, e remover uma pequena fração de pontos de uma amostra muito grande tem efeito cada vez mais desprezível sobre essa estimativa. É o oposto do regime demonstrado na aula (poucos pontos, alta sensibilidade), não uma contradição dele.

### Instabilidade estrutural — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Num conjunto de dados em que várias variáveis são fortemente correlacionadas entre si (quase redundantes para prever a classe), a instabilidade estrutural de uma árvore tende a ser maior do que em variáveis pouco correlacionadas.

**Resposta:** Verdadeiro

**Justificativa:** Quando duas variáveis carregam quase a mesma informação sobre a classe, a disputa entre elas na busca gulosa fica "quase empatada" — pequenas perturbações no treino podem inclinar a balança de uma para outra, mudando qual variável é escolhida no corte. Com variáveis pouco correlacionadas (como as duas gaussianas praticamente independentes do exemplo da aula), essa disputa raramente é tão apertada.

### Instabilidade estrutural — item (d)

**Heurística:** Falsa equivalência

**Afirmação:** ✗ Como a estrutura de uma árvore pode mudar substancialmente com a remoção de poucos pontos de treino, as previsões dessa árvore para a maioria dos pontos de teste também mudam substancialmente sempre que a estrutura muda.

**Resposta:** Falso

**Justificativa:** Instabilidade **estrutural** (qual variável/limiar é escolhido) e instabilidade **preditiva** (o quanto as previsões mudam) são coisas relacionadas, mas não equivalentes — trocar qual variável entra primeiro pode reorganizar a árvore sem mudar muito a região efetiva em que a maioria dos pontos cai, especialmente longe da fronteira que de fato se deslocou. Igualar as duas ignora essa distinção.

### Partição rígida e descontinuidades — item (a)

**Heurística:** Limite

**Afirmação:** ✔ À medida que o número de folhas de uma árvore de regressão cresce sem limite, o tamanho de cada descontinuidade entre folhas vizinhas tende a diminuir, mas a partição continua sendo, em qualquer profundidade finita, uma função em degraus.

**Resposta:** Verdadeiro

**Justificativa:** Mais folhas significam degraus mais estreitos e saltos menores entre eles (como a figura da senoide já sugeria), mas a estrutura fundamental — cada ponto pertence a exatamente uma folha, com um valor constante ali — nunca deixa de existir em profundidade finita. O limite "melhora" o ajuste sem jamais alcançar a suavidade de uma função verdadeiramente contínua.

### Partição rígida e descontinuidades — item (b)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se, em vez de prever a média constante em cada folha, a árvore previsse uma reta local ajustada por mínimos quadrados dentro de cada folha, as descontinuidades entre folhas vizinhas desapareceriam automaticamente, sem qualquer restrição adicional.

**Resposta:** Falso

**Justificativa:** Trocar "constante por folha" por "reta por folha" (uma árvore de modelo linear) não muda o fato de que a **partição continua rígida** — cada ponto ainda pertence a exatamente uma folha, com sua própria reta ajustada independentemente das vizinhas. Nada garante que as retas de duas folhas adjacentes coincidam exatamente na fronteira entre elas; a menos que essa continuidade seja imposta explicitamente como restrição extra, o salto na fronteira persiste, só que agora entre duas retas em vez de dois patamares constantes.

### Partição rígida e descontinuidades — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Na aplicação de precificação de imóveis desta aula (California Housing), dois imóveis com `MedInc` quase idêntico, mas de lados opostos de um limiar de corte, podem receber previsões de preço bastante diferentes, mesmo sendo quase indistinguíveis em todo o resto.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente a consequência prática da rigidez da partição aplicada ao próprio exemplo já construído nesta aula: dois pontos a uma distância mínima em `MedInc`, um de cada lado do limiar $4{,}8973$ da raiz, caem em folhas diferentes (com médias de folha bem distintas, como `1{,}68` de um lado e `3{,}21` do outro nas primeiras folhas) — a previsão salta de um patamar para outro sem transição, apesar dos imóveis serem quase idênticos.

### Partição rígida e descontinuidades — item (d)

**Heurística:** Falsa equivalência

**Afirmação:** ✗ Como a rigidez da partição é a mesma característica que permite à árvore modelar interações não-lineares sem exigir que sejam especificadas de antemão, conclui-se que a rigidez da partição não tem nenhuma desvantagem prática relevante.

**Resposta:** Falso

**Justificativa:** É exatamente o contrário do que a Seção de Limites conclui: a mesma característica estrutural (partição em regiões distintas) traz a vantagem (capturar interações sem especificá-las) E a desvantagem (descontinuidades onde a função verdadeira é suave) ao mesmo tempo — uma não anula a outra. Concluir "sem desvantagem relevante" a partir de "tem uma vantagem" é precisamente o tipo de generalização apressada que a síntese final da aula ("nenhum dos dois extremos é gratuito") avisa para não fazer.

