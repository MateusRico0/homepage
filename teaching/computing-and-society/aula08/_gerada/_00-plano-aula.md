> **Origem (2026-10-05):** esta aula foi escrita como Aula 6 e ficou em
> `aula06/` até o commit `818be15`, quando a disciplina foi reordenada
> (Aula 6 = Dados e Viés; Aula 7 = Fairness). Foi recuperada em
> `aula08/` com três adaptações: (1) a Abertura revisa as Aulas 6–7 e
> retoma a Ponte da Aula 7 ("todo esse cálculo roda em algum lugar
> físico"); (2) o Fechamento faz a Ponte para a Aula 9 (Gênero e
> Diversidade, início da Parte 3), e a última Pausa Ativa passou a ser
> "Quem Estava na Sala?"; (3) os exercícios ganharam `## Contexto e
> notação`. O restante do plano abaixo é o original; onde ele diz
> "Aulas 4–5" como ideia-ponte, leia "Aulas 6–7". As fontes, antes em
> `_01-fontes.md`, estão no fim deste arquivo.

## Resumo — Aula 8: Architecture, Energy, and the Material Cost of Digital Infrastructure

As Aulas 1–5 tratam software como prática sociotécnica em escalas
progressivamente mais amplas: o mapa de atores de um sistema (Aula 1),
a ética normativa e o Ciclo Ético (Aula 2), a responsabilidade
profissional (Aula 3), os mecanismos estruturais e deliberados dentro
de uma equipe de engenharia (Aula 4), e o kit metodológico que essa
equipe usa para decidir o que construir, com seu duplo uso de entender
ou direcionar o usuário (Aula 5). Esta aula muda de escala outra vez:
sai do comportamento do usuário individual e vai para a **materialidade
física da infraestrutura computacional** — energia, água, minerais,
território — e para quem, concretamente, arca com esse custo quando
ele não é o consumidor final do serviço digital.

