# Gabarito — Aula 12

Gabarito consolidado: justificativa analítica de cada item de V/F dos
exercícios finais (`index.qmd`) e a solução discutida de cada pausa
ativa da aula. Nunca publicado no site (prefixo `_`).

## Pausas Ativas

### Pausa 1 — O Antipadrão do Status e a Fragilidade de Evolução

**Pergunta motivadora:** Se um novo requisito pedir um estado
"EM_ANALISE_DE_FRAUDE" entre "NOVO" e "PAGO" no `Pedido` do antipadrão,
quantos métodos já existentes precisam ser abertos e editados — e o
que esse número revela sobre a real causa da fragilidade do design?

**Discussão:** Três métodos precisam de edição — `pagar()`,
`cancelar()` e `enviar()` — porque todos os três verificam o campo
`status` internamente antes de decidir o que fazer. Trocar o tipo de
`status` de `String` para `enum` eliminaria o risco de um valor
inválido, mas não eliminaria a necessidade de editar os três métodos:
o problema estrutural não é o tipo do campo, é a lógica de transição
estar fisicamente espalhada por vários métodos que também carregam
regra de negócio não relacionada ao fluxo. Esse número (três, não um)
revela que a causa real da fragilidade não é "faltam mais `if`s" — é a
ausência de um único lugar responsável por decidir o fluxo.

**V/F resolvido:**
- ✗ No `Pedido` do antipadrão, inserir um novo estado exige editar apenas o método `pagar()`, já que é o único que decide a transição de "NOVO" para "PAGO".
- ✔ Um teste unitário que verifica "cancelar um pedido já pago dispara estorno" precisa, antes de chamar `cancelar()`, montar um `Pedido` cujo campo `status` já esteja manualmente ajustado para `"PAGO"`.
- ✗ Se o tipo do campo `status` fosse trocado de `String` para um `enum` Java, isso sozinho eliminaria a necessidade de abrir `pagar()`, `cancelar()` e `enviar()` ao adicionar um estado novo.
- ✔ A fragilidade de evolução do `Pedido` do antipadrão nasce do fato de a lógica de transição de estado estar fisicamente distribuída dentro de vários métodos que também contêm lógica de negócio não relacionada ao fluxo.

---

### Pausa 2 — Strategy vs. State: Mesma Topologia, Intenções Diferentes

**Pergunta motivadora:** Se alguém disser que o State Pattern é apenas
"um Strategy com nomes diferentes", por que essa afirmação, apesar de
a topologia de classes ser quase idêntica, erra o ponto central da
intenção arquitetural de cada padrão?

**Discussão:** A afirmação confunde "mesma forma de classes" com
"mesma intenção arquitetural". No Strategy, a troca de implementação é
decidida por um agente **externo** ao Contexto — o código cliente que
chama `setEstrategia(...)`; a estratégia concreta nunca se
autossubstitui. No State, é o próprio objeto de estado atual —
`EstadoNovo`, por exemplo — quem decide e executa a transição para
`EstadoPago` como efeito colateral de processar uma operação de
negócio (`pagar()`), sem que nenhum código cliente externo precise
invocar a troca. A estrutura de classes (interface + implementações)
é necessária, mas não suficiente, para definir o padrão: o que
diferencia os dois é *quem* decide qual implementação está ativa e
*quando* essa decisão acontece — não o número de métodos da interface.

**V/F resolvido:**
- ✗ Em um `CalculadoraDeFrete` que usa Strategy, é o próprio objeto `FreteExpresso` injetado que decide, sozinho e sem intervenção externa, substituir-se por `FreteGratis` durante a execução do sistema.
- ✔ Num `Pedido` usando State, é fisicamente o objeto `EstadoNovo` — e não um código cliente externo chamando `pedido.setEstrategia(new EstadoPago())` — quem invoca a transição para `EstadoPago` como consequência de `pagar()` ter sido chamado.
- ✗ Se um `ConcreteState` do padrão State fosse instanciado e injetado manualmente por código cliente externo antes de qualquer operação de negócio ocorrer no Contexto, essa prática ainda preservaria integralmente a intenção arquitetural original do State Pattern.
- ✗ O fato de tanto Strategy quanto State definirem uma interface implementada por múltiplas classes concretas é suficiente, por si só, para classificá-los como o mesmo padrão de projeto sob nomes diferentes.

