## Resumo — Aula 12

A Aula 11 fechou dois dos três pilares do "tríptico da estabilidade": o **dado** (Value Object) e a **gênese** (Builder, Factory Method). Esta aula fecha o terceiro pilar — o **fluxo** — com o padrão **State**, e em seguida abre a fronteira externa do sistema com o padrão **Adapter**. O `Pedido`, já purificado pelo Strategy (Aula 10) e pelo Builder (Aula 11), ainda controla seu ciclo de vida (`Novo → Pago → Enviado → Cancelado`) através de uma `String status` e uma bateria de `if/else` — o mesmo antipadrão de Obsessão por Primitivos já combatido na Aula 11, agora aplicado ao *comportamento* em vez do *dado*. O State resolve isso convertendo cada fase do ciclo de vida numa classe polimórfica, com uma topologia de classes quase idêntica à do Strategy — o contraste deliberado entre os dois (mesma estrutura, intenção arquitetural oposta: algoritmo injetado de fora vs. comportamento que muda a si mesmo) é o fio condutor central do primeiro bloco de conteúdo novo. Na segunda metade, a aula muda de escopo: em vez de proteger o objeto por dentro, ataca o problema de uma fronteira que aponta para fora — como o sistema conversa com uma biblioteca de terceiros ou legada cuja interface não bate com o contrato que o domínio espera. O padrão **Adapter** resolve isso com uma camada de tradução, sem modificar nem o cliente nem o legado.

**Pré-requisitos (conferidos no dicionário de `_progresso.md` e no resumo da Aula 11):** Strategy e sua topologia Context/Strategy/ConcreteStrategy (Aula 10); OCP (Aula 10); Obsessão por Primitivos e Fail-Fast no construtor (Aula 11); Value Object/imutabilidade (Aula 11, contraste indireto — State é sobre comportamento mutável controlado, não dado imutável); vocabulário GoF e as três famílias de padrões, com State já anunciado como exemplo Comportamental e Adapter como exemplo Estrutural no diagrama de árvore da Aula 11.

**Objetivos de aprendizagem:** (1) reconhecer o antipadrão de máquina de estados codificada em `String`/`switch` e sua violação do OCP; (2) projetar um State Pattern (Context/State/ConcreteState) com delegação pura e transição segura; (3) articular com precisão por que State não é "Strategy com nome diferente", apesar da topologia de classes quase idêntica; (4) decidir onde colocar a lógica de transição entre estados (nos próprios estados vs. centralizada no Contexto), avaliando o trade-off de acoplamento; (5) reconhecer quando uma fronteira externa (SDK, biblioteca legada) exige um Adapter, e projetar um Object Adapter que isole essa tradução; (6) explicar por que a indústria prefere Object Adapter (composição) a Class Adapter (herança).

**Estratégia Pedagógica:** Estratégia A (Outside-In) — assim como as Aulas 9, 10 e 11, o objeto de estudo é um padrão de projeto (um "modelo" estrutural nomeado), não uma linguagem matemática de fundamentação; a aula parte do antipadrão procedural concreto (switch de status, SDK incompatível) para só depois nomear e formalizar a solução (State, Adapter).

## Plano de aula — Aula 12 (carga horária: ~110 min)

1. **Abertura: Revisão e Introdução** (~10 min) — revisão do tríptico (Value Object, Builder/Factory Method) fechado na Aula 11; ideia-ponte: hoje fechamos o terceiro pilar (fluxo) e abrimos a fronteira externa; roteiro de 4 perguntas; problema motivador (`Pedido` com `String status` e `if/else` em `pagar()`/`cancelar()`); Pausa Ativa 1.
2. **O Antipadrão do Status como Primitivo** (~15 min) — o método inchado com verificação de status na primeira linha, o acoplamento temporal, a fragilidade de evolução (novo estado = editar todos os métodos), reconexão explícita com a Obsessão por Primitivos da Aula 11 (agora aplicada ao comportamento). Termina com a pergunta "e se convertêssemos cada status numa classe?" que o bloco seguinte responde.
3. **O Padrão State: Estrutura e Delegação** (~25 min) — motivação (estados como "estratégias de comportamento"), estrutura Context/State/ConcreteState, o `Pedido` reescrito com `EstadoPedido`/`EstadoNovo`/`EstadoPago`, a "cegueira deliberada" do Contexto, diagrama TikZ do ciclo de vida (`Novo → Pago → Enviado`, com `Cancelado` acessível de `Novo` e `Pago` mas não de `Enviado`); contraste explícito Strategy vs. State (mesma topologia de classes, injeção externa vs. auto-mutação) com diagrama TikZ comparativo. Pausa Ativa 2 ao final.
4. **Onde Colocar a Transição, e o Ciclo de Vida Robusto** (~15 min) — Opção A (estados conhecem o próximo estado) vs. Opção B (Contexto centraliza a tabela), trade-off de acoplamento vs. condicionais; caso prático com `EstadoPago.cancelar()` disparando estorno e `EstadoEnviado.cancelar()` lançando exceção — fecha o arco do State mostrando o polimorfismo substituindo o `if (status == ...)` por completo.
5. **Ponte: da Fronteira Interna à Fronteira Externa** (~10 min) — o objeto agora se comporta corretamente por dentro (Strategy, Builder, State); mas o mundo externo (SDK de pagamento, biblioteca de log de terceiros) fala um protocolo diferente do que o domínio espera — motivação do Adapter via cenário de incompatibilidade de interfaces.
6. **O Padrão Adapter: Tradução de Protocolos** (~25 min) — o dilema do legado (não posso mudar o SDK, não devo contaminar meu domínio), estrutura do Adapter como tradutor posicionado na fronteira, Object Adapter vs. Class Adapter (por que a composição vence), estudo de caso de unificação de log (`LoggerModerno`/`LogServicoLegado`/`LogAdapter`) aplicado a eventos de transição de estado do `Pedido` (liga Adapter de volta ao State recém-visto). Diagrama TikZ da camada de tradução. Pausa Ativa 3.
7. **Fechamento** (~10 min) — retomar as 4 perguntas da abertura; nomear o que fica em aberto (Decorator, Observer, e a Síntese Arquitetural da Aula 10.tex) para a Aula 13+.

