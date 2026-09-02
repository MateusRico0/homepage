# Respostas das Pausas Ativas — Aula 3

> Arquivo de apoio, não publicado (prefixo `_`). Discute as 8 perguntas
> motivadoras das pausas ativas do `index.qmd` e dá a solução dos
> respectivos V/F. O `index.qmd` publicado só contém a pergunta em cada
> pausa ativa, nunca a resolução.
>
> (Os 12 blocos de V/F da seção Exercícios do `index.qmd` **não** são
> discutidos aqui — ficam para o aluno resolver por conta, com
> justificativa disponível só ao professor em `_02-solucoes.md`.)

## Densidade x grupo: a paisagem já resolve o problema sozinha?

Não: um limiar fixo $\lambda$ sobre $p(\mathbf{x})$ diz quais pontos
estão "acima" da linha, mas não diz, por si só, quais desses pontos
formam a mesma componente conectada — isso exige um passo algorítmico
a mais (determinar conectividade), que é exatamente o que o resto da
aula constrói (conjuntos de nível, grafo de alcançabilidade mútua,
MST, árvore condensada). Ordenar os pacientes por densidade estimada e
cortar a lista ao meio também não basta, pelo mesmo motivo: densidade
alta não garante coerência espacial — nada impede que os pontos mais
densos estejam espalhados em duas concentrações bem separadas, não uma
massa única. Por outro lado, se a paisagem inteira fosse uma única
crista sem nenhum vale separando regiões, não haveria estrutura de
cluster genuína a recuperar — qualquer partição imposta seria
arbitrária, já que não existe critério de densidade para justificá-la.
A lógica de "componente conectada de densidade alta" transfere para
qualquer domínio com concentrações bem separadas — por exemplo,
detecção de fraude com dois golpes distintos, cada um formando sua
própria concentração no espaço de atributos, mesmo sem nunca ter visto
o rótulo do tipo de golpe.

- ✗ Um limiar sozinho diz quais pontos estão "acima" — não diz quais desses pontos formam a mesma componente conectada.
- ✔ Sem vale nenhum separando regiões, não há estrutura de cluster genuína — qualquer corte imposto seria arbitrário.
- ✗ Ordenar por densidade e cortar ao meio ignora conectividade espacial.
- ✔ A lógica de componente conectada de alta densidade transfere para qualquer domínio com concentrações bem separadas.

## Vale raso entre duas montanhas

A resposta depende inteiramente de onde $\lambda$ corta — e é exatamente
essa dependência que faz "cluster" virar uma hierarquia indexada por
$\lambda$, não uma resposta fixa e única. Se o vale nunca é totalmente
seco (densidade sempre estritamente positiva ao longo do caminho),
então, para $\lambda$ baixo o bastante, sempre existe um caminho "alto o
bastante" ligando as duas montanhas — nesse limiar, contam como um
cluster só. Já se o vale chega a ter densidade exatamente zero em algum
ponto, nenhum $\lambda>0$ jamais conecta as duas montanhas por cima
desse ponto: é uma barreira genuína, não uma questão de escolha de
limiar. E um vale raso não é, por si só, evidência de que a divisão é
"sempre um artefato" — pode ser estrutura real (duas subpopulações
genuinamente distintas, ainda que próximas).

- ✔ Vale nunca seco → para $\lambda$ baixo o bastante, existe caminho alto conectando — um cluster só nesse limiar.
- ✗ A resposta tem resposta fixa, independente de $\lambda$ — é exatamente por isso que "cluster" vira uma hierarquia indexada por $\lambda$.
- ✔ Vale com densidade exatamente zero em algum ponto: nenhum $\lambda>0$ conecta por cima desse ponto — barreira genuína.
- ✗ Vale raso não é evidência de "sempre um artefato" — pode ser estrutura real (duas subpopulações genuinamente distintas).

## O limite $\lambda \to \infty$

