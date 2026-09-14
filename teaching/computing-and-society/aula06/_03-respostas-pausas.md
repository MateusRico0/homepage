# Respostas das Pausas Ativas — Aula 6

> Arquivo não publicado (`_03-respostas-pausas.md`) — nunca deve ser
> incluído no `index.qmd`. As notas em HTML publicadas contêm só a
> pergunta provocadora e o V/F sem resolução; os slides RevealJS
> mostram o V/F resolvido (✔/✗), mas sem a discussão longa abaixo.

---

## Pausa 1 (Bloco 1 — Abertura): A Nuvem Tem Peso?

**Discussão da pergunta provocadora:** Hoje, o custo material da IA
(energia, água, minerais) é pago, majoritariamente, por quem hospeda
fisicamente a infraestrutura — muitas vezes um território distante de
quem usa o serviço final. Se esse custo fosse totalmente visível e
cobrado diretamente de quem se beneficia (por exemplo, um preço por
consulta que refletisse o custo real de água e energia gasto), o
incentivo econômico mudaria primeiro para reduzir o *uso* (menos
consultas, modelos mais eficientes) — mas, na prática atual, quem paga
o custo material não é, em geral, quem decide onde construir nem quem
usa o serviço. É exatamente essa desconexão entre quem decide, quem
usa e quem paga que os Blocos seguintes da aula desembrulham com um
caso real.

**V/F — resolução:**

- ✔ Se a infraestrutura de nuvem não dependesse de nenhum resfriamento
  físico de hardware, grande parte da pressão por água e energia
  discutida nesta aula deixaria de existir. **Verdadeiro** — sem a
  necessidade física de dissipar calor gerado pelo processamento, boa
  parte da pressão concreta por água e energia perderia sua causa
  material central.
- ✗ No limite em que a energia e a água usadas por um data center não
  competissem com nenhum outro uso local, a tensão discutida nesta aula
  deixaria de se aplicar a esse caso. **Falso** — mesmo nesse cenário
  ideal, a tensão nasceria de outros fatores do artigo (quem decide,
  quem é consultado, que território hospeda a infraestrutura), não só
  do custo de oportunidade de energia/água.
- ✔ A mesma lógica se aplicaria a um usuário de streaming que nunca
  pensa nos servidores físicos por trás de cada vídeo assistido.
  **Verdadeiro** — mesma estrutura de invisibilização da infraestrutura
  física por trás da interface de uso.
- ✗ Como a IA depende de energia, água e minerais, toda tecnologia
  digital produz o mesmo nível de impacto material que um data center
  de treinamento de IA em larga escala. **Falso** — a aula não afirma
  equivalência de escala entre todo tipo de tecnologia digital.

---

## Pausa 2 (Bloco 2 — Materialidade): O Preço Escondido do Resfriamento

**Discussão da pergunta provocadora:** Não. "Energia limpa" resolve
apenas o eixo energético da equação — de onde vem a eletricidade usada
pelos servidores. Mas a Tabela 14.1 de Maciel & Viterbo (2020) lista
diretivas separadas para consumo de água, consumo de material e
reciclabilidade do produto, além de energia; o resfriamento de
servidores em escala industrial é, tipicamente, um consumidor
intensivo de água, independentemente de a energia elétrica usada vir
de fonte limpa ou não. Um data center pode ser "100% energia limpa" e
ainda assim reter grande pressão hídrica sobre mananciais locais — é
exatamente esse ponto cego que a leitura de Maciel & Viterbo já
antecipava, antes mesmo de qualquer caso concreto ser discutido.

**V/F — resolução:**

- ✔ Se toda a energia usada por um data center viesse de fontes
  renováveis, mas o resfriamento ainda dependesse de grandes volumes
  de água de mananciais locais, a diretiva de "Consumo de Água" da
  Tabela 14.1 continuaria sendo violada. **Verdadeiro** — energia limpa
  resolve o eixo energético, não o eixo hídrico do resfriamento, que é
  uma dimensão distinta.
- ✔ No limite em que um hardware nunca precisasse ser substituído, a
  diretiva de "Reciclabilidade do Produto" perderia parte de sua
  urgência prática. **Verdadeiro** — sem geração de resíduo eletrônico,
  essa diretiva específica perde parte de sua urgência prática, mesmo
  continuando válida em princípio.
