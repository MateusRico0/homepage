# Respostas das Pausas Ativas — Aula 3

> Arquivo não publicado (`_03-respostas-pausas.md`) — nunca deve ser
> incluído no `index.qmd`. As notas em HTML publicadas contêm só a
> pergunta provocadora e o V/F sem resolução; os slides RevealJS
> mostram o V/F resolvido (✔/✗), mas sem a discussão longa abaixo.

---

## Pausa 1 (Bloco 1 — Abertura, caso BART): Um argumento correto, mas sem poder de se fazer valer

**Discussão da pergunta provocadora:** O desfecho do caso BART separa
duas coisas que é fácil confundir: um código estar "certo" — ter um
argumento coerente sobre o que deveria acontecer — e um código ter
força real — existir alguém ou algo com poder de fazer esse argumento
prevalecer. O IEEE tinha o argumento certo (o código profissional é
parte implícita do contrato; segui-lo não deveria ser motivo de
demissão), mas não tinha nenhum mecanismo institucional capaz de
impor essa leitura ao empregador ou ao tribunal — só uma carta *amicus
curiae*, que é persuasão, não coerção. Isso é exatamente a lacuna que
os Blocos 3 e 4 vão nomear: falta um conselho de profissão, com poder
legal de registro/fiscalização, por trás do código do IEEE.

**V/F — resolução:**

- ✔ Se o tribunal tivesse aceitado integralmente o argumento do IEEE,
  agir de acordo com o código profissional passaria a valer como
  cumprimento de uma obrigação contratual — tornando a demissão, em
  princípio, contestável como quebra de contrato, não como
  insubordinação. **Verdadeiro** — é a lógica do próprio argumento do
  IEEE: se o código é parte do contrato, cumpri-lo é cumprir o
  contrato.
- ✗ Como os engenheiros aceitaram um acordo extrajudicial de
  indenização, isso significa que a Justiça reconheceu formalmente que
  a demissão foi ilegal e que a tese do IEEE prevaleceu como parte do
  contrato de trabalho. **Falso** — um acordo extrajudicial evita
  justamente uma decisão formal do tribunal sobre o mérito; aceitar
  indenização não é vitória jurídica da tese do IEEE, só encerra o
  litígio sem decidi-lo.
- ✔ Uma enfermeira que, depois de ser ignorada nos canais internos do
  hospital, leva ao conselho de administração uma preocupação de
  segurança do paciente, e é demitida em seguida, ocupa posição
  estruturalmente análoga à dos engenheiros do BART — mesmo numa
  profissão e época diferentes. **Verdadeiro** — mesma estrutura
  institucional (alertar → ser ignorado → escalar → ser demitido),
  transposta para outro domínio; a profissão e a época mudam, o
  mecanismo não.
- ✗ Se os engenheiros do BART nunca tivessem contornado a hierarquia e
  apenas repetido os mesmos memos internos indefinidamente, sem
  acionar o conselho ou a imprensa, a falha de segurança que causou o
  acidente de outubro de 1972 teria deixado de existir. **Falso** — a
  falha técnica existia independentemente de como os engenheiros
  escolheram agir; contornar (ou não) a hierarquia decidiu se eles
  foram demitidos, não se o sistema tinha ou não um problema real de
  segurança.

---

## Pausa 2 (Bloco 2, meio — Código da ACM): Um código com muitas cláusulas: elas sempre convergem?

**Discussão da pergunta provocadora:** Não, as cláusulas de um mesmo
código não são garantidamente coerentes entre si na prática. O código
da ACM foi desenhado para que as três partes se reforcem, mas nada
impede uma organização de cumprir a retórica de uma cláusula (1.1,
"contribuir para a sociedade") sem cumprir a prática de outra (2.5,
"avaliação abrangente de riscos") — é exatamente esse descompasso
entre discurso e prática que o Bloco 5 vai nomear como
*window-dressing*. A lição para quem lê um código: cláusulas
aspiracionais amplas (Parte 1) não substituem cláusulas operacionais
específicas (Parte 2) — e vice-versa.

**V/F — resolução:**

- ✗ Uma empresa que divulga publicamente um compromisso com o
  princípio 1.1 da ACM, mas nunca implementa nenhuma medida concreta
  de avaliação de risco exigida pelo princípio 2.5, está cumprindo o
  código da ACM, porque 1.1 e 2.5 pertencem a partes independentes do
  texto. **Falso** — as partes do código não são independentes nem
  substituíveis; cumprir a retórica de 1.1 sem a prática de 2.5 é
  exatamente o tipo de lacuna entre discurso e ação que o código, como
  um todo, pretende evitar.
