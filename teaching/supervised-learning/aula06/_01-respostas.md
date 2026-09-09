# Gabarito — Aula 6

Gabarito consolidado: justificativa analítica de cada item de V/F dos
exercícios finais (`index.qmd`) e a solução discutida de cada pausa
ativa da aula. Nunca publicado no site (prefixo `_`).

## Pausas Ativas

### Pausa 1 — Antes de Ajustar: O que "Melhor Reta" Já Pressupõe?

**Pergunta motivadora:** Se eu te desse duas retas diferentes, ambas
passando "no meio" da nuvem de pontos, como você decidiria qual é
"melhor" sem fazer nenhuma conta?

**Discussão:** "Melhor" não pode significar apenas "passa perto da
média" — qualquer reta que passe pelo ponto médio $(\bar x,\bar y)$ tem
soma de desvios (sem elevar ao quadrado) exatamente zero, mesmo retas
absurdas, giradas em ângulos que claramente não acompanham a nuvem.
Duas retas com o mesmo ponto médio podem ter inclinações completamente
diferentes e tratar os desvios de forma muito distinta. Um critério
"melhor reta" só é informativo se penalizar desvios de um jeito que
distinga retas boas de ruins — é isso que a soma de quadrados resolve.

**V/F resolvido:**
- ✗ Duas retas que passam pelo mesmo ponto médio $(\bar x,\bar y)$ da nuvem de dados são necessariamente igualmente boas, pois ambas capturam a tendência central dos dados.
- ✔ Se todos os pontos da nuvem estivessem exatamente sobre uma única reta (sem nenhum ruído), qualquer critério razoável de "melhor reta" apontaria para essa mesma reta.
- ✗ Um termostato que prevê a temperatura de amanhã a partir da de hoje enfrenta a mesma estrutura de "melhor reta", mas isso não implica que a inclinação ótima seja necessariamente próxima de 1.
- ✔ Julgar "melhor reta" pela soma dos desvios (sem quadrado, sem valor absoluto) é degenerado: qualquer reta pela média $(\bar x,\bar y)$ tem soma de desvios zero, inclusive retas absurdas.

---

### Pausa 2 — Projeção, Resíduos e Equações Normais

**Pergunta motivadora:** Geometricamente, por que o vetor de resíduos
$y-\hat y$ ser ortogonal ao subespaço gerado pelas colunas de $X$ é
exatamente a condição que caracteriza a MELHOR aproximação, e não uma
coincidência do cálculo?

**Discussão:** Não é coincidência — é Pitágoras. Mover $\hat y$ para
qualquer outro ponto do subespaço $\mathcal S$ só pode *aumentar* a
distância $\lVert y-\hat y\rVert$, porque qualquer deslocamento dentro
de $\mathcal S$ soma um termo estritamente positivo à distância ao
quadrado. Ortogonalidade é a única forma de $\hat y$ não deixar
"sobra" evitável dentro do subespaço — é exatamente essa condição que
as equações normais ($X^T(y-X\hat\beta)=0$) impõem algebricamente.

**V/F resolvido:**
- ✔ Minimizar $\lVert y-X\beta\rVert^2$ e minimizar $\lVert y-X\beta\rVert$ produzem o mesmo $\hat\beta$, porque a raiz quadrada é estritamente crescente em distâncias não-negativas.
- ✔ Se as colunas de $X$ forem linearmente dependentes, $X^TX$ deixa de ser invertível e $\hat\beta$ perde unicidade — mas a projeção $\hat y=X\hat\beta$ continua bem definida e única.
- ✗ Num sistema de recomendação com perfis latentes linearmente dependentes, a lógica de projeção continua valendo, mas a unicidade de $\hat\beta$ não — a mesma ressalva do item anterior.
- ✗ Ortogonalidade ao subespaço $\mathcal S$ não implica resíduo nulo — só implica que o resíduo não tem componente dentro de $\mathcal S$; se $y\notin\mathcal S$ (o caso típico com ruído real), o resíduo é não-nulo e ainda assim ortogonal a $\mathcal S$.

---

### Pausa 3 — Premissas do Ruído Gaussiano Homocedástico

**Pergunta motivadora:** Se a variância do ruído crescesse conforme a
renda mediana aumenta — imóveis mais caros têm preços mais
"espalhados" — o que exatamente, na construção da verossimilhança de
hoje, deixaria de valer?

