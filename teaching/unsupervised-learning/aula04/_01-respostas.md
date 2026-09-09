# Respostas da Aula 4 — Pausas Ativas e Gabarito dos Exercícios

> Arquivo de apoio, não publicado (prefixo `_`). Duas partes: (1)
> discussão em prosa das 5 pausas ativas do `index.qmd` (a pergunta
> motivadora + a resolução do V/F, que no `index.qmd` só aparece nos
> slides RevealJS, nunca nas notas HTML); (2) o gabarito completo (com
> heurística e justificativa) dos 7 blocos de V/F da seção Exercícios,
> que ficam sem solução no `index.qmd` publicado — trabalho para o
> aluno resolver por conta. As 3 questões discursivas da seção
> Exercícios não têm gabarito único registrado aqui (são abertas, para
> discussão em aula/monitoria), seguindo o mesmo padrão das aulas
> anteriores desta disciplina.

## Parte 1 — Pausas Ativas

### Pausa 1 — Ruído do HDBSCAN vs. ambiguidade do GMM

A pergunta pergunta se um paciente marcado como ruído pelo HDBSCAN é
necessariamente "igualmente parecido" com as duas populações. Não é: o
HDBSCAN mede densidade **local geométrica** (o paciente não tem vizinhos
suficientes por perto, na escala de `min_samples`/`min_cluster_size`),
enquanto o GMM mede probabilidade **sob um modelo global** ajustado a
todos os dados. As duas noções podem discordar — um paciente pode
escapar do limiar de densidade local do HDBSCAN e, ainda assim, cair
claramente dentro da elipse de um único componente do GMM, com
responsabilidade próxima de $1$. A responsabilidade $50/50$ também não
depende só de distância euclidiana bruta às médias: como a fórmula de
Bayes pondera pela densidade completa (incluindo covariância e peso de
mistura), duas médias diferentes com formas/pesos diferentes podem
deslocar o ponto de equilíbrio para longe do ponto médio geométrico. No
caso degenerado em que os dois componentes têm exatamente a mesma média
e covariância, a densidade cancela na razão de Bayes e sobra só
$\gamma(z_k)=\pi_k$, independente de onde o ponto está — um bom
lembrete de que a responsabilidade é sempre uma função dos parâmetros
inteiros do modelo, não só da posição do ponto.

- ✔ Um paciente marcado como ruído pode receber responsabilidade
  próxima de $1$ sob um GMM — "vale geométrico local" e "ambiguidade
  probabilística global" não são a mesma coisa.
- ✗ Responsabilidade $0{,}5/0{,}5$ não implica equidistância euclidiana
  bruta — depende de $\pi_k$ e $\Sigma_k$ também.
- ✔ Com densidades idênticas nos componentes, a razão de Bayes cancela
  o termo de densidade, sobrando só $\pi_k$, para qualquer ponto.
- ✔ A mesma lógica (sobreposição contínua pede resposta contínua)
  transfere para qualquer domínio com segmentos que se misturam.

### Pausa 2 — O que significa responsabilidade 50/50

A pergunta contrasta a incerteza de uma moeda (evento futuro, ainda não
decidido) com a incerteza sobre a origem de um paciente (fato já
determinado, mas desconhecido para nós). A responsabilidade $50/50$ é a
melhor estimativa do modelo sobre um fato fixo — o paciente realmente
nasceu de uma única população, o GMM só não tem evidência suficiente
nos dois atributos usados para decidir qual. Mais atributos não reduz
automaticamente essa ambiguidade: pode até piorar (maldição da
dimensionalidade, Aula 2) ou simplesmente confirmar que a sobreposição
é real também em mais dimensões. No Passo M (Bloco 6), um paciente
$50/50$ não é descartado nem ignorado — ele contribui com metade do seu
peso para a reestimação de **cada** um dos dois componentes,
exatamente como fração. E se o modelo verdadeiro tivesse só $1$
componente, esperaríamos ver muito mais gente perto de $50/50$ (na
verdade, todo mundo perto de $\pi_k$ para $K=1$ isso seria trivialmente
$1$, mas a intuição geral é: quanto menos separação real, mais gente na
faixa ambígua) do que os $9$ casos observados, que são a exceção, não a
regra, entre os $569$ pacientes.

