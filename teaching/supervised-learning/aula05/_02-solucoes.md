# Soluções — Questões de Verdadeiro/Falso (Aula 5)

> Arquivo de apoio, não publicado (prefixo `_`). Contém a resposta e a
> justificativa de cada item das 12 questões de V/F do `index.qmd`. O
> `index.qmd` publicado continua sem solução — este arquivo existe só
> para conferência do professor/monitor, seguindo a metodologia de
> criação de questões definida em `../../CLAUDE.md`.

### Prioris Reais vs. Sintéticas (Aula 1) — item (a)

**Heurística:** Limite

**Afirmação:** ✔ Se a prevalência real de diabetes nesta população fosse de $0{,}1\%$ em vez de $35{,}1\%$, o cruzamento das conjuntas se deslocaria ainda mais em direção à cauda da distribuição dos diabéticos, tornando o corte ótimo mais extremo do que o observado hoje.

**Resposta:** Verdadeiro

**Justificativa:** Quanto menor a priori da classe rara, maior a evidência relativa exigida para declará-la — o limiar de razão de verossimilhanças $\pi_A/\pi_B$ cresce, empurrando o cruzamento das conjuntas cada vez mais para dentro da cauda da classe rara. É a mesma direção do efeito observado ao ir de $50/50$ para $65/35$ e depois para $95/5$: quanto mais extrema a assimetria, mais extremo o deslocamento.

### Prioris Reais vs. Sintéticas (Aula 1) — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Como a Aula 1 usou uma razão de prioris de $19$ para $1$ e esta aula usa uma razão de aproximadamente $1{,}86$ para $1$, conclui-se que o cruzamento das conjuntas de hoje está estruturalmente mais próximo do cruzamento das condicionais do que estava na Aula 1.

**Resposta:** Verdadeiro

**Justificativa:** Isto é verificável nos números computados: hoje a distância normalizada entre os dois cruzamentos é de aproximadamente $0{,}09$ ($0{,}581 \to 0{,}671$), contra aproximadamente $0{,}25$ na Aula 1 ($0{,}47\to0{,}72$). Quanto mais perto de $1$ a razão de prioris, mais perto os dois cruzamentos ficam um do outro — no limite $\pi_A=\pi_B$, colapsam num só. Não é um item "armadilha": é a mesma conclusão da pausa ativa do Bloco 1, testada de outro ângulo.

### Prioris Reais vs. Sintéticas (Aula 1) — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Num problema de detecção de fraude em que apenas $0{,}5\%$ das transações são fraudulentas, o mesmo argumento do cruzamento de conjuntas (em vez de condicionais) se aplica, mesmo que a variável observada não seja glicose nem tenha suporte em $[0,1]$.

**Resposta:** Verdadeiro

**Justificativa:** O argumento de ponderar cada densidade condicional pela priori da sua classe (PRML eqs. 1.78–1.79) não depende da família distribucional nem do suporte da variável — depende só de existirem densidades condicionais e prioris desiguais. Beta em $[0,1]$ foi só a escolha didática da Aula 1 e desta aula; o princípio geométrico é o mesmo em qualquer domínio com classes desbalanceadas.

### Prioris Reais vs. Sintéticas (Aula 1) — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Já que a Beta ajustada aos diabéticos ($a=3{,}18,\ b=1{,}78$) tem parâmetros diferentes da Beta ajustada aos não-diabéticos ($a=3{,}49,\ b=4{,}50$), isso por si só garante que as duas curvas nunca se cruzam mais de uma vez no intervalo $[0,1]$.

**Resposta:** Falso

**Justificativa:** Parâmetros diferentes não garantem nenhuma contagem específica de cruzamentos — duas densidades contínuas quaisquer podem se cruzar zero, uma, ou várias vezes, dependendo da forma exata de cada curva. O fato de os parâmetros serem diferentes é necessário para que as curvas não sejam idênticas, mas não é suficiente para limitar o número de cruzamentos a um só.

### Beta como Estimador de Densidade (Aula 1) — item (a)

**Heurística:** Limite

**Afirmação:** ✔ No limite em que $a=b=1$, a distribuição Beta se reduz à uniforme em $[0,1]$, e o ajuste por máxima verossimilhança deixaria de conseguir distinguir as duas classes por qualquer diferença de forma.

**Resposta:** Verdadeiro

**Justificativa:** $\text{Beta}(1,1)$ é, por definição, a densidade uniforme em $[0,1]$. Se as duas classes convergissem para esse caso, as duas curvas ajustadas seriam idênticas (ambas planas), e nenhuma informação de forma restaria para separar as classes — toda a discriminação teria que vir só das prioris.

