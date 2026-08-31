## Resumo — Aula 4: Human, Social, and Ethical Dimensions of Software Engineering

As Aulas 1–3 construíram o vocabulário (sistema sociotécnico, ética
normativa, códigos profissionais e as estruturas — conselho, lei — que
lhes dão força), sempre olhando a **profissão** e o **profissional**
individual. Esta aula muda de nível: olha a **prática de engenharia de
software em si** como um processo social, não uma sequência neutra de
passos técnicos. Dois mecanismos concretos sustentam essa tese: (1) a
**Lei de Conway** — a arquitetura de um sistema tende a copiar a
estrutura de comunicação de quem o constrói, não o contrário; e (2) a
**elicitação de requisitos como processo social** — "descobrir o que o
cliente quer" já é um ato de poder (quem é ouvido, quem não é, o que
fica de fora da especificação). A aula fecha mostrando como traduzir um
compromisso ético/social abstrato em artefato concreto de engenharia:
requisito não-funcional, decisão de arquitetura, ou porta de processo
(checklist de revisão, gate de CI).

**Pré-requisitos:** Aula 1 (sistema sociotécnico, mapa de atores) e
Aula 3 (responsabilidade profissional, códigos de conduta — agora
generalizada de "o profissional individual segue um código" para "o
processo de engenharia, estruturalmente, distribui responsabilidade de
um jeito que nem sempre é visível a quem está dentro dele").

**Objetivos de aprendizagem** (do `index.qmd`, Lesson 4, texto fornecido
pelo usuário):
- **Objectives:** Explore software engineering as a sociotechnical
  discipline, analyzing industry roles, communication dynamics
  (Conway's Law), and requirements elicitation as social processes.
  Demonstrate how to translate social responsibilities and human impact
  into architectural decisions, requirements, and development
  workflows.
- **Expected Competencies:** Ability to map stakeholder interactions
  and industry roles, analyze sociotechnical trade-offs in requirements
  engineering, and translate ethical commitments into non-functional
  requirements and concrete code architecture.

**Leitura recomendada** (do `index.qmd`, Lesson 4): Ian Sommerville
(2015), *Software Engineering* (10th Ed.), Cap. 1 (Introduction to
Sociotechnical Systems) e Cap. 4 (Requirements Engineering); Catherine
D'Ignazio & Lauren F. Klein (2020), *Data Feminism*, Cap. 2 ("Collect,
Analyze, Imagine, Teach"); Marc Steen (2022), *Ethics for People Who
Work in Tech*, Cap. 5 (já usado na Aula 3 para outro recorte — aqui
reaproveitado para a ponte entre compromisso ético e requisito
concreto); Mel Conway (1968), *How Do Committees Invent?* (o artigo
original da Lei de Conway).

**⚠️ Pendência antes da Etapa 3 (Fontes):** dos quatro textos acima, só
o de Steen já está symlinkado em `_fontes/` (`EthTech.pdf`, reaproveitado
da Aula 1/3). **Sommerville, Data Feminism, e o artigo de Conway não
têm PDF disponível em `_fontes/` nem encontrado em outro lugar do disco**
(busquei). Preciso que você (a) forneça/linke esses PDFs em `_fontes/`
(convenção do projeto: link simbólico, nunca copiar o arquivo de
verdade), ou (b) autorize eu buscar o artigo de Conway online — é um
artigo curto de 1968 amplamente disponível gratuitamente, então é fácil
de citar literalmente mesmo sem PDF local — e, para Sommerville/Data
Feminism, seguir com conhecimento geral consolidado desses textos
(conceitos amplamente documentados/citados: capítulos de Sociotechnical
Systems e Requirements Engineering do Sommerville; o enquadramento de
poder em coleta de dados do Cap. 2 de Data Feminism), **sinalizando
explicitamente no `index.qmd` que não é citação literal verificada
contra a página do livro** (regra de precisão de conteúdo do
`CLAUDE.md`) até que o PDF real esteja disponível.

## Plano de aula — Aula 4 (carga horária nominal: ~60–70min)

> Mesmo padrão das Aulas 1–2 (nominal ~50min, cresce se o professor
> aprofundar exemplos "na prática"): esta aula tem 2 blocos técnicos
> centrais (Conway + Requisitos), então arredondei a estimativa um
> pouco acima do nominal-base da disciplina. Candidatos naturais a
> cortar ao vivo, se a carga real for menor: o detalhamento de exemplos
> "na prática" do Bloco 5, não a estrutura dos 6 blocos.

1.  **Abertura — Um sistema quebrado por comunicação, não por código**
    (~8 min) — Organizador prévio: a Aula 3 tratou responsabilidade
    como algo que um profissional individual carrega (seguir ou não um
    código). Hoje perguntamos: e quando o problema não está em nenhuma
    decisão individual, mas na própria estrutura de como o time se
    organiza para construir o sistema? Revisão rápida do mapa de atores
    da Aula 1. **Roteiro explícito** (4 perguntas que a aula responde):
    (i) por que a arquitetura de um sistema tende a copiar o
    organograma de quem o construiu; (ii) levantar requisitos é um ato
    neutro de "descobrir o que o cliente quer", ou um processo social
    com voz e poder desiguais; (iii) como um compromisso ético/social
    abstrato (ex.: acessibilidade, privacidade) se transforma em algo
    concreto no código e no processo de desenvolvimento; (iv) que
    decisões de processo (quem participa, como decisões são revisadas)
    mudam o resultado técnico final. Problema motivador: um caso real
    de sistema fragmentado/inconsistente entre módulos, rastreável a
    times que não se comunicavam — a se confirmar/detalhar na Etapa 3
    (busca de um caso documentado; o próprio artigo de Conway (1968)
    provavelmente já traz um exemplo concreto de 1968, a checar).
    Pausa ativa fechando o bloco.

2.  **Intuição — O Mapa de Papéis da Indústria** (~10 min) — Antes de
    formalizar, mostrar concretamente quem participa da construção de
    um sistema de software real (PM/PO, dev, QA, UX, operações/SRE,
    stakeholders de negócio, usuário final) e por onde um pedido
    "simples" do usuário passa antes de virar código — cada passagem é
    uma tradução, e cada tradução perde ou adiciona algo. Isso já
    entrega a intuição de que "requisito" não é um dado bruto, é o
    produto de uma cadeia de pessoas — falta só nomear os dois
    mecanismos formais (Blocos 3–4).

3.  **A Lei de Conway: Premissas e Passo a Passo** (~15 min) — Bloco
    central 1. Premissas: (a) construir uma interface entre duas partes
    de um sistema exige comunicação entre quem constrói cada parte; (b)
    organizações minimizam custo de comunicação alinhando equipes a
    subsistemas. Passo a passo: (i) se dois módulos interagem mas os
    times que os constroem não se falam, a interface entre eles tende a
    ficar malfeita/inconsistente; (ii) para reduzir esse custo, a
    organização (consciente ou não) tende a alinhar a fronteira dos
    times à fronteira dos módulos; (iii) resultado: a arquitetura do
    sistema, no fim, espelha o organograma — não por design técnico
    deliberado, mas por pressão estrutural de comunicação; (iv)
    implicação prática — a "Manobra Inversa de Conway": para mudar a
    arquitetura de um sistema de forma duradoura, muitas vezes é preciso
    mudar primeiro a estrutura do time, não só o código.

4.  **Elicitação de Requisitos como Processo Social** (~15 min) — Bloco
    central 2. Reenquadrar o processo clássico de Engenharia de
    Requisitos do Sommerville (elicitação → análise → especificação →
    validação) como uma sequência de decisões sociais, não uma extração
    neutra: quem é entrevistado como "o usuário" (e quem não é);
    requisitos de grupos sem poder de voz no processo tendem a ficar
    implícitos ou de fora da especificação formal; conectar com o
    enquadramento de Data Feminism (Cap. 2) sobre como a coleta de
    dados/requisitos já embute estruturas de poder existentes, antes de
    qualquer modelo ou código ser escrito.

5.  **Da Responsabilidade Social ao Artefato de Engenharia Concreto**
    (~15 min) — Fechar o "gap" entre principío e prática: um exemplo
    guiado, passo a passo, de como um compromisso social/ético abstrato
    (ex.: "o sistema deve ser acessível a usuários com baixa visão")
    se traduz em (i) um Requisito Não-Funcional específico e testável;
    (ii) uma decisão de arquitetura registrada (ADR) que o implementa;
    (iii) uma porta de processo (checklist de revisão de PR, gate de
    CI) que impede regressão. Reconectar com a Lei de Conway do Bloco 3:
    se não existe *nenhum* time/pessoa responsável por essa fronteira,
    o requisito tende a "cair no buraco" entre equipes, do mesmo jeito
    que uma interface técnica sem dono cai.

6.  **Fechamento e Ponte para a Aula 5** (~8 min) — Retomar as quatro
    perguntas da abertura, uma frase cada. O que fica em aberto: hoje
    vimos que decisões de processo/organização têm consequência técnica
    e social — mas essa consequência também é **material**: a Aula 5
    (Parte 2 do curso, "Computação e Seus Impactos") mostra que
    decisões de arquitetura (ex.: quantos serviços, onde rodam) têm
    também um custo ambiental e energético real, não só organizacional.