- ✔ É incerteza sobre um fato já determinado, não sobre um evento
  aleatório futuro.
- ✗ Mais atributos não garante menos ambiguidade para pontos
  específicos.
- ✔ Responsabilidade fracionária = peso fracionário no Passo M, nunca
  descartado.
- ✔ Com um único componente verdadeiro, a ambiguidade tenderia a ser
  muito mais disseminada do que os $9$ casos raros observados.

### Pausa 3 — Responsabilidade muda com os parâmetros

A pergunta testa se $\gamma(z_{nk})$ é uma propriedade fixa do ponto ou
uma função dos parâmetros correntes do modelo. É a segunda: a cada
rodada do EM, os parâmetros mudam (Passo M) e a responsabilidade é
recalculada do zero a partir deles (novo Passo E) — não existe
"responsabilidade permanente" de um paciente. Sobre o efeito de dobrar
a covariância do componente maligno: o raciocínio "gaussiana mais
espalhada sempre atribui mais densidade a todo ponto" é uma falsa
generalização — a densidade gaussiana se normaliza a integral $1$, então
espalhar a covariância **reduz o pico** e aumenta a cauda; o efeito
líquido sobre a responsabilidade de um ponto específico depende de
onde ele está (perto do pico ou na cauda), não é uniformemente "mais
densidade". Dois pacientes idênticos em atributos, com a mesma
responsabilidade hoje, podem divergir depois de uma rodada de
reestimação porque o Passo M usa a soma sobre **todos** os pontos —
qualquer assimetria em como os dois entram nessa soma agregada (por
exemplo, se um deles aparece duplicado no dataset) muda o resultado
para ambos de forma diferente. Com $K=1$, não há termo concorrente no
denominador de Bayes — a razão degenera trivialmente em $1$.

- ✔ $\gamma(z_{nk})$ é recalculada a cada rodada — função corrente dos
  parâmetros, nunca fixa ao ponto.
- ✗ Covariância maior reduz o pico da densidade (normalização) — o
  efeito sobre $\gamma$ depende da posição do ponto, não é sempre
  "aumenta".
- ✔ Dois pacientes idênticos podem divergir se entrarem de forma
  assimétrica nas somas agregadas do Passo M.
- ✔ Com $K=1$, a razão de Bayes degenera em $1$ para o único
  componente, sempre.

### Pausa 4 — GMM completo é sempre melhor que o KMeans?

A pergunta pede para não tratar "o GMM generaliza matematicamente o
KMeans" como "o GMM é sempre a escolha prática melhor". As quatro
afirmações exploram por que não: (1) mais parâmetros (covariância livre
por componente) exige mais dados para estimar sem overfitar — com
poucos pontos por cluster, o KMeans, mais restrito, generaliza melhor;
(2) se os clusters verdadeiros já são esféricos e homogêneos entre si,
o GMM convergiria para algo parecido com a suposição do KMeans, e a
vantagem prática se estreita; (3) um cluster alongado é exatamente o
caso em que a liberdade de covariância do GMM compensa — o KMeans,
travado em bolas circulares do mesmo tamanho, cortaria esse cluster de
forma artificial perto da fronteira com outro; (4) "caso particular
matemático" (um limite formal) não implica nada sobre velocidade de
convergência prática — o KMeans, com menos parâmetros e uma atualização
mais simples por iteração, tipicamente converge em menos iterações, não
mais.

- ✔ Mais parâmetros com poucos dados por cluster pode overfitar —
  KMeans generaliza melhor nesse regime.
- ✔ Com covariâncias verdadeiramente esféricas e idênticas, a vantagem
  prática do GMM sobre o KMeans encolhe.
- ✔ Cluster alongado: GMM orienta/estica a elipse; KMeans corta
  artificialmente na fronteira.
- ✗ "Caso particular" é relação de limite matemático, não de
  velocidade — KMeans tipicamente converge em menos iterações.

### Pausa 5 — Mais componentes, mais verossimilhança? (fechamento)