### Beta como Estimador de Densidade (Aula 1) — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Se, em vez de ajustar uma Beta por máxima verossimilhança, alguém decidisse usar a média e o desvio-padrão amostrais para "adivinhar" $a$ e $b$ por um método de momentos, o resultado coincidiria exatamente com o obtido por `scipy.stats.beta.fit`, porque ambos otimizam a mesma função.

**Resposta:** Falso

**Justificativa:** Método de momentos e máxima verossimilhança são estimadores diferentes, que só coincidem por acaso em casos especiais (como a própria Gaussiana). Para a Beta, as estatísticas suficientes do MLE são $\sum\ln x_n$ e $\sum\ln(1-x_n)$ — não a média e a variância amostrais — e é exatamente por isso que a Aula 1 apontou que a Beta não tem MLE em forma fechada via momentos simples.

### Beta como Estimador de Densidade (Aula 1) — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Num sensor industrial que mede uma proporção (por exemplo, fração de peças defeituosas por lote, sempre em $[0,1]$), o mesmo ajuste de Beta por classe (lote bom vs. lote ruim) se aplicaria naturalmente, sem exigir Gaussiana ou outra família com suporte ilimitado.

**Resposta:** Verdadeiro

**Justificativa:** A Beta é a família natural para variáveis com suporte fechado em $[0,1]$, precisamente porque respeita esse limite (uma Gaussiana atribuiria probabilidade positiva a valores fora de $[0,1]$, o que não faz sentido para uma proporção). A mecânica de ajuste é idêntica à usada com Glicose normalizada.

### Beta como Estimador de Densidade (Aula 1) — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como a Beta ajustada aos não-diabéticos tem $b_0=4{,}50 > a_0=3{,}49$, conclui-se que essa distribuição é necessariamente simétrica em torno de $0{,}5$.

**Resposta:** Falso

**Justificativa:** $\text{Beta}(a,b)$ é simétrica em torno de $0{,}5$ apenas quando $a=b$. Aqui $a_0=3{,}49 \ne b_0=4{,}50$, então a distribuição é assimétrica (levemente deslocada para a esquerda de $0{,}5$) — a desigualdade $b_0>a_0$ não implica simetria alguma, implica exatamente o contrário.

### Erro Tipo I/II e Assimetria de Custos (Aula 1) — item (a)

**Heurística:** Limite

**Afirmação:** ✔ No limite em que o custo de um escape (diabético não identificado) tende a infinito relativamente ao custo de um alarme falso, o limiar de decisão ótimo se deslocaria para a esquerda, classificando cada vez mais pacientes como diabéticos até declarar quase todos positivos.

**Resposta:** Verdadeiro

**Justificativa:** No limiar de custo ponderado ($C_I\pi_A f_A(t)=C_{II}\pi_B f_B(t)$), fazer $C_{II}\to\infty$ força o limiar a se mover para minimizar a área de escape a quase qualquer preço em alarmes falsos — no limite extremo, declarar todo mundo diabético elimina os escapes por completo, ao custo de maximizar os alarmes falsos.

### Erro Tipo I/II e Assimetria de Custos (Aula 1) — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Se um exame de triagem fosse ajustado para ter exatamente zero alarmes falsos, isso garantiria automaticamente que ele também tem poucos escapes, já que os dois tipos de erro tendem a se mover na mesma direção quando o limiar muda.

**Resposta:** Falso

**Justificativa:** É exatamente o oposto do que a Aula 1 estabeleceu como o compromisso fundamental: mover o limiar troca uma área de erro pela outra, nunca reduz as duas juntas. Zero alarmes falsos normalmente exige um limiar extremo que maximiza os escapes, não os minimiza.

### Erro Tipo I/II e Assimetria de Custos (Aula 1) — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Num sistema de moderação de conteúdo automatizado que decide entre "remover" e "manter" uma postagem, a mesma lógica de troca entre Erro Tipo I (remover conteúdo legítimo) e Erro Tipo II (manter conteúdo problemático) se aplica, com custos claramente diferentes conforme o contexto da plataforma.

**Resposta:** Verdadeiro

**Justificativa:** É a mesma estrutura de custo assimétrico entre dois tipos de erro, só que fora do domínio médico — moderação de conteúdo é um exemplo padrão onde a escolha de limiar reflete uma decisão de negócio/política sobre qual erro custa mais, exatamente como na triagem.

