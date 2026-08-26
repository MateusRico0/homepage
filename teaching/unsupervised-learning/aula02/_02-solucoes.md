# Soluções — Questões de Verdadeiro/Falso (Aula 2)

> Arquivo de apoio, não publicado (prefixo `_`). Contém a resposta e a
> justificativa de cada item das 12 questões de V/F do `index.qmd`. O
> `index.qmd` publicado continua sem solução — este arquivo existe só
> para conferência do professor/monitor, seguindo a metodologia de
> criação de questões definida em `../../CLAUDE.md`.

## Concentração de volume na hiperesfera

**a.** [ ] Se $\epsilon=0{,}5$ (a casca cobre metade do raio), a fração do volume de uma esfera de raio 1 contida nessa casca, em $D=1$ dimensão, é exatamente $0{,}5$.

**Heurística:** Caso limite
**Resposta:** Verdadeiro
**Justificativa:** Com $D=1$, a fórmula $1-(1-\epsilon)^D$ se reduz a $1-(1-\epsilon)=\epsilon$; para $\epsilon=0{,}5$, dá exatamente $0{,}5$ — o caso trivial em que "esfera" é só um segmento e a fração de volume é literalmente a fração linear.

**b.** [ ] Para qualquer $\epsilon\in(0,1)$ fixo, a fração do volume contida na casca de espessura $\epsilon$ é uma função estritamente crescente de $D$.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Como $0<1-\epsilon<1$, a potência $(1-\epsilon)^D$ é estritamente decrescente em $D$; logo $1-(1-\epsilon)^D$ é estritamente crescente em $D$. É exatamente o mecanismo que faz a fração tender a 1 conforme $D\to\infty$.

**c.** [ ] Um argumento análogo ao da hiperesfera se aplicaria a um hipercubo de lado 1 em $D$ dimensões: a fração do volume contida numa casca de espessura relativa $\epsilon$ próxima da superfície do cubo também tenderia a 1 conforme $D\to\infty$.

**Heurística:** Transferência de domínio
**Resposta:** Verdadeiro
**Justificativa:** O "núcleo" do hipercubo, encolhido por $\epsilon$ de cada lado, tem volume $(1-2\epsilon)^D$ (para $\epsilon<0{,}5$) — uma potência de um número menor que 1, que tende a zero conforme $D$ cresce, exatamente como $(1-\epsilon)^D$ na esfera. A fração fora do núcleo (perto da superfície) tende a 1 pela mesma razão estrutural: volume escala como (comprimento)$^D$.

**d.** [ ] Se a massa de probabilidade de uma Gaussiana multivariada se concentra numa casca fina afastada da média em alta dimensão, isso implica que a moda da distribuição (o ponto de densidade máxima) não é mais o ponto de $\mathbf{x}$ onde a maior parte da massa de probabilidade está localizada.

**Heurística:** Transferência de domínio
**Resposta:** Verdadeiro
**Justificativa:** A densidade pontual $f(\mathbf{x})$ ainda é máxima na média (é a moda, no sentido usual). Mas a massa de probabilidade numa casca radial de raio $r$ é proporcional a $r^{D-1}f(r)$ (o fator $r^{D-1}$ vem do volume da casca em coordenadas polares), que é maximizada num raio $r^*>0$ que cresce com $D$ — não em $r=0$. Densidade máxima (moda) e concentração de massa (onde "a maior parte da probabilidade está") deixam de coincidir em alta dimensão — exatamente o que a Figura 1.23 do PRML ilustra.

---

## As fórmulas do ESL (comprimento de aresta e distância mediana)

**a.** [ ] Segundo $e_p(r)=r^{1/p}$, para capturar uma fração fixa $r<1$ dos dados, o comprimento de aresta necessário aumenta conforme $p$ aumenta.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Para $0<r<1$ fixo, $1/p\to 0$ conforme $p\to\infty$, e $r^{1/p}\to r^0=1$. Como $r<1$, elevar $r$ a uma potência cada vez menor o aproxima de 1 — o comprimento de aresta necessário cresce (a "vizinhança local" precisa cobrir cada vez mais da amplitude de cada eixo).

