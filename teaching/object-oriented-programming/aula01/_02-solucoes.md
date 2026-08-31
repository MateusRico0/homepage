# Soluções — Questões de Verdadeiro/Falso (Aula 1)

> Arquivo de apoio, não publicado (prefixo `_`). Contém a resposta e a
> justificativa de cada item das 12 questões de V/F do `index.qmd`. O
> `index.qmd` publicado continua sem solução — este arquivo existe só
> para conferência do professor/monitor, seguindo a metodologia de
> criação de questões definida em `../../CLAUDE.md`.

### TRUE e o custo de mudança — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Um código pode ser 100% funcional e passar em todos os testes automatizados e, ainda assim, falhar completamente no critério TRUE proposto por Sandi Metz.

**Resposta:** Verdadeiro

**Justificativa:** TRUE não é um critério de corretude funcional — é um critério de facilidade de mudança. Um código pode fazer exatamente o que deveria (passar em todos os testes) e ainda ser rígido, frágil e imóvel: qualquer mudança pequena pode forçar uma cascata de alterações em módulos dependentes, quebrar partes sem conexão lógica com o que foi alterado, ou não poder ser reaproveitado fora do contexto original. Um aluno que confunde "funciona hoje" com "é bem projetado" cairia nessa pegadinha.

### TRUE e o custo de mudança — item (b)

**Heurística:** Contrafactual

**Afirmação:** ✗ Uma correção rápida (*quick fix*) que funciona perfeitamente, mas ensina ao próximo programador que ler o código a ignorar os padrões de design do sistema, ainda satisfaz a propriedade *Exemplary*.

**Resposta:** Falso

**Justificativa:** *Exemplary* não é sobre o código funcionar — é sobre o código encorajar quem o modifica a manter as mesmas qualidades de design, não degradá-las. Uma correção que funciona mas ensina um mau padrão (por exemplo, duplicar uma regra de negócio em vez de centralizá-la, ou ignorar validação) viola exatamente essa propriedade, mesmo passando todos os testes. O erro conceitual seria achar que "funcionar" e "ser Exemplary" são a mesma coisa.

### TRUE e o custo de mudança — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Um código *Reasonable* impõe que qualquer mudança tenha sempre o mesmo custo fixo, independente do benefício.

**Resposta:** Falso

**Justificativa:** *Reasonable* exige proporcionalidade entre o custo de uma mudança e o benefício que ela traz — não um custo fixo e constante. Uma mudança pequena e de baixo benefício deve ser barata; uma mudança grande e de alto benefício pode custar mais, desde que a relação continue proporcional. Um código *Reasonable* que impusesse sempre o mesmo custo, batizando qualquer alteração (trivial ou não) com a mesma "epopeia", estaria descrevendo justamente o sintoma de rigidez que o TRUE quer evitar.

### TRUE e o custo de mudança — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Rigidez, fragilidade e imobilidade descrevem, na prática, o mesmo problema estrutural visto de ângulos diferentes — um sistema que elimina a rigidez necessariamente também deixa de sofrer de fragilidade e imobilidade.

**Resposta:** Falso

**Justificativa:** Os três sintomas são distintos e independentes. Rigidez é uma mudança forçando cascata em módulos dependentes; fragilidade é o sistema quebrar em lugares sem conexão lógica com a alteração; imobilidade é a impossibilidade de reaproveitar o código fora do contexto original por causa de dependências. Um sistema pode, por exemplo, deixar de ser rígido (uma mudança local não propaga mais) e continuar frágil (efeitos colaterais inesperados em partes distantes) ou imóvel (ainda amarrado a dependências que impedem reuso). Tratá-los como sinônimos é a falsa equivalência: resolver um sintoma não resolve os outros dois automaticamente.

### Espaço do Problema vs. Paradigma Procedural — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Reorganizar um programa procedural em vários arquivos e módulos, sem alterar o fato de que funções externas continuam manipulando diretamente as *structs* de dados, já elimina o risco de efeito colateral apontado no paradigma procedural.

**Resposta:** Falso

**Justificativa:** O risco do paradigma procedural não vem de como os arquivos estão organizados — vem de dados serem estruturas passivas manipuladas livremente por funções externas, sem que nenhuma delas seja a "guardiã" da regra de negócio. Dividir o código em módulos ou arquivos diferentes não muda essa relação: qualquer uma dessas funções, em qualquer arquivo, ainda pode alterar os dados de forma inadvertida. O erro seria confundir organização de arquivos (um problema de estrutura de projeto) com unificação de dados e comportamento (o problema arquitetural real que a OO resolve).

### Espaço do Problema vs. Paradigma Procedural — item (b)

**Heurística:** Contrafactual

**Afirmação:** ✗ Uma classe cujos atributos são todos declarados `public`, mas cujos métodos que os utilizam ficam definidos dentro da mesma classe, já realiza plenamente a proposta orientada a objetos de unir dados e comportamento.

**Resposta:** Falso

**Justificativa:** Colocar dados e métodos dentro do mesmo arquivo/classe é só união *sintática*. Se os atributos são `public`, qualquer código externo pode alterá-los diretamente, ignorando os métodos que supostamente encapsulariam as regras — exatamente o mesmo risco do paradigma procedural (dados manipulados livremente de fora). A proposta real da OO exige que o objeto seja o único guardião do seu estado, o que depende de os atributos serem protegidos (`private`), não apenas de estarem "ao lado" dos métodos.

