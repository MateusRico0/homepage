## Resumo — Aula 7

Fonte: `_fontes/material/Teoria/Aula 6.tex`, **segunda metade** (linhas
657–1123) — continuação direta da Aula 6 (Interfaces). Cobre Polimorfismo
(definição, *late binding*), a taxonomia de Cardelli-Wegner (Universal:
Inclusão e Paramétrico; Ad-hoc: Sobrecarga e Coerção), a tabela de Binding
Estático vs. Dinâmico, o "Fim do IF" e o Princípio Aberto/Fechado (OCP), e
Generics (o problema dos *raw types*, Generics como etiqueta de tipo).

**Pré-requisitos:** Aula 6 completa (interfaces como contrato; a pergunta
que fica em aberto lá: como o compilador aceita múltiplas formas por trás
do mesmo tipo `Pagavel`?).

## Plano de aula — Aula 7 (carga horária estimada: ~120min)

1. **Abertura: a pergunta da Aula 6** (~5 min) — `Pagavel forma` recebe
   ora um `Pix`, ora um `Cartao`; falta explicar o mecanismo.
2. **O que é Polimorfismo, e o mecanismo de Late Binding** (~20 min) —
   "muitas formas"; o compilador só checa que o método existe na
   interface; a JVM decide, em tempo de execução, qual código roda,
   olhando o objeto real na Heap.
3. **A taxonomia de Cardelli-Wegner** (~25 min) — Universal (Inclusão via
   interfaces/herança; Paramétrico via Generics) vs. Ad-hoc (Sobrecarga;
   Coerção); por que a sobrecarga é "polimorfismo aparente" — viola OCP.
4. **Binding estático vs. dinâmico: a tabela comparativa** (~15 min) —
   quando ocorre, quem decide, exemplos, e por que a OO aposta no
   dinâmico (desacoplamento total).
5. **O fim do "Mar de IFs" e o OCP** (~20 min) — código antes (cadeia de
   `if/else` sobre `String tipo`) e depois (uma linha de delegação
   polimórfica); "aberto para extensão, fechado para modificação"; a
   meta-regra: precisar de um `if` de tipo é sinal de que o polimorfismo
   não foi usado.
6. **Generics: da lista "aceita-tudo" à etiqueta de tipo** (~25 min) — o
   problema dos *raw types* (erro tardio, `ClassCastException`); Generics
   move a detecção para o tempo de compilação; vantagens: robustez,
   legibilidade, reuso, performance.
7. **Fechamento e ponte** (~10 min) — Interfaces + Polimorfismo + Generics
   fecham o "capítulo" de tipagem e contrato; ponte para a Aula 8:
   Herança — o outro mecanismo de polimorfismo, com um custo de
   acoplamento que as interfaces evitam.