**b.** [ ] A fórmula $d(p,N)=(1-(1/2)^{1/N})^{1/p}$ prevê que, mantendo $p$ fixo e aumentando $N$ para infinito, a distância mediana ao vizinho mais próximo da origem tende a zero.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Conforme $N\to\infty$, $1/N\to 0$ e $(1/2)^{1/N}\to (1/2)^0=1$, então $1-(1/2)^{1/N}\to 0$. Elevado a qualquer potência positiva finita $1/p$, o resultado ainda tende a zero. Faz sentido: com infinitos pontos, o vizinho mais próximo da origem fica arbitrariamente perto dela.

**c.** [ ] Se, para $N=500$ e $p=10$, a distância mediana ao vizinho mais próximo da origem é $\approx 0{,}52$ (mais da metade do raio), então, necessariamente, mais da metade dos 500 pontos está a uma distância menor que $0{,}52$ da origem.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** $d(p,N)$ é a mediana da distribuição de "distância do **primeiro/mais próximo** vizinho até a origem", uma estatística sobre o **mínimo** das distâncias de todos os pontos — não a mediana das distâncias individuais dos 500 pontos até a origem. Essas são duas quantidades completamente diferentes: a primeira descreve o comportamento do ponto mais próximo; a segunda, a distribuição de todos os pontos. O aluno que confunde as duas comete exatamente o erro que a fonte adverte ser contraintuitivo.

**d.** [ ] O crescimento da densidade amostral necessária, $N^{1/p}$, e o crescimento do comprimento de aresta necessário, $r^{1/p}$, são dois sintomas independentes da maldição da dimensionalidade, sem relação matemática direta entre si.

**Heurística:** Falsa dicotomia
**Resposta:** Falso
**Justificativa:** Os dois vêm exatamente da mesma identidade — volume escala como (comprimento)$^D$ em $D$ dimensões. É essa mesma lei de escala que faz tanto o comprimento de aresta ($V\propto \text{comprimento}^p$) quanto a densidade amostral necessária ($N\propto \text{densidade}^p$, invertendo a mesma relação) dependerem de potências $1/p$. Não são sintomas independentes — são a mesma causa geométrica vista de dois ângulos.

---

## Concentração de medida e métricas de distância

**a.** [ ] Se o contraste relativo $(\text{dist}_{\max}-\text{dist}_{\min})/\text{dist}_{\min}$ tende a zero conforme $d$ cresce, isso implica que a distância absoluta entre pontos também tende a zero.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** Contraste relativo tendendo a zero significa que $\text{dist}_{\max}$ e $\text{dist}_{\min}$ ficam **próximos entre si** (na razão) — não que qualquer um dos dois tende a zero em valor absoluto. Na prática, ao aumentar $d$ com atributos padronizados, as distâncias absolutas tendem a **crescer** (mais termos ao quadrado somados), mesmo enquanto a diferença relativa entre a mais próxima e a mais distante desaparece.

**b.** [ ] Num dataset em que só um pequeno subconjunto dos atributos carrega informação relevante para a tarefa e o restante é ruído independente, aumentar $d$ usando apenas os atributos informativos NÃO deveria produzir a mesma queda no contraste relativo observada ao aumentar $d$ com atributos aleatórios (informativos + ruído).

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** A concentração de medida é impulsionada especificamente por dimensões de ruído independentes, que diluem o sinal sem acrescentar estrutura real. Aumentar $d$ só com atributos genuinamente informativos (correlacionados com a estrutura real dos dados) não tem esse efeito diluidor — o contraste relativo pode até se manter estável ou cair muito mais lentamente.

**c.** [ ] O fato de o contraste relativo cair de $\approx 220$ (d=2) para $\approx 10$ (d=30) no Breast Cancer Wisconsin depende da escolha específica desse dataset, e um dataset sintético com atributos i.i.d. uniformes mostraria, em geral, o oposto (contraste relativo crescente com $d$).

**Heurística:** Transferência de domínio
**Resposta:** Falso
**Justificativa:** A concentração de medida é um resultado geral para dados i.i.d. em alta dimensão (Beyer et al., 1999) — um dataset sintético com atributos i.i.d. mostraria a **mesma** tendência de queda do contraste relativo, tipicamente de forma ainda mais limpa (sem a estrutura de correlação real entre atributos clínicos que existe no Breast Cancer Wisconsin). O fenômeno não é uma peculiaridade deste dataset específico.

