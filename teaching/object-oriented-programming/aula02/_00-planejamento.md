## Resumo — Aula 2

Fonte: `_fontes/material/Teoria/Aula 2.tex` ("Objetos como Máquinas de
Estado"). Aprofunda o encapsulamento da Aula 1 formalizando o objeto como
uma **máquina de estados finita** (DFA): atributos = estado, métodos =
transições. Cobre o anti-padrão do Modelo Anêmico, invariantes de classe,
o construtor como base de uma indução matemática (Fail-Fast), CQS
(Command-Query Separation), Design by Contract (pré/pós-condições), o kit
de exceções padrão do Java, e o contrato `equals()`/`hashCode()`
(identidade física vs. lógica).

**Pré-requisitos:** Aula 1 completa (Estado/Comportamento/Identidade,
encapsulamento, classe `Produto`, `this`).

## Plano de aula — Aula 2 (carga horária: ~140min)

1. **Abertura e ponte** (~5 min) — Retomar a promessa da Aula 1: o
   construtor validando o preço do `Produto`. Pergunta: e se o preço vier
   negativo — o construtor deveria "consertar" o valor ou recusar o
   objeto?
2. **Struct passivo vs. agente ativo** (~15 min) — Contraste C (`struct`
   + função externa) vs. Java (`Pedido` com `pagar()` interno). O objeto
   como responsável por sua própria consistência.
3. **O anti-padrão do Modelo Anêmico** (~15 min) — Getters/setters cegos
   para tudo esvaziam o objeto de regra de negócio; a "Regra de Ouro": se
   você precisa `get` para decidir por fora e depois `set`, o design
   falhou.
4. **A Máquina de Estados Finita (DFA) e o objeto** (~20 min) — Teoria do
   autômato (estados, transições, determinismo); mapeamento estado=
   atributos, transição=métodos; diagrama de estados do `Produto`
   (CADASTRADO → DISPONÍVEL → ESGOTADO), com a invariante estoque ≥ 0.
5. **Invariantes: do laço à classe** (~15 min) — Invariante de laço
   (Insertion Sort) como analogia formal; invariante de classe como a
   generalização para o ciclo de vida do objeto; exemplos de
   `ContaBancaria`, `Triangulo` e `Carrinho` (propriedade derivada).
6. **O construtor como base da indução, e Fail-Fast** (~15 min) — Analogia
   com prova por indução finita (base = construtor, passo = métodos);
   "Objeto Zumbi" como consequência de um construtor permissivo; exemplo
   `Produto` com validação agressiva.
7. **CQS: Comandos vs. Consultas** (~15 min) — Métodos são ou Comandos
   (mutam, retornam `void`) ou Consultas (retornam dado, sem efeito
   colateral); o perigo de misturar os dois (`verificarSaldo()` que cobra
   taxa).
8. **Design by Contract** (~10 min) — Pré-condições (culpa do cliente) vs.
   pós-condições (culpa do autor da classe); exemplo `processarSaque`.
9. **Exceções como defesa: Fail-Fast contra códigos de erro** (~15 min) —
   Por que `-1`/`false` falha silenciosamente; o kit de exceções padrão
   (`IllegalArgumentException`, `IllegalStateException`,
   `NullPointerException` via `Objects.requireNonNull`); exemplo
   `Elevador`.
10. **Identidade física vs. lógica: `equals()` e `hashCode()`** (~15 min)
    — O paradoxo de dois `Produto` "iguais" que a JVM trata como
    diferentes; o contrato inseparável equals/hashCode; analogia do
    armazém (corredor = hash, etiqueta = equals).
11. **Fechamento e ponte** (~5 min) — Recapitular o objeto como máquina de
    estados encapsulada e blindada; ponte para a Aula 3: escopo, ciclo de
    vida e o contrato interface vs. implementação (Aula 3 do curso real,
    "O Contrato do Objeto, Escopo e Identidade").

## Fontes usadas — Aula 2

> Mesmo padrão da Aula 1: fonte primária é `Teoria/Aula 2.tex` (material de
> aula do próprio professor). Citações aos livros-base foram herdadas como
> já estavam no material, não reconferidas contra os PDFs nesta sessão.

### Fonte 1: `Teoria/Aula 2.tex` — "Objetos como Máquinas de Estado"
**Uso pretendido:** aula inteira.

**Trecho — struct vs. agente ativo:**
> "A Orientação a Objetos inverte essa lógica. Em Java, a classe não
> apenas agrupa os dados, mas também contém as funções (métodos) que têm
> o direito de alterar esses dados. [...] Essa união indissociável entre
> dados e as regras que os governam é o que chamamos de encapsulamento
> forte \citep{bloch2008effective}."

**Trecho — Modelo Anêmico:**
> "O verdadeiro design rico (Rich Domain Model) exige que evitemos
> setters genéricos sempre que possível. A mudança de estado deve ser
> provocada por métodos verbais que denotem uma intenção clara de
> negócio (pagar(), enviar(), cancelar())."

**Trecho — DFA e o objeto:**
> "A grande revelação do Design Orientado a Objetos é que todo objeto bem
> projetado é a implementação física de uma Máquina de Estados
> Encapsulada. [...] Ref: Hopcroft, Motwani & Ullman, 'Introduction to
> Automata Theory, Languages, and Computation'."

**Trecho — construtor como base da indução:**
> "Base da Indução (n=0): O construtor C(args) tem o dever arquitetural
> de garantir que o novo objeto o satisfaça o ∈ V desde o seu primeiro
> milissegundo de vida na memória Heap. [...] Passo Indutivo (n ⟹ n+1):
> Dado um objeto que já se encontra em um estado sₙ ∈ V, qualquer método
> público m(sₙ) invocado sobre ele deve obrigatoriamente resultar em um
> estado subsequente sₙ₊₁ ∈ V."

**Trecho — CQS:**
> "O princípio CQS dita que qualquer método público de uma classe deve
> pertencer exclusivamente a um destes dois papéis [...] Ref:
> \citeauthor{meyer1988object}, 'Object-Oriented Software Construction' e
> \citeauthor{fowler2002patterns}."

**Trecho — kit de exceções (Bloch):**
> "\citet{bloch2008effective} defende fortemente a reutilização das
> exceções padrão do Java, pois elas fornecem um vocabulário universal
> que qualquer programador da equipe entenderá imediatamente."

**Trecho — equals/hashCode:**
> "Joshua Bloch no Effective Java explica que classes que representam
> 'Valores de Negócio' [...] exigem que o desenvolvedor sobrescreva o
> comportamento herdado da classe Object. [...] A regra fundamental aqui
> é o contrato inseparável entre o equals() e o hashCode()."

---

## Notas sobre as fontes

- Duas referências aparecem pela primeira vez nesta aula, fora dos 5
  livros-base já symlinkados em `_fontes/`: Hopcroft, Motwani & Ullman
  ("Introduction to Automata Theory...", citada só para a definição de
  DFA) e Meyer/Fowler (CQS, Design by Contract). Não foram adicionados
  PDFs para essas — são citações pontuais de uma ideia, não fontes
  usadas em profundidade ao longo da disciplina.
- O diagrama de estados do `Produto` (CADASTRADO/DISPONÍVEL/ESGOTADO) no
  `index.qmd` é uma adaptação em TikZ do diagrama já existente em
  `Aula 2.tex` (mesmos três estados e transições), recolorido com a
  paleta do IC.