### Erro Tipo I/II e Assimetria de Custos (Aula 1) — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como o corte pela conjunta (Bloco 1 desta aula) reduziu o número total de erros em relação ao corte pelas condicionais, conclui-se que ele é a escolha certa independentemente de qualquer consideração sobre o custo relativo de alarmes falsos e escapes.

**Resposta:** Falso

**Justificativa:** Minimizar a contagem total de erros (perda 0-1) só é a escolha certa quando os dois tipos de erro têm o mesmo custo. Sob custos assimétricos — como o cenário de triagem discutido no Bloco 2 — o limiar correto é o ponderado pelo custo, não necessariamente o que minimiza o número bruto de erros.

### Independência Condicional: Preço Variável (Aula 2) — item (a)

**Heurística:** Limite

**Afirmação:** ✔ Se, em vez de Glicose e IMC, o Bloco 2 tivesse usado dois atributos definidos de forma redundante (por exemplo, "IMC em kg/m²" e "IMC em unidades arbitrárias que são o dobro do IMC em kg/m²"), a correlação intra-classe entre eles seria próxima de $1$, e a suposição de independência do Naive Bayes pagaria um preço bem maior do que o observado hoje.

**Resposta:** Verdadeiro

**Justificativa:** Dois atributos redundantes (um sendo função linear exata do outro) têm correlação $1$; a covariância diagonal ignoraria essa dependência completa, tratando informação duplicada como duas fontes independentes — o pior caso possível para a suposição de independência.

### Independência Condicional: Preço Variável (Aula 2) — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como o Naive Bayes produziu exatamente a mesma acurácia que a Gaussiana de covariância plena no Pima (Glicose/IMC), conclui-se que, para qualquer par de atributos deste dataset, a suposição de independência condicional nunca custaria nada.

**Resposta:** Falso

**Justificativa:** O resultado vale para o par (Glicose, IMC), que por acaso tem correlação intra-classe baixa. Outros pares de atributos do mesmo dataset (por exemplo, Insulina e Glicose, fisiologicamente ligadas) podem ter correlação bem mais alta e, portanto, um preço de independência bem maior — generalizar de um par para "qualquer par" é o erro de inferência aqui.

### Independência Condicional: Preço Variável (Aula 2) — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Num modelo de triagem de spam que assume independência condicional entre a presença das palavras "grátis" e "promoção" dado o rótulo (spam/não-spam), o preço dessa suposição dependeria de quão correlacionadas essas duas palavras realmente são dentro de cada classe — a mesma lógica do Bloco 2, fora do domínio médico.

**Resposta:** Verdadeiro

**Justificativa:** É a mesma mecânica do Bloco 2 (e do exemplo "grátis/ganhador" da Aula 2): o preço da independência condicional é proporcional à correlação real ignorada, não uma constante do método Naive Bayes.

### Independência Condicional: Preço Variável (Aula 2) — item (d)

**Heurística:** Limite

**Afirmação:** ✔ Se duas variáveis fossem independentes tanto na classe A quanto na classe B, mas com médias diferentes entre as classes, a Gaussiana de covariância diagonal (Naive Bayes) ainda poderia separar as duas classes razoavelmente bem, sem qualquer prejuízo vindo da suposição de independência.

**Resposta:** Verdadeiro

**Justificativa:** Se a independência condicional é genuína (não uma simplificação, mas um fato dos dados), a covariância diagonal não descarta nenhuma informação real — a separação entre classes vem inteiramente da diferença de médias, que a covariância diagonal captura sem perdas.

### Teoria da Decisão e Risco Posterior (Aula 2) — item (a)

**Heurística:** Limite

**Afirmação:** ✔ Se a matriz de perdas $L(k,a)$ atribuísse custo zero a todo acerto e custo idêntico a qualquer tipo de erro (Tipo I ou Tipo II), o limiar de decisão que minimiza o risco posterior $\rho(a\mid x)$ coincidiria com o limiar de $0{,}5$ de probabilidade posterior.

**Resposta:** Verdadeiro

**Justificativa:** Com perda $0$-$1$ simétrica, minimizar o risco posterior se reduz a escolher a classe de maior probabilidade posterior (regra MAP) — no caso binário, isso é exatamente declarar a classe com posteriori $>0{,}5$.

### Teoria da Decisão e Risco Posterior (Aula 2) — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Num cenário em que o custo de um escape é dez vezes o custo de um alarme falso, o limiar ótimo de probabilidade posterior para declarar "diabético" seria maior do que $0{,}5$, tornando mais difícil, não mais fácil, declarar a classe rara.

**Resposta:** Falso