No limite $\lambda\to\infty$, $L_\lambda$ tende ao conjunto vazio, em
geral — nenhuma densidade real é infinita, então nenhum ponto sobrevive
ao limiar. O número de componentes conexas de $L_\lambda$ é uma função
não-crescente de $\lambda$: conforme $\lambda$ sobe, componentes só
podem se dividir ou desaparecer, nunca se fundir — e no limite tudo vai
a zero. Se as modas (picos) da densidade têm alturas suficientemente
diferentes entre si, existe sim um $\lambda$ finito que isola cada moda
como sua própria componente, escolhido logo abaixo do menor pico
relevante. E mesmo com $p(\mathbf{x})>0$ em todo o espaço, $L_\lambda$
para $\lambda$ pequeno-positivo pode ainda ter várias componentes —
"positivo" não é "uniformemente alto"; pode haver vales rasos acima de
zero mas abaixo de $\lambda$.

- ✔ $\lambda\to\infty$: $L_\lambda\to\emptyset$, em geral (nenhuma densidade real é infinita).
- ✔ Número de componentes é não-crescente em $\lambda$ — só funde subindo, nunca divide.
- ✔ Existe $\lambda$ que isola cada moda, se as alturas forem bem diferentes e o limiar for escolhido com cuidado.
- ✔ Mesmo com $p>0$ em todo lugar, $L_\lambda$ pequeno-positivo pode ter várias componentes.

## O caso extremo $\mathrm{core}_K=0$

Com os dois núcleos em zero, $d_{\mathrm{mreach}}(a,b)=d(a,b)$ — a
distância bruta decide sozinha, porque nenhum dos dois termos de núcleo
compete com ela no máximo. Não basta, porém, que só um dos dois seja
zero: o outro ainda entra no $\max$, então a distância bruta só domina
sozinha se ambos os núcleos forem zero (ou menores que $d(a,b)$). No
caso mais extremo, com os três termos em zero (inclusive $d(a,b)=0$,
os próprios pontos coincidindo), o máximo é trivialmente zero. E esse
caso não é "impossível na prática": dados reais com valores repetidos
ou arredondados (medições discretizadas, por exemplo) produzem *core
distance* zero com frequência — o caso precisa ser tratado na
implementação, não descartado como irrelevante.

- ✔ Com os dois núcleos em zero, $d_{\mathrm{mreach}}(a,b)=d(a,b)$ — a distância bruta decide.
- ✗ Não basta um dos dois ser zero — o outro ainda entra no $\max$; só se ambos forem zero a bruta domina sozinha.
- ✔ Com os três termos em zero, o máximo é zero.
- ✗ Dados reais com valores repetidos/arredondados produzem core distance zero com frequência — o caso precisa ser tratado.

## Um ponto de ruído no vale

Um único ponto bem posicionado no meio do vale cria uma aresta curta
ligando os dois clusters através dele, fazendo a ligação simples
fundi-los num nível de dissimilaridade bem mais baixo do que fundiria
sem esse ponto — a MST é sensível a arestas individuais, não a uma
média global de pesos, então inserir um único vértice pode mudar
radicalmente a topologia local da árvore. Isso é exatamente o
*chaining* citado do ESL: um defeito explícito do método de ligação
simples. A alcançabilidade mútua reduz esse problema (o *core distance*
do ponto de ruído tende a ser grande, penalizando a aresta), mas não o
elimina em toda circunstância — daí a necessidade adicional de
`min_cluster_size`/persistência no Bloco 6, que ataca o problema de
frente, exigindo que um cluster "sobreviva" por um tamanho mínimo, não
só por uma cadeia fina de pontos.

- ✔ Um único ponto bem posicionado cria uma aresta curta ligando os dois clusters — funde-os num nível bem mais baixo.
- ✗ A MST é sensível a arestas individuais — inserir um vértice pode mudar radicalmente a topologia local, não só uma média global.
- ✔ Isso é exatamente o *chaining* citado do ESL.
- ✗ $d_{\mathrm{mreach}}$ reduz o problema, mas não elimina encadeamento em toda circunstância — daí a necessidade adicional de `min_cluster_size`.

## Reduzindo `min_cluster_size` para 2

Ramos pequenos da árvore condensada, antes descartados como "perda" do
cluster-pai, passam a valer como clusters próprios quando
`min_cluster_size` cai para 2 — então a fração de ruído tende a cair.
Mas isso reintroduz uma versão do encadeamento da ligação simples pura:
uma cadeia fina de 2-3 pontos já basta para ser aceita como cluster
próprio. `min_cluster_size` afeta, sim, a fração de ruído — não só a
contagem de clusters distintos. E escolher `min_cluster_size` continua
sendo, mesmo no HDBSCAN, uma decisão de escala imposta pelo usuário: a
persistência decide *quais* ramos sobrevivem dado a árvore condensada,
mas não decide, por si só, o tamanho mínimo que conta como ramo. O
HDBSCAN troca "escolher $\lambda$" por "escolher `min_cluster_size`" —
não elimina a decisão de escala, só a move para um parâmetro mais
estável e mais fácil de interpretar (Bloco 7).

