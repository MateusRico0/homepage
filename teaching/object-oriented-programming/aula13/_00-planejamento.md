## Resumo — Aula 13

A Aula 12 fechou o "tríptico da estabilidade" do objeto por dentro (dado, gênese, fluxo) e abriu a primeira fronteira externa do sistema com o Adapter. Esta aula completa o quarteto de padrões estruturais/comportamentais do curso com mais duas peças, ambas sobre **estrutura dinâmica em tempo de execução**: o **Decorator**, que resolve — por composição, no runtime — o mesmo problema de explosão combinatória que a herança estática já havia gerado (Aula 10), agora aplicado a um único objeto que precisa acumular responsabilidades opcionais; e o **Observer**, que resolve o acoplamento de notificação entre um objeto núcleo e um número variável de subsistemas periféricos que precisam reagir às suas mudanças de estado, sem que o núcleo os conheça. Os dois padrões compartilham o mesmo espírito — "trocar uma estrutura rígida decidida em tempo de compilação por uma estrutura flexível decidida em tempo de execução" — e por isso formam um par natural: o exemplo de fechamento do Decorator (uma cadeia de notificadores do `Pedido`) é reaproveitado como o próprio cenário-problema que abre o Observer, criando uma transição sem costura entre as duas metades da aula.

**Pré-requisitos (conferidos no dicionário de `_progresso.md` e no resumo da Aula 12):** a explosão combinatória e "favoreça composição sobre herança" (Aula 10); o vocabulário GoF e as três famílias de padrões (Aula 11); OCP (Aula 10); a cegueira deliberada do State/Adapter perante detalhes que não lhes dizem respeito (Aula 12); `PedidoObserver`/`EmailService` ainda não introduzidos — nome livre para esta aula.

**Objetivos de aprendizagem:** (1) reconhecer o limite estrutural da herança estática diante de responsabilidades opcionais e cumulativas, e quantificar a explosão combinatória ($2^N$); (2) projetar um Decorator (interface comum, decorator abstrato com repasse, decoradores concretos com `super.metodo()` + acréscimo) e explicar a dualidade É-UM/TEM-UM que o sustenta; (3) reconhecer o Decorator no ecossistema real (`java.io`) e replicar o mesmo raciocínio num domínio próprio; (4) diagnosticar o acoplamento de notificação em cascata como violação do OCP; (5) projetar um Observer (Subject/Observer, registro e broadcast) e articular a inversão de controle que ele produz; (6) comparar os modelos de tráfego de dados Push e Pull e seus trade-offs de acoplamento; (7) mapear a topologia local do Observer para uma Arquitetura Orientada a Eventos distribuída.

**Estratégia Pedagógica:** Estratégia A (Outside-In) — como nas Aulas 9–12, o objeto de estudo são dois padrões de projeto nomeados; a aula parte do antipadrão procedural concreto (explosão de subclasses; cascata de chamadas diretas a serviços) para só depois nomear e formalizar a solução (Decorator, Observer).

## Plano de aula — Aula 13 (carga horária: ~115 min)

