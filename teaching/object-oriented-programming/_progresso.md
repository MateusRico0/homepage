# Progresso — Object-Oriented Programming

Estrutura conforme `CLAUDE.md`, com uma diferença importante desta
disciplina em relação às outras 4 já publicadas: a fonte primária não são
livros de terceiros lidos do zero, e sim o **material de aula já ministrado
pelo próprio professor** (`_fontes/material/`, símlink para
`Disciplinas/Programação Orientada a Objetos/1s2026/material`) — LaTeX/Beamer
com blocos `\begin{article}` (prosa/notas) e `\begin{frame}` (slides), já
citando os 5 livros-base. `_fontes/` também tem symlinks para os 5 livros
(`weisfeld.pdf`, `bloch.pdf`, `metz.pdf`, `arnold-gosling.pdf`, `eckel.pdf`).

**Achado desta sessão:** o usuário tinha esquecido de adicionar `_fontes/`
numa rodada anterior; quando adicionou, os 5 PDFs foram colados como cópia
real (não symlink) — violação direta da regra do `CLAUDE.md` contra
versionar PDF de direitos autorais no git. Corrigido: 3 dos 5 livros já
existiam em `Disciplinas/.../1s2025/Livros/`; os outros 2 (Arnold & Gosling,
Eckel) foram movidos para lá; todas as cópias no repositório foram apagadas
e substituídas por symlinks. A pasta `material/` (idêntica a
`Disciplinas/.../1s2026/material`) também virou symlink.

**Decisão do usuário sobre o processo:** para as 12 aulas desta disciplina,
o usuário dispensou explicitamente a aprovação em cada etapa (plano →
fontes → aula completa) — diferente do fluxo padrão do `CLAUDE.md` para as
outras disciplinas. Também pediu que o código apareça de forma proeminente
nas aulas ("em orientação a objetos é melhor mostrar os códigos"), já que é
o cerne do assunto.

**Sem chunks de código executável (Python/Jupyter) nesta disciplina** — os
exemplos são blocos de código Java estáticos (com destaque de sintaxe),
como já eram no material original. Diagramas de memória (Stack/Heap,
primitivos vs. referências) usam TikZ, adaptados dos `tikzpicture`
originais, recoloridos com a paleta do IC.

**Divergência entre planejamento e material real, ainda não resolvida
totalmente:** o `index.qmd` da disciplina tinha sido escrito (por outra
sessão) como 12 "Lessons" sequenciais, mas o `planejamento.tex` real do
curso é mais rico — duas trilhas por semana (10 Aulas Teóricas + 10 Aulas
Práticas do projeto "UniShop") — e a Aula 1 teórica real, sozinha, já
cobre o equivalente a quase 2 das 12 Lessons originalmente esboçadas.
A entrada da Lesson 1 no `index.qmd` já foi atualizada para bater com o
que a Aula 1 real entrega; as Lessons 2–12 **ainda não foram conferidas**
contra os arquivos `Teoria/Aula N.tex` correspondentes — isso deve ser
revisto aula a aula, à medida que cada uma for construída, não de uma vez
só.

## Aula 1 — O Paradigma Orientado a Objetos e a Máquina Java

