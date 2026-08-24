# Fontes usadas — Aula 6

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

## Notas sobre as fontes

- Esta aula usa só a primeira metade de `Aula 6.tex`; a segunda metade
  (Polimorfismo, Binding, OCP, Generics) vira a Aula 7, com seu próprio
  `_01-fontes.md`.
- Os 15 blocos de V/F (3 itens) e 10 discursivas do arquivo original
  cobrem a aula inteira (interfaces + polimorfismo); os itens 1, 2, 3, 8,
  9, 10, 15 (V/F) e as discursivas 1, 2, 3, 7, 8 tratam de interfaces e
  exceções — usados como base para os 12 blocos e 3 discursivas desta
  aula. O restante fica para a Aula 7.