**d.** [ ] Padronizar os atributos (subtrair a média, dividir pelo desvio) antes de calcular distâncias é irrelevante para o fenômeno de concentração de medida — ele ocorreria de forma idêntica mesmo sem essa padronização.

**Heurística:** Contrafactual
**Resposta:** Falso
**Justificativa:** A tendência qualitativa (queda do contraste com $d$) persistiria, mas os valores numéricos específicos, não. Sem padronização, atributos de escala muito maior (ex.: `area_mean`, na casa das centenas) dominariam completamente o cálculo de distância Euclidiana, distorcendo o contraste relativo medido — não seria "idêntico", como o item afirma.

---

## O resultado geral $p(\mathbf{x})=K/(NV)$

**a.** [ ] A derivação de $p(\mathbf{x})=K/(NV)$ depende da suposição de que $p(\mathbf{x})$ é aproximadamente constante dentro da região $R$ — se essa suposição falhar (por exemplo, $R$ grande demais numa região de densidade muito variável), a estimativa fica sistematicamente distorcida mesmo com $N$ muito grande.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** A suposição $P\approx p(\mathbf{x})V$ (densidade aproximadamente constante em $R$) é uma das duas premissas contraditórias da derivação (PRML, p. 122). Se $R$ é grande numa região de densidade variável, o viés introduzido não desaparece com $N\to\infty$ — é um viés estrutural da escolha de $V$, não um problema de tamanho de amostra.

**b.** [ ] A aproximação $K\simeq NP$ é uma consequência de a distribuição binomial $\mathrm{Bin}(K\mid N,P)$ ficar mais concentrada em torno da sua média conforme $N$ cresce — não é uma igualdade exata para qualquer $N$ finito.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** PRML é explícito: "For large N, this distribution will be sharply peaked around the mean and so $K\simeq NP$" — é uma aproximação assintótica (a variância relativa $P(1-P)/N$ diminui com $N$), não uma identidade exata para $N$ pequeno.

**c.** [ ] Se $V\to 0$ mantendo $N$ fixo, a estimativa $K/(NV)$ tende, na prática, a ficar mais estável e menos ruidosa, porque $R$ fica mais fiel à suposição de densidade constante.

**Heurística:** Contrafactual
**Resposta:** Falso
**Justificativa:** É exatamente o oposto — conforme $V\to 0$ com $N$ fixo, o número esperado de pontos capturados, $K\approx NP\approx Np(\mathbf{x})V$, também tende a zero. Poucos pontos tornam a binomial cada vez menos concentrada em torno da média (maior variância relativa), aumentando o ruído da estimativa — mesmo que a suposição de densidade constante melhore. É a tensão que a própria fonte descreve como "duas suposições contraditórias".

**d.** [ ] As duas rotas — fixar $K$ e achar $V$, ou fixar $V$ e achar $K$ — produzem, em geral, estimativas numericamente idênticas ponto a ponto, para o mesmo dataset e os mesmos valores nominais de "quantos pontos" ou "que tamanho de região" foram usados.

**Heurística:** Falsa dicotomia
**Resposta:** Falso
**Justificativa:** As duas rotas compartilham a mesma identidade geral, mas são estimadores diferentes — o Bloco 6 mostrou exatamente isso: KDE ($h=1{,}0$) e $k$-NN ($K=20$) concordam no grosso da distribuição, mas divergem visivelmente nas caudas, porque um tem largura fixa e o outro adaptativa. "Vêm da mesma identidade" não significa "produzem os mesmos números".

---

## $k$-NN para densidade

**a.** [ ] A relação $p(\mathbf{x})\propto 1/d_K(\mathbf{x})^D$ implica que, para o mesmo valor de $d_K(\mathbf{x})$, a densidade estimada em $D=30$ dimensões é numericamente igual à densidade estimada em $D=2$ dimensões.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** A relação é de **proporcionalidade**, não igualdade — a constante de proporcionalidade envolve o volume de uma esfera unitária em $D$ dimensões ($K_D$ na notação de PRML), que depende fortemente de $D$. O mesmo $d_K(\mathbf{x})$ produz volumes $V\propto d_K^D$ muito diferentes para $D=2$ e $D=30$, e portanto densidades estimadas numericamente diferentes.

