# Soluções — Questões de Verdadeiro/Falso (Aula 1)

> Arquivo de apoio, não publicado (prefixo `_`). Contém a resposta e a
> justificativa de cada item das 12 questões de V/F do `index.qmd`. O
> `index.qmd` publicado continua sem solução — este arquivo existe só
> para conferência do professor/monitor, seguindo a metodologia de
> criação de questões definida em `../../CLAUDE.md`.

## Distribuições, priori e fronteira de decisão

**a.** [ ] Se as duas classes fossem igualmente frequentes ($\pi_A=\pi_B=0{,}5$) em vez de $\pi_A=0{,}95$, o cruzamento das conjuntas passaria a coincidir exatamente com o cruzamento das condicionais $T_{COND}$.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** Com prioris iguais, $p(x,\mathcal{C}_A)=0{,}5\,f_A(x)$ e $p(x,\mathcal{C}_B)=0{,}5\,f_B(x)$ são as condicionais escaladas pela MESMA constante; o ponto onde as conjuntas se cruzam é exatamente onde $f_A(x)=f_B(x)$, ou seja, $T_{COND}$. É a assimetria das prioris ($0{,}95$ vs. $0{,}05$) que empurra $T_{CONJ}$ para longe de $T_{COND}$ no cenário real da aula.

**b.** [ ] No limite em que $\pi_A \to 1$, o cruzamento das conjuntas $T_{CONJ}$ tende a se afastar cada vez mais do cruzamento das condicionais $T_{COND}$, na direção do território de B.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Quanto mais próxima de $1$ a priori de A, mais a conjunta de A domina em relação à de B em qualquer ponto, exigindo que $x$ esteja cada vez mais "no território natural de B" antes que a conjunta de B ainda vença. O efeito já visto na aula ($\pi_A=0{,}95 \Rightarrow T_{CONJ}\approx0{,}72$, bem à direita de $T_{COND}\approx0{,}47$) só se intensifica conforme $\pi_A\to1$.

**c.** [ ] Considere uma triagem de segurança em aeroportos em que $99\%$ dos passageiros não representam ameaça. Mesmo com condicionais simétricas e bem separadas, cortar sempre no cruzamento das CONDICIONAIS (ignorando essa priori $99\%/1\%$) não é a regra de decisão ótima sob perda 0-1.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** É a mesma lição do Bloco 2 transferida para um domínio novo: sob perda 0-1, a regra ótima corta no cruzamento das CONJUNTAS, que incorpora a priori; ignorar uma priori tão assimétrica ($99\%/1\%$) e cortar nas condicionais é exatamente o erro "igualmente plausíveis $\ne$ igualmente prováveis" que a aula identifica.

**d.** [ ] Como o cruzamento das condicionais não depende das prioris, conclui-se que a taxa de erro total (Tipo I + Tipo II, ponderados pelas prioris) também não depende de onde as prioris colocam o peso relativo entre os dois tipos de erro.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** Duas coisas diferentes: o PONTO onde as condicionais se cruzam de fato não depende das prioris (é só $f_A(x)=f_B(x)$). Mas o erro total esperado, $\pi_A\cdot\text{TipoI}(t)+\pi_B\cdot\text{TipoII}(t)$, pondera cada tipo de erro pela respectiva priori — mudar essa ponderação muda qual $t$ minimiza o erro total, mesmo que o ponto de cruzamento das condicionais em si permaneça fixo.

---

## Teorema de Bayes e o exemplo da triagem médica

**a.** [ ] No limite em que a prevalência da doença tende a zero, mantendo sensibilidade e falso positivo fixos em $0{,}90$ e $0{,}03$, a posteriori $p(D\mid+)$ também tende a zero.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** $p(D\mid+)=\dfrac{\pi\cdot0{,}90}{\pi\cdot0{,}90+(1-\pi)\cdot0{,}03}$; conforme $\pi\to0$, o numerador vai a zero mais rápido que o denominador (que tende a $0{,}03>0$), então a razão toda vai a zero. É a versão extrema do efeito de base rate já visto no exemplo da aula ($\pi=0{,}01\Rightarrow p(D\mid+)\approx23\%$).