---

### Pausa 3 — O Dilema da Herança no Adapter

**Pergunta motivadora:** Se o `LogAdapter` decidisse estender
(`extends`) `LogServicoLegado` em vez de compô-lo por injeção, que
capacidade futura o sistema perderia especificamente quando o
fornecedor lançasse uma nova subclasse de `LogServicoLegado`?

**Discussão:** O sistema perderia a capacidade de reaproveitar
automaticamente a nova subclasse. Um Object Adapter (composição)
continua funcionando sem alteração nenhuma quando o objeto injetado no
construtor é substituído por uma subclasse do legado — ele trata o
legado, e qualquer subclasse dele, como uma caixa preta acessada só
pela API pública, via polimorfismo. Um Class Adapter (`extends`), por
outro lado, está preso via herança a uma única classe-mãe fixa em
tempo de compilação; uma nova subclasse do fornecedor exigiria
escrever um segundo Adapter dedicado só para ela. A mesma composição
que garante essa flexibilidade também é o que permite, em teste
automatizado, substituir o legado real por um objeto simulado (*mock*)
sem alterar o `LogAdapter` — vantagem que a herança anularia.

**V/F resolvido:**
- ✔ Um `LogAdapter` construído por composição (Object Adapter) continua funcionando corretamente mesmo que o objeto injetado no construtor seja, na verdade, uma subclasse de `LogServicoLegado` lançada pelo fornecedor depois que o `LogAdapter` já havia sido escrito.
- ✔ Um `LogAdapter` que estendesse `LogServicoLegado` (Class Adapter) precisaria ser reescrito ou duplicado para conseguir adaptar especificamente uma nova subclasse do legado, mesmo que essa subclasse só adicionasse um método novo sem alterar `registrarLogNoArquivo`.
- ✔ Trocar `LogServicoLegado legado` por uma injeção via construtor no `LogAdapter` (em vez de herança) é o que permite substituir, em um teste automatizado, o legado real por uma versão simulada (*mock*) sem alterar o código do `LogAdapter`.
- ✗ Se `LogServicoLegado` expusesse um método `protected` usado internamente por suas próprias subclasses, um `LogAdapter` implementado como Object Adapter teria acesso direto a esse método da mesma forma que um Class Adapter teria.

## Exercícios de V/F

### O Antipadrão do Status como Primitivo — item (a)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um método que verifica `if (status.equals("PAGO"))` como primeira instrução antes de executar qualquer lógica de negócio caracteriza o mesmo tipo de acoplamento temporal descrito para o antipadrão do `Pedido`, independentemente de o valor de `status` ser uma `String` ou um `enum`.

**Resposta:** Verdadeiro

**Justificativa:** O acoplamento temporal (a obrigação de reconstruir corretamente o estado interno antes de invocar um método) nasce de o método verificar sua própria pré-condição via um campo de estado — isso é independente do tipo desse campo. Trocar `String` por `enum` só elimina valores inválidos, não a estrutura do problema.

### O Antipadrão do Status como Primitivo — item (b)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um sistema de emissão de boletos que usa um campo `int codigoSituacao` (0 = emitido, 1 = pago, 2 = vencido) verificado em cinco métodos diferentes da mesma classe está estruturalmente exposto ao mesmo padrão de fragilidade de evolução descrito para o `Pedido`.

**Resposta:** Verdadeiro