**Discussão:** O símbolo que ganharia um índice $n$ é justamente
$\sigma^2$ — de uma constante única para uma função $\sigma^2(x_n)$
que varia por observação. A fatoração da verossimilhança conjunta em
produto de densidades individuais sobrevive (ainda depende só da
suposição de independência, não de homocedasticidade), mas a forma de
cada fator muda: cada termo carregaria seu próprio $\sigma(x_n)$, e a
log-verossimilhança teria $\ln\sigma(x_n)$ dentro do somatório, em vez
de um único $N\ln\sigma$ fatorado para fora.

**V/F resolvido:**
- ✔ Se $\sigma^2$ dependesse de $x_n$, a verossimilhança conjunta ainda seria produto das densidades individuais (assumindo independência), mas cada fator teria sua própria variância $\sigma^2(x_n)$.
- ✔ No limite $\sigma^2\to0$, a densidade gaussiana se concentra inteiramente sobre o valor predito, e o modelo probabilístico se aproxima do caso determinístico sem ruído.
- ✗ Verificar homocedasticidade num sensor não garante nada sobre outro sensor, nem do mesmo fabricante — a suposição nunca "generaliza de graça", exige checagem individual.
- ✗ A estimativa de mínimos quadrados continua sendo uma escolha razoável mesmo sem normalidade exata (ela minimiza RSS por construção); o que se perde sem normalidade é a interpretação como MLE, não a validade do ponto estimado.

---

### Pausa 4 — OLS = MLE: O Que a Prova Realmente Diz

**Pergunta motivadora:** A busca numérica encontrou exatamente o mesmo
$\hat\beta$ que a fórmula fechada, a menos de $10^{-8}$. Isso prova que
maximizar a log-verossimilhança SEMPRE encontra o mínimo de RSS, para
qualquer distribuição de ruído — ou é uma coincidência do caso
gaussiano?

**Discussão:** É uma propriedade do caso gaussiano especificamente — a
prova do Bloco 3 usou explicitamente a forma exponencial-quadrática
$\exp\{-(\cdot)^2/2\sigma^2\}$ da densidade gaussiana, num passo
específico da derivação (isolar o termo em $\beta$). Trocar o ruído
assumido por outra distribuição (Laplace, por exemplo) produziria
outra função de erro a minimizar pela mesma lógica geral — mas não a
mesma soma de quadrados. A confirmação numérica é uma verificação
empírica sobre um dataset específico com um otimizador que convergiu
corretamente, não uma prova matemática geral; a prova matemática é a
derivação algébrica do Bloco 3.

**V/F resolvido:**
- ✔ Se o ruído fosse Laplace em vez de gaussiano, maximizar a verossimilhança levaria a minimizar a soma dos valores absolutos dos resíduos, não a soma de quadrados.
- ✔ No limite $N\to\infty$ com modelo verdadeiramente linear e gaussiano, $\hat\beta_{\text{MLE}}$ e $\hat\sigma^2_{\text{MLE}}$ convergem para os valores populacionais, e o viés relativo de $\hat\sigma^2_{\text{MLE}}$ desaparece assintoticamente.
- ✗ Comparar log-verossimilhanças máximas entre famílias distribucionais diferentes (gaussiana vs. Bernoulli) não é válido sem correção (AIC/BIC) — as escalas não são diretamente comparáveis.
- ✗ Confirmar numericamente para um dataset e um otimizador que convergiu corretamente não estende a garantia a qualquer otimizador (um que não converge não chegaria ao mesmo ponto).

## Exercícios de V/F

### Geometria da Projeção e Resíduos — item (a)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Se o vetor observado $y$ já estivesse exatamente dentro do subespaço gerado pelas colunas de $X$ (por exemplo, se os dados não tivessem ruído algum), a projeção $\hat y$ coincidiria com o próprio $y$, e o resíduo seria o vetor nulo.

**Resposta:** Verdadeiro

**Justificativa:** A projeção ortogonal de um vetor sobre um subespaço que já o contém é o próprio vetor — não há "sobra" fora do subespaço para descartar, então o resíduo é nulo.

### Geometria da Projeção e Resíduos — item (b)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Se o número de colunas de $X$ (incluindo o intercepto) fosse igual ao número de observações $N$, e essas colunas fossem linearmente independentes, o subespaço $\mathcal S$ ocuparia todo o espaço $\mathbb R^N$, e o ajuste por mínimos quadrados reproduziria $y$ exatamente, com resíduo nulo em todos os pontos.