A pergunta antecipa o problema central da Aula 5: por que a
log-verossimilhança de treino não serve, sozinha, para escolher $K$.
Qualquer solução com $K=2$ pode ser "imitada" por uma solução com
$K=10$ simplesmente zerando o peso $\pi_k$ dos $8$ componentes extras —
logo, o ótimo com $K=10$ nunca é pior que o ótimo com $K=2$ no mesmo
conjunto de treino. Isso é exatamente por que escolher $K$ maximizando
a verossimilhança de treino não é confiável: o critério empurra sempre
para mais componentes, não para o número real. A mesma lógica de "mais
flexibilidade sempre ajusta melhor o treino, sem necessariamente
generalizar" já apareceu nesta disciplina antes (por exemplo, ajustar
formas cada vez mais flexíveis aos dados de treino sem controle de
complexidade). E colapsar a covariância de um dos $10$ componentes
sobre um único ponto não dá uma verossimilhança "artificialmente
baixa" — dá uma verossimilhança tendendo a **infinito** (a
singularidade do Bloco 4), o oposto do que a afirmação sugere.

- ✔ $K=10$ nunca fica pior que $K=2$ no treino — pode sempre "imitar" a
  solução menor.
- ✗ Por isso mesmo não é um critério confiável — sempre favorece mais
  componentes.
- ✔ É a mesma lógica de overfitting já vista antes nesta disciplina.
- ✗ Colapsar sobre um ponto dá verossimilhança tendendo a infinito, não
  "baixa".

---

## Parte 2 — Gabarito dos Exercícios (Verdadeiro/Falso)

### Partição rígida vs. probabilística — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Uma partição probabilística (GMM) e uma partição
rígida (HDBSCAN ou KMeans) respondem exatamente à mesma pergunta
matemática, diferindo apenas na forma de apresentar a resposta final.

**Resposta:** Falso

**Justificativa:** Não é só uma questão de apresentação — os métodos
otimizam objetivos diferentes (distorção rígida vs. verossimilhança sob
um modelo gerador com variável latente) e usam noções diferentes de
"pertencimento" (densidade local conectada vs. probabilidade posterior
sob um modelo global). Arredondar uma responsabilidade não reproduz a
lógica de conectividade do HDBSCAN, nem vice-versa.

### Partição rígida vs. probabilística — item (b)

**Heurística:** Caso limite

**Afirmação:** ✔ Se dois clusters verdadeiros são separados por um vale
de densidade genuíno, o GMM, ao convergir bem, tende a atribuir
responsabilidades próximas de $0$ ou $1$ para a maioria dos pontos.

**Resposta:** Verdadeiro

**Justificativa:** Um vale de densidade genuíno geralmente corresponde
a componentes gaussianos bem separados (médias distantes relativas às
covariâncias) — nesse regime, a razão de Bayes já favorece fortemente
um dos dois componentes para a maioria dos pontos, mesmo sem forçar o
limite $\epsilon\to0$ do Bloco 8. Ser "probabilístico" não significa
"sempre ambíguo": significa que a ferramenta consegue expressar
ambiguidade quando ela existe, não que a produz artificialmente.

### Partição rígida vs. probabilística — item (c)

**Heurística:** Aplicação

**Afirmação:** ✔ A principal vantagem prática do GMM sobre o HDBSCAN
nesta aula é que o GMM nunca deixa nenhum ponto sem atribuição, mesmo
que fracionária.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente o contraste do Bloco 2 e do Bloco 7: os
$168$ pacientes que o HDBSCAN descartou como ruído recebem, no GMM, uma
responsabilidade concreta (ambígua ou não) para cada componente —
nenhum paciente fica "sem resposta".

### Partição rígida vs. probabilística — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Um paciente com responsabilidade $(0{,}5,0{,}5)$ é
necessariamente um erro de convergência do algoritmo.

**Resposta:** Falso

**Justificativa:** É o oposto do que o Bloco 2/5 demonstra: uma
responsabilidade $50/50$ é a resposta honesta do modelo quando a
evidência realmente não pende para nenhum lado (sobreposição real entre
populações) — não um sintoma de bug ou não-convergência.

### Variável latente e a história geradora do GMM — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ $z_n$ é observado durante o ajuste do modelo aos
dados — é essa observação que permite calcular $\gamma(z_{nk})$
diretamente, sem precisar de Bayes.

