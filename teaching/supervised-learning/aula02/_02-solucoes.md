# Soluções — Questões de Verdadeiro/Falso (Aula 2)

> Arquivo de apoio, não publicado (prefixo `_`). Contém a resposta e a
> justificativa de cada item das 12 questões de V/F do `index.qmd`. O
> `index.qmd` publicado continua sem solução — este arquivo existe só
> para conferência do professor/monitor, seguindo a metodologia de
> criação de questões definida em `../../CLAUDE.md`.

## A maldição da dimensionalidade

**a.** [ ] No limite em que $d\to\infty$, mantendo $M=10$ fixo por eixo, o número de células $M^d$ cresce mais rápido do que qualquer conjunto de dados de tamanho polinomial em $d$.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Crescimento exponencial ($M^d$) sempre ultrapassa qualquer crescimento polinomial em $d$ para $d$ suficientemente grande — é um fato assintótico padrão. Nenhum orçamento de dados que cresça só polinomialmente com $d$ acompanha o número de células.

**b.** [ ] Se, em vez de $M$ células por eixo, usássemos apenas $M=2$ (uma grade binária), o problema de crescimento exponencial em $d$ desapareceria.

**Heurística:** Contrafactual
**Resposta:** Falso
**Justificativa:** $2^d$ ainda é exponencial em $d$ — para $d=15$, já são $32{.}768$ células; para $d=50$, cerca de $10^{15}$. Reduzir $M$ muda a base da exponencial, não elimina o expoente $d$ que é a real fonte do problema.

**c.** [ ] Num problema de reconhecimento de imagens em que cada pixel é uma dimensão (por exemplo, $28\times28=784$ dimensões), um histograma multidimensional ingênuo seria ainda mais inviável do que o exemplo de $d=15$ desta aula.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** Com $d=784$ em vez de $d=15$, o número de células $M^d$ é astronomicamente maior — o mesmo argumento da aula, só que num domínio real e muito comum (imagens), onde a dimensionalidade típica já supera em muito o exemplo didático.

**d.** [ ] Como o problema vem do crescimento exponencial de $M^d$, comprar mais capacidade computacional (mais GPUs) resolveria a maldição da dimensionalidade.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** O problema fundamental é de ESCASSEZ DE DADOS — não há dados reais suficientes para preencher $M^d$ células de forma confiável, não importa quanto poder de processamento se tenha disponível para lidar com elas. Mais GPUs não criam mais dados.

---

## Teoria da decisão: risco e regra de Bayes

**a.** [ ] No limite em que a matriz de perda $L$ se torna a perda 0-1, a regra de Bayes coincide exatamente com a regra do posterior máximo.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Sob perda 0-1, minimizar o risco posterior $\rho(a\mid\mathbf{x})=\sum_k L(k,a)p(\mathcal{C}_k\mid\mathbf{x})$ se reduz a minimizar $1-p(\mathcal{C}_a\mid\mathbf{x})$, que é o mesmo que maximizar $p(\mathcal{C}_a\mid\mathbf{x})$ — exatamente a regra do posterior máximo.

**b.** [ ] Se a matriz de perda $L$ fosse alterada para ter custos muito diferentes entre os tipos de erro, mas a posteriori $p(\mathcal{C}_k\mid\mathbf{x})$ permanecesse a mesma, a regra de decisão ótima poderia mudar, mesmo sem nenhuma mudança na posteriori.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** O risco posterior depende do PRODUTO entre $L$ e a posteriori; mudar $L$ muda esse produto e, portanto, qual ação minimiza o risco — mesmo que a posteriori em si não tenha mudado nem um pouco.

**c.** [ ] Num sistema de aprovação de crédito, se o custo de aprovar um mau pagador for muito maior que o de recusar um bom pagador, a regra ótima recusará crédito mesmo para clientes com posteriori de bom pagador moderadamente alta (ex: $60\%$), não só abaixo de $50\%$.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** É o mesmo deslocamento de limiar do exemplo médico/de fraude da aula, transferido para crédito: um custo assimétrico grande desloca o limiar de decisão para longe de $0{,}5$, tornando a recusa a decisão ótima mesmo com alguma evidência a favor da aprovação.