### Espaço do Problema vs. Paradigma Procedural — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ No exemplo do desconto, a visão orientada a objetos calcula o desconto por fora e depois grava o resultado no objeto `Produto`.

**Resposta:** Falso

**Justificativa:** Essa é exatamente a descrição da visão *procedural* do exemplo (uma função externa calcula e sobrescreve o preço). Na visão orientada a objetos, quem calcula e decide se o desconto é aceitável é o próprio `Produto` — você diz "aplique 10% de desconto em si mesmo" e o objeto pode até recusar. Atribuir esse comportamento de calcular-por-fora à OO troca exatamente a relação de causa e efeito que distingue os dois paradigmas.

### Espaço do Problema vs. Paradigma Procedural — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Mesmo que um sistema orientado a objetos declare todos os atributos de suas classes como `public`, ele deixa de correr o risco de dados globais manipulados livremente por funções externas, simplesmente por estar estruturado em classes.

**Resposta:** Falso

**Justificativa:** O risco de dados manipulados livremente por código externo não desaparece só porque o sistema usa a sintaxe de classes — ele desaparece quando os atributos são protegidos (`private`) e só podem ser alterados através de métodos que aplicam regras de negócio. Um sistema orientado a objetos com atributos `public` reproduz, na prática, o mesmo risco do paradigma procedural: qualquer parte do código pode alterar o estado sem checar nenhuma regra. Usar `class` não é, por si só, encapsulamento.

### Estado, Comportamento e Identidade — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se o Estado de um objeto `Produto` mudar (por exemplo, após `aplicarDesconto`), sua Identidade também muda, pois o objeto passa a representar uma versão diferente de si mesmo.

**Resposta:** Falso

**Justificativa:** Identidade e Estado são propriedades independentes. A Identidade é a garantia da JVM de que aquela instância é fisicamente única na memória (seu endereço na Heap), e essa garantia vale *independentemente* de como o Estado mude ao longo do tempo. O mesmo objeto `Produto` continua sendo o mesmo objeto (mesma identidade) antes e depois de `aplicarDesconto` alterar seu `preco` — é precisamente por isso que um objeto pode evoluir seu estado sem nunca deixar de ser "ele mesmo". Confundir mudança de estado com perda de identidade é o erro central deste item.

### Estado, Comportamento e Identidade — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Dois objetos com o mesmo estado são necessariamente o mesmo objeto na memória.

**Resposta:** Falso

**Justificativa:** É a própria analogia usada na aula: dois pacotes idênticos de arroz, com o mesmo preço, são bens distintos no estoque real. Dois objetos `Produto` com exatamente o mesmo `nome` e `preco` continuam sendo duas instâncias fisicamente distintas na Heap, cada uma com seu próprio endereço de memória. Igualdade de estado (valores dos atributos) não implica identidade (unicidade física) — são propriedades ortogonais.

### Estado, Comportamento e Identidade — item (c)

**Heurística:** Limite

**Afirmação:** ✗ Um objeto sem nenhum método público, apenas atributos, ainda pode ter Comportamento, desde que seu Estado seja suficientemente rico e detalhado.

**Resposta:** Falso

**Justificativa:** Comportamento é definido pelas ações que o objeto pode realizar — seus métodos, aquilo que ele *faz* diante de um estímulo. Um objeto sem nenhum método (só atributos) não tem como reagir a nada: ele é, na prática, uma estrutura de dados passiva, do tipo que o paradigma procedural manipula de fora. Nenhuma quantidade de Estado, por mais rico que seja, substitui a ausência de Comportamento — são propriedades diferentes, não intercambiáveis. No limite (zero métodos), o Comportamento é zero, independentemente do Estado.

### Estado, Comportamento e Identidade — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Um objeto `ContaBancaria` com saldo negativo por falha de sistema e sem nome de titular perde sua Identidade, deixando de ser uma instância única na memória.

**Resposta:** Falso

**Justificativa:** A aula distingue explicitamente identidade física de integridade lógica: um objeto assim é um "zumbi" no domínio (seu Estado é logicamente inválido), mas sua Identidade física — a unicidade do endereço na Heap garantida pela JVM — continua absolutamente intacta. O objeto não desaparece nem se funde com outro; ele apenas representa um estado inconsistente com as regras de negócio. Confundir "estado corrompido" com "identidade perdida" é exatamente o erro que este item testa.

### Encapsulamento e Ocultamento de Informação — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Uma classe cujos atributos são todos `private`, mas cujos métodos públicos apenas devolvem e recebem esses atributos sem qualquer validação (getters/setters triviais), está tão protegida contra fragilidade quanto uma classe com validação de invariantes, como a que valida o preço em `Produto`.

**Resposta:** Falso

**Justificativa:** Declarar o atributo `private` é só a metade sintática do encapsulamento; a proteção real vem de os métodos que o acessam aplicarem regras (invariantes). Um getter/setter trivial (`setPreco(double p) { this.preco = p; }`, sem o `if (p >= 0)`) permite que qualquer código externo grave um valor inválido através do setter — na prática, é equivalente a ter o atributo `public`, porque não existe barreira lógica alguma, só uma barreira de sintaxe. A classe `Produto` da aula é precisamente o contraexemplo: `setPreco` só aceita `p >= 0`, e é essa validação (não o `private` isolado) que sustenta o invariante e reduz fragilidade.

