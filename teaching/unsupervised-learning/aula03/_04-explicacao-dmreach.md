# Entendendo $d_{\mathrm{mreach}}$ (distância de alcançabilidade mútua)

Anotação de apoio, não publicada — só para eu entender melhor antes de decidir o
que (se algo) muda no `index.qmd`.

**Três versões anteriores desta nota tinham erros que esta corrige:** a
primeira omitia o `minPts` do DBSCAN; a segunda corrigiu isso mas ainda
tratava "$d_{\mathrm{mreach}}(a,b)\le\varepsilon$" como se determinasse
sozinho se $a$ e $b$ ficam no mesmo cluster — não determina, a definição de
cluster no DBSCAN é **recursiva** (uma cadeia de conexões, não um par
isolado); a terceira corrigiu isso mas ainda usava $K=\text{minPts}$ direto —
**errado por um**, porque $N_\varepsilon(p)$ conta o próprio $p$ e
$\mathrm{core}_K(p)$ não. Verifiquei numericamente contra o `DBSCAN` do
`scikit-learn` (ver seção 2): o valor certo é $K=\text{minPts}-1$.

## 1. A definição do DBSCAN é recursiva — isso é o ponto central

DBSCAN tem dois parâmetros: $\varepsilon$ e `minPts` (perto do $K$ do core
distance, mas não exatamente igual — a relação exata, $K=\text{minPts}-1$, é
a seção 2; no HDBSCAN esse papel é feito por `min_samples`).

- Um ponto $p$ é **núcleo** (*core point*) se $|N_\varepsilon(p)|\ge
  \text{minPts}$ — pelo menos `minPts` vizinhos a distância $\le\varepsilon$.
- $q$ é **diretamente densidade-alcançável** a partir de $p$ se $p$ é núcleo e
  $d(p,q)\le\varepsilon$.
- $q$ é **densidade-alcançável** a partir de $p$ se existe uma **cadeia** de
  pontos $p=x_0, x_1, \dots, x_n=q$ onde cada $x_{i+1}$ é diretamente
  densidade-alcançável a partir de $x_i$ — ou seja, o fecho transitivo da
  relação anterior, não um único passo.
- Um **cluster** é um conjunto maximal de pontos conectados por essas cadeias.

O ponto crítico: **dois pontos podem estar arbitrariamente longe um do outro
(distância bruta grande) e ainda assim pertencer ao mesmo cluster**, desde que
exista uma cadeia de núcleos densos ligando os dois passo a passo. Pense nas
duas luas desta aula: dois pontos nas pontas opostas da mesma lua estão longe
um do outro em linha reta, mas pertencem ao mesmo cluster porque existe uma
trilha contínua de pontos densos acompanhando o arco da lua inteira, cada elo
da corrente perto o bastante do próximo.

## 2. O que a fórmula do $d_{\mathrm{mreach}}$ realmente captura: só um elo da corrente

$$d_{\mathrm{mreach}}(a,b) = \max\bigl(\mathrm{core}_K(a),\ \mathrm{core}_K(b),\ d(a,b)\bigr)$$

**Cuidado com a contagem: $K$ não é `minPts`, é `minPts - 1`.**
$N_\varepsilon(p)$, na convenção original do DBSCAN (Ester et al., 1996) e a
que o `scikit-learn` usa, **conta o próprio $p$** — a distância de $p$ a si
mesmo é $0\le\varepsilon$, sempre. Então "$|N_\varepsilon(p)|\ge\text{minPts}$"
significa "pelo menos $\text{minPts}-1$ **outros** pontos a distância
$\le\varepsilon$" — e $\mathrm{core}_K(p)$, por definição, é a distância ao
$K$-ésimo vizinho **sem contar $p$**. Os dois só batem com

$$K = \text{minPts} - 1.$$

Testei isso numericamente (`sklearn.cluster.DBSCAN` vs.
`NearestNeighbors` para o core distance, mesmo `eps`, ambos os $K$): com
$K=\text{minPts}-1$ o conjunto de pontos-núcleo bate exatamente
(109 de 109, no meu teste); com $K=\text{minPts}$ direto, não bate
(109 vs. 102) — sobra sistematicamente um vizinho de diferença, exatamente o
efeito de contar ou não o próprio ponto.

Com o $K$ certo, "$p$ é núcleo a um limiar $\varepsilon$" tem uma tradução
direta em termos de core distance:

$$p \text{ é núcleo} \iff |N_\varepsilon(p)|\ge \text{minPts} \iff \mathrm{core}_K(p)\le\varepsilon,\quad K=\text{minPts}-1$$

