# Gabarito — Aula 13

## Pausas Ativas (resolução em prosa)

### Pausa Ativa 1 — Explosão Combinatória

**Pergunta motivadora:** Se a cafeteria decidir oferecer 5 adicionais independentes (Leite, Chocolate, Chantilly, Canela, Mel), quantas classes distintas a estratégia de herança estática exigiria para representar todas as combinações possíveis — e o que esse número revela sobre por que "adicionar mais uma subclasse quando precisar" nunca é uma resposta sustentável nesse cenário?

Com 5 adicionais independentes, o número de combinações possíveis é $2^5 = 32$ (incluindo a combinação vazia, representada pelo `Cafe` puro). Esse número — muito maior do que os 5 adicionais em si — revela que o problema não é "faltam algumas subclasses", é que modelar cada *combinação* como uma classe é, por construção matemática, insustentável assim que o número de eixos independentes cresce: o crescimento é exponencial, não linear, então nenhuma quantidade razoável de "subclasses adicionadas sob demanda" alcança o total de combinações reais que os clientes poderão pedir.

- ✔ Se a cafeteria removesse a opção de combinar adicionais entre si (isto é, o cliente só pudesse escolher exatamente um adicional ou nenhum), o número de subclasses necessárias para representar todas as combinações cresceria linearmente com o número de adicionais, em vez de exponencialmente — sem combinação permitida, bastam $N+1$ classes (uma por adicional, mais a base); é precisamente a possibilidade de combinar que gera o crescimento exponencial visto no cenário original.
- ✔ No limite em que o número de adicionais independentes tende a infinito, a razão entre o número de subclasses exigidas pela herança estática e o número de adicionais oferecidos também tende a infinito — $2^N/N \to \infty$ quando $N \to \infty$: o crescimento exponencial supera qualquer crescimento linear de referência, por maior que seja a constante.
- ✔ Um sistema de seguros que precisa combinar de forma independente e cumulativa cobertura contra roubo, incêndio e desastres naturais em uma única apólice sofreria da mesma explosão combinatória se cada combinação de coberturas fosse modelada como uma subclasse de `Apolice` — mesma assinatura estrutural do problema (eixos independentes e cumulativos modelados como subclasses), domínio diferente.
- ✗ Para 5 adicionais independentes, a estratégia de herança estática exigiria exatamente 5 subclasses novas, uma para cada adicional individual, sem necessidade de subclasses para as combinações entre eles — falso: são $2^5 = 32$ combinações possíveis (incluindo a ausência de qualquer adicional), não 5; é exatamente essa confusão entre "número de adicionais" e "número de combinações possíveis entre eles" que subestima o tamanho real do problema.

**Voltando à pergunta:** $2^5 = 32$ classes seriam necessárias — um número que expõe, de forma concreta, por que a herança estática é insustentável diante de eixos de variação independentes e cumulativos: o crescimento é exponencial em relação ao número de adicionais, não linear, e por isso nenhuma estratégia de "adicionar uma subclasse por vez, conforme a necessidade surge" alcança essa combinatória.

### Pausa Ativa 2 — A Recursão e a Transparência do Decorator

**Pergunta motivadora:** Se, no exemplo do `NotificadorComRetry` envolvendo um `NotificadorComLog` que por sua vez envolve um `NotificadorEmail`, o método `enviar()` for chamado na camada mais externa, em que ordem exatamente a lógica de cada camada é executada — e o que essa ordem revela sobre por que o cliente nunca precisa saber quantas camadas existem?

A chamada desce do mais externo (`NotificadorComRetry`) para o mais interno (`NotificadorEmail`): `NotificadorComRetry.enviar()` executa sua lógica de retry e, dentro do laço, chama `super.enviar()` — que é o `enviar()` de `NotificadorComLog` — que registra o log e então chama `super.enviar()` — que é o `enviar()` de `NotificadorEmail`, que efetivamente envia a mensagem. Cada camada só conhece a próxima camada imediatamente interna (guardada em `notificadorDecorado`), nunca o topo da pilha nem a composição completa. É exatamente essa "cegueira" de cada camada sobre o resto da cadeia que permite ao cliente empilhar, remover ou reordenar decoradores livremente sem que nenhuma classe precise saber quantas outras existem acima ou abaixo dela.