Funde as duas sessões teóricas originais (`Teoria/Aula 1.1.tex` — "O
Paradigma Orientado a Objetos" — e `Aula 1.2.tex` — "Orientação a Objetos
em Java") numa aula só, mantendo a mesma sequência e os mesmos exemplos
(o `Produto` do supermercado).

- [x] `_00-plano-aula.md` — 10 blocos (~140 min, sessão dupla): TRUE/custo
      de mudança, paradigma procedural vs. OO, Estado/Comportamento/
      Identidade/Encapsulamento, Classe vs. Objeto, JVM/Bytecode/JIT,
      memória (Stack/Heap/GC/alcançabilidade/try-with-resources), anatomia
      da classe em código (`Produto` construído incrementalmente),
      modificadores de acesso e `this`/sombreamento, primitivos vs.
      referências (com prova da reatribuição). **Corte consciente:**
      Docker/DevContainer/Maven, presentes na segunda metade de
      `Aula 1.2.tex`, foram deixados de fora — é conteúdo de ambiente de
      desenvolvimento, não de Orientação a Objetos, sem paralelo nas
      outras 9 aulas.
- [x] `_01-fontes.md` — fontes primárias são os próprios `.tex` da aula
      (trechos citados literalmente deles, não dos livros); citações aos 5
      livros-base foram herdadas como já estavam no material original,
      **não reconferidas página a página** nesta sessão (diferente do
      padrão de offset-verificado das outras disciplinas) — registrado
      como pendência caso algum dia seja necessário.
- [x] `index.qmd` — escrito sem chunks Python/Jupyter (código Java estático
      em blocos ```` ```java ````); 2 diagramas TikZ (cópia de primitivo,
      cópia de referência/"controle remoto"), adaptados dos `tikzpicture`
      do material original com paleta do IC. 3 pausas ativas + 3 testes
      V/F com resposta separada, intercalados ao longo da aula (padrão
      `callout-tip` com o tema como título, mesmo padrão maduro já usado
      em `supervised-learning`). Exercícios: 3 discursivas + 12 blocos de
      V/F de 4 itens (curados a partir dos ~35 blocos de 3 itens e 18
      discursivas somados dos dois arquivos `.tex` de origem). Validado
      com `quarto render --to html` e `--to revealjs` (kernel
      `~/Documents/Research/sensible-deep-moo/code/.venv`, mesmo usado nas
      outras disciplinas) — sem erro; sequência de slides conferida via
      extração de headings (nenhum duplicado, todo V/F com sua Resposta
      logo depois).
- [x] Etapa 5 (`index.qmd` da disciplina) — entrada da Lesson 1 atualizada
      e linkada para `./aula01/index.qmd`, com título e descrição batendo
      com o conteúdo real (não precisou de aprovação explícita, por
      decisão do usuário para esta disciplina).

## Aula 2 — O Objeto como Máquina de Estados

Fonte: `Teoria/Aula 2.tex`. Cobre struct passivo vs. agente ativo, o
anti-padrão do Modelo Anêmico, a máquina de estados finita (DFA) mapeada
para atributos/métodos (com diagrama de estados do `Produto` em TikZ),
invariantes (do laço à classe), o construtor como base de indução
(Fail-Fast), CQS, Design by Contract, o kit de exceções padrão, e o
contrato `equals()`/`hashCode()`. `_00-plano-aula.md`, `_01-fontes.md` e
`index.qmd` escritos; validado com `quarto render --to html` e
`--to revealjs`, sem erro; 3 pausas ativas + 3 testes V/F confirmados via
extração de headings; Exercícios com 3 discursivas + 12 blocos de V/F de 4
itens. `index.qmd` da disciplina atualizado (Lesson 2 relinkada e
redescrita para bater com o conteúdo real).

## Aula 3 — Composição de Sistemas: Contratos e Estabilidade

Fonte: `Teoria/Aula 3.tex` — cujo título e conteúdo reais **divergem** do
resumo de `planejamento.tex` para "Aula 3" ("O Contrato do Objeto, Escopo
e Identidade"); o `.tex` real trata de outra coisa (colaboração entre
objetos, interface vs. implementação, Lei de Demeter, Tell-Don't-Ask,
Plug-and-Play) — usado como fonte de verdade, não o resumo do
planejamento. `_00-plano-aula.md`, `_01-fontes.md` e `index.qmd`
escritos; validado nos dois formatos. **Achado de processo:** a primeira
versão só tinha 2 dos 3 testes V/F mínimos intercalados nos slides —
corrigido adicionando um terceiro na seção de Plug-and-Play antes de
finalizar. `index.qmd` da disciplina atualizado (Lesson 3 relinkada e
redescrita — o assunto real não tem nada a ver com "Scope, Lifecycle, and
Identity" do esboço original).

## Aula 4 — Decomposição e Responsabilidade

Fonte: `Teoria/Aula 4.tex`. Cobre a Classe Deus (`Pedido` com 5
responsabilidades), coesão/acoplamento, SRP + Teste do "E", refatoração
via DI/delegação (`Pagavel` + `ServicoEmail`), a Teoria do Ator de Robert
Martin, a métrica LCOM, os riscos opostos de fragmentação excessiva
(Cirurgia de Espingarda) e Modelo Anêmico, os três tipos de associação
(Dependência/Agregação/Composição), e Delegação fechando o ciclo com a
Lei de Demeter da Aula 3. `_00-plano-aula.md`, `_01-fontes.md` e
`index.qmd` escritos; validado nos dois formatos. **Mesmo achado de
processo da Aula 3:** a primeira versão só tinha 2 dos 3 pares de teste
V/F mínimos — corrigido adicionando um terceiro (Delegação/Tell-Don't-Ask)
antes de finalizar; confirmado por extração de headings. `index.qmd` da
disciplina atualizado (Lesson 4 relinkada e redescrita).

**Nota:** o `Aula 4.tex` já cobre boa parte do que a Lesson 5 original
("Delegation and Coupling") previa (DI, delegação) — a Aula 5 real
(`Aula 5.tex`, ainda não lida) provavelmente cobre interfaces
formalizadas e JUnit, não só delegação básica; conferir ao chegar lá.

## Aula 5 — Acoplamento e Contratos

Fonte: `Teoria/Aula 5.tex`. Cobre o falso desacoplamento (associação via
construtor não garante desacoplamento lógico), Feature Envy e a cura
*Move Method*, a métrica CBO, a Escala de Myers (Conteúdo/Comum/Estampa/
Dados) com um exemplo de código por nível, GRASP/Especialista na
Informação, e o Princípio da Inversão de Dependência (DIP) resolvendo o
"pesadelo da expansão" de `Cliente` com `if/else` para cada meio de
pagamento. Termina com um gancho explícito para Polimorfismo/Interfaces
na Aula 6 — mantido como tal na conclusão do `index.qmd`.
`_00-plano-aula.md`, `_01-fontes.md` e `index.qmd` escritos; validado nos
dois formatos, 3 pares de V/F confirmados de primeira (sem o erro das
Aulas 3–4). `index.qmd` da disciplina atualizado (Lesson 5 relinkada e
redescrita — desta vez o assunto real bateu bem com "Delegation and
Coupling" do esboço original, só ficou mais rico: métricas CBO/Myers,
GRASP e DIP não estavam previstos).

## Aula 6 — Interfaces e o Contrato de Comportamento

Fonte: `Teoria/Aula 6.tex` (primeira metade — arquivo real tem 1241
linhas, cobrindo o equivalente a 2 aulas do site). Cobre Interface como
Contrato de Comportamento (`Pagavel`/`Pix`), Interfaces Modernas
(`default`/`static`/`private`, o padrão "Mutador Cego"), Interface vs.
Classe Abstrata, Tipos como comportamento (não DNA), e Exceções como
Guardas de Contrato (Fail-Fast, erro de silenciar, try-catch,
`Notificavel`/`EstrategiaDesconto`/`ServicoLogistico`).
`_00-plano-aula.md`, `_01-fontes.md` e `index.qmd` escritos; validado
nos dois formatos. **Mesmo achado de processo de novo:** faltou o
terceiro par de V/F na primeira passada — adicionado na seção de
Interfaces Modernas antes de finalizar. `index.qmd` da disciplina
atualizado (Lesson 6 relinkada e redescrita).

**Nota de numeração:** como `Aula 6.tex` virou duas aulas do site (esta e
a próxima, sobre Polimorfismo/Generics), a contagem final de aulas da
disciplina deve passar de 12 — o número final só fica claro depois de
ler todos os `Teoria/Aula N.tex` restantes.

## Aula 7 — Polimorfismo, Binding e Generics

Fonte: `Teoria/Aula 6.tex` (segunda metade). Cobre Polimorfismo e Late
Binding, a taxonomia de Cardelli-Wegner (Universal: Inclusão/Paramétrico;
Ad-hoc: Sobrecarga/Coerção), a tabela Static vs. Dynamic Binding, o fim
do "Mar de IFs" com o OCP, e Generics (raw types → etiqueta de tipo em
compilação). `_00-plano-aula.md`, `_01-fontes.md` e `index.qmd`
escritos; validado nos dois formatos. **Mesmo lapso de novo:** só 2 pares
de V/F na primeira versão — corrigido com um terceiro na seção de OCP.
`index.qmd` da disciplina atualizado: essa Lesson 7 **substituiu**
"Inheritance and the Substitution Principle" (empurrada para a Aula 8,
ainda não escrita) — a numeração das Lessons 8+ do esboço original ainda
não foi reconciliada com o conteúdo real; isso será feito de uma vez só
depois de ler `Teoria/Aula 7.tex`, `8.tex`, `9.tex` e `10.tex`, em vez de
ir ajustando lesson a lesson.

## Aula 8 — Herança: DNA, Fragilidade e Template Method

Fonte: `Teoria/Aula 7.tex` (primeira metade, linhas 1–740 de 1583 —
arquivo real também vira duas aulas do site). Cobre a mecânica de
`extends`/DNA compartilhado, a fragilidade de invariantes sem `final`, o
Problema da Classe Base Frágil (bug de contagem dupla), critério
herança-vs-composição (DNA + necessidade polimórfica), invariantes
invisíveis (ordem, retorno, `super`), a base como guardiã (`private` +
`final` + *hooks*), Classes Abstratas (metáfora do chassi), Herança de
Estado vs. Comportamento, e Template Method (Princípio de Hollywood).
`_00-plano-aula.md`, `_01-fontes.md` e `index.qmd` escritos; validado
nos dois formatos. **Mesmo lapso pela terceira vez:** só 2 pares de V/F
na primeira versão — adicionado um terceiro (Template Method) antes de
finalizar; considerar, nas próximas aulas, já escrever os 3 pares de
cara em vez de corrigir depois. `index.qmd` da disciplina atualizado:
Lesson 8 agora é esta aula (Herança), empurrando "Polymorphism and
Abstract Classes" do esboço original para dentro do conteúdo real
(Polimorfismo já virou a Aula 7; Classes Abstratas entraram aqui).

**Checkpoint de escopo (após 8 aulas):** a disciplina já passou de 12
para pelo menos 15-16 aulas reais, porque `Aula 6.tex` e `Aula 7.tex`
(fontes) são densos o bastante para virar 2 aulas do site cada. Ainda
faltam ler `Aula 7.tex` (segunda metade: Liskov + exceções
estruturadas), `Aula 8.tex`, `9.tex` e `10.tex` — todos ainda não
conferidos, podem ter o mesmo padrão de densidade.

## Conformidade retroativa — Aulas 7 e 8 (2026-08-30)

Sessão dedicada a trazer `aula07/index.qmd` e `aula08/index.qmd` para
conformidade com a versão atual do `CLAUDE.md` (regras de Pausa Ativa e
de Exercícios maturadas depois que essas duas aulas foram escritas).
Escopo estritamente esses dois arquivos — `aula01`–`aula06` ficaram de
fora (sendo tratadas em paralelo por outra sessão) e nenhum diagrama
TikZ existe em nenhuma das duas aulas (`grep -c '{.tikz'` = 0 em ambas),
então não havia trabalho de diagrama a fazer.

**1. Pausas Ativas (3 por aula) — estrutura unificada.** Nas duas
aulas, cada pausa tinha a pergunta motivadora num `callout-tip`
compartilhado (correto), mas o V/F condutor vivia num bloco
`content-visible when-format="revealjs"` separado, com itens em
formato solto `a. Texto.`/`b.`/`c.`/`d.` (sem glifo) — violando a regra
de que o V/F condutor deve aparecer identicamente em notas E slides, só
a resolução ficando exclusiva do RevealJS. Corrigido nas 6 pausas (3 +
3): mesclado pergunta motivadora + V/F condutor num único
`callout-tip` compartilhado (título = a pergunta, itens em `- □
Texto.`), seguindo o padrão maduro de
`supervised-learning/aula01/index.qmd`. A Resposta (mantida exclusiva
do RevealJS) foi convertida de `a. **Verdadeiro** — ...` para `- ✔
Texto — justificativa.` / `- ✗ Texto — justificativa.`, com um
fragmento final "Voltando à pergunta" sintetizando a resposta à
pergunta motivadora, também seguindo o padrão maduro.

**2. Exercícios (12 blocos × 4 itens = 48, por aula) — formato e
conteúdo.** Wrapper trocado de `::: {.callout-tip}` para `:::
{.callout-note icon=false}` nos 24 blocos (12 por aula); itens
convertidos de `a. ( ) Texto.` para `- □ Texto.` em todos os 96 itens.
As 6 questões discursivas (3 por aula) já estavam corretas, não foram
tocadas.

**Reescrita de itens que violavam a metodologia de V/F do
`CLAUDE.md`** (paráfrase literal de frase da aula, ou pergunta
definicional "X é Y", proibidas pela seção "Metodologia de criação de
cada item de V/F"): 10 itens na Aula 7 (blocos "O que é Polimorfismo"
item a; "Late Binding" itens a,b; "Polimorfismo Universal" itens a,c,d;
"Polimorfismo Ad-hoc" itens a,c,d; "Binding Estático vs. Dinâmico" item
a) e 17 itens na Aula 8 (blocos "Herança como Identidade" item c; "O
Modificador `protected`" item c; "O Problema da Classe Base Frágil"
item a; "Herança por Conveniência" itens a,c; "Invariantes Invisíveis"
itens a,c,d; "Herança de Estado vs. Comportamento" itens a,b; "Template
Method: o Esqueleto" item b; "Inversão de Controle" itens a,b,d;
"Vantagens e Riscos do Template Method" itens a,b; "Síntese" item b).
Cada reescrita manteve o tema original do item, mas passou a nascer de
uma das 4 heurísticas exigidas (Contrafactual, Limite, Transferência,
Falsa dicotomia) — normalmente convertendo uma frase quase idêntica ao
texto da aula (ex.: "Polimorfismo é a capacidade de uma variável ou
método assumir comportamentos diferentes...", cópia quase literal da
definição no corpo do texto) num cenário concreto e testável (ex.:
"Duas classes que implementam métodos com o mesmo nome, mas sem
relação de herança ou interface comum entre elas, já caracterizam
polimorfismo..." — Falso, testando Falsa Dicotomia). Os `git diff`
completos de `aula07/index.qmd` e `aula08/index.qmd` documentam o
antes/depois exato de cada item.

**Arquivos novos criados** (primeira resolução destes itens — nunca
haviam sido resolvidos antes nesta disciplina): `aula07/_02-solucoes.md`
e `aula08/_02-solucoes.md` (48 entradas cada, heurística + resposta +
justificativa por item, seguindo o formato de
`supervised-learning/aula01/_02-solucoes.md`); `aula07/_03-respostas-pausas.md`
e `aula08/_03-respostas-pausas.md` (discussão em prosa de cada pergunta
motivadora + V/F resolvido com glifos ✔/✗, seguindo o formato de
`unsupervised-learning/aula01/_03-respostas-pausas.md`).

**Validação.** (1) `quarto render index.qmd --to html` e `--to
revealjs` nas duas aulas: zero erros; únicos avisos são pré-existentes
e não relacionados (`WARN: Unable to read listing item description...`
de outras disciplinas). (2) Checador de balanceamento de `:::` (pilha
LIFO, escrito para esta sessão): zero erros, pilha vazia ao final, nas
duas aulas. (3) `grep '☐\|☒\|- \[ \]\|- \[x\]\|( )'` em `index.qmd`,
`_02-solucoes.md` e `_03-respostas-pausas.md` das duas aulas: nenhuma
ocorrência. (4) Contagem programática no `notas.html` renderizado
(`_site/`): 12 blocos `callout-note`, 4 itens `□` por bloco (48 no
total), 3 itens na lista de questões discursivas — em ambas as aulas.
(5) Comparação de texto entre `notas.html` e `slides.html` renderizados:
os 12 itens `□` de cada pausa (3×4) aparecem verbatim em ambos os
formatos; `✔`/`✗` aparecem só no `slides.html` (12 ocorrências),
nunca no `notas.html` (0 ocorrências) — confirmando que a resolução
nunca vaza para as notas publicadas.

**Achado não relacionado ao escopo desta sessão, verificado e não é
específico desta disciplina:** o campo `date: today` do YAML virou
`date: "2026-08-30"` (data literal) em `aula07`/`aula08`. Verificação
adicional (sessão supervisora) confirma que isso **não é uma anomalia
isolada** — todas as 8 aulas desta disciplina (incluindo as que nenhum
agente desta rodada tocou ainda) e ao menos uma aula de cada outra
disciplina do site (`supervised-learning`, `optimization-linear-algebra`,
`unsupervised-learning`) têm o mesmo `date: "2026-08-30"` literal.
É claramente um processo automatizado de todo o site (provável
candidato: o `homepage-preview.service` persistente), não algo
introduzido por esta sessão — não precisa de reversão nem investigação
específica desta disciplina.

## Auditoria de conformidade com o `CLAUDE.md` atual — Aulas 1–8 (2026-08-31)

A pedido do usuário ("revise todas as aulas de orientação a objetos sob
o novo claude.md"), auditei e corrigi as 8 aulas já construídas contra
as regras atuais do `CLAUDE.md` (essa disciplina foi construída sob uma
versão anterior das regras). Trabalho feito via 4 agentes em paralelo
(2 aulas cada), com verificação independente minha depois de cada um.

**Gaps encontrados, uniformes nas 8 aulas:**
1. Pausas ativas: o V/F condutor (4 itens) estava isolado só nos slides
   (deveria aparecer igual nas notas) e usava `a./b./c./d.` sem glifo;
   a Resposta usava `**Verdadeiro**`/`**Falso**` em vez de `✔`/`✗`.
2. Exercícios: os 12 blocos de V/F usavam `callout-tip` + `a. ( )` em
   vez de `callout-note icon=false` + `- □`.
3. Nenhuma aula tinha `_02-solucoes.md` nem `_03-respostas-pausas.md`.
4. Aulas 1–2 (únicas com diagramas TikZ): dimensionamento via atributos
   de fence (`{.tikz .nostretch .center width="N%"}`), que não têm
   efeito nenhum — corrigido para o wrapper `.fig-resize` (mesmo
   mecanismo real já usado nas outras disciplinas do site).

**Correção:** todos os 4 pontos acima corrigidos nas 8 aulas,
preservando o código Java e o conteúdo pedagógico original. Vários
itens de V/F que eram paráfrase quase literal de uma definição da aula
(proibido pelo `CLAUDE.md`) foram reescritos para nascer de uma das 4
heurísticas exigidas (Contrafactual, Limite, Transferência, Falsa
dicotomia) — ver os `_progresso.md` por aula (entradas anteriores desta
sessão) para o antes/depois de cada rewrite.

**Falhas de sessão durante o processo:** os 4 agentes atingiram o
limite de sessão (reset 4:10am) antes de terminar completamente —
retomei manualmente o que faltava: 2 itens de V/F faltantes em
`aula02/_02-solucoes.md` (bloco "Estado, Comportamento e Identidade
(revisitados)", itens c/d) e o arquivo `aula04/_03-respostas-pausas.md`
inteiro (nunca chegou a ser criado). `aula03/_03-respostas-pausas.md`
parecia truncado por ter poucas linhas (33, vs. ~100 nas outras) mas
na verdade estava completo — só era mais denso (menos linhas em
branco); falso alarme, não precisou de correção.

**Bug no meu próprio checador de balanceamento de `:::`:** a versão
usada nas sessões anteriores só reconhecia abertura de div com chaves
(`::: {.classe}`), não a forma abreviada do Pandoc sem chaves (`:::
columns`) — isso gerou um falso positivo de erro de balanceamento em
`aula02/index.qmd` (linha 496). Corrigido o checador para tratar
qualquer `:::` seguido de conteúdo não-vazio como abertura,
independente de chaves; reconfirmado zero erros reais nas 8 aulas.

**Achado de infraestrutura, não específico desta auditoria:** os
arquivos `notas.html`/`slides.html` aparecem e desaparecem sozinhos
direto nas pastas `aulaNN/` (fora de `_site/`) — confirmado que não são
produzidos pelos meus comandos `quarto render` (que sempre escrevem em
`_site/`); é algum processo de preview em segundo plano específico
desta disciplina, pré-existente a esta sessão. Não removido — parece
ser parte do fluxo de trabalho local do professor para esta disciplina
especificamente (diferente das outras 4 disciplinas do site, que não
têm esse comportamento).

**Validação final (sessão supervisora, independente dos 4 agentes):**
render completo (`--to html` e `--to revealjs`) das 8 aulas, checado
imediatamente após cada render para evitar corrida com o processo de
preview em segundo plano — zero erros/warnings relevantes. Balanço de
`:::` limpo nas 8 aulas (checador corrigido). `grep`
`☐|☒|- \[ \]|- \[x\]|( )` limpo em todos os `index.qmd`,
`_02-solucoes.md` e `_03-respostas-pausas.md`. Contagem de `□`
confirmada em `_site/`: 60 por aula nas notas (48 exercícios + 12
pausas), 12 nos slides (só pausas — Exercícios é exclusivo de notas,
como o `CLAUDE.md` exige); `✔`/`✗` confirmados só nos slides (12 por
aula), zero nas notas, nas 8 aulas. 48/48 entradas em cada
`_02-solucoes.md` confirmadas.

## Aulas 9–12+ (numeração provisória)

Não iniciadas. Cada uma deve ser conferida contra o `Teoria/Aula N.tex`
correspondente em `_fontes/material/` antes de escrever — não presumir que
a Lesson N já esboçada no `index.qmd` da disciplina bate 1:1 com o
conteúdo real da Aula N do material, nem que o resumo de `planejamento.tex`
bate com o `.tex` real (já divergiu na Aula 3). Ao terminar cada aula,
conferir também se ela precisa de pelo menos 3 pares de teste V/F
intercalados nos slides antes de dar a aula por concluída (a Aula 3 quase
saiu com só 2).