**Justificativa:** É o inverso do resultado correto. O limiar ótimo é $c_I/(c_I+c_{II})$; com $c_{II}$ (custo do escape) dez vezes maior que $c_I$, o limiar cai bem abaixo de $0{,}5$ — fica *mais fácil*, não mais difícil, declarar a classe rara, porque o custo de deixar passar um caso positivo é alto.

### Teoria da Decisão e Risco Posterior (Aula 2) — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Numa seguradora que decide entre "aceitar apólice" e "recusar apólice" com custos assimétricos entre aceitar um mau pagador e recusar um bom pagador, a mesma estrutura de risco posterior $\rho(a\mid x)=\sum_k L(k,a)p(\mathcal{C}_k\mid x)$ se aplica, com a mesma lógica de deslocamento de limiar por assimetria de custo.

**Resposta:** Verdadeiro

**Justificativa:** É a mesma formalização de decisão sob risco, com uma matriz de perdas específica do domínio de crédito/seguros no lugar da matriz médica — a estrutura matemática (e o deslocamento de limiar por assimetria) é idêntica.

### Teoria da Decisão e Risco Posterior (Aula 2) — item (d)

**Heurística:** Limite

**Afirmação:** ✗ Como o risco de Bayes $R^\star$ é definido como o valor esperado do risco posterior mínimo sobre a distribuição de $X$, ele é sempre estritamente positivo, mesmo quando as classes não se sobrepõem em nenhum ponto do espaço de atributos.

**Resposta:** Falso

**Justificativa:** Se as densidades condicionais de classe não se sobrepõem em ponto alguma, existe uma partição do espaço que classifica tudo corretamente, e o risco posterior mínimo é zero em todo $x$ — logo $R^\star=0$, não estritamente positivo. Sobreposição é precisamente a condição que gera erro de Bayes irredutível; sem ela, o erro de Bayes desaparece.

### Naive Bayes: Generativo, Não Discriminativo (Aula 2) — item (a)

**Heurística:** Limite

**Afirmação:** ✔ Se um modelo generativo (como o Naive Bayes Gaussiano) estimar $p(\mathbf{x}\mid\mathcal{C}_k)$ e $\pi_k$ corretamente para cada classe, ele automaticamente também é capaz de gerar novos exemplos sintéticos plausíveis de cada classe, amostrando dessas densidades — capacidade que um classificador puramente discriminativo, que só estima $p(\mathcal{C}_k\mid\mathbf{x})$ diretamente, não tem por construção.

**Resposta:** Verdadeiro

**Justificativa:** É a definição operacional de "generativo": modelar a densidade completa dos dados por classe permite amostrar dela. Um modelo discriminativo nunca modela $p(\mathbf{x}\mid\mathcal{C}_k)$, só a fronteira/posteriori — não tem de onde amostrar novos $\mathbf{x}$.

### Naive Bayes: Generativo, Não Discriminativo (Aula 2) — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como o Naive Bayes é um modelo generativo, ele necessariamente tem acurácia de classificação igual ou maior do que qualquer modelo discriminativo treinado com os mesmos dados.

**Resposta:** Falso

**Justificativa:** É o contrário da lição "classifica bem, estima mal" — na prática, modelos discriminativos frequentemente superam modelos generativos em acurácia pura, especialmente quando a suposição distribucional do generativo (aqui, independência condicional) está incorreta. Ser generativo não é uma garantia de superioridade preditiva.

### Naive Bayes: Generativo, Não Discriminativo (Aula 2) — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Num cenário de poucos dados de treino, a estrutura extra imposta por um modelo generativo (como a fatoração de independência do Naive Bayes) pode compensar a falta de dados o suficiente para superar um modelo discriminativo mais flexível mas sem essa estrutura — o mesmo tipo de troca "menos flexibilidade, mais parcimônia" discutida no Bloco 3 desta aula sobre árvores.

**Resposta:** Verdadeiro

**Justificativa:** É um resultado conhecido na literatura (Ng & Jordan, 2001): modelos generativos com menos parâmetros efetivos podem convergir mais rápido com poucos dados, mesmo perdendo para discriminativos flexíveis quando há dados abundantes — a mesma troca entre parcimônia e flexibilidade que aparece na comparação entre árvores simples e complexas.

### Naive Bayes: Generativo, Não Discriminativo (Aula 2) — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Se duas classes tiverem exatamente a mesma densidade condicional $p(\mathbf{x}\mid\mathcal{C}_k)$, mas prioris diferentes, um modelo generativo ainda conseguiria, em princípio, produzir uma fronteira de decisão não trivial entre elas, baseada só na diferença de prioris.