### Encapsulamento e Ocultamento de Informação — item (b)

**Heurística:** Transferência

**Afirmação:** ✗ Em uma equipe pequena e de confiança, em que nenhum código malicioso jamais seria escrito, o Ocultamento de Informação deixa de trazer benefício, pois sua função é impedir invasões externas.

**Resposta:** Falso

**Justificativa:** A própria aula é explícita: Ocultamento de Informação não é uma medida de segurança contra invasores, é uma medida de engenharia contra a fragilidade do próprio código. Mesmo numa equipe inteiramente confiável, sem qualquer intenção maliciosa, o benefício do Information Hiding permanece: impedir que outras partes do sistema criem uma dependência física com a estrutura interna de um objeto, para que esse objeto possa mudar por dentro sem quebrar código externo. O risco que o IH mitiga é o do acoplamento acidental, não o de ataques — por isso ele continua útil mesmo sem nenhuma ameaça de segurança no horizonte.

### Encapsulamento e Ocultamento de Informação — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Um objeto que expõe os métodos públicos `getSaldo()` e `setSaldo(double)`, permitindo que código externo leia o saldo, decida se deve subtrair o valor de uma compra, e então grave o novo saldo de volta, está aplicando corretamente o princípio *Tell, Don't Ask*.

**Resposta:** Falso

**Justificativa:** Esse é exatamente o antipadrão *Ask, Don't Tell* — extrair dados do objeto (`getSaldo()`) para que o código externo tome a decisão e depois grave o resultado de volta (`setSaldo(...)`). O princípio *Tell, Don't Ask* propõe o oposto: delegar a decisão para dentro do objeto (por exemplo, um método `debitar(valorCompra)` que ele mesmo executa e cujas invariantes ele mesmo protege). Usar o jargão correto ("está aplicando Tell, Don't Ask") para descrever exatamente o padrão contrário é a armadilha deste item.

### Encapsulamento e Ocultamento de Informação — item (d)

**Heurística:** Contrafactual

**Afirmação:** ✗ Uma classe cujos atributos são todos `public`, mas que ainda define métodos como `aplicarDesconto()` ao lado desses atributos, preserva a autonomia do objeto, pois dados e comportamento continuam fisicamente dentro da mesma classe.

**Resposta:** Falso

**Justificativa:** A autonomia do objeto depende de ele ser o único caminho para alterar seu próprio estado — e isso só é garantido quando os atributos são protegidos (`private`). Se `preco` fosse `public`, qualquer código externo poderia executar `produto.preco = -50` diretamente, ignorando completamente `aplicarDesconto()` e qualquer regra que ele implemente. A mera presença de métodos ao lado de atributos públicos não impede o bypass; a classe volta a se comportar como uma estrutura procedural, mesmo compilando como uma `class` Java.

### Classe vs. Objeto/Instância — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Se duas equipes de desenvolvimento diferentes escreverem `new Produto(...)` no mesmo sistema, ambas estão, de fato, criando cópias físicas independentes da classe `Produto`, e não apenas instâncias que compartilham o mesmo bytecode.

**Resposta:** Falso

**Justificativa:** `new Produto(...)` cria uma *instância* — um bloco físico na Heap com identidade própria e valores concretos — não uma nova cópia da *classe*. A classe (seu bytecode, seus métodos) é carregada uma única vez no Method Area/Metaspace pelo `ClassLoader`, independentemente de quantas equipes, ou quantas vezes, o código `new Produto(...)` seja executado. Todas as instâncias, de qualquer equipe, compartilham exatamente o mesmo código executável já carregado.

### Classe vs. Objeto/Instância — item (b)

**Heurística:** Limite

**Afirmação:** ✗ Se um sistema instanciar 10.000 objetos `Cliente` ao carregar os dados de um banco, a memória consumida para armazenar o bytecode dos métodos de `Cliente` cresce proporcionalmente a esses 10.000 objetos.

**Resposta:** Falso

**Justificativa:** O bytecode dos métodos é carregado uma única vez no Method Area/Metaspace, independentemente de quantas instâncias existam — seja 1, seja 10.000. O que cresce proporcionalmente ao número de instâncias é a memória da Heap, onde cada objeto guarda seus próprios dados isolados (nome, saldo, etc. de cada `Cliente`). Confundir a área que cresce com o número de instâncias (Heap) com a área do código compartilhado (Method Area) é o erro estrutural que este item testa.

### Classe vs. Objeto/Instância — item (c)

**Heurística:** Limite

**Afirmação:** ✗ Ao reiniciar a JVM e executar o mesmo programa novamente, o bytecode das classes já utilizadas na execução anterior continua disponível no Metaspace, sem precisar ser recarregado a partir do arquivo `.class`.

**Resposta:** Falso

**Justificativa:** O Metaspace é memória RAM associada a um processo da JVM em execução, não um armazenamento persistente. Quando a JVM é encerrada, todo o conteúdo do Metaspace daquela execução — incluindo o bytecode carregado — desaparece junto com o processo. Ao iniciar uma nova execução (mesmo do mesmíssimo programa), o `ClassLoader` precisa ler novamente o arquivo `.class` do disco e recarregar as classes na memória da nova JVM. Isso reforça o ponto da aula de que a classe "existe na memória para fornecer as instruções" apenas enquanto a JVM daquela execução estiver viva — não é um cache permanente entre execuções.

