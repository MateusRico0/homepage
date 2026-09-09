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

## Fontes usadas — Aula 6

> Mesmo padrão das aulas anteriores: fonte primária é `Teoria/Aula 6.tex`
> — que no material original é uma única aula longa ("Interfaces,
> Polimorfismo e a Tipos de Tipo", 1241 linhas), dividida aqui em duas
> aulas do site (Aula 6: Interfaces e Exceções; Aula 7: Polimorfismo e
> Generics) por tamanho. Citações herdadas do material original, não
> reconferidas contra os PDFs nesta sessão.

### Fonte 1: `Teoria/Aula 6.tex`, §1–4 (linhas 16–424)
**Uso pretendido:** Interfaces, Interfaces Modernas, Interface vs. Classe Abstrata, Tipos.

**Trecho — interface como contrato:**
> "Uma interface não é uma classe; ela é um Contrato de Comportamento.
> Enquanto uma classe define o que um objeto é (seu estado e DNA), a
> interface define o que um objeto faz."

**Trecho — Mutador Cego:**
> "A interface atua como um 'maestro' que detém a regra de negócio (o
> cérebro), enquanto a classe concreta detém o armazenamento (os
> músculos)."

**Trecho — tipo como comportamento:**
> "O tipo de um objeto é definido não pelo que ele guarda (seus campos de
> dados), mas pelas mensagens às quais ele responde (seus métodos)."

### Fonte 2: `Teoria/Aula 6.tex`, §5 (linhas 425–656)
**Uso pretendido:** Exceções como Guardas de Contrato.

**Trecho:**
> "O compilador é o primeiro nível de defesa [...] Entretanto, ele é
> 'cego' para as regras de negócio. Uma exceção é a forma de um objeto
> dizer: 'Eu recebi o tipo correto, mas os dados violam as regras da
> minha existência'."

**Trecho — diretriz de responsabilidade:**
> "objetos de baixo nível (como o Pix) lançam exceções; objetos de alto
> nível (como o Controller) decidem como o sistema deve reagir a elas."

---

### Notas sobre as fontes

- Esta aula usa só a primeira metade de `Aula 6.tex`; a segunda metade
  (Polimorfismo, Binding, OCP, Generics) vira a Aula 7, com seu próprio
  `_01-fontes.md`.
- Os 15 blocos de V/F (3 itens) e 10 discursivas do arquivo original
  cobrem a aula inteira (interfaces + polimorfismo); os itens 1, 2, 3, 8,
  9, 10, 15 (V/F) e as discursivas 1, 2, 3, 7, 8 tratam de interfaces e
  exceções — usados como base para os 12 blocos e 3 discursivas desta
  aula. O restante fica para a Aula 7.