**Justificativa:** É o mesmo antipadrão transferido para outro domínio: a lógica de transição de estado espalhada por vários métodos da mesma classe, em vez de concentrada num único lugar, é o que causa a fragilidade — não importa se o campo se chama `status` ou `codigoSituacao`, nem se é `String` ou `int`.

### O Antipadrão do Status como Primitivo — item (c)

**Heurística:** Caso limite/extremo

**Afirmação:** ✗ Se um novo estado for adicionado a um sistema que usa o antipadrão de status-como-primitivo, o compilador Java emitirá um erro de compilação em todo método que não trate explicitamente esse novo estado.

**Resposta:** Falso

**Justificativa:** Um campo `String`/`int` verificado por cadeias de `if/else` não oferece nenhuma garantia de exaustividade em tempo de compilação — um método que simplesmente não considera o novo estado compila normalmente e falha silenciosamente em tempo de execução. É exatamente essa ausência de rede de segurança do compilador que agrava a fragilidade do antipadrão.

### O Antipadrão do Status como Primitivo — item (d)

**Heurística:** Contrafactual

**Afirmação:** ✔ Testar isoladamente a transição "de PAGO para CANCELADO dispara estorno" num sistema que usa o antipadrão de status exige reconstruir manualmente o estado interno do objeto antes de invocar o método sob teste, ao contrário do que ocorreria com uma implementação via State Pattern.

**Resposta:** Verdadeiro

**Justificativa:** No antipadrão, só existe uma classe `Pedido`; testar o comportamento de "pago" exige montar um `Pedido` inteiro com `status="PAGO"` antes de chamar `cancelar()`. Com State, `EstadoPago.cancelar(pedido)` pode ser exercitado isolando a classe de estado diretamente, sem reconstruir o ciclo de vida completo do objeto.

### Estrutura do Padrão State (Context/State/ConcreteState) — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ No padrão State, o método responsável por trocar a referência de estado no Contexto (`setEstado`) deveria ser público, para que qualquer código cliente externo pudesse forçar uma transição arbitrária sempre que necessário.

**Resposta:** Falso

**Justificativa:** Deixar `setEstado` livremente público para qualquer cliente externo reintroduz exatamente o mecanismo de injeção externa que caracteriza o Strategy, esvaziando a intenção do State — que é o próprio fluxo de negócio, através dos `ConcreteState`, decidir e executar suas próprias transições.

### Estrutura do Padrão State (Context/State/ConcreteState) — item (b)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Se `EstadoNovo.enviar()` lançasse uma exceção informando que o pedido ainda não foi pago, essa exceção estaria expressando uma regra de negócio genuína do domínio, e não um defeito de implementação do padrão State.

**Resposta:** Verdadeiro

**Justificativa:** É a mesma lógica de Fail-Fast/Design by Contract já estudada: uma pré-condição de negócio ("não se envia o que não foi pago") sendo enforced no ponto exato onde é violada. A exceção é o padrão funcionando como esperado, não um sintoma de mau design.

### Estrutura do Padrão State (Context/State/ConcreteState) — item (c)

**Heurística:** Caso limite/extremo

**Afirmação:** ✗ Depois de aplicado o State Pattern, a complexidade ciclomática da classe `Pedido` aumenta em relação à versão com `if/else`, porque agora ela precisa gerenciar referências para múltiplas classes de estado diferentes.

**Resposta:** Falso

**Justificativa:** O efeito é o oposto: a complexidade ciclomática de `Pedido` **cai**, porque as cadeias condicionais somem dos seus métodos — `Pedido` passa a apenas delegar (`estadoAtual.pagar(this)`). A complexidade não desaparece do sistema, mas se distribui entre classes pequenas e coesas, cada uma com um único caminho de execução.

### Estrutura do Padrão State (Context/State/ConcreteState) — item (d)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um `Pedido` que armazena `EstadoPedido estadoAtual` e delega `pagar()` para `estadoAtual.pagar(this)` permite que o comportamento de `pagar()` mude completamente ao longo da vida do objeto sem que o código-fonte do método `pagar()` no `Pedido` seja alterado uma única vez.