- ✗ Se `BebidaDecorator` não implementasse a interface `Bebida`, mas apenas contivesse uma referência interna a um objeto `Bebida`, ainda seria possível empilhar `Leite` sobre `Chocolate` da mesma forma transparente que o padrão Decorator permite hoje — falso: sem implementar `Bebida` (o lado É-UM), o decorador não poderia ser passado como argumento para outro decorador nem tratado polimorficamente pelo código cliente; a transparência do padrão exige as duas relações — É-UM e TEM-UM — simultaneamente.
- ✔ Se um `Cafe` puro (sem nenhum decorador aplicado) tiver seu `getCusto()` chamado diretamente, o resultado é idêntico ao que se obteria encadeando zero decoradores em torno dele — o caso de zero camadas de wrapping é apenas o caso degenerado da mesma recursão — a recursão do Decorator sempre termina no objeto núcleo; com zero decoradores aplicados, a "recursão" se reduz trivialmente à própria chamada direta sobre `Cafe`.
- ✔ Um sistema de processamento de texto que permite aplicar, de forma independente e em qualquer ordem, negrito, itálico e sublinhado sobre um texto-base poderia usar a mesma estrutura de Decorator vista para `Bebida`, com cada estilo implementado como uma classe que envolve o texto anterior — exemplo clássico de transferência do mesmo mecanismo de composição em camadas para outro domínio.
- ✗ Como o `BufferedInputStream` decora qualquer `InputStream`, incluindo outro `BufferedInputStream` já aplicado, envolver um fluxo já bufferizado com um segundo `BufferedInputStream` automaticamente dobra a velocidade de leitura, já que dois buffers armazenam mais dados que um — falso: a flexibilidade estrutural do Decorator (poder envolver qualquer `InputStream`, inclusive outro decorador) não implica que toda composição traga benefício real; empilhar dois buffers redundantes tende só a adicionar overhead de cópia entre eles, sem ganho de desempenho proporcional.

### Pausa Ativa 3 — Push vs. Pull e a Escala Distribuída

**Pergunta motivadora:** Se um novo tipo de observador precisar, no futuro, de um dado que hoje não está entre os parâmetros enviados pelo modelo Push atual (por exemplo, o valor total do pedido), o que precisa mudar no sistema — e por que essa mesma pergunta, respondida de outro jeito, é exatamente o argumento a favor do modelo Pull?

Com o modelo Push atual (`aoFaturar(String id)`), adicionar um observador que precisa do valor total do pedido exigiria alterar a assinatura do método de notificação para incluir esse novo parâmetro — e essa mudança quebraria todos os observadores existentes que implementam a assinatura antiga e não esperam o parâmetro extra. É exatamente esse custo de refatoração em cascata que o modelo Pull evita: ao enviar apenas uma referência ao próprio Sujeito, cada observador (presente ou futuro) extrai exatamente os dados de que precisa via métodos públicos, sem forçar nenhuma mudança de assinatura sobre os observadores que já existem. O preço dessa flexibilidade é o acoplamento bidirecional: o observador passa a depender da API pública do Sujeito.