### Classe vs. Objeto/Instância — item (d)

**Heurística:** Transferência

**Afirmação:** ✗ Se a classe `Cliente` tiver um campo `static` que conta quantas instâncias já foram criadas, esse contador vive na Heap, dentro de uma das instâncias de `Cliente`, e não no Metaspace junto com o restante dos membros estáticos da classe.

**Resposta:** Falso

**Justificativa:** A aula é explícita: no Method Area (Metaspace) ficam "o bytecode dos métodos e os membros `static`". Um contador `static` pertence à classe como um todo, não a nenhuma instância específica — por isso ele é armazenado junto com o restante dos dados estáticos da classe, na mesma área de memória do bytecode, e não dentro de nenhum objeto individual na Heap. Se o contador vivesse dentro de uma instância, cada `Cliente` teria sua própria cópia do contador, o que contradiz a própria natureza de um campo `static` (compartilhado por todas as instâncias).

### JVM, Bytecode e Portabilidade (WORA) — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ O `javac` compila o código-fonte Java diretamente para instruções nativas da CPU hospedeira.

**Resposta:** Falso

**Justificativa:** A compilação em Java ocorre em duas etapas distintas: primeiro o `javac` transforma o `.java` em Bytecode (`.class`), independente de plataforma; só depois, em tempo de execução, a JVM mapeia esse bytecode para instruções nativas do ambiente hospedeiro (com ajuda do JIT). Se o `javac` compilasse direto para código nativo de uma CPU específica, o `.class` gerado deixaria de ser portável, e o lema *Write Once, Run Anywhere* simplesmente não existiria — é justamente a existência dessa camada intermediária de bytecode que sustenta a portabilidade.

### JVM, Bytecode e Portabilidade (WORA) — item (b)

**Heurística:** Limite

**Afirmação:** ✗ Se a JVM instalada em uma determinada máquina tiver um *bug* de implementação e interpretar um opcode do Bytecode de forma diferente do especificado, o mesmo arquivo `.class` ainda produzirá exatamente o mesmo resultado em qualquer ambiente, pois a portabilidade do Bytecode independe da JVM usada.

**Resposta:** Falso

**Justificativa:** A garantia de WORA depende de que exista "uma JVM compatível" — ou seja, uma implementação que respeite corretamente a especificação do bytecode. O Bytecode em si é só uma sequência de instruções independente de plataforma; ele não executa sozinho, e sua interpretação correta depende inteiramente da JVM que o lê. Uma JVM com bug que interpreta um opcode de forma diferente do especificado produzirá um resultado diferente naquele ambiente, quebrando a portabilidade — a garantia de WORA é condicional à conformidade da JVM, não uma propriedade absoluta e automática do arquivo `.class`.

### JVM, Bytecode e Portabilidade (WORA) — item (c)

**Heurística:** Transferência

**Afirmação:** ✗ Um arquivo `.class` compilado em uma máquina Windows pode ser executado em um servidor Linux sem qualquer JVM instalada, desde que o processador de ambas as máquinas seja da mesma arquitetura (por exemplo, x86-64).

**Resposta:** Falso

**Justificativa:** O Bytecode não é código de máquina de nenhuma arquitetura específica — mesmo que o processador seja idêntico nas duas máquinas, o sistema operacional não sabe interpretar instruções de bytecode Java diretamente. É a JVM, não o hardware, que faz a ponte entre o `.class` e as instruções nativas do ambiente. Sem uma JVM compatível instalada no servidor Linux, o arquivo `.class` simplesmente não executa, independentemente de a CPU ser igual à da máquina onde foi compilado — confundir compatibilidade de hardware com a necessidade de runtime é o erro central deste item.

### JVM, Bytecode e Portabilidade (WORA) — item (d)

**Heurística:** Limite

**Afirmação:** ✗ Mesmo sem nenhuma JVM instalada no ambiente hospedeiro, o Bytecode de um programa Java consegue ser executado diretamente pelo sistema operacional, já que foi compilado uma vez pelo `javac`.

**Resposta:** Falso

**Justificativa:** O `javac` produz Bytecode, não código de máquina — o sistema operacional não sabe executar Bytecode diretamente, ele só executa instruções nativas do processador. A JVM é o intermediário obrigatório que lê o Bytecode e o traduz (com ajuda do JIT) para instruções que o hardware realmente entende. No caso limite de não haver nenhuma JVM disponível, o `.class` não tem como ser executado, ponto — não existe um caminho alternativo direto entre bytecode e sistema operacional.

### O Compilador JIT — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ O JIT compila o programa inteiro para código nativo assim que a aplicação é iniciada.

**Resposta:** Falso

**Justificativa:** O JIT não compila tudo de antemão — ele faz *profiling* ativo do programa em execução, identifica os *hotspots* (métodos e laços chamados com altíssima frequência) e só então os traduz para código nativo, com base no comportamento real observado. Compilar o programa inteiro no início seria, na prática, uma compilação AOT (ahead-of-time) tradicional, perdendo justamente a vantagem do JIT: otimizar com informação que só existe depois que a aplicação já está rodando e mostrando seu comportamento real.