**b.** [ ] Se dois pontos $\mathbf{x}_1$ e $\mathbf{x}_2$ têm o mesmo valor de $d_K(\mathbf{x})$ para o mesmo $K$, o modelo de $k$-NN atribui a eles a mesma densidade estimada, independentemente de quaisquer outras diferenças entre suas vizinhanças.

**Heurística:** Caso limite
**Resposta:** Verdadeiro
**Justificativa:** Por construção, $p(\mathbf{x})=K/(NV)$ com $V$ determinado inteiramente por $d_K(\mathbf{x})$ (via $V\propto d_K(\mathbf{x})^D$) — o estimador não usa nenhuma outra informação sobre a disposição espacial dos $K$ vizinhos dentro da esfera. Dois pontos com o mesmo $d_K$ recebem, por definição, a mesma densidade estimada, mesmo que suas vizinhanças sejam, de outra forma, muito diferentes (isso também revela uma limitação: o método descarta informação sobre a distribuição interna dos vizinhos).

**c.** [ ] Aumentar $K$ de 5 para 50 num ponto na região mais densa dos dados produz uma variação relativa menor em $d_K(\mathbf{x})$ do que a mesma variação de $K$ produziria num ponto na cauda da distribuição.

**Heurística:** Transferência de domínio
**Resposta:** Verdadeiro
**Justificativa:** É a propriedade de suavização adaptativa verificada numericamente nesta aula: em $x_0=12$ (denso), $d_K$ passa de $\approx 0{,}04$ a $\approx 0{,}29$; em $x_0=25$ (cauda), de $\approx 1{,}49$ a $\approx 5{,}27$ — uma variação absoluta e relativa muito maior na região esparsa.

**d.** [ ] Como o $k$-NN não assume nenhuma forma funcional para $p(\mathbf{x})$, ele está imune a qualquer viés sistemático — ao contrário do ajuste Gaussiano da Aula 1, que pode enviesar a estimativa se a forma verdadeira não for Gaussiana.

**Heurística:** Falsa dicotomia
**Resposta:** Falso
**Justificativa:** Não assumir uma forma paramétrica elimina o viés de **forma** (a Gaussiana errada), mas não elimina outras fontes de viés — por exemplo, o próprio $K$ como parâmetro de suavização introduz viés (subestimar/sobrestimar densidade conforme $K$ é mal escolhido), e o método sofre viés perto das bordas do suporte dos dados. "Não-paramétrico" não é sinônimo de "sem viés".

---

## "Isto não é uma densidade de verdade"

**a.** [ ] O fato de a integral de $p(\mathbf{x})\propto 1/d_K(\mathbf{x})^D$ sobre todo o espaço divergir é uma consequência de como a cauda dessa função decai com a distância, não um erro de implementação específico de algum software.

**Heurística:** Transferência de domínio
**Resposta:** Verdadeiro
**Justificativa:** É um fato matemático sobre a forma funcional do estimador — a taxa na qual $d_K(\mathbf{x})$ cresce com a distância a pontos de treino não é rápida o suficiente para compensar o crescimento do "volume" do espaço, fazendo a integral divergir. É citado explicitamente por PRML como propriedade do método, não como um bug de qualquer implementação particular.

**b.** [ ] Ainda que o modelo de $k$-NN não seja uma densidade normalizada, ele pode ser usado de forma válida para ordenar pontos do menos denso ao mais denso.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** A comparação relativa (qual ponto tem $d_K$ menor, e portanto densidade estimada maior) não depende de a função integrar a 1 — só depende de a relação $p(\mathbf{x})\propto 1/d_K(\mathbf{x})^D$ preservar a ordem correta entre pontos, o que ela faz.

**c.** [ ] Se o objetivo fosse calcular a probabilidade exata de um novo ponto pertencer a uma região específica do espaço (uma integral de $p(\mathbf{x})$ sobre essa região), o modelo de $k$-NN, sem modificação, forneceria essa probabilidade corretamente.

**Heurística:** Contrafactual
**Resposta:** Falso
**Justificativa:** Como a função não integra a 1 sobre todo o espaço, qualquer integral sobre uma sub-região não corresponde a uma probabilidade válida (o "total" de referência está errado). É exatamente a limitação anunciada por PRML: útil para comparação relativa, não para cálculo de probabilidade calibrada.

