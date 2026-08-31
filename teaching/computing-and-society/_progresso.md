# Progresso — Computing and Society

Estrutura conforme `CLAUDE.md`: `index.md` é o planejamento do semestre;
cada aula é `aulaNN/` com `00-plano-aula.md`, `01-fontes.md`, `02-aula.qmd`.
Fontes em `fontes/`: `CSV1.pdf`, `CSV2.pdf`, `CSV3.pdf` (Maciel & Viterbo,
2020, 3 volumes), `EthEng.pdf` (Van de Poel & Royakkers, 2011), `EthTech.pdf`
(Steen, 2022).

**Diferença estrutural desta disciplina:** é humanidades/ética, não STEM.
Por decisão do usuário, o `.qmd` não usa chunks de código Python/simulação
— só prosa (HTML/RevealJS via `content-visible`). Sem `exemplos-estilo/`
ainda (as outras disciplinas são todas STEM; não fazem sentido como
referência de tom aqui — considerar usar a própria Aula 1 como exemplo
depois de aprovada, como já feito nas outras disciplinas).

**Atualização (2026-08-24): Mermaid → TikZ.** A decisão original acima
("diagramas Mermaid para modelos conceituais") foi revista a pedido
explícito do usuário — os diagramas da Aula 3 foram convertidos para
TikZ, alinhando esta disciplina com a convenção já usada nas disciplinas
STEM (ver `../CLAUDE.md`, seção "Sugestão de fluxogramas e diagramas").
Esta nota substitui a decisão anterior; novas aulas desta disciplina
devem usar TikZ, não Mermaid, para diagramas.

## Aula 3: conversão de diagramas para TikZ + slides mais completos (2026-08-24)

- **6 diagramas Mermaid convertidos para TikZ** (3 conceitos, cada um
  com uma versão para as notas HTML e uma condensada para os slides):
  linha do tempo do caso BART; "quantas profissões o Brasil regula"
  (cadeia com um ramo tracejado destacando a Informática); comparação
  Landon & Landon vs. Ciclo Ético. As duas últimas passaram de layout
  vertical (`flowchart TB`, sem cores) para **horizontal, com paleta
  clara** (tons pastéis das cores do IC — azul, laranja, verde-água,
  vermelho —, texto preto em vez de branco sobre fundo saturado),
  pedido explícito do usuário visando legibilidade em slides projetados.
- **Bug real encontrado e corrigido: `step` é uma palavra reservada do
  TikZ/pgf** (usada para espaçamento de grade, ex. `grid[step=1cm]`).
  Nomear um estilo customizado `step/.style={...}` faz o pgfkeys tentar
  interpretar `[step]` como essa chave nativa, que "requer um valor" —
  o estilo é silenciosamente ignorado, o nó perde toda formatação
  (cor, tamanho mínimo, alinhamento), e o resultado colapsa numa caixa
  de proporção degenerada (larga e quase sem altura). Diagnosticado
  compilando o trecho TikZ isoladamente com `pdflatex` fora do pipeline
  Quarto/Pandoc até isolar o erro exato (`pgfkeys Error: The key
  '/tikz/step' requires a value`). Corrigido renomeando o estilo para
  `tlbox`. Lição para diagramas futuros: evitar nomes de estilo que
  colidam com chaves nativas do TikZ (`step`, `above`, `below`, `left`,
  `right`, `node`, etc. são candidatos arriscados).
- **Segundo problema, não relacionado, encontrado no caminho:** os
  nós usavam posicionamento relativo (`right=Xmm of nome`, da
  biblioteca `positioning`) em vez de coordenadas absolutas — resultou
  em todos os nós colapsando na origem ("aglomerado de caixas",
  relatado pelo usuário). Os diagramas já validados nesta disciplina
  (e nas disciplinas STEM) nunca dependem de `positioning`; usam
  coordenadas explícitas `at (x,y)` ou a árvore nativa do TikZ
  (`child{...}`). Corrigido convertendo todos os nós para `at (x,y)`
  explícito — mais verboso, mas não depende de nenhuma biblioteca extra
  estar carregada no pipeline de renderização.
- **Terceiro problema, também no caminho:** o estilo de seta usava
  `>=Stealth` (exige a biblioteca `arrows.meta`), que não está
  confirmada como carregada neste pipeline; causava o erro visualmente
  enganoso `pgf@stop` aparecendo como texto literal no diagrama.
  Corrigido removendo `>=Stealth`, usando só `->` simples — o mesmo
  padrão já usado nos diagramas validados das disciplinas STEM.