### O Compilador JIT — item (b)

**Heurística:** Limite

**Afirmação:** ✗ Um método chamado apenas uma única vez durante toda a execução do programa é considerado um *hotspot* pelo JIT e recebe prioridade de compilação para código nativo.

**Resposta:** Falso

**Justificativa:** *Hotspots* são definidos exatamente pelo oposto: métodos e laços chamados com altíssima frequência. Um método executado uma única vez está no extremo contrário do espectro — ele não gera dados suficientes de profiling para justificar o custo de compilá-lo para código nativo, e continua sendo simplesmente interpretado. Priorizar métodos raramente executados desperdiçaria o próprio propósito do JIT, que é investir esforço de compilação onde o retorno (tempo de execução economizado) é maior.

### O Compilador JIT — item (c)

**Heurística:** Transferência

**Afirmação:** ✗ Em uma aplicação de vida muito curta, como uma função *serverless* que roda por poucos milissegundos e termina, a compilação JIT tende a trazer mais vantagem de desempenho do que a compilação estática (AOT).

**Resposta:** Falso

**Justificativa:** O JIT precisa de tempo de execução para fazer *profiling*, identificar os *hotspots* e só então compilá-los — esse processo tem um custo inicial ("aquecimento") que só se paga ao longo de uma execução suficientemente longa para os *hotspots* serem executados muitas vezes após a compilação. Numa aplicação que termina em poucos milissegundos, não há tempo para esse ciclo de profiling e compilação compensar; a aplicação já teria terminado antes de qualquer *hotspot* ser otimizado. É justamente por isso que a aula associa a vantagem do JIT a "aplicações servidoras de longa duração" — o cenário contrário (vida muito curta) favorece a compilação estática (AOT), que já entrega código nativo desde o primeiro instante.

### O Compilador JIT — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Como o JIT compila os *hotspots* para código nativo, um programa Java em execução deixa de ter qualquer trecho de código sendo interpretado pela JVM a partir desse ponto, comportando-se como um binário totalmente compilado.

**Resposta:** Falso

**Justificativa:** O JIT compila *seletivamente* apenas os *hotspots* — os trechos identificados como muito frequentes. O restante do código (caminhos raros, tratamento de casos excepcionais, métodos pouco usados) continua sendo executado por interpretação do Bytecode. A execução de um programa Java é, a qualquer momento, um modelo híbrido — parte interpretada, parte nativa —, nunca um binário inteiramente compilado como sugere a afirmação. Usar corretamente o jargão ("compila os hotspots") para concluir algo estruturalmente errado ("tudo passa a ser nativo") é a armadilha deste item.

### Stack, Heap e Alcançabilidade — item (a)

**Heurística:** Transferência

**Afirmação:** ✗ No método `processarPedido()` do exemplo da aula, se `enviarEmailConfirmacao(p1)` criasse internamente um novo objeto `Email` com `new`, esse objeto `Email` seria armazenado na mesma área de memória (Stack) que a variável local `p1`.

**Resposta:** Falso

**Justificativa:** Todo objeto criado com `new`, em qualquer método, é alocado fisicamente na Heap — essa regra não depende de qual método faz a criação, nem de onde ele foi chamado. O que iria para a Stack, dentro de `enviarEmailConfirmacao`, seria apenas a *variável de referência* local que aponta para esse novo objeto `Email` (semelhante a como `p1` guarda o endereço do `Pedido`) — o objeto `Email` em si, com seus próprios dados, ficaria na Heap, exatamente como o `Pedido` do exemplo original.

### Stack, Heap e Alcançabilidade — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Se um objeto for criado com `new` dentro de um método, mas a variável que o referencia for declarada `static` em vez de local, o objeto passa a ser alocado no Metaspace junto com a classe, em vez da Heap.

**Resposta:** Falso

**Justificativa:** `new` sempre aloca o objeto na Heap, independentemente de a variável que o referencia ser local ou `static`. O que muda quando a referência é `static` é apenas *onde a referência em si fica armazenada* — junto aos membros estáticos da classe, no Method Area/Metaspace — e por quanto tempo ela permanece uma raiz de alcançabilidade (uma GC Root praticamente eterna), não onde o objeto referenciado é fisicamente guardado. Confundir a localização da referência com a localização do objeto é exatamente o erro que este item testa (e é a mesma confusão que está por trás da retenção obsoleta com `cacheInfinito`, discutida mais adiante na aula).

### Stack, Heap e Alcançabilidade — item (c)

**Heurística:** Contrafactual

**Afirmação:** ✗ No método `processarPedido()`, se a variável `p1` fosse declarada `static` em vez de local, o objeto `Pedido` que ela referencia se tornaria elegível para coleta assim que o método terminasse, exatamente como aconteceria com uma variável local comum.

**Resposta:** Falso

**Justificativa:** É o efeito exatamente oposto. Uma variável local desaparece (junto com seu frame na Stack) ao fim do método, deixando o objeto que ela referenciava potencialmente órfão e, se nenhuma outra referência existir, elegível para coleta. Já uma variável `static` é ela mesma uma GC Root, que persiste enquanto a classe estiver carregada — bem além do término de qualquer método. Se `p1` fosse `static`, o `Pedido` continuaria alcançável (e, portanto, NÃO elegível para coleta) mesmo depois de `processarPedido()` terminar, exatamente o mecanismo de retenção obsoleta discutido com o `cacheInfinito` mais adiante na aula.