- ✔ Se o `PedidoSubject` usasse o modelo Pull (passando apenas a própria referência para `update(PedidoSubject pedido)`) em vez do modelo Push, adicionar um observador que precisa do valor total do pedido não exigiria alterar a assinatura do método de notificação já usado pelos observadores existentes — exatamente a vantagem central do Pull: o observador extrai o que precisa via *getters*, sem forçar mudança na assinatura do callback.
- ✔ Se o número de observadores registrados em um `PedidoSubject` crescer para um valor muito grande, o `Pedido` (o Sujeito) continua sem precisar conhecer o tipo concreto de nenhum deles, porque o `for` de broadcast opera apenas sobre a interface `PedidoObserver` — o grau de desacoplamento não depende da quantidade de observadores registrados, só da abstração usada para armazená-los e percorrê-los.
- ✔ Um sistema de sensores IoT que publica leituras de temperatura para múltiplos painéis de monitoramento, sem que o sensor conheça quantos ou quais painéis existem, está aplicando a mesma inversão de controle que o Observer aplica entre `PedidoSubject` e seus observadores — mesma estrutura publicador-assinante, domínio diferente.
- ✗ Migrar de um Observer local (dentro da mesma JVM) para uma Arquitetura Orientada a Eventos distribuída (com Kafka ou RabbitMQ) exige abandonar completamente o princípio de desacoplamento do Observer, já que agora os componentes rodam em processos e máquinas diferentes — falso: a topologia permanece conceitualmente idêntica ao migrar de escala; a EDA não abandona o desacoplamento do Observer, ela o escala — produtores e consumidores continuam desconhecendo a identidade física uns dos outros, exatamente como Sujeito e observadores locais.

## Exercícios — Justificativas de Verdadeiro/Falso

### A Explosão Combinatória e o Limite da Herança Estática — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se a cafeteria decidisse tratar cada adicional como um atributo booleano dentro da própria classe `Cafe`, em vez de como uma subclasse, o número de classes necessárias deixaria de crescer exponencialmente com o número de adicionais, mas a decisão de quais adicionais existem passaria a ser fixada em tempo de compilação dentro de `Cafe`.

**Resposta:** Verdadeiro

**Justificativa:** Usar atributos booleanos dentro de `Cafe` (`temLeite`, `temChocolate`, ...) de fato evita a explosão de subclasses — o número de classes deixa de depender do número de adicionais. Mas o conjunto de adicionais possíveis passa a estar fixado dentro do código-fonte de `Cafe`: adicionar um novo adicional exige editar essa classe e recompilá-la, uma forma diferente (mas real) de rigidez em tempo de compilação, ainda que sem explosão combinatória de classes.

### A Explosão Combinatória e o Limite da Herança Estática — item (b)

**Heurística:** Caso limite

**Afirmação:** ✔ Se a cafeteria oferecesse apenas 1 adicional opcional, o número de subclasses exigido pela herança estática seria idêntico ao que a mesma situação exigiria sob o padrão Decorator (uma classe para representar o objeto simples, outra para o objeto com o adicional).

**Resposta:** Verdadeiro

**Justificativa:** Com $N=1$, a herança estática exige $2^1=2$ classes (`Cafe` e `CafeComLeite`), e o Decorator também usaria 2 classes (`Cafe` e `Leite`, mais a classe abstrata `BebidaDecorator`, que é infraestrutura reutilizável, não específica de um adicional). No caso trivial de um único adicional, as duas estratégias empatam em número de classes por adicional — é só quando o número de adicionais cresce que a herança diverge exponencialmente enquanto o Decorator continua crescendo linearmente (uma classe nova por adicional, não por combinação).

### A Explosão Combinatória e o Limite da Herança Estática — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um editor de imagens que aplica filtros (preto-e-branco, sépia, desfoque) de forma independente e cumulativa sobre uma foto sofreria do mesmo tipo de explosão combinatória se cada combinação de filtros fosse modelada como uma subclasse de `Imagem`.

**Resposta:** Verdadeiro

**Justificativa:** A assinatura estrutural do problema é idêntica à da cafeteria: filtros opcionais, cumulativos e combináveis livremente, modelados como subclasses, geram $2^N$ combinações para $N$ filtros — exatamente o mesmo colapso, em outro domínio.

### A Explosão Combinatória e o Limite da Herança Estática — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Bastaria usar interfaces em vez de classes abstratas para representar `CafeComLeite`, `CafeComChocolate` etc. para eliminar a explosão combinatória, já que interfaces não sofrem do mesmo problema de herança múltipla que classes sofrem em Java.

**Resposta:** Falso

**Justificativa:** O problema da explosão combinatória não nasce da distinção classe/interface, nasce de modelar cada *combinação* de adicionais como um tipo à parte. Trocar `extends` por `implements` não muda o fato de que ainda seria preciso um tipo (classe ou interface) para cada uma das $2^N$ combinações possíveis — o número de tipos necessários continuaria exponencial.