(se a distância até o $K$-ésimo vizinho, sem contar $p$, já é
$\le\varepsilon$, existem ao menos $K$ outros pontos dentro do raio
$\varepsilon$ — mais o próprio $p$, dá $K+1=\text{minPts}$ pontos em
$N_\varepsilon(p)$ — é a própria definição de $\mathrm{core}_K$ batendo com a
de núcleo.) Logo:

$$\mathrm{core}_K(p)\le\varepsilon \ \text{e}\ \mathrm{core}_K(q)\le\varepsilon \ \text{e}\ d(p,q)\le\varepsilon
\quad\iff\quad
d_{\mathrm{mreach}}(p,q)\le\varepsilon$$

Isso é verdade e é uma equivalência exata — **mas ela é sobre uma única
aresta direta** (um elo), exatamente o mesmo grau de generalidade que
"diretamente densidade-alcançável" tem no DBSCAN. Ela diz: "$p$ é núcleo, $q$ é
núcleo, e os dois estão próximos o bastante para uma conexão de um só passo."
Ela **não** diz nada sobre pares de pontos que só se conectam através de
outros pontos intermediários — e é exatamente aí que mora a recursão que a
versão anterior desta nota tinha perdido. Para dois pontos nas pontas opostas
de uma lua, $d(a,b)$ é grande, então $d_{\mathrm{mreach}}(a,b)$ também é
grande (o máximo nunca fica menor que $d(a,b)$) — **não existe aresta direta
entre eles**, mesmo que acabem no mesmo cluster.

## 3. Onde entra a recursão: componentes conexas de um grafo, não pares isolados

A resposta certa: monte um grafo com todos os pontos como nós, e uma aresta
entre $u,v$ sempre que $d_{\mathrm{mreach}}(u,v)\le\varepsilon$ (pela seção 2,
isso conecta exatamente os pares de núcleos próximos o bastante — um elo por
vez). Dois pontos $a,b$ pertencem ao **mesmo cluster** se, e somente se, eles
estão na **mesma componente conexa** desse grafo — ou seja, existe **algum**
caminho $a=x_0,x_1,\dots,x_n=b$ (passando por quantos pontos intermediários
forem necessários) onde cada par consecutivo satisfaz
$d_{\mathrm{mreach}}(x_i,x_{i+1})\le\varepsilon$.

Componente conexa de um grafo **é**, literalmente, o fecho transitivo da
relação de aresta — a mesma construção que o DBSCAN faz "na mão", ponto por
ponto, ao definir densidade-alcançável como cadeia de conexões diretas. Nada
mudou na lógica; só trocamos "vizinhos dentro de $\varepsilon$" (DBSCAN) por
"vizinhos com $d_{\mathrm{mreach}}\le\varepsilon$" (HDBSCAN) como regra de
aresta, e a etapa de "seguir a cadeia" é feita pela própria definição de
componente conexa, não precisa ser reafirmada à parte.

## 4. A ligação com o Bloco 5: caminho de gargalo (*minimax path*) e a MST

Existe uma forma equivalente, e mais útil computacionalmente, de dizer "$a$ e
$b$ estão na mesma componente conexa a um limiar $\varepsilon$": o **caminho
de gargalo** entre $a$ e $b$ — o menor valor possível, dentre todos os
caminhos que ligam $a$ a $b$, do **maior** peso de aresta ao longo do caminho
— é $\le\varepsilon$. ("Gargalo" porque o caminho só é tão bom quanto o pior
elo dele; você quer o caminho cujo pior elo é o menos ruim possível.)

Fato clássico de teoria dos grafos: esse caminho de gargalo entre $a$ e $b$ é
exatamente o caminho entre $a$ e $b$ dentro da **Árvore Geradora Mínima**
(MST) do grafo completo com pesos $d_{\mathrm{mreach}}$ — e o custo desse
caminho de gargalo é o maior peso de aresta ao longo desse trecho da árvore.
Não precisa testar todos os caminhos possíveis (exponenciais); a MST já
resolve o problema do caminho de gargalo entre **qualquer** par de pontos de
uma vez só.

É exatamente por isso que o Bloco 5 do `index.qmd` constrói a MST logo depois
de definir $d_{\mathrm{mreach}}$: a MST não é um passo à parte, é a ferramenta
computacional que implementa a recursão da seção 3 sem precisar simular
explicitamente cada cadeia de conexões. "Cortar a MST em todas as arestas com
peso $>\varepsilon$ e olhar os pedaços que sobraram" dá exatamente as mesmas
componentes conexas do grafo inteiro a esse $\varepsilon$ — e ligação simples
(*single linkage*), que o mesmo bloco introduz, é justamente essa lógica.

## 5. Como isso realmente vira o DBSCAN clássico