**b.** [ ] Se a prevalência da doença fosse $50\%$ em vez de $1\%$ (mantendo sensibilidade $0{,}90$ e falso positivo $0{,}03$), a posteriori $p(D\mid+)$ passaria a ser maior que $90\%$.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** Com $\pi=0{,}5$: $p(D\mid+)=\dfrac{0{,}5\times0{,}90}{0{,}5\times0{,}90+0{,}5\times0{,}03}=\dfrac{0{,}45}{0{,}465}\approx96{,}8\%$, de fato acima de $90\%$ — o oposto do efeito de base rate baixa: com prevalência alta, um resultado positivo é uma evidência forte e confiável.

**c.** [ ] Num teste de triagem usado em campanhas de vacinação em massa, com prevalência ainda menor (1 em 10.000) e sensibilidade e especificidade excelentes (99% cada), a proporção de positivos que são realmente doentes seria ainda menor do que no exemplo da aula.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** Com $\pi=0{,}0001$, sensibilidade $0{,}99$, falso positivo $0{,}01$: $p(D\mid+)=\dfrac{0{,}0001\times0{,}99}{0{,}0001\times0{,}99+0{,}9999\times0{,}01}\approx0{,}98\%$ — bem menor que os $\approx23\%$ do exemplo da aula, apesar da sensibilidade e especificidade melhores. Prevalência baixa domina até testes excelentes.

**d.** [ ] Como a evidência $p(+)$ é definida como $\sum_k p(+\mid\mathcal{C}_k)p(\mathcal{C}_k)$, ela representa a probabilidade de um resultado positivo vindo especificamente da classe doente.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** A evidência é a probabilidade MARGINAL de um positivo, somada sobre TODAS as classes (doente e saudável) — é o mesmo denominador para qualquer classe do numerador, não uma quantidade específica de uma classe. Confundir a evidência (marginal) com uma conjunta específica é o erro clássico neste ponto da fórmula de Bayes.

---

## A distribuição Beta e detecção de anomalias

**a.** [ ] No limite em que $a\to\infty$ e $b\to\infty$ mantendo $a/(a+b)$ constante, a distribuição Beta se concentra cada vez mais estreitamente em torno de sua média, tendendo a uma distribuição degenerada.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** $\text{Var}=\dfrac{ab}{(a+b)^2(a+b+1)}$; escrevendo $a=kp$, $b=k(1-p)$ com $p$ fixo e $k\to\infty$, a variância se reduz a $\dfrac{p(1-p)}{k+1}\to0$. Mais "pseudo-observações" concentram a distribuição — a mesma lógica por trás de um prior Beta ficando mais "confiante" à medida que mais dados são incorporados.

**b.** [ ] Se os dados de uma folha realmente seguissem uma Beta em forma de U ($a=0{,}5$, $b=0{,}5$), um estimador de momentos ainda recuperaria corretamente esses parâmetros a partir da média e variância amostrais, mesmo sem assumir nada sobre a forma da distribuição.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** O estimador de momentos é uma inversão puramente algébrica de duas equações (média e variância) — não assume unimodalidade nem qualquer forma específica. Dada média e variância populacionais corretas, a fórmula recupera $a=b=0{,}5$ tão bem quanto recuperaria parâmetros de uma Beta unimodal.

**c.** [ ] Num sistema de recomendação que modela a taxa de cliques (CTR) de cada anúncio, a Beta seria uma escolha tão razoável quanto no exemplo de escores de anomalia desta aula, e sofreria da mesma armadilha se algum anúncio tivesse CTR observada de exatamente $0\%$ ou $100\%$.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** CTR é uma aplicação real e padrão de modelos Beta (inclusive combinada com Binomial em modelos Beta-Binomial de ad tech); a mesma patologia de zeros/uns exatos quebrando $\ln(0)$ na verossimilhança se aplica sem qualquer diferença estrutural.

