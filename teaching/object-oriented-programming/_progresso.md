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

## Conformidade com o `CLAUDE.md` novo (consolidação de arquivos + anti-picotamento) — Aulas 1–8 (2026-09-03)

A pedido do usuário ("refaça todas as aulas de orientação a objetos com
essas novas diretivas", aprovação por etapa dispensada explicitamente),
as 8 aulas já publicadas foram atualizadas para o `CLAUDE.md` reescrito
nesta sessão. Trabalho feito via 4 agentes em paralelo (2 aulas cada),
com verificação independente minha (leitura de disco + re-render de
todas as 8 aulas nos dois formatos) depois.

**1. Consolidação de arquivos de apoio (4→2 por aula).** `_00-plano-aula.md`
+ `_01-fontes.md` → `_00-planejamento.md` (Resumo / Plano de aula / Fontes
usadas, template da Etapa 2 do `CLAUDE.md`); `_02-solucoes.md` +
`_03-respostas-pausas.md` → `_01-respostas.md` (Gabarito V/F + Respostas
das Pausas Ativas). Conteúdo preservado integralmente em todas as 8 —
cada agente conferiu por diff/contagem antes de apagar os 4 arquivos
antigos com `rm`. Nenhum conteúdo pedagógico do `index.qmd` foi alterado
por este passo; a contagem de 12 blocos de V/F por aula (acima da nova
faixa recomendada de 6–10 do `CLAUDE.md`) foi mantida como está — a
faixa nova é orientação para aulas futuras, não uma obrigação de cortar
conteúdo já aprovado.

**2. Passada anti-picotamento nos slides.** Aplicada a todas as 8 aulas
pela primeira vez (regra nova desta sessão). Slides genuinamente finos —
quase sempre um bloco de código isolado sem nenhum comentário próprio,
cujo comentário morava só no slide vizinho — foram fundidos, apagando
o `## heading` intermediário (nunca os `:::` dos fragmentos). Total: 9
merges em 6 das 8 aulas (aula01: 0 — já estava consistente; aula02: 2;
aula03: 1; aula04: 2; aula05: 1; aula06: 1; aula07: 2; aula08:
verificado pelo agente antes de uma interrupção, resultado íntegro
conforme validação minha abaixo). Nenhum slide foi sobre-fundido; casos
ambíguos (comparações antes/depois com código nos dois lados, pares
pergunta/resposta de pausa ativa) foram deixados como estavam por já
carregarem um ponto de aterrissagem substancial cada.

**3. Validação final (minha, independente dos 4 agentes).** Um dos 4
agentes (aula08) parou após consolidar os arquivos e editar o
`index.qmd`, mas sem confirmar os renders finais (relatou que ficaria
"esperando" um lock do `.quarto` liberar e encerrou sem retomar) —
completei a verificação eu mesmo: checador de balanceamento de `:::`
limpo, `quarto render --to html` e `--to revealjs` bem-sucedidos.
Depois, re-renderizei as 8 aulas inteiras (`--to html` e `--to
revealjs`, uma de cada vez) para descartar qualquer regressão cruzada —
`aula03 --to html` falhou na primeira tentativa por uma corrida
conhecida no cache `.quarto/project-cache` compartilhado entre renders
concorrentes (mesmo sintoma relatado por vários agentes durante o
trabalho paralelo), e teve sucesso limpo na segunda tentativa, sem
nenhuma mudança de arquivo. Todas as 16 renderizações (8 aulas × 2
formatos) confirmadas limpas ao final, sem erros nem avisos.

## Aula 9 — Substituição e Falha: o Princípio de Liskov e a Taxonomia de Exceções

Fonte: `Teoria/Aula 7.tex`, **segunda metade** (linhas 759–1411 de
1582 — a Aula 8 já havia consumido 1–758). Cobre três blocos reais:
(1) um recap compacto de Late Binding/VTable/`@Override` como
preservação de contrato (subtipagem e substituibilidade, o protocolo
de despacho de 4 passos, `@Override` como guarda sintático, não
semântico); (2) o **Princípio da Substituição de Liskov** — definição
formal ($\forall x{:}T,\phi(x)\implies\forall y{:}S,\phi(y)$), as três
regras de contrato (pré-condições não fortalecidas, pós-condições não
enfraquecidas, invariantes preservadas), o paradoxo Círculo-Elipse
(com diagrama TikZ da bifurcação de violação), e contratos de exceção
como quarta forma de violar o LSP; (3) **taxonomia de exceções** — erro
como transição de estado prevista, árvore de falhas por domínio
(diagrama TikZ de hierarquia), captura polimórfica, tradução/wrapping
preservando a causa original, e o critério Checked (Mundo) vs.
Unchecked (DNA/Fail-Fast).

**Decisão de escopo (uma aula, não duas):** apesar do trecho-fonte
cobrir três tópicos, o bloco de Late Binding/VTable é majoritariamente
recapitulação/aprofundamento mecânico de conteúdo já lançado nas Aulas
7 (Late Binding) e 8 (Classe Base Frágil, Composição sobre Herança já
tratadas em profundidade) — não precisou do mesmo peso de um bloco
inteiramente novo. Com esse bloco comprimido, o total estimado (~130
min) ficou dentro da faixa 90–140 min já calibrada pelas 8 aulas
publicadas, então não houve necessidade de dividir em aula09+aula10
como aconteceu com `Aula 6.tex` e a primeira metade de `Aula 7.tex`.
**Nada ficou pendente para uma futura aula10 a partir deste
trecho-fonte** — o arco Herança→LSP→Exceções de `Aula 7.tex` está
totalmente coberto entre a Aula 8 e esta Aula 9.

`_00-planejamento.md`, `index.qmd` e `_01-respostas.md` escritos, já
no formato consolidado de 2 arquivos de apoio adotado nesta sessão
para as Aulas 1–8 (ver entrada acima). **Diagramas TikZ (3, novos
nesta aula):** despacho de VTable (cadeia referência → objeto no Heap
→ VTable → método executado), bifurcação do paradoxo Círculo-Elipse
(`setAxes(10,20)` força violar a natureza do objeto ou a expectativa
do cliente), e árvore de hierarquia de exceções de domínio
(`LojaException` → Infraestrutura/Negócio → especialistas) — todos com
a paleta IC (`icblue`/`icorange`/`icred`) e wrapper `.fig-resize`,
seguindo o padrão já usado nas Aulas 1–2.

**Exercícios:** 3 discursivas + **9 blocos** de V/F de 4 itens (36
itens) — dentro da nova faixa flexível do `CLAUDE.md` (6–10 blocos),
calibrado pela densidade real desta aula (três subtemas, mas o
primeiro comprimido), não esticado até o teto da faixa só para bater
uma cota. Todos os itens são originais (nenhum reaproveitado verbatim
do `\section*{Exercícios de Fixação}` do próprio `.tex`, cujos ~25
blocos de V/F são majoritariamente definicionais — formato que o
`CLAUDE.md` desta disciplina proíbe explicitamente); os temas desses
blocos-fonte serviram só de inspiração temática, registrado em
`_00-planejamento.md`.

**Achado de processo (correção durante a sessão):** o item (b) do
bloco "Taxonomia do Erro e Captura Polimórfica" foi escrito
inicialmente com uma afirmação mal formada (descrevia a ordem
*correta* de captura — específica antes de genérica — mas alegava que
essa ordem "perdia" a reação específica, o oposto do que essa ordem
garante). Corrigido para testar o comportamento real e verificável do
compilador Java (código inalcançável/erro de compilação quando o
`catch` genérico vem antes do específico), mantendo a heurística de
Caso Limite. Identificado por um script de verificação cruzada entre
os itens `- □` do `index.qmd` e o campo **Afirmação** de
`_01-respostas.md` (comparação de texto exato), que também confirmou
as demais 35 correspondências.

**Validação:** checador de balanceamento de `:::` (pilha LIFO): zero
erros, pilha vazia. `quarto render --to html` e `--to revealjs`: ambos
"Output created", sem erros/avisos relevantes (só os avisos padrão do
Inkscape na conversão TikZ→SVG, já vistos nas Aulas 1–2). Contagem
programática: 48 `□` em `notas.html` (36 exercícios + 12 pausas), 12
`□` em `slides.html` (só pausas, antes da resolução); `✔`/`✗`: 0 em
`notas.html`, 12 em `slides.html` (9 verdadeiros + 3 falsos,
distribuídos 3+1 em cada uma das 3 pausas). Revisão de picotamento nos
headings `##` do bloco RevealJS: 1 ajuste feito durante a construção
(fundido "O Problema: Vazamento de Detalhe Técnico" — um único
fragmento — com o slide seguinte "A Solução: Wrapping", que continuava
a mesma ideia). `index.qmd` da disciplina atualizado: a Lesson 9 antiga
("Breaking Contracts (Exceptions)", esboço genérico desatualizado) foi
substituída pelo título e descrição reais desta aula.

## Aulas 10–12+ (numeração provisória)

Depois de `aula09`, restam ainda inteiros: `Aula 8.tex`, `Aula 9.tex`,
`Aula 10.tex` e `Revisão.tex`, cada um a conferir integralmente antes
de escrever (não presumir que a Lesson N já esboçada no `index.qmd` da
disciplina bate 1:1 com o conteúdo real, nem que o resumo de
`planejamento.tex` bate com o `.tex` real — já divergiu antes). Ao
terminar cada aula, conferir também se ela precisa de pelo menos 3
pares de teste V/F intercalados nos slides antes de dar a aula por
concluída.

## Aula 10 — O Colapso da Herança e a Era da Composição: o Padrão Strategy

Fonte: `Teoria/Aula 8.tex` (1115 linhas — arquivo completo, ao contrário
das Aulas 8–9, que dividiram `Aula 7.tex` ao meio). Cobre as quatro
primeiras seções reais do `.tex`: (1) **A Ilusão e o Custo da Herança**
— a fusão estrutural do `extends`, a "ilusão da produtividade"
(`PedidoInternacional extends Pedido` só para ganhar métodos de graça),
o acoplamento estrutural como o vínculo mais rígido da OO, Herança de
Estado vs. Comportamento, e o peso físico da herança de estado na Heap
(a "Subclasse Gorda", via `Ebook extends ProdutoBase`); (2) **O Colapso
da Hierarquia** — um cenário de e-commerce (`Produto` → `ProdutoFisico`/
`ProdutoDigital` × Nacional/Importado) forçando uma explosão
combinatória de subclasses, e a proibição de herança múltipla de
classes em Java (Problema do Diamante) fechando qualquer saída por
herança; (3) **A Era da Composição e Modularidade** — o princípio do
GoF ("favoreça composição sobre herança"), a virada de *is-a* para
*has-a*, a teoria da quase-decomponibilidade de Herbert Simon, a
analogia eletrodoméstico integrado vs. modular, e os tipos de
composição (Agregação vs. Associação) com o Especialista da
Informação; (4) **O que fazer então?** — o labirinto de `if/else` para
meios de pagamento, a tentativa fracassada por herança
(`PedidoPix`/`PedidoCartao`, confundindo identidade com papel), e a
resolução via padrão **Strategy** (interface `Pagavel`, injeção de
dependência, delegação, topologia Context/Strategy/ConcreteStrategy,
Late Binding/VTable revisitado, e o OCP em ação).

**Decisão de escopo (divide em aula10 + aula11 futura):** `Aula 8.tex`
tem 1115 linhas, comparável em tamanho a `Aula 6.tex` e `Aula 7.tex`,
ambos já divididos em duas aulas do site cada. As quatro seções usadas
nesta aula formam um arco fechado (problema → princípio → solução
nomeada) que já soma ~125–135 min estimados (dentro da faixa 90–140 já
calibrada) — as duas seções finais do `.tex` (`Padrões de Projeto`,
linhas 806–917: origem histórica/Christopher Alexander, o marco GoF de
1994, o que padrões NÃO são, o vocabulário arquitetural, e a visão
geral das três famílias; e `Conclusão`, linhas 917–943) ficaram de fora
e são o ponto de partida exato de uma **Aula 11** futura. Nada do arco
Herança→Composição→Strategy ficou pendente: só o vocabulário geral de
padrões (que não depende de nada não visto ainda) migrou para a Aula
11.

**Reaproveitamento deliberado de nomenclatura.** A interface `Pagavel`
e as classes `Pix`/`Cartao`/`Boleto`, já usadas nas Aulas 8–9 como
**subclasses** de `MeioPagamentoBase`, foram reaproveitadas nesta aula
como implementações independentes de `Pagavel` injetadas por
composição/Strategy — não é coincidência de nomes, é o contraste
pedagógico central da aula: o mesmo domínio, resolvido de duas formas
estruturalmente diferentes. Por causa disso, o bloco de Fragile Base
Class (já coberto em profundidade na Aula 8 via `GerenciadorDeCobrancas`
e o bug de contagem dupla) foi tratado apenas como referência breve
nesta aula — o ângulo novo é o custo físico de memória da herança de
estado (Subclasse Gorda) e a explosão combinatória, nenhum dos dois já
visto antes.

`_00-planejamento.md`, `index.qmd` e `_01-respostas.md` escritos, no
formato consolidado de 2 arquivos de apoio já em uso desde a Aula 9.
**Diagramas TikZ (3, novos nesta aula):** a matriz de explosão
combinatória (grid Físico/Digital × Nacional/Importado, com nota do
terceiro eixo levando a 8 classes), a bifurcação do Problema do
Diamante (`Produto` → `ProdutoFisico`/`ProdutoImportado` →
`FisicoImportado` tentando herdar dos dois, marcado como erro de
compilação), e a topologia do padrão Strategy (Context `Pedido` → has-a
→ Strategy `Pagavel` ← implementam ← `Pix`/`Cartao`/`Boleto`) — todos
com a paleta IC (`icblue`/`icorange`/`icred`) e wrapper `.fig-resize`,
seguindo o padrão já usado nas Aulas 1–2 e 9.

**Exercícios:** 3 discursivas + **8 blocos** de V/F de 4 itens (32
itens), dentro da faixa flexível do `CLAUDE.md` (6–10 blocos),
calibrado pelos quatro subtemas reais da aula (fusão/peso da herança,
colapso combinatório, composição/modularidade, Strategy). Todos os
itens são originais (nenhum reaproveitado verbatim do
`\section*{Exercícios de Fixação}` do próprio `.tex`, cujos 25 blocos
de V/F de formato `( )` são majoritariamente definicionais — proibido
pelo `CLAUDE.md` desta disciplina); os temas desses blocos-fonte
serviram só de inspiração temática, registrado em
`_00-planejamento.md`.

**Achado de processo (correção durante a sessão):** um script de
verificação cruzada entre os itens `- □` do `index.qmd` e o campo
**Afirmação** de `_01-respostas.md` (comparação de texto exato)
encontrou 1 divergência: o item (b) do bloco "Composição, Agregação e
Associação" tinha, em `_01-respostas.md`, o texto e o veredito da Pausa
Ativa 2 colados por engano no lugar do item de exercício real (que tem
texto e veredito diferentes — o exercício pergunta se uma dependência
de ciclo de vida faz a relação "deixar de se encaixar" em Associação,
resposta Verdadeiro; a pausa pergunta se a relação "ainda seria
corretamente descrita" como Associação, resposta Falso). Corrigido
substituindo pelo texto e pela justificativa corretos, batendo com o
`index.qmd`; as demais 43 correspondências (32 exercícios + 12 itens de
pausa) foram confirmadas idênticas na primeira passada.

**Revisão de picotamento nos headings `##` do bloco RevealJS:** feita
durante a construção, antes de considerar os slides prontos (não como
retrabalho posterior). 3 ajustes: (1) fundido o slide "A Regra de Ouro
do GoF" (só a citação + 1 frase) com o slide seguinte "Três Razões
Estruturais", que elaborava a mesma ideia; (2) fundido o slide
"Desmembrando a Lógica: `Pedido` Delega" (2 fragmentos curtos, sem
código) com o slide seguinte "Definindo a Fronteira: o Contrato
Abstrato", que continha o código correspondente; (3) fundido o slide de
uma linha só "A Pergunta Certa" como fragmento final do slide anterior
"A Tentativa por Herança: o Colapso da Identidade", por ser o desfecho
direto da mesma ideia, não um ponto de aterrissagem próprio.

**Correção de uma inconsistência entre aulas, fora do escopo original
mas necessária:** o fechamento da Aula 9 (`aula09/index.qmd`, seção
"Ponte para a Aula 10" e o slide "O que Aprendemos") prometia
explicitamente que a Aula 10 traria "Factory Method, Builder e Adapter"
— texto escrito antes de `Aula 8.tex` ter sido lido, presumindo que o
esboço genérico antigo da Lesson 10 (`Creational and Structural
Patterns`) bateria com o conteúdo real. Como o conteúdo real de
`Aula 8.tex` é sobre o colapso da herança e o padrão Strategy (não
sobre padrões de criação), a ponte da Aula 9 foi corrigida para
apontar corretamente para este conteúdo, para não deixar uma promessa
factualmente errada numa aula já publicada. `aula09` re-renderizado nos
dois formatos após a correção — sem erros.

**Validação.** Checador de balanceamento de `:::` (pilha LIFO): zero
erros, pilha vazia, em `index.qmd` (antes e depois dos 3 ajustes de
picotamento). `quarto render --to html` e `--to revealjs`: ambos
"Output created", sem erros (a primeira rodada teve os avisos padrão do
Inkscape na conversão TikZ→SVG, já vistos nas Aulas 1–2 e 9; a segunda
rodada, com os SVGs em cache, não teve nem esses). Contagem programática
no `_site/`: 44 `□` em `notas.html` (32 exercícios + 12 pausas), 12 `□`
em `slides.html` (só pausas, antes da resolução); `✔`/`✗`: 0 em
`notas.html`, 12 em `slides.html` (3 pausas × 4 itens). `grep`
`☐|☒|- \[ \]|- \[x\]` limpo em `index.qmd` e `_01-respostas.md`.
`index.qmd` da disciplina atualizado: Lesson 10 agora aponta para
`./aula10/index.qmd` com título/conteúdo reais (Colapso da Herança e
Composição/Strategy); a Lesson 11 antiga ("Behavioral Patterns:
Strategy and Observer") teve sua descrição ajustada para não mais
prometer Strategy — que já foi ensinado aqui — passando a descrever o
vocabulário geral de Padrões de Projeto (origem, GoF, o que padrões NÃO
são, as três famílias), que é o conteúdo real ainda não escrito das
duas seções finais de `Aula 8.tex`. A Lesson 11 continua sem link (a
aula ainda não foi construída).

## Aula 11 — Padrões de Projeto: Vocabulário, Imutabilidade e a Gênese Segura do Objeto

Fontes: (a) `Teoria/Aula 8.tex`, linhas 806–944 — as duas seções finais
do arquivo, deliberadamente deferidas pela Aula 10: vocabulário geral
de Padrões de Projeto (origem em Christopher Alexander, marco GoF de
1994, o que um padrão explicitamente NÃO é, o vocabulário arquitetural
como linguagem ubíqua, e as três famílias — Comportamento/Estrutural/
Criação); (b) `Teoria/Aula 9.tex` (1180 linhas, lida por completo) —
usado até a linha 590 (Imutabilidade/Value Object) e 591–990 (Criação
Segura: Builder e Factory Method + DIP na criação); a seção
`State Pattern` (linhas 353–590 — nota: o State Pattern efetivamente
começa em 353 e a seção de Criação Segura em 591, ambas lidas na
íntegra para decidir o corte) e a `Conclusão` final (992–1005) ficaram
para a Aula 12.

**Decisão de escopo (aula11 recebe vocabulário + Value Object + Builder
+ Factory Method; State Pattern vai para a Aula 12):** o material
combinado de `Aula 9.tex` (Value Object + State + Builder + Factory
Method) mais o vocabulário de `Aula 8.tex` era claramente denso demais
para uma aula de 90–140 min sem comprimir as derivações principiadas
que o `CLAUDE.md` exige. A divisão seguiu a fronteira que o próprio
esboço da disciplina já sinalizava (Parte 4: "Padrões de Criação e
Estruturais" vs. "Padrões de Comportamento"): esta aula ficou com o
vocabulário geral (que não depende de nada ainda não visto) mais três
padrões de proteção de dado/gênese (Value Object, Builder, Factory
Method), todos de espírito Criacional/Estrutural; o State Pattern,
genuinamente Comportamental e pensado pelo próprio `.tex` de origem
para contrastar diretamente com o Strategy já visto na Aula 10, fica
para a Aula 12. O corte exato na linha 353 de `Aula 9.tex` preserva um
arco fechado nesta aula (vocabulário → dado imutável → objeto que nasce
validado) sem nenhuma dependência pendente — Builder e Factory Method
não citam nem pressupõem State. Carga horária estimada: ~127 min
(dentro da faixa 90–140 já calibrada). **Nada do trecho usado nesta
aula ficou pendente**; o que resta para a Aula 12: o State Pattern
completo e a `Conclusão` de `Aula 9.tex` (que resume os "três pilares"
incluindo State — cabe melhor no fechamento da Aula 12).

**Reaproveitamento/adaptação de nomes.** O Value Object usa `Dinheiro`
diretamente do `.tex` (encaixa naturalmente no domínio: o total de um
`Pedido`). O Builder usa `PedidoBuilder`/`Pedido` diretamente do `.tex`,
sem adaptação — o próprio material de origem já usa o domínio do curso
aqui. O Factory Method e a DIP do `.tex` usam exemplos genéricos
(`NotificacaoFactory`/`Notificacao`, `Servico`/`Database`/`DBFactory`)
sem ligação ao fio condutor de e-commerce; esta aula adapta os nomes
para `NotificacaoPedidoFactory`/`NotificacaoPedido` (notificações de
status de pedido) e `ServicoDePedidos`/`RepositorioPedidos`/
`RepositorioPedidosFactory`, mantendo a mecânica do `.tex` inalterada —
mesma decisão já tomada na Aula 10 ao reaproveitar `Pagavel`/`Pix`/
`Cartao`/`Boleto`.

`_00-planejamento.md`, `index.qmd` e `_01-respostas.md` escritos, no
formato consolidado de 2 arquivos de apoio já em uso desde a Aula 9.
**Diagramas TikZ (3, novos nesta aula):** a árvore de taxonomia das
três famílias de padrões (GoF → Comportamento/Estrutural/Criação →
exemplos, com Strategy já destacado como representante Comportamental
visto na Aula 10); o diagrama de memória comparando *aliasing* (duas
referências Stack apontando para o mesmo `Retangulo` mutável na Heap,
uma mutação corrompendo a outra) com o Value Object (`d1`/`d2`
apontando para instâncias `Dinheiro` distintas, a original intacta); e
o fluxo passo a passo do Builder (`PedidoBuilder` acumulando campos →
`build()` como portão de validação → `Pedido` imutável nascendo ou a
exceção sendo lançada) — todos com a paleta IC (`icblue`/`icorange`/
`icred`) e wrapper `.fig-resize`, seguindo o padrão já usado nas Aulas
1–2, 9 e 10.

**Exercícios:** 3 discursivas + **8 blocos** de V/F de 4 itens (32
itens), dentro da faixa flexível do `CLAUDE.md` (6–10 blocos),
calibrado pelos subtemas reais da aula (vocabulário/famílias,
aliasing, Entidade vs. VO, Obsessão por Primitivos, Builder, Factory
Method, DIP). Todos os itens são originais (nenhum reaproveitado
verbatim do `\section*{Exercícios de Fixação}` de `Aula 9.tex`, cujos
25 blocos de V/F em formato `( )` são majoritariamente definicionais —
proibido pelo `CLAUDE.md` desta disciplina); os temas desses blocos-
fonte serviram só de inspiração temática, registrado em
`_00-planejamento.md`.

**Achado de processo (correção durante a sessão, mesmo padrão já visto
nas Aulas 9–10):** um script de verificação cruzada entre os itens
`- □` do `index.qmd` e o campo **Afirmação** de `_01-respostas.md`
(comparação de texto exato) encontrou, na primeira passada, que os 12
itens `✔`/`✗` de resolução das 3 pausas ativas nos slides haviam sido
**parafraseados** em vez de reaproveitar o texto literal da pergunta
`□` com uma justificativa apenas anexada ao final (o padrão exigido
pelo `CLAUDE.md`: "reescreva cada item trocando `□` pelo glifo
resolvido", mantendo o texto igual). Corrigido nas 3 pausas (12 itens):
cada resolução agora reproduz o texto exato do item `□` correspondente,
com `— justificativa curta` anexado após um travessão, igual ao padrão
já usado nas Aulas 9–10. As 32 correspondências dos blocos de
Exercícios (índice `□` vs. `_01-respostas.md`) estavam corretas desde a
primeira passada.

**Validação.** Checador de balanceamento de `:::` (pilha LIFO): zero
erros, pilha vazia, antes e depois da correção das pausas. `quarto
render --to html` e `--to revealjs`: ambos "Output created", sem erros
nem avisos (avisos padrão do Inkscape na primeira rodada, ausentes na
segunda com os SVGs em cache). Contagem programática no `_site/`: 44
`□` em `notas.html` (32 exercícios + 12 pausas), 12 `□` em
`slides.html` (só pausas, antes da resolução); `✔`/`✗`: 0 em
`notas.html`, 12 em `slides.html` (6 verdadeiros + 6 falsos,
distribuídos entre as 3 pausas). `grep` `☐|☒|- \[ \]|- \[x\]|( )` limpo
em `index.qmd` e `_01-respostas.md`. Revisão de picotamento nos
headings `##` do bloco RevealJS (34 slides extraídos e revisados em
sequência): nenhum merge necessário — o diagrama das três famílias e o
diagrama de *aliasing* já foram construídos com o comentário na mesma
slide da figura (evitando de origem o antipadrão descrito no
`CLAUDE.md`), e os slides mais curtos (ex.: "Revisão: Fail-Fast na
Instanciação", "A Fábrica na Prática", "O `new` como a Cola Mais Forte
do Código") seguem o mesmo padrão já aceito em aulas anteriores de
"código substancial + um fragmento de comentário" como ponto de
aterrissagem válido. `index.qmd` da disciplina atualizado: Lesson 11
agora aponta para `./aula11/index.qmd` com título e conteúdo reais
(vocabulário de padrões, Value Object, Builder, Factory Method/DIP); a
Lesson 12 antiga ("Architectural Pattern — MVC", placeholder genérico)
teve sua descrição ajustada para descrever o State Pattern (conteúdo
real já lido em `Aula 9.tex`, linhas 353–590, mas ainda não escrito),
sem fabricar conteúdo de MVC — que segue sem fonte confirmada até que
`Aula 10.tex` seja lido por uma sessão futura.

## Aula 12 — O Antipadrão do Status, o Padrão State e o Padrão Adapter

Fonte: `Teoria/Aula 9.tex`, seção `State Pattern` (linhas 353–590,
adiada pela Aula 11 por ser Comportamental, não Criacional/Estrutural)
+ `Teoria/Aula 10.tex` (830 linhas antes dos exercícios), lido
integralmente. Cobre: o antipadrão de status-como-primitivo (`String`
verificada no início de cada método do `Pedido`) e sua fragilidade de
evolução; o padrão State (Context/State/ConcreteState) como cura,
delegando `pagar()`/`cancelar()`/`enviar()` para classes de estado
polimórficas; o contraste explícito Strategy vs. State (mesma
topologia, decisão externa vs. auto-mutação interna); onde colocar a
lógica de transição (estados conhecerem o próximo estado vs. tabela
centralizada no Contexto); um ciclo de vida robusto (`EstadoPago`,
`EstadoEnviado`) com regras de negócio via exceção; a motivação e
estrutura do padrão Adapter (tradução de protocolo numa fronteira
externa incompatível, caso de uso de unificação de log com um sistema
legado); Object Adapter vs. Class Adapter (composição vence por
testabilidade e compatibilidade futura); e uma ligação final,
explícita, entre State (fluxo interno) e Adapter (fronteira externa)
coexistindo na mesma classe `EstadoPago`.

**Decisão de escopo (uma aula, não mais):** de `Aula 10.tex`, só as
seções `Introdução e Revisão` (framing, sem conteúdo novo), `Strategy`
(recapitulação breve, já coberta em profundidade na Aula 10 do site) e
`Padrão Adapter` foram usadas. Ficam explicitamente pendentes para
aulas futuras: `O Padrão Decorator e a Composição Dinâmica` (linhas
399–553), `O Padrão Observer e o Desacoplamento de Eventos` (555–743),
e `Síntese Arquitetural e o Estabelecimento de Fronteiras` (745–827) —
esta última lê como o fechamento real do curso (fronteiras
arquiteturais, matriz de decisão, "próximos passos"), não uma aula de
MVC separada; não existe nenhuma seção de MVC em nenhum dos 10
arquivos `Teoria/Aula N.tex` lidos até agora. `index.qmd` da disciplina
atualizado: Lesson 12 agora aponta para `./aula12/index.qmd` com título
e conteúdo reais (State + Adapter); adicionada uma nova Lesson 13
placeholder (`*(not yet written)*`) cobrindo Decorator + Observer, para
não perder esse conteúdo do esboço público — a Síntese Arquitetural
ainda não tem lesson designada, será decidido quando construída.

**Conteúdo construído:** 2 diagramas TikZ (transição de estados do
`Pedido`, camada de tradução do Adapter), 3 pausas ativas, 3
discursivas + 8 blocos de V/F de 4 itens (32 itens), todos originais
pelas 4 heurísticas exigidas.

**Achado de processo — retomada após limite de sessão.** O agente que
construiu esta aula (`_00-planejamento.md` e `index.qmd`) atingiu o
limite de sessão da conta (reset 3h America/Sao_Paulo) antes de
escrever `_01-respostas.md`, rodar a verificação final e atualizar
`index.qmd`/`_progresso.md` da disciplina — retomado manualmente por
mim: escrevi `_01-respostas.md` (32 justificativas de V/F + discussão
das 3 pausas, lendo a resolução já embutida no RevealJS de `index.qmd`
para garantir consistência), e completei os dois updates de arquivo.

**Validação (minha).** Checador de balanceamento de `:::`: zero
erros, pilha vazia (`index.qmd` já estava correto, herdado do agente).
`quarto render --to html` e `--to revealjs`: ambos "Output created",
sem erros (só os avisos padrão do Inkscape na conversão TikZ→SVG).
Contagem programática: 44 `□` em `notas.html` (32 exercícios + 12
pausas), 0 `✔`/`✗`; 12 `□` em `slides.html` (só pausas,
pré-resolução), 12 `✔`/`✗` (resoluções). Único `type="checkbox"`
encontrado em ambos os HTMLs é a regra CSS genérica `ul.task-list li
input[type="checkbox"]` do tema (não um checkbox real renderizado) —
confirmado inofensivo.

## Aula 13 — O Padrão Decorator e o Padrão Observer: Composição Dinâmica e Desacoplamento de Eventos

Fonte: `Teoria/Aula 10.tex`, linhas 399–743 — `\section{O Padrão Decorator
e a Composição Dinâmica}` (399–553) + `\section{O Padrão Observer e o
Desacoplamento de Eventos}` (555–743), lidas na íntegra. Cobre: a
explosão combinatória da herança estática diante de responsabilidades
opcionais e cumulativas (cenário da cafeteria, $2^N$ subclasses); a
estrutura do Decorator (dualidade É-UM/TEM-UM, `Bebida`/`BebidaDecorator`/
`Leite`/`Chocolate`, repasse puro + acréscimo via `super`); o exemplo real
do `java.io` (`BufferedInputStream`/`FileInputStream`) e uma réplica
original no domínio do curso — uma cadeia de notificadores do `Pedido`
(`Notificador`/`NotificadorEmail`/`NotificadorComLog`/`NotificadorComRetry`)
que também evidencia que, ao contrário do custo aditivo da bebida, a
*ordem* das camadas pode mudar o comportamento observável; o perigo do
acoplamento de notificação em cascata (`Pedido` com `EmailService`/
`LogService`/`InventarioService` como dependências diretas, violação do
OCP); a estrutura do Observer (Subject/Observer, `PedidoObserver`/
`PedidoSubject`, registro e broadcast, inversão de controle); as
estratégias de tráfego de dados Push vs. Pull; e a generalização do
Observer local para uma Arquitetura Orientada a Eventos distribuída
(Sujeito→Produtor, callback→Tópicos/Filas, Observador→Consumidor/
microsserviço, Kafka/RabbitMQ).

**Decisão de escopo (aula13 = Decorator + Observer; aula14 = só a
Síntese):** a `\section{Síntese Arquitetural e o Estabelecimento de
Fronteiras}` (linhas 745–827 de `Aula 10.tex`) ficou de fora desta aula
e é o ponto de partida exato de uma **Aula 14** futura — ela lê como o
fechamento/capítulo de síntese do curso (fronteiras núcleo estável vs.
periferia volátil, matriz de decisão comparando os quatro padrões
Strategy/Adapter/Decorator/Observer, e a conclusão "próximos passos"),
não um quinto padrão a ensinar, e pode legitimamente sair mais curta
que as demais aulas sem precisar de conteúdo inventado para
compensar — inclusive porque o próprio `.tex` fecha essa seção
anunciando (incorretamente, à luz do que o site já construiu) "SOLID"
como próximo tema; a Aula 14 deve tratar essa frase de fechamento do
`.tex` como não vinculante, já que este curso já cobriu OCP em
profundidade (Aula 10) e não há necessidade de reabrir SOLID do zero.
Decorator (399–553) e Observer (555–743) formam um par natural — ambos
resolvem "trocar uma decisão de compilação por uma decisão de
execução", um para um único objeto (Decorator) e outro para a
comunicação entre vários objetos (Observer) — e o exemplo de fechamento
do Decorator (a cadeia de notificadores do `Pedido`) foi desenhado
deliberadamente para ser reaproveitado como o próprio cenário de
abertura do Observer (o mesmo domínio de notificação, dois problemas
estruturais diferentes), evitando uma seção de ponte artificialmente
fina entre as duas metades da aula. Carga horária estimada: ~115 min
(dentro da faixa 90–140 já calibrada). Segue ainda não lido desta
disciplina: `Teoria/Aula 8.tex` e `Aula 9.tex` já foram integralmente
usados (Aulas 10–12); `Revisão.tex` é o único arquivo de fonte que
ainda não foi aberto por nenhuma sessão — mencionado no `_progresso.md`
como o lugar onde MVC poderia (ou não) aparecer, ainda sem confirmação.

**Conteúdo original desta sessão (não literal do `.tex`):** a classe
`Chocolate` (segundo decorador concreto, mesma estrutura de `Leite`,
mencionada só em prosa no `.tex` original) foi escrita para dar
suporte de código ao diagrama de recursão de três camadas; a cadeia de
notificadores `Notificador`/`NotificadorEmail`/`NotificadorComLog`/
`NotificadorComRetry` é inteiramente nova (não está no `.tex`), desenhada
especificamente para (a) ecoar o ângulo do Java I/O do próprio material
e (b) servir de ponte de domínio para o Observer, que já usa
`Pedido`/notificação como cenário-fonte.

`_00-planejamento.md`, `index.qmd` e `_01-respostas.md` escritos, no
formato consolidado de 2 arquivos de apoio já em uso desde a Aula 9.
**Diagramas TikZ (3, novos nesta aula):** a cadeia de wrapping recursivo
do Decorator (`Cafe` → `Leite` → `Chocolate`, setas tracejadas descendo
via `super.getCusto()` e setas coloridas subindo com o valor acumulado
5,00 → 6,50 → 8,50); a topologia publicador-assinante do Observer
(`PedidoSubject` → interface `PedidoObserver` ← `EmailService`/
`LogService`/`InventarioService`); e o mapeamento lado a lado Observer
local vs. Arquitetura Orientada a Eventos (Sujeito local/Produtor de
Eventos, interface de callback/Tópicos e Filas, Observadores locais/
Consumidores de Eventos) — todos com a paleta IC (`icblue`/`icorange`/
`icred`) e wrapper `.fig-resize`, seguindo o padrão já usado nas Aulas
1–2 e 9–12.

**Exercícios:** 3 discursivas + **8 blocos** de V/F de 4 itens (32
itens), dentro da faixa flexível do `CLAUDE.md` (6–10 blocos),
calibrado pelos oito subtemas reais da aula (explosão combinatória,
estrutura do Decorator, recursão, java.io/cadeia de notificadores,
acoplamento em cascata, estrutura do Observer, Push/Pull, EDA
distribuída). Todos os itens são originais (nenhum reaproveitado
verbatim do `\section*{Exercícios de Fixação: Aula 10}` do próprio
`.tex`, cujos itens são majoritariamente definicionais — formato que o
`CLAUDE.md` desta disciplina proíbe explicitamente); os temas desses
blocos-fonte serviram só de inspiração temática, registrado em
`_00-planejamento.md`.

**Achado de processo (correção durante a sessão, mesmo padrão já visto
nas Aulas 9–12):** ao escrever `_01-respostas.md`, a primeira versão da
resolução da Pausa Ativa 1 continha um item de rascunho duplicado (um
`✗` de um item que na verdade era `✔`, seguido por uma nota
inconsistente sobre o próprio erro) — não chegou a ser publicado no
`index.qmd`, mas foi detectado e removido de `_01-respostas.md` antes
da checagem cruzada final, via edição direta. Um script de verificação
cruzada entre os 44 itens `- □` do `index.qmd` (12 de pausas + 32 de
exercícios) e o texto de cada item resolvido em `_01-respostas.md`
(comparando prefixo exato, já que a convenção desta disciplina descarta
o ponto final da afirmação original antes de anexar `— justificativa`)
confirmou as 44 correspondências sem nenhuma divergência de conteúdo
depois da correção.

**Achado de processo (TikZ):** o primeiro render falhou com `! Package
tikz Error: You need to say \usetikzlibrary{calc}` no diagrama de
recursão do Decorator, que usa aritmética de coordenadas
(`($(leite.south)+(-0.2,0)$)`) para deslocar o ponto de chegada das
setas de retorno — corrigido adicionando `calc` à lista de bibliotecas
TikZ desse diagrama (nas duas cópias, notas e slides); os demais 2
diagramas da aula não usam aritmética de coordenadas e não precisaram
do ajuste.

**Validação.** Checador de balanceamento de `:::` (pilha LIFO): zero
erros, pilha vazia, antes e depois da correção do TikZ. `quarto render
--to html` e `--to revealjs`: ambos "Output created", sem erros (só os
avisos padrão do Inkscape na conversão TikZ→SVG, já vistos nas Aulas
1–2 e 9–12). Contagem programática no `_site/`: 44 `□` em `notas.html`
(32 exercícios + 12 pausas), 0 `✔`/`✗`; 12 `□` em `slides.html` (só
pausas, pré-resolução), 12 `✔`/`✗` (8 verdadeiros + 4 falsos,
distribuídos 3+2+3 verdadeiros e 1+2+1 falsos nas 3 pausas). Único
`type="checkbox"` encontrado em ambos os HTMLs é a regra CSS genérica
`ul.task-list li input[type="checkbox"]` do tema (não um checkbox real
renderizado) — confirmado inofensivo, mesmo padrão das Aulas 7–12.
`index.qmd` da disciplina atualizado: Lesson 13 agora aponta para
`./aula13/index.qmd` com título e conteúdo reais (Decorator + Observer);
Lesson 14 adicionada como novo placeholder não linkado, cobrindo a
Síntese Arquitetural (fronteiras núcleo/periferia, matriz de decisão
dos quatro padrões) ainda não escrita.

## Aula 14 — Síntese Arquitetural: Núcleo Estável, Periferia Volátil e o Encerramento do Curso

Fonte: `Teoria/Aula 10.tex`, `\section{Síntese Arquitetural e o Estabelecimento de
Fronteiras}`, linhas 745–827 — a última seção de `Aula 10.tex`, lida na íntegra,
exatamente o trecho que a Aula 13 já havia deliberadamente deferido para esta
aula. Esta é a **última aula nova da disciplina**: não introduz um quinto
padrão, e sim consolida os quatro já ensinados (Strategy, Adapter, Decorator,
Observer) sob uma única moldura arquitetural — a fronteira entre um núcleo
estável (contratos, interfaces, regras de negócio que mudam raramente) e uma
periferia volátil (implementações concretas, SDKs de terceiros, infraestrutura
sujeita a pressão de mercado); a "Regra de Ouro" da dependência (o código
estável nunca depende do código volátil; a dependência aponta sempre para as
abstrações), generalizando o DIP (Aula 5) e o OCP (Aula 10) já vistos
separadamente; a matriz de decisão comparando intenção e critério de uso dos
quatro padrões; e a análise de que cada padrão ataca um tipo específico de
acoplamento nocivo (Strategy: condicional; Adapter: sintático; Decorator:
taxonômico; Observer: temporal/identidade).

**Decisão de escopo (aula deliberadamente mais curta, ~80 min em vez de
90–140 min):** o trecho-fonte é, por natureza, um capítulo de síntese/
fechamento — não há antipadrão novo a diagnosticar nem mecânica de código
nova a formalizar, só uma reorganização do que já foi construído nas Aulas
10–13. Seguindo a nota deixada pela própria Aula 13 (que já sinalizava que
esta aula "pode legitimamente sair mais curta que as demais... sem precisar
de conteúdo inventado para compensar"), a carga horária real (~80 min) não
foi esticada até a faixa das aulas anteriores — reflete a densidade genuína
da fonte, não um corte de conteúdo pedagógico.

**Decisão sobre o fechamento do `.tex` ("Próxima Aula: Expandindo o
SOLID"):** o parágrafo final do material de origem anuncia SOLID completo
como tema da aula seguinte do curso original do professor. Essa promessa
**não foi reaproveitada** nesta aula — o OCP já foi coberto em profundidade
(Aula 10), e esta é a última aula planejada da disciplina no site (não há
Aula 15). A Conclusão foi reescrita como um fechamento genuíno de curso,
retomando explicitamente o problema de abertura da Aula 1 (o custo de
mudança e o acrônimo TRUE de Sandi Metz — Transparent, Reasonable, Usable,
Exemplary) em vez de abrir um gancho para conteúdo que não será escrito —
mesma decisão de princípio já tomada no fechamento da Aula 13 em relação a
essa mesma alusão do `.tex` a SOLID.

`_00-planejamento.md`, `index.qmd` e `_01-respostas.md` escritos, no formato
consolidado de 2 arquivos de apoio já em uso desde a Aula 9. **Diagramas
TikZ (2, novos nesta aula, ambos sem aritmética de coordenadas — não houve
necessidade de `usetikzlibrary{calc}` e nenhum erro de compilação ocorreu):**
a fronteira genérica núcleo/periferia (um núcleo estável envolto por uma
parede de abstração, com quatro exemplos de periferia — SDK de pagamento,
banco de dados, serviço de e-mail, algoritmo sazonal de frete — apontando
para dentro da parede); e a síntese visual dos quatro padrões como quatro
"paredes" diferentes ao redor do mesmo núcleo `Pedido`, cada uma rotulada
com o tipo específico de acoplamento que resolve (Strategy/condicional,
Adapter/sintático, Decorator/taxonômico, Observer/temporal-identidade) —
ambos com a paleta IC (`icblue`/`icorange`/`icred`) e wrapper `.fig-resize`,
seguindo o padrão já usado nas Aulas 1–2 e 9–13.

**Pausas ativas: 2 (não 3), calibradas ao tamanho real da aula** — uma ao
final do bloco de Fronteiras Arquiteturais, outra ao final da Matriz de
Decisão; dentro da faixa flexível que o `CLAUDE.md` já previa para uma aula
genuinamente mais curta. **Exercícios:** 3 discursivas + **6 blocos** de V/F
de 4 itens (24 itens) — no piso da faixa flexível do `CLAUDE.md` (6–10
blocos), calibrado pela densidade real da aula (dois blocos de conteúdo
novo, não quatro ou cinco como nas Aulas 10–13). Todos os itens são
originais (nenhum reaproveitado verbatim do `\section*{Exercícios de
Fixação: Aula 10}` do próprio `.tex`, já consultado só como inspiração
temática nas Aulas 12–13 e não usado literalmente aqui tampouco).

**Achado de processo (verificação cruzada):** um script comparando os 24
itens `- □` de Exercícios do `index.qmd` (excluídos os 8 itens `- □` das 2
pausas ativas, que ficam num `callout-tip` compartilhado à parte) contra o
campo **Afirmação** de `_01-respostas.md` confirmou as 24 correspondências
exatas na primeira passada — nenhuma correção necessária desta vez. Os 8
itens de pausa ativa também foram conferidos manualmente contra a resolução
em `_01-respostas.md`: idênticos, exceto pela convenção já documentada nas
Aulas 9–13 de descartar o ponto final da afirmação original antes de anexar
`— justificativa`.

**Validação.** Checador de balanceamento de `:::` (pilha LIFO): zero erros,
pilha vazia. `quarto render --to html` e `--to revealjs`: ambos "Output
created", sem erros (só os avisos padrão do Inkscape na conversão TikZ→SVG,
já vistos nas Aulas 1–2 e 9–13). Contagem programática no `_site/`: 32 `□`
em `notas.html` (24 exercícios + 8 pausas), 0 `✔`/`✗`; 8 `□` em
`slides.html` (só pausas, pré-resolução), 8 `✔`/`✗` (resoluções). Único
`type="checkbox"` encontrado em ambos os HTMLs é a regra CSS genérica
`ul.task-list li input[type="checkbox"]` do tema (não um checkbox real
renderizado) — confirmado inofensivo, mesmo padrão das Aulas 7–13. Revisão
de picotamento nos headings `##`/`#` do bloco RevealJS (14 slides
extraídos e revisados em sequência, com contagem de caracteres por seção
como checagem adicional): nenhum merge necessário — os 3 slides mais curtos
(60, 48 e 9 caracteres) são os divisores de seção `#` (title-slides sem
conteúdo próprio, mesmo padrão estrutural já usado em todas as aulas
anteriores desta disciplina, não um caso de picotamento real), e as duas
figuras TikZ já foram construídas com o comentário na mesma slide da
figura, evitando de origem o antipadrão descrito no `CLAUDE.md`. `index.qmd`
da disciplina atualizado: Lesson 14 agora aponta para `./aula14/index.qmd`
com título e conteúdo reais (matriz de decisão dos quatro padrões,
fronteira núcleo/periferia, fechamento do curso), substituindo o
placeholder `*(not yet written)*`; nenhuma Lesson 15 foi adicionada.

**Sobre `Revisão.tex` (lido integralmente nesta sessão — o último arquivo
de `Teoria/` ainda não aberto por nenhuma sessão).** É um documento de
**revisão/recapitulação pura** para estudo/prova: slides organizados em 3
blocos temáticos (Execução Virtualizada e Ciclo de Vida de Memória;
Encapsulamento, Invariantes e Coesão Estrutural; Subtipagem, Contratos e
Extensibilidade), cada um já com V/F resolvidos e questões discursivas já
com gabarito embutido no próprio arquivo. Cobre exclusivamente conteúdo já
lecionado nas Aulas 1, 2, 4, 5, 8, 9 e 12 (JVM/bytecode/JIT, Stack/Heap/GC,
cópia defensiva vs. imutabilidade, invariantes de classe e `private`,
Modelo Anêmico, Tell-Don't-Ask, coesão/acoplamento, interfaces, herança
caixa-branca vs. composição caixa-preta, fragilidade da superclasse, LSP,
DIP) — inclusive um exercício de Observer/OCP (`SensorAmbiente`/
`Interessado`) estruturalmente idêntico ao `Pedido`/`PedidoObserver` já
ensinado na Aula 13. **Nenhum conceito novo, não coberto em nenhuma das 14
aulas do site, foi encontrado** — não há MVC, não há SOLID formal, não há
nenhum padrão de projeto além do Observer já ensinado. Por ser puramente
material de recapitulação para prova, com gabaritos já embutidos e sem
nenhuma seção deliberadamente deferida (ao contrário dos `Aula N.tex`, que
sempre tiveram algum corte consciente registrado), **`Revisão.tex` não
gerou uma Aula 15** — está fora do escopo do pipeline `index.qmd`/`aulaNN`
desta disciplina, que é sobre construir aulas de conteúdo novo, não sobre
compilar material de revisão. Nenhuma ação adicional é necessária sobre
este arquivo.

## Encerramento da leitura de `Teoria/` — todos os arquivos consumidos

Com esta sessão, **todos os arquivos de `_fontes/material/Teoria/` foram
lidos e, quando continham conteúdo pedagógico novo, transformados em aula**:
`Aula 1.1.tex`/`Aula 1.2.tex` (Aula 1), `Aula 2.tex` (Aula 2), `Aula 3.tex`
(Aula 3), `Aula 4.tex` (Aula 4), `Aula 5.tex` (Aula 5), `Aula 6.tex` (Aulas
6–7), `Aula 7.tex` (Aulas 8–9), `Aula 8.tex` (Aulas 10–11), `Aula 9.tex`
(Aulas 11–12), `Aula 10.tex` (Aulas 12–14), e `Revisão.tex` (lido e
consumido nesta sessão como material de recapitulação pura, sem gerar aula
nova, conforme justificado acima). Não resta nenhum arquivo de `Teoria/`
não lido, e não resta nenhuma seção deliberadamente deferida de um `Aula
N.tex` ainda pendente de uma aula futura — a disciplina `object-oriented-
programming`, aula01 a aula14, está **completa em relação ao material de
teoria real** (`_fontes/material/Teoria/`) disponível para este curso.
