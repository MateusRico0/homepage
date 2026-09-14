## Resumo — Aula 6: Architecture, Energy, and the Material Cost of Digital Infrastructure

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

## Plano de aula — Aula 6 (carga horária nominal: ~90–95min)

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

8. **Fechamento e Ponte para a Aula 7** (~8 min) — Retomar as cinco
   perguntas da abertura, uma frase cada. O que fica em aberto: hoje
   vimos que o custo material da IA é distribuído de forma desigual e
   sistematicamente invisibilizado por narrativas de progresso e
   sustentabilidade — mas essa mesma lógica de "um sistema aparentemente
   neutro e técnico esconde uma desigualdade estrutural que ninguém
   precisou 'decidir' explicitamente" se estende, na Aula 7, para dentro
   do próprio algoritmo: os dados que treinam um sistema de IA carregam
   uma história de viés que, sem auditoria, produz discriminação
   automatizada da mesma forma silenciosa.

## Fontes usadas — Aula 6

Ver `_01-fontes.md` para os trechos literais completos, com verificação
de offset de página de cada PDF. Resumo das fontes usadas:

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