**Lógica de transição entre blocos:** o Bloco 2 termina com uma pergunta sem resposta ("e se cada status virasse uma classe?") que o Bloco 3 resolve nomeando o State. O Bloco 3 termina estabelecendo a estrutura, mas deixa em aberto "quem decide o próximo estado?" — o Bloco 4 resolve. O Bloco 4 fecha o arco interno do objeto; o Bloco 5 vira a câmera para fora (fronteira externa), motivando o Adapter que os Blocos 6 resolve.

## Fontes usadas — Aula 12

### Fonte 1: `Teoria/Aula 9.tex`, `\section{State Pattern}`, linhas 353–590

**Uso pretendido:** todo o conteúdo do padrão State desta aula — o antipadrão do switch/case, a motivação (estados como estratégias de comportamento), a estrutura Context/State/ConcreteState, a mecânica de delegação com `protected setEstado`, o dilema de onde colocar a lógica de transição, e o caso prático robusto (`EstadoPago`/`EstadoEnviado` com estorno e exceção de cancelamento proibido).

**Trechos citados literalmente (português original):**

> "O grande desafio em modelar objetos com ciclos de vida (como um Pedido, uma Conexão de Rede ou um Personagem de Jogo) é que eles reagem a estímulos de forma distinta em cada fase. Se tentarmos gerir isto de forma procedural, acabamos com métodos "inchados" onde a primeira linha é sempre uma verificação de status. Isto cria um acoplamento temporal: a ordem das chamadas importa, mas a lógica para garantir essa ordem está espalhada e escondida atrás de condicionais."

> "Reparem como o código acima é rígido. Cada novo estado adicionado ao sistema atua como uma "bomba" que obriga a mexer em todos os métodos que dependem de status. Além disso, a variável status (muitas vezes uma String ou um int) é um exemplo de Obsessão por Primitivos. Não há nada que impeça o programador de definir um status inválido por engano. O padrão State surge para converter este controlo de fluxo em estrutura de objetos."

> "A motivação central do State é a limpeza arquitetural. Ao transformarmos cada estado numa classe polimórfica, isolamos o comportamento. O Context (ex: um Player de música) passa a ser apenas um hospedeiro que delega todas as ações para um objeto de estado. Quando o estado muda, o objeto hospedeiro simplesmente aponta para uma nova instância de uma classe diferente. Isto permite que o sistema cresça horizontalmente: novos estados significam novas classes, não novos ifs."

> "Evolução da aula anterior: Se o Strategy injeta algoritmos, o State permite que o objeto mude de classe (em efeito) durante o tempo de execução."

> "O ponto chave é o método setEstado. Ele é tipicamente marcado como protected ou com visibilidade de pacote para que apenas as classes de estado (que geralmente residem no mesmo pacote) possam disparar transições. Isto impede que o cliente externo mude o estado do pedido de forma arbitrária (ex: saltar de "Novo" diretamente para "Entregue"), preservando a integridade da máquina de estados."

> "Esta é a decisão de design mais difícil no State Pattern. Se o EstadoA instancia o EstadoB, eles tornam-se dependentes. No entanto, para processos de negócio onde o passo B segue obrigatoriamente o A, esta é a forma mais limpa de modelar."

> "Uma técnica avançada para evitar o acoplamento entre estados é usar uma Factory de Estados ou fazer com que o método de estado retorne o próximo estado, deixando para o Contexto apenas a tarefa de atualizar a referência: this.estado = estado.proximo();."

> "Neste exemplo, vemos o polimorfismo em ação. [...] Tudo isso sem um único if (status == ...). O código torna-se auto-documentado: se você quer saber o que acontece quando um pedido pago é cancelado, você abre a classe EstadoPago e a resposta está lá, isolada de ruídos."

