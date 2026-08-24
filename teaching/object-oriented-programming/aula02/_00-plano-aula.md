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

## Plano de aula — Aula 2 (carga horária estimada: ~140min)

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