**Resposta:** Verdadeiro

**Justificativa:** É o Open/Closed Principle em ação via polimorfismo: o comportamento efetivo de `pagar()` muda conforme `estadoAtual` muda de referência, mas o código-fonte do método `pagar()` do `Pedido` — a linha `estadoAtual.pagar(this)` — nunca precisa ser reaberto.

### Strategy vs. State: Mesma Topologia, Intenções Diferentes — item (a)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um sistema de checkout onde o cliente escolhe explicitamente, no carrinho, qual `EstrategiaFrete` usar, e onde o `Pedido` decide sozinho, como consequência de um pagamento bem-sucedido, transitar de `EstadoNovo` para `EstadoPago`, está aplicando Strategy e State no mesmo sistema para dois problemas arquiteturais distintos.

**Resposta:** Verdadeiro

**Justificativa:** O critério que distingue os dois padrões — quem decide a troca de implementação, e quando — está presente de forma limpa nesse cenário: escolha externa e explícita (Strategy) para o frete, auto-transição interna como efeito colateral de negócio (State) para o ciclo de vida do pedido. Nada impede os dois coexistirem no mesmo sistema, para problemas diferentes.

### Strategy vs. State: Mesma Topologia, Intenções Diferentes — item (b)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se um engenheiro implementasse o State de forma que um código cliente externo chamasse `pedido.forcarEstado(new EstadoPago())` livremente a qualquer momento, essa implementação preservaria a intenção arquitetural original do padrão da mesma forma que a implementação vista em aula.

**Resposta:** Falso

**Justificativa:** Essa implementação reintroduz o mecanismo de injeção externa característico do Strategy, esvaziando o ponto central do State: o objeto decidir e mudar sua própria "personalidade" como efeito colateral do seu próprio fluxo de negócio, não por ordem externa arbitrária.

### Strategy vs. State: Mesma Topologia, Intenções Diferentes — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ A razão pela qual Strategy e State não são o mesmo padrão sob nomes diferentes está exclusivamente no número de métodos que a interface de cada um declara, e não em quem decide a troca de implementação.

**Resposta:** Falso

**Justificativa:** É exatamente o oposto: a estrutura de classes (interface + implementações concretas) é necessária, mas não suficiente, para definir o padrão. O que realmente diferencia Strategy de State é *quem* decide qual implementação está ativa e *quando* — não a forma sintática da interface.

### Strategy vs. State: Mesma Topologia, Intenções Diferentes — item (d)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um `ConcreteState` que, ao processar uma operação de negócio, decide autonomamente instanciar e ativar o próximo estado da máquina está exercendo o mesmo papel decisório que, no Strategy, pertence ao código cliente que injeta a estratégia no Contexto.

**Resposta:** Verdadeiro

**Justificativa:** É a inversão exata do lugar da decisão entre os dois padrões: no Strategy, o cliente externo decide e injeta; no State, o próprio `ConcreteState` assume esse papel decisório internamente, como consequência do processamento de negócio.

### Onde Colocar a Lógica de Transição — item (a)

**Heurística:** Caso limite/extremo

**Afirmação:** ✗ Centralizar a decisão de qual é o próximo estado dentro de um método do Contexto (Opção B) elimina completamente a necessidade de estruturas condicionais em qualquer parte do sistema.

**Resposta:** Falso

**Justificativa:** Centralizar a decisão no Contexto não elimina condicionais — apenas as move para um único lugar (o método do Contexto que decide o próximo estado), em vez de removê-las do sistema por completo.

### Onde Colocar a Lógica de Transição — item (b)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Fazer com que `EstadoNovo` conheça diretamente a classe `EstadoPago` (Opção A) introduz um acoplamento entre classes de estado que é aceitável quando a sequência de transições já reflete uma regra de negócio estável e conhecida.