- **Cache duplo, útil de saber para depuração futura:** além do cache
  normal do Quarto (`index_files/`, por aula), o filtro
  `pandoc-ext/diagram` mantém um cache próprio, persistente e fora do
  projeto, em `~/.cache/pandoc-diagram-filter/` (chaveado pelo conteúdo
  do diagrama). Ao depurar um diagrama que parece "não atualizar" apesar
  de mudanças no `.qmd`, limpar os dois caches, não só `index_files/`.
- **Slides "mais completos"** (feedback direto do usuário): revisão de
  densidade em 3 pontos identificados como abaixo do padrão das notas
  HTML — "Mapeando a Formação da Computação no Brasil" (histórico do
  Bloco 4, ganhou a citação de página e o elo com a regulamentação dos
  anos 1970), "O Elo Fica Completo" (fechamento do Bloco 3, caixa
  desnecessária removida), e principalmente "O Que Fica Desta Aula"
  (fechamento da aula inteira — reescrito para retomar explicitamente
  as 3 perguntas do "plano de hoje" da abertura, uma a uma, seguindo o
  padrão de fechamento do `CLAUDE.md`, que antes só existia nas notas
  HTML, não nos slides).
- Revalidado com `quarto render --to html` e `--to revealjs`, sem
  erro nem warning; balanço de divs conferido por script; dimensões
  dos 6 SVGs gerados conferidas uma a uma (proporções plausíveis,
  nenhuma caixa degenerada).

## Achado importante: citação quebrada no `index.md`

A leitura recomendada original de **três aulas** (1, 7, 13) citava "Maciel
& Viterbo (2020), Vol. 2, Capítulo 2: Análise Cultural de Sistemas
Computacionais" — **capítulo que não existe**. Confirmado pelo sumário
real dos dois volumes: o Vol. 2 não tem Capítulo 2 (a numeração continua
do Vol. 1, começa no Cap. 9); o Capítulo 2 do Vol. 1 é sobre pós-graduação,
sem relação com o tema.

- **Corrigido no `index.md`** (a pedido explícito do usuário, que também
  autorizou usar `EthTech.pdf` como suporte adicional): substituído pelo
  Cap. 10 real do Vol. 2 ("Cultura na Prática da Computação", Salgado &
  Leitão, pp. 46–80) — mais próximo tematicamente — e adicionado Steen
  (2022), Cap. 3 "Is Technology a Neutral Tool?" como leitura
  complementar à Aula 1.
- **Aulas 7 e 13:** mesma citação quebrada, corrigida também (mesmo
  substituto), mas **sem verificar se o Cap. 10 de fato serve para essas
  aulas** — só resolvido o erro factual, não a adequação de conteúdo.
- **Achado extra, ainda não corrigido:** a leitura de Steen citada na
  Aula 7 ("Chapter 2: Ethics of Consequences") também parece errada — o
  Cap. 2 real do EthTech é "What do we mean with ethics?"; o mais próximo
  do título citado é o Cap. 9 "Consequences and outcomes" (p. 67).
  Sinalizado no `index.md`, não resolvido — assunto de quando chegarmos
  na Aula 7.

## Aula 1 — Computing as a Socio-Technical System

- [x] `00-plano-aula.md` — 5 blocos, **50 min** (não ~105 min como no
      rascunho inicial — correção de orçamento de tempo feita pelo
      usuário na segunda rodada). Núcleo: o mapa de atores (Van de Poel &
      Royakkers §1.6) recebeu o maior bloco (15 min) por ser o que a
      competência esperada do `index.md` pede de fato.
- [x] `01-fontes.md` — 8 fontes (Van de Poel & Royakkers Cap. 1 + Steen
      Cap. 3), todas com trecho literal extraído e verificado (offset de
      página confirmado por leitura direta, não assumido: +14 no EthEng,
      +9 no EthTech a partir do Cap. 3 — **atenção**, o offset do EthTech
      não é constante no livro inteiro, há uma página de abertura de
      parte não numerada que desloca o offset em 4 páginas em algum ponto
      antes do Cap. 3). Maciel & Viterbo Cap. 10 está na leitura
      recomendada mas **não foi lido** — o plano se sustentou inteiramente
      nas outras duas fontes.