**d.** [ ] Como treinar apenas com dados "normais" permite estimar bem a densidade $p(x\mid\mathcal{C}_A)$, conclui-se que a taxa de detecção (Tipo II) também pode ser calculada diretamente dos dados de treino, sem qualquer suposição adicional sobre as anomalias.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** Estimar bem $p(x\mid\mathcal{C}_A)$ não dá nenhuma informação sobre $p(x\mid\mathcal{C}_B)$ (a densidade das anomalias), que é justamente o que se precisa para calcular a taxa de detecção. Sem dados rotulados de anomalia, esse número exige alguma suposição extra (por exemplo, sobre a forma ou localização de $\mathcal{C}_B$).

---

## Tipos de erro e o limiar de decisão

**a.** [ ] Se, em vez de duas classes unimodais com uma única região de sobreposição, a classe B fosse bimodal (uma "bolha" de densidade de cada lado de A), deslocar o limiar $t$ para a direita poderia, em algum trecho, reduzir simultaneamente as duas taxas de erro.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** No caso unimodal com um único cruzamento (o cenário da aula), mover $t$ para a direita tem uma troca monotônica clara: menos Tipo I, mais Tipo II. Com B bimodal envolvendo A, existe a possibilidade de, ao mover $t$, sair de uma bolha de B (reduzindo Tipo II ali) e ainda se afastar da cauda de A (reduzindo Tipo I também) — a troca monotônica é uma consequência da geometria específica do caso unimodal-com-um-cruzamento, não uma lei geral.

**b.** [ ] No limite em que o limiar captura toda a reta como pertencente a uma única classe, a taxa de erro associada a essa classe vai a zero e a do outro tipo vai a $100\%$, independentemente da forma das densidades.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Se toda a reta é classificada como uma única classe, nenhum ponto dessa classe é classificado errado (erro $0\%$ para ela) e todo ponto da outra classe é classificado errado (erro $100\%$ para ela) — uma consequência puramente da definição de erro, válida para qualquer forma de densidade.

**c.** [ ] Num sistema de triagem de spam, se "Tipo I" for classificar um e-mail legítimo como spam e "Tipo II" for deixar passar um spam verdadeiro, qual rótulo é "Tipo I" depende de qual classe é declarada a hipótese nula — não é uma propriedade fixa do problema.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** É a mesma convenção estatística da aula (Tipo I/Tipo II só fazem sentido depois de escolher a hipótese nula) aplicada a um domínio diferente: se a hipótese nula fosse "é spam" em vez de "é legítimo", os rótulos Tipo I/Tipo II trocariam de lugar, mesmo com a mesma matriz de confusão subjacente.

**d.** [ ] Como aumentar o limiar $t$ tipicamente reduz a taxa de erro Tipo I e aumenta a Tipo II, conclui-se que a soma Tipo I + Tipo II é sempre constante, não importa onde $t$ esteja.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** As duas taxas se movem em direções opostas, mas não necessariamente na mesma "quantidade" — a soma Tipo I + Tipo II tem sua própria forma em função de $t$, com um mínimo em algum ponto específico (relacionado a $T_{CONJ}$, dependendo dos pesos). Se a soma fosse sempre constante, minimizar o erro total não faria sentido como problema — e é exatamente esse problema que os Blocos 2–4 resolvem.

---

## Priori, verossimilhança, evidência e posteriori

**a.** [ ] Se, em vez de duas classes, tivéssemos $K=10$ classes, a evidência $p(x)$ ainda seria calculada somando a conjunta $p(x,\mathcal{C}_j)$ sobre todas as classes, agora com 10 termos.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** A Regra da Soma não é uma peculiaridade do caso $K=2$ — a evidência é sempre $\sum_{j=1}^K p(x,\mathcal{C}_j)$, com quantos termos forem necessários para cobrir todas as classes possíveis.

**b.** [ ] No limite em que $\pi_A\to 1$, a posteriori $p(\mathcal{C}_A\mid x)$ tende a $1$ para qualquer valor observado de $x$, mesmo que $x$ seja um valor típico da classe B.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Com $\pi_B\to 0$, o termo $\pi_B\,p(x\mid\mathcal{C}_B)$ no denominador de Bayes desaparece independentemente do quão bem $x$ se encaixe em B, deixando a posteriori de A dominante — um prior suficientemente extremo pode, no limite, sobrepor-se a qualquer evidência finita.