**Resposta:** Verdadeiro

**Justificativa:** Todo design é uma troca: acoplar `EstadoNovo` a `EstadoPago` diretamente custa flexibilidade, mas ganha simplicidade — uma troca aceitável quando a sequência de transições é uma regra de negócio fixa e já conhecida, não algo que mude com frequência.

### Onde Colocar a Lógica de Transição — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Uma técnica em que o método de transição retorna o próximo estado (`this.estado = estado.proximo();`) permite ao Contexto atualizar sua referência sem conter uma cadeia de `if/else` comparando o tipo do estado atual.

**Resposta:** Verdadeiro

**Justificativa:** Delegar ao próprio estado a responsabilidade de determinar (e retornar) o próximo estado é o que permite ao Contexto ficar com uma única linha de atribuição polimórfica, sem precisar perguntar "que tipo de estado é esse?" através de uma cadeia condicional.

### Onde Colocar a Lógica de Transição — item (d)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se a ordem de transições de um sistema mudasse com muita frequência por decisão de negócio (por exemplo, um fluxo de aprovação configurável por cliente), a Opção A (transição fixa nos estados) seria estruturalmente mais adequada do que uma tabela de transições configurável mantida fora das classes de estado.

**Resposta:** Falso

**Justificativa:** É o oposto: quando a sequência de transições muda com frequência por decisão de negócio, fixá-la no código-fonte das classes de estado (Opção A) exige reabrir e recompilar classes a cada mudança — uma tabela de transições configurável, mantida fora do código, se adapta sem exigir nova compilação.

### O Ciclo de Vida Robusto e o Polimorfismo em Ação — item (a)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ O fato de `EstadoPago.cancelar()` chamar `realizarEstornoFinanceiro()` antes de mudar o estado, enquanto `EstadoNovo.cancelar()` apenas muda o estado sem estornar nada, é uma expressão direta do polimorfismo substituindo uma cadeia de `if (status == ...)`.

**Resposta:** Verdadeiro

**Justificativa:** Cada `ConcreteState` implementa `cancelar()` com o comportamento específico que faz sentido para aquele estado — sem que nenhum código precise perguntar "qual é o status atual?" antes de decidir o que fazer. Isso é exatamente o papel do polimorfismo substituindo condicionais.

### O Ciclo de Vida Robusto e o Polimorfismo em Ação — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Se `EstadoEnviado.cancelar()` lança uma exceção proibindo o cancelamento, isso significa que o padrão State, ao contrário do antipadrão original, não é capaz de expressar a regra de negócio "produtos em trânsito não podem ser cancelados".

**Resposta:** Falso

**Justificativa:** É exatamente o oposto: lançar a exceção é a forma como o State expressa essa regra de negócio, de forma isolada e explícita dentro de `EstadoEnviado`, sem misturar essa lógica com o comportamento de nenhum outro estado.

### O Ciclo de Vida Robusto e o Polimorfismo em Ação — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um desenvolvedor que precisa entender o que acontece quando um pedido pago é cancelado, ao usar o State Pattern, encontra essa resposta isolada dentro da classe `EstadoPago`, sem precisar ler os outros estados.

**Resposta:** Verdadeiro

**Justificativa:** Essa localidade de leitura é uma das vantagens centrais do State sobre o antipadrão: o comportamento de "cancelar quando pago" mora inteiramente em `EstadoPago.cancelar()`, sem exigir que o leitor percorra um método monolítico com ramos para todos os estados possíveis.

### O Ciclo de Vida Robusto e o Polimorfismo em Ação — item (d)

**Heurística:** Caso limite/extremo

**Afirmação:** ✗ Adicionar um novo estado "EM_ANALISE_DE_FRAUDE" ao sistema baseado em State Pattern exige alterar o código-fonte de `EstadoNovo`, `EstadoPago` e `EstadoEnviado` da mesma forma que exigiria no antipadrão original baseado em `String status`.