**Resposta:** Verdadeiro

**Justificativa:** $N$ colunas linearmente independentes em $\mathbb R^N$ geram o espaço inteiro; a projeção de qualquer $y\in\mathbb R^N$ sobre $\mathbb R^N$ é o próprio $y$ — é o caso degenerado de interpolação perfeita (zero graus de liberdade sobrando).

### Geometria da Projeção e Resíduos — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Num algoritmo de recomendação que aproxima as avaliações de um usuário como combinação linear de "perfis latentes" pré-definidos, a mesma lógica de projeção ortogonal sobre o subespaço gerado pelos perfis garante que a aproximação encontrada terá erro zero sempre que houver pelo menos dois perfis latentes disponíveis.

**Resposta:** Falso

**Justificativa:** Ter "pelo menos dois" perfis não garante que o vetor de avaliações esteja dentro do subespaço que eles geram — erro zero só ocorre se o vetor alvo pertencer exatamente a esse subespaço, o que depende da dimensão do subespaço relativa à dimensão do problema, não de uma contagem mínima arbitrária de perfis.

### Geometria da Projeção e Resíduos — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como o resíduo $y-\hat y$ é ortogonal a cada coluna de $X$ individualmente, ele é necessariamente ortogonal a qualquer vetor fora do subespaço $\mathcal S$ também.

**Resposta:** Falso

**Justificativa:** Ortogonalidade às colunas de $X$ garante ortogonalidade a todo o subespaço $\mathcal S$ que elas geram (por linearidade) — mas nada garante ortogonalidade a um vetor arbitrário fora de $\mathcal S$, que pode ter componentes em qualquer direção.

### RSS, Equações Normais e Posto de X — item (a)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Se todas as colunas de atributos de $X$ (exceto o intercepto) fossem multiplicadas por uma mesma constante $c\ne 0$ antes do ajuste, o vetor $\hat\beta$ mudaria (os coeficientes correspondentes seriam divididos por $c$), mas a previsão $\hat y=X\hat\beta$ e o RSS mínimo permaneceriam exatamente os mesmos.

**Resposta:** Verdadeiro

**Justificativa:** Reescalar uma coluna por $c$ e dividir o coeficiente correspondente por $c$ deixa o produto $X\beta$ inalterado — a reta ajustada e a soma de quadrados mínima não dependem da escala escolhida para os atributos.

### RSS, Equações Normais e Posto de X — item (b)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ No limite em que $X$ tem uma única coluna (só o intercepto, sem nenhum atributo), a equação normal $X^T(y-X\hat\beta)=0$ se reduz a dizer que $\hat\beta_0$ é exatamente a média amostral $\bar y$.

**Resposta:** Verdadeiro

**Justificativa:** Com $X$ sendo um vetor de uns, a equação normal vira $\mathbf 1^T(y-\hat\beta_0\mathbf 1)=0$, ou seja, $\sum(y_n-\hat\beta_0)=0$, cuja solução é exatamente $\hat\beta_0=\bar y$.

### RSS, Equações Normais e Posto de X — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Num ajuste de calibração de instrumento, a mesma equação normal determinaria os coeficientes independentemente do tipo de sensor, e a extrapolação da reta ajustada para leituras muito fora do intervalo calibrado teria a mesma confiabilidade estatística que dentro do intervalo calibrado.

**Resposta:** Falso

**Justificativa:** A equação normal de fato não depende do tipo físico do sensor — mas extrapolar para fora do intervalo onde os dados de calibração existiram nunca tem a mesma confiabilidade estatística que interpolar dentro dele; não há garantia de que a relação linear observada continue válida fora da faixa observada.

### RSS, Equações Normais e Posto de X — item (d)

**Heurística:** Caso limite/extremo

**Afirmação:** ✗ Como $\text{RSS}(\beta)$ é uma função quadrática (e portanto convexa) de $\beta$, ela tem sempre um único mínimo global estritamente, mesmo quando as colunas de $X$ são linearmente dependentes ($X^TX$ singular).

**Resposta:** Falso

**Justificativa:** $\text{RSS}(\beta)$ é sempre convexa, mas só é **estritamente** convexa quando $X^TX$ é não-singular (posto completo). Quando $X^TX$ é singular, existe um subespaço inteiro de vetores $\beta$ que atingem o mesmo valor mínimo de RSS — o mínimo deixa de ser único, mesmo continuando global.