- ✔ Se a Parte 3 do código (liderança profissional) não existisse, um
  profissional sem cargo de gestão ainda estaria integralmente
  coberto pelas Partes 1 e 2 nas decisões técnicas do seu próprio
  trabalho. **Verdadeiro** — a Parte 3 acrescenta obrigações
  específicas de quem lidera pessoas ou sistemas; não substitui nem
  restringe as Partes 1 e 2, que valem para qualquer profissional, com
  ou sem cargo de liderança.
- ✔ A lógica do princípio 3.7 da ACM se aplicaria, por analogia, a um
  provedor de nuvem que hospeda a maior parte dos aplicativos
  bancários de um país, mesmo esse provedor nunca sendo mencionado
  como exemplo no texto do código. **Verdadeiro** — o critério do
  princípio é o grau de integração à infraestrutura social, não uma
  lista fechada de exemplos; um provedor de nuvem crítico se encaixa
  no mesmo critério que um sistema de pagamento nacional.
- ✗ Como o código da ACM é organizado em três partes numeradas, isso
  significa que, em qualquer conflito entre cláusulas de partes
  diferentes, a parte de número mais baixo (Parte 1) sempre tem
  precedência automática sobre as demais. **Falso** — o código não
  estabelece essa hierarquia numérica entre partes; a numeração é
  organizacional, não uma ordem de precedência em caso de conflito.

---

## Pausa 3 (Bloco 2, fim — taxonomia): Consultivo, mas não disciplinar: o que isso muda na prática?

**Discussão da pergunta provocadora:** Muito pouco, no sentido de
consequência institucional imediata. Um profissional que viola
abertamente uma cláusula da ACM, do IEEE-CS/ACM, da NSPE ou da FEANI
pode sofrer desaprovação moral dentro da comunidade profissional, mas
nenhuma dessas quatro entidades tem, por si só, poder legal de impedir
esse profissional de continuar trabalhando — porque nenhuma delas é um
conselho de profissão com poder de registro e fiscalização. É
precisamente essa ausência que motiva o Bloco 3: o que, de fato,
transformaria "consultivo" em "disciplinar" com dentes reais?

**V/F — resolução:**

- ✔ Um engenheiro de software que viola abertamente o princípio PUBLIC
  do código IEEE-CS/ACM, mas nunca causou dano concreto a ninguém,
  ainda pode continuar exercendo a profissão livremente, porque
  nenhuma das quatro entidades tem poder de revogar seu direito de
  trabalhar. **Verdadeiro** — sem conselho por trás, nenhuma das
  quatro entidades tem poder legal de impedir o exercício da
  profissão; a única consequência é reputacional/moral dentro da
  comunidade.
- ✗ Se a ACM decidisse, unilateralmente, expulsar um sócio por violar
  o código, essa expulsão teria, por si só, o mesmo efeito prático
  sobre a carreira dele que uma cassação de registro pelo CREA tem
  sobre um engenheiro civil. **Falso** — filiação voluntária à ACM não
  é pré-condição legal para exercer a profissão em lugar nenhum;
  perdê-la não equivale a perder um registro que a lei exige para
  trabalhar, como o do CREA.
- ✔ A mesma lógica "consultivo, não disciplinar" se aplicaria a um
  código de ética interno de uma ONG sem qualquer vínculo com órgão
  fiscalizador externo. **Verdadeiro** — é a mesma estrutura fora da
  engenharia: um código sem fiscalização externa orienta decisões, mas
  não expulsa ninguém do mercado de trabalho por violá-lo.
- ✗ Como o texto afirma que "a maioria dos códigos profissionais de
  engenharia é consultiva", isso implica que nenhum código de
  engenharia, em nenhum país, jamais teve algum componente
  disciplinar. **Falso** — "a maioria" não é "todos"; o próprio
  contraste feito no Bloco 3 é com códigos corporativos, descritos
  como mais frequentemente disciplinares — a fonte não afirma uma
  ausência universal.

---

## Pausa 4 (Bloco 3, fim — conselho e LGPD): Dois mecanismos de força legal: quando um supre a ausência do outro?