**d.** [ ] Normalizar a saída do $k$-NN dividindo pelo seu valor máximo observado no conjunto de teste resolve, por si só, o problema da integral divergente e produz uma densidade de probabilidade válida.

**Heurística:** Falsa dicotomia
**Resposta:** Falso
**Justificativa:** Dividir por um máximo observado é uma renormalização pontual arbitrária — não controla o comportamento da cauda da função em todo o espaço, que é a causa raiz da divergência da integral. Uma constante de reescala finita não pode "curar" uma integral que diverge.

---

## Janela de Parzen e kernel gaussiano

**a.** [ ] A janela de Parzen (hipercubo) e o kernel gaussiano produzem a mesma estimativa de densidade sempre que $h$ é escolhido de forma equivalente nos dois casos, porque ambos implementam exatamente a mesma função de peso.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** As duas são funções de peso diferentes — uma é um corte rígido (peso 1 dentro do cubo, 0 fora), a outra decai suavemente com a distância. Não existe escolha de $h$ que as torne idênticas; a razão de introduzir o kernel gaussiano é justamente eliminar as descontinuidades que o hipercubo produz, algo que nenhuma escolha de $h$ resolveria dentro da própria janela de Parzen.

**b.** [ ] Um ponto de treino localizado exatamente na borda de um hipercubo de largura $h$ centrado num ponto de consulta $\mathbf{x}$ pode contar ou não para $K$, dependendo de detalhes de borda (inclusão estrita ou não) que não têm análogo no kernel gaussiano, que atribui peso positivo (ainda que pequeno) a qualquer distância finita.

**Heurística:** Transferência de domínio
**Resposta:** Verdadeiro
**Justificativa:** A definição de PRML usa $|u_i|\le 1/2$ (inclusão na borda), mas qualquer convenção de fronteira é, por natureza, uma decisão discreta e arbitrária — o kernel gaussiano, por decair suavemente e nunca ser exatamente zero, não tem esse tipo de ambiguidade de borda.

**c.** [ ] As condições $k(u)\ge 0$ e $\int k(u)\,du=1$ (PRML, eq. 2.251–2.252) seriam violadas por um kernel gaussiano com $h$ negativo, mas não por nenhuma outra escolha razoável de $h>0$.

**Heurística:** Contrafactual
**Resposta:** Falso
**Justificativa:** Na fórmula do kernel gaussiano, $h$ só aparece via $h^2$ — um $h$ negativo produz exatamente a mesma função que $|h|$, então não viola as condições de não-negatividade nem de normalização. O caso realmente problemático é $h=0$ (divisão por zero, indefinido), não $h<0$. A premissa do item está errada sobre qual valor de $h$ de fato causa problema.

**d.** [ ] Trocar o kernel gaussiano por um kernel uniforme (janela dura) de mesma largura $h$ elimina completamente a possibilidade de descontinuidades na densidade estimada.

**Heurística:** Falsa dicotomia
**Resposta:** Falso
**Justificativa:** É o oposto do que a aula mostrou: a janela dura (hipercubo/uniforme) é exatamente a fonte original das descontinuidades nas bordas — o kernel gaussiano foi introduzido para **eliminar** esse problema, não o contrário. Trocar de volta para uma janela dura reintroduziria as descontinuidades.

---

## $h$ como parâmetro de suavização

**a.** [ ] No limite $h\to 0^+$, cada ponto de treino distinto se torna, ele mesmo, um pico isolado da densidade estimada — no limite, até $N$ picos, um por ponto de treino.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Conforme $h\to 0$, cada gaussiana no somatório colapsa numa função cada vez mais estreita e alta, centrada em seu próprio ponto de treino, com contribuição desprezível em qualquer outro lugar — no limite, a soma se torna (proporcional a) uma soma de funções delta, uma por ponto distinto. É a extrapolação natural do padrão já observado nesta aula ($h=0{,}3$ produzindo 12 picos, mais que $h=1{,}0$ ou $h=3{,}0$).

**b.** [ ] Se dois datasets diferentes têm o mesmo número de pontos $N$ mas escalas muito diferentes (um varia entre 0 e 1, outro entre 0 e 1000), usar o mesmo valor absoluto de $h$ para os dois produzirá, em geral, graus de suavização relativa muito diferentes.