### Premissas do Modelo Gaussiano Homocedástico — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se assumíssemos que os erros $\epsilon_n$ são gaussianos mas NÃO independentes entre observações, a verossimilhança conjunta deixaria de ser simplesmente o produto das densidades marginais de cada observação.

**Resposta:** Verdadeiro

**Justificativa:** A fatoração da densidade conjunta como produto de densidades individuais é consequência direta da suposição de independência — sem ela, a densidade conjunta exigiria modelar a estrutura de correlação entre observações, não apenas suas marginais.

### Premissas do Modelo Gaussiano Homocedástico — item (b)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Se a variância do ruído $\sigma^2$ fosse igual para todas as observações mas extremamente grande (tendendo a infinito), o modelo linear perderia praticamente toda sua capacidade preditiva, mesmo que $\beta$ estivesse corretamente especificado.

**Resposta:** Verdadeiro

**Justificativa:** Com $\sigma^2\to\infty$, a distribuição condicional de $Y$ dado $X$ se torna cada vez mais dispersa em torno da média correta $\beta^TX$ — o valor médio previsto continua certo, mas a incerteza em torno dele domina completamente qualquer previsão individual útil.

### Premissas do Modelo Gaussiano Homocedástico — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Num modelo que prevê o tempo de resposta de um servidor a partir da carga de requisições, supor ruído gaussiano homocedástico seria razoável se a variabilidade não dependesse da carga, e essa suposição nunca precisaria ser verificada empiricamente depois do ajuste, pois o próprio ajuste por mínimos quadrados a confirma automaticamente.

**Resposta:** Falso

**Justificativa:** O ajuste por mínimos quadrados não verifica homocedasticidade — ele simplesmente minimiza RSS independentemente de a suposição valer ou não. Confirmar (ou refutar) homocedasticidade exige inspecionar os resíduos depois do ajuste (como a própria aula fez ao encontrar heterocedasticidade real nos dados), nunca é uma garantia automática do procedimento de ajuste.

### Premissas do Modelo Gaussiano Homocedástico — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como o modelo desta aula assume $Y\mid X\sim\mathcal N(\beta^TX,\sigma^2)$, isso implica que a distribuição marginal (não condicional) de $Y$ também deve ser gaussiana, para o modelo fazer sentido.

**Resposta:** Falso

**Justificativa:** O modelo só faz uma suposição sobre a distribuição **condicional** de $Y$ dado $X$. A distribuição marginal de $Y$ depende também de como $X$ está distribuído na população, e em geral não é gaussiana (é uma mistura de gaussianas ponderada pela distribuição de $X$) — a suposição do modelo não exige nada sobre essa marginal.

### Construção da Verossimilhança Conjunta — item (a)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Se, em vez de tomar o logaritmo da verossimilhança, trabalhássemos diretamente com o produto de densidades $\prod_n\mathcal N(y_n\mid\beta^Tx_n,\sigma^2)$, maximizar esse produto em relação a $\beta$ ainda levaria exatamente ao mesmo $\hat\beta$ obtido via log-verossimilhança, porque o logaritmo é uma função estritamente crescente.

**Resposta:** Verdadeiro

**Justificativa:** Uma função estritamente crescente preserva a localização do máximo — maximizar $f(\beta)$ ou $\ln f(\beta)$ (com $f>0$) sempre produz o mesmo $\hat\beta$. O log só é usado por conveniência algébrica (transforma produto em soma), não porque muda o resultado.

### Construção da Verossimilhança Conjunta — item (b)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ No caso extremo de $N=1$ (uma única observação), a "log-verossimilhança" ainda pode ser escrita pela mesma fórmula geral, mas maximizá-la em relação a $\beta$ (com mais de um parâmetro livre) não determina um único $\hat\beta$, porque há infinitas retas passando exatamente por um ponto.

**Resposta:** Verdadeiro

**Justificativa:** Com um único ponto e dois ou mais parâmetros livres ($\beta_0,\beta_1,\ldots$), existe uma família inteira de retas com RSS$=0$ passando exatamente por esse ponto — todas maximizam igualmente a log-verossimilhança, sem um único ótimo.

### Construção da Verossimilhança Conjunta — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Num modelo que assume que o tempo entre chegadas de clientes segue uma distribuição exponencial (não gaussiana), a mesma lógica de multiplicar densidades e tomar o logaritmo se aplicaria, mas o valor numérico do máximo obtido seria sempre diretamente comparável ao valor máximo da log-verossimilhança gaussiana desta aula, permitindo escolher qual das duas descreve melhor seus dados só comparando os números brutos.

