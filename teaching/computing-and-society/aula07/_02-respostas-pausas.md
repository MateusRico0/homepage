# Respostas das Pausas Ativas — Aula 7

> Arquivo não publicado (`_02-respostas-pausas.md`) — nunca deve ser
> incluído no `index.qmd`. As notas em HTML publicadas contêm só a
> pergunta provocadora e o V/F sem resolução; os slides RevealJS
> mostram o V/F resolvido (✔/✗), mas sem a discussão longa abaixo.

---

## Pausa 1 (Bloco 1 — Revisão e Introdução): Ninguém Programou Para Discriminar — E Agora?

**Discussão da pergunta provocadora:** o ponto da pergunta é forçar o
aluno a sair do nível "o modelo é enviesado" (constatação) para o nível
"como eu mediria isso antes do lançamento" (procedimento). A resposta
exige duas decisões, não uma: (i) **qual medida do resultado da decisão**
comparar (não a acurácia geral, que pode esconder erro concentrado — o
próprio exemplo da Aula 6, 99% de acurácia geral com 100% de erro num
grupo minoritário), e (ii) **entre quais grupos**, definidos por um
atributo sensível. Nenhuma das duas escolhas é neutra: a primeira já
antecipa o Bloco 4 (existem várias métricas possíveis, cada uma captura
algo diferente); a segunda antecipa o Bloco 3 (o atributo sensível $Z$).
A pergunta também prepara o terreno para desmontar duas armadilhas
comuns de raciocínio: tratar uma única diferença encontrada como prova
suficiente e definitiva de injustiça (ignorando que "injusto segundo
qual métrica" já é uma escolha), e tratar uma auditoria única, feita
antes do lançamento, como suficiente para sempre (ignorando o Bloco 6,
sobre fairness de longo prazo).

- ✗ Falso — acurácia geral pode esconder um erro concentrado num grupo
  (o caso da Aula 6: 99% de acurácia geral, 100% de erro num grupo
  minoritário).
- ✔ Verdadeiro — é exatamente o que o resto da aula formaliza: comparar
  uma medida do *resultado* da decisão entre grupos definidos por um
  atributo sensível.
- ✗ Falso — o Bloco 4 mostra que existem várias métricas de injustiça,
  cada uma capturando uma noção diferente; uma diferença pode violar
  uma métrica e não outra, e a escolha de qual métrica importa é, ela
  mesma, uma decisão ética.
- ✗ Falso — o Bloco 6 mostra que fairness estática, medida uma vez, não
  é suficiente: decisões de hoje mudam o dado de amanhã.

---

## Pausa 2 (Bloco 3 — O Dado Sensível $Z$): Por Que Tirar a Coluna Não Basta?

**Discussão da pergunta provocadora:** o cenário é deliberadamente
realista (uma fintech, gênero, aprovação de crédito) para que o aluno
projete o mecanismo abstrato de proxy — já visto na Aula 6 com CEP e
histórico de saúde — sobre um caso novo, sem que a aula precise
reexplicar o conceito de proxy do zero. O ponto mais sutil do item 3 (o
"cerco" de remover proxies individuais um a um) é mostrar que
**correlação individual fraca não implica ausência de padrão conjunto**:
um conjunto de variáveis, cada uma fracamente correlacionada com $Z$
sozinha, pode ainda assim permitir que o modelo reconstrua $Z$ a partir
da combinação delas. Isso é uma generalização direta da "falha da
cegueira de atributo" apresentada na aula, e vale a pena verbalizar em
sala: não existe uma lista finita de colunas "proibidas" que, uma vez
removida, resolve o problema — o problema é estrutural, não uma lista de
exceções.

- ✗ Falso — é exatamente o mecanismo descrito na aula: proxies
  reconstroem a informação removida, sem erro de cálculo nenhum
  envolvido.
- ✔ Verdadeiro — esse é o mecanismo da falha de "justiça pela
  ignorância": informação sensível sobrevive, espalhada, em variáveis
  correlacionadas.
- ✗ Falso — remover proxies individuais não garante a remoção de
  padrões que emergem de **combinações** de variáveis, cada uma
  fracamente correlacionada com $Z$ sozinha, mas conjuntamente
  informativas.
- ✔ Verdadeiro — mesmo mecanismo de proxy: a instituição de ensino
  carrega, de forma correlacionada, informação sobre origem
  socioeconômica e, indiretamente, sobre atributos sensíveis
  distribuídos de forma desigual entre instituições.

---

## Pausa 3 (Bloco 4 — Definindo (In)Justiça com Probabilidade): Duas Métricas, Dois Resultados Diferentes

**Discussão da pergunta provocadora:** o cenário de admissão
universitária foi escolhido porque tem uma assimetria realista e
documentada (acesso desigual a preparação prévia) que faz $Y=1$ (estar
"de fato qualificado" segundo o critério da prova) ter taxas diferentes
entre os grupos de partida — a condição exata sob a qual o Teorema da
Impossibilidade morde. O item mais importante para discutir em sala é o
terceiro: ele força o aluno a fazer a conta mentalmente (se a taxa de
qualificados no grupo A é menor, igualar a taxa de aprovação **total**
exige aprovar uma fração maior de não qualificados de A do que de B) —
é a crítica formal à Paridade Demográfica, escrita como consequência
lógica, não como afirmação solta. O quarto item existe para reforçar,
por contraste, que Igualdade de Oportunidade tem seu próprio ponto cego
(não controla o tratamento dos não qualificados) — as duas críticas do
Bloco 4, uma de cada vez, aplicadas ao mesmo cenário.

- ✔ Verdadeiro — (i) iguala taxas de aprovação totais (Paridade
  Demográfica); (ii) iguala a chance de aprovação só entre qualificados
  (Igualdade de Oportunidade).
- ✗ Falso — são equivalentes só no caso particular em que a fração de
  qualificados já é igual entre os grupos; quando as taxas de
  qualificação real diferem (como no enunciado), as duas opções
  produzem resultados diferentes.
- ✔ Verdadeiro — é exatamente a crítica formal à Paridade Demográfica:
  para igualar a taxa total quando a qualificação real difere, o
  sistema precisa compensar aprovando não qualificados do grupo com
  menos qualificados.
- ✗ Falso — Igualdade de Oportunidade só controla o tratamento de quem
  **é** qualificado; não impõe nada sobre a taxa de falso positivo
  entre não qualificados de cada grupo, que pode continuar desigual.

---

## Pausa 4 (Bloco 6 — Fairness de Longo Prazo): O Que a Auditoria Não Está Vendo

**Discussão da pergunta provocadora:** o cenário reproduz, em miniatura,
o problema central do bloco — uma auditoria que parece rigorosa
(comparar taxas de inadimplência entre grupos) mas que, por construção,
só enxerga quem já recebeu uma decisão positiva. O item mais produtivo
para discussão em sala é o terceiro: ele pede que o aluno **inverta o
lugar onde procura discriminação** — não na taxa de pagamento de quem
foi aprovado, mas na própria taxa de aprovação/recusa, que pode ser o
ponto onde a disparidade real está concentrada. Vale conectar
explicitamente de volta ao caso do algoritmo de saúde da Abertura: lá, a
"aprovação" era receber acompanhamento clínico extra, e o proxy (custo
histórico) já continha o viés antes mesmo de qualquer resultado de
saúde futuro ser observado.

- ✗ Falso — a auditoria compara só quem recebeu crédito; nada garante
  que a decisão de conceder ou recusar, em si, seja igualmente justa
  entre os grupos.
- ✔ Verdadeiro — é exatamente o problema dos rótulos seletivos: o
  rótulo (pagou/não pagou) só existe para quem foi aprovado.
- ✔ Verdadeiro — a disparidade pode estar concentrada na própria
  decisão de aprovação/recusa, um ponto que a auditoria proposta não
  consegue enxergar.
- ✗ Falso — mais amostra de aprovados não resolve, porque o viés está
  em *quem nunca entra* na amostra (os recusados), não no tamanho da
  amostra dos aprovados.

---

## Pausa 5 (Bloco 7 — Viés em Imagem e Linguagem): O Padrão Que Ninguém Programou

**Discussão da pergunta provocadora:** o cenário generaliza
deliberadamente o exemplo de "brancura como padrão" (dado na aula para
raça em legendagem de imagens) para um recorte étnico diferente, sem
nomear qual — o objetivo é testar se o aluno reconhece a **estrutura**
do fenômeno (padrão não marcado vs. desvio marcado), não se decorou o
exemplo específico da aula. O quarto item é o mais importante
pedagogicamente: ele tenta induzir o aluno a tratar "viés em modelo de
imagem" como uma categoria separada de "fairness algorítmica" (que ele
pode ter associado só a decisões tabulares dos Blocos 3–6) — a resposta
correta reforça que a definição de fairness da aula (tratamento
condicionado a um atributo sensível $Z$) não depende da modalidade do
dado.

- ✗ Falso — nenhum dos exemplos da aula (cirurgiã/babá, brancura como
  padrão) exigiu decisão explícita de um engenheiro; o padrão emerge do
  dado de treino via máxima verossimilhança.
- ✔ Verdadeiro — mesmo mecanismo: o modelo captura, sem instrução
  direta, a correlação estatística presente no dado.
- ✔ Verdadeiro — "padrão sem menção" vs. "desvio com menção explícita"
  é a mesma estrutura, generalizável a qualquer grupo definido por um
  atributo sensível.
- ✗ Falso — a aula define fairness em termos de tratamento desigual
  condicionado a um atributo sensível $Z$; isso vale tanto para
  decisões tabulares (Blocos 3–6) quanto para saídas de modelos
  generativos de imagem/linguagem (este bloco) — a modalidade do dado
  não muda a definição.