**Heurística:** Transferência de domínio
**Resposta:** Verdadeiro
**Justificativa:** $h$ é uma largura absoluta; o mesmo $h=1$ é uma suavização enorme (relativa à amplitude) no dataset que varia entre 0 e 1, e praticamente imperceptível no dataset que varia entre 0 e 1000. É por isso que, na prática, $h$ costuma ser escolhido em relação à escala dos dados (ex.: um múltiplo do desvio padrão), não como um número absoluto fixo.

**c.** [ ] O trade-off entre $h$ pequeno (ruidoso) e $h$ grande (borrado) é conceitualmente o mesmo trade-off entre viés e variância discutido em outros contextos de ajuste de modelo — $h$ pequeno tende a variância alta, $h$ grande tende a viés alto.

**Heurística:** Transferência de domínio
**Resposta:** Verdadeiro
**Justificativa:** $h$ pequeno faz a estimativa depender fortemente dos pontos exatos observados (alta variância entre amostras diferentes do mesmo processo); $h$ grande impõe uma suposição forte de suavidade que pode não corresponder à realidade (viés sistemático, borrando estrutura real como a bimodalidade). É exatamente a mesma lógica do trade-off viés-variância de qualquer escolha de complexidade de modelo.

**d.** [ ] Escolher $h$ de forma a minimizar o erro no próprio conjunto de treino (sem nenhuma validação separada) tende a favorecer valores de $h$ artificialmente pequenos.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** Conforme $h\to 0$, a densidade estimada se aproxima cada vez mais de "picos exatamente nos pontos observados" (item a), o que minimiza qualquer métrica de erro avaliada nesses mesmos pontos de treino — um sobreajuste clássico. Sem um conjunto de validação separado, o critério empurraria $h$ para valores pequenos demais, não generalizáveis.

---

## $k$-NN vs. KDE: suavização adaptativa vs. fixa

**a.** [ ] A vantagem da suavização adaptativa do $k$-NN é mais pronunciada em datasets onde a densidade real varia muito de uma região para outra do que em datasets aproximadamente uniformes.

**Heurística:** Transferência de domínio
**Resposta:** Verdadeiro
**Justificativa:** Se a densidade real já é aproximadamente uniforme, uma largura fixa (KDE) e uma largura adaptativa ($k$-NN) tendem a se comportar de forma parecida — a vantagem da adaptação só se manifesta quando há regiões muito densas ao lado de regiões muito esparsas, como no próprio exemplo de `radius_mean` (região densa perto de 12–13, cauda esparsa perto de 25).

**b.** [ ] Como o $k$-NN adapta $d_K(\mathbf{x})$ à densidade local, ele nunca pode sofrer do mesmo problema de "borrar estrutura real" que o KDE sofre com $h$ grande demais.

**Heurística:** Falsa dicotomia
**Resposta:** Falso
**Justificativa:** O $k$-NN tem seu próprio análogo desse problema: $K$ grande demais (no limite, $K=N$) também borra toda a estrutura local, como discutido no aviso do Bloco 4 — a esfera cresce até englobar quase todo o conjunto, e a densidade estimada fica quase constante. Adaptação de largura não é imunidade a excesso de suavização; só muda o mecanismo pelo qual o excesso ocorre.

**c.** [ ] Se dois pontos de consulta estão na mesma região densa dos dados, mas um deles coincide exatamente com um ponto de treino e o outro não, isso não deveria, em geral, causar uma diferença grande em $d_K(\mathbf{x})$ para $K$ moderado ou grande.

**Heurística:** Caso limite
**Resposta:** Verdadeiro
**Justificativa:** A degenerescência de $d_K\to 0$ (item b do Bloco "$k$-NN para densidade") só é severa para $K=1$, quando o próprio ponto coincidente domina inteiramente a distância. Para $K$ moderado ou grande, o $K$-ésimo vizinho é determinado pela dispersão geral de muitos pontos próximos, não por um único ponto coincidente — o efeito de uma coincidência isolada se dilui.

**d.** [ ] A concordância visual entre as curvas de KDE e $k$-NN no grosso da distribuição de `radius_mean` (Bloco 6) seria esperada mesmo se um dos dois métodos estivesse capturando um artefato espúrio e o outro não.