### Estrutura do Decorator: Wrapping, É-UM e TEM-UM — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se `Leite` chamasse `bebidaDecorada.getCusto()` diretamente no seu construtor, em vez de dentro do método `getCusto()` sobrescrito, o custo acumulado refletiria apenas o valor do objeto decorado no momento da criação de `Leite`, não permitindo que mudanças posteriores no objeto interno fossem refletidas em chamadas futuras.

**Resposta:** Verdadeiro

**Justificativa:** Calcular e guardar o custo no construtor "congelaria" o valor no momento da criação; qualquer mutação posterior no objeto decorado (por exemplo, uma promoção aplicada depois) não seria refletida, porque o `getCusto()` de `Leite` retornaria o valor armazenado, não recalcularia via delegação. É por isso que o padrão delega a cada chamada, dentro do próprio método, e não uma única vez no construtor.

### Estrutura do Decorator: Wrapping, É-UM e TEM-UM — item (b)

**Heurística:** Caso limite

**Afirmação:** ✔ Se um cliente empilhasse dez decoradores `Leite` seguidos sobre o mesmo `Cafe` (`new Leite(new Leite(... new Cafe() ...))`), o custo final refletiria dez incrementos de R$ 1,50 aplicados sucessivamente, mesmo sem existir nenhuma subclasse dedicada a "café com dez leites".

**Resposta:** Verdadeiro

**Justificativa:** Cada camada de `Leite` soma seu próprio acréscimo de forma independente — a recursão simplesmente atravessa dez camadas em vez de uma. Nenhuma classe nova é necessária para esse caso extremo, o que evidencia a vantagem central do Decorator sobre a herança estática: a quantidade de camadas é uma decisão de runtime, não de projeto de classes.

### Estrutura do Decorator: Wrapping, É-UM e TEM-UM — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um sistema de permissões que envolve um `Usuario` base com decoradores como `PermissaoAdmin` e `PermissaoAuditor`, cada um acrescentando checagens de acesso ao redor do usuário original, estaria aplicando a mesma estrutura É-UM/TEM-UM vista em `BebidaDecorator`.

**Resposta:** Verdadeiro

**Justificativa:** A mesma dualidade estrutural se aplica: cada decorador de permissão implementaria a interface do `Usuario` (É-UM) e conteria uma referência ao usuário decorado (TEM-UM), permitindo empilhar checagens de acesso de forma cumulativa e transparente ao código cliente.

### Estrutura do Decorator: Wrapping, É-UM e TEM-UM — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como o Decorator implementa a mesma interface do objeto que envolve, um decorador concreto nunca deveria sobrescrever um método herdado de `BebidaDecorator`, pois isso quebraria o repasse puro que define o padrão.

**Resposta:** Falso

**Justificativa:** É exatamente o oposto: o repasse puro é o comportamento **padrão** de `BebidaDecorator` (a classe abstrata), mas cada decorador concreto (`Leite`, `Chocolate`) *precisa* sobrescrever os métodos para acrescentar seu próprio comportamento sobre o repasse (via `super.getCusto() + acréscimo`) — sem essa sobrescrita, o decorador não teria nenhum efeito observável.

### A Recursão no Decorator: `BebidaDecorator` e `Leite` — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se `Cafe.getCusto()` retornasse um valor diferente a cada chamada (por exemplo, por causa de uma promoção aleatória), uma cadeia `new Chocolate(new Leite(new Cafe()))` ainda produziria um resultado consistente com a soma dos acréscimos de cada camada sobre o valor retornado por `Cafe` naquela chamada específica.

**Resposta:** Verdadeiro

**Justificativa:** O mecanismo de delegação recursiva não depende de `Cafe.getCusto()` ser determinístico — cada chamada de `getCusto()` na cadeia dispara uma nova descida até `Cafe`, e o valor que ele retornar naquele instante é o que sobe acumulando os acréscimos de `Leite` e `Chocolate`. A consistência está no mecanismo (soma sobre o valor retornado *naquela* chamada), não na estabilidade do valor de `Cafe` entre chamadas diferentes.

