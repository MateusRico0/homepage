# Soluções — Exercícios de Verdadeiro/Falso (Aula 1)

> Arquivo de apoio, não publicado (prefixo `_`). Contém a heurística e a
> justificativa de cada item de V/F da seção "Exercícios" do `index.qmd`.
> O `index.qmd` publicado nunca tem essa resolução — é trabalho do aluno
> resolver por conta, fora do horário de aula.

### Profiling sem rótulos e distribuição empírica vs. teórica — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se decidíssemos usar diretamente a distribuição empírica (sem ajustar nenhuma família teórica) para decidir o que é típico, o resultado seria imune ao problema de ruído em regiões com poucos dados — já que a distribuição empírica é "literalmente o que foi observado".

**Resposta:** Falso

**Justificativa:** É exatamente o oposto. A aula afirma diretamente que a distribuição empírica "é ruidosa (poucos dados numa região dão uma estimativa tremendamente instável)". Ser "literalmente o que foi observado" não protege contra ruído — na verdade, é a fonte dele: regiões com poucos dados dão estimativas instáveis exatamente porque não há nada para suavizar o efeito de amostras pequenas. O aluno que confunde "nunca está errada" (uma afirmação sobre fidelidade aos dados observados) com "imune a ruído" (uma afirmação sobre estabilidade estatística) comete o erro central deste item.

### Profiling sem rótulos e distribuição empírica vs. teórica — item (b)

**Heurística:** Caso limite/extremo

**Afirmação:** ✗ No limite em que o número de observações $N$ tende a infinito, a diferença prática entre usar a distribuição empírica diretamente e ajustar uma família teórica (Gaussiana) tende a desaparecer completamente, mesmo se a verdadeira distribuição dos dados não for Gaussiana.

**Resposta:** Falso

**Justificativa:** $N\to\infty$ resolve o problema de *ruído* de estimação (a distribuição empírica fica cada vez mais estável e informativa), mas não resolve um problema de *especificação*: se a família teórica escolhida (Gaussiana) não é a forma verdadeira dos dados, ajustá-la sempre produzirá uma descrição sistematicamente errada, não importa quantos dados existam. Mais dados reduzem variância de estimação, não corrigem viés de forma funcional — a mesma lição repetida ao longo da aula ("a suposição pode estar errada... um tema que volta na aula inteira").

### Profiling sem rótulos e distribuição empírica vs. teórica — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um sistema de detecção de fraude em cartões de crédito que descreve o comportamento "típico" de um usuário a partir do histórico de transações, para depois flagar desvios, está aplicando a mesma lógica de *profiling* desta aula, mesmo sem envolver sensores de temperatura ou vibração.

**Resposta:** Verdadeiro

**Justificativa:** *Profiling* é definido na aula de forma abstrata — "descrever o comportamento típico de uma população... para depois reconhecer o que se desvia dela" — sem depender do domínio específico (sensores de máquina). Detecção de fraude em transações segue exatamente essa estrutura: descrever o comportamento típico do usuário, depois flagar desvios. É transferência direta da mesma lógica para outro domínio.

### Profiling sem rótulos e distribuição empírica vs. teórica — item (d)

**Heurística:** Falsa dicotomia/falsa equivalência

**Afirmação:** ✗ Como a distribuição empírica "nunca está errada" (é literalmente o que foi observado), isso significa que ela é sempre a melhor escolha para descrever o comportamento típico de uma população, superior a qualquer família teórica ajustada.

**Resposta:** Falso

**Justificativa:** "Nunca estar errada" (ser uma descrição fiel do que foi observado) não é o mesmo que "ser a melhor ferramenta" — a aula lista explicitamente dois problemas práticos da distribuição empírica (ruído, incapacidade de generalizar para pontos não observados) que a tornam pior, na prática, do que uma família teórica bem escolhida. Fidelidade aos dados observados e utilidade prática são propriedades diferentes; confundir as duas é a falsa equivalência deste item.

### A Gaussiana multivariada: parâmetros e geometria — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se $\Sigma$ fosse a matriz identidade em vez de uma matriz geral positiva definida, as curvas de nível de densidade constante da Gaussiana multivariada deixariam de ser elipsoides orientados e se tornariam círculos (ou esferas) centrados em $\boldsymbol\mu$.

**Resposta:** Verdadeiro

**Justificativa:** Os autovalores de $\Sigma=I$ são todos iguais a 1, e todo vetor é autovetor — não há direção de orientação preferencial. Sem eixos de comprimentos distintos, o elipsoide degenera na figura mais simétrica possível: um círculo (2D) ou esfera (3D+) centrado em $\boldsymbol\mu$.

### A Gaussiana multivariada: parâmetros e geometria — item (b)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ No limite em que um dos autovalores de $\Sigma$ tende a zero (mantendo os demais fixos), as elipses de densidade constante da Gaussiana degeneram numa figura de dimensão menor (por exemplo, de uma elipse para um segmento de reta, em duas dimensões).

