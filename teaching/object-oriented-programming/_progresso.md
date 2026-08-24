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

## Aulas 9–12+ (numeração provisória)

Não iniciadas. Cada uma deve ser conferida contra o `Teoria/Aula N.tex`
correspondente em `_fontes/material/` antes de escrever — não presumir que
a Lesson N já esboçada no `index.qmd` da disciplina bate 1:1 com o
conteúdo real da Aula N do material, nem que o resumo de `planejamento.tex`
bate com o `.tex` real (já divergiu na Aula 3). Ao terminar cada aula,
conferir também se ela precisa de pelo menos 3 pares de teste V/F
intercalados nos slides antes de dar a aula por concluída (a Aula 3 quase
saiu com só 2).