**d.** [ ] Como o risco de Bayes $R^\star$ é o menor risco esperado dado o modelo verdadeiro, conclui-se que $R^\star=0$ sempre que o modelo $p(\mathbf{x},\mathcal{C}_k)$ usado for corretamente especificado.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** Correção da especificação do modelo não implica ausência de sobreposição entre as classes; se as densidades verdadeiras se sobrepõem, $R^\star>0$ mesmo com o modelo perfeitamente correto — é exatamente o erro de Bayes irredutível da Aula 1, generalizado para perda arbitrária.

---

## Bayes para $K$ classes e modelos generativos

**a.** [ ] Se, em vez de $K=2$, tivéssemos $K=5$ classes, a regra "decida pela conjunta maior" deixaria de valer, sendo necessário reformular o argumento de otimalidade da Aula 1 do zero.

**Heurística:** Contrafactual
**Resposta:** Falso
**Justificativa:** O argumento de minimizar o erro esperado escolhendo a classe de maior conjunta nunca usou $K=2$ como hipótese essencial — ele generaliza diretamente para $\arg\max_k p(\mathbf{x},\mathcal{C}_k)$ com qualquer $K$, sem precisar de reformulação.

**b.** [ ] No limite em que a priori de uma das $K$ classes tende a zero, a probabilidade de o modelo generativo sortear essa classe tende a zero, mesmo que sua condicional $p(\mathbf{x}\mid\mathcal{C}_k)$ seja idêntica às demais.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** No processo gerativo em duas etapas, a classe é sorteada PRIMEIRO segundo $\pi_k$; se $\pi_k\to0$, essa classe praticamente nunca é sorteada, independentemente de como sua condicional se pareça com as demais.

**c.** [ ] Num sistema de diagnóstico com 5 doenças possíveis mutuamente exclusivas mais "saudável" (6 classes), a evidência $p(\mathbf{x})$ ainda seria a soma da conjunta sobre as 6 classes, só com mais termos do que no caso $K=2$.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** A Regra da Soma não é uma peculiaridade do caso binário — $p(\mathbf{x})=\sum_{j=1}^K p(\mathbf{x},\mathcal{C}_j)$ vale para qualquer $K$, incluindo o caso de 6 hipóteses diagnósticas.

**d.** [ ] Como substituir a família gaussiana por uma rede neural profunda muda a forma funcional usada para $p(\mathbf{x}\mid\mathcal{C}_k)$, isso também muda o conceito de modelo generativo em si.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** O CONCEITO de modelo generativo (sortear a classe, depois os dados condicional à classe, combinar via Bayes) permanece o mesmo; trocar gaussiana por rede neural muda só a FAMÍLIA de distribuições usada para representar $p(\mathbf{x}\mid\mathcal{C}_k)$, não o conceito por trás da abordagem.

---

## O modelo generativo em duas etapas

**a.** [ ] No limite em que todas as $K$ classes têm a mesma condicional $p(\mathbf{x}\mid\mathcal{C}_k)$, o modelo generativo em duas etapas se reduz, na prática, a sortear $\mathbf{x}$ de uma única distribuição comum, independentemente de qual classe foi sorteada.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Se todas as condicionais coincidem, saber qual classe foi sorteada na primeira etapa não afeta em nada a distribuição de onde $\mathbf{x}$ vem na segunda etapa — a classe se torna irrelevante para o valor de $\mathbf{x}$ observado, equivalente a amostrar sempre da mesma distribuição comum.

**b.** [ ] Se um modelo discriminativo fosse usado no lugar do modelo generativo, ainda seria possível gerar novos dados sintéticos $\mathbf{x}$ amostrando do modelo ajustado, exatamente como no caso generativo.

**Heurística:** Contrafactual
**Resposta:** Falso
**Justificativa:** Um modelo puramente discriminativo nunca estima $p(\mathbf{x}\mid\mathcal{C}_k)$ nem $p(\mathbf{x})$ — não há de onde amostrar novos dados sintéticos. Essa é precisamente a capacidade que se perde ao "jogar fora os dados" e modelar só a fronteira.