**Resposta:** Verdadeiro

**Justificativa:** O comprimento do eixo associado a um autovalor $\lambda_i$ escala com $\sqrt{\lambda_i}$. Se $\lambda_i\to 0$, esse eixo encolhe até desaparecer, e a elipse (que tinha dois eixos de comprimento finito) degenera numa figura de dimensão menor — em 2D, um segmento de reta ao longo do eixo remanescente.

### A Gaussiana multivariada: parâmetros e geometria — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Ao descrever a distribuição conjunta de altura e peso de uma população adulta com uma Gaussiana bivariada, os autovetores de $\hat\Sigma$ ainda dariam a orientação dos eixos de densidade constante e os autovalores ainda dariam o comprimento desses eixos, exatamente como no exemplo de temperatura/vibração desta aula.

**Resposta:** Verdadeiro

**Justificativa:** A relação entre autovetores/autovalores de $\Sigma$ e a geometria das elipses de densidade constante é uma propriedade matemática da Gaussiana multivariada em si, não uma peculiaridade do exemplo de sensores. Vale para qualquer par de variáveis correlacionadas, incluindo altura/peso.

### A Gaussiana multivariada: parâmetros e geometria — item (d)

**Heurística:** Falsa dicotomia/falsa equivalência

**Afirmação:** ✗ Como $\Sigma$ precisa ser simétrica e positiva definida, qualquer matriz simétrica com todas as entradas positivas automaticamente satisfaz essa exigência e pode servir como matriz de covariância válida.

**Resposta:** Falso

**Justificativa:** "Todas as entradas positivas" e "positiva definida" são propriedades diferentes. Positiva definida significa que todos os autovalores são positivos (equivalentemente, $\mathbf{v}^T\Sigma\mathbf{v}>0$ para todo $\mathbf{v}\ne\mathbf{0}$) — uma matriz simétrica pode ter todas as entradas positivas e ainda assim ter autovalores negativos, falhando a exigência. Um contraexemplo numérico simples: $\begin{bmatrix}1&2\\2&1\end{bmatrix}$ tem entradas todas positivas, mas autovalores $3$ e $-1$ — não é positiva definida.

### Por que a Gaussiana (entropia máxima e Teorema Central do Limite) — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se abandonássemos a suposição de que os dados vêm de uma soma de muitos efeitos pequenos e independentes (a justificativa do Teorema Central do Limite), a razão de "máxima entropia dada média e covariância fixas" ainda seria, por si só, uma justificativa independente e válida para escolher a Gaussiana.

**Resposta:** Verdadeiro

**Justificativa:** A aula apresenta as duas razões explicitamente como independentes ("duas razões clássicas") — a propriedade de máxima entropia é uma afirmação puramente sobre a família Gaussiana dada uma restrição de momentos, e não depende, para ser verdadeira, de nenhuma suposição sobre como os dados foram gerados (soma de efeitos pequenos). Remover a justificativa do TCL não invalida a justificativa de entropia máxima.

### Por que a Gaussiana (entropia máxima e Teorema Central do Limite) — item (b)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ No limite em que se conhece muito mais sobre a distribuição dos dados do que apenas a média e a covariância (por exemplo, sabe-se de antemão que a distribuição tem duas modas distintas), o argumento de máxima entropia deixa de recomendar a Gaussiana como a escolha menos comprometida.

**Resposta:** Verdadeiro

**Justificativa:** O argumento de máxima entropia é condicional às restrições impostas: "dada média e covariância fixas". Se soubermos mais sobre a distribuição (por exemplo, que ela é bimodal), essa informação extra é uma restrição adicional que a Gaussiana não respeita — a distribuição de entropia máxima *sujeita a essa restrição adicional* não seria mais a Gaussiana. A "escolha menos comprometida" depende do que já se sabe.

### Por que a Gaussiana (entropia máxima e Teorema Central do Limite) — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um erro de medição resultante da soma de muitos ruídos pequenos e independentes (erro de instrumento, flutuação térmica, arredondamento etc.) é um caso em que a justificativa do Teorema Central do Limite para usar uma Gaussiana se aplica, mesmo fora do contexto de sensores de uma máquina.

**Resposta:** Verdadeiro

**Justificativa:** A justificativa do TCL citada na aula é genérica: "a soma de muitas variáveis aleatórias tende a uma Gaussiana... plausível como modelo de ruído agregado ou de medições que resultam de muitos efeitos pequenos somados". Erro de medição composto por muitas fontes pequenas e independentes é exatamente esse cenário, em qualquer domínio.

### Por que a Gaussiana (entropia máxima e Teorema Central do Limite) — item (d)

**Heurística:** Falsa dicotomia/falsa equivalência

**Afirmação:** ✗ Como a Gaussiana é a distribuição de entropia máxima dada média e covariância fixas, isso implica que ela é sempre a distribuição mais provável de ter gerado qualquer conjunto de dados observado.

**Resposta:** Falso