### Stack, Heap e Alcançabilidade — item (d)

**Heurística:** Limite

**Afirmação:** ✗ Se um objeto A for referenciado apenas por um objeto B, e o objeto B, por sua vez, também não for alcançável a partir de nenhuma GC Root, o objeto A ainda é considerado alcançável, pois existe pelo menos uma referência apontando para ele.

**Resposta:** Falso

**Justificativa:** Alcançabilidade não é sobre "existir alguma referência apontando para o objeto" — é sobre existir um *caminho a partir de uma GC Root* até o objeto. Se B não é alcançável a partir de nenhuma raiz, então o caminho de qualquer GC Root até A (que passaria necessariamente por B) também está quebrado, e A é igualmente inalcançável, mesmo tendo uma referência (a de B) apontando para ele. Esse é o cenário clássico de uma "ilha" de objetos que se referenciam mutuamente mas estão desconectados de qualquer raiz — todos nessa ilha são elegíveis para coleta.

### Retenção Obsoleta e Recursos do Sistema — item (a)

**Heurística:** Limite

**Afirmação:** ✗ O Java é imune a qualquer forma de acúmulo indevido de objetos na memória, graças ao Garbage Collector.

**Resposta:** Falso

**Justificativa:** O Java evita o *memory leak* clássico (ponteiro perdido, memória inacessível e irrecuperável), mas não é imune a acúmulo indevido de objetos — ele sofre de retenção obsoleta: uma coleção `static`, por exemplo, mantém referências alcançáveis para objetos que a lógica de negócio já descartou, e a JVM não tem como saber que eles não servem mais para nada. O GC só coleta o que está *inalcançável*; objetos ainda referenciados, mesmo que inúteis, nunca são coletados. "Qualquer forma" é o exagero que torna a afirmação falsa — o Garbage Collector resolve um tipo específico de problema, não todo acúmulo possível de memória.

### Retenção Obsoleta e Recursos do Sistema — item (b)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se o método `registrar()` do `MonitorDeVendas` removesse cada `Pedido` do `cacheInfinito` imediatamente após inseri-lo, essa estrutura estática deixaria de causar retenção obsoleta, mesmo continuando a existir como GC Root.

**Resposta:** Verdadeiro

**Justificativa:** A causa raiz da retenção obsoleta não é a mera existência de uma coleção `static` (que é sempre uma GC Root, viva enquanto a classe estiver carregada) — é o fato de ela reter referências para objetos que a lógica de negócio já não precisa mais. Se cada `Pedido` fosse removido do mapa logo depois de ser usado, o `cacheInfinito` continuaria sendo uma GC Root eterna, mas apontando para um mapa vazio (ou só com pedidos ainda em uso) — nenhum objeto obsoleto ficaria retido. Isso mostra que o problema está na política de limpeza (ou na ausência dela), não na natureza `static` da estrutura em si.

### Retenção Obsoleta e Recursos do Sistema — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Um objeto `Scanner` usado para ler um arquivo, se simplesmente saísse de escopo ao fim de um método sem ser explicitamente fechado, teria seu identificador de arquivo do sistema operacional liberado no mesmo instante em que o objeto se tornasse elegível para coleta pelo GC.

**Resposta:** Falso

**Justificativa:** Tornar-se elegível para coleta (ficar inalcançável) e ser efetivamente coletado pelo GC são dois momentos diferentes, e o GC age em tempo não-determinístico — pode levar um tempo arbitrário até de fato coletar o objeto, e mesmo a coleta em si não garante que qualquer recurso do sistema operacional associado seja liberado no mesmo instante. É exatamente por essa imprevisibilidade que o GC não é a ferramenta adequada para liberar arquivos, sockets ou conexões de banco: recursos escassos do sistema operacional exigem liberação determinística, via `try-with-resources`, e não podem depender do momento (incerto) em que o coletor decidir agir.

### Retenção Obsoleta e Recursos do Sistema — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Se o bloco `try` de um `try-with-resources` terminar sem lançar nenhuma exceção, o método `close()` do recurso não é chamado, pois `close()` serve apenas para lidar com falhas.

**Resposta:** Falso

**Justificativa:** O `try-with-resources` chama `close()` sempre, ao final do bloco — com sucesso ou com exceção. A linguagem injeta um "finally" invisível que garante o fechamento determinístico do recurso independentemente de como o bloco terminou. Achar que `close()` só entra em ação diante de falhas inverte o próprio motivo de existir do try-with-resources: ele existe para garantir que o recurso seja *sempre* devolvido ao sistema operacional, não apenas quando algo dá errado.

### Modificadores de Acesso — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se o método `depositar(double valor)` da classe `ContaBancaria` fosse declarado `private`, o código externo que hoje chama `conta.depositar(100)` continuaria compilando normalmente, só deixaria de funcionar em tempo de execução.

**Resposta:** Falso