**c.** [ ] Num sistema que gera imagens sintéticas de rostos realistas, o procedimento é conceitualmente uma amostragem de $p(\mathbf{x})$ (ou $p(\mathbf{x}\mid\mathcal{C}_k)$) — a mesma ideia central do modelo generativo desta aula, com uma família de distribuições muito mais sofisticada.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** É exatamente o ponto de "IA generativa usa o mesmo conceito, muda só a família" aplicado a um exemplo concreto e atual: gerar rostos sintéticos é amostrar de um modelo ajustado a dados, o mesmo princípio dos $5$ parâmetros gaussianos, só que com uma família muito mais rica.

**d.** [ ] Como um modelo discriminativo modela diretamente a fronteira sem passar por $p(\mathbf{x}\mid\mathcal{C}_k)$, conclui-se que ele modela diretamente $p(\mathbf{x})$, em vez da posteriori.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** "Não modela $p(\mathbf{x}\mid\mathcal{C}_k)$" não implica "modela $p(\mathbf{x})$" — um modelo discriminativo tipicamente modela a POSTERIORI $p(\mathcal{C}_k\mid\mathbf{x})$ (ou só a fronteira) diretamente, sem nunca estimar nenhuma densidade de $\mathbf{x}$, nem condicional nem marginal.

---

## Generativo, discriminativo e "IA generativa"

**a.** [ ] No limite em que um classificador discriminativo só precisa prever a classe mais provável (sem uma pontuação de confiança calibrada), ele pode dispensar completamente qualquer estimativa exata de $p(\mathbf{x}\mid\mathcal{C}_k)$ ou de $p(\mathcal{C}_k\mid\mathbf{x})$, bastando aprender a fronteira certa.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Se o único objetivo é a decisão (não a probabilidade em si), basta que o modelo aprenda de que lado da fronteira um ponto cai — nenhuma estimativa numericamente correta de densidade ou posteriori é estritamente necessária para isso, um caso extremo do espírito discriminativo.

**b.** [ ] Se um modelo discriminativo, além de aprender a fronteira, também precisasse necessariamente estimar $p(\mathbf{x})$ como subproduto do treinamento, ele deixaria de ser, por definição, discriminativo.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** "Discriminativo" é definido justamente por NÃO precisar modelar $p(\mathbf{x})$; se essa estimativa se tornasse uma necessidade do procedimento, a própria definição da categoria deixaria de se aplicar — é quase uma verdade por definição, mas que testa se o conceito foi entendido com precisão.

**c.** [ ] Num problema em que se quer não só classificar e-mails como spam, mas também gerar exemplos sintéticos de spam para aumentar o treino, um modelo puramente discriminativo não bastaria para essa segunda tarefa, mesmo sendo excelente na primeira.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** Gerar exemplos novos exige amostrar de uma densidade — algo que só um modelo generativo (ou um componente generativo) provê. Um discriminativo excelente em classificar não ajuda em nada nessa segunda tarefa, evidenciando a diferença prática entre os dois paradigmas.

**d.** [ ] Como um modelo discriminativo "joga fora" a informação de $p(\mathbf{x}\mid\mathcal{C}_k)$ que o generativo usaria, conclui-se que ele sempre precisa de mais parâmetros do que um modelo generativo equivalente para o mesmo problema.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** É o oposto do que geralmente acontece: por não precisar modelar a densidade completa de $\mathbf{x}$ por classe, um modelo discriminativo tipicamente precisa de MENOS parâmetros para resolver a mesma tarefa de classificação, não mais. "Joga fora informação" não implica "precisa de mais parâmetros" — a intuição aqui está invertida.

---

## Contraexemplos de independência: causa comum e XOR

