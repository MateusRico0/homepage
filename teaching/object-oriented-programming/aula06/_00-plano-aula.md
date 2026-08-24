## Resumo — Aula 6

Fonte: `_fontes/material/Teoria/Aula 6.tex` ("Interfaces, Polimorfismo e
Tipos"), **primeira metade** — o arquivo real é longo o suficiente para
virar duas aulas do site; esta cobre Interfaces (contrato de
comportamento), Interfaces Modernas (default/static/private, o padrão
"Mutador Cego"), Interface vs. Classe Abstrata, Tipos como comportamento
(não DNA), e Exceções como Guardas de Contrato. A segunda metade
(Polimorfismo, Binding, OCP, Generics) vira a Aula 7.

**Pré-requisitos:** Aulas 1–5 completas (encapsulamento, associação,
delegação, DIP — a Aula 5 terminou com o gancho: como o compilador aceita
`Pagavel formaDePagamento = new Pix()` e depois `= new Cartao()`?).

## Plano de aula — Aula 6 (carga horária estimada: ~130min)

1. **Abertura: o gancho da Aula 5** (~5 min) — DIP exigiu uma abstração
   (`Pagavel`); falta o mecanismo de linguagem que a torna real.
2. **Interfaces: o contrato de comportamento** (~20 min) — Interface
   define o que um objeto *faz*, não o que ele *é*; analogia da tomada
   elétrica; a interface `Pagavel` e a classe `Pix` honrando o contrato
   com `@Override`.
3. **Interfaces modernas: default, static, private** (~20 min) — Java 8+
   permite comportamento em interfaces sem quebrar retrocompatibilidade;
   o padrão "Mutador Cego" — a interface detém a regra (juros), a classe
   concreta detém o armazenamento.
4. **Interface vs. Classe Abstrata** (~10 min) — a fronteira é o estado:
   interface proíbe atributos de instância, classe abstrata permite.
5. **Tipos: comportamento, não DNA** (~15 min) — um tipo é definido pelas
   mensagens que o objeto responde, não pelo que ele guarda; `Pix` e
   `CartaoDeCredito` sem nada em comum em dados, mesmo tipo `Pagavel`.
6. **Exceções como Guardas de Contrato** (~25 min) — o compilador não
   sabe que um preço negativo é um erro conceitual; Fail-Fast no
   `Pix.criarCobranca`; o erro de silenciar (retornar `null`/`0`); o
   try-catch do `CheckoutController` como barreira de contenção.
7. **Refatorando o sistema: três contratos novos** (~20 min) —
   `Notificavel` (canal de comunicação), `EstrategiaDesconto` (regra de
   negócio protegida de valores absurdos), `ServicoLogistico` (rastreio
   delegado); cada um com uma exceção própria guardando o contrato.
8. **Fechamento e ponte** (~5 min) — o sistema virou uma "sociedade de
   especialistas"; ponte para a Aula 7: como a mesma variável `Pagavel`
   aceita `Pix` e `Cartao` em tempo de execução — Polimorfismo.
