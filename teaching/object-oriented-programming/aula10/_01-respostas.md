# Gabarito — Aula 10

Gabarito consolidado: a solução discutida de cada pausa ativa da aula.
O gabarito das questões de Verdadeiro/Falso dos exercícios finais é
público, em `soluções.qmd`. Nunca publicado no site (prefixo `_`).

## Pausas Ativas

### Pausa 1 — O Colapso da Hierarquia e a Explosão Combinatória

**Pergunta motivadora:** Se hoje o e-commerce adicionasse um terceiro
eixo de variação (Perecível vs. Não-Perecível) ainda usando herança
pura, quantas classes-folha existiriam — e por que dobrar de 4 para 8
não é o pior problema dessa abordagem?

**Discussão:** Cada eixo binário adicional multiplica (não soma) o
número de combinações possíveis: com 2 eixos binários já temos
$2 \times 2 = 4$ folhas (`FisicoNacional`, `FisicoImportado`,
`DigitalNacional`, `DigitalImportado`); um terceiro eixo binário eleva
isso para $2^3 = 8$. Mas o número de classes, por si só, não é a pior
consequência — é sintoma de um problema mais grave: a regra fiscal de
produtos importados (a lógica que diferencia `FisicoImportado` de
`FisicoNacional`) precisa ser **duplicada** em cada folha que representa
um produto importado, porque a herança simples não tem como
compartilhar essa regra entre `FisicoImportado` e `DigitalImportado`
sem recorrer à herança múltipla — que o Java proíbe. O resultado prático
é que uma mudança na lei fiscal (por exemplo, uma nova alíquota)
precisa ser replicada manualmente em múltiplos arquivos, com alto risco
de esquecer um deles e deixar o sistema com regras fiscais
inconsistentes entre produtos físicos e digitais importados.

**V/F resolvido:**
- ✔ Em uma hierarquia de herança pura que já modela dois eixos binários independentes com 4 subclasses-folha, a adição de um terceiro eixo binário eleva esse número para 8, mantendo a mesma lógica de crescimento.
- ✗ Se Java permitisse herança múltipla de classes sem nenhuma outra mudança de linguagem, o problema de duplicação de lógica fiscal entre `FisicoImportado` e `DigitalImportado` desapareceria completamente, sem risco de ambiguidade.
- ✔ Um sistema de biblioteca que precisa classificar itens simultaneamente por Formato (Físico/Digital) e por Categoria de Empréstimo (Curto Prazo/Longo Prazo) enfrentaria o mesmo padrão de explosão combinatória se modelado por herança de classes pura.
- ✗ Herança de classes é uma ferramenta inadequada para qualquer sistema que apresente mais de uma característica variável, mesmo quando essas características não são independentes entre si (por exemplo, quando uma determina totalmente a outra).

---

### Pausa 2 — Composição, Agregação e Associação

**Pergunta motivadora:** Por que dizer que o Carrinho "tem" Produtos
(Agregação) e o Cliente "usa" um Cartão de Crédito (Associação) leva a
decisões de código diferentes sobre quem cria e quem destrói cada
objeto?

**Discussão:** A diferença entre Agregação e Associação não é de
vocabulário — é sobre **quem é responsável pelo ciclo de vida** de cada
objeto envolvido na relação. Numa Agregação (`CarrinhoDeCompras`/
`Produto`), o "Todo" agrupa referências às partes, mas as partes têm
existência própria fora dessa relação: o código de exclusão de um
carrinho nunca deveria disparar a exclusão dos produtos no estoque —
eles pertencem, em última instância, ao catálogo, não ao carrinho. Numa
Associação (`Cliente`/`CartaoDeCredito`), a autonomia é ainda maior: nem
sequer existe uma direção de posse — o cartão pode ser criado, migrado
entre contas ou encerrado por um sistema bancário completamente
independente do ciclo de vida do cliente que o está usando no momento.
Codificar essa distinção corretamente evita dois erros simétricos:
apagar em cascata algo que deveria sobreviver (deletar produtos do
estoque ao esvaziar um carrinho) ou deixar um objeto "órfão" sem dono
claro quando na verdade ele deveria ter um ciclo de vida amarrado a
outro.

**V/F resolvido:**
- ✔ Se todos os Produtos de um Carrinho fossem deletados do sistema no exato instante em que o Carrinho é deletado, essa relação deixaria de ser uma Agregação clássica e passaria a se comportar como Composição estrita.
- ✗ Se o Cliente fosse implementado de forma que a existência do CartaoDeCredito dependesse inteiramente do Cliente (o cartão nunca poderia existir sem aquele cliente específico), essa relação ainda seria corretamente descrita como Associação livre.
- ✔ Uma classe Playlist que agrupa referências a Musica, mas cujas músicas continuam existindo na biblioteca mesmo depois que a Playlist é apagada, exemplifica o mesmo padrão de Agregação visto no Carrinho de Compras.
- ✗ Aplicar o princípio do Especialista da Informação significa que toda funcionalidade relacionada, de qualquer forma, a um objeto deve ser implementada dentro dele, mesmo que envolva conectar-se a servidores externos.

---

### Pausa 3 — O Padrão Strategy e o Princípio Aberto/Fechado

**Pergunta motivadora:** Se amanhã a loja quiser aceitar pagamento via
Criptomoeda, por que a resposta certa nunca deveria envolver abrir e
editar o arquivo `Pedido.java`?

**Discussão:** A resposta está no que exatamente `Pedido` conhece: ele
mantém uma referência ao tipo `Pagavel` (a abstração), nunca a uma
classe concreta como `Pix` ou `Cartao`. Toda a variação de comportamento
fica isolada dentro de quem implementa `Pagavel` — o `Pedido` só sabe
que, seja qual for o objeto injetado, ele responde a
`processarPagamento(double)`. Quando um novo meio de pagamento surge
(Criptomoeda), a única peça nova no sistema é uma classe que implementa
`Pagavel`; nenhuma linha de `Pedido` muda, porque `Pedido` nunca precisou
saber quantas nem quais implementações de `Pagavel` existem no mundo.
Isso é o Princípio Aberto/Fechado em estado puro: o sistema está aberto
para receber esse novo comportamento (basta escrever a classe nova) e
fechado para modificação do código já testado e em produção (`Pedido`
não é tocado, não precisa ser recompilado, e não corre risco de
regressão nas regras de Pix, Cartão ou Boleto que já funcionavam).

**V/F resolvido:**
- ✔ Se o Contexto (`Pedido`) precisasse verificar, com um `if`, se a estratégia injetada é uma instância de `Pix` antes de chamar `processarPagamento()`, isso indicaria que o padrão Strategy não foi implementado corretamente.
- ✗ Se a interface `Pagavel` não existisse e o `Pedido` dependesse diretamente da classe concreta `Pix`, ainda seria possível trocar a estratégia de pagamento em tempo de execução sem modificar o código de `Pedido`.
- ✔ Um sistema de notificações que aceita diferentes canais (`EmailNotificador`, `SmsNotificador`, `PushNotificador`) implementando uma interface comum `Notificador`, injetada no objeto que dispara os alertas, segue a mesma topologia Context/Strategy/ConcreteStrategy vista no pagamento.
- ✗ O Princípio Aberto/Fechado exige que uma classe nunca seja modificada depois de escrita, mesmo para corrigir um bug real dentro de sua própria lógica interna.