**Resposta:** Falso

**Justificativa:** É exatamente o oposto da premissa (3) do Bloco 3:
$z_n$ nunca é observado — só $\mathbf{x}_n$ é. É justamente por não
observar $z_n$ que Bayes é necessário para inferir a probabilidade
posterior $\gamma(z_{nk})=p(z_{nk}=1\mid\mathbf{x}_n)$.

### Variável latente e a história geradora do GMM — item (b)

**Heurística:** Aplicação

**Afirmação:** ✔ A codificação 1-de-$K$ de $\mathbf{z}$ garante que,
para qualquer ponto gerado pelo modelo, exatamente uma população é
responsável por ele.

**Resposta:** Verdadeiro

**Justificativa:** É a própria definição da codificação 1-de-$K$
apresentada no Bloco 3: um vetor binário com exatamente uma coordenada
igual a $1$ — nunca zero, nunca mais de uma, por construção.

### Variável latente e a história geradora do GMM — item (c)

**Heurística:** Caso limite

**Afirmação:** ✔ Se $\pi_1=1$ e todos os demais $\pi_k=0$, a
distribuição marginal do GMM se reduz exatamente ao modelo de uma
única gaussiana da Aula 1.

**Resposta:** Verdadeiro

**Justificativa:** Com $\pi_1=1$ e os demais nulos, a soma
$\sum_k\pi_k\mathcal{N}(\mathbf{x}\mid\mu_k,\Sigma_k)$ tem um único
termo sobrevivente, $\mathcal{N}(\mathbf{x}\mid\mu_1,\Sigma_1)$ —
exatamente o modelo de uma gaussiana ajustado na Aula 1. O GMM
generaliza a Aula 1 como caso particular quando $K=1$ (ou quando um
$\pi_k$ domina completamente).

### Variável latente e a história geradora do GMM — item (d)

**Heurística:** Aplicação

**Afirmação:** ✔ Marginalizar $z$ é o que conecta a formulação
generativa nova desta aula à fórmula de mistura de gaussianas já
escrevível desde a Aula 1.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente a passagem do Bloco 3: somar
$p(z)p(\mathbf{x}\mid z)$ sobre os $K$ estados de $z$ recupera
$p(\mathbf{x})=\sum_k\pi_k\mathcal{N}(\mathbf{x}\mid\mu_k,\Sigma_k)$ —
a mesma soma que já era matematicamente possível de escrever antes,
agora justificada por uma história geradora explícita.

### Log-verossimilhança do GMM e a necessidade do EM — item (a)

**Heurística:** Caso limite

**Afirmação:** ✔ A dificuldade de maximizar $\ln p(X\mid\pi,\mu,\Sigma)$
diretamente desaparece se $K=1$.

**Resposta:** Verdadeiro

**Justificativa:** Com $K=1$, a soma dentro do logaritmo (Bloco 4) tem
um único termo — $\ln[\pi_1\mathcal{N}(\mathbf{x}_n\mid\mu_1,\Sigma_1)]$
—, e o $\ln$ age diretamente sobre a exponencial gaussiana, cancelando
limpo, exatamente como na solução fechada da Aula 1.

### Log-verossimilhança do GMM e a necessidade do EM — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Uma singularidade da log-verossimilhança representa um
bom ajuste generalizável do modelo, só num regime numérico extremo.

**Resposta:** Falso

**Justificativa:** É o oposto do que o Bloco 4 explica: uma
singularidade é um caso patológico de *overfitting* de um único ponto
(a variância de um componente colapsa exatamente sobre ele), não um bom
ajuste — é por isso que se buscam máximos locais bem-comportados, não
o "máximo global" degenerado.

### Log-verossimilhança do GMM e a necessidade do EM — item (c)

**Heurística:** Aplicação

**Afirmação:** ✔ Rodar o EM com várias inicializações (`n_init`) e
escolher a de maior log-verossimilhança mitiga o risco de máximo local
ruim — não evita singularidades.

**Resposta:** Verdadeiro