**Resposta:** Falso

**Justificativa:** Se as densidades condicionais são idênticas em todo $x$, a razão $p(x\mid\mathcal{C}_A)/p(x\mid\mathcal{C}_B)$ é constante ($=1$) em todo o espaço, e a decisão ótima favorece a classe de maior priori **em todo ponto**, sem variar com $x$ — não há fronteira alguma (nem trivial nem não trivial): uma única classe domina o espaço inteiro.

### Impureza como Verossimilhança (Aula 3) — item (a)

**Heurística:** Limite

**Afirmação:** ✔ Se todas as folhas de uma árvore de classificação tivessem exatamente $\hat p_{\tau k}=1$ para alguma classe $k$ e $0$ para as demais (pureza total), a entropia de cada folha seria zero e a log-verossimilhança do modelo, avaliada nos próprios dados de treino, seria a maior possível ($0$, já que $\ln 1=0$).

**Resposta:** Verdadeiro

**Justificativa:** Pureza total dá $H(\hat p_\tau)=0$ e, pela identidade $\ell_\tau(\hat p_\tau)=-N_\tau H(\hat p_\tau)$, log-verossimilhança $=0$ — o máximo teórico, já que $\ln(\text{probabilidade})\le 0$ sempre, com igualdade só quando a probabilidade prevista para a classe verdadeira de cada ponto é exatamente $1$.

### Impureza como Verossimilhança (Aula 3) — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como reduzir entropia é equivalente a maximizar a log-verossimilhança categórica ($\ell_\tau(\hat p_\tau)=-N_\tau H(\hat p_\tau)$), qualquer split que reduza a entropia ponderada também reduz necessariamente o erro bruto de classificação (proporção de pontos mal classificados pela regra de majoritária).

**Resposta:** Falso

**Justificativa:** É exatamente o que o contraexemplo deliberado da Aula 3 mostrou: dois splits podem ter o mesmo erro bruto ($0{,}25$ em ambos) mas ganhos de informação bem diferentes ($0{,}216$ contra $0{,}131$ nats). A equivalência é entre impureza (entropia/Gini) e verossimilhança — não entre impureza e erro bruto de classificação, que são medidas distintas e podem discordar.

### Impureza como Verossimilhança (Aula 3) — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Num modelo de regressão logística ajustado por máxima verossimilhança (fora do escopo desta aula, mas análogo em espírito), a mesma lógica de "ajustar parâmetros para maximizar a probabilidade dos dados observados" se aplicaria, ainda que a forma funcional da verossimilhança seja diferente da categórica usada nas folhas de uma árvore.

**Resposta:** Verdadeiro

**Justificativa:** MLE é um princípio geral, não exclusivo de árvores — regressão logística maximiza uma verossimilhança de Bernoulli condicionada linearmente nos atributos; a forma funcional muda, o princípio de ajuste (maximizar a probabilidade dos dados observados) não.

### Impureza como Verossimilhança (Aula 3) — item (d)

**Heurística:** Limite

**Afirmação:** ✗ Se duas folhas tivessem o mesmo número de pontos $N_\tau$ e a mesma proporção majoritária $\hat p_{\tau,\text{maj}}$, elas teriam necessariamente a mesma entropia e o mesmo Gini, independentemente de qualquer outra diferença entre elas.

**Resposta:** Falso

**Justificativa:** No caso binário (como o Pima, diabético/não-diabético), a afirmação seria verdadeira, porque $H(p)=H(1-p)$ e $\text{Gini}(p)=\text{Gini}(1-p)$ são funções simétricas em torno de $0{,}5$ e dependem só de $p_{\text{maj}}$. Mas a afirmação foi escrita sem restringir a $K=2$ classes — com $K>2$, duas folhas podem ter a mesma proporção majoritária e distribuir o restante da massa entre as classes minoritárias de formas muito diferentes (concentrada numa só, ou espalhada por várias), produzindo entropias e Ginis diferentes. A generalização de um fato binário para qualquer $K$ é o erro aqui.

### Miopia Gulosa e Interações (Aula 3) — item (a)

**Heurística:** Limite

**Afirmação:** ✔ Se dois atributos só forem informativos em **combinação** (por exemplo, "Glicose alta E IMC alto" prediz diabetes, mas nenhum dos dois isoladamente prediz bem), um algoritmo guloso de árvore pode demorar mais splits — ou nunca — para capturar essa interação, comparado a um cenário em que cada atributo já é informativo isoladamente.

**Resposta:** Verdadeiro