- [x] `02-aula.qmd` — escrito nesta sessão, sem código Python (só prosa +
      2 diagramas Mermaid: mapa de atores recriando a Figura 1.6 de Van
      de Poel & Royakkers, e o *feedback loop* de algoritmos de redes
      sociais). Validado com `quarto render --to html` e `--to revealjs`,
      sem erro.

## Etapa 5 — index.md

Link da Aula 1 adicionado (não existia nenhum antes). Mesmo padrão das
outras disciplinas: `../../society/aula01/notas.html` (+ Slides).

## Aula 2 — What is Ethics, and The Ethical Cycle

- [x] `00-plano-aula.md` — 5 blocos, ~50 min nominais (nota explícita no
      próprio plano: conteúdo de texto/slides é mais profundo do que cabe
      em 50 min falados, igual à Aula 1).
- [x] `01-fontes.md` — 29 fontes (Van de Poel & Royakkers Caps. 3 e 5,
      Steen Cap. 16), passou por **duas rodadas**: a segunda incorporou
      feedback do usuário — trocou o exemplo de conflito de normas
      kantiano (trabalho infantil/IKEA, considerado ruim) pelo exemplo já
      do livro (provas de alunos vs. amigo) + o assassino à porta de Kant
      (sinalizado como externo ao livro-base); aprofundou ética do
      cuidado; usou o Ford Pinto como caso central atravessando três das
      quatro teorias, mostrando profundidade revertendo conclusões dentro
      de cada teoria (não só entre teorias); adicionou provocações de
      fim de subseção (nos slides) usando Study/Discussion Questions do
      próprio livro (pp. 107–108); expandiu "quando voltar" no Ciclo
      Ético em três mecanismos nomeados, com honestidade explícita sobre
      quais são citação literal do livro (Seta 2) vs. reconstrução nossa
      (Setas 1 e 3).