**c.** [ ] Num tribunal, se o "prior" for a crença de culpa antes de ver evidência e a "verossimilhança" for o quão bem a evidência se encaixa com a culpa, um prior muito baixo de culpa (presunção de inocência) exige evidência proporcionalmente mais forte para produzir uma posteriori de culpa convincente.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** É a mesma mecânica de Bayes vista na triagem médica (prior baixo exige razão de verossimilhança grande para deslocar a posteriori de forma substancial), transferida para um domínio de raciocínio jurídico — uma analogia comum e correta na literatura de raciocínio bayesiano.

**d.** [ ] Como a posteriori é proporcional ao produto entre verossimilhança e priori, duas classes com a mesma verossimilhança $p(x\mid\mathcal{C}_k)$ num ponto $x$ sempre têm posteriores iguais nesse ponto, independentemente das prioris.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** Igualar as verossimilhanças não iguala as posteriores se as prioris forem diferentes — a posteriori é proporcional ao PRODUTO dos dois termos, então diferenças na priori se propagam diretamente para diferenças na posteriori, mesmo com verossimilhanças idênticas.

---

## Densidade vs. probabilidade

**a.** [ ] No limite em que um intervalo $[a,b]$ encolhe para um único ponto, a probabilidade $P(a\le X\le b)$ tende a zero, mesmo que a densidade $p(a)$ seja um número grande (por exemplo, $1000$).

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** $P(a\le X\le b)=\int_a^b p(x)dx \approx p(a)\cdot(b-a)$ para um intervalo estreito; não importa quão grande seja $p(a)$, multiplicar por $(b-a)\to0$ leva o produto a zero. É exatamente a distinção entre densidade (pode ser grande) e probabilidade de um ponto (sempre zero no limite contínuo).

**b.** [ ] Se $X$ fosse uma variável aleatória discreta em vez de contínua, a afirmação "$P(X=x)=0$ para qualquer ponto isolado" deixaria de valer em geral.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** Para variáveis discretas, a função de massa de probabilidade atribui, tipicamente, massa positiva a pontos individuais — é exatamente o que a distingue de uma densidade contínua. $P(X=x)=0$ é uma propriedade das variáveis CONTÍNUAS, não uma lei universal de toda variável aleatória.

**c.** [ ] Numa distribuição Uniforme$[0,\,10^{-6}]$, a densidade dentro do intervalo vale $10^6$, e isso não viola nenhum axioma de probabilidade, pois a integral sobre todo o domínio continua valendo exatamente $1$.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** Densidade $=1/(10^{-6})=10^6$; integral $=10^6\times10^{-6}=1$ — consistente. É a mesma lógica do exemplo Uniforme$[0,0{,}01]$ (densidade $100$) já usado na aula, levada a um extremo ainda mais acentuado.

**d.** [ ] Como a densidade $p(x)$ pode ultrapassar $1$ sem problema algum, conclui-se que ela também pode ser negativa em algum ponto, desde que a integral total sobre o domínio ainda valha $1$.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** Não há restrição de que $p(x)\le1$ (não é um axioma real), mas $p(x)\ge0$ EM TODO PONTO é, sim, um axioma genuíno de qualquer densidade de probabilidade. Confundir uma restrição inexistente ("$\le1$") com a que de fato existe ("$\ge0$") é o erro deste item.

---

## Mudança de variável e o Jacobiano

**a.** [ ] Se a transformação $y=g(x)$ não fosse bijetora (por exemplo, $y=x^2$ com $x$ variando em toda a reta real), a fórmula $p_Y(y)=p_X(g^{-1}(y))|dx/dy|$ ainda poderia ser aplicada diretamente, sem nenhuma modificação.

**Heurística:** Contrafactual
**Resposta:** Falso
**Justificativa:** Para uma transformação não-bijetora, cada $y$ pode ter múltiplos $x$ correspondentes (para $y=x^2$ em toda a reta, $x=\pm\sqrt y$); a fórmula correta soma as contribuições de TODOS os ramos da inversa, não aplica um único ramo cegamente. Ignorar essa soma subestima a densidade transformada.