- ✔ A mesma lógica se aplicaria a uma mineradora de criptomoeda que usa
  só energia hidrelétrica, mas resfria seus servidores consumindo água
  de um rio local. **Verdadeiro** — mesma estrutura: energia limpa não
  elimina, sozinha, o consumo de outro recurso natural usado no
  resfriamento.
- ✗ Como a Tabela 14.1 lista "utilizar menos hardware" em quase toda
  diretiva, a única forma de tornar um data center sustentável é
  reduzir drasticamente sua capacidade de processamento. **Falso** — a
  tabela lista várias estratégias além de reduzir hardware (eficiência
  de software, escolha de fabricante, matérias-primas recicláveis).

---

## Pausa 3 (Bloco 3 — Caso Central): Quem Decidiu Isso, Exatamente?

**Discussão da pergunta provocadora:** O resultado (priorizar
resfriamento sobre direitos territoriais) emerge de uma sequência de
decisões de arquitetura — onde hospedar, quanta energia reservar,
quanta água usar para resfriamento — tomadas sem que a comunidade
afetada estivesse formalmente representada no processo de decisão.
Ninguém precisa escrever "vamos marginalizar a Tekoa Pekuruty" para que
esse resultado aconteça: basta que a comunidade nunca apareça como
interessado formal nas decisões sobre reserva de energia e uso do
território — o mesmo mecanismo de ausência de interessado (*stakeholder*
sem poder de decisão) já visto no mapa de atores da Aula 1 e no mapa de
papéis da Aula 4, agora operando em escala territorial.

**V/F — resolução:**

- ✔ Se a Scala AI City tivesse sido construída numa região sem
  histórico de instabilidade elétrica e sem comunidade indígena no
  entorno, o caso não teria as mesmas duas evidências concretas de
  custo territorial. **Verdadeiro** — os dois fatores de risco
  específicos citados pelo artigo são parte do que dá concretude
  empírica ao caso.
- ✔ No limite em que a reserva de energia fosse pequena o suficiente
  para não competir com o consumo elétrico local, um dos dois
  problemas centrais do caso deixaria de se aplicar. **Verdadeiro** —
  a pressão sobre a rede é consequência direta da magnitude da reserva
  relativa à capacidade local.
- ✔ A mesma lógica se aplicaria a um cabo de fibra óptica submarino que
  reserva a única faixa costeira apta a ancoragem numa comunidade
  pesqueira, sem consultá-la. **Verdadeiro** — mesma estrutura de
  infraestrutura crítica reservando recurso escasso à custa de
  comunidade não consultada, em outro tipo de infraestrutura.
- ✗ Como o artigo descreve a Scala AI City como priorizando resfriamento
  sobre direitos territoriais, qualquer expansão de data center na
  América Latina produz necessariamente o mesmo padrão. **Falso** — o
  artigo usa um caso documentado, não uma prova de regra universal sem
  exceção.

---

## Pausa 4 (Bloco 4 — Arcabouço Teórico): Inclusão Predatória: Inclusão de Verdade?

**Discussão da pergunta provocadora:** Não necessariamente. A definição
de zona de sacrifício digital do artigo exige que a inclusão seja
**predatória** — o território recebe investimento e presença física
(infraestrutura, servidores, reserva de recurso), mas como sítio de
extração, não como beneficiário proporcional. "Aparecer no mapa" não é
o mesmo que "se beneficiar" ou "ter sido consultado sobre os termos
dessa inclusão" — é exatamente essa diferença que separa zona de
sacrifício digital (inclusão predatória) de um caso de inclusão
genuína, onde o território de fato ganha algo proporcional ao que
cede.

**V/F — resolução:**

- ✔ Se um Estado atraísse investimento em IA sem acomodar interesse de
  capital transnacional nem externalizar custo ambiental/social, o
  paradoxo da soberania digital não se aplicaria a esse caso.
  **Verdadeiro** — sem essa troca, faltaria exatamente o mecanismo que
  o artigo descreve como paradoxal.
- ✗ No limite em que um território fosse totalmente excluído de
  qualquer investimento digital, esse território se qualificaria como
  zona de sacrifício digital. **Falso** — exclusão total é a definição
  de redlining digital, não de zona de sacrifício, que exige inclusão
  (ainda que predatória).
