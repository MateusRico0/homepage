# Fontes usadas — Aula 5

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

## Notas sobre as fontes

- Duas referências pontuais aparecem sem PDF symlinkado: Chidamber &
  Kemerer (1994, métricas CK/CBO) e Glenford Myers (escala de
  acoplamento) — citações de conceito, não aprofundadas com página exata.
- O código de exemplo (`Pedido`/`Carrinho`, `Notificacao`, `Cliente`/
  `Cartao`/`Pix`/`Boleto`) foi reaproveitado quase literalmente do `.tex`
  original.