### A Recursão no Decorator: `BebidaDecorator` e `Leite` — item (b)

**Heurística:** Caso limite

**Afirmação:** ✔ Na cadeia `new Chocolate(new Leite(new Cafe()))`, se removêssemos a chamada `super.getCusto()` de dentro do método `getCusto()` de `Chocolate`, o valor final retornado ignoraria completamente o custo acumulado por `Leite` e por `Cafe`, refletindo apenas o acréscimo do próprio `Chocolate`.

**Resposta:** Verdadeiro

**Justificativa:** `super.getCusto()` é exatamente o elo que conecta a camada atual com o valor acumulado por todas as camadas internas. Removê-lo quebra a cadeia recursiva no ponto de `Chocolate`: o método deixa de descer para `Leite`/`Cafe` e retorna apenas o valor que `Chocolate` adicionaria, um caso-limite que expõe a dependência estrutural do padrão em relação a essa chamada.

### A Recursão no Decorator: `BebidaDecorator` e `Leite` — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Uma pilha (`Stack`) de chamadas de função em qualquer linguagem de programação, na qual cada função retorna depois de invocar a próxima, compartilha a mesma lógica estrutural de "delegar para dentro e acumular ao retornar" que a cadeia de decoradores usa para calcular `getCusto()`.

**Resposta:** Verdadeiro

**Justificativa:** A pilha de chamadas de função é a mesma estrutura recursiva geral que o Decorator usa deliberadamente para acumular valores: descer delegando, subir acumulando — o Decorator apenas dá nome e reuso a essa estrutura no contexto de composição dinâmica de objetos.

### A Recursão no Decorator: `BebidaDecorator` e `Leite` — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como cada decorador concreto soma um valor fixo ao custo do objeto que envolve, a ordem em que os decoradores são empilhados (`new Chocolate(new Leite(new Cafe()))` vs. `new Leite(new Chocolate(new Cafe()))`) sempre produz um custo final diferente.

**Resposta:** Falso

**Justificativa:** Para operações puramente aditivas sobre um número (soma de acréscimos fixos), a ordem das camadas não altera o resultado final — a soma é comutativa. `getCusto()` produziria R$ 8,50 em qualquer uma das duas ordens. (Isso contrasta deliberadamente com o exemplo do `NotificadorComRetry`/`NotificadorComLog`, bloco seguinte, onde a ordem das camadas *sim* muda o comportamento observável, porque a operação ali não é aditiva/comutativa.)

### Decorator no Mundo Real: `java.io` e a Cadeia de Notificadores — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se `BufferedInputStream` estendesse diretamente `FileInputStream` em vez de decorar a interface `InputStream`, o mesmo `BufferedInputStream` não poderia ser usado para adicionar buffer a um `SocketInputStream` (leitura de rede) sem duplicar código.

**Resposta:** Verdadeiro

**Justificativa:** Herdar diretamente de `FileInputStream` prenderia `BufferedInputStream` a essa única classe concreta em tempo de compilação; para bufferizar um `SocketInputStream`, seria preciso criar uma segunda classe (`BufferedSocketInputStream`), duplicando a lógica de buffer. Decorar a interface `InputStream` é o que permite ao mesmo `BufferedInputStream` envolver qualquer implementação concreta.

### Decorator no Mundo Real: `java.io` e a Cadeia de Notificadores — item (b)

**Heurística:** Caso limite

**Afirmação:** ✔ Se um `NotificadorComRetry` envolvesse um `NotificadorComLog`, que por sua vez envolvesse um `NotificadorEmail`, e a tentativa de envio falhasse repetidamente até esgotar as tentativas de retry, o log registrado pelo `NotificadorComLog` ainda seria disparado a cada tentativa individual, não apenas uma vez ao final.

**Resposta:** Verdadeiro

**Justificativa:** Como `NotificadorComLog` está na camada logo abaixo de `NotificadorComRetry`, cada iteração do laço de retry chama `super.enviar()`, que é o `enviar()` de `NotificadorComLog` — portanto o log é registrado uma vez por tentativa, não uma única vez ao final da série de tentativas.