**Justificativa:** É a assinatura clássica da miopia gulosa (padrão tipo XOR): como o algoritmo escolhe o melhor split imediato por variável isolada, uma interação que só aparece na combinação de duas variáveis pode não gerar ganho de informação suficiente em nenhum split individual para ser escolhida — o algoritmo pode nunca "ver" a interação.

### Miopia Gulosa e Interações (Aula 3) — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como a árvore do Bloco 3 encontrou um split de raiz com ganho de informação positivo, isso garante que esse mesmo split apareceria na raiz de qualquer árvore treinada com um subconjunto diferente, mas ainda representativo, dos mesmos pacientes.

**Resposta:** Falso

**Justificativa:** É a instabilidade estrutural que a Aula 3 demonstrou explicitamente: no experimento de perturbação daquela aula, remover apenas $5$ de $398$ pontos deslocou o limiar da raiz de forma visível. Um split "ótimo" numa amostra não vem com garantia de estabilidade sob reamostragem, mesmo que a amostra alternativa seja igualmente representativa.

### Miopia Gulosa e Interações (Aula 3) — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Num algoritmo de busca de rotas que escolhe, a cada cruzamento, a rua que parece mais rápida sem simular o trajeto completo até o destino, a mesma limitação de miopia gulosa das árvores de decisão se aplica — a melhor escolha local não garante a melhor rota global.

**Resposta:** Verdadeiro

**Justificativa:** É a mesma estrutura algorítmica (decisão gulosa local sem simulação do resultado futuro completo), fora do domínio de árvores — a analogia captura corretamente por que otimalidade local não implica otimalidade global em qualquer busca gulosa.

### Miopia Gulosa e Interações (Aula 3) — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Se a árvore permitisse profundidade ilimitada (uma folha por paciente), a miopia gulosa deixaria de ser um problema, porque toda combinação de atributos relevante acabaria sendo capturada em algum nível suficientemente profundo da árvore.

**Resposta:** Falso

**Justificativa:** Profundidade ilimitada resolve um problema diferente (capacidade/memorização, levando a overfitting) — não resolve a miopia, que é sobre a *ordem e o critério* de escolha de cada split, não sobre quantos splits são permitidos. Uma árvore muito profunda ainda pode ter sido guiada por escolhas gulosas subótimas nos primeiros níveis, só que agora também memoriza ruído.

### Axis-Aligned vs. Elipses (Aulas 2 e 3) — item (a)

**Heurística:** Limite

**Afirmação:** ✔ Se a fronteira de decisão verdadeira entre duas classes fosse exatamente uma reta na diagonal do espaço de atributos (não paralela a nenhum eixo), uma árvore de decisão precisaria, em geral, de mais splits para aproximá-la do que uma Gaussiana com covariância plena adequadamente ajustada.

**Resposta:** Verdadeiro

**Justificativa:** É a limitação estrutural nomeada na Aula 3: splits axis-aligned só conseguem aproximar uma fronteira diagonal por uma escada de cortes perpendiculares aos eixos, exigindo cada vez mais splits para reduzir o erro de aproximação, enquanto uma Gaussiana de covariância plena (equivalente a uma fronteira linear inclinada, no caso LDA) representa a diagonal exatamente com uma única fronteira.

### Axis-Aligned vs. Elipses (Aulas 2 e 3) — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como a árvore do Bloco 3 e a Gaussiana do Bloco 2 usam exatamente os mesmos dois atributos (Glicose e IMC), suas fronteiras de decisão são necessariamente muito parecidas visualmente, independentemente da forma funcional de cada modelo.

**Resposta:** Falso

**Justificativa:** Usar os mesmos atributos não implica fronteiras parecidas — a forma funcional de cada modelo (staircase axis-aligned da árvore vs. elipse/linha inclinada da Gaussiana) determina o formato da fronteira de decisão, não apenas quais variáveis entram nela.

### Axis-Aligned vs. Elipses (Aulas 2 e 3) — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Num problema de visão computacional em que a fronteira de decisão relevante depende de uma combinação linear de pixels vizinhos (não alinhada aos eixos originais da imagem), a mesma limitação estrutural das árvores axis-aligned se aplicaria, favorecendo modelos capazes de fronteiras oblíquas.

**Resposta:** Verdadeiro

**Justificativa:** A limitação de fronteiras axis-aligned é sobre a geometria da partição, não sobre o domínio específico — qualquer fronteira que dependa de combinações lineares de atributos originais (pixels, aqui) sofre da mesma ineficiência de aproximação por uma árvore de decisão.

### Axis-Aligned vs. Elipses (Aulas 2 e 3) — item (d)