**a.** [ ] No exemplo de "causa comum" (grátis/ganhador dado a classe), no limite em que a classe deixa de ter qualquer influência sobre as duas palavras, a dependência marginal entre elas desaparece, mesmo mantendo a independência condicional dada a classe.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Se $p(\text{grátis}\mid c)$ é a mesma para todo $c$, então $p(\text{grátis},\text{ganhador})=\sum_c \pi_c\, p(\text{grátis}\mid c)\,p(\text{ganhador}\mid c) = p(\text{grátis})\sum_c\pi_c\,p(\text{ganhador}\mid c)=p(\text{grátis})p(\text{ganhador})$ — a dependência marginal induzida pela causa comum desaparece exatamente quando a causa deixa de diferenciar os efeitos.

**b.** [ ] No exemplo do XOR, se observássemos apenas uma pista parcial sobre $\mathcal{C}$ (por exemplo, "provavelmente $1$", com $70\%$ de confiança), $x_1$ e $x_2$ permaneceriam exatamente tão dependentes quanto no caso de observar $\mathcal{C}=1$ com certeza.

**Heurística:** Contrafactual
**Resposta:** Falso
**Justificativa:** Condicionar em $\mathcal{C}=1$ com certeza força $x_2=1-x_1$ (dependência perfeita); uma evidência parcial e incerta sobre $\mathcal{C}$ induz uma dependência mais fraca entre $x_1,x_2$, não idêntica ao caso de certeza total — o grau de dependência induzida escala com o quanto se sabe sobre a causa comum.

**c.** [ ] Num sistema de recomendação em que a popularidade geral de um produto afeta tanto "número de cliques" quanto "número de compras", essas duas variáveis podem ser marginalmente dependentes mesmo sendo condicionalmente independentes dado o nível de popularidade.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** É a mesma estrutura de causa comum do exemplo grátis/ganhador, transferida para métricas de e-commerce: a popularidade (análoga à classe) cria dependência marginal entre cliques e compras, mesmo que, fixado o nível de popularidade, as duas sejam condicionalmente independentes.

**d.** [ ] Como o XOR mostra que condicionar pode CRIAR dependência entre variáveis originalmente independentes, conclui-se que condicionar em qualquer variável adicional sempre aumenta (ou mantém) a dependência entre duas variáveis, nunca a reduz.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** O próprio exemplo de "causa comum" desta aula mostra o oposto: condicionar na classe reduz a dependência entre "grátis" e "ganhador" (de fortemente dependentes marginalmente para condicionalmente independentes). Condicionar pode criar dependência (XOR) OU removê-la (causa comum) — a direção depende da estrutura causal, não é uma regra fixa.

---

## Independência vs. independência condicional

**a.** [ ] Se $X_1,X_2$ forem marginalmente independentes mas NÃO condicionalmente independentes dada uma terceira variável $Z$, isso contradiz o exemplo do XOR desta aula, que mostrou exatamente o padrão oposto.

**Heurística:** Contrafactual
**Resposta:** Falso
**Justificativa:** É exatamente o padrão que o XOR mostrou, não o oposto: $x_1,x_2$ são marginalmente independentes, mas condicionalmente DEPENDENTES dado $\mathcal{C}=x_1\oplus x_2$. A afirmação descreve corretamente o exemplo, então dizer que "contradiz" é o erro.

**b.** [ ] No limite em que a classe $C$ tem um único valor possível, independência condicional dada $C$ e independência marginal passam a significar exatamente a mesma coisa.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Se $C$ só pode assumir um valor, condicionar em $C$ não fornece nenhuma informação (é uma constante), então $p(x_1,x_2\mid C)=p(x_1,x_2)$ trivialmente — as duas noções colapsam na mesma afirmação quando não há variação em $C$ para diferenciar.

**c.** [ ] Em genética, dois genes podem ser fortemente correlacionados na população geral (por estarem ligados a uma etnia comum), mas condicionalmente independentes dentro de qualquer subgrupo étnico específico — a mesma estrutura de "causa comum" do exemplo do e-mail.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** É um fenômeno real e conhecido em genética populacional (estratificação populacional): a etnia (ou ancestralidade) funciona como causa comum, criando correlação marginal entre marcadores genéticos que são condicionalmente independentes dentro de cada subpopulação.