O fio condutor não é mais uma métrica de produto, é um **caso real e
atual**: a expansão de data centers de Inteligência Artificial na
América Latina, ancorada no artigo de pesquisa de Beatriz Cardoso
Nascimento (aluna de graduação do Instituto de Computação da UNICAMP)
e Marcos Medeiros Raimundo (2026, ainda não publicado em veículo
formal — tratado como *manuscript*/*working paper*), "Digital
Sovereignty in the Polycrisis: Technological Dependency, Invisible
Infrastructure, and AI Sacrifice Zones in Latin America". O caso
central é o projeto real **Scala AI City**, em Eldorado do Sul (RS):
uma reserva de 5 GW de energia apesar da instabilidade elétrica
regional e das enchentes catastróficas de 2024, marginalizando a
comunidade Mbyá-Guarani da Tekoa Pekuruty. A aula usa esse caso como
**problema motivador concreto** (Estratégia A, *Outside-In*) antes de
introduzir o arcabouço teórico do artigo (soberania digital, policrise
global, zonas de sacrifício digital, colonialismo verde) e, depois,
conecta esse arcabouço de volta às leituras-base já aprovadas da
disciplina (Van de Poel & Royakkers, Cap. 10 — Sustentabilidade; Maciel
& Viterbo, Vol. 2, Cap. 14 — Sustentabilidade em Computação), que
fornecem o vocabulário técnico de análise de ciclo de vida, TI Verde e
diretivas de projeto que respondem diretamente às competências de
"eficiência energética em arquitetura" e "ciclo de vida do lixo
eletrônico" já fixadas na ementa desta disciplina.

**Pré-requisitos:** nenhum bloco específico de aula anterior é
pré-requisito direto de conteúdo (esta aula abre um domínio novo:
materialidade física, não comportamento do usuário) — mas a aula
retoma, na Abertura, a tese que atravessa as Aulas 4–5 ("uma escolha
aparentemente só técnica tem consequência real fora do próprio
código/comportamento do usuário") como ideia-ponte (Ausubel) para
esticar essa mesma tese até o domínio material.

**Achado de correção de ementa, resolvido nesta sessão:** as duas
leituras recomendadas já aprovadas da Lesson 6 citavam capítulos com
numeração errada, no mesmo padrão de citação quebrada já documentado em
outras aulas desta disciplina (ver `_progresso.md`, "Achado importante:
citação quebrada"). Verificado por leitura direta do sumário de cada
livro nesta sessão:
- **Van de Poel & Royakkers (2011):** a ementa cita "Chapter 9:
  Sustainability, Ethics, and Technology". O sumário real do livro
  (`Ethics, Technology, and Engineering`, p. ix) mostra que esse
  capítulo é o **Capítulo 10** (pp. 277–300); o Capítulo 9 real é "The
  Distribution of Responsibility in Engineering" (pp. 249–276), sobre o
  *problem of many hands* — tema diferente, sem relação direta com
  sustentabilidade.
- **Maciel & Viterbo (2020), Vol. 2:** a ementa cita "Capítulo 8:
  Sustentabilidade em Computação". O sumário real do Vol. 2 mostra que
  o capítulo com esse título é o **Capítulo 14** (pp. 175–204,
  autoria de Vânia Neris, Kamila Rodrigues, Renata Rodrigues Oliveira e
  Newton Galindo Jr.); o Capítulo 8 real do Vol. 2 é outro tema, sobre
  cultura de dados abertos.

**Decisão de escopo desta sessão:** ao contrário das correções
análogas já feitas em Lições 1, 2 e 3, **estas duas não foram
aplicadas** ao `../index.qmd` — a instrução desta sessão limitou
explicitamente as edições permitidas nesse arquivo a exatamente duas:
transformar o título da Lesson 6 em link, e acrescentar a terceira
leitura (Nascimento & Raimundo) à lista já existente, mantendo o texto
das duas leituras originais intacto. As correções de numeração ficam
**sinalizadas aqui e em `_progresso.md`**, no mesmo padrão já usado
para a citação pendente da Aula 7 (Steen) — resolvidas só na citação
usada dentro do próprio `aula06/index.qmd` (que cita corretamente Cap.
14 e Capítulo 10), não na ementa pública da disciplina.

**Objetivos de aprendizagem** (do `../index.qmd`, Lesson 6, texto já
aprovado, tratado como contrato de escopo, exceto pela correção de
numeração de capítulo acima):
- **Objectives:** Analyze the environmental and material impacts of
  technology, including the carbon footprint of data centers, energy
  efficiency in system architecture, and the electronic waste
  lifecycle and disposal.
- **Expected Competencies:** Ability to assess energy consumption and
  environmental lifecycle trade-offs when designing and deploying
  computational infrastructure.

**Leitura recomendada** (do `../index.qmd`, Lesson 6, com a terceira
leitura adicionada nesta sessão): Maciel & Viterbo (2020), Vol. 2, Cap.
14 "Sustentabilidade e Computação"; Van de Poel & Royakkers (2011),
Cap. 10 "Sustainability, Ethics, and Technology"; **Nascimento &
Raimundo (2026)**, "Digital Sovereignty in the Polycrisis:
Technological Dependency, Invisible Infrastructure, and AI Sacrifice
Zones in Latin America" (manuscrito/*working paper*, Instituto de
Computação, UNICAMP).

## Estratégia Pedagógica

**Estratégia A (Outside-In)** — a única aula desta disciplina, até
aqui, que reintroduz explicitamente o rótulo formal (usado nas
disciplinas STEM desta pasta): o assunto se presta bem a essa lógica
porque existe um **caso concreto, real e recente** (Scala AI City) rico
o bastante para funcionar como problema motivador completo antes de
qualquer conceito formal — do mesmo jeito que a Aula 4 abriu com o caso
COBOL/ALGOL de Conway antes de formalizar a Lei de Conway. A progressão
é: caso motivador concreto (Scala AI City, Eldorado do Sul) → a
materialidade física que o caso expõe (energia, água, minerais) →
arcabouço teórico que nomeia o mecanismo (soberania digital, policrise,
zonas de sacrifício digital) → ampliação comparativa (outros casos
latino-americanos) → síntese prática ligando de volta ao vocabulário
técnico de projeto (ciclo de vida, TI Verde) que a ementa já previa →
fechamento com uma ética territorial de síntese.

## Plano de aula — Aula 8 (carga horária nominal: ~90–95min)

1. **Abertura — Da Nuvem Etérea à Materialidade do Concreto** (~8 min)
   — Revisão: as Aulas 4–5 mostraram que uma escolha aparentemente "só
   técnica" (arquitetura de requisitos, escolha de métrica) tem
   consequência real fora do próprio código ou do comportamento do
   usuário. Ideia central (Ausubel): hoje essa mesma tese se estica até
   o domínio **material** — uma escolha de arquitetura de sistema
   (onde hospedar, quantos servidores, como resfriar) tem custo físico
   real, em energia, água, minerais e terra, que ninguém "decidiu"
   explicitamente impor a quem paga esse custo. Roteiro explícito (5
   perguntas, ver abaixo). Problema motivador: a Inteligência
   Artificial é vendida como algo "etéreo", uma "nuvem" sem peso — mas
   e se ela pesar, literalmente, gigawatts, litros de água e hectares
   de terra indígena? Pausa ativa fechando o bloco.

2. **A Materialidade Escondida: Energia, Água e Minerais por Trás da
   Nuvem** (~10 min) — Desenvolve o problema motivador com o
   vocabulário técnico da leitura de Maciel & Viterbo (2020, Cap. 14):
   TI Verde como conjunto de práticas para reduzir o impacto ambiental
   de recursos tecnológicos; a Tabela 14.1 do livro (diretivas
   ambientais para soluções de TI) mostra que a construção e a
   manutenção de hardware já demandam consumo de água, energia e
   minerais antes mesmo de qualquer uso — e que o resfriamento
   (*cooling*) de hardware é, especificamente, um dos pontos de maior
   consumo de água e energia. Ponte imediata para o Bloco 3: é
   exatamente esse resfriamento, em escala industrial, que está no
   centro do caso Scala AI City.

3. **Caso Central: Scala AI City e a Tekoa Pekuruty (Eldorado do Sul)**
   (~15 min) — O caso motivador da Abertura, aprofundado com os dados
   do artigo de Nascimento & Raimundo (2026): reserva de 5 GW de
   energia em Eldorado do Sul (Rio Grande do Sul), apesar da
   instabilidade elétrica regional e da vulnerabilidade a desastres
   climáticos (as enchentes catastróficas de 2024 atingiram
   exatamente essa região); o projeto marginaliza a comunidade
   Mbyá-Guarani da Tekoa Pekuruty, priorizando o resfriamento de
   servidores sobre direitos territoriais ancestrais. Nota explícita
   de autoria: esta é uma pesquisa de uma aluna de graduação deste
   próprio Instituto de Computação, orientada pelo professor — usada
   deliberadamente como o eixo narrativo da aula, não como mais uma
   citação de rodapé.

4. **Arcabouço Teórico: Soberania Digital, Policrise e Zonas de
   Sacrifício Digital** (~15 min) — Nomeia formalmente os mecanismos
   que o caso Scala AI City ilustra: **soberania digital** (a
   capacidade de um Estado exercer autoridade sobre sua arquitetura
   digital — quatro dimensões: infraestrutural, de dados, regulatória
   e epistêmica); **policrise global** (crises climáticas, energéticas
   e sociais causalmente entrelaçadas, não isoladas); **zonas de
   sacrifício digital** (territórios onde a degradação ambiental e a
   desapropriação social são tratadas como o preço aceitável da
   integração tecnológica) — contrastadas explicitamente com
   **redlining digital** (que segrega/exclui do serviço), já que zonas
   de sacrifício operam por **inclusão predatória**: o território é
   "incluído" no mapa da IA global não como beneficiário, mas como
   sítio de extração.

5. **Ampliando o Olhar: Querétaro, Módulo Penco e o Greenwashing do
   Pará** (~15 min) — Dois casos de contraste/amplitude do mesmo
   artigo, mostrando que o padrão de Eldorado do Sul não é isolado:
   Querétaro (México), onde centros de dados corporativos prosperam em
   meio à fragilidade hídrica e elétrica local, com aumento de 151% nos
   apagões entre 2014 e 2023; e o "Módulo Penco" (Chile), extração de
   terras raras para hardware de IA em terreno de resistência histórica
   Mapuche, rejeitado por 99% da população em consulta pública. Depois,
   o caso da Coalizão LEAF no Pará: um acordo de R$ 1 bilhão de créditos
   de carbono assinado sem consulta às comunidades indígenas e
   quilombolas afetadas — violando o padrão de Consentimento Livre,
   Prévio e Informado (CLPI) da Convenção 169 da OIT — como exemplo de
   **colonialismo verde**: a narrativa de sustentabilidade usada para
   obscurecer, não resolver, a externalização de custo ambiental.

6. **Da Crítica ao Projeto: Ciclo de Vida e TI Verde** (~15 min) —
   Volta ao vocabulário técnico das duas leituras-base já aprovadas da
   ementa, agora com o caso latino-americano como pano de fundo:
   definição de Brundtland de desenvolvimento sustentável (Van de Poel
   & Royakkers, Cap. 10) e as duas justiças que ela articula
   (intergeracional e intrageracional) e o princípio do poluidor-pagador;
   **análise de ciclo de vida** (produção → uso → descarte) como
   ferramenta de projeto que mapeia o impacto ambiental de um sistema
   computacional de ponta a ponta — a ferramenta certa para a
   competência de "ciclo de vida do lixo eletrônico" da ementa; TI
   Verde e a distinção "Verde Por Software" (sistemas que promovem
   sustentabilidade) vs. "Verde No Software" (tornar o próprio software
   mais sustentável). Ponte: essas ferramentas de projeto, aplicadas
   civicamente, é o que uma resposta responsável ao padrão do Bloco 3
   exigiria — mas o Bloco 3 mostrou que a decisão real (Scala AI City)
   não passou por elas.

7. **Síntese: Rumo a uma Ética Territorial** (~8 min) — O conceito de
   ética territorial do artigo de Nascimento & Raimundo: tratar o
   território não como jurisdição legal passiva, mas como entidade
   multidimensional que une o ecossistema físico ao espaço culturalmente
   apropriado; a soberania digital genuína depende de uma ética que
   recuse deixar a expansão computacional apagar epistemologias e
   realidades vividas das populações locais. Síntese prática: um
   checklist de perguntas para avaliar uma decisão de infraestrutura
   digital (quem paga o custo material, quem foi consultado, que
   narrativa de sustentabilidade está sendo usada e para proteger o
   quê).

8. **Fechamento e Ponte para a Aula 9** (~8 min) — Retomar as cinco
   perguntas da abertura, uma frase cada. O que fica em aberto: o custo
   material da IA é distribuído de forma desigual e invisibilizado por
   narrativas de progresso e sustentabilidade (mesma estrutura das
   Aulas 6–7, com energia, água e território no lugar do dado); falta
   transformar a ética territorial em procedimento (quem consulta, com
   que poder de veto, em que etapa). Pausa Ativa final: "Quem Estava na
   Sala?" — que custos uma equipe de projeto homogênea deixaria de ver.
   Ponte para a Aula 9: a Parte 2 terminou perguntando quem *não*
   estava na sala; a Parte 3 começa perguntando quem *está* — gênero,
   diversidade e composição da equipe.

## Fontes usadas — Aula 8

Os trechos literais completos, com verificação de offset de página de
cada PDF, estão na seção "Trechos literais" no fim deste arquivo. Resumo das fontes usadas:

1. **Nascimento & Raimundo (2026)** — fonte central da aula (caso
   motivador, arcabouço teórico inteiro): lida por completo (5 páginas
   de texto + referências), PDF acessado via
   `_fontes/Computação e Sociedade/Cloud/Digital_Sovereignty_in_the_Polycrisis.pdf`
   (symlink de diretório já existente, sem novo symlink necessário).
   Numeração impressa = numeração do PDF (offset 0, documento sem
   pré-textual). **Verificação de venue:** o PDF não indica, em nenhum
   lugar do próprio texto (cabeçalho, rodapé, ou primeira página), o
   nome de um periódico ou anais de conferência — nenhuma marca d'água
   de *venue*, nenhum cabeçalho de conferência, nenhum DOI. Tratado
   como manuscrito/*working paper* não publicado, citado como
   "Nascimento & Raimundo (2026)" sem afirmar veículo de publicação.
2. **Van de Poel & Royakkers (2011)**, Cap. 10 "Sustainability, Ethics,
   and Technology" (pp. 277–300) — definição de Brundtland (p. 283),
   justiça intergeracional/intrageracional e princípio do
   poluidor-pagador (p. 284), análise de ciclo de vida (p. 293).
3. **Maciel & Viterbo (2020)**, Vol. 2, Cap. 14 "Sustentabilidade e
   Computação" (pp. 175–204) — TI Verde (pp. 182–183), Obsolescência
   Programada/e-waste (pp. 178–186), Tabela 14.1 de diretivas
   ambientais para soluções de TI (pp. 193–195), distinção Verde Por
   Software/Verde No Software (p. 187).

## Nota sobre a heurística de Transferência de Domínio nesta aula

Seguindo a convenção já registrada em `_progresso.md` (Aula 4 e Aula
5): os itens de V/F que usam a heurística 3 (Transferência de Domínio)
permanecem dentro do território **computação/infraestrutura
tecnológica**, nunca migrando para um domínio estapafúrdio ou
decorativo. Nesta aula específica, isso significa: transferir entre
diferentes casos reais de infraestrutura digital (outro data center,
outro país, outro tipo de recurso natural em disputa), nunca para
agropecuária, mineração não digital, ou qualquer outro domínio fora de
tecnologia — mesmo quando o conceito em jogo (ex.: justiça
intergeracional, ciclo de vida de um produto) tivesse, em princípio,
aplicação mais ampla.

---

## Trechos literais (antigo `_01-fontes.md`)

> Trechos literais extraídos lendo diretamente as páginas de cada PDF
> (não reescritos de memória, não traduzidos nesta etapa — a tradução
> só acontece no `index.qmd`, conforme `../../CLAUDE.md`).

---

### Fonte central: Nascimento & Raimundo (2026)

`../_fontes/Computação e Sociedade/Cloud/Digital_Sovereignty_in_the_Polycrisis.pdf`
— "Digital Sovereignty in the Polycrisis: Technological Dependency,
Invisible Infrastructure, and AI Sacrifice Zones in Latin America",
Beatriz Cardoso Nascimento e Marcos Medeiros Raimundo, Instituto de
Computação, UNICAMP. Documento de 7 páginas (5 de texto + 2 de
referências), sem numeração de página impressa distinta da paginação
do PDF (offset 0). Lido **por completo**.

**Verificação de veículo de publicação (pedido explícito do usuário,
antes de assumir "não publicado"):** o PDF não traz, em nenhuma página,
nome de periódico, anais de conferência, marca d'água, cabeçalho de
*venue*, DOI, ou qualquer outro indício de publicação formal — só
título, autoria, afiliação (Instituto de Computação, UNICAMP) e
e-mails institucionais (`b247403@dac.unicamp.br`, `mrai@unicamp.br`).
Tratado nesta aula como **manuscrito/*working paper* não publicado**,
citado como "Nascimento & Raimundo (2026)" sem atribuir nenhum veículo.
A seção final do próprio artigo ("Author Contributions") confirma a
autoria dividida: Beatriz Cardoso Nascimento com
*Conceptualization, Methodology, Investigation, Writing – original
draft, Writing – review & editing*; Marcos Medeiros Raimundo com
*Supervision, Writing – review & editing, Conceptualization* — ou
seja, é uma orientação de pesquisa de graduação do próprio professor
desta disciplina, não uma citação de terceiros.

#### Fonte 1: Resumo (*Abstract*)

**Uso pretendido:** epígrafe/resumo do argumento central da aula
inteira (Bloco 1, Abertura, e retomado no Bloco 4).

**Trecho:**
> "This paper examines the expansion of Artificial Intelligence (AI)
> infrastructure in Latin America through the lenses of the planetary
> polycrisis and dependency theory. We investigate how the Brazilian
> State's response to the expansion of AI points to a reproduction of
> technological dependency and digital sacrifice zones. We argue that
> the uncritical race to implement massive data centers, fueled by
> state incentives and transnational capital, externalizes material
> costs to the territory. Drawing on recent evidence from Latin
> American cases, we conclude that achieving digital sovereignty in
> the Global South requires confronting the metabolic costs of AI
> within the limits of the climate crisis under a territorial ethics
> framework."

---

#### Fonte 2: Introdução — materialidade da IA (p. 1)

**Uso pretendido:** núcleo do Bloco 1 (Abertura) e Bloco 2
(Materialidade) — a tese de que a IA é vendida como "etérea" mas é
fisicamente concreta.

**Trecho:**
> "Artificial Intelligence (AI) is frequently marketed as a weightless
> technology: an ethereal realm of pure logic existing in a
> disembodied 'cloud'. However, beneath this layer of algorithmic
> abstraction lies materiality: AI is made of soil, water, and energy.
> Its existence depends on the extraction of rare minerals, the
> massive consumption of electricity, and the intensive use of water
> for cooling server farms [Crawford 2021]."

**Nota de precisão:** a última frase cita Crawford (2021), *The Atlas
of AI* — livro não lido diretamente nesta sessão (não symlinkado nesta
disciplina). O trecho é citado aqui como texto de Nascimento &
Raimundo (2026), não como citação direta de Crawford; no `index.qmd`,
sinalizar que a atribuição da ideia a Crawford (2021) vem de segunda
mão, via o artigo, não de leitura direta do livro.

---

#### Fonte 3: Policrise global (p. 1)

**Uso pretendido:** Bloco 4 — definição do conceito de policrise
global, citando Lawrence et al. (2022).

**Trecho:**
> "The concept of global polycrisis describes the occurrence of crises
> across multiple global systems that become causally entangled in
> ways that significantly degrade humanity's prospects [Lawrence et
> al. 2022]. In the context of AI, this can mean fueling consumerism
> through recommendation algorithms, developing surveillance and
> autonomous weapons, and embedding itself in carbon-intensive
> infrastructures [Gozum and Eballo 2025]."

---

#### Fonte 4: Soberania digital — quatro dimensões (pp. 1–2)

**Uso pretendido:** núcleo do Bloco 4 — definição formal de soberania
digital e suas quatro dimensões.

**Trecho:**
> "These dynamics fundamentally tension the notion of *digital
> sovereignty*. Although the term remains a site of intense conceptual
> contestation [Grohmann and Costa Barbosa 2026, Couture and Toupin
> 2019], it can be broadly understood as a state's capacity to
> exercise authority over its digital architecture, govern data flows
> within its jurisdiction, and implement governance models aligned
> with its own legal, cultural, and strategic interests. This pursuit
> of autonomy encompasses at least four critical dimensions —
> infrastructural, data, regulatory, and epistemic sovereignty — which
> are indispensable for a nation to steer its digital destiny [de
> Freitas 2025]."

---

#### Fonte 5: A contradição da soberania digital no Sul Global (p. 2)

**Uso pretendido:** Bloco 4 — o paradoxo de que buscar soberania digital
frequentemente exige o oposto (capital estrangeiro, acomodação de
interesses transnacionais).

**Trecho:**
> "However, in the context of the global polycrisis, the quest for
> such sovereignty is often paradoxical: the material requirements of
> AI expansion frequently force a trade-off between domestic autonomy
> and the urgent attraction of foreign technological capital. [...] In
> this context, the pursuit of digital sovereignty becomes
> contradictory, as achieving infrastructural autonomy often requires
> attracting foreign capital and accommodating the interests of
> transnational corporations. This dynamic reflects a reconfiguration
> of structural dependency, where states facilitate the externalization
> of environmental and social costs in exchange for participation in
> the global digital economy [Varon and Foletto 2025]. As a result,
> certain territories are transformed into digital sacrifice zones,
> where ecological degradation and social dispossession are normalized
> as the price of technological progress."

---

#### Fonte 6: Zonas de sacrifício digital vs. redlining digital (p. 3)

**Uso pretendido:** núcleo do Bloco 4 — definição formal de zona de
sacrifício digital, e o contraste explícito com redlining digital
(inclusão predatória vs. exclusão).

**Trecho:**
> "Building on the work of [Brodie 2023, Fernandes 2026], we define
> *digital sacrifice zones* in Latin America as territories where
> environmental destruction and resource depletion are deemed as the
> necessary price for technological integration by a political and
> economical judgment on its discardability. Unlike the usual concept
> of *digital redlining* [Friedline and Chen 2021, D'ignazio and Klein
> 2023] — which focuses on the segregation and denial of services —
> digital sacrifice zones are characterized by *predatory inclusion*.
> In this logic, the territory is 'included' in the global AI map not
> as a beneficiary of digital progress, but as a site of resource
> extraction and metabolic waste."

---

#### Fonte 7: IA como acelerador metabólico (pp. 2–3)

**Uso pretendido:** Bloco 4 — a ideia de que a IA acelera processos
extrativos ao mesmo tempo em que sua própria existência física demanda
energia e água em escala sem precedentes.

**Trecho:**
> "However, the coloniality of power persists in AI, refashioned
> through algorithmic systems, data infrastructures, and
> political-economic logics [Correa Lucero and Martens 2025].
> Developed economies maintain a facade of decoupling growth from
> environmental impact by externalizing resource-intensive burdens to
> the Global South [Görg et al. 2020], thus creating *sacrifice zones*:
> sites of concentrated environmental injustice [Juskus 2023]. In this
> context, AI serves as a metabolic accelerator: it optimizes and
> speeds up extractive processes while its own physical existence
> demands an unprecedented scale of electricity and water."

---

#### Fonte 8: Caso central — Scala AI City, Eldorado do Sul (p. 4)

**Uso pretendido:** núcleo do Bloco 3 (caso central da aula inteira).

**Trecho:**
> "Material Contradictions of Compute. The LEAF Coalition is not an
> isolated phenomenon but part of a systemic reconfiguration of Latin
> American territories into digital sacrifice zones where metabolic
> costs are externalized to the periphery. In Eldorado do Sul, the
> Scala AI City captures a massive 5 GW energy reservation despite the
> region's electrical instability and vulnerability to climate
> disasters, including the 2024 floods [Samuel 2025], marginalizing
> the Mbyá-Guarani of Tekoa Pekuruty and prioritizing server cooling
> over ancestral land rights [LAPIN 2025]."

---

#### Fonte 9: Casos de contraste — Querétaro e Módulo Penco (p. 4)

**Uso pretendido:** Bloco 5 — ampliação comparativa do caso central.

**Trecho:**
> "This logic of resource prioritization is replicated in Querétaro,
> Mexico, where corporate data hubs thrive amidst severe water and
> electrical fragility while local communities faced a 151% increase
> in power outages between 2014 and 2023 [Quijano and Soria 2025].
> Further south, the 'Módulo Penco' in Chile targets sites of historic
> Mapuche resistance for rare earth extraction to supply AI hardware —
> a project rejected by 99% of the local population in public
> consultations [Peña and Ananías 2025]."

---

#### Fonte 10: Greenwashing — o caso LEAF/Pará (p. 3)

**Uso pretendido:** Bloco 5 — caso de colonialismo verde/greenwashing,
contrastando a narrativa oficial com a violação do CLPI (Convenção 169
da OIT).

**Trecho:**
> "AI Colonialism in Greenwashing. The financialization of nature
> through green narratives represents a contemporary frontier of value
> extraction in the age of AI. A salient example is the involvement of
> Big Tech corporations in the LEAF (Lowering Emissions by
> Accelerating Forest Finance) Coalition, a public-private initiative
> that finances tropical forest protection by purchasing
> jurisdictional carbon credits from large-scale, state-led REDD+
> projects [LAPIN 2025]. In 2024, the government of Pará signed a R$ 1
> billion agreement to sell carbon credits to the coalition without
> consultation to the Indigenous and Quilombola communities residing
> in the affected territories. This omission directly contravenes the
> normative pillars of Free, Prior, and Informed Consent (FPIC)
> established by the ILO Convention 169 [Terra de Direitos 2025]."
>
> "While official narratives framed the deal as a victory for
> conservation, the actual policies reveal a corporate-aligned agenda
> [Horn and Ramos 2025]. This dynamic operationalizes *green
> colonialism*: the Amazon is repositioned as a financial asset to
> offset the carbon footprints of Global North corporations [Fernandes
> and Bringel 2025]. As Big Tech infrastructure expands through
> energy-intensive data centers in the Global North – exponentially
> increasing fossil fuel emissions – these corporations opt to
> purchase carbon credits rather than reducing their material impact
> at the source [LAPIN 2025]."

---

#### Fonte 11: Ética territorial (p. 4)

**Uso pretendido:** núcleo do Bloco 7 (Síntese).

**Trecho:**
> "Toward a Southern Territorial Ethics. These cases illustrate that
> there is no software without hardware, and no hardware without the
> reliance on predatory resource extraction from Indigenous lands
> [Faustino and Lippold 2023]. Confronting the metabolic costs of AI
> requires *territorial ethics*, understood as a conglomerate of
> principles regulating the behavior of relations between subjects and
> the territory [Cuervo 2011]. Within the Latin American context, this
> framework demands that territory be treated not as a passive legal
> jurisdiction but as a multidimensional entity that binds the
> physical ecosystem to culturally appropriated spaces [Cuervo 2011].
> [...] Achieving digital sovereignty thus depends on a territorial
> ethics that refuses to let computational expansion erase the diverse
> epistemologies and lived realities of the plural Souths [Milan and
> Treré 2019]."

---

#### Fonte 12: Conclusão do artigo (p. 4)

**Uso pretendido:** Bloco 8 (Fechamento) — síntese final do argumento,
para retomar no fechamento da aula.

**Trecho:**
> "This paper has argued that the expansion of AI infrastructure in
> Latin America is far from an ethereal technological advancement,
> representing instead a material reconfiguration of colonial
> dependency within the global polycrisis. [...] This work invites a
> broader dialogue on a territorial ethics that confronts the climate
> crisis and asserts the right of marginalized geographies to refuse
> predatory inclusion, ensuring that digital sovereignty in the Global
> South does not result in the ecological and epistemic erasure of its
> territories."

---

#### Fonte 13 (opcional, ponto de precisão de pesquisa): Declaração de Considerações Éticas (p. 5)

**Uso pretendido:** menção breve no Bloco 3, como exemplo de boa
prática de disclosure de posicionalidade de pesquisa — só se encaixar
sem atrapalhar o fluxo da aula (avaliação feita na Etapa 3).

**Trecho:**
> "The authors acknowledge their positionality as researchers based at
> a latin american public university. [...] Although we do not belong
> to the Indigenous or Quilombola communities mentioned, this research
> was conducted through an ethical commitment to amplify Southern
> epistemologies and critique the structural mechanisms of their
> marginalization. The primary ethical challenge was ensuring the
> accurate representation of marginalized communities' struggles
> without speaking for them, but rather analyzing the structural
> mechanisms that produce their invisibility."

---

### Fonte: Van de Poel & Royakkers (2011)

`../_fontes/Computação e Sociedade/Ethics, Technology, and Engineering -- van de Poel and Royakkers -- 2011.pdf`
— **Capítulo 10**, "Sustainability, Ethics, and Technology" (autoria de
Michiel Brumsen dentro do livro), pp. 277–300.

**Correção de ementa (achado desta sessão):** a Lesson 6 já aprovada no
`../index.qmd` citava "Chapter 9: Sustainability, Ethics, and
Technology" — capítulo com numeração errada. Confirmado pelo sumário
real do livro (p. ix): o Capítulo 9 real é "The Distribution of
Responsibility in Engineering" (pp. 249–276, sobre o *problem of many
hands*), sem relação com sustentabilidade; o capítulo correto,
"Sustainability, Ethics, and Technology", é o **Capítulo 10** (pp.
277–300). Numeração impressa do livro = numeração do PDF menos 0 (sem
offset: `pdftotext` extraiu a numeração de rodapé de página
diretamente, conferida contra o sumário, mesmo valor em ambos). **Não
corrigido no `../index.qmd`** — o escopo desta sessão para aquele
arquivo ficou restrito a duas edições (link do título + nova leitura);
a correção fica sinalizada aqui e em `_progresso.md` para decisão numa
sessão futura, mesmo padrão já usado para a citação pendente da Aula 7
(Steen). A citação usada neste `_01-fontes.md` e no `aula06/index.qmd`
já emprega o capítulo correto (10).

#### Fonte 14: A definição de Brundtland (p. 283)

**Uso pretendido:** núcleo do Bloco 6 — definição formal de
desenvolvimento sustentável.

**Trecho:**
> "Sustainable development is development that meets the needs of the
> present without compromising the ability of future generations to
> meet their own needs. It contains within it two key concepts: the
> concept of 'needs,' in particular the essential needs of the world's
> poor, to which over-riding priority should be given; and the idea of
> limitations imposed by the state of technology and social
> organization on the environment's ability to meet present and future
> needs. (World Commission on Environment and Development, 1987)"

---

#### Fonte 15: Justiça intergeracional, intrageracional e o poluidor-pagador (p. 284)

**Uso pretendido:** Bloco 6 — as duas justiças que fundamentam
moralmente o desenvolvimento sustentável, e o princípio do
poluidor-pagador.

**Trecho:**
> "The heart of sustainable development lies in two kinds of justice.
> The first kind of justice relates to the division of resources
> between our own generation and future generations: intergenerational
> justice. [...] Next to that, sustainable development requires a just
> division of resources within our own generation (compare the First
> and the Third World): intragenerational justice."
>
> "Essentially, this is an extension of the polluter pays principle or
> the notion that 'the one who breaks something is also expected to
> mend it.' The point of departure is that damage to the environment
> must be repaired by the party responsible for the damage."

---

#### Fonte 16: Análise de ciclo de vida (p. 293)

**Uso pretendido:** núcleo do Bloco 6 — ferramenta de projeto que
mapeia o impacto ambiental de um produto/sistema computacional ao
longo de todo o ciclo de vida (produção, uso, descarte) — resposta
direta à competência de "ciclo de vida do lixo eletrônico" da ementa.

**Trecho:**
> "The point of departure for life cycle analysis is that you must be
> able to compare the environmental impact you cause with your design
> with alternative designs in order to achieve a sustainable design.
> This can be done by mapping the environmental impact across the
> entire cycle of extraction, refining, production, use, and
> disposal."
>
> "Life cycle analysis: An analysis that maps the environmental impact
> of a product across the entire cycle of production, use, and
> disposal."

---

### Fonte: Maciel & Viterbo (2020), Vol. 2

`../_fontes/Computação e Sociedade/Computação e Sociedade | Volume 2 - A sociedade -- Maciel e Viterbo -- 2020.pdf`
— **Capítulo 14**, "Sustentabilidade e Computação" (autoria de Vânia
Neris, Kamila Rodrigues, Renata Rodrigues Oliveira e Newton Galindo
Jr.), pp. 175–204.

**Correção de ementa (achado desta sessão, mesmo padrão já documentado
em `_progresso.md` para outras Lessons desta disciplina):** a Lesson 6
já aprovada citava "Vol. 2, Capítulo 8: Sustentabilidade em
Computação" — capítulo com numeração errada. Confirmado pelo sumário
real do Vol. 2: o capítulo com esse título é o **Capítulo 14** (pp.
175–204); o Capítulo 8 real do Vol. 2 trata de outro tema. **Não
corrigido no `../index.qmd`** — mesma decisão de escopo explicada
acima, na fonte de Van de Poel & Royakkers (edições daquele arquivo
restritas a link do título + nova leitura nesta sessão); sinalizado
aqui e em `_progresso.md`. Numeração impressa do PDF = numeração do
livro (offset 0, conferido diretamente pelas quebras de página `pdftotext`
contra os números de rodapé visíveis no texto extraído).

#### Fonte 17: TI Verde (p. 182)

**Uso pretendido:** Bloco 2 (Materialidade) — definição de TI Verde
como conjunto de práticas para reduzir o impacto ambiental de recursos
tecnológicos.

**Trecho:**
> "Na área da Computação, há iniciativas na literatura como as de
> Tecnologia da Informação Verde (TI Verde), uma tendência mundial
> voltada para a redução do impacto dos recursos tecnológicos no meio
> ambiente. A TI Verde disponibiliza um conjunto de práticas para
> tornar mais sustentável e menos prejudicial o uso de tecnologia,
> propondo para isso, estratégias para compatibilizar o uso de recursos
> naturais de forma adequada às políticas sustentáveis existentes
> dentro das organizações (HESS, 2009). Exemplos práticos de
> estratégias incluem o uso de recursos tecnológicos que consumam menos
> energia, o uso de matéria prima e substâncias menos tóxicas nos
> processos produtivos e o descarte responsável dos produtos por meio
> da reciclagem e da reutilização de materiais (MONTEIRO et al.,
> 2012)."

---

#### Fonte 18: Obsolescência programada e descarte (pp. 178–186)

**Uso pretendido:** Bloco 2/Bloco 6 — o problema do descarte
incorreto de dispositivos (e-waste) e da obsolescência programada.

**Trecho (legenda da Figura 14.2, p. 179, e texto de abertura do
capítulo, p. 178):**
> "Figura 14.2 Obsolescência Programada."
>
> "A ampla adesão aos dispositivos móveis e aos computadores portáteis,
> assim como o uso constante da Internet, têm facilitado o dia a dia
> das pessoas, especialmente para a comunicação. Entretanto, esses
> recursos também se relacionam a problemas como o descarte incorreto
> dos dispositivos, o consumo desenfreado, disparidades econômicas,
> entre outros."

**Trecho adicional (p. 186, sobre o desafio GrandIHCBr):**
> "[...] o estímulo ao respeito ao próximo, ao transporte racional com
> logística otimizada e produção de veículos inteligentes, à boa
> alimentação e à gestão eficaz dos suprimentos, ao desenvolvimento de
> soluções eficazes para o e-waste etc. (NERIS et al., 2012)."

---

#### Fonte 19: Tabela 14.1 — diretivas ambientais para hardware e resfriamento (pp. 193–195)

**Uso pretendido:** núcleo do Bloco 2/Bloco 6 — as diretivas concretas
de projeto que ligam diretamente ao caso Scala AI City (consumo de
água/energia para resfriamento de hardware).

**Trecho (linha "Consumo [de Água]", p. 193, adaptada de Galindo Junior, 2017):**
> "Contexto: A construção e manutenção de partes de computadores
> implica em consumo de água. Sustentabilidade: Utilizar menos
> hardware; priorizar fabricantes que utilizem menos água para
> produção e operação de seus produtos; e, correlacionado, usar
> softwares mais eficientes energeticamente, isto é, que demandem
> menos processamento, e por consequência, menos necessidade de
> resfriamento por água."

**Trecho (linha "Consumo e Fontes [de Energia]", p. 194):**
> "Contexto: A construção e manutenção de partes de computadores
> implica em consumo de recursos energéticos. Sustentabilidade:
> Utilizar menos hardware; priorizar fabricantes que atentem para a
> eficiência de consumo energético na construção e operação de seus
> produtos [...]; utilizar hardware em que o resfriamento dependa
> minimamente de combustíveis fósseis; e, correlacionado, usar
> softwares mais eficientes energeticamente [...]."

**Trecho (linha "Reciclabilidade do Produto", p. 195):**
> "Contexto: A construção e manutenção de partes de computadores e
> produção de software demanda o uso recursos, que pode ser reciclável
> (reutilizado), ou não. Sustentabilidade: Utilizar menos hardware; e
> priorizar fabricantes que atentem para uso de matérias-primas
> recicláveis na produção. Também priorizar sistemas de software
> flexíveis que atendam a diferentes contextos de uso, minimizando a
> necessidade de atualizações constantes."

---

#### Fonte 20: Verde Por Software vs. Verde No Software (p. 187)

**Uso pretendido:** Bloco 6 — distinção entre tecnologia que promove
sustentabilidade e tecnologia que é, ela mesma, mais sustentável.

**Trecho:**
> "Verde Por Software - Aqueles desenvolvidos para domínios que
> trabalham para preservar a sustentabilidade no meio ambiente, ou
> seja, sistemas de software que servem como ferramentas para apoiar os
> objetivos de sustentabilidade; Verde No Software - Como tornar o
> software mais sustentável, resultando em um produto de software que
> os autores consideram 'ambientalmente amigável'."

---

### Conhecimento geral consolidado (sem citação literal) usado nesta aula

- **Bloco 4:** os detalhes factuais específicos das enchentes de 2024
  no Rio Grande do Sul (contexto histórico do desastre em si, além do
  que o artigo de Nascimento & Raimundo já cita) são de conhecimento
  público amplamente documentado na imprensa brasileira — mencionados
  na aula apenas como contexto factual de apoio ao caso, não como
  citação literal de nenhuma fonte jornalística específica lida nesta
  sessão.
- **Bloco 6:** a terminologia de "carbon footprint"/pegada de carbono
  de data centers, fora do que está literalmente nas Fontes 14–20
  acima, é tratada como conhecimento consolidado da área de TI
  Verde/computação sustentável, sem citação de página adicional.