**Heurística:** Limite

**Afirmação:** ✔ Se um conjunto de dados tiver uma fronteira de decisão verdadeiramente alinhada aos eixos (por exemplo, "diabético se, e somente se, Glicose $>140$"), a árvore de decisão deveria, em geral, precisar de menos splits para representá-la do que uma Gaussiana de covariância plena precisaria de parâmetros ajustados para aproximá-la bem.

**Resposta:** Verdadeiro

**Justificativa:** É o complemento exato do item (a): quando a fronteira verdadeira já é um corte reto perpendicular a um eixo, um único split da árvore a representa exatamente, enquanto uma Gaussiana precisaria aproximar esse "degrau" abrupto com uma superfície suave, tipicamente com mais erro residual ou exigindo covariâncias artificiais para se aproximar do corte reto.

### Erro de Treino e Validação (Aula 4) — item (a)

**Heurística:** Limite

**Afirmação:** ✔ Se a árvore do Bloco 3 tivesse sido avaliada apenas nos dados de treino usados para ajustá-la, a acurácia relatada ($77{,}4\%$) seria uma estimativa otimista do desempenho esperado em pacientes novos, mesmo sem qualquer intenção de enganar.

**Resposta:** Verdadeiro

**Justificativa:** É a tese central da Aula 4: $\hat R(\theta)$ é enviesado para baixo (otimista) sempre que $\theta$ foi escolhido observando os mesmos dados usados para calcular $\hat R$ — não é uma questão de intenção, é uma consequência estrutural do procedimento de ajuste.

### Erro de Treino e Validação (Aula 4) — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como a acurácia de teste ($75{,}2\%$) desta árvore é menor que a acurácia de treino ($77{,}4\%$), a diferença de $2{,}2$ pontos percentuais garante, por si só, que este modelo está sofrendo de overfitting severo, no mesmo grau do experimento de profundidade $15$ da Aula 4.

**Resposta:** Falso

**Justificativa:** Um gap de $2{,}2$ pontos percentuais é uma diferença modesta, típica de generalização normal — muito distante do padrão de overfitting severo do experimento de profundidade $15$ (treino em $100\%$, memorização completa). A mera existência de um gap não determina sua severidade; magnitude importa.

### Erro de Treino e Validação (Aula 4) — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Num sistema de aprovação de crédito treinado com dados históricos e nunca reavaliado com clientes novos, o mesmo viés otimista do erro de treino se aplicaria à métrica interna de acurácia usada pela equipe de desenvolvimento.

**Resposta:** Verdadeiro

**Justificativa:** O viés do erro de treino é uma propriedade do procedimento de medição (medir no mesmo dado que ajustou o modelo), não do domínio médico — aplica-se a qualquer sistema preditivo avaliado só nos dados de treino, incluindo crédito.

### Erro de Treino e Validação (Aula 4) — item (d)

**Heurística:** Limite

**Afirmação:** ✗ Se um modelo tivesse acurácia de treino e de teste exatamente iguais, isso provaria que o modelo generaliza perfeitamente para qualquer paciente futuro, não só para os presentes no conjunto de teste usado.

**Resposta:** Falso

**Justificativa:** O conjunto de teste é, ele mesmo, uma amostra finita com variabilidade amostral própria — igualdade entre treino e teste numa amostra específica não elimina a incerteza sobre o risco esperado populacional $R(\theta)$, exatamente o motivo pelo qual a CV e o Bootstrap desta aula existem: para quantificar essa incerteza remanescente, não para eliminá-la com um único número coincidente.

### Duas Perguntas do Bootstrap (Aula 4) — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Se o objetivo fosse responder "quão confiável é a acurácia de $75{,}2\%$ medida no meu conjunto de teste fixo, sem retreinar nada", a técnica correta seria reamostrar as previsões do teste com reposição, não reamostrar e reajustar o conjunto de treino.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente a primeira das duas aplicações do Bootstrap discutidas nesta aula: fixar o modelo e reamostrar as previsões do teste mede a incerteza de medição daquele número específico, sem envolver o processo de ajuste.

### Duas Perguntas do Bootstrap (Aula 4) — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como as duas aplicações do Bootstrap desta aula (reamostrar teste vs. reamostrar+reajustar treino) produziram intervalos de confiança parcialmente sobrepostos ($[69{,}0\%,81{,}0\%]$ e $[69{,}2\%,77{,}9\%]$), conclui-se que elas estão, na prática, respondendo à mesma pergunta estatística.

**Resposta:** Falso

