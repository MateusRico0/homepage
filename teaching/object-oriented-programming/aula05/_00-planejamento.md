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

## Fontes usadas — Aula 5

> Mesmo padrão das aulas anteriores: fonte primária é `Teoria/Aula 5.tex`.
> Citações herdadas do material original, não reconferidas contra os PDFs
> nesta sessão.

### Fonte 1: `Teoria/Aula 5.tex` — "Acoplamento e Contratos"
**Uso pretendido:** aula inteira.

**Trecho — Feature Envy (Fowler):**
> "Martin Fowler define a Feature Envy (Inveja de Recursos) como um
> 'cheiro de código' onde um método parece mais interessado nos dados de
> um objeto colaborador do que nos atributos da sua própria classe."

**Trecho — CBO:**
> "Utilizamos a métrica CBO (Coupling Between Object Classes), definida
> na clássica Suíte de Métricas CK (Chidamber & Kemerer, 1994) [...]
> Contagem de CBO para Pedido: 2 [...] Contagem de CBO para Pedido: 1."

**Trecho — Escala de Myers:**
> "Glenford Myers estabeleceu uma taxonomia clássica que classifica o
> acoplamento num espectro de toxicidade arquitetural [...] Nível
> Crítico (Conteúdo) [...] Nível Alto (Comum) [...] Nível Médio
> (Estampa) [...] Nível Ideal (Dados)."

**Trecho — GRASP / Especialista na Informação:**
> "O framework GRASP (General Responsibility Assignment Software
> Patterns), consolidado por Craig Larman. O pilar fundamental [...] é o
> padrão Especialista na Informação (Information Expert). [...] a
> responsabilidade de realizar uma tarefa deve ser atribuída à classe que
> possui a maior quantidade de informações necessárias para cumpri-la."

**Trecho — DIP:**
> "Aplicamos o Princípio da Inversão de Dependência (DIP), formulado por
> Robert C. Martin. [...] Módulos de alto nível não devem depender de
> módulos de baixo nível. Ambos devem depender de abstrações."

---

### Notas sobre as fontes

- Duas referências pontuais aparecem sem PDF symlinkado: Chidamber &
  Kemerer (1994, métricas CK/CBO) e Glenford Myers (escala de
  acoplamento) — citações de conceito, não aprofundadas com página exata.
- O código de exemplo (`Pedido`/`Carrinho`, `Notificacao`, `Cliente`/
  `Cartao`/`Pix`/`Boleto`) foi reaproveitado quase literalmente do `.tex`
  original.