**Discussão da pergunta provocadora:** A parcialidade importa
exatamente onde o mecanismo existente (LGPD) não alcança. A LGPD
regula o tratamento de dados pessoais — não regula quem pode se
chamar "profissional de Computação", nem exige nenhuma competência
técnica mínima fora do contexto de dados pessoais. Um profissional
cujo trabalho nunca toca dado pessoal (ex.: simulação numérica pura)
está, hoje, fora do alcance de qualquer um dos dois mecanismos
discutidos — não porque a LGPD "não seja suficientemente forte", mas
porque ela regula outra coisa. É esse tipo de lacuna estrutural,
específica, que a pergunta pede para localizar.

**V/F — resolução:**

- ✔ Um profissional de computação que constrói exclusivamente sistemas
  internos de simulação numérica, sem qualquer dado pessoal envolvido,
  está, hoje, totalmente fora do alcance de qualquer regulação
  judicializada discutida neste bloco. **Verdadeiro** — sem dado
  pessoal envolvido, a LGPD simplesmente não se aplica, e não existe
  conselho de profissão para preencher essa lacuna.
- ✔ No limite em que uma organização deixasse de tratar qualquer dado
  pessoal, ela deixaria de estar sujeita aos princípios do Art. 6º da
  LGPD sobre esse tratamento específico, mesmo continuando sujeita a
  outras leis gerais. **Verdadeiro** — os princípios do Art. 6º são
  princípios sobre tratamento de dados pessoais; sem dado pessoal
  identificável, o objeto de regulação desses princípios
  especificamente deixa de existir.
- ✔ A mesma lógica de "regular o comportamento, e não a identidade de
  quem o exerce" que caracteriza a LGPD também descreve como leis de
  defesa do consumidor regulam a relação entre qualquer empresa e seus
  clientes, independentemente de existir ou não um conselho
  profissional de vendedores. **Verdadeiro** — é a mesma lógica de
  regulação por comportamento/atividade, transposta para outro
  domínio, independente de licenciamento profissional de quem vende.
- ✗ Como o Brasil tem uma lei geral de proteção de dados desde 2018,
  isso resolve, na prática, a mesma lacuna que a ausência de um
  conselho de profissão deixa em aberto. **Falso** — os dois
  mecanismos regulam coisas diferentes (quem exerce vs. como os dados
  são tratados); a LGPD não substitui o que um conselho faria sobre,
  por exemplo, competência técnica mínima para exercer a profissão
  fora do contexto de dados pessoais.

---

## Pausa 5 (Bloco 4, meio — regulamentar a Informática no Brasil): O que cada argumento resolve, e o que não resolve?

**Discussão da pergunta provocadora:** Cada desvantagem listada pelo
livro é um argumento contra uma consequência específica da
regulamentação, não contra a regulamentação como um todo. "Aumento de
custo" é um argumento sobre anuidades, não sobre a existência de um
conselho em si — some o custo, e o argumento perde a base. "Redução da
multidisciplinaridade" é um argumento histórico sobre como a área se
formou. "Não resolve precarização" reconhece que um conselho e um
sindicato cobrem funções diferentes — nenhum dos dois substitui o
outro. Ler as desvantagens como "logo, não regulamentar" ignora que
elas são, na verdade, um mapa de trade-offs distributivos: quem paga o
quê, e quem ganha o quê, com cada escolha.

**V/F — resolução:**

- ✗ Se a Informática brasileira tivesse sido regulamentada já nos anos
  1970, isso teria impedido, sozinho, o crescimento posterior da área
  para mais de mil cursos de graduação em 2016. **Falso** —
  regulamentação da profissão e expansão de cursos de graduação são
  mecanismos independentes; nada na fonte liga regulamentar o
  exercício profissional a limitar a oferta de cursos.
- ✔ No limite em que um conselho de Informática cobrasse a mesma
  anuidade que hoje é cobrada por profissionais autônomos sem
  filiação nenhuma (custo adicional zero), a crítica de "aumento de
  custo" listada pelo livro deixaria de se aplicar a esse conselho
  hipotético. **Verdadeiro** — a crítica é especificamente sobre
  custo; sem custo adicional, ela deixa de valer para esse cenário
  hipotético (mesmo que outras críticas continuem valendo).
- ✔ A crítica de que "conselhos não têm meios para evitar a
  precarização do trabalho, papel que cabe aos sindicatos" se
  aplicaria igualmente a um cenário em que a Informática fosse
  regulamentada, mas os profissionais não tivessem nenhum sindicato
  atuante no setor. **Verdadeiro** — é a extensão lógica da mesma
  divisão de papéis "conselho ≠ sindicato" para um cenário em que
  nenhuma das duas estruturas cobriria essa função.