1. **Abertura: Revisão e Introdução** (~10 min) — revisão do tríptico interno (Strategy/Builder/State) e da primeira fronteira externa (Adapter) fechados na Aula 12; ideia-ponte: hoje, duas peças finais compartilham o mesmo espírito — trocar decisão de compilação por decisão de runtime, uma para um único objeto (Decorator), outra para a comunicação entre vários objetos (Observer); roteiro de 4 perguntas; problema motivador (cafeteria com opcionais de bebida). Pausa Ativa 1.
2. **O Limite da Herança Estática e a Explosão Combinatória** (~15 min) — cenário da cafeteria (`Cafe`, `Leite`, `Chocolate`, `Chantilly`), a armadilha taxonômica (`CafeComLeite`, `CafeComLeiteEChocolate`, ...), a fórmula $2^N$, o sintoma de rigidez e repetição. Termina com a pergunta "e se pudéssemos envolver o objeto em camadas, decididas uma a uma, em tempo de execução?", que o bloco seguinte resolve.
3. **O Padrão Decorator: Estrutura, Wrapping e Transparência** (~20 min) — definição do GoF, a estrutura de "cebola", a dualidade É-UM/TEM-UM, a interface `Bebida`, a classe `BebidaDecorator` (repasse puro) e o decorador concreto `Leite` (`super.getCusto() + acréscimo`); diagrama TikZ da estrutura recursiva de wrapping. Transparência: o cliente não distingue objeto núcleo de objeto decorado.
4. **Análise da Recursão, o Mundo Real (Java I/O) e a Cadeia de Notificadores** (~20 min) — caminhada passo a passo da chamada recursiva `getCusto()` através das camadas; o exemplo consagrado `BufferedInputStream`/`FileInputStream` do `java.io`; réplica do mesmo raciocínio no domínio do curso — uma cadeia de notificadores do `Pedido` (`Notificador`/`NotificadorEmail`/`NotificadorComLog`/`NotificadorComRetry`), que planta a semente do problema do próximo bloco. Pausa Ativa 2 ao final.
5. **Ponte: da Fronteira de um Objeto ao Acoplamento entre Objetos** (~5 min) — o Decorator resolveu como um único objeto acumula responsabilidades; mas o `Pedido` ainda tem outro problema, ortogonal: ele conhece diretamente cada serviço periférico que precisa notificar (e-mail, log, estoque) — motivação do Observer.
6. **O Perigo do Acoplamento de Notificação e o Padrão Observer** (~20 min) — o `Pedido` com `EmailService`/`LogService`/`InventarioService` como dependências diretas, o efeito cascata, a violação do OCP (novo canal = editar `Pedido`); definição do GoF, a topologia Subject/Observer, o código `PedidoObserver`/`EmailService`/`PedidoSubject` com registro e broadcast; a inversão de controle.
7. **Estratégias de Dados (Push vs. Pull) e do Observer Local à Arquitetura Distribuída** (~15 min) — o trade-off Push (simples, rígido) vs. Pull (flexível, acopla o observador à API do sujeito); o mapeamento Sujeito→Produtor de Eventos, interface de callback→Tópicos/Filas, Observador→Consumidor/Microsserviço (Kafka/RabbitMQ). Pausa Ativa 3.
8. **Fechamento** (~10 min) — retomar as 4 perguntas da abertura; nomear o que fica em aberto (a Síntese Arquitetural — fronteiras estável/volátil, matriz de decisão dos quatro padrões, conclusão do curso) para a Aula 14.

**Lógica de transição entre blocos:** o Bloco 2 termina com uma pergunta sem resposta ("e se envolvêssemos o objeto em camadas?") que o Bloco 3 resolve nomeando o Decorator. O Bloco 4 fecha o arco do Decorator mas seu último exemplo (cadeia de notificadores do `Pedido`) é reaproveitado literalmente como abertura do Bloco 6 — a mesma classe de cenário (notificação de eventos do `Pedido`), agora com um problema diferente (múltiplos observadores independentes, não uma pilha de responsabilidades sobre o mesmo objeto). O Bloco 6 termina estabelecendo a estrutura, mas deixa em aberto "como o Sujeito decide o que enviar?" — o Bloco 7 resolve com Push/Pull e depois escala a discussão para sistemas distribuídos.

## Fontes usadas — Aula 13

### Fonte 1: `Teoria/Aula 10.tex`, `\section{O Padrão Decorator e a Composição Dinâmica}`, linhas 399–553

**Uso pretendido:** todo o conteúdo do padrão Decorator desta aula — a explosão combinatória da herança estática, a estrutura de "cebola" (wrapping) e a dualidade É-UM/TEM-UM, a implementação `Bebida`/`BebidaDecorator`/`Leite`, e o exemplo real do `java.io` (`BufferedInputStream`/`FileInputStream`).

**Trechos citados literalmente (o material desta disciplina já está em português no original — não é tradução de livro em inglês):**

> "Até este ponto da disciplina, enfatizámos que a composição oferece mais flexibilidade do que a herança. O padrão Decorator leva esse argumento ao extremo, resolvendo o problema de adicionar responsabilidades a objetos individuais de forma dinâmica, sem afetar outros objetos da mesma classe e sem recorrer à criação de uma árvore de herança gigantesca e ingovernável."

> "Este design colapsa rapidamente devido à explosão combinatória. À medida que novos adicionais são introduzidos, o número de subclasses cresce exponencialmente ($2^N$). Se a cafeteria passar a oferecer 10 adicionais diferentes, o sistema precisará de mais de mil classes apenas para representar as combinações possíveis."

> "A solução do Decorator é tratar os adicionais não como tipos filiados à classe mãe, mas como 'envelopes' (ou wrappers) que envolvem o objeto original. A grande sacada arquitetural do Decorator está na sua estrutura de tipos dupla: ele É-UM (implementa a interface do componente) ao mesmo tempo em que ele TEM-UM (contém uma instância da mesma interface)."