**b.** [ ] No limite em que a derivada $g'(x)\to 0$ num ponto, a densidade transformada $p_Y(y)$ nesse ponto tende a $+\infty$ (supondo $p_X$ positiva e finita ali).

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** $p_Y(y)=p_X(x)/|g'(x)|$; conforme $g'(x)\to0$, o denominador vai a zero e a razão diverge. É o mecanismo por trás do fator Jacobiano: uma transformação que "achata" localmente comprime probabilidade num intervalo de $y$ cada vez menor, inflando a densidade ali.

**c.** [ ] Ao converter uma distribuição de renda de reais para log(reais), a moda da distribuição pode mudar de posição relativa, mesmo sendo a mesma variável aleatória subjacente, só medida numa escala diferente.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** É exatamente a não-invariância da moda sob reparametrização, aplicada a um caso real e comum (renda vs. log-renda): o fator Jacobiano da transformação $\log$ pesa diferente em diferentes pontos, podendo deslocar onde a densidade transformada atinge seu pico.

**d.** [ ] Como a moda de uma densidade pode mudar sob reparametrização, a decisão de classificação $\arg\max_k p(\mathcal{C}_k\mid x)$ também muda de classe vencedora dependendo de como $x$ é parametrizado.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** É o oposto: comparar POSTERIORES de classes diferentes no mesmo ponto $x$ é diferente de encontrar a MODA de uma única densidade. Ao reparametrizar $x\to y=g(x)$, todas as posteriores concorrentes ganham o MESMO fator Jacobiano multiplicativo, que se cancela na comparação $\arg\max_k$ — por isso a decisão discreta é imune, mesmo que a moda de uma densidade isolada não seja.

---

## Momentos de uma distribuição

**a.** [ ] No limite em que uma distribuição se torna cada vez mais concentrada (variância $\to 0$), sua curtose em excesso não necessariamente tende a zero.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Curtose é um momento PADRONIZADO (a quarta potência dividida pelo quadrado da variância) — depende da FORMA da distribuição, não da sua escala. Uma Uniforme cada vez mais estreita mantém curtose em excesso $-1{,}2$ para sempre, não importa quão pequena fique a variância; concentração não implica "ficar mais parecido com uma Gaussiana".

**b.** [ ] Como distribuições simétricas em torno da média têm *skewness* zero, conclui-se que *skewness* zero implica necessariamente que a distribuição é simétrica.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** É um erro de conversa: simetria $\Rightarrow$ *skewness* zero é verdadeiro, mas a implicação inversa não é — existem distribuições assimétricas cujo terceiro momento padronizado se anula por cancelamento entre desvios positivos e negativos, sem que a distribuição seja simétrica.

**c.** [ ] Numa distribuição de renda familiar (cauda longa à direita), espera-se *skewness* positiva, e a média tende a ficar acima da mediana, não abaixo.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** É um fato bem estabelecido sobre distribuições de renda: a cauda longa à direita (poucas famílias muito ricas) puxa a média para cima, acima da mediana — a assinatura clássica de *skewness* positiva num caso real e comum.

**d.** [ ] Como curtose em excesso zero indica uma cauda comparável à Gaussiana, conclui-se que toda distribuição com curtose em excesso zero deve ser, ela mesma, uma Gaussiana.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** Compartilhar um único momento (o quarto, padronizado) não implica ser a mesma distribuição — existem distribuições não-Gaussianas com curtose em excesso exatamente zero. Um momento é um ponto de comparação, não uma impressão digital completa da distribuição.

---

## Caudas leves vs. pesadas

**a.** [ ] No limite em que os graus de liberdade $\nu$ da distribuição $t$ de Student tendem a infinito, sua cauda deixa de ser mais pesada que a Gaussiana e a distribuição converge para a própria Gaussiana.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** É um resultado clássico: $t_\nu \to \mathcal{N}(0,1)$ conforme $\nu\to\infty$ (a incerteza extra sobre a variância, que gera a cauda pesada, desaparece quando há graus de liberdade suficientes para estimá-la com precisão).