**Justificativa:** "Máxima entropia dada média e covariância" é uma afirmação sobre qual distribuição é a menos comprometida quando só se conhecem esses dois momentos — não é uma afirmação sobre qual distribuição é mais provável de ter gerado dados reais específicos. Dados genuinamente multimodais, por exemplo (tema do Bloco 7), podem ter sido gerados por uma distribuição muito diferente da Gaussiana, mesmo tendo média e covariância bem definidas.

### Ajuste por máxima verossimilhança — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se, em vez de $\hat\Sigma_{\text{ML}} = \frac1N\sum_n(\ldots)$, dividíssemos por $N-1$ desde o início, o estimador resultante deixaria de ser viesado.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente a correção descrita na aula: $\mathbb{E}[\hat\Sigma_{\text{ML}}]=\frac{N-1}{N}\Sigma$, então dividir por $N-1$ em vez de $N$ produz $\tilde\Sigma$ com $\mathbb{E}[\tilde\Sigma]=\Sigma$ — não viesado. É literalmente o `np.cov` padrão do NumPy, citado na aula.

### Ajuste por máxima verossimilhança — item (b)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ No limite em que $N\to\infty$, a diferença relativa entre $\hat\Sigma_{\text{ML}}$ (dividido por $N$) e $\tilde\Sigma$ (dividido por $N-1$) tende a zero.

**Resposta:** Verdadeiro

**Justificativa:** A razão entre os dois estimadores é $N/(N-1)$ (ou sua potência $d$-ésima para o determinante, como a própria figura da aula mostra), e $N/(N-1)\to 1$ conforme $N\to\infty$. O viés relativo desaparece assintoticamente, mesmo que o viés continue existindo tecnicamente para todo $N$ finito.

### Ajuste por máxima verossimilhança — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um analista que ajusta $\hat{\boldsymbol\mu}$ e $\hat\Sigma$ a partir de uma amostra de retornos financeiros diários, em vez de leituras de sensores, obteria o mesmo tipo de viés sistemático em $\hat\Sigma_{\text{ML}}$ descrito nesta aula, pela mesma razão matemática.

**Resposta:** Verdadeiro

**Justificativa:** O viés de $\hat\Sigma_{\text{ML}}$ é uma propriedade da fórmula do estimador de máxima verossimilhança em si (dividir por $N$ em vez de $N-1$), não uma peculiaridade dos dados de sensores. Qualquer conjunto de dados ajustado com essa mesma fórmula sofre do mesmo viés, pela mesma derivação matemática.

### Ajuste por máxima verossimilhança — item (d)

**Heurística:** Falsa dicotomia/falsa equivalência

**Afirmação:** ✗ Como $\hat\Sigma_{\text{ML}}$ subestima a covariância verdadeira, isso significa que $\hat{\boldsymbol\mu}$ (a média amostral) também é, necessariamente, um estimador viesado da média verdadeira.

**Resposta:** Falso

**Justificativa:** O viés de $\hat\Sigma_{\text{ML}}$ e a propriedade de $\hat{\boldsymbol\mu}$ são resultados matemáticos distintos e independentes. A média amostral $\hat{\boldsymbol\mu}=\frac1N\sum_n\mathbf{x}_n$ é um estimador não viesado da média verdadeira ($\mathbb{E}[\hat{\boldsymbol\mu}]=\boldsymbol\mu$) — o viés de $\hat\Sigma_{\text{ML}}$ vem especificamente de usar a própria $\hat{\boldsymbol\mu}$ estimada (em vez da média verdadeira desconhecida) dentro da fórmula da covariância, um efeito que não se propaga para o estimador da média.

### A armadilha $N\le d$ — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se, em vez de $N\le d$, a condição fosse $N>d$ mas ainda assim $N$ próximo de $d$ (por exemplo, $N=d+1$), $\hat\Sigma_{\text{ML}}$ seria tecnicamente invertível, mas isso não impediria a estimativa de covariância de ser pouco confiável.

**Resposta:** Verdadeiro

**Justificativa:** Invertibilidade é uma condição de posto (precisa de posto $d$, alcançável tecnicamente com $N=d+1$ pontos em posição genérica), mas não é uma garantia de qualidade estatística. Com poucos pontos além do mínimo necessário, a estimativa de $\Sigma$ tem alta variância — a aula já anuncia isso como "a maldição da dimensionalidade que abre a Aula 2", que trata exatamente da degradação que continua acontecendo mesmo quando $N>d$ vale tecnicamente.

### A armadilha $N\le d$ — item (b)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ No caso-limite em que $d=1$ (um único sensor, não dois), a exigência $N>d$ se reduz a $N>1$ — bastam pelo menos 2 observações para $\hat\Sigma_{\text{ML}}$ ser, em princípio, calculável e não trivialmente nula.

**Resposta:** Verdadeiro