- ✔ Ramos pequenos, antes descartados, passam a valer como clusters — ruído tende a cair.
- ✔ Reintroduz uma versão do encadeamento — cadeias finas voltam a contar como cluster.
- ✗ Afeta, sim, a fração de ruído — não só a contagem de clusters.
- ✔ `min_cluster_size` continua sendo escolha de escala do usuário — persistência decide quais ramos sobrevivem, não o tamanho mínimo de ramo.

## "Resolver" a maldição aumentando `min_cluster_size`

Aumentar `min_cluster_size` até encontrar algum cluster de novo em 30
dimensões ataca o sintoma (nenhum cluster aparecia), não a causa
(distâncias em 30D perderam poder discriminativo) — a maldição não tem
solução mágica dentro do próprio algoritmo. Um cluster que só aparece
forçando esse parâmetro bem alto não é, por esse único motivo,
necessariamente tão confiável estatisticamente quanto o cluster puro de
54 pacientes encontrado com 2 atributos no Bloco 6 — pode ser um
artefato do limiar, não estrutura real. A solução mais direta,
sugerida já na Aula 2 e reaproveitável aqui, é reduzir a
dimensionalidade antes de rodar o HDBSCAN, não só ajustar
`min_cluster_size`. E o problema não é exclusivo de métodos baseados em
densidade como o HDBSCAN: qualquer método de clustering baseado em
distância entre pontos sofre sua própria versão da maldição —
distâncias em geral (não só as baseadas em densidade) perdem
significado geométrico relativo em alta dimensão — nenhum método
baseado em distância escapa por completo.

- ✔ Ataca o sintoma, não a causa — distâncias continuam sem poder discriminativo.
- ✗ Um cluster que só aparece forçando `min_cluster_size` alto não é automaticamente tão confiável quanto o cluster puro do Bloco 6.
- ✔ Reduzir dimensionalidade primeiro é a rota mais direta — a mesma lição da Aula 2.
- ✗ Nenhum método baseado em distância escapa por completo — o problema não é exclusivo de métodos baseados em densidade.

## Partição rígida ou probabilística?

Se os dois subtipos verdadeiramente se sobrepõem numa faixa contínua de
biomarcadores, sem um vale de densidade genuíno entre eles, uma
atribuição probabilística tende a refletir melhor essa ambiguidade do
que forçar cada paciente a um rótulo único. A força de pertencimento
que o HDBSCAN já calcula é interna ao cluster ao qual o ponto foi
atribuído — não é o mesmo que distribuir probabilidade entre *todos*
os clusters, como o GMM/EM faz; os dois não são equivalentes. No
limite em que os dois subtipos verdadeiros são separados por um vale de
densidade exatamente zero, a atribuição probabilística do GMM/EM
converge para probabilidades próximas de $0$ ou $1$ — coincidindo, na
prática, com a atribuição rígida do HDBSCAN nesse caso limite. Fora
desse limite, a escolha entre partição rígida e probabilística não é
só uma questão de conveniência computacional: reflete uma hipótese
diferente sobre a estrutura real dos dados, e os métodos só coincidem
no caso limite do vale genuíno. A escolha depende de crer (ou não) que
existe um vale de densidade genuíno separando os subtipos — exatamente
a pergunta que a Aula 4 equipa o aluno para responder com uma
ferramenta nova.

- ✔ Sobreposição contínua e genuína → probabilística reflete melhor a ambiguidade real.
- ✗ A força de pertencimento do HDBSCAN é interna ao cluster atribuído — não é o mesmo que distribuir probabilidade entre todos os clusters.
- ✔ Vale de densidade zero → GMM/EM converge para probabilidades extremas, coincidindo com HDBSCAN nesse limite.
- ✗ Não é só conveniência — reflete uma hipótese diferente sobre a estrutura dos dados; os métodos coincidem só no caso limite acima.