- ✔ A mesma lógica de tensão entre dimensões de soberania se aplicaria
  a um país com soberania regulatória forte mas dependente de nuvem
  estrangeira. **Verdadeiro** — mesmo tipo de desequilíbrio entre
  dimensões de soberania digital, com outro par de dimensões.
- ✗ Como soberania digital exige controle sobre quatro dimensões, um
  país só é "digitalmente soberano" com as quatro plenamente
  realizadas, sem grau intermediário. **Falso** — o artigo trata as
  dimensões como graduais e potencialmente desiguais, não como um
  pacote binário.

---

## Pausa 5 (Bloco 5 — Ampliando o Olhar): Um Acordo "Verde" Sem Quem Vive na Terra

**Discussão da pergunta provocadora:** A narrativa oficial apresenta o
acordo LEAF/Pará como "vitória para a conservação"; mas o próprio
artigo mostra que ele foi assinado sem consulta às comunidades
indígenas e quilombolas residentes no território afetado — uma
omissão que viola diretamente o padrão de Consentimento Livre, Prévio
e Informado (CLPI) da Convenção 169 da OIT. A divergência entre
narrativa e política real é exatamente o mecanismo do colonialismo
verde: uma linguagem de sustentabilidade («compensação», «créditos de
carbono», «conservação») é usada para justificar um acordo financeiro
que, na prática, segue a mesma lógica de externalização de custo
territorial vista nos outros casos da aula, sem incluir quem vive na
terra na decisão.

**V/F — resolução:**

- ✔ Se o governo do Pará tivesse realizado consulta livre, prévia e
  informada antes de assinar o acordo, a violação da Convenção 169 não
  teria ocorrido da mesma forma. **Verdadeiro** — a violação específica
  apontada é justamente a ausência dessa consulta.
- ✔ No limite em que uma empresa reduzisse suas próprias emissões a
  zero na fonte, o mecanismo de colonialismo verde do caso LEAF/Pará
  perderia sua função específica (compensar em vez de reduzir).
  **Verdadeiro** — sem emissão para compensar, essa função específica
  desaparece.
- ✔ A mesma lógica se aplicaria a uma empresa de tecnologia que compra
  compensações florestais distantes enquanto aumenta o consumo real de
  energia fóssil na origem. **Verdadeiro** — mesma estrutura de
  greenwashing, usando compensação distante para mascarar aumento real
  na origem.
- ✗ Como o acordo foi assinado sem consulta, toda compra de crédito de
  carbono é, por definição, colonialismo verde. **Falso** — o problema
  apontado é a falta de consulta e a captura corporativa desse caso
  específico, não o mecanismo de crédito de carbono em si.

---

## Pausa 6 (Bloco 6 — Ciclo de Vida): O Ciclo Que Ninguém Vê Até o Fim

**Discussão da pergunta provocadora:** Estaria faltando o impacto
ambiental das fases de **produção** (extração de minerais, manufatura
do hardware) e de **descarte** (o que acontece com o servidor ao final
da vida útil — reciclagem, ou resíduo eletrônico sem tratamento). A
análise de ciclo de vida existe exatamente para evitar essa
contabilidade parcial: medir só a fase de uso é como avaliar o impacto
ambiental de um carro olhando só para o escapamento, sem considerar a
mineração dos materiais da bateria nem o destino do veículo quando é
descartado.

**V/F — resolução:**

- ✔ Se toda a energia da fase de operação viesse de fontes renováveis,
  a análise de ciclo de vida ainda poderia revelar impacto significativo
  nas fases de produção e descarte. **Verdadeiro** — a análise cobre
  as três fases separadamente; resolver uma não resolve as outras.
- ✔ No limite em que um hardware fosse produzido, usado e descartado
  sem nenhuma extração de matéria-prima nova, a fase de "extração"
  perderia parte de seu impacto característico. **Verdadeiro** — sem
  extração nova, essa fase específica perde o impacto que normalmente
  lhe é atribuído.
- ✔ A mesma lógica se aplicaria a uma fabricante de smartphones que só
  divulga o baixo consumo de energia no uso, sem informar o impacto da
  mineração do lítio da bateria. **Verdadeiro** — mesma lógica de
  ocultação parcial, aplicada a outro produto.