**d.** [ ] Como a independência condicional dada a classe é a suposição central do Naive Bayes, conclui-se que, se essa suposição for violada, o Naive Bayes necessariamente terá desempenho ruim de classificação.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** É exatamente o ponto da questão discursiva 2 desta aula: a suposição pode estar fortemente violada e o classificador ainda ter boa acurácia, porque sob perda 0-1 só importa qual classe recebe o *score* maior, não se a posteriori estimada está numericamente correta.

---

## O algoritmo Naive Bayes

**a.** [ ] No limite em que uma probabilidade condicional estimada é exatamente zero para algum atributo, o *score* logarítmico dessa classe tende a $-\infty$, não importa quão altas sejam as demais probabilidades condicionais.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** A soma de logs tem um termo $\ln(0)=-\infty$; somar $-\infty$ a qualquer conjunto de números finitos ainda resulta em $-\infty$ — nenhuma quantidade de evidência favorável nos outros atributos compensa esse único termo.

**b.** [ ] Se, em vez de suavização, a correção para probabilidade zero fosse simplesmente ignorar aquele atributo no cálculo do *score* daquela instância, isso teria um efeito equivalente à suavização, só calculado de outra forma.

**Heurística:** Contrafactual
**Resposta:** Falso
**Justificativa:** Ignorar o atributo remove sua contribuição por completo (equivalente a um termo neutro); suavização, em vez disso, mantém a contribuição do atributo, só deslocando a probabilidade estimada de $0$ para um valor pequeno mas positivo — os dois efeitos matemáticos são diferentes, não duas implementações da mesma correção.

**c.** [ ] Num classificador de sentimento de texto, se a palavra "maravilhoso" nunca apareceu nos exemplos rotulados como "negativo", um Naive Bayes sem suavização atribuiria zero de probabilidade a qualquer review negativo que contenha essa palavra, não importa o resto do texto.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** É a mesma patologia da probabilidade zero, transferida para um cenário realista e comum de NLP: uma única palavra nunca vista numa classe zera completamente o *score* daquela classe para qualquer texto que a contenha.

**d.** [ ] Como somar logaritmos evita o problema de multiplicar muitos números pequenos (*underflow* numérico), a soma de logs também resolve, por si só, o problema de uma probabilidade estimada exatamente zero.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** São dois problemas numéricos distintos: *underflow* vem de multiplicar muitos números pequenos POSITIVOS (resolvido pela soma de logs); probabilidade zero quebra o log em si ($\ln 0=-\infty$), um problema que a soma de logs não resolve — é a suavização, uma técnica separada, que evita isso.

---

## A escolha de família por atributo

**a.** [ ] Se um atributo categórico com $M=5$ níveis fosse, por engano, modelado como contínuo e Gaussiano, o Naive Bayes ainda produziria uma pontuação numérica para cada classe, mas essa pontuação deixaria de corresponder a uma probabilidade genuína sobre os 5 níveis discretos.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** O algoritmo mecanicamente ainda calcula uma densidade Gaussiana para qualquer valor numérico de entrada — ele "roda" sem erro — mas essa densidade não reflete corretamente a estrutura discreta dos 5 níveis categóricos; o modelo é mal especificado, mesmo que produza um número.

**b.** [ ] No limite em que um atributo categórico tem $M=2$ níveis, a distribuição Categórica usada para modelá-lo se reduz a uma Bernoulli, com apenas 1 parâmetro livre por classe.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Uma Categórica com $M$ níveis tem $M-1$ parâmetros livres (o último é determinado pela restrição de soma 1); com $M=2$, isso dá exatamente $1$ parâmetro livre — a própria parametrização da Bernoulli.

**c.** [ ] Num prontuário médico misto (idade contínua, tipo sanguíneo categórico com 4 níveis, presença de sintoma binária), o Naive Bayes poderia legitimamente usar três famílias de distribuição diferentes para essas três colunas.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** É exatamente a flexibilidade já estabelecida na aula (misturar Gaussiana, Categórica, Bernoulli por coluna), aplicada a um exemplo médico concreto e realista com três tipos de atributo diferentes.