> "Como todos os componentes — tanto o núcleo quanto os envelopes — assinam a mesmíssima interface, o código cliente que invoca os métodos permanece completamente alheio a quantas camadas de decoração foram empilhadas."

> "A classe BebidaDecorator é o coração técnico do padrão. Sendo abstrata, ela implementa a interface Bebida e obriga a passagem de um objeto Bebida em seu construtor. Seus métodos padrão fazem apenas o repasse puro das chamadas para o objeto interno."

> "Essa mesma lógica foi utilizada pelos engenheiros da Sun Microsystems ao desenharem o pacote java.io. [...] Em vez de criarem uma classe rígida chamada BufferedFileInputStream via herança, eles criaram a classe genérica BufferedInputStream, que estende e decora qualquer tipo de InputStream."

### Fonte 2: `Teoria/Aula 10.tex`, `\section{O Padrão Observer e o Desacoplamento de Eventos}`, linhas 555–743

**Uso pretendido:** todo o conteúdo do padrão Observer desta aula — o perigo do acoplamento de notificação/efeito cascata, a estrutura Subject/Observer, o código `PedidoObserver`/`EmailService`/`PedidoSubject`, as estratégias Push vs. Pull, e a escala do Observer local até a Arquitetura Orientada a Eventos distribuída.

**Trechos citados literalmente:**

> "O problema surge quando uma ação realizada no núcleo do sistema dispara um efeito cascata que exige a atualização ou notificação de múltiplos subsistemas periféricos. [...] Se o negócio decidir incluir o envio de uma mensagem WhatsApp ou uma notificação Push sempre que um pedido for fechado, o engenheiro de software será forçado a abrir o ficheiro Pedido.java para injetar um novo serviço."

> "A solução para quebrar o vínculo rígido de notificações é a aplicação do padrão Observer. Ele estabelece uma relação de dependência do tipo um-para-muitos baseada no anonimato de quem recebe. [...] O fluxo de controle é invertido: em vez de o Pedido controlar ativamente o comportamento do EmailService, os serviços secundários passam a subscrever voluntariamente o ciclo de vida do Pedido."

> "Ao analisarmos a classe PedidoSubject, notamos que o array interno armazena referências para a interface PedidoObserver e não para as classes de infraestrutura diretamente. [...] Se precisarmos de remover o envio de e-mails do sistema, basta deixar de registar o objeto correspondente na inicialização. A classe PedidoSubject permanece intacta e imutável, respeitando plenamente o Open/Closed Principle."

> "No modelo Push, o Sujeito assume o papel ativo de empacotar as informações relevantes e passá-las como parâmetros diretamente na assinatura do método de notificação. [...] Mudar a assinatura da interface para adicionar novos parâmetros quebrará todas as classes de observadores já existentes."

> "Como alternativa, o modelo Pull propõe um fluxo invertido. O método de notificação passa apenas uma referência genérica do próprio objeto Sujeito. [...] ele introduz um acoplamento bidirecional sutil: o observador agora precisa conhecer a interface pública do sujeito para extrair os dados."

> "Quando migramos para sistemas distribuídos de alta disponibilidade e microsserviços, a topologia permanece conceitualmente idêntica, mas as ferramentas mudam de escala. O Sujeito local transforma-se no Produtor de Eventos [...] A lista interna de observadores é substituída por um barramento de mensagens ou Message Broker robusto (como Apache Kafka ou RabbitMQ)."

> "'O Observer é o átomo fundamental que viabiliza sistemas reativos distribuídos.'"

**Nota de escopo (não usado nesta aula, decisão de divisão detalhada no `_progresso.md` da disciplina):** `\section{Síntese Arquitetural e o Estabelecimento de Fronteiras}` (linhas 745–827 de `Aula 10.tex`) — fronteiras estável/volátil, matriz de decisão comparando os quatro padrões (Strategy, Adapter, Decorator, Observer), e a conclusão da jornada de isolamento — fica para a Aula 14, que funciona como o fechamento/capítulo de síntese do curso. O `\section*{Exercícios de Fixação: Aula 10}` (linhas 830+) foi consultado só como inspiração temática para os blocos de V/F desta aula, não reaproveitado verbatim (a maioria de seus itens é definicional, formato proibido pelo `CLAUDE.md` desta disciplina).