**Heurística:** Falsa dicotomia
**Resposta:** Falso
**Justificativa:** É o oposto da lógica usada na aula: dois métodos independentes, com mecanismos de suavização diferentes, concordando sobre uma estrutura (a bimodalidade) é evidência de que ela é real — não um artefato de um método específico. Se um estivesse capturando um artefato espúrio que o outro não captura, esperaríamos discordância, não concordância.

---

## Custo computacional e armazenamento

**a.** [ ] A necessidade de armazenar todo o conjunto de treino, citada para $k$-NN e KDE, é uma consequência de esses métodos não resumirem os dados em um número fixo de parâmetros — ao contrário do ajuste Gaussiano da Aula 1, que resume $N$ pontos em $\hat{\boldsymbol\mu}$ e $\hat\Sigma$.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** É exatamente o contraste estrutural entre paramétrico e não-paramétrico: o ajuste Gaussiano comprime toda a informação relevante dos $N$ pontos em $d+d(d+1)/2$ números; $k$-NN e KDE, por não assumirem forma nenhuma, precisam manter acesso a cada ponto individual para qualquer consulta nova.

**b.** [ ] Se o objetivo fosse só classificar um único ponto novo (não estimar densidade em toda parte), o custo de avaliar $k$-NN ou KDE nesse único ponto ainda cresceria, em geral, com $N$.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Avaliar a densidade (ou encontrar os $K$ vizinhos) em um único ponto de consulta, sem estrutura de indexação especial, exige comparar esse ponto com todos os $N$ pontos de treino — custo $O(N)$ por consulta, mesmo que só se queira um resultado.

**c.** [ ] Construir uma estrutura de busca em árvore para os dados de treino (mencionado por PRML como mitigação) elimina completamente a necessidade de armazenar o conjunto de treino.

**Heurística:** Falsa dicotomia
**Resposta:** Falso
**Justificativa:** Uma estrutura de árvore acelera a **busca**, mas ainda precisa armazenar (de forma organizada) os próprios pontos de treino — não elimina o armazenamento, só reduz o custo de encontrar os vizinhos relevantes dentro dele.

**d.** [ ] O custo de armazenamento de $k$-NN/KDE e a exigência de $N>d$ para $\hat\Sigma$ na Aula 1 são, ambos, formas do mesmo problema subjacente: dados insuficientes relativos à complexidade do modelo.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** São problemas relacionados ao tema geral de dimensionalidade, mas não o mesmo problema: a exigência $N>d$ é uma questão de **identificabilidade/invertibilidade** de um número finito de parâmetros (falha mesmo com $N$ grande, se $N<d$); o custo de armazenamento de $k$-NN/KDE existe **mesmo quando $N\gg d$** — não é resolvido por ter mais dados, é uma propriedade estrutural de qualquer método que não resuma os dados em parâmetros fixos.

---

## Maldição da dimensionalidade em métodos não-paramétricos

**a.** [ ] Como $k$-NN e KDE não assumem nenhuma família paramétrica, eles não sofrem de nenhuma versão da maldição da dimensionalidade — só o ajuste Gaussiano da Aula 1 sofre desse problema.

**Heurística:** Falsa dicotomia
**Resposta:** Falso
**Justificativa:** É o ponto central do Bloco 7: "não-paramétrico" não é "imune". $k$-NN e KDE sofrem sua própria versão — custo de armazenamento crescente e, segundo o ESL, exigência de densidade amostral $\propto N^{1/p}$ para manter a mesma qualidade de estimativa local conforme $p$ cresce.

**b.** [ ] Segundo o ESL, manter a mesma densidade amostral (cobertura local) ao passar de $p=1$ para $p=10$ dimensões exigiria multiplicar o tamanho do conjunto de dados por um fator que cresce exponencialmente com $p$.

**Heurística:** Transferência de domínio
**Resposta:** Verdadeiro
**Justificativa:** Da relação densidade $\propto N^{1/p}$, manter a mesma densidade ao mudar de $p=1$ para $p$ dimensões exige $N_p = N_1^p$ — uma potência de $N_1$ que cresce exponencialmente com $p$ (ex.: $N_1=100\Rightarrow N_{10}=100^{10}$, exatamente o exemplo citado pelo ESL).