**Justificativa:** Com $d=1$, $\Sigma$ é escalar (a variância de uma única variável). Com um único ponto ($N=1$), a variância amostral é sempre zero (não há dispersão em torno de uma média calculada de um único valor) — degenerada, embora "invertível" no sentido trivial de ser um número positivo seria falso aqui (seria zero). Com $N\ge 2$ pontos distintos, a variância amostral é, genericamente, positiva e bem definida. Isso é consistente com a regra geral $N>d$.

### A armadilha $N\le d$ — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um cientista de dados que tenta ajustar uma Gaussiana multivariada a um conjunto de apenas 5 amostras de pacientes, cada uma com 20 exames diferentes ($d=20$), enfrentaria exatamente o mesmo problema de posto insuficiente em $\hat\Sigma_{\text{ML}}$ descrito nesta aula para os sensores da máquina.

**Resposta:** Verdadeiro

**Justificativa:** $N=5 \le d=20$ é exatamente a condição de falha descrita na aula: o posto de $\hat\Sigma_{\text{ML}}$ é, no máximo, $N-1=4$, insuficiente para o posto $d=20$ necessário para invertibilidade. O problema é estrutural (uma questão de contagem de graus de liberdade), não específico do domínio de sensores de máquina.

### A armadilha $N\le d$ — item (d)

**Heurística:** Falsa dicotomia/falsa equivalência

**Afirmação:** ✗ Como o problema de $N\le d$ é sobre a matriz $\hat\Sigma$ não ser invertível, isso significa que $\hat{\boldsymbol\mu}$ também deixa de ser calculável nesse regime.

**Resposta:** Falso

**Justificativa:** $\hat{\boldsymbol\mu}=\frac1N\sum_n\mathbf{x}_n$ é uma simples média aritmética — sempre calculável para qualquer $N\ge 1$ e qualquer $d$, sem exigir nenhuma condição de posto ou invertibilidade. O problema de $N\le d$ afeta especificamente $\hat\Sigma$ (por envolver uma matriz que precisa ser invertida para calcular Mahalanobis), não a média.

### A distância de Mahalanobis — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se $\Sigma$ fosse a matriz identidade, a distância de Mahalanobis calculada com essa matriz coincidiria exatamente com a distância Euclidiana usual.

**Resposta:** Verdadeiro

**Justificativa:** Com $\Sigma=I$, $\Sigma^{-1}=I$ também, e $D_M(\mathbf{x})^2=(\mathbf{x}-\boldsymbol\mu)^TI(\mathbf{x}-\boldsymbol\mu)=(\mathbf{x}-\boldsymbol\mu)^T(\mathbf{x}-\boldsymbol\mu)$, que é exatamente o quadrado da distância Euclidiana. É a afirmação citada literalmente do PRML na aula.

### A distância de Mahalanobis — item (b)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ No caso-limite em que a variância ao longo de uma direção específica tende a zero (mantendo as demais fixas), um deslocamento nessa direção, mesmo minúsculo em unidades brutas, faz a distância de Mahalanobis tender a infinito.

**Resposta:** Verdadeiro

**Justificativa:** O autovalor de $\Sigma^{-1}$ associado a essa direção é o inverso do autovalor de $\Sigma$ nessa mesma direção — se a variância (autovalor de $\Sigma$) tende a zero, o autovalor correspondente de $\Sigma^{-1}$ tende a infinito. Qualquer componente não nula de deslocamento nessa direção, multiplicada por um fator que tende a infinito, faz $D_M^2$ divergir. É a formalização extrema de "$\Sigma^{-1}$ estica nas direções de baixa variância".

### A distância de Mahalanobis — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Num contexto de avaliação de crédito com duas variáveis fortemente correlacionadas (renda e limite do cartão), um cliente com valores atípicos mas que respeitam a correlação usual entre as duas variáveis teria uma distância de Mahalanobis menor do que um cliente com valores dentro da faixa normal de cada variável isoladamente, mas que quebra essa correlação — pela mesma lógica dos pontos B e C desta aula.

**Resposta:** Verdadeiro

**Justificativa:** É a mesma estrutura geométrica dos pontos B e C generalizada para outro domínio: deslocar-se ao longo da direção de correlação "custa pouco" em Mahalanobis (mesmo parecendo atípico em unidades brutas), enquanto quebrar a correlação "custa muito" (mesmo parecendo normal em cada variável isolada). A lógica não depende de o domínio ser sensores de máquina.

### A distância de Mahalanobis — item (d)

**Heurística:** Falsa dicotomia/falsa equivalência

**Afirmação:** ✗ Como a distância de Mahalanobis "estica" o espaço nas direções de baixa variância, isso significa que ela sempre atribui distâncias maiores a pontos mais distantes em unidades Euclidianas brutas.

**Resposta:** Falso

**Justificativa:** É exatamente o oposto do que os pontos B e C demonstram: B está mais longe do centro em unidades Euclidianas brutas, mas tem Mahalanobis *menor* que C (que está mais perto em unidades brutas). "Esticar nas direções de baixa variância e comprimir nas de alta variância" significa que a ordem de distâncias pode se inverter completamente dependendo da direção do deslocamento — não que Mahalanobis preserve a ordem Euclidiana.