**Justificativa:** São dois problemas distintos discutidos no Bloco 7:
múltiplos máximos locais (mitigado por múltiplas inicializações) e
singularidades (que exigem salvaguardas específicas, como um piso
mínimo de variância, já embutidas no `sklearn`).

### Log-verossimilhança do GMM e a necessidade do EM — item (d)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se a log-verossimilhança do GMM tivesse solução
fechada, o EM ainda assim seria necessário, só que como alternativa
igualmente rápida.

**Resposta:** Falso

**Justificativa:** Se houvesse solução fechada, não haveria motivo
algum para usar um algoritmo iterativo — o EM existe precisamente
**porque** não há forma fechada (Bloco 4); com solução fechada, o EM
seria estritamente desnecessário, não uma alternativa "igualmente
rápida" (na prática seria mais lento, por ser iterativo).

### O Passo E: responsabilidades e Bayes — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ $\gamma(z_{nk})$ é a probabilidade a **priori** de o
ponto $n$ vir do componente $k$, calculada antes de observar
$\mathbf{x}_n$.

**Resposta:** Falso

**Justificativa:** É o oposto: $\pi_k$ é a probabilidade a priori;
$\gamma(z_{nk})=p(z_{nk}=1\mid\mathbf{x}_n)$ é a probabilidade a
**posteriori**, calculada depois de observar $\mathbf{x}_n$, via Bayes
(Bloco 3/5).

### O Passo E: responsabilidades e Bayes — item (b)

**Heurística:** Aplicação

**Afirmação:** ✔ Para um ponto $n$ fixo, $\sum_k\gamma(z_{nk})=1$,
independentemente dos valores correntes de $\pi,\mu,\Sigma$.

**Resposta:** Verdadeiro

**Justificativa:** A fórmula do Passo E (Bloco 5) normaliza pela soma
sobre todos os $K$ componentes no denominador — por construção, a soma
das responsabilidades de um ponto é sempre $1$, quaisquer que sejam os
parâmetros correntes.

### O Passo E: responsabilidades e Bayes — item (c)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se dois componentes têm o mesmo $\mu_k,\Sigma_k$ mas
pesos diferentes, a responsabilidade para o de maior peso será sempre
estritamente maior, para qualquer ponto.

**Resposta:** Falso

**Justificativa:** Com densidades idênticas nos dois componentes
($\mathcal{N}(\mathbf{x}\mid\mu_1,\Sigma_1)=\mathcal{N}(\mathbf{x}\mid
\mu_2,\Sigma_2)$ para todo $\mathbf{x}$), a razão de Bayes cancela o
termo de densidade e $\gamma(z_{nk})=\pi_k$ exatamente — a comparação
entre pesos é sempre a mesma proporção $\pi_1{:}\pi_2$, então "maior
peso $\Rightarrow$ responsabilidade maior" é verdade aqui, mas a
afirmação erra ao dizer que isso é geral para "qualquer ponto" como se
fosse uma propriedade universal do Bayes — na verdade só vale neste
caso degenerado específico (densidades iguais); em geral, a densidade
de cada componente no ponto pesa tanto quanto o prior, podendo reverter
a ordem.

### O Passo E: responsabilidades e Bayes — item (d)

**Heurística:** Aplicação

**Afirmação:** ✔ Recalcular $\gamma(z_{nk})$ após cada Passo M é
necessário porque os parâmetros usados na fórmula de Bayes mudaram.

**Resposta:** Verdadeiro

**Justificativa:** É a lógica central do ciclo EM (Bloco 7):
$\gamma(z_{nk})$ é função dos parâmetros correntes, não uma etiqueta
fixa — mudar os parâmetros no Passo M invalida as responsabilidades
antigas, exigindo um novo Passo E.

### O Passo M: atualizações ponderadas — item (a)

**Heurística:** Caso limite

**Afirmação:** ✔ $\mu_k=\frac1{N_k}\sum_n\gamma(z_{nk})\mathbf{x}_n$ se
reduz à média aritmética simples quando $\gamma(z_{nk})=1/K$ para todo
ponto e componente.

**Resposta:** Verdadeiro