**d.** [ ] Como cada atributo contribui seu próprio termo de log-verossimilhança para a soma do passo 3, misturar famílias diferentes por coluna quebra essa soma, pois os termos passam a ter unidades ou escalas incompatíveis.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** Cada termo é o log da verossimilhança DAQUELE atributo, comparado entre classes — o que importa é a comparação entre classes para o MESMO atributo, não a compatibilidade "de escala" entre atributos diferentes. Eventuais diferenças de escala entre famílias afetam igualmente todas as classes e não impedem a soma nem distorcem o *argmax*.

---

## O caso binário: custo e priori viram um limiar

**a.** [ ] No limite em que $c_{II}/c_I\to\infty$, o limiar de decisão ótimo tende ao extremo que quase sempre declara a classe associada a evitar o Tipo II, mesmo com posteriori muito baixa a favor dela.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Conforme a razão de custos cresce sem limite, o limiar ótimo se desloca cada vez mais para o extremo — a mesma tendência já vista nas curvas da aula para razões $1$, $5$ e $20$, levada ao seu limite.

**b.** [ ] Se a perda deixasse de ser 0-1 e passasse a ser fortemente assimétrica, a regra de Bayes deixaria de coincidir com a regra do posterior máximo, mesmo que a posteriori $p(\mathcal{C}_k\mid\mathbf{x})$ permanecesse exatamente a mesma.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** A coincidência entre regra de Bayes e regra do posterior máximo é uma peculiaridade da perda 0-1; sob perda assimétrica, a regra ótima passa a depender do VALOR da posteriori em relação a um limiar deslocado, não só de qual classe tem a maior posteriori.

**c.** [ ] Num sistema de controle de qualidade industrial, se deixar passar um produto defeituoso custar 20 vezes mais que descartar um produto bom por engano, a regra ótima usará um limiar de posteriori bem abaixo de $50\%$ para declarar "defeituoso".

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** É o mesmo mecanismo de deslocamento de limiar do exemplo médico da aula, aplicado a controle de qualidade industrial: um custo assimétrico de $20\times$ desloca o limiar bem para longe de $50\%$, na direção de detectar mais defeitos à custa de mais falsos alarmes.

**d.** [ ] Como mudar os custos da matriz de perda desloca o limiar de decisão ótimo, conclui-se que mudar os custos também muda a posteriori $p(\mathcal{C}_k\mid\mathbf{x})$ calculada pelo modelo.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** A posteriori é uma quantidade estatística, calculada a partir dos dados e do modelo — ela não sabe nada sobre custos. Os custos entram só na hora de decidir o que FAZER com a posteriori (onde colocar o limiar), nunca no cálculo da posteriori em si.

---

## Risco de Bayes e a ressalva que importa

**a.** [ ] No limite em que as densidades condicionais das classes se tornam idênticas, o risco de Bayes $R^\star$ sob perda 0-1 tende ao seu valor máximo possível, $\min(\pi_A,\pi_B)$ — o mesmo teto já visto na Aula 1.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Densidades idênticas eliminam qualquer informação discriminativa em $\mathbf{x}$; o melhor que se pode fazer é sempre prever a classe majoritária, com erro $\min(\pi_A,\pi_B)$ — o teto do risco de Bayes para prioris fixas, o mesmo fato já estabelecido na Aula 1, agora reconectado ao conceito mais geral de risco.

**b.** [ ] Se o modelo $p(\mathbf{x},\mathcal{C}_k)$ usado estiver errado (mal especificado), a regra de Bayes calculada a partir desse modelo errado ainda seria, por definição, ótima em relação ao mundo real, não só em relação ao modelo assumido.

**Heurística:** Contrafactual
**Resposta:** Falso
**Justificativa:** É exatamente "a ressalva que importa": a regra de Bayes é ótima SE a posteriori usada estiver certa. Se o modelo estiver errado, a regra calculada a partir dele é ótima em relação a esse modelo, não necessariamente em relação ao mundo real.