**Resposta:** Falso

**Justificativa:** A parte sobre multiplicar densidades e logaritmar é válida para qualquer família de distribuições — mas comparar valores brutos de log-verossimilhança máxima entre famílias distribucionais diferentes (gaussiana vs. exponencial) não é uma comparação válida sem correção; são escalas e normalizações distintas, não diretamente comparáveis pelo valor numérico bruto.

### Construção da Verossimilhança Conjunta — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como a log-verossimilhança desta aula é $\ell(\beta,\sigma^2)=-\frac N2\ln(2\pi)-N\ln\sigma-\frac{\text{RSS}(\beta)}{2\sigma^2}$, maximizar $\ell$ em relação a $\beta$ e maximizar $\ell$ em relação a $\sigma^2$ são operações que precisam ser feitas simultaneamente, nunca uma depois da outra, porque os dois parâmetros aparecem na mesma expressão.

**Resposta:** Falso

**Justificativa:** É exatamente o oposto do que a aula faz: para qualquer $\sigma^2>0$ fixo, maximizar $\ell$ em relação a $\beta$ equivale a minimizar $\text{RSS}(\beta)$ (o termo $1/2\sigma^2$ é apenas um fator multiplicativo positivo que não muda onde está o mínimo) — dando $\hat\beta_{\text{OLS}}$ independentemente de $\sigma^2$. Só depois, com $\hat\beta$ fixo, maximiza-se em relação a $\sigma^2$. A sequência funciona perfeitamente bem.

### O Teorema Central: OLS = MLE — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se a variância $\sigma^2$ fosse conhecida e fixa de antemão (não estimada), o valor de $\hat\beta$ que maximiza a log-verossimilhança ainda seria exatamente o mesmo $\hat\beta_{\text{OLS}}$, porque $\sigma^2$ entra na log-verossimilhança apenas como um fator multiplicativo positivo do termo que depende de $\beta$.

**Resposta:** Verdadeiro

**Justificativa:** Para qualquer $\sigma^2>0$ fixo, o único termo de $\ell$ que depende de $\beta$ é $-\text{RSS}(\beta)/(2\sigma^2)$ — maximizar isso em relação a $\beta$ equivale a minimizar $\text{RSS}(\beta)$, independentemente do valor específico de $\sigma^2$.

### O Teorema Central: OLS = MLE — item (b)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Se, por hipótese, $\text{RSS}(\hat\beta)=0$ para o $\hat\beta$ que minimiza a soma de quadrados (ajuste perfeito, sem nenhum resíduo), o estimador $\hat\sigma^2_{\text{MLE}}=\text{RSS}(\hat\beta)/N$ seria exatamente zero, e a log-verossimilhança avaliada nesse ponto tenderia a $+\infty$ conforme $\sigma\to0$ nessa mesma expressão, revelando uma degenerescência do modelo gaussiano nesse caso extremo.

**Resposta:** Verdadeiro

**Justificativa:** Com $\text{RSS}=0$, $\ell=-\frac N2\ln(2\pi)-N\ln\sigma$; conforme $\sigma\to0^+$, $\ln\sigma\to-\infty$, então $-N\ln\sigma\to+\infty$ — a log-verossimilhança diverge, um sintoma conhecido de degenerescência do ajuste perfeito no modelo gaussiano.

### O Teorema Central: OLS = MLE — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Se, em outro domínio qualquer, alguém provar que maximizar uma verossimilhança assumida é algebricamente idêntico a minimizar uma soma de quadrados, essa prova por si só já implica que o ruído daquele modelo específico foi assumido gaussiano, porque é a densidade gaussiana (e nenhuma outra densidade comum) que produz esse termo quadrático especificamente na log-verossimilhança.

**Resposta:** Verdadeiro

**Justificativa:** É o mesmo mecanismo do Bloco 3 rodado ao contrário: a forma exponencial-quadrática $\exp\{-(\cdot)^2/2\sigma^2\}$ é o que torna a log-verossimilhança gaussiana literalmente uma soma de quadrados com sinal trocado. Outras densidades comuns (Laplace, por exemplo) produzem outros termos (valor absoluto) — só a gaussiana produz especificamente o termo quadrático que colapsa em minimizar RSS.