### Decorator no Mundo Real: `java.io` e a Cadeia de Notificadores — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um pipeline de processamento de dados que envolve uma fonte de dados bruta com camadas sucessivas de validação, transformação e cache, cada uma implementando a mesma interface da anterior, está aplicando a mesma lógica de composição em camadas vista em `BufferedInputStream` e na cadeia de notificadores do `Pedido`.

**Resposta:** Verdadeiro

**Justificativa:** Mesma estrutura de composição recursiva em camadas, aplicada a um domínio de pipeline de dados em vez de streams de I/O ou notificações — cada camada adiciona uma responsabilidade e delega para a camada interna.

### Decorator no Mundo Real: `java.io` e a Cadeia de Notificadores — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como `NotificadorComLog` e `NotificadorComRetry` decoram a mesma interface `Notificador`, a ordem em que são aplicados (log por fora do retry, ou retry por fora do log) é irrelevante para o comportamento observável do sistema.

**Resposta:** Falso

**Justificativa:** A ordem muda o comportamento observável: com `NotificadorComRetry` por fora (como no exemplo da aula), o log dispara a cada tentativa de reenvio; com `NotificadorComLog` por fora, o log dispararia uma única vez, antes de todas as tentativas de retry ocorrerem internamente. Diferente do custo aditivo do exemplo da bebida, esta composição não é comutativa.

### O Acoplamento de Notificação em Cascata — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se `Pedido.fecharPedido()` recebesse `EmailService`, `LogService` e `InventarioService` por injeção de dependência via construtor, em vez de instanciá-los internamente, isso sozinho já eliminaria a necessidade de editar `Pedido` sempre que um canal de notificação novo (como SMS) for adicionado.

**Resposta:** Falso

**Justificativa:** Injeção de dependência resolve o problema de acoplamento a implementações concretas (permite trocar `EmailService` por um mock, por exemplo), mas não resolve o problema estrutural do OCP aqui em jogo: `Pedido` ainda precisaria de um novo campo e uma nova linha de chamada dentro de `fecharPedido()` para cada canal novo, mesmo que os serviços existentes sejam injetados. Só uma lista de abstrações percorrida em broadcast (Observer) elimina essa necessidade de editar `Pedido`.

### O Acoplamento de Notificação em Cascata — item (b)

**Heurística:** Caso limite

**Afirmação:** ✗ Se `Pedido` precisasse notificar zero subsistemas periféricos (nenhum e-mail, log ou atualização de estoque), a arquitetura de dependências diretas do exemplo original ainda seria uma violação do OCP, mesmo sem nenhuma chamada real no corpo de `fecharPedido()`.

**Resposta:** Falso

**Justificativa:** A violação do OCP se manifesta como a necessidade de *modificar* `Pedido` quando um requisito novo aparece. Sem nenhuma notificação a fazer, não há ainda nenhuma dependência concreta codificada em `Pedido`, logo não há violação a apontar nesse estado — o problema só se manifesta no momento em que o primeiro (ou um novo) canal de notificação precisa ser adicionado.

### O Acoplamento de Notificação em Cascata — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Uma função de checkout de e-commerce que, após confirmar um pagamento, chama diretamente APIs de frete, de fidelidade e de recomendação de produtos dentro do mesmo método, sofre do mesmo tipo de acoplamento de notificação em cascata descrito para o `Pedido`.

**Resposta:** Verdadeiro

**Justificativa:** Mesma assinatura estrutural: um método de negócio central que conhece e invoca diretamente múltiplos subsistemas periféricos, tornando-se refém das assinaturas e da disponibilidade de cada um deles.

### O Acoplamento de Notificação em Cascata — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ O problema do `Pedido` com `EmailService`/`LogService`/`InventarioService` é resolvido simplesmente movendo as três chamadas para um método privado separado dentro da própria classe `Pedido`, já que isso reduz o tamanho do método `fecharPedido()`.

**Resposta:** Falso