**c.** [ ] Num sistema de aprovação de empréstimos com suposições simplificadas (independência entre variáveis correlacionadas na realidade), a regra de decisão pode classificar bem a maioria dos casos sob perda 0-1, mesmo que as probabilidades de inadimplência estimadas estejam sistematicamente erradas.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** É o mesmo fenômeno do Naive Bayes ("classifica bem, estima mal") transferido para risco de crédito: sob perda 0-1, o que importa é o *ranking* correto entre bom/mau pagador, não a calibração exata das probabilidades — um modelo mal especificado ainda pode decidir bem na maioria dos casos.

**d.** [ ] Como a regra de Bayes minimiza o risco posterior calculado a partir de $p(\mathcal{C}_k\mid\mathbf{x})$, a teoria da decisão garante, como parte do seu resultado, que esse $p(\mathcal{C}_k\mid\mathbf{x})$ usado é o verdadeiro processo gerador dos dados.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** A teoria da decisão otimiza a AÇÃO dado um modelo assumido — ela nunca verifica, nem garante, que esse modelo é o processo real que gerou os dados. Confundir "a regra é ótima dado o modelo" com "o modelo está correto" é exatamente a ressalva que este bloco existe para destacar.

---

## O exemplo do e-mail: "grátis" e "ganhador"

**a.** [ ] No limite em que $p(\text{grátis}=1\mid\text{spam})$ e $p(\text{grátis}=1\mid\text{ham})$ se tornam iguais, a conjunta marginal $p(\text{grátis}=1,\text{ganhador}=1)$ passa a ser exatamente igual ao produto das marginais, mesmo mantendo a independência condicional dada a classe.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Se $p(\text{grátis}\mid c)=g$ para todo $c$ (constante), então $p(\text{grátis},\text{ganhador})=\sum_c\pi_c\,g\,p(\text{ganhador}\mid c)=g\sum_c\pi_c\,p(\text{ganhador}\mid c)=g\cdot p(\text{ganhador})=p(\text{grátis})p(\text{ganhador})$ — a independência marginal emerge quando "grátis" deixa de depender da classe.

**b.** [ ] Se a prevalência de spam fosse $\pi_{\text{spam}}=0{,}99$ em vez de $0{,}5$ (mantendo as mesmas condicionais), a dependência marginal entre "grátis" e "ganhador" seria menor do que no cenário original da aula ($\pi_{\text{spam}}=0{,}5$).

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** Verificado numericamente: com $\pi_{\text{spam}}=0{,}5$, o "gap" entre a conjunta e o produto das marginais é $\approx0{,}119$; com $\pi_{\text{spam}}=0{,}99$, cai para $\approx0{,}005$. Quando a classe fica quase determinística (quase tudo é spam), ela deixa de funcionar como um "mixer" eficaz entre os dois regimes condicionais bem diferentes, e a dependência induzida encolhe.

**c.** [ ] O mesmo padrão de "causa comum" explicaria por que, num hospital, "tosse" e "febre" podem ser marginalmente dependentes mesmo sendo condicionalmente independentes dado o diagnóstico (gripe ou não).

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** É a mesma estrutura causal exata (o diagnóstico afeta as taxas de ambos os sintomas, gerando dependência marginal entre eles, mesmo que sejam condicionalmente independentes dado o diagnóstico) — um exemplo clássico de raciocínio probabilístico médico, análogo ao do e-mail.

**d.** [ ] Como a independência condicional dada a classe É satisfeita exatamente no exemplo de "grátis"/"ganhador" (foi construído assim), conclui-se que o Naive Bayes sempre estimará bem a posteriori em qualquer conjunto de dados de spam, não só neste exemplo controlado.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** O exemplo foi CONSTRUÍDO deliberadamente para satisfazer a suposição do Naive Bayes exatamente — isso não generaliza para dados reais de spam, onde a independência condicional quase certamente é violada em algum grau. Um caso ilustrativo satisfazer a suposição por construção não implica que dados reais também a satisfaçam.