**b.** [ ] Se uma distribuição de cauda pesada fosse usada para modelar erros de medição de um instrumento, eventos a $5\sigma$ de distância da média deixariam de ser "praticamente impossíveis".

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** É exatamente a definição operacional de cauda pesada: decaimento mais lento (polinomial, não exponencial-quadrático) atribui probabilidade não-desprezível a desvios extremos que uma Gaussiana consideraria virtualmente impossíveis.

**c.** [ ] Em mercados financeiros, retornos diários de ações costumam ter caudas mais pesadas que a Gaussiana, consistente com o uso de distribuições como a $t$ de Student em vez da Gaussiana para modelar retornos.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** É um fato amplamente documentado em finanças quantitativas (eventos extremos — "crashes" e "rallies" — muito mais frequentes do que um modelo Gaussiano preveria), e é exatamente por isso que distribuições de cauda mais pesada são usadas nesse domínio.

**d.** [ ] Como a distribuição $t$ de Student com poucos graus de liberdade tem cauda mais pesada que a Gaussiana, ela necessariamente não tem variância finita, para qualquer valor de $\nu$.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** "Cauda mais pesada que a Gaussiana" e "variância infinita" são coisas diferentes: a $t$ de Student com $\nu>2$ tem variância finita ($\nu/(\nu-2)$), apesar de ainda ter cauda mais pesada que a Gaussiana. Só para $\nu\le2$ a variância deixa de ser finita — a afirmação "para qualquer $\nu$" é o exagero que a torna falsa.

---

## Forma fechada vs. máxima verossimilhança (Beta)

**a.** [ ] Se, em vez da Beta, os dados de uma folha realmente seguissem uma distribuição Gaussiana, o MLE dos parâmetros também exigiria um procedimento numérico iterativo, assim como ocorre com a Beta.

**Heurística:** Contrafactual
**Resposta:** Falso
**Justificativa:** O MLE gaussiano tem fórmula fechada (média e variância amostrais, como visto na Aula 3) — não precisa de nenhum procedimento iterativo. É exatamente o contraste que torna a Beta um caso interessante: nem toda distribuição tem essa sorte.

**b.** [ ] No limite em que $a=b$ (Beta simétrica em torno de $0{,}5$), o estimador de momentos produziria uma estimativa de $a$ igual à de $b$ só se a média amostral for exatamente $0{,}5$.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Nas fórmulas do estimador de momentos, $\hat a = \bar x\left(\frac{\bar x(1-\bar x)}{s^2}-1\right)$ e $\hat b=(1-\bar x)\left(\frac{\bar x(1-\bar x)}{s^2}-1\right)$ compartilham o mesmo fator entre parênteses; $\hat a=\hat b$ exige $\bar x=1-\bar x$, ou seja, $\bar x=0{,}5$ exatamente.

**c.** [ ] Ao ajustar uma Beta por máxima verossimilhança num pacote estatístico, o software provavelmente usa um método numérico iterativo para resolver as equações de verossimilhança, em vez de uma fórmula fechada.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** É comportamento padrão e documentado de implementações reais (como `scipy.stats.beta.fit`): como as equações de verossimilhança envolvem a função digama (sem inversa em forma fechada), o ajuste numérico (Newton-Raphson ou similar) é a prática usual.

**d.** [ ] Como o MLE é assintoticamente eficiente e o estimador de momentos, em geral, não é, conclui-se que o estimador de momentos é sempre uma escolha pior, para qualquer tamanho de amostra $N$.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** "Assintoticamente" é uma propriedade de amostras GRANDES; para $N$ pequeno, essa garantia não se aplica, e o estimador de momentos pode ser perfeitamente competitivo (ou até preferível, por evitar problemas numéricos da otimização). Generalizar "sempre pior, para qualquer $N$" ignora a qualificação "assintoticamente" da própria definição.

---

## Armadilha de zeros e uns exatos

**a.** [ ] No limite em que $a\to 0^+$ (mantendo $b$ fixo), a densidade da Beta próxima de $x=0$ diverge cada vez mais rapidamente, tornando uma observação exatamente igual a $0$ ainda mais problemática.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** O termo $x^{a-1}$ na densidade da Beta tem expoente cada vez mais negativo conforme $a\to0^+$, intensificando a divergência perto de $x=0$ — o extremo mais acentuado do problema já identificado para qualquer $a<1$.