### Os pontos B e C: geometria da crista — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se o ponto C, em vez de se deslocar ao longo do eixo de baixa variância, tivesse se deslocado a mesma distância Euclidiana ao longo do eixo de alta variância (a crista), sua distância de Mahalanobis resultante seria menor do que a calculada originalmente para C.

**Resposta:** Verdadeiro

**Justificativa:** $\Sigma^{-1}$ comprime na direção de alta variância (mesma distância Euclidiana ao longo da crista "custa pouco" em Mahalanobis) e estica na direção de baixa variância (mesma distância Euclidiana fora da crista "custa muito"). Deslocar C na direção de alta variância, em vez de baixa variância, necessariamente reduziria sua distância de Mahalanobis para a mesma distância Euclidiana.

### Os pontos B e C: geometria da crista — item (b)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Se as variâncias de temperatura e vibração fossem exatamente iguais e a correlação entre elas fosse zero, não haveria mais diferença entre "longe na crista" e "fora da crista" — qualquer direção de deslocamento produziria a mesma distância de Mahalanobis para um mesmo deslocamento Euclidiano.

**Resposta:** Verdadeiro

**Justificativa:** Variâncias iguais e correlação zero significam $\Sigma=\sigma^2 I$ (matriz escalar) — todos os autovalores são iguais, não há mais "direção de alta variância" nem "direção de baixa variância" privilegiada. Nesse caso $D_M^2=\frac{1}{\sigma^2}\|\mathbf{x}-\boldsymbol\mu\|^2$, um múltiplo escalar da distância Euclidiana ao quadrado, igual em todas as direções — a distinção entre "crista" e "fora da crista" deixa de existir porque não há mais crista.

### Os pontos B e C: geometria da crista — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Num modelo com três variáveis fortemente correlacionadas entre si (por exemplo, três medidas relacionadas do tamanho de um objeto), a mesma lógica dos pontos B e C se generalizaria: um ponto que respeita a relação de correlação entre as três teria Mahalanobis pequena mesmo se distante em unidades brutas, e um ponto que quebra essa relação teria Mahalanobis grande mesmo perto em unidades brutas.

**Resposta:** Verdadeiro

**Justificativa:** A mecânica de "esticar/comprimir" de $\Sigma^{-1}$ generaliza para qualquer dimensão $d$: os autovetores de $\Sigma$ definem as direções de alta e baixa variância em $\mathbb{R}^d$, e o mesmo argumento (deslocar ao longo de uma direção de alta variância "custa pouco"; deslocar-se perpendicularmente a ela, "quebrando" a estrutura de correlação, "custa muito") vale igualmente com três ou mais variáveis correlacionadas.

### Os pontos B e C: geometria da crista — item (d)

**Heurística:** Falsa dicotomia/falsa equivalência

**Afirmação:** ✗ Como o ponto B está mais longe do centro em distância Euclidiana do que o ponto C, isso implica necessariamente que B deveria ser considerado mais anômalo do que C por qualquer critério razoável de anomalia.

**Resposta:** Falso

**Justificativa:** É exatamente o ponto central do exemplo B/C: por Mahalanobis (e pelo $p$-valor derivado dela no Bloco 5), B é *menos* anômalo que C, mesmo sendo mais distante em unidades Euclidianas brutas — porque B respeita a estrutura de correlação dos dados, e C a quebra. "Distância Euclidiana maior" não é um critério razoável de anomalia quando há correlação entre as variáveis; é exatamente essa a lição do bloco.

### Do limiar fixo ao $p$-valor — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se, em vez de comparar $D_M(\mathbf{x})^2$ a um limiar fixo, sempre reportássemos o $p$-valor $p(\mathbf{x})=1-F_{\chi^2_d}(D_M(\mathbf{x})^2)$, ainda seria possível recuperar exatamente a mesma decisão binária "típico/anômalo" do limiar fixo, escolhendo o $\alpha$ apropriado.

**Resposta:** Verdadeiro

**Justificativa:** A aula afirma diretamente: "o limiar fixo é o caso particular $p(\mathbf{x})<\alpha$". Qualquer decisão binária feita com um limiar fixo em $D_M^2$ corresponde a um limiar equivalente em $p(\mathbf{x})$ (já que $F_{\chi^2_d}$ é uma função monótona) — basta escolher $\alpha$ de forma consistente com o limiar original.

### Do limiar fixo ao $p$-valor — item (b)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ No caso-limite em que $D_M(\mathbf{x})^2\to 0$ (o ponto exatamente na média ajustada $\hat{\boldsymbol\mu}$), o $p$-valor $p(\mathbf{x})$ tende a $1$.

**Resposta:** Verdadeiro