**c.** [ ] O fato de $k$-NN e KDE precisarem armazenar todo o conjunto de treino é agravado, não resolvido, pelo crescimento da quantidade de dados necessária em alta dimensão — os dois problemas se combinam.

**Heurística:** Transferência de domínio
**Resposta:** Verdadeiro
**Justificativa:** Se a maldição exige exponencialmente mais dados para manter a qualidade da estimativa em alta dimensão, e cada ponto adicional precisa ser armazenado e revisitado, os dois problemas — custo de armazenamento e necessidade de mais dados — se reforçam mutuamente, não se cancelam.

**d.** [ ] Uma forma de escapar completamente da maldição da dimensionalidade, para qualquer método não-paramétrico, é aumentar $N$ até que $N>2^d$.

**Heurística:** Falsa dicotomia
**Resposta:** Falso
**Justificativa:** Não existe um limiar simples desse tipo que "resolva" a maldição — a concentração de medida (Bloco 2) é um fenômeno geométrico que persiste independentemente de quão grande $N$ seja; aumentar $N$ ajuda a mitigar o problema de dados esparsos, mas não elimina o colapso do contraste relativo de distâncias, que é sobre geometria, não sobre quantidade de dados.

---

## Ponte para a Aula 3: $d_K(\mathbf{x})$ como métrica de grafo

**a.** [ ] Reaproveitar $d_K(\mathbf{x})$ como métrica de densidade local para construir um grafo é possível porque o valor de $d_K(\mathbf{x})$ já foi mostrado, no Bloco 4, como inversamente relacionado à densidade local — a mesma quantidade, um uso diferente.

**Heurística:** Transferência de domínio
**Resposta:** Verdadeiro
**Justificativa:** É exatamente a lógica da ponte: $d_K(\mathbf{x})$ pequeno significa região densa, $d_K(\mathbf{x})$ grande significa região esparsa — essa mesma informação, hoje usada para estimar $p(\mathbf{x})$, pode orientar quais pontos "fazem sentido" conectar num grafo de densidade (Aula 3), sem precisar de nenhuma modificação na quantidade em si.

**b.** [ ] Se dois pontos $\mathbf{x}_1,\mathbf{x}_2$ pertencem à mesma região de alta densidade, é razoável esperar que $d_K(\mathbf{x}_1)$ e $d_K(\mathbf{x}_2)$ sejam parecidos entre si, para o mesmo $K$.

**Heurística:** Caso limite
**Resposta:** Verdadeiro
**Justificativa:** Como $d_K(\mathbf{x})$ é determinado pela densidade local (Bloco 4), pontos na mesma vizinhança de alta densidade devem ter valores parecidos de $d_K$ para o mesmo $K$ — é a mesma propriedade que permitiu, no Bloco 6, comparar $x_0=12$ com outro ponto próximo na mesma região densa e ver pouca variação em $d_K$.

**c.** [ ] Usar $d_K(\mathbf{x})$ para construir caminhos num grafo exige, necessariamente, resolver primeiro o problema de a integral de $1/d_K(\mathbf{x})^D$ divergir — sem isso, a construção do grafo não é matematicamente válida.

**Heurística:** Contrafactual
**Resposta:** Falso
**Justificativa:** A divergência da integral só é um problema quando se quer tratar a quantidade como uma densidade de probabilidade calibrada (Bloco "isto não é uma densidade de verdade"). Usar $d_K(\mathbf{x})$ como métrica relativa de proximidade/densidade para conectar pontos num grafo não exige normalização nenhuma — é exatamente o tipo de uso "comparação relativa" que já vimos ser válido sem resolver a integral.

**d.** [ ] A escolha de $K$ que funcionava bem para estimar densidade no Bloco 4 (nem pequeno, nem grande demais) é, a priori, um bom candidato para o mesmo papel de parâmetro de suavização na construção do grafo da Aula 3, ainda que a validação final dependa do contexto de clustering, não só de densidade.

**Heurística:** Transferência de domínio
**Resposta:** Verdadeiro
**Justificativa:** Como o papel estrutural de $K$ (suavização local, nem ruidoso nem borrado) não muda entre os dois usos, é razoável usar a mesma faixa de valores como ponto de partida — mas o item já reconhece, corretamente, que a validação definitiva depende do objetivo de clustering da Aula 3, não só da qualidade de estimativa de densidade isolada.