**Justificativa:** Sobreposição numérica de intervalos não implica identidade conceitual das perguntas — uma mede incerteza de medição de uma acurácia fixa, a outra mede instabilidade do procedimento de ajuste em si. Podem coincidir numericamente numa amostra específica e ainda serem, estruturalmente, respostas a perguntas diferentes.

### Duas Perguntas do Bootstrap (Aula 4) — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Numa pesquisa médica que quer saber não só "qual é a acurácia deste modelo específico" mas "quão instável é o processo de treinar este tipo de modelo nesta população", reamostrar e reajustar o conjunto de treino é a técnica mais adequada, não reamostrar só as previsões de um modelo já fixo.

**Resposta:** Verdadeiro

**Justificativa:** É a segunda aplicação do Bootstrap discutida — reamostrar e reajustar o treino simula "o que aconteceria se treinássemos de novo com uma amostra ligeiramente diferente da mesma população", exatamente a pergunta sobre instabilidade do procedimento, não sobre um modelo já fixo.

### Duas Perguntas do Bootstrap (Aula 4) — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Se o intervalo de confiança do Bootstrap para uma estatística for muito largo, isso significa necessariamente que o código do Bootstrap tem um erro de implementação, já que reamostragem com reposição deveria sempre produzir intervalos estreitos.

**Resposta:** Falso

**Justificativa:** Um intervalo largo é frequentemente um resultado legítimo — reflete alta variância amostral genuína (amostra pequena, estatística instável), não um bug. Reamostragem com reposição não tem nenhuma garantia embutida de produzir intervalos estreitos; ela estima a variabilidade real, seja ela pequena ou grande.

### Vazamento de Dados e Relato Honesto (Aula 4) — item (a)

**Heurística:** Limite

**Afirmação:** ✔ No limite em que a normalização de atributos (subtrair a média, dividir pelo desvio-padrão) for calculada usando a amostra inteira antes do split de validação cruzada, em vez de dentro de cada fold, a estimativa de erro produzida se aproxima da estimativa otimista do erro de treino, mesmo que nenhum rótulo seja usado diretamente nesse cálculo.

**Resposta:** Verdadeiro

**Justificativa:** Vazamento não exige uso direto dos rótulos — qualquer transformação (mesmo não supervisionada, como normalização) calculada com dados que incluem o fold de validação deixa esse fold "contaminado" por informação que deveria ser invisível, aproximando o resultado do otimismo do erro de treino.

### Vazamento de Dados e Relato Honesto (Aula 4) — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como o experimento de vazamento do ESL (Aula 4) usou rótulos artificialmente aleatórios só para tornar o efeito visível com clareza didática, conclui-se que esse tipo de vazamento não ocorre em datasets reais, onde o rótulo tem relação genuína com os atributos.

**Resposta:** Falso

**Justificativa:** O uso de rótulos aleatórios foi um recurso didático para isolar e exagerar o efeito (tornando visível que o "sinal" detectado era puro artefato do vazamento), mas o mecanismo do vazamento — selecionar atributos usando dados que depois entram no fold de validação — ocorre igualmente em datasets com relação real entre rótulo e atributos; ele infla a estimativa de desempenho de qualquer forma, só que de um jeito mais difícil de perceber quando já existe sinal genuíno.

### Vazamento de Dados e Relato Honesto (Aula 4) — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Numa competição de previsão de preços de imóveis em que os participantes normalizam os atributos usando toda a base disponível antes de fazer sua própria validação cruzada interna, o mesmo mecanismo de vazamento de informação da Aula 4 se aplica, mesmo fora do domínio médico desta aula.

**Resposta:** Verdadeiro

**Justificativa:** O mecanismo de vazamento (transformação aprendida fora do fold, aplicada dentro dele) não depende do domínio — aplica-se a qualquer pipeline de validação cruzada em que uma etapa de pré-processamento "vê" dados que deveriam estar isolados em cada fold.

### Vazamento de Dados e Relato Honesto (Aula 4) — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Reportar somente a média da acurácia de validação cruzada, sem o desvio-padrão, produz um número tecnicamente correto (a média está certa), então essa prática não constitui um problema de honestidade estatística — é apenas uma escolha de estilo de relatório, sem custo prático.

**Resposta:** Falso

**Justificativa:** A Aula 4 tratou isso explicitamente como um problema real, não estilístico: omitir o desvio-padrão esconde a incerteza da estimativa, dando uma falsa sensação de precisão — o número da média pode estar "correto" e ainda assim induzir uma decisão errada (por exemplo, preferir um modelo cuja média é ligeiramente maior, mas cuja variabilidade também é bem maior).