- ✗ Como a TI Verde promove "Verde Por Software" e "Verde No Software",
  qualquer sistema em uma dessas categorias está isento de impacto
  ambiental relevante. **Falso** — as categorias descrevem uma
  orientação de projeto, não uma garantia de impacto zero.

---

## Pausa 7 (Bloco 7 — Síntese): Um Checklist Territorial

**Discussão da pergunta provocadora:** Não há uma resposta fixa
correta — o exercício pede para aplicar o checklist (quem paga o custo
material, quem foi consultado, que narrativa de sustentabilidade está
em jogo, se ferramentas técnicas de projeto foram usadas) a um caso
concreto escolhido pelo próprio aluno. O padrão pedagógico central é o
próprio exercício de leitura crítica: para a maioria dos projetos de
infraestrutura digital do cotidiano, a resposta a "quem foi consultado"
tende a ser "ninguém que arca com o custo material direto" — é
justamente esse padrão de ausência de consulta que a aula pede para
aprender a notar.

**V/F — resolução:**

- ✔ Se um data center publicasse consulta livre, prévia e informada
  antes da construção, atenderia a uma das exigências centrais da
  ética territorial, mesmo podendo ser criticado por outros motivos.
  **Verdadeiro** — consulta prévia documentada atende a uma das quatro
  perguntas do checklist.
- ✔ No limite em que um território fosse tratado exclusivamente como
  jurisdição legal, sem consideração cultural/ecológica/ancestral, isso
  seria o oposto do que a ética territorial propõe. **Verdadeiro** — é
  exatamente o oposto da proposta do artigo.
- ✔ A mesma lógica do checklist se aplicaria à avaliação de um cabo de
  fibra óptica internacional e comunidades costeiras em sua rota.
  **Verdadeiro** — aplicação direta do checklist a outro tipo de
  infraestrutura digital.
- ✗ Como a ética territorial defende tratar o território além de
  jurisdição legal, nenhum projeto deveria, em hipótese alguma, ser
  construído em território tradicional, independentemente de consulta
  ou compensação. **Falso** — a ética territorial exige consulta
  genuína e divisão justa, não uma proibição absoluta e incondicional.

---

## Pausa 8 (Bloco 8 — Fechamento): O Que Mais Está Escondido Atrás da Tela?

**Discussão da pergunta provocadora:** Vários candidatos plausíveis,
todos antecipando a Aula 7: um sistema de reconhecimento facial
treinado majoritariamente com rostos de pele clara, que erra mais em
rostos de pele escura, sem que nenhum engenheiro tenha "decidido"
discriminar; um algoritmo de concessão de crédito treinado com
decisões humanas históricas que já refletiam discriminação, herdando
esse padrão sem intenção explícita; um sistema de recrutamento
automatizado que aprende, dos currículos históricos de uma empresa, um
viés de gênero que ninguém programou de propósito. Em todos os casos,
o padrão é o mesmo desta aula: uma consequência real e mensurável que
ninguém precisou decidir explicitamente para que ela existisse.

**V/F — resolução:**

- ✔ Se toda a energia e água usada por data centers de IA viessem de
  fontes com impacto desprezível, e nenhuma comunidade tivesse direitos
  afetados, o argumento sobre "zonas de sacrifício digital" perderia
  sua base empírica de aplicação, mesmo continuando coerente em teoria.
  **Verdadeiro** — sem custo material real recaindo sobre nenhuma
  comunidade, falta a base empírica do argumento aplicado a esse caso.
- ✔ No limite em que toda decisão de arquitetura já considerasse
  explicitamente seu custo material e territorial completo, a
  categoria de "custo não decidido explicitamente" deixaria de
  descrever essa decisão. **Verdadeiro** — se já fosse sempre
  considerado, deixaria de ser, por definição, um custo "não decidido
  explicitamente".
- ✔ A mesma lógica estrutural se estenderia ao argumento da Aula 7 de
  que dados históricos podem carregar viés discriminatório sem que
  nenhum engenheiro o tenha programado de propósito. **Verdadeiro** —
  é exatamente a ponte para a Aula 7.
- ✗ Como esta aula mostrou custo territorial real da infraestrutura de
  IA, a única forma responsável é interromper por completo seu
  desenvolvimento, sem alternativa intermediária. **Falso** — a
  síntese da aula propõe alternativas intermediárias (consulta
  genuína, ética territorial, ferramentas de projeto), não abandono
  total.
