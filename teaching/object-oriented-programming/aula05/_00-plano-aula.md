## Resumo — Aula 5

Fonte: `_fontes/material/Teoria/Aula 5.tex` ("Acoplamento e Contratos").
Mostra que composição via construtor (Aula 4) não garante, sozinha,
desacoplamento lógico — um objeto pode "espreitar" os dados de um
colaborador associado (Inveja de Recursos). Cobre a métrica CBO, a
Escala de Myers (Conteúdo/Comum/Estampa/Dados), o padrão GRASP
Especialista na Informação, e termina no Princípio da Inversão de
Dependência (DIP), com um gancho explícito para Herança e Interfaces na
Aula 6.

**Pré-requisitos:** Aulas 1–4 completas (encapsulamento, Demeter, SRP,
associação e delegação).

## Plano de aula — Aula 5 (carga horária estimada: ~140min)

1. **Abertura: o falso desacoplamento** (~10 min) — Separar em arquivos e
   passar via construtor não é suficiente; `Pedido` pode receber um
   `Carrinho` "corretamente" e ainda assim invadir sua caixa preta.
2. **Feature Envy: o `Pedido` que inveja o `Carrinho`** (~15 min) —
   `carrinho.getItens()` iterado por fora; o diagnóstico ("a lógica devia
   morar onde os dados estão"); a cura via *Move Method*.
3. **Medindo: a métrica CBO** (~15 min) — Contar classes externas
   conhecidas; comparar CBO=2 (Inveja) vs. CBO=1 (delegação pura).
4. **A Escala de Myers: do pior ao ideal** (~30 min) — Acoplamento de
   Conteúdo (atributo público mutado por fora), Comum (chamada estática a
   `Notificacao`), Estampa (passar `Cliente` inteiro por um e-mail),
   Dados (passar só a `String` necessária) — cada nível com exemplo e
   refatoração.
5. **GRASP: o Especialista na Informação** (~10 min) — A responsabilidade
   pertence a quem tem os dados; `Carrinho`, não `Pedido`, deve calcular
   seu total.
6. **O limite da composição: acoplamento a classes concretas** (~20 min)
   — `Cliente` com `private Cartao`; o pesadelo da expansão
   (`if (cartao) ... else if (pix) ...`), violando o OCP.
7. **DIP: o Muro de Fronteira** (~15 min) — Módulos de alto nível não
   devem depender de baixo nível; ambos dependem de abstrações
   (`Pagavel`); a inversão: `Cartao`/`Pix` se adaptam ao contrato, não o
   contrário.
8. **O gancho: múltiplas identidades e a barreira da tipagem** (~15 min)
   — Como o compilador aceita que `Pagavel formaDePagamento` receba ora
   um `Pix`, ora um `Cartao`? A resposta — Polimorfismo — fica para a
   próxima aula.
9. **Fechamento e ponte** (~5 min) — Ponte explícita para a Aula 6:
   Herança e Interfaces como os mecanismos de linguagem que tornam o
   contrato `Pagavel` real.