Juntando as seções 1–4: fixado um $\varepsilon$, as componentes conexas do
grafo com arestas $\{(u,v): d_{\mathrm{mreach}}(u,v)\le\varepsilon\}$ são
exatamente os clusters do DBSCAN$(\varepsilon,\ \text{minPts}=K+1)$ — na
variante chamada **DBSCAN\*** no artigo do HDBSCAN (Campello, Moulavi &
Sander, 2013), que só liga núcleo a núcleo (pontos que não são núcleo nunca
recebem aresta nenhuma nesse grafo, pela seção 2 — eles caem fora como ruído,
sem a etapa extra de "anexar ponto de borda ao cluster mais próximo" que o
DBSCAN original faz por cima disso).

A vantagem de passar por $d_{\mathrm{mreach}}$ + MST em vez de rodar o DBSCAN
do jeito tradicional (crescer região por região, para um $\varepsilon$ fixo
de cada vez) é que a MST já contém, numa estrutura só, o resultado do DBSCAN*
para **todo** valor de $\varepsilon$ simultaneamente — cortar a MST em
diferentes alturas dá diferentes $\varepsilon$, sem recalcular nada. É
literalmente a hierarquia que o Bloco 6 (árvore condensada + persistência)
explora, em vez de escolher um $\varepsilon$ só e aceitar a partição que sair.

## Resumo em uma frase

$d_{\mathrm{mreach}}(a,b)\le\varepsilon$ decide só se existe uma **aresta
direta** entre $a$ e $b$ (os dois são núcleos e estão perto); se $a$ e $b$
acabam no **mesmo cluster** é uma pergunta sobre **conectividade no grafo** —
existe uma cadeia de arestas diretas ligando os dois, possivelmente através de
muitos outros pontos — que é exatamente a mesma ideia recursiva do DBSCAN,
só que resolvida de uma vez para todo $\varepsilon$ através da MST.

## Apêndice: exemplo numérico verificado (com $K=2$, não degenerado)

Fiquei em dúvida se a equivalência da seção 2 não seria só um acidente de
$K=1$ (onde $\mathrm{core}_K$ vira só "distância ao vizinho mais próximo",
um caso especial fácil demais). Testei de novo com $K=2$ (`minPts=3`) — o
`max(\cdot,\cdot,\cdot)` já não é trivial nesse caso, porque com $K\ge2$ o
core distance de um ponto pode ser maior *ou* menor que a distância bruta
até um vizinho específico, dependendo de quantos outros pontos há por perto.

**Setup:** 9 pontos — grupo $A$ = quadrado $2\times2$ na origem (pontos
$0$–$3$), grupo $B$ = o mesmo quadrado deslocado $10$ unidades (pontos
$4$–$7$), ponto $8$ isolado bem longe. $\varepsilon=1{,}6$, `minPts=3`
$\Rightarrow K=2$.

Cada ponto do grid tem $\mathrm{core}_2=1{,}0$ (os dois lados do quadrado que
tocam esse ponto estão a distância $1$). O ponto isolado tem
$\mathrm{core}_2\approx19{,}6$.

Repare que o máximo genuinamente muda de termo dominante conforme o par:

- $d_{\mathrm{mreach}}(0,1) = \max(1{,}0,\ 1{,}0,\ 1{,}0) = 1{,}0$ — os três
  empatados (vizinhos diretos do quadrado).
- $d_{\mathrm{mreach}}(1,2) = \max(1{,}0,\ 1{,}0,\ 1{,}414) = 1{,}414$ — aqui
  é a **distância bruta** que vence (a diagonal do quadrado), não o core
  distance. Isso não apareceria com $K=1$ de um jeito tão claro.
- $d_{\mathrm{mreach}}(0,8) = \max(1{,}0,\ 19{,}6,\ 20{,}6) = 20{,}6$ — aqui
  quem domina é a distância bruta de novo (já é enorme por si só), mas o
  core distance do ponto isolado também seria suficiente sozinho para
  estourar $\varepsilon$.

**Verificação:** pontos-núcleo do `sklearn.cluster.DBSCAN(eps=1.6,
min_samples=3)` = $\{0,\dots,7\}$ — idêntico ao teste
$\mathrm{core}_2(p)\le\varepsilon$. Labels do DBSCAN:
`[0,0,0,0,1,1,1,1,-1]`. Componentes do grafo $d_{\mathrm{mreach}}$ cortado em
$\varepsilon=1{,}6$: `[0,0,0,0,1,1,1,1,2]` — mesmo agrupamento dos
pontos-núcleo (o número do rótulo é arbitrário, o particionamento é
idêntico), ponto $8$ isolado nos dois. Confere: a equivalência não depende
de $K=1$, continua exata com $K=2$.