**Justificativa:** $p(\mathbf{x})=P(D_M(\mathbf{X}')^2\ge D_M(\mathbf{x})^2)$. Como $D_M(\mathbf{X}')^2\ge 0$ sempre (é uma soma de quadrados), a probabilidade de ser $\ge 0$ é trivialmente $1$. Um ponto exatamente na média é, por definição, o menos surpreendente possível sob o modelo ajustado — daí o $p$-valor máximo.

### Do limiar fixo ao $p$-valor — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Se, em outro contexto (não sensores de máquina), $D_M(\mathbf{x})^2$ ainda seguisse $\chi^2_d$ sob o modelo ajustado, a mesma fórmula $p(\mathbf{x})=1-F_{\chi^2_d}(D_M(\mathbf{x})^2)$ poderia ser usada para converter a distância num $p$-valor, independentemente do domínio da aplicação.

**Resposta:** Verdadeiro

**Justificativa:** A derivação de $D_M(\mathbf{x})^2\sim\chi^2_d$ (verificada na aula via $\mathbf{Y}=\Sigma^{-1/2}(\mathbf{X}-\boldsymbol\mu)\sim\mathcal{N}(0,I_d)$) depende só da suposição de que $\mathbf{x}$ vem de uma Gaussiana multivariada — um resultado de estatística geral, não específico de sensores de máquina. A fórmula de conversão se aplica sempre que essa suposição for razoável.

### Do limiar fixo ao $p$-valor — item (d)

**Heurística:** Falsa dicotomia/falsa equivalência

**Afirmação:** ✗ Como o $p$-valor ordena os pontos por "quão surpreendentes" eles são, isso significa que ele não pode mais ser usado para tomar uma decisão binária de "típico vs. anômalo" — a única forma de decidir seria olhando o ranking completo dos pontos.

**Resposta:** Falso

**Justificativa:** As duas funções não são mutuamente exclusivas. O $p$-valor generaliza o limiar fixo (que é um caso particular dele, $p(\mathbf{x})<\alpha$), mas continua permitindo decisões binárias exatamente da mesma forma — só que com a opção adicional de, se desejado, também usar o ranking completo. Ganhar uma capacidade extra (ordenar por surpresa) não implica perder a capacidade anterior (decidir com um limiar).

### A armadilha de interpretação do $p$-valor — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se o modelo ajustado ($\hat{\boldsymbol\mu}$, $\hat\Sigma$) estivesse severamente errado (por exemplo, ajustado a partir de dados de um regime de operação diferente do real), o $p$-valor calculado ainda seria uma medida confiável da probabilidade de $\mathbf{x}$ pertencer à verdadeira distribuição dos dados.

**Resposta:** Falso

**Justificativa:** É exatamente a armadilha de interpretação nomeada na aula: o $p$-valor é "uma afirmação sobre o modelo, condicional a ele estar certo — não é uma afirmação sobre a origem de $\mathbf{x}$." A própria aula afirma textualmente: "se o modelo estiver errado, o $p$-valor também estará."

### A armadilha de interpretação do $p$-valor — item (b)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ No caso extremo em que o modelo ajustado é uma aproximação perfeita da distribuição verdadeira dos dados (nenhum erro de especificação), a distinção entre "probabilidade de um ponto do modelo ajustado ser tão extremo quanto x" e "probabilidade de x vir da distribuição verdadeira" desaparece — as duas interpretações coincidem.

**Resposta:** Verdadeiro

**Justificativa:** A armadilha de interpretação existe precisamente por causa do risco de erro de especificação (modelo ajustado ≠ distribuição verdadeira). Se esse erro for zero — o modelo ajustado é idêntico à distribuição verdadeira —, as duas afirmações ("sob o modelo ajustado" e "sob a distribuição verdadeira") se referem exatamente à mesma distribuição, e a distinção colapsa por não haver mais nada para distinguir.

### A armadilha de interpretação do $p$-valor — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um sistema de triagem de spam que calcula um "$p$-valor" de quão atípico um e-mail é, comparado a um modelo ajustado de e-mails legítimos, sofreria exatamente da mesma armadilha de interpretação descrita nesta aula, caso o modelo ajustado não represente bem os e-mails legítimos reais.

**Resposta:** Verdadeiro

**Justificativa:** A armadilha de interpretação é uma propriedade lógica da definição de $p$-valor (uma afirmação condicional ao modelo estar certo), independente do domínio de aplicação. Qualquer sistema que use essa mesma lógica — sensores de máquina, e-mails, ou qualquer outro — herda a mesma vulnerabilidade se o modelo ajustado for uma má aproximação da realidade.

### A armadilha de interpretação do $p$-valor — item (d)

**Heurística:** Falsa dicotomia/falsa equivalência

**Afirmação:** ✗ Como um $p$-valor pequeno indica que um ponto é estatisticamente surpreendente sob o modelo ajustado, isso significa, sem mais suposições, que esse ponto certamente não pertence à população de interesse.

**Resposta:** Falso

**Justificativa:** É exatamente a confusão que a aula avisa explicitamente para evitar: "$p(\mathbf{x})$ pequeno não significa 'probabilidade de $\mathbf{x}$ pertencer à distribuição verdadeira'". "Surpreendente sob o modelo ajustado" é uma afirmação sobre o modelo; "não pertence à população verdadeira" é uma afirmação sobre a realidade — as duas só coincidem se o modelo estiver certo, uma suposição adicional que o item tenta remover ("sem mais suposições").

### Conjunta vs. por dimensão — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se as duas variáveis (temperatura e vibração) fossem, de fato, estatisticamente independentes uma da outra, o teste "por dimensão" (que assume independência) produziria, em geral, resultados muito parecidos com o teste "conjunto" (Mahalanobis).

**Resposta:** Verdadeiro

**Justificativa:** O erro do teste por dimensão vem especificamente de ignorar correlação que de fato existe. Se a suposição de independência que ele faz for verdadeira (não há correlação real para ignorar), não há informação sendo descartada, e os dois testes devem convergir para resultados semelhantes.

### Conjunta vs. por dimensão — item (b)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ No caso-limite em que a correlação entre as duas variáveis é exatamente $1$ (correlação perfeita), o teste "por dimensão" (que ignora a correlação) cometeria o maior erro possível de sobre ou subestimação do $p$-valor, comparado ao teste conjunto.

**Resposta:** Verdadeiro

**Justificativa:** Correlação perfeita é o caso em que a informação ignorada pelo teste por dimensão (a relação entre as variáveis) é máxima — as duas variáveis carregam, nesse limite, a mesma informação de uma única direção, e tratá-las como independentes descarta o máximo possível de estrutura real. É o extremo oposto do item (a) (correlação zero, nenhum erro).

### Conjunta vs. por dimensão — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ No Naive Bayes de Aprendizado Supervisionado, a mesma suposição de independência entre atributos é feita para simplificar o cálculo, ao custo de "limitar a capacidade do modelo de capturar correlações interessantes nos dados" — exatamente a mesma tensão custo/benefício discutida nesta aula para o teste por dimensão.

**Resposta:** Verdadeiro

**Justificativa:** É a comparação explícita feita na própria aula: "a mesma lição do preço da suposição de independência do Naive Bayes, agora em teste de hipótese em vez de classificação". A citação do PRML sobre $\Sigma$ diagonal usada na aula é literalmente sobre essa mesma tensão (mais rápido de inverter, ao custo de limitar a captura de correlações).

### Conjunta vs. por dimensão — item (d)

**Heurística:** Falsa dicotomia/falsa equivalência

**Afirmação:** ✗ Como o teste conjunto (Mahalanobis) usa mais parâmetros ($d(d+1)/2$ em vez de $d$), ele é sempre estritamente mais preciso do que o teste por dimensão, para qualquer conjunto de dados e qualquer tamanho de amostra $N$.

**Resposta:** Falso

**Justificativa:** Mais parâmetros não é sinônimo de mais precisão — é exatamente a tensão da armadilha $N\le d$ (Bloco 4): estimar $d(d+1)/2$ parâmetros exige mais dados do que estimar $d$ parâmetros, e com $N$ pequeno relativo a $d$, a estimativa de $\hat\Sigma$ completa pode ser instável ou até impossível de inverter, enquanto a versão diagonal (por dimensão) continua bem definida com muito menos dados. "Mais expressivo" tem um custo de dados que pode superar seu benefício quando $N$ é limitado.

### Multimodalidade — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se a população real de fato tivesse duas subpopulações bem distintas (dois regimes de operação), mas ajustássemos, ainda assim, uma única Gaussiana, os parâmetros $\hat{\boldsymbol\mu}$ e $\hat\Sigma$ resultantes seriam matematicamente inválidos (não calculáveis).

**Resposta:** Falso

**Justificativa:** A aula é explícita: "o ajuste 'funciona' no sentido de que a matemática produz $\hat{\boldsymbol\mu}$ e $\hat\Sigma$ válidos". As fórmulas de máxima verossimilhança são simples médias/produtos externos — sempre calculáveis para qualquer conjunto de dados, multimodal ou não. O problema não é a matemática falhar, é a *descrição resultante* ser enganosa mesmo com números perfeitamente válidos.

### Multimodalidade — item (b)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ No caso-limite em que as duas subpopulações estão extremamente distantes uma da outra (bem separadas), a Gaussiana única ajustada teria uma variância muito inflada, mas a média ajustada $\hat{\boldsymbol\mu}$ ainda cairia, aproximadamente, entre as duas subpopulações — numa região onde poucos dados reais efetivamente existem.

**Resposta:** Verdadeiro

**Justificativa:** A média amostral é uma média ponderada de todos os pontos; com duas subpopulações bem separadas e de tamanhos comparáveis, essa média cai entre as duas nuvens, numa região vazia de dados reais — o comportamento clássico de "média cega entre os dois modos" citado na aula. A variância precisa ser grande o suficiente para cobrir a dispersão total (incluindo a distância entre os centros das duas subpopulações), ficando inflada.

### Multimodalidade — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um modelo de detecção de anomalias em transações financeiras que mistura, sem saber, transações de dois perfis de cliente muito diferentes (por exemplo, pessoa física e pessoa jurídica) sofreria do mesmo problema de multimodalidade descrito nesta aula para os regimes de operação da máquina.

**Resposta:** Verdadeiro

**Justificativa:** O problema de multimodalidade é sobre a estrutura dos dados (duas subpopulações genuinamente distintas) em relação à suposição do modelo (uma única forma Gaussiana), não sobre o domínio específico dos sensores. Misturar perfis de cliente muito diferentes é a mesma estrutura de dados problemática, em outro domínio.

### Multimodalidade — item (d)

**Heurística:** Falsa dicotomia/falsa equivalência

**Afirmação:** ✗ Como o ajuste Gaussiano "funciona" no sentido de produzir $\hat{\boldsymbol\mu}$ e $\hat\Sigma$ válidos mesmo com dados multimodais, isso significa que a descrição resultante da população é necessariamente confiável para decidir o que é típico ou anômalo.

**Resposta:** Falso

**Justificativa:** É exatamente o contraste que a aula estabelece: "o ajuste 'funciona'... e mesmo assim a descrição resultante mente sobre a forma real dos dados". Um cálculo ser matematicamente bem-sucedido (produzir números válidos) não garante que o resultado seja uma descrição útil ou confiável da realidade — os dois são propriedades independentes.

### Outliers no ajuste e ponte para a Aula 2 — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se os outliers estivessem presentes apenas no conjunto de teste (pontos novos avaliados), mas não no conjunto usado para ajustar $\hat{\boldsymbol\mu}$ e $\hat\Sigma$, o problema de $\hat\Sigma$ inflada descrito nesta aula não ocorreria.

**Resposta:** Verdadeiro

**Justificativa:** O mecanismo do problema é específico: outliers *no conjunto de ajuste* deslocam a média e inflam a covariância estimadas, porque essas estatísticas são calculadas a partir desses mesmos pontos. Um outlier avaliado como ponto de teste, depois do ajuste já ter sido feito com dados limpos, não influencia $\hat{\boldsymbol\mu}$ e $\hat\Sigma$ — ele só seria (corretamente) classificado como atípico pelo modelo já ajustado.

### Outliers no ajuste e ponte para a Aula 2 — item (b)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ No caso-limite em que só um único ponto do conjunto de ajuste é um outlier extremo, entre milhares de pontos típicos, o efeito desse único ponto sobre $\hat{\boldsymbol\mu}$ e $\hat\Sigma$ tenderia a ser desprezível.

**Resposta:** Verdadeiro

**Justificativa:** $\hat{\boldsymbol\mu}$ e $\hat\Sigma$ são médias sobre $N$ pontos — a contribuição de um único ponto para uma média de $N$ termos escala como $1/N$. Com $N$ da ordem de milhares, o efeito de um único outlier, mesmo extremo, se dilui e tende a ficar pequeno (embora não seja exatamente zero) — ao contrário do caso de poucos outliers numa amostra pequena, onde o efeito pode ser dominante.

### Outliers no ajuste e ponte para a Aula 2 — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ A Aula 2 relaxa a suposição de forma única (Gaussiana) usando $k$-NN e KDE, mas essa mudança, por si só, não resolve o problema de outliers no ajuste — a mesma vulnerabilidade a outliers poderia, em princípio, aparecer também em estimadores não-paramétricos de densidade, não sendo uma exclusividade do modelo Gaussiano.

**Resposta:** Verdadeiro

**Justificativa:** A aula qualifica o problema de outliers como "um problema de robustez... fora do escopo desta aula", não como algo intrinsecamente ligado à forma paramétrica Gaussiana. Abandonar a suposição de forma (o que a Aula 2 faz) ataca um problema diferente (a rigidez da forma funcional); a robustez a outliers é uma questão ortogonal, que também pode afetar estimadores não-paramétricos que dependem da posição bruta de todos os pontos.

### Outliers no ajuste e ponte para a Aula 2 — item (d)

**Heurística:** Falsa dicotomia/falsa equivalência

**Afirmação:** ✗ Como a Aula 2 vai abandonar a suposição de forma paramétrica (Gaussiana), isso significa que ela também vai automaticamente resolver o problema da maldição da dimensionalidade que a exigência $N>d$ desta aula já anunciou.

**Resposta:** Falso

**Justificativa:** A própria aula avisa o oposto ao fazer a ponte: "o preço dessa liberdade — a maldição da dimensionalidade... — é o assunto de lá." Abandonar a suposição de forma paramétrica troca um problema (a forma pode estar errada) por outro (a maldição da dimensionalidade aparece de um jeito diferente, não paramétrico) — não elimina a dificuldade, só muda sua natureza.
