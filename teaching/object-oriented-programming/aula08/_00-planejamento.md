## Resumo — Aula 8

Fonte: `_fontes/material/Teoria/Aula 7.tex` ("Herança, Liskov e a Gestão
Estruturada de Falhas"), **primeira metade** (linhas 1–740) — o arquivo
real (1583 linhas) é longo o bastante para virar duas aulas do site; esta
cobre a mecânica e os perigos da Herança (`extends`, DNA, classe base
frágil, herança vs. composição, invariantes invisíveis), Classes
Abstratas, Herança de Estado vs. Comportamento, e o padrão Template
Method. A segunda metade (Liskov Substitution Principle e tratamento
estruturado de exceções) vira a Aula 9.

**Pré-requisitos:** Aulas 1–7 completas (interfaces, polimorfismo,
Generics — a pergunta que fica: existe outro mecanismo de polimorfismo,
que compartilha estrutura, não só comportamento?).

## Plano de aula — Aula 8 (carga horária estimada: ~140min)

1. **Abertura: do papel social à essência** (~10 min) — Interface define
   o que o objeto faz; Herança define o que ele *é* — a relação "É-UM",
   o acoplamento mais forte da OO.
2. **A mecânica: `extends` e o DNA compartilhado** (~15 min) —
   `MeioPagamentoBase`/`Cartao`; herança de atributos como incorporação
   física, não associação externa; `protected` como "encapsulamento de
   linhagem".
3. **A fragilidade das invariantes de base** (~15 min) — sem `final`, a
   subclasse pode burlar a regra do pai; o Problema da Classe Base
   Frágil (o bug de contagem dupla em `processarLote`).
4. **Quando herdar, e quando não** (~15 min) — herança por conveniência
   é um erro (`GerenciadorDeCobrancas` não é uma `ListaDeContatos`);
   especialização legítima exige DNA compartilhado **e** necessidade de
   tratamento polimórfico.
5. **O vínculo de sangue: acoplamento estrutural e invariantes
   invisíveis** (~20 min) — efeito cascata, a "alteração inocente" que
   quebra um filho existente; pressupostos de ordem, semântica de
   retorno, o problema do `super`.
6. **A base como guardiã: blindando a linhagem** (~15 min) — atributos
   `private` no pai, métodos `final`, métodos-gancho (*hooks*)
   `protected abstract`.
7. **Classes Abstratas: a máquina semi-acabada** (~15 min) — a metáfora
   do chassi; protocolo de estado parcial; o compilador como "inspetor
   de fábrica" recusando `new` em classe abstrata.
8. **Herança de Estado vs. Comportamento** (~15 min) — herdar métodos é
   fluido; herdar atributos é alocação física compulsória; a "subclasse
   gorda"; acoplamento de representação e o custo de refatorar o pai.
9. **Template Method** (~15 min) — o esqueleto do algoritmo num método
   `final`; ganchos abstratos preenchidos pelo filho; Inversão de
   Controle e o Princípio de Hollywood ("não nos ligue, nós ligamos para
   você").
10. **Fechamento e ponte** (~5 min) — Herança resolve reuso de estrutura,
    mas abre a pergunta: quando é seguro dizer que um filho pode
    substituir o pai em qualquer lugar? Ponte para a Aula 9: o Princípio
    da Substituição de Liskov.

## Fontes usadas — Aula 8

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

### Notas sobre as fontes

- Esta aula usa só a primeira metade de `Aula 7.tex` (1583 linhas no
  total); a segunda metade (Liskov Substitution Principle, gestão
  estruturada de exceções) vira a Aula 9, com seu próprio
  `_01-fontes.md`.
- Os exemplos de código (`MeioPagamentoBase`/`Cartao`/`Pix`,
  `GerenciadorDeCobrancas`, o Template Method de `realizarPagamento`)
  foram reaproveitados quase literalmente do `.tex` original.
