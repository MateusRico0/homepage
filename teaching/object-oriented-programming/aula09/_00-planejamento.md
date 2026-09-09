## Resumo — Aula 9

Fonte: `_fontes/material/Teoria/Aula 7.tex`, **segunda metade** (linhas
759–1411 de 1582) — a Aula 8 já consumiu a primeira metade (Herança:
mecânica, fragilidade, Classes Abstratas, Template Method). Esta aula
fecha o arco de Herança/Polimorfismo com três blocos de conteúdo real:
(1) um recap compacto de Late Binding/VTable e o contrato de
sobrescrita, já que Polimorfismo de Inclusão e Late Binding foram
introduzidos na Aula 7 — aqui o foco é a mecânica de despacho em tempo
de execução e o que `@Override` realmente promete; (2) o **Princípio da
Substituição de Liskov (LSP)**, formalizando quando um filho pode
substituir o pai com segurança (pré-condições, pós-condições,
invariantes, o paradoxo Círculo-Elipse, e a instabilidade de contratos
de exceção); (3) a **taxonomia de exceções** como ferramenta de design —
hierarquia de domínio, captura polimórfica, tradução/wrapping, e o
critério de decisão Checked vs. Unchecked.

**Pré-requisitos:** Aula 7 (Late Binding, Cardelli-Wegner, Generics) e
Aula 8 (Herança, DNA, Classe Base Frágil, Template Method) completas —
o dicionário de notações já traz "É-UM", VTable/Late Binding,
Fail-Fast, e o kit de exceções padrão (`IllegalArgumentException`/
`IllegalStateException`) da Aula 2.

**Decisão de escopo (uma aula, não duas):** embora o trecho-fonte cubra
três tópicos reais, o primeiro (Late Binding/VTable/Override) é em boa
parte recapitulação e aprofundamento mecânico de conteúdo já lançado nas
Aulas 7–8 (Late Binding já foi definido; Classe Base Frágil e
Composição-sobre-Herança já foram tratadas em profundidade na Aula 8) —
não exige o mesmo peso de bloco que um tópico inteiramente novo. Com
esse bloco comprimido a ~20 min, o total estimado (~130 min: ver plano
abaixo) fica dentro da faixa 90–140 min já calibrada pelas 8 aulas
publicadas desta disciplina, então não há necessidade de dividir em
aula09+aula10 como aconteceu com `Aula 6.tex` e a primeira metade de
`Aula 7.tex`.

**Estratégia Pedagógica:** Estratégia B (Inside-Out com Problema-Fio) —
o "problema-fio" é sempre a pergunta "posso confiar cegamente numa
substituição?", primeiro aplicada ao binding de métodos (o compilador
vê `T`, a JVM executa `S`), depois ao contrato semântico completo (LSP)
e por fim ao contrato de falha (taxonomia de exceções) — as três partes
são a mesma pergunta de substituibilidade vista em três camadas cada vez
mais rigorosas, não três algoritmos desconexos (o que justificaria a
Estratégia A).

## Plano de aula — Aula 9 (carga horária estimada: ~130min)

1. **Abertura: Revisão e Introdução** (~10 min) — revisão de Herança
   (Aula 8: "É-UM", DNA compartilhado, Classe Base Frágil) e Late
   Binding (Aula 7); ideia-ponte: herdar dá reuso de estrutura, mas não
   responde quando é seguro *substituir* o pai por um filho; roteiro
   explícito (4 perguntas); problema motivador com `Pagavel`/`Pix`.
2. **Do binding ao contrato: Late Binding, VTable e `@Override`**
   (~20 min) — subtipagem e substituibilidade (`Pagavel p = new Pix()`);
   a mecânica de despacho (lente do compilador vs. realidade do Heap,
   consulta à VTable); `@Override` como preservação de assinatura e
   semântica, não só sintaxe. Pausa ativa 1.
3. **O Princípio da Substituição de Liskov: a definição formal**
   (~15 min) — de "parece o mesmo tipo" para "é seguro substituir";
   formalização $\forall x{:}T,\ \phi(x) \implies \forall y{:}S,\ \phi(y)$;
   a intuição do "cliente cego" (`realizarCheckOut`).
4. **As três regras de contrato do LSP** (~20 min) — pré-condições (não
   seja mais exigente), pós-condições (não entregue menos), preservação
   de invariantes (as "leis de física" da base) — cada regra com o
   contraexemplo de violação do `.tex` (`criarCobranca` exigindo
   `valor >= 100`, retornando `""`, saldo negativo).
5. **O Paradoxo Círculo-Elipse** (~15 min) — a falácia do "É-UM" do
   mundo real aplicada cegamente ao software mutável; diagrama TikZ da
   bifurcação de violação (`setAxes(10,20)` força escolher entre violar
   a própria natureza ou a expectativa do cliente). Pausa ativa 2.