**Justificativa:** Extrair as chamadas para um método privado melhora a organização/legibilidade local, mas não remove o acoplamento: `Pedido` ainda conhece e depende diretamente das três classes concretas, e ainda precisaria ser editado (mesmo que só nesse método privado) para adicionar um canal novo — a violação do OCP permanece intacta.

### Estrutura do Observer: Subject, Observer e Broadcast — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se `PedidoSubject.observadores` fosse declarado como `List<EmailService>` em vez de `List<PedidoObserver>`, ainda seria possível registrar um `SmsService` nessa lista, desde que `SmsService` implementasse a interface `PedidoObserver`.

**Resposta:** Falso

**Justificativa:** O sistema de tipos do Java não permite: uma `List<EmailService>` só aceita instâncias de `EmailService` (ou subclasses dela). `SmsService` implementar `PedidoObserver` não o torna um `EmailService`; ele só poderia ser adicionado a uma lista tipada como `List<PedidoObserver>` — exatamente por isso o Sujeito deve depender da interface, não de uma classe concreta.

### Estrutura do Observer: Subject, Observer e Broadcast — item (b)

**Heurística:** Caso limite

**Afirmação:** ✔ Se a lista `observadores` de `PedidoSubject` estiver vazia no momento em que `faturar()` é chamado, o método ainda executa corretamente a lógica de negócio principal, apenas sem disparar nenhuma notificação.

**Resposta:** Verdadeiro

**Justificativa:** O laço `for` sobre uma lista vazia simplesmente não itera nenhuma vez; a lógica de negócio (processar o faturamento) roda normalmente antes do laço e é completamente independente de haver ou não observadores registrados — mais uma evidência do desacoplamento entre regra de negócio e notificação.

### Estrutura do Observer: Subject, Observer e Broadcast — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um sistema de notícias que mantém uma lista de assinantes de uma newsletter, notificando todos eles sempre que um novo artigo é publicado, sem saber se o assinante é uma pessoa física ou um outro sistema automatizado, está aplicando a mesma estrutura Subject/Observer vista no `PedidoSubject`.

**Resposta:** Verdadeiro

**Justificativa:** Mesma topologia um-para-muitos com anonimato de identidade concreta do lado dos assinantes — o publicador (fonte de notícias) só conhece a interface de notificação comum, exatamente como `PedidoSubject` só conhece `PedidoObserver`.

### Estrutura do Observer: Subject, Observer e Broadcast — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Registrar um observador em `PedidoSubject` usando `registrar(PedidoObserver o)` cria necessariamente uma dependência do `PedidoSubject` em relação à classe concreta do observador registrado, da mesma forma que ocorria na versão original com `EmailService` fixo.

**Resposta:** Falso

**Justificativa:** É exatamente o oposto — o parâmetro do método `registrar` é tipado como `PedidoObserver` (a interface), então `PedidoSubject` nunca referencia nem depende da classe concreta de quem é registrado; essa é precisamente a diferença estrutural que elimina a dependência direta presente na versão original com `EmailService` fixo.

### Push vs. Pull: Estratégias de Tráfego de Dados — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se o modelo Push do `PedidoSubject` já enviasse tanto o `id` quanto o valor total do pedido como parâmetros de `aoFaturar(String id, double valor)`, adicionar um observador que só precisa do `id` não exigiria nenhuma mudança na assinatura da interface `PedidoObserver`.

**Resposta:** Verdadeiro

**Justificativa:** Uma vez que a assinatura já inclui os dois parâmetros, qualquer observador (existente ou novo) pode simplesmente ignorar o parâmetro que não usa — o problema do Push só aparece quando um observador precisa de um dado que a assinatura *ainda não inclui*, forçando uma mudança que quebraria os observadores já existentes.

### Push vs. Pull: Estratégias de Tráfego de Dados — item (b)

**Heurística:** Caso limite

**Afirmação:** ✔ No modelo Pull, se o objeto `Subject` passado para `update(Subject s)` não expuser nenhum método público além de construtores, o observador fica impossibilitado de extrair qualquer dado relevante, tornando a notificação praticamente inútil.

**Resposta:** Verdadeiro