### O Teorema Central: OLS = MLE — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como $\hat\beta_{\text{MLE}}=\hat\beta_{\text{OLS}}$ sob o modelo gaussiano desta aula, conclui-se que máxima verossimilhança e mínimos quadrados são sempre a mesma coisa, para qualquer modelo estatístico, não apenas para regressão linear sob ruído gaussiano.

**Resposta:** Falso

**Justificativa:** A equivalência provada nesta aula é específica do ruído gaussiano aditivo em regressão linear — sob outra suposição de ruído (Laplace) ou outro tipo de modelo (regressão logística, Aula 7), a máxima verossimilhança leva a minimizar uma função de erro diferente, não a soma de quadrados.

### Viés do MLE de $\sigma^2$ — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se, em vez de dividir por $N$, dividíssemos $\text{RSS}(\hat\beta)$ por $N-2$ (número de observações menos o número de parâmetros de $\beta$ nesta aula), o estimador resultante teria valor esperado exatamente igual a $\sigma^2$ verdadeiro — mas deixaria de ser o estimador de máxima verossimilhança.

**Resposta:** Verdadeiro

**Justificativa:** É o estimador não-viesado clássico de $\sigma^2$ em regressão linear — corrige exatamente o viés introduzido por estimar $\beta$ a partir dos mesmos dados usados para medir a dispersão residual, mas o estimador de máxima verossimilhança é, por definição, $\text{RSS}/N$, não essa versão corrigida.

### Viés do MLE de $\sigma^2$ — item (b)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Conforme $N\to\infty$ (mantendo o número de parâmetros de $\beta$ fixo), a diferença relativa entre $\hat\sigma^2_{\text{MLE}}=\text{RSS}/N$ e o estimador não-viesado $\text{RSS}/(N-2)$ tende a zero, porque $N/(N-2)\to1$.

**Resposta:** Verdadeiro

**Justificativa:** A razão entre os dois estimadores é exatamente $N/(N-2)$ — conforme $N$ cresce com o número de parâmetros fixo, essa razão converge a 1, e o viés relativo desaparece assintoticamente.

### Viés do MLE de $\sigma^2$ — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ O mesmo padrão de viés reaparece em qualquer estimador de variância obtido por máxima verossimilhança que primeiro estime uma média (ou um hiperplano) a partir dos mesmos dados; e por isso, na prática, é sempre preferível reportar o estimador não-viesado em vez do MLE, em qualquer aplicação, sem exceção.

**Resposta:** Falso

**Justificativa:** A primeira parte (o padrão de viés é geral) é correta — é o mesmo fenômeno já visto para a variância gaussiana. Mas a conclusão de que o estimador não-viesado é "sempre preferível... sem exceção" é um exagero: viés não é o único critério de qualidade de um estimador (ver item seguinte, sobre erro quadrático médio).

### Viés do MLE de $\sigma^2$ — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como $\hat\sigma^2_{\text{MLE}}$ é viesado para baixo, ele é necessariamente um estimador pior do que o estimador não-viesado $\text{RSS}/(N-2)$ em qualquer critério razoável de qualidade, incluindo o erro quadrático médio do próprio estimador de $\sigma^2$.

**Resposta:** Falso

**Justificativa:** Viés é só um dos componentes do erro quadrático médio (MSE = viés² + variância). Um estimador viesado pode ter variância menor o bastante para ter MSE menor que a versão não-viesada — "viesado" não implica "pior em qualquer critério", é uma generalização indevida do fato do viés isoladamente.

### Verificação Numérica e Otimização — item (a)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Se a otimização numérica desta aula tivesse sido inicializada num ponto de partida muito distante de $\hat\beta_{\text{OLS}}$, o algoritmo Nelder-Mead ainda convergiria ao mesmo ponto ótimo, porque a log-verossimilhança gaussiana em função de $\beta$ é uma função côncava sem outros máximos locais.

**Resposta:** Verdadeiro

**Justificativa:** Para $\sigma$ fixo, $\ell(\beta)$ é uma parábola invertida (côncava) em $\beta$ — tem um único máximo global, sem máximos locais escondidos onde um otimizador possa ficar preso, independentemente de onde a busca comece.

### Verificação Numérica e Otimização — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Se a grade usada para visualizar a superfície de log-verossimilhança tivesse resolução extremamente grosseira, o pico da grade poderia ficar deslocado do verdadeiro $\hat\beta_{\text{OLS}}$ — e, por essa razão, sempre que uma forma fechada exata existir, o grid search se torna uma ferramenta cientificamente inútil, sem nenhum valor pedagógico ou de verificação.

