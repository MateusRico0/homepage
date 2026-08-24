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