**Resposta:** Falso

**Justificativa:** No antipadrão, os três métodos do `Pedido` monolítico precisam ser reabertos igualmente. Com State, só as classes diretamente envolvidas na transição para/a partir do novo estado precisam mudar (tipicamente só `EstadoNovo`, que passaria a poder transitar para o novo estado) — estados sem relação direta, como `EstadoEnviado`, podem permanecer intocados.

### O Dilema da Incompatibilidade e o Papel do Adapter — item (a)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ O padrão Adapter resolve especificamente o problema de uma interface externa incompatível com o contrato que o domínio já usa, sem exigir alteração nem do código do fornecedor externo, nem do código cliente que já confia na interface esperada.

**Resposta:** Verdadeiro

**Justificativa:** É a definição central do padrão: o Adapter absorve a tradução numa terceira classe nova, preservando intacto tanto o código do fornecedor (muitas vezes nem sequer disponível para alteração) quanto o código cliente já escrito contra a interface esperada.

### O Dilema da Incompatibilidade e o Papel do Adapter — item (b)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se a equipe decidisse modificar diretamente as classes de negócio centrais para chamar os métodos nativos do sistema legado de auditoria, essa prática produziria o mesmo nível de isolamento arquitetural que o uso de um Adapter produziria.

**Resposta:** Falso

**Justificativa:** Modificar as classes de negócio para chamar diretamente a API do legado contamina o modelo de domínio com detalhes de infraestrutura voláteis — exatamente o oposto do isolamento que o Adapter produz ao concentrar essa dependência numa única classe de fronteira.

### O Dilema da Incompatibilidade e o Papel do Adapter — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ No `LogAdapter`, o parâmetro de severidade fixo (`1`) passado para `registrarLogNoArquivo` é um detalhe de tradução que o Adapter absorve, evitando que ele precise ser conhecido por todas as classes de negócio que disparam eventos de log.

**Resposta:** Verdadeiro

**Justificativa:** Detalhes de tradução como códigos numéricos fixos exigidos pela API legada são exatamente o tipo de "número mágico" que o Adapter encapsula, evitando que se espalhe por todas as classes de negócio que precisam registrar eventos.

### O Dilema da Incompatibilidade e o Papel do Adapter — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Um Adapter, por definição do padrão, deve alterar o comportamento interno de pelo menos uma das duas interfaces que ele está harmonizando para que a tradução funcione corretamente.

**Resposta:** Falso

**Justificativa:** O Adapter nunca altera o comportamento interno de nenhum dos dois lados — ele só traduz chamadas na fronteira entre eles, delegando para a implementação real depois de adaptar a assinatura/formato da chamada.

### Object Adapter vs. Class Adapter — item (a)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um `LogAdapter` implementado como Object Adapter continua funcionando sem nenhuma alteração de código se o objeto `LogServicoLegado` injetado no construtor for substituído por uma subclasse dele lançada pelo fornecedor após o Adapter já estar em produção.

**Resposta:** Verdadeiro

**Justificativa:** Por composição, o Adapter só depende da API pública declarada pelo tipo `LogServicoLegado` — qualquer subclasse válida (presente ou futura) satisfaz esse contrato via polimorfismo, sem exigir nenhuma alteração no `LogAdapter`.

### Object Adapter vs. Class Adapter — item (b)

**Heurística:** Contrafactual

**Afirmação:** ✗ Um `LogAdapter` implementado como Class Adapter (via `extends LogServicoLegado`) consegue adaptar automaticamente qualquer subclasse futura do legado, porque a herança propaga essa capacidade para toda a árvore de classes.

**Resposta:** Falso

**Justificativa:** É o oposto: `extends` fixa o Adapter, em tempo de compilação, a uma única classe-mãe específica. Uma nova subclasse lançada pelo fornecedor exigiria escrever um Class Adapter dedicado a ela — a herança não propaga essa capacidade automaticamente.