**Justificativa:** O modelo Pull depende inteiramente da API pública do Sujeito para que o observador consiga extrair dados; sem nenhum *getter* público exposto, não há como o observador obter informação alguma a partir da referência recebida, evidenciando o caso-limite em que o Pull falha por falta de superfície pública.

### Push vs. Pull: Estratégias de Tráfego de Dados — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um sistema de sensores que envia, a cada leitura, apenas um identificador do sensor que mudou (modelo Pull), deixando o painel de monitoramento responsável por consultar o valor atual da temperatura, sofre do mesmo tipo de acoplamento bidirecional descrito para o modelo Pull do Observer.

**Resposta:** Verdadeiro

**Justificativa:** O painel precisa conhecer a API pública do sensor para consultar o valor — exatamente o acoplamento bidirecional sutil descrito para o modelo Pull: o observador passa a depender da interface pública do sujeito.

### Push vs. Pull: Estratégias de Tráfego de Dados — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como o modelo Pull é mais flexível a longo prazo do que o Push, ele deveria ser sempre preferido, independentemente de quão homogêneas e estáveis sejam as necessidades de dados dos observadores.

**Resposta:** Falso

**Justificativa:** A escolha entre Push e Pull é um trade-off, não uma hierarquia absoluta: quando as necessidades de dados dos observadores são homogêneas e bem conhecidas, o Push é mais simples e direto, sem o custo do acoplamento bidirecional que o Pull introduz. Preferir sempre um dos dois ignora o contexto que motiva a escolha.

### Do Observer Local à Arquitetura Orientada a Eventos — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se um sistema trocasse seu `PedidoSubject` local por um Produtor de Eventos publicando em um tópico Kafka, os Consumidores de Eventos ainda poderiam, em princípio, permanecer completamente alheios à identidade física uns dos outros, da mesma forma que os observadores locais não conheciam a identidade concreta uns dos outros.

**Resposta:** Verdadeiro

**Justificativa:** A topologia permanece conceitualmente idêntica ao migrar de escala — o desacoplamento entre observadores (ou consumidores) é uma propriedade da estrutura publicador/canal/assinante, preservada independentemente de os assinantes estarem na mesma JVM ou em processos distintos.

### Do Observer Local à Arquitetura Orientada a Eventos — item (b)

**Heurística:** Caso limite

**Afirmação:** ✔ Se um sistema distribuído tiver um único Consumidor de Eventos assinando um único tópico, a topologia ainda é conceitualmente uma aplicação do padrão Observer, mesmo com apenas um assinante em vez de muitos.

**Resposta:** Verdadeiro

**Justificativa:** A relação "um-para-muitos" do Observer degenera, no caso limite de um único assinante, em "um-para-um" sem deixar de ser uma aplicação válida do padrão — o mecanismo de desacoplamento (publicador não conhece assinante concreto) continua presente independentemente da cardinalidade.

### Do Observer Local à Arquitetura Orientada a Eventos — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um sistema de biblioteca que notifica automaticamente todos os leitores inscritos em uma fila de espera assim que um livro é devolvido, sem que o sistema de devolução saiba quantos leitores estão na fila, está aplicando a mesma lógica de mapeamento Sujeito→Produtor de Eventos vista na evolução do Observer para EDA.

**Resposta:** Verdadeiro

**Justificativa:** Mesma lógica de publicador que dispara um evento (devolução) para uma lista de interessados sem conhecê-los individualmente — mapeável diretamente para Sujeito→Produtor de Eventos, Observadores→Consumidores.

### Do Observer Local à Arquitetura Orientada a Eventos — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Migrar do Observer local para uma Arquitetura Orientada a Eventos distribuída elimina a necessidade de definir contratos (interfaces/esquemas de mensagem) entre publicador e consumidores, já que o barramento de mensagens absorve toda a responsabilidade de comunicação.

**Resposta:** Falso

**Justificativa:** O barramento de mensagens transporta os eventos, mas não elimina a necessidade de um contrato compartilhado sobre o formato/esquema dessas mensagens — produtor e consumidores ainda precisam concordar sobre a estrutura dos dados publicados, o análogo distribuído da interface `PedidoObserver` do Observer local.