**Justificativa:** A aula é explícita: tentar acessar um membro `private` de fora da classe "não gera um aviso, gera um erro de compilação". Se `depositar` passasse a ser `private`, qualquer código externo que o chamasse deixaria de compilar imediatamente — o build falharia antes mesmo do programa rodar. Não existe uma fase intermediária em que o código compila mas "falha silenciosamente" em tempo de execução; o compilador Java fiscaliza o acesso a membros `private` estaticamente, no momento da compilação.

### Modificadores de Acesso — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Uma classe `ContaBancaria` com o atributo `saldo` declarado `public`, mas com um método privado `validarSaldo()` chamado internamente antes de qualquer operação, ainda impede que código externo execute `conta.saldo = -5000` diretamente.

**Resposta:** Falso

**Justificativa:** Se `saldo` é `public`, código externo pode atribuir qualquer valor diretamente ao atributo, sem passar por nenhum método da classe — nem por `depositar()`, nem por `validarSaldo()`, nem por nenhuma outra "alfândega" interna. A existência de um método privado de validação não tem efeito nenhum sobre esse caminho de acesso direto, porque `conta.saldo = -5000` nunca chama método algum. A proteção contra essa escrita inválida depende exclusivamente de `saldo` ser `private` — é isso, e só isso, que força toda alteração a passar pelos métodos públicos da classe.

### Modificadores de Acesso — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Um projeto Java com várias classes no mesmo pacote (*package*), mas sem nenhuma relação de herança entre elas, ainda impede completamente que um atributo `private` de uma classe seja acessado diretamente por outra classe desse mesmo pacote.

**Resposta:** Verdadeiro

**Justificativa:** O modificador `private` restringe o acesso ao escopo da própria classe declarante, e essa restrição não é afetada por organização em pacotes: mesmo duas classes no mesmíssimo pacote não conseguem acessar diretamente o atributo `private` uma da outra (diferentemente do modificador *default*/package-private, que não foi discutido na aula, mas que teria esse comportamento mais permissivo). A "pista falsa" deste item é sugerir que estar no mesmo pacote poderia abrir uma exceção para `private` — não abre.

### Modificadores de Acesso — item (d)

**Heurística:** Transferência

**Afirmação:** ✗ Se um atributo `private` for acessado por outra classe através de *reflection* (pacote `java.lang.reflect`), a JVM impede essa leitura da mesma forma rígida com que o compilador impede o acesso direto em código-fonte comum.

**Resposta:** Falso

**Justificativa:** `private` é uma restrição aplicada pelo compilador ao código-fonte comum — é o `javac` que rejeita `objeto.atributoPrivado` fora da classe, gerando erro de compilação. A API de *reflection*, porém, contorna essa barreira: com `Field.setAccessible(true)`, é possível ler e até alterar atributos `private` de outra classe em tempo de execução, sem erro de compilação nem, por padrão, bloqueio da JVM. Isso conecta com o ponto já feito na aula sobre Ocultamento de Informação: `private` é uma ferramenta de engenharia contra o acoplamento acidental do código-fonte comum, não uma barreira de segurança absoluta e impenetrável em qualquer circunstância.

### Escopo, Sombreamento e `this` — item (a)

**Heurística:** Transferência

**Afirmação:** ✔ Se um construtor `Produto(String nome)` não tiver nenhum parâmetro com o mesmo nome de um atributo da classe, ainda é possível ocorrer sombreamento entre uma variável local declarada dentro do próprio corpo do construtor e algum atributo da classe.

**Resposta:** Verdadeiro

**Justificativa:** O sombreamento é uma regra geral de resolução de escopo — ocorre sempre que um identificador declarado num escopo mais interno tem o mesmo nome de um identificador do escopo mais externo, e não é exclusivo ao caso parâmetro-versus-atributo discutido na aula. Uma variável local declarada dentro do corpo do construtor (por exemplo, `String preco = "temp";`, se `preco` também fosse o nome de um atributo da classe) sombreia esse atributo exatamente pela mesma regra: o compilador prioriza sempre o escopo mais interno. O caso do parâmetro é só o exemplo mais comum, não o único gatilho possível.

### Escopo, Sombreamento e `this` — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Se um construtor tiver um parâmetro chamado `nome`, igual ao atributo `nome` da classe, e o corpo do construtor for `nome = nome;`, o valor do atributo `nome` da instância passa a ser igual ao valor do parâmetro depois que essa linha é executada.

**Resposta:** Falso

**Justificativa:** É exatamente o erro lógico descrito na aula: `nome = nome;`, sem `this`, resolve as duas ocorrências para o parâmetro local (o escopo mais interno) — a linha atribui a variável local a ela mesma e "morre" inteiramente na Stack. O atributo da classe (na Heap) nunca é tocado e permanece com seu valor padrão (`null`, para uma `String`). Achar que a atribuição "de algum jeito" alcança o atributo, só porque os nomes coincidem, é precisamente a armadilha que motiva a existência de `this.nome = nome;`.

### Escopo, Sombreamento e `this` — item (c)

**Heurística:** Limite

**Afirmação:** ✗ Se um método de instância usar apenas o nome simples de um atributo (sem o prefixo `this.`) e não houver nenhum parâmetro ou variável local com o mesmo nome naquele escopo, o Java ainda assim falha em compilar, pois toda referência a um atributo exige obrigatoriamente o prefixo `this.`.

**Resposta:** Falso