### Object Adapter vs. Class Adapter — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ A principal razão pela qual a indústria prefere o Object Adapter é estética — o código fica mais curto — e não uma diferença estrutural de acoplamento entre as duas abordagens.

**Resposta:** Falso

**Justificativa:** A preferência é estrutural, não estética: o Object Adapter (composição) desacopla o Adapter da implementação concreta do legado, permite reaproveitar subclasses futuras e facilita testes com mocks — vantagens de acoplamento, não de brevidade de código.

### Object Adapter vs. Class Adapter — item (d)

**Heurística:** Contrafactual

**Afirmação:** ✗ Substituir a composição (`private LogServicoLegado legado`) por herança (`extends LogServicoLegado`) no `LogAdapter` tornaria mais fácil, e não mais difícil, substituir o legado real por um objeto simulado (*mock*) em um teste automatizado.

**Resposta:** Falso

**Justificativa:** É o oposto: composição via injeção de construtor é o que permite passar um mock no lugar do objeto real em teste; substituir por herança elimina esse ponto de injeção, tornando a substituição por mock mais difícil, não mais fácil.

### Estudo de Caso: Unificação de Log e a Fronteira com o State — item (a)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Se `EstadoPago` chamar `pedido.getLogger().info(...)` para registrar uma transição, essa classe de estado permanece livre de qualquer conhecimento sobre a existência de `LogServicoLegado`.

**Resposta:** Verdadeiro

**Justificativa:** `EstadoPago` conhece só a abstração de logging exposta pelo `Pedido` — o `LogAdapter` (e o `LogServicoLegado` que ele encapsula) fica inteiramente escondido atrás dessa fronteira, exatamente o isolamento que o Adapter existe para produzir.

### Estudo de Caso: Unificação de Log e a Fronteira com o State — item (b)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Se o fornecedor do sistema de auditoria legado mudar a assinatura de `registrarLogNoArquivo` de `(String, int)` para `(String, String)`, um sistema que usa `LogAdapter` corretamente precisaria alterar apenas a classe `LogAdapter`, sem tocar em nenhuma classe de estado do `Pedido`.

**Resposta:** Verdadeiro

**Justificativa:** Toda a dependência do formato exato da API legada está concentrada dentro do `LogAdapter` — uma mudança de assinatura do lado do fornecedor se resolve editando só essa classe de fronteira, sem se propagar para as classes de estado que só conhecem a interface abstrata de logging.

### Estudo de Caso: Unificação de Log e a Fronteira com o State — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ A combinação de State (para o fluxo interno) e Adapter (para a fronteira externa) na mesma classe `EstadoPago` representa uma violação do princípio de que cada classe deve aplicar exatamente um único padrão de projeto.

**Resposta:** Falso

**Justificativa:** Não existe tal princípio: padrões de projeto resolvem problemas arquiteturais ortogonais entre si, e nada impede uma mesma classe de participar de mais de um padrão simultaneamente — aqui, `EstadoPago` participa do State (decidindo sua própria transição) e, ao delegar uma chamada de log, se beneficia do Adapter que outra classe implementa.

### Estudo de Caso: Unificação de Log e a Fronteira com o State — item (d)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um sistema onde `Pedido` recebe um `LoggerModerno` por injeção de dependência, em vez de instanciar diretamente `new LogServicoLegado()` dentro de suas classes de estado, permite substituir o logger por um *mock* em testes automatizados sem alterar as classes de estado.

**Resposta:** Verdadeiro

**Justificativa:** É a mesma vantagem de testabilidade já vista com Strategy, Factory Method e o próprio Adapter: injetar a dependência via construtor, em vez de instanciá-la diretamente, é o que abre espaço para trocar a implementação real por um mock em teste, sem tocar no código das classes de estado.