**b.** [ ] Se todos os dados de treino, por coincidência, estivessem estritamente dentro do intervalo aberto $(0,1)$ — sem nenhum zero ou um exato —, a armadilha discutida nesta aula deixaria de ser uma preocupação para aquele conjunto específico, mesmo que $a<1$ ou $b<1$.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** A patologia é sobre observações EXATAMENTE em $0$ ou $1$ quebrando o termo logarítmico da verossimilhança — se nenhum ponto observado está exatamente nas bordas, a verossimilhança permanece finita e bem definida em cada ponto, não importa quão pequenos sejam $a$ ou $b$.

**c.** [ ] Num conjunto de avaliações de produtos normalizadas para $[0,1]$ (nota de 0 a 5 estrelas dividida por 5), é comum observar exatamente os valores extremos $0$ e $1$, tornando essa armadilha uma preocupação prática real, não só teórica.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** Notas mínimas e máximas (1 estrela ou 5 estrelas, por exemplo) são comuns em dados de avaliação real — um contraexemplo concreto à ideia de que essa armadilha é "só teórica", desta vez num domínio diferente do exemplo de escores de anomalia da aula.

**d.** [ ] Como o *clipping* para $[\varepsilon,1-\varepsilon]$ é uma correção honesta desde que $\varepsilon$ seja declarado, conclui-se que qualquer escolha de $\varepsilon$ produz resultados de ajuste igualmente bons.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** "Honesta" refere-se à transparência metodológica (a escolha é declarada, não escondida) — isso não garante qualidade numérica: um $\varepsilon$ grande demais distorce os dados originais substancialmente, enquanto um $\varepsilon$ pequeno os perturba pouco. Transparência e qualidade do ajuste são eixos diferentes.

---

## Erro de Bayes e detecção com uma única densidade

**a.** [ ] No limite em que $p(x\mid\mathcal{C}_A)$ e $p(x\mid\mathcal{C}_B)$ se tornam idênticas em todo o domínio, o erro de Bayes tende ao valor máximo possível para um problema de duas classes.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Se as condicionais são idênticas, $x$ não carrega nenhuma informação distintiva entre as classes; o melhor que qualquer classificador pode fazer é sempre prever a classe majoritária, com erro $\min(\pi_A,\pi_B)$ — precisamente o teto do erro de Bayes possível para prioris fixas, atingido exatamente neste caso extremo.

**b.** [ ] Um classificador arbitrariamente complexo (bilhões de parâmetros), treinado com dados infinitos, poderia reduzir o erro de Bayes a zero, mesmo havendo sobreposição real entre as densidades das classes.

**Heurística:** Contrafactual
**Resposta:** Falso
**Justificativa:** O erro de Bayes é um piso irredutível determinado pela sobreposição real das densidades verdadeiras — nenhuma quantidade de capacidade do modelo ou de dados pode superá-lo; mais parâmetros e mais dados aproximam o classificador do limite de Bayes, nunca o ultrapassam.

**c.** [ ] Num sistema de reconhecimento facial em que duas pessoas têm rostos extremamente parecidos (gêmeos idênticos), mesmo o melhor classificador teoricamente possível terá uma taxa de erro irredutível maior que zero para distinguir essas identidades, refletindo a sobreposição real das características faciais.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** É uma instância real e bem conhecida do mesmo princípio: quando a sobreposição entre distribuições de características é genuína (gêmeos idênticos), nenhum classificador — por melhor que seja — escapa do erro de Bayes correspondente a essa sobreposição.

**d.** [ ] Como todo número de "taxa de detecção" de um detector treinado só com dados normais depende de alguma suposição sobre as anomalias, conclui-se que esses detectores nunca são úteis na prática, já que a suposição pode estar errada.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** Depender de uma suposição não é o mesmo que ser inútil — significa que o número reportado deve ser interpretado com essa suposição em mente. Detectores de anomalia treinados só com dados normais são amplamente usados com sucesso na prática (fraude, monitoramento industrial); a conclusão "nunca são úteis" é um exagero que a aula não sustenta.