- ✗ Como o livro reconhece "vantagens e desvantagens" da
  regulamentação sem tomar partido explícito, a decisão de
  regulamentar ou não é, do ponto de vista do próprio livro, uma
  questão puramente técnica, sem dimensão de valores ou de quem ganha
  e quem perde. **Falso** — as vantagens/desvantagens listadas são,
  precisamente, sobre quem ganha e quem perde com a escolha (custo
  para profissionais, qualidade para a sociedade, flexibilidade de
  mercado) — uma questão distributiva, não neutra.

---

## Pausa 6 (Bloco 4, fim — comparação internacional): Três países, três desfechos: o que muda a "força" de uma proteção de título?

**Discussão da pergunta provocadora:** A força de uma regra depende de
haver ou não sanção legal por não segui-la — não de quantas pessoas
escolhem segui-la voluntariamente. O exame da NCEES morreu porque
dependia de adesão voluntária: sem exigência legal, baixa demanda
bastou para descontinuá-lo. O título de "engineer" no Canadá é forte
justamente porque tem essa sanção legal por trás — e é por isso que a
exceção de Alberta em 2024 foi notável: uma província afrouxando uma
proteção que, ao contrário do exame americano, realmente tinha dentes.
O CITP britânico fica no meio: dá prestígio, mas sem consequência legal
para quem não o tem. Os três casos, lidos juntos, mostram que "força"
e "popularidade voluntária" são eixos diferentes.

**V/F — resolução:**

- ✔ Se o Reino Unido exigisse o CITP como licença obrigatória para
  atuar em TI, a distinção entre "regulamentação plena" e a "terceira
  via" deixaria de fazer sentido para esse país. **Verdadeiro** —
  tornar o CITP obrigatório colapsaria a "via intermediária" na
  categoria de regulamentação plena, eliminando a própria razão de
  chamá-lo de terceira via.
- ✔ No limite em que a APEGA decidisse proibir completamente o uso de
  "software engineer" mesmo fora de contextos de engenharia
  regulamentada, essa seria uma ampliação, não uma redução, do escopo
  da proteção de título. **Verdadeiro** — é o sentido oposto ao que
  Alberta fez em 2024 (abrir exceção); proibir mais amplamente é
  apertar a proteção, não afrouxá-la.
- ✔ A tensão entre "proteção de título forte, mas questionada na
  prática" que aparece no caso canadense se repetiria, em princípio,
  em qualquer profissão brasileira regulamentada se uma nova
  especialidade técnica surgisse rapidamente sem estar prevista na lei
  original. **Verdadeiro** — mesma tensão institucional (especialidade
  nova vs. lei antiga), transferida para qualquer profissão
  regulamentada no Brasil, não só computação/engenharia.
- ✗ Como o Reino Unido optou por um título voluntário em vez de
  regulamentação plena, e isso não impediu o desenvolvimento da
  indústria de software britânica, conclui-se que qualquer forma de
  regulamentação plena necessariamente atrapalharia uma indústria de
  tecnologia. **Falso** — um único caso não sustenta uma afirmação
  causal universal; a própria fonte só conclui que nenhum país
  resolveu essa questão de forma limpa, não que regulamentação plena
  seja, em geral, prejudicial.

---

## Pausa 7 (Bloco 5, fim — limites dos códigos): Se um código não pode ser "vivido" à risca, ele ainda vale alguma coisa?