**Resposta:** Falso

**Justificativa:** A primeira parte é correta (grades grosseiras introduzem erro de discretização), mas a conclusão é um exagero: o grid search desta própria aula teve valor real de verificação/pedagógico (mostrar visualmente que a superfície tem um único pico exatamente onde a forma fechada aponta) mesmo com uma forma fechada disponível.

### Verificação Numérica e Otimização — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Em problemas de otimização com muitos parâmetros (por exemplo, uma rede neural com milhões de pesos), a mesma ideia de verificar uma solução fechada contra uma busca numérica deixaria de ser prática simplesmente por causa do volume de contas — não porque o princípio de comparação deixe de fazer sentido.

**Resposta:** Verdadeiro

**Justificativa:** O princípio (comparar um resultado analítico contra uma busca numérica independente) continua logicamente válido em qualquer dimensão; o que muda é a viabilidade computacional de visualizar/varrer uma superfície com milhões de dimensões, uma limitação prática, não conceitual.

### Verificação Numérica e Otimização — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como a otimização numérica confirmou o resultado da forma fechada neste exemplo específico, isso prova matematicamente (não apenas ilustra empiricamente) que $\hat\beta_{\text{MLE}}=\hat\beta_{\text{OLS}}$ para qualquer conjunto de dados sob o modelo gaussiano.

**Resposta:** Falso

**Justificativa:** A confirmação numérica vale para um dataset específico e um otimizador que convergiu corretamente — é uma ilustração empírica, não uma prova geral. A prova matemática de que a equivalência vale para qualquer conjunto de dados é a derivação algébrica feita no Bloco 3, não a checagem numérica.

### Limitações: Heterocedasticidade, Censura e Não-Linearidade — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se `MedHouseVal` não fosse artificialmente censurado em $5{,}00001$, o $\hat\beta_1$ estimado para `MedInc` provavelmente mudaria, porque essas observações censuradas concentram-se desproporcionalmente entre os imóveis de renda mais alta.

**Resposta:** Verdadeiro

**Justificativa:** Como a censura afeta principalmente a cauda de renda alta, "destelhar" esses valores mudaria justamente a relação entre `MedInc` alto e `MedHouseVal`, a região que mais influencia a inclinação estimada.

### Limitações: Heterocedasticidade, Censura e Não-Linearidade — item (b)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ No extremo em que a censura afetasse 100% das observações (todos os valores exibidos como exatamente $5{,}00001$), a variância amostral de `MedHouseVal` seria zero, e o ajuste de mínimos quadrados encontraria $\hat\beta_1=0$.

**Resposta:** Verdadeiro

**Justificativa:** Se $y$ é constante, $\text{Cov}(x,y)=0$ para qualquer $x$, e $\hat\beta_1=\text{Cov}(x,y)/\text{Var}(x)=0$ — não há variação em $y$ para nenhum atributo explicar.

### Limitações: Heterocedasticidade, Censura e Não-Linearidade — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Num estudo de sobrevivência com censura à direita, a mesma distorção de ignorar a censura se aplicaria, subestimando o tempo médio de sobrevivência — mas esse problema desapareceria automaticamente com uma amostra suficientemente grande, já que o viés de censura diminui conforme $N$ aumenta.

**Resposta:** Falso

**Justificativa:** O viés de censura é sistemático (estrutural), não um efeito de variância amostral — aumentar $N$ reduz a incerteza em torno de uma estimativa, mas não corrige um viés que vem de ignorar uma distorção presente em cada observação censurada; o viés persiste independentemente do tamanho da amostra.

### Limitações: Heterocedasticidade, Censura e Não-Linearidade — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como a variância dos resíduos cresce com `MedInc` (heterocedasticidade real, confirmada nos dados desta aula), o modelo linear ajustado por mínimos quadrados se torna inútil para prever `MedHouseVal`, e nenhuma previsão feita a partir dele deveria ser usada.

**Resposta:** Falso

**Justificativa:** Heterocedasticidade compromete a confiabilidade da quantificação de incerteza em torno das previsões (intervalos de confiança, testes de hipótese), não a validade do ponto central previsto — as previsões pontuais continuam informativas, só precisam ser interpretadas com o cuidado adicional de que a incerteza real varia com `MedInc`.
