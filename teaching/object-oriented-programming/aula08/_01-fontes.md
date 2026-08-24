# Fontes usadas — Aula 8

> Fonte primária: primeira metade de `Teoria/Aula 7.tex` (linhas 1–740).
> Citações herdadas do material original, não reconferidas contra os
> PDFs nesta sessão.

### Fonte 1: `Teoria/Aula 7.tex`, linhas 16–232 (Herança: mecânica e "quando herdar")
**Trecho — Interface vs. Herança:**
> "Enquanto a Interface define um papel social (o que o objeto faz), a
> Herança define a sua essência (o que o objeto é). [...] relação
> 'É-UM' (IS-A) [...] o acoplamento vitalício: o vínculo mais forte da
> Orientação a Objetos."

**Trecho — Classe Base Frágil (bug de contagem dupla):**
> "Se passarmos uma lista com 3 valores para cartao.processarLote(), [...]
> o resultado final será 6, duplicando a contagem de forma errônea."

**Trecho — herança por conveniência:**
> "O gerenciador não é uma lista; ele apenas usa uma lista."

### Fonte 2: `Teoria/Aula 7.tex`, linhas 234–526 (acoplamento, invariantes invisíveis, classes abstratas)
**Trecho — Fragile Base Class:**
> "O termo Fragile Base Class descreve a situação em que as superclasses
> são tão fundamentais para a sobrevivência das subclasses que se tornam
> virtualmente impossíveis de modificar ou evoluir."

**Trecho — classe abstrata como chassi:**
> "Pense nela como um chassi de carro: tem rodas, bancos e suspensão, mas
> não possui motor. [...] a fábrica precisa decidir se finalizará aquela
> estrutura como um CarroEletrico ou um veículo a Combustao."

### Fonte 3: `Teoria/Aula 7.tex`, linhas 528–740 (Estado vs. Comportamento, Template Method)
**Trecho — subclasse gorda:**
> "Adicionar um campo na classe base aumenta instantaneamente o tamanho
> de todos os milhares de objetos filhos na memória."

**Trecho — Template Method / Princípio de Hollywood:**
> "Inversão de Controle (IoC), frequentemente resumido pelo jargão
> arquitetural: 'Não nos ligue, nós ligamos para você' (O Princípio de
> Hollywood)."

---

## Notas sobre as fontes

- Esta aula usa só a primeira metade de `Aula 7.tex` (1583 linhas no
  total); a segunda metade (Liskov Substitution Principle, gestão
  estruturada de exceções) vira a Aula 9, com seu próprio
  `_01-fontes.md`.
- Os exemplos de código (`MeioPagamentoBase`/`Cartao`/`Pix`,
  `GerenciadorDeCobrancas`, o Template Method de `realizarPagamento`)
  foram reaproveitados quase literalmente do `.tex` original.