**Justificativa:** `this` existe para *desambiguar* um conflito de nomes entre escopos — ele resolve o problema do sombreamento, não é uma exigência sintática universal. Quando não há nenhum parâmetro ou variável local com o mesmo nome do atributo naquele escopo, referenciar o atributo pelo nome simples compila e funciona perfeitamente, porque não existe ambiguidade nenhuma para o compilador resolver. Tratar `this.` como obrigatório em toda e qualquer referência a atributo é generalizar demais o papel específico que `this` desempenha.

### Escopo, Sombreamento e `this` — item (d)

**Heurística:** Transferência

**Afirmação:** ✗ Se dois objetos `p1` e `p2` da classe `Produto` chamarem o mesmo método `aplicarDesconto(10)` ao mesmo tempo, em duas threads diferentes, ambos os objetos serão alterados simultaneamente, pois `this` é compartilhado entre as duas execuções do método.

**Resposta:** Falso

**Justificativa:** `this` não é uma referência global compartilhada pelo método — é vinculado individualmente a cada chamada, de acordo com a instância sobre a qual o método foi invocado. Quando `p1.aplicarDesconto(10)` e `p2.aplicarDesconto(10)` executam (mesmo simultaneamente, em threads diferentes), cada execução tem seu próprio `this` apontando para a respectiva instância — a chamada em uma thread altera `p1`, a chamada na outra altera `p2`, cada um isoladamente. É exatamente esse mecanismo (já discutido na aula) que garante que rodar o mesmo bytecode não faça uma instância "vazar" alterações para a outra; achar que `this` é compartilhado inverteria essa garantia.

### Passagem de Parâmetros: Primitivos vs. Referências — item (a)

**Heurística:** Limite

**Afirmação:** ✗ Se um método Java recebesse um array com 10 milhões de elementos como parâmetro, a JVM copiaria fisicamente todos os 10 milhões de valores para a Stack do método antes de executá-lo.

**Resposta:** Falso

**Justificativa:** Um array é um tipo de referência, não um primitivo — o "valor" copiado ao passá-lo como parâmetro é apenas o endereço de memória (a referência), exatamente como acontece com `Produto p`. Os 10 milhões de elementos continuam armazenados numa única cópia física, na Heap; o parâmetro do método recebe só uma cópia do "controle remoto" que aponta para esse bloco de memória. É exatamente essa distinção fina — cópia da referência, não do conteúdo — que permite passar objetos e coleções pesadas para métodos sem duplicar memória a cada chamada.

### Passagem de Parâmetros: Primitivos vs. Referências — item (b)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se um método receber um parâmetro `int` e multiplicá-lo por 2 internamente, a variável original que foi passada para o método também dobra de valor depois que a chamada retorna.

**Resposta:** Falso

**Justificativa:** Para tipos primitivos, o "valor" copiado é o próprio dado — a JVM cria uma cópia isolada do número na Stack do método chamado. Multiplicar essa cópia por 2 altera só a variável local dentro do método; a variável original do chamador, sendo uma cópia física separada e independente, permanece com seu valor original depois que a chamada retorna. Esse é exatamente o "isolamento total" dos tipos primitivos descrito na aula, em contraste com o comportamento dos tipos de referência.

### Passagem de Parâmetros: Primitivos vs. Referências — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Ao passar dois objetos `Produto` diferentes (a TV e a Geladeira) para dois parâmetros do mesmo método, cada parâmetro guarda uma cópia de um endereço de memória diferente, mesmo que os dois objetos tivessem, por coincidência, exatamente os mesmos valores de `nome` e `preco`.

**Resposta:** Verdadeiro

**Justificativa:** Isso combina duas ideias da aula: a Identidade de um objeto é física e independente do seu Estado (dois objetos com valores idênticos ainda são instâncias distintas, cada uma com seu próprio endereço na Heap), e passar um objeto para um método sempre copia o valor da referência — o endereço guardado na variável. Como TV e Geladeira são objetos distintos, seus endereços na Heap são necessariamente diferentes, então cada parâmetro do método recebe uma cópia de um endereço diferente, independentemente de os valores de `nome` e `preco` coincidirem ou não.

### Passagem de Parâmetros: Primitivos vs. Referências — item (d)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se, dentro do método `sabotarProduto(Produto prod)`, a reatribuição `prod = new Produto("Geladeira", 3000.0)` ocorresse ANTES da chamada `prod.setPreco(999.0)`, o objeto TV original do chamador ainda assim acabaria com o preço alterado para 999.0.

**Resposta:** Falso

**Justificativa:** A ordem das operações importa porque `prod` é uma variável que pode ser reapontada. No exemplo original da aula, `prod.setPreco(999.0)` executa primeiro, enquanto `prod` ainda guarda o endereço da TV — por isso a TV é alterada e a mudança é vista por quem chamou. Se a reatribuição `prod = new Produto("Geladeira", ...)` ocorresse *antes*, `prod` passaria a apontar para o novo objeto Geladeira, e a chamada seguinte `prod.setPreco(999.0)` alteraria a Geladeira, não a TV — a TV original do chamador permaneceria com seu preço original, intocada. Isso mostra que o resultado depende de qual objeto `prod` está apontando *no momento exato* de cada chamada, não apenas de quais linhas de código existem no método.