**Discussão da pergunta provocadora:** Sim — os três limites
(autointeresse/*window-dressing*, vagueza/contradição, impossibilidade
de proteção real) mostram que nenhum código, isoladamente, garante um
resultado ético ou protege quem o segue. Mas isso é diferente de dizer
que o código não serve para nada. Um código continua funcionando como
ponto de partida: nomeia valores, oferece uma primeira orientação, dá
linguagem comum para discutir um dilema. O que ele não faz — e nenhuma
das estruturas vistas até aqui (conselho, lei, código) faz por conta
própria — é substituir o julgamento moral ativo de quem enfrenta a
situação real. É exatamente por isso que a deliberação estruturada
(Ciclo Ético, Landon & Landon) continua indispensável mesmo onde
código, conselho e lei já existem.

**V/F — resolução:**

- ✗ Como os três limites mostram que nenhum código garante um
  resultado ético, a conclusão lógica é que um profissional que ignora
  completamente os códigos de conduta está na mesma posição moral de
  um que os usa como ponto de partida para o julgamento. **Falso** — a
  própria conclusão da aula é o oposto: usar o código como ponto de
  partida (mesmo sabendo de seus limites) não é equivalente a
  ignorá-lo por completo.
- ✗ No limite em que um código de conduta fosse escrito de forma
  perfeitamente precisa, sem nenhuma cláusula vaga e sem qualquer
  conflito entre cláusulas, a crítica de autointeresse/*window-
  dressing* deixaria de poder se aplicar a esse código. **Falso** —
  precisão textual e autointeresse são dimensões independentes; um
  código muito preciso ainda pode ser usado retoricamente ("olha como
  somos rigorosos") sem nenhuma fiscalização real por trás dele.
- ✔ A tensão entre "lealdade crítica" e "lealdade acrítica" se
  aplicaria, em princípio, a uma cientista de dados que decide entre
  seguir uma diretriz que julga equivocada e alertar sua liderança,
  mesmo sem cláusula de código escrita cobrindo essa situação
  específica. **Verdadeiro** — a distinção crítica/acrítica é uma
  ferramenta de raciocínio moral geral, não amarrada à existência de
  uma cláusula escrita específica.
- ✗ Como nenhum dos limites é suficiente para declarar os códigos
  indesejáveis, a crítica correta a fazer a um código real é sempre
  sobre defeitos de redação do próprio texto, nunca sobre a ausência
  de estrutura institucional por trás dele. **Falso** — o fio condutor
  dos Blocos 3 e 4 é justamente que a estrutura institucional (conselho,
  lei) por trás do código importa tanto quanto, ou mais que, a redação
  do texto em si.

---

## Pausa 8 (Bloco 6 — Fechamento, caso Snowden): Sem código específico, sem estrutura nenhuma?

**Discussão da pergunta provocadora:** Não — faltar um código
específico para uma situação não deixa essa situação sem nenhuma
estrutura de análise disponível. Dois recursos continuam de pé: (1)
princípios amplos de códigos existentes, como o ACM 1.1, cujo critério
de aplicação é o impacto social de uma ação de computação, não uma
lista fechada de casos previstos; e (2) processos de deliberação
independentes de qualquer código específico — o Ciclo Ético da Aula 2
e o processo de 5 passos de Landon & Landon, que estruturam fatos,
interessados, alternativas e consequências, sem depender de nenhuma
cláusula escrita cobrir exatamente o caso em questão. O caso Snowden
funciona como teste de estresse dessa ideia: mesmo no limite de "nenhum
código pensado para essa pessoa", a aula ainda tem ferramentas para
estruturar a pergunta.

**V/F — resolução:**

- ✔ O princípio ACM 1.1, originalmente pensado para decisões de
  produto de software, se estenderia, por analogia de escopo, ao caso
  de um prestador de serviços de infraestrutura de TI que decide expor
  um programa de vigilância em massa ao público. **Verdadeiro** — o
  critério do princípio é o grau de impacto social da ação em
  computação, não uma lista fechada de casos previstos no texto.
- ✔ No limite em que absolutamente nenhum princípio de nenhum código
  de conduta de computação mencionasse valores como privacidade ou
  interesse público, o processo de Landon & Landon (ou o Ciclo Ético)
  ainda teria uma forma de estruturar uma decisão sobre o caso Snowden.
  **Verdadeiro** — os dois processos estruturam fatos, interessados,
  alternativas e consequências independentemente de existir um código
  específico que cubra o caso.
- ✗ Como nenhum código profissional tradicional foi escrito pensando
  especificamente na posição de Snowden, a pergunta sobre se ele agiu
  eticamente não pode ser respondida com nenhum rigor, restando só
  opinião pessoal sem qualquer estrutura. **Falso** — ausência de
  código específico não é ausência de estrutura de deliberação; é
  exatamente o que o Ciclo Ético e o processo de Landon & Landon
  fornecem.
- ✗ Se Snowden fosse formalmente filiado a um conselho profissional
  disciplinar, isso teria, por si só, tornado a pergunta ética sobre
  sua ação irrelevante, substituída inteiramente por uma pergunta
  puramente disciplinar/legal. **Falso** — um conselho disciplinar
  decide consequências institucionais e legais; não substitui a
  pergunta ética sobre se a ação foi correta — mesma lição do Bloco 5:
  nenhuma estrutura institucional substitui o julgamento moral.