**Justificativa:** Com $\gamma(z_{nk})=1/K$ constante, $N_k=N/K$ para
todo $k$, e $\mu_k=\frac{1}{N/K}\sum_n\frac1K\mathbf{x}_n=\frac1N\sum_n
\mathbf{x}_n$ — a média aritmética simples de todos os $N$ pontos,
igual para todos os componentes (caso degenerado em que nenhum
componente é informativo).

### O Passo M: atualizações ponderadas — item (b)

**Heurística:** Aplicação

**Afirmação:** ✔ $N_k$ pode assumir um valor não inteiro, mesmo com $N$
inteiro.

**Resposta:** Verdadeiro

**Justificativa:** $N_k=\sum_n\gamma(z_{nk})$ é uma soma de números
reais entre $0$ e $1$ (responsabilidades fracionárias) — não uma
contagem de pontos. O próprio Bloco 6 dá o exemplo: um componente que
"convence" $50$ pacientes por completo e $20$ pela metade tem
$N_k=60{,}0$ exatamente por acaso; em geral o resultado é fracionário.

### O Passo M: atualizações ponderadas — item (c)

**Heurística:** Contrafactual

**Afirmação:** ✗ A atualização de $\Sigma_k$ usa o $\mu_k$ da rodada
**anterior**, não o recém-calculado nesta mesma rodada.

**Resposta:** Falso

**Justificativa:** É o oposto do que o Bloco 7 (algoritmo completo)
especifica: dentro do mesmo Passo M, calcula-se primeiro o novo
$\mu_k$, e **depois** usa-se esse valor já atualizado para calcular
$\Sigma_k$ — a mesma ordem já usada na Aula 1 para uma única gaussiana.
Usar o $\mu_k$ antigo produziria uma covariância inconsistente com a
média corrente.

### O Passo M: atualizações ponderadas — item (d)

**Heurística:** Aplicação

**Afirmação:** ✔ A restrição $\sum_k\pi_k=1$ é o único motivo do
multiplicador de Lagrange — $\mu_k$ e $\Sigma_k$ não têm restrição
análoga.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente a assimetria do Bloco 6: $\mu_k$ e
$\Sigma_k$ são livres (qualquer vetor/matriz definida positiva serve),
então suas derivadas igualadas a zero já isolam a solução diretamente;
só $\pi_k$ tem uma restrição de soma a respeitar, exigindo o
multiplicador de Lagrange para incorporar essa restrição na
otimização.

### KMeans como caso limite do GMM — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Covariâncias esféricas, porém diferentes entre
componentes ($\Sigma_1=\epsilon_1I\ne\Sigma_2=\epsilon_2I$), não
bastariam para reproduzir exatamente a atribuição rígida do KMeans no
limite.

**Resposta:** Verdadeiro

**Justificativa:** A derivação do Bloco 8 depende especificamente de um
único $\epsilon$ compartilhado — é essa premissa que faz o termo de
normalização $(2\pi\epsilon)^{D/2}$ cancelar igualmente entre
componentes na razão de Bayes, sobrando só a comparação das distâncias
$\|\mathbf{x}-\mu_k\|^2$. Com $\epsilon_k$ diferentes, o termo de
normalização não cancela, e a "vitória" de um componente no limite
dependeria de uma combinação de distância **e** da razão entre os
$\epsilon_k$, não seria idêntica à regra pura "vizinho mais próximo" do
KMeans.

### KMeans como caso limite do GMM — item (b)

**Heurística:** Aplicação

**Afirmação:** ✔ O limite $\epsilon\to0$ produz atribuição rígida
porque a exponencial do componente mais próximo domina
exponencialmente — não porque os $\pi_k$ se igualam.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente o texto do PRML citado no Bloco 8: o
resultado vale "independentemente dos valores de $\pi_k$, desde que
nenhum seja exatamente zero" — a dominância vem da divisão por
$\epsilon\to0$ dentro da exponencial, não de qualquer relação entre os
pesos de mistura.

### KMeans como caso limite do GMM — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Um GMM com covariâncias esféricas idênticas, mas
$\epsilon$ grande, produziria responsabilidades próximas às do KMeans.

**Resposta:** Falso