6. **Contratos de exceção e a instabilidade do LSP** (~10 min) — ponte
   entre LSP e o próximo bloco: exceções fazem parte da assinatura;
   lançar uma exceção nova e mais ampla no filho quebra o cliente do
   pai tanto quanto violar pré/pós-condição.
7. **Taxonomia do erro: hierarquia e captura polimórfica** (~15 min) —
   erro como transição de estado prevista, não "acidente"; a árvore de
   falhas (`LojaException` → Infraestrutura/Negócio → especialistas);
   captura polimórfica escolhendo o nível de reação.
8. **Tradução de exceções (Wrapping) e o Princípio da Menor Surpresa**
   (~15 min) — por que a camada de negócio não deve conhecer
   `SQLException`; reembalar preservando a causa original.
9. **Checked vs. Unchecked: o critério de responsabilidade** (~15 min) —
   DNA (Unchecked, Fail-Fast, não se recupera bug com `try/catch`) vs.
   Mundo (Checked, plano de contingência); o exemplo de
   `realizarPagamento` com as três estratégias (validar, tratar,
   reembalar) juntas. Pausa ativa 3.
10. **Fechamento** (~5 min) — retomar as 4 perguntas da abertura; ponte
    para a Aula 10 (Factory Method, Builder, Adapter — a preocupação
    muda de "o objeto se comporta certo?" para "como construímos e
    conectamos objetos complexos sem vazar essa complexidade?").

## Fontes usadas — Aula 9

### Fonte 1: `Teoria/Aula 7.tex`, linhas 759–826 (Subtipagem, Substituibilidade e VTable)

**Uso pretendido:** abrir o bloco de Late Binding revisitado, ancorando
a mecânica de despacho na VTable.

**Trecho:**
> "O polimorfismo de inclusão é o mecanismo que permite que diferentes
> subtipos sejam tratados de forma uniforme através de uma abstração
> comum. Se $S$ é um subtipo de $T$, então objetos do tipo $T$ podem ser
> substituídos por instâncias de $S$ sem que o sistema precise conhecer
> a identidade concreta da classe."

**Trecho — mecânica da VTable:**
> "A chamada é feita sobre uma referência de tipo Pagavel. A JVM segue o
> ponteiro da referência até o endereço do objeto no Heap. Ela consulta
> a VTable (Virtual Method Table) da classe concreta (ex: Pix). Ela
> executa o endereço de memória da implementação específica encontrada
> na tabela."

---

### Fonte 2: `Teoria/Aula 7.tex`, linhas 828–958 (Sobrescrita como contrato)

**Uso pretendido:** fundamentar por que `@Override` é uma promessa
semântica, não só uma anotação sintática — ponte direta para o LSP.

**Trecho:**
> "A sobrescrita (@Override) é o mecanismo que permite ao especialista
> modificar o *como*, preservando rigorosamente o *o quê*. O contrato do
> método deve ser mantido: se o pai promete 'validar', o filho não pode
> alterar a semântica para 'deletar'."

---

### Fonte 3: `Teoria/Aula 7.tex`, linhas 961–1032 (LSP: definição formal e regras de pré/pós-condição)

**Uso pretendido:** apresentar a definição formal do LSP e as regras de
contravariância/covariância que estruturam o Bloco 4.

**Trecho — definição formal:**
> "se $S$ é um subtipo de $T$, então objetos do tipo $T$ podem ser
> substituídos por objetos do tipo $S$ sem que as propriedades
> desejáveis do programa sejam alteradas."

**Trecho — pré-condições:**
> "A subclasse deve ser tão tolerante quanto o pai. Se a base aceita
> qualquer número positivo, o filho não pode decidir restringir esse
> domínio exigindo valores acima de 100. Isso quebraria qualquer código
> cliente que estivesse passando valores legítimos (ex: 50) e que
> subitamente dispararia uma IllegalArgumentException inesperada."

**Trecho — pós-condições:**
> "A subclasse deve ser tão generosa quanto o pai. Se a base promete
> retornar um objeto válido ou lançar uma exceção, o filho não pode
> enfraquecer essa garantia retornando null ou estados vazios
> inconsistentes. O filho pode até entregar algo mais refinado, mas
> nunca menos do que o prometido."

**Trecho — invariantes:**
> "Leis internas, como 'o saldo nunca pode ser negativo', são a
> integridade da 'linhagem'. Uma subclasse não pode subverter essas
> leis, independentemente de ter acesso direto aos atributos protegidos
> (protected)."

---

### Fonte 4: `Teoria/Aula 7.tex`, linhas 1034–1096 (O Paradoxo Círculo-Elipse e contratos de exceção)

**Uso pretendido:** o contraexemplo central do Bloco 5 (diagrama TikZ) e
a ponte do Bloco 6 para exceções.

**Trecho — paradoxo:**
> "Um Retangulo permite alterar altura e largura de forma independente
> via setAxes(a, b). Um Quadrado, por sua vez, exige que a == b. [...]
> Se o cliente invocar retangulo.setAxes(10, 20) em um objeto que ele
> acredita ser um Retangulo (mas que é, na verdade, um Quadrado), o
> objeto terá que escolher entre violar sua própria natureza matemática
> ou ignorar o pedido do cliente."

**Trecho — contratos de exceção:**
> "As exceções fazem parte da assinatura do contrato. O LSP exige que
> uma subclasse não 'assuste' o cliente com exceções que ele não está
> preparado para tratar. [...] Lançar exceções como
> UnsupportedOperationException para 'pular' métodos que o filho não
> quis implementar é, invariavelmente, uma violação do LSP."

---

### Fonte 5: `Teoria/Aula 7.tex`, linhas 1133–1237 (Taxonomia do erro, hierarquia e captura polimórfica)

**Uso pretendido:** abrir o bloco de exceções tratando o erro como
transição de estado prevista, e fundamentar a árvore de exceções e a
captura polimórfica (com diagrama TikZ de hierarquia).

**Trecho — erro como fluxo alternativo:**
> "O erro não é um 'acidente' ou algo que 'deu errado'; é uma saída
> prevista de uma função quando as pré-condições não permitem o
> sucesso."

**Trecho — hierarquia de tipos:**
> "Não trate exceções como simples mensagens de texto; trate-as como uma
> Hierarquia de Tipos que espelha o domínio de negócio."

**Trecho — captura polimórfica:**
> "A principal vantagem da herança aplicada às exceções é o Polimorfismo
> no Catch. Ele permite que o sistema reaja com o nível de especificidade
> adequado ao contexto."

---

### Fonte 6: `Teoria/Aula 7.tex`, linhas 1238–1386 (Wrapping, Checked vs. Unchecked, Fail-Fast, Menor Surpresa)

**Uso pretendido:** fundamentar os Blocos 8 e 9 (tradução de exceções e
o critério de design Checked/Unchecked).

**Trecho — wrapping:**
> "O CheckoutController não deveria lidar com SQLException ou
> TimeoutException. Isso é detalhe de implementação. [...] Capture o
> erro técnico e 're-embale' em um erro de domínio."

**Trecho — critério Checked vs. Unchecked:**
> "A escolha entre uma exceção Checked ou Unchecked não é técnica, é
> sobre quem detém a responsabilidade."

**Trecho — Fail-Fast:**
> "Valide no construtor ou no início do método. Se algo está errado,
> lance a exceção imediatamente. [...] É muito mais fácil debugar um
> erro que aconteceu na entrada do que um erro que se manifesta 10
> minutos depois por causa de um dado que foi salvo errado no banco."

**Trecho — Princípio da Menor Surpresa:**
> "O sistema de erro faz parte da Interface Pública. Ele deve ser
> previsível. [...] Se um método diz que lança SaldoInsuficienteException,
> ele não deve deixar escapar um NullPointerException interno."

---

### Notas sobre as fontes

- Fonte primária: `Teoria/Aula 7.tex`, segunda metade (linhas
  759–1411) — o mesmo arquivo cuja primeira metade virou a Aula 8. A
  seção final `\section{Conclusão}` do `.tex` (linhas 1387–1411), que
  encerra o arco Herança+LSP+Exceções do arquivo inteiro, foi lida e
  usada apenas na parte referente a LSP/exceções no fechamento desta
  aula — a parte sobre Herança já foi coberta no fechamento da Aula 8.
- `\section*{Exercícios de Fixação}` do próprio `.tex` (linhas
  1412–1582: 25 blocos de V/F de 3 itens no formato `( )` + 15
  discursivas) foi lida como pool de referência de temas, mas **não
  reaproveitada verbatim** — a maioria dos itens de V/F ali é de
  formato definicional ("X é considerado Y", "X permite Z") that o
  `CLAUDE.md` desta disciplina proíbe explicitamente (paráfrase
  literal/pergunta definicional). Os 9 blocos de V/F e as 3 discursivas
  desta aula (seção Exercícios do `index.qmd`) são **originais**,
  construídos a partir das 4 heurísticas exigidas, usando os mesmos
  temas do `.tex` (VTable, LSP pré/pós/invariantes, Círculo-Elipse,
  captura polimórfica, wrapping, Checked/Unchecked) como ponto de
  partida temático, não como texto-fonte.
- Nenhuma citação aos 5 livros-base (Weisfeld, Bloch, Metz,
  Arnold-Gosling, Eckel) foi incluída nesta aula: não há, nos PDFs
  symlinkados em `_fontes/`, uma página específica já verificada nesta
  sessão para os pontos exatos tratados aqui (LSP formal, VTable,
  taxonomia de exceções) — por instrução do usuário, preferiu-se citar
  o `.tex` da própria disciplina (fonte primária real, per
  `_progresso.md`) a inventar um número de página não conferido.