- [x] `02-aula.qmd` — sem código Python, só prosa + Mermaid. Passou por
      **duas rodadas completas**: a primeira gerou o conteúdo inicial; a
      segunda (pedido explícito do usuário: "recomece desde
      planejamento, mas não precisa das minhas intervenções") reescreveu
      substancialmente os Blocos 2, 3 e 5 incorporando todo o feedback
      listado acima, sem parar para aprovação intermediária. Corrigido
      também um bug de numeração de seções (`###` pulando `##`, gerando
      "3.0.1" em vez de "3.1" no sumário). Validado com
      `quarto render --to html` e `--to revealjs`, sem erro, div-balance
      verificado por script Python a cada rodada.
- [x] Etapa 5 (`index.md`) — **ainda não feita**, pendente aprovação do
      usuário sobre o conteúdo final desta segunda rodada.

### Nota de infraestrutura: `output-dir` do `_quarto.yml`

Durante esta rodada, `content/teaching/_quarto.yml` foi encontrado com
uma alteração não commitada: `output-dir` mudou de `"../../static/"`
para `"../../teaching/static/"`. Perguntado ao usuário, que confirmou
**manter** o novo valor. Efeito prático: a partir desta rodada, os
HTMLs renderizados da Aula 2 foram gravados em
`mraimundo/teaching/static/society/aula02/` (novo local), não mais em
`mraimundo/static/society/aula02/` (local antigo, usado pela Aula 1 e
pelas primeiras renderizações da própria Aula 2 nesta sessão — ficou
com uma cópia desatualizada, não removida). Se o Hugo do site espera os
HTMLs em `mraimundo/static/`, os links do `index.md` (Etapa 5) e a
publicação real do site podem quebrar até que a Aula 1 e as outras
disciplinas também migrem para o novo caminho, ou até o `_quarto.yml`
volte ao valor antigo — vale confirmar com o usuário antes de publicar.

## Aula 3 — Computing, Its Domains, and Professional Responsibility

- [x] `_00-plano-aula.md` — reestruturado em 2 rodadas nesta sessão
      (2026-08-25): (1) reordenação em 6 blocos (BART → códigos
      concretos → conselho+LGPD/GDPR → regular ou não [Brasil+mundo] →
      limites → fechamento); (2) a pedido do usuário, a partir dos
      slides de uma versão anterior da disciplina: Dez Mandamentos
      removidos ("são bem tocos"), ACM Code e IEEE-CS/ACM Code
      aprofundados (cláusulas numeradas + gloss "na prática", citados
      como fonte primária/oficial), LGPD/GDPR fundida ao bloco de
      conselho de profissão (duas formas de regulação judicializada),
      autorregulação-para-evitar-regulação explicitada no bloco de
      limites (caso Tozer). Framework de Ruggiero avaliado e
      **descartado por decisão do usuário** (não está em nenhuma fonte
      da disciplina).
- [x] `_01-fontes.md` — 17 fontes dos livros-texto + fontes
      primárias/legais sinalizadas como tal (ACM Code, IEEE-CS/ACM SE
      Code, Lei 13.709/2018 Art. 6º) + fontes web da comparação
      internacional (NCEES, Engineers Canada, BCS).
- [x] `index.qmd` — reescrito por completo nesta sessão, com Exercícios
      (3 discursivas + 12 blocos de V/F, seguindo a metodologia de
      heurísticas do `../CLAUDE.md`) e 4 exercícios de checagem
      intercalados nos slides (um por bloco, Blocos 2–5). **Bug
      encontrado e corrigido:** um `::: {.fig-resize}` aninhado
      diretamente dentro de um `::: {.fragment}`, precedido de `<br/>`,
      faz o Reveal.js/Pandoc perder o fechamento do div (o texto do
      fence e as aspas do atributo `style` leakam como texto literal,
      com aspas convertidas para curly quotes pelo smart-quotes — sinal
      de que o div não foi reconhecido). Ocorria em exatamente 2 dos 9
      usos de `.fig-resize` nos slides (os 2 que estavam aninhados
      dentro de um `.fragment`; os que ficam no nível do slide, fora de
      fragment, não têm o problema). **Corrigido fundindo as duas
      classes num único div** (`::: {.fragment .fig-resize style="..."}`)
      em vez de aninhar dois divs — mesmo efeito visual (revelação
      progressiva + redimensionamento), sem a combinação problemática.
      Lição para diagramas futuros nesta e em outras disciplinas: não
      aninhar `.fig-resize` dentro de `.fragment` como dois divs
      separados; usar um único div com as duas classes.
- [x] `_02-solucoes.md` — justificativa dos 48 itens de V/F (12 blocos
      × 4), com heurística nomeada por item.
- Validado com `quarto render --to html` e `--to revealjs` (usando
  `--output-dir` para um diretório de teste, já que o pipeline normal
  do projeto não deixou os `.html` renderizados no lugar esperado do
  código-fonte — investigar isso separadamente se for bloquear alguma
  tarefa futura). Sem warning, sem erro, balanço de divs conferido por
  script.
- **Pendente:** Etapa 5 (link no `index.md` da disciplina) — só depois
  de aprovação do usuário sobre o conteúdo final desta rodada.

## Renumeração do semestre (2026-08-30)

A pedido do usuário, uma nova Aula 4 ("Human, Social, and Ethical
Dimensions of Software Engineering") foi inserida no `index.qmd` entre
a Aula 3 (atual) e a antiga Aula 4 ("Architecture, Energy, and the
Material Cost of Digital Infrastructure") — usuário escolheu
explicitamente **inserir**, não substituir. Todas as aulas 4–15
antigas foram renumeradas +1 (agora 5–16); nenhuma pasta `aulaNN/`
precisou ser renomeada, pois só `aula01`–`aula03` existiam até aqui.
**Correção em cascata:** a Aula 3 já construída/aprovada tinha, em duas
passagens (notas e slides), uma ponte de fechamento dizendo "A Aula 4
abre a Parte 2... custo material e ambiental" — isso ficou factualmente
errado com a nova Aula 4 (que continua na Parte 1). Corrigido nas duas
passagens de `aula03/index.qmd` para apontar a ponte imediata para a
nova Aula 4 (engenharia de software como prática sociotécnica) e só
depois, na Aula 5, para a Parte 2.

## Aula 4: Human, Social, and Ethical Dimensions of Software Engineering

- Etapa 1 (identificação) confirmada pelo usuário — texto completo do
  `index.qmd` (objetivos, competências, leituras) fornecido por ele.
- Etapa 2: `_00-plano-aula.md` criado — 6 blocos, ~60–70min nominal
  (mesmo padrão de Aulas 1–2), sem rótulo de Estratégia A/B (convenção
  já não usada nesta disciplina humanidades/não-STEM).
- **Fontes ausentes resolvidas (2026-08-30), a pedido do usuário
  ("Pode seguir para buscar os materiais sozinho"):**
  - Conway (1968), "How Do Committees Invent?": PDF completo baixado
    do site oficial do autor (melconway.com/Home/pdf/committees.pdf,
    3.081.567 bytes, confirmado via `Content-Length`) e symlinkado em
    `_fontes/conway1968.pdf`.
  - D'Ignazio & Klein (2020), *Data Feminism*, Cap. 2: edição de
    acesso aberto da MIT Press, baixada de um mirror legítimo hospedado
    pela Rutgers University (`sites.rutgers.edu/critical-ai/`) e
    symlinkada em `_fontes/datafeminism_cap2.pdf`.
  - **Primeira tentativa de symlink usou caminho relativo com
    profundidade errada (`../../../` em vez de caminho absoluto) e
    ficou quebrado silenciosamente** — Bash confirmou com `ls -la`
    (mostra o link "existindo"), mas `readlink -f`/`cat` revelaram que
    o destino não existia. Corrigido usando caminho absoluto, igual à
    convenção já usada pelos outros symlinks de `_fontes/` desta
    disciplina. **Lição:** sempre confirmar um symlink novo com
    `readlink -f` ou lendo o arquivo de verdade, não só com `ls -la`.
  - Ian Sommerville, *Software Engineering* (10ª ed.): **nenhuma fonte
    gratuita legítima encontrada** — as únicas cópias completas
    online são não autorizadas (ex.: PDF do livro comercial hospedado
    em `archive.org` sob o acervo de outro curso universitário);
    decidi não usar. Blocos 2 e 4 usam conhecimento geral consolidado
    desses capítulos, sinalizado como tal no `index.qmd`, sem citação
    literal.
  - Todos os trechos literais extraídos e documentados em
    `aula04/_01-fontes.md`, incluindo uma correção de ementa (Steen,
    "Chapter 5: Value Sensitive Design and Responsible Innovation" não
    existe no livro real — são dois capítulos distintos, 18 e 19).
- Etapa 3 (fontes) concluída.

## Aula 4: `index.qmd` completo, exercícios e pausas construídos (2026-08-30)

- **`index.qmd` escrito por completo** (2100 linhas), 6 blocos do
  `_00-plano-aula.md`, seguindo a Estratégia B-like sem rótulo formal
  (convenção de humanidades desta disciplina): Abertura (caso
  COBOL/ALGOL de Conway) → Mapa de Papéis da Indústria (sinalizado como
  conhecimento geral, sem citação literal de Sommerville) → Lei de
  Conway (premissas + Manobra Inversa) → Elicitação de Requisitos como
  Processo Social (Data Feminism + caso DGEI) → Da Responsabilidade
  Social ao Artefato Concreto (VSD de Steen + cadeia NFR→ADR→gate de
  CI) → Fechamento e ponte para a Aula 5. Todos os 7 trechos citados de
  `_01-fontes.md` traduzidos para português ("tradução livre") no
  `index.qmd`, nunca deixados em inglês.
- **2 diagramas TikZ**, cada um com versão para notas (maior, mais
  legendas) e versão condensada para slides (`.fragment .fig-resize`
  fundidos num único div, seguindo a lição já registrada na Aula 3):
  (a) Lei de Conway — dois painéis lado a lado (equipes que se
  comunicam → interface bem definida; equipes que não se comunicam →
  interface inconsistente), redesenho da ideia do artigo, não
  reprodução literal de nenhuma figura de Conway; (b) cadeia
  compromisso ético → NFR testável → ADR → gate de CI, com uma caixa de
  alerta conectando de volta ao mecanismo da Lei de Conway ("requisito
  cai no buraco sem dono da fronteira").
- **6 pausas ativas** (uma por bloco, incluindo Abertura e Fechamento —
  cobertura mais completa que a Aula 3, que só tinha 4, nos Blocos
  2–5), cada uma com Pergunta Motivadora + dica (idêntica em notas e
  slides) e V/F de 4 itens com `□`; resposta nos slides com `✔`/`✗`
  reexibindo a pergunta motivadora, conforme `../CLAUDE.md`. Discussão
  completa das 6 perguntas + resolução dos 24 itens em
  `aula04/_03-respostas-pausas.md` (novo).
- **Exercícios**: exatamente 3 discursivas + 12 blocos de V/F (48
  itens), cobrindo a aula de ponta a ponta (papéis da indústria, Lei de
  Conway — premissas/manobra/caso concreto, requisitos como processo
  social, Data Feminism, caso DGEI, processo do Sommerville, VSD,
  cadeia NFR/ADR/CI, conexão Conway+requisito sem dono, síntese/ponte
  para a Aula 5). Todo item construído a partir de uma das 4
  heurísticas do `../CLAUDE.md` (contrafactual/limite/transferência/
  falsa dicotomia), nenhuma pergunta definicional. Justificativa dos 48
  itens em `aula04/_02-solucoes.md` (novo).
- **Bug real encontrado e corrigido: `<br/>` imediatamente seguido de
  `::: {.callout-tip icon=false}` sem linha em branco entre eles faz o
  Pandoc engolir a fence de abertura como texto/HTML bruto**, deixando
  o `:::` de fechamento correspondente sem par — ele sobra como texto
  literal `<p>:::</p>` no HTML renderizado. Diferente do bug já
  registrado na Aula 3 (`.fig-resize` aninhado em `.fragment` como dois
  divs separados — aqui os dois já estavam corretamente fundidos em um
  só). Ocorria em exatamente 1 dos vários usos de `<br/>` seguido de
  fence no arquivo (bloco de resposta do diagrama da Lei de Conway nos
  slides). Diagnosticado isolando com `pandoc -f markdown -t html`
  puro (sem os filtros do Quarto) e buscando por `:::` literal no HTML
  de saída — biseção rápida, sem precisar rodar o pipeline completo a
  cada tentativa. Corrigido inserindo uma linha em branco entre o
  `<br/>` e a fence seguinte. **Lição para diagramas/callouts futuros
  nesta e em outras disciplinas:** nunca deixar um `<br/>` colado
  (sem linha em branco) imediatamente antes de uma fence de abertura
  `::: {...}` — o problema não é o aninhamento em si (fundir classes já
  resolve o caso da Aula 3), é a ausência de linha em branco separando
  HTML bruto de uma fence nova.
- **Achado de infraestrutura, não relacionado a esta aula:** durante a
  validação, `quarto render` falhou no projeto inteiro com
  `FilesystemLoop: Too many levels of symbolic links`, apontando para
  `publications/ahmoliveira/*.qmd` — dois arquivos com `git status`
  modificado (não committado), evidentemente de uma sessão concorrente
  trabalhando em outra parte do site ao mesmo tempo. Não toquei nesses
  arquivos (fora do escopo desta tarefa). Contornado criando um
  `_quarto.yml` local temporário em `aula04/` (`project: type:
  default` + só o filtro `diagram`, sem os filtros `participants.lua`/
  `links.lua`, irrelevantes para uma aula) e um symlink local
  `_extensions -> ../../../_extensions`, para que o Quarto tratasse
  `aula04/` como raiz de projeto isolada e não precisasse enumerar o
  projeto inteiro (onde estava o link quebrado). **Os dois — o
  `_quarto.yml` temporário e o symlink `_extensions` — foram removidos
  depois da validação**; não fazem parte do commit desta aula. Se o
  link quebrado em `publications/ahmoliveira/` ainda existir numa
  sessão futura, o mesmo contorno serve.
- **Validado:** `quarto render --to html` e `--to revealjs`, sem erro
  nem warning (após o fix do `<br/>`); balanço de divs `:::` conferido
  por script Python (LIFO, incluindo contagem de colchetes por linha);
  ausência de `☐`/`☒`/`- [ ]` confirmada por grep; 3 discursivas + 12
  blocos de 4 itens de V/F (48 total) confirmados por contagem
  programática a partir do `index.qmd` e novamente no `notas.html`
  renderizado (seção "Exercícios" sobrevive ao render, com
  subseções 7.1–7.3 no sumário); termos-chave (Lei de Conway, COBOL,
  Data Feminism, contra-dados, DGEI, Value Sensitive Design) presentes
  em ambos `notas.html` e `slides.html`; nenhum trecho em inglês restou
  sem tradução (todas as 7 fontes citadas aparecem só com "tradução
  livre" no `index.qmd`) — corrigido no caminho um slide que usava só a
  sigla "VSD" sem nunca expandir "Value Sensitive Design" por extenso
  nos slides (adicionado).
**Etapa 5 concluída (2026-08-30):** usuário aprovou ("pode seguir e
fechar"). Entrada da Lesson 4 no `../index.qmd` convertida de texto
simples para link: `* [**Lesson 4: Human, Social, and Ethical
Dimensions of Software Engineering**](./aula04/index.qmd)`. Aula 4
encerrada.

**Verificação independente (2026-08-30, sessão supervisora):**
reconferi os 7 itens de validação do agente — todos confirmados
(balanço LIFO limpo, glifos limpos, 72 ocorrências de `□` = 48 dos
Exercícios + 24 das 6 pausas ativas, `output-file` correto, aviso de
não-literalidade do Sommerville presente e bem colocado no Bloco 2,
nenhum trecho em inglês sobrou, 4 diagramas TikZ renderizados como SVG
com proporções plausíveis). **Limpeza:** o agente deixou `notas.html`,
`slides.html` e um `.gitignore` residuais direto em `aula04/` (deveriam
existir só em `_site/`, como em toda outra aula do projeto) — removidos.
**Achado importante, fora do escopo desta aula:** o `quarto render`
do projeto inteiro está **quebrado agora** por um symlink circular real
em `publications/mraimundo/best-practices-for-responsible-machine-learning-in-credit-sc.qmd`
(aponta para `../mraimundo/` do próprio diretório, resolvendo pra si
mesmo — confirmado com `readlink -f`, não é falso positivo). Os
arquivos correspondentes em `publications/ahmoliveira/` aparecem como
modificados no `git status`, sinal de que outra sessão está com
trabalho em andamento ali — não toquei nesses arquivos. Isso bloqueia
qualquer `quarto render` na raiz do projeto até ser corrigido (por
quem estiver com esse trabalho em andamento), incluindo o preview
automático do site. Vale avisar o usuário.

## Correções na Aula 4 (2026-08-31), a pedido do usuário

Feedback do usuário: "a aula está um pouco quebrada" + pedido para
explicar papéis e elicitação de requisitos com mais cuidado antes dos
aspectos sociais. Dois problemas reais encontrados e corrigidos:

**1. Bug estrutural/glifo nas 6 pausas ativas** (não percebido na
verificação anterior, que só checava a contagem agregada de `□`, não
onde cada um estava): cada pausa tinha o Pergunta+V/F duplicado — uma
vez nas notas (`content-visible html unless-format=revealjs`, com `□`
correto) e de novo, reescrito, só nos slides (`content-visible
revealjs`, usando `a./b./c./d.` sem glifo nenhum — o mesmo formato
antigo já corrigido em `object-oriented-programming` nesta sessão).
Corrigido nas 6 pausas: removida a duplicata revealjs-only do
Pergunta+V/F (agora um único bloco compartilhado, sem
`content-visible`, usando `□`), mantida só a Resposta como
revealjs-only, convertida de `a. ✔ Texto` para `- ✔ Texto` (lista com
glifo, não letra solta).

**2. Conteúdo raso em papéis e elicitação de requisitos, antes da
virada social** — Bloco 2 (Mapa de Papéis) tinha uma tabela de papéis
sem explicar por que essa divisão existe; Bloco 4 (Elicitação) nomeava
as 4 etapas clássicas (Sommerville) em uma frase e já pulava para "cada
etapa esconde uma decisão social", sem nunca explicar o que cada etapa
faz de fato. Adicionado: no Bloco 2, um parágrafo sobre por que a
especialização em papéis existe (raciocínios genuinamente diferentes —
negócio, percepção humana, corretude, falha em escala) e uma coluna de
"Artefato que produz" na tabela; no Bloco 4, uma explicação mecânica
completa das 4 etapas com técnicas reais (elicitação: entrevistas,
*workshops*, etnografia, protótipos descartáveis; análise/negociação:
MoSCoW, modelo de Kano, matrizes de trade-off; especificação: casos de
uso, histórias de usuário com critérios de aceite; validação: revisões
estruturadas, *walkthroughs*, protótipos de baixa fidelidade) — só
depois disso a pergunta social ("quem participa, quem fica de fora de
cada atividade concreta") é apresentada. Espelhado nos slides com
fragmentos equivalentes (1 slide novo em cada bloco).

**Validação:** balanço de `:::` limpo (script LIFO); `grep`
`☐|☒|- \[ \]|- \[x\]|^[a-d]\. ` limpo; `quarto render --to html` e
`--to revealjs` sem erro; termos novos (MoSCoW, Kano) confirmados
presentes em ambos os HTMLs renderizados; contagem de `Exercícios`
confirmada intacta (não afetada por essas edições, que ficaram todas
antes da seção de Exercícios).

## Aulas 5–16

Não iniciadas.