### Fonte 2: `Teoria/Aula 9.tex`, `\section{Conclusão}`, linhas 992–1005

**Uso pretendido:** síntese de fechamento do "tríptico da estabilidade" completo (dado, gênese, fluxo), reaproveitada no Fechamento desta aula.

**Trecho:**

> "Nesta aula, fechamos o ciclo de vida interno do objeto. Vimos que a qualidade do software começa na forma como os dados são estruturados na memória (Imutabilidade), passa pela forma como o comportamento é distribuído (State) e termina na segurança da sua criação (Creational Patterns). Na próxima aula, expandiremos esta visão para as fronteiras externas, explorando como os objetos se harmonizam através de contratos e adaptadores."

### Fonte 3: `Teoria/Aula 10.tex`, `\section{Introdução e Revisão}`, linhas 16–167 (framing, não reensinado em profundidade)

**Uso pretendido:** só como conectivo breve — a metáfora da "parede corta-fogo arquitetural" e o vetor Rígido→Flexível→Protocolar→Isolado justificam por que, depois de proteger o objeto por dentro (Aulas 10–12 até o State), a aula vira a atenção para a fronteira externa (Adapter). O recap de Strategy/OCP em `\section{Strategy}` (linhas 168–268) **não é reensinado** — já coberto em profundidade na Aula 10; usado aqui só para a frase de transição "o Strategy já resolveu como o núcleo isola algoritmos voláteis; falta isolar interfaces incompatíveis".

**Trechos citados literalmente:**

> "O objetivo central não é apenas o domínio sintático dos padrões de projeto do GoF (Gang of Four), mas a compreensão de sua função como delimitadores de fronteira. Interfaces não devem ser interpretadas meramente como obrigações de implementação de métodos, mas sim como garantias formais de isolamento."

> "\"A qualidade de uma fronteira é medida pelo que você NÃO precisa saber sobre o seu vizinho para interagir com ele.\""

### Fonte 4: `Teoria/Aula 10.tex`, `\section{Padrão Adapter}`, linhas 270–398

**Uso pretendido:** todo o conteúdo do padrão Adapter desta aula — o dilema do legado/SDK incompatível, a definição do Adapter como tradutor, Object Adapter vs. Class Adapter, e o estudo de caso de unificação de log.

**Trechos citados literalmente:**

> "No desenvolvimento de sistemas comerciais modernos, a integração com componentes externos é uma constante inescapável. [...] O conflito surge quando a interface oferecida por esses componentes externos não se alinha com a abstração conceitual que a sua equipe desenhou para o domínio da aplicação."

> "Esta desconexão gera um dilema arquitetural perigoso. Como o código do fornecedor externo está encapsulado em um arquivo JAR binário ou em uma biblioteca fechada, alterá-lo para que ele se adeque à sua interface é impossível. Por outro lado, se você decidir modificar as suas classes de negócio centrais para chamar diretamente os métodos do SDK do banco, você estará contaminando o seu modelo de domínio com detalhes de infraestrutura voláteis."

> "\"Adapter permite que classes trabalhem juntas mesmo que não pudessem de outra forma por causa de interfaces incompatíveis.\""

> "O funcionamento prático segue um fluxo de delegação estrita. O Cliente faz uma chamada baseando-se em uma interface abstrata que ele conhece e confia. O Adapter implementa essa interface esperada, o que o torna aceitável aos olhos do Cliente. No entanto, por dentro do método implementado, o Adapter possui uma referência para o objeto do fornecedor externo."

> "O grande problema dessa abordagem [Class Adapter] é o acoplamento estático em tempo de compilação. O Adapter passa a conhecer os detalhes íntimos e o estado interno da classe herdada, violando o encapsulamento. [...] se o fornecedor lançar uma nova subclasse da ferramenta deles, o Class Adapter não conseguirá reaproveitá-la."

> "Por essa razão, a indústria adota quase exclusivamente o Object Adapter, que se apoia no princípio da composição (\"Tem-Um\"). [...] esse mesmo Adapter é capaz de trabalhar com qualquer subclasse presente ou futura do objeto legado."

> "Sem o Adapter, os desenvolvedores teriam que espalhar números mágicos [...] por todas as classes de negócio que precisassem disparar mensagens para a biblioteca do parceiro. [...] o Adapter age como uma junta de dilatação que absorve os tremores causados por mudanças em sistemas de terceiros."

**Nota de escopo (não usado nesta aula, fica para Aula 13+):** `\section{O Padrão Decorator e a Composição Dinâmica}` (linhas 399–553), `\section{O Padrão Observer e o Desacoplamento de Eventos}` (linhas 555–743), e `\section{Síntese Arquitetural e o Estabelecimento de Fronteiras}` (linhas 745–827) de `Aula 10.tex` — ver decisão de escopo detalhada no `_progresso.md` da disciplina.