**Justificativa:** A verificação numérica do Bloco 8 mostra exatamente
o contrário: com $\epsilon=1{,}0$ (grande, relativo à escala dos
dados), a responsabilidade média máxima é só $0{,}904$ — bem longe de
$1$ — e a concordância com o KMeans é $95{,}78\%$, não $100\%$. É
precisamente o $\epsilon$ **pequeno** que aproxima do KMeans; formato
esférico e idêntico sozinho não basta sem o limite.

### KMeans como caso limite do GMM — item (d)

**Heurística:** Aplicação

**Afirmação:** ✔ O KMeans, por não estimar covariância, não representa
clusters com formas alongadas/giradas de forma diferente entre si — só
bolas do mesmo tamanho.

**Resposta:** Verdadeiro

**Justificativa:** É a consequência direta da premissa (1) do Bloco 8
($\Sigma_k=\epsilon I$ idêntico para todos): todos os clusters do
KMeans são, por construção, esféricos e do mesmo "raio" efetivo — a
elipse alongada e maior do componente maligno mostrada no Bloco 7
simplesmente não é representável nesse regime.

### O resultado no Breast Cancer Wisconsin — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ O ARI do GMM ser maior é, sozinho, prova de que o GMM
é estritamente superior ao HDBSCAN para clustering em geral.

**Resposta:** Falso

**Justificativa:** O Bloco 7 é explícito sobre isso: a comparação de
ARI favorece estruturalmente o GMM aqui porque ele atribui todo mundo
a algum componente, enquanto o HDBSCAN descarta $29{,}5\%$ dos
pacientes como ruído (o que já penaliza o ARI do HDBSCAN nessa
métrica específica) — isso é uma consequência de como cada método trata
os pontos difíceis **deste** dataset, não uma prova de superioridade
geral do GMM sobre HDBSCAN.

### O resultado no Breast Cancer Wisconsin — item (b)

**Heurística:** Aplicação

**Afirmação:** ✔ O GMM atribuir responsabilidade máxima a todos os
$569$ pacientes permite calcular o ARI sobre a população inteira, ao
contrário do ARI do HDBSCAN excluindo ruído.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente a diferença de contabilidade discutida
no Bloco 7: o ARI de $0{,}792$ do GMM usa todos os $569$ pacientes; já
um dos dois ARIs do HDBSCAN citados da Aula 3 ($0{,}644$) exclui
explicitamente os $168$ pacientes de ruído da comparação, exigindo essa
exclusão para ser calculado daquela forma.

### O resultado no Breast Cancer Wisconsin — item (c)

**Heurística:** Transferência

**Afirmação:** ✗ O componente $1$ do GMM ($189$M/$8$B) é mais puro
proporcionalmente do que o cluster $100\%$ maligno de $54$ pacientes do
HDBSCAN.

**Resposta:** Falso

**Justificativa:** O componente $1$ do GMM tem pureza
$189/197\approx95{,}9\%$ — alta, mas estritamente menor que os $100\%$
de pureza do cluster de $54$ pacientes do HDBSCAN (Aula 3). O GMM cobre
bem mais pacientes malignos ($189$ vs. $54$), mas ao custo de incluir
$8$ benignos que o cluster mais restrito do HDBSCAN não incluía — um
trade-off entre cobertura e pureza, não uma superioridade em ambos os
eixos ao mesmo tempo.

### O resultado no Breast Cancer Wisconsin — item (d)

**Heurística:** Contrafactual

**Afirmação:** ✗ Os $9$ pacientes de responsabilidade mais ambígua
estão necessariamente entre os $168$ marcados como ruído pelo HDBSCAN.

**Resposta:** Falso

**Justificativa:** Verificado numericamente: dos $9$ pacientes com
$|\gamma-0{,}5|<0{,}05$ no GMM, só $3$ (índices $41$, $318$, $489$)
foram marcados como ruído pelo HDBSCAN — os outros $6$ caíram dentro do
cluster majoritariamente benigno do HDBSCAN, apesar de o GMM os achar
ambíguos. Os dois fenômenos vêm de critérios diferentes (densidade
local vs. probabilidade posterior global) e não coincidem
necessariamente ponto a ponto, mesmo nascendo da mesma região geral de
sobreposição entre as duas populações.
