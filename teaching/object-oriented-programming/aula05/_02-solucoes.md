# Soluções — Questões de Verdadeiro/Falso (Aula 5)

> Arquivo de apoio, não publicado (prefixo `_`). Contém a resposta e a
> justificativa de cada item das 12 questões de V/F do `index.qmd`. O
> `index.qmd` publicado continua sem solução — este arquivo existe só
> para conferência do professor/monitor, seguindo a metodologia de
> criação de questões definida em `../../CLAUDE.md`.

### Falso Desacoplamento — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ O acoplamento físico (separação em arquivos) garante, por si só, o desacoplamento lógico entre classes.

**Resposta:** Falso

**Justificativa:** É exatamente a distinção central do bloco. Acoplamento físico é sobre como as classes se instanciam/referenciam (construtor, arquivos separados); acoplamento lógico é sobre o que um método faz com a referência que recebeu. `Pedido` recebia `Carrinho` de forma fisicamente correta e ainda cometia Feature Envy processando os dados por fora.

### Falso Desacoplamento — item (b)

**Heurística:** Transferência

**Afirmação:** ✔ Numa classe `RelatorioFinanceiro` que recebe um `Carrinho` pelo construtor e itera diretamente sobre seus itens internos para somar valores, a mesma falha de Feature Envy desta aula se aplica, mesmo em um contexto de relatório, não de pedido.

**Resposta:** Verdadeiro

**Justificativa:** O mecanismo do Feature Envy não depende do nome da classe orquestradora — depende de extrair os dados internos de um colaborador e processá-los por fora, em vez de pedir ao colaborador que faça o processamento. `RelatorioFinanceiro` comete exatamente o mesmo erro estrutural que `Pedido` cometia antes do *Move Method*.

### Falso Desacoplamento — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ O paradigma da Caixa Preta permite acessar os dados internos de um colaborador associado, desde que via getter.

**Resposta:** Falso

**Justificativa:** É o oposto do que a Caixa Preta exige. Usar um getter para extrair a estrutura interna e processá-la por fora é justamente o mecanismo de Feature Envy — o getter não "legitima" o acesso, só disfarça a violação de encapsulamento atrás de uma chamada de método.

### Falso Desacoplamento — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Ter a referência de um objeto não dá o direito de processar seus dados internos por fora dele.

**Resposta:** Verdadeiro

**Justificativa:** É a mesma distinção do item (a), na direção afirmativa: possuir uma referência resolve só o acoplamento físico. Processar os dados obtidos por essa referência em vez de delegar o processamento ao próprio objeto é a violação lógica (Feature Envy/Tell-Don't-Ask) que a aula ataca.

### Feature Envy (Inveja de Recursos) — item (a)

**Heurística:** Limite

**Afirmação:** ✗ No limite em que um método usa um único getter de um colaborador, uma única vez, para uma leitura simples e isolada, isso já caracteriza Feature Envy com a mesma severidade do exemplo de `calcularCustoTotal()` desta aula.

**Resposta:** Falso

**Justificativa:** A gravidade do Feature Envy está ligada a *processar* dados extraídos de outro objeto (iterar, somar, decidir com base neles) — não ao simples ato de chamar um getter uma vez. Uma leitura isolada e pontual não reproduz o padrão de `calcularCustoTotal()`, que itera a lista inteira do `Carrinho` e recalcula por fora.

### Feature Envy (Inveja de Recursos) — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ O sintoma clássico é o uso repetitivo de getters de um colaborador para processar dados externamente.

**Resposta:** Verdadeiro

**Justificativa:** É o sintoma descrito por Fowler e retomado nesta aula: a obsessão por getters para extrair e processar dados de fora é o sinal mais visível de que um método deveria pertencer à classe que detém os dados.

### Feature Envy (Inveja de Recursos) — item (c)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se, em vez de mover a lógica de soma para o `Carrinho` (*Move Method*), apenas renomeássemos o método `calcularCustoTotal()` para `somarItensExternamente()`, o Feature Envy estaria resolvido.

**Resposta:** Falso

**Justificativa:** Renomear não muda a mecânica: `Pedido` continuaria extraindo a lista de itens do `Carrinho` e somando por fora, exatamente a violação original. *Move Method* resolve o problema porque move o *comportamento* para onde os dados estão — um nome novo no método antigo não move nada.

### Feature Envy (Inveja de Recursos) — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Feature Envy não tem relação nenhuma com o princípio "Tell, Don't Ask".

**Resposta:** Falso

**Justificativa:** Feature Envy É a violação de Tell-Don't-Ask em ação: em vez de "mandar" o `Carrinho` calcular seu próprio total (Tell), `Pedido` "pergunta" pelos itens e calcula por conta própria (Ask). As duas ideias descrevem o mesmo problema de ângulos diferentes.

### A Métrica CBO — item (a)

**Heurística:** Limite

**Afirmação:** ✔ No limite em que uma classe depende de uma única classe externa, mas invoca dezenas de métodos diferentes dela, o CBO dessa classe continua sendo 1, independentemente do número de chamadas.

**Resposta:** Verdadeiro

**Justificativa:** CBO conta *classes* externas distintas, não *chamadas* de método. Uma classe pode chamar 50 métodos diferentes de uma única classe externa e ainda ter CBO=1 — o número de chamadas afeta outras métricas (como acoplamento de mensagens), não o CBO.

### A Métrica CBO — item (b)

**Heurística:** Transferência

**Afirmação:** ✔ Refatorar de Feature Envy para delegação pura tende a reduzir o CBO da classe orquestradora.

**Resposta:** Verdadeiro

**Justificativa:** É a generalização do resultado numérico visto na aula (CBO de `Pedido` caindo de 2 para 1 ao remover a dependência direta de `Produto`): sempre que a delegação elimina uma dependência transitiva que só existia para o processamento manual, o CBO da classe que delega tende a cair.

### A Métrica CBO — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Manter o CBO baixo reduz o risco de Efeito Cascata e facilita testes isolados.

**Resposta:** Verdadeiro

**Justificativa:** É a mesma lógica do exemplo isolado (2 classes) escalada para um sistema real com centenas de classes: menos dependências por classe significa menos superfície afetada quando uma dependência muda, e menos colaboradores reais para simular/mockar em um teste unitário.

### A Métrica CBO — item (d)

**Heurística:** Limite

**Afirmação:** ✗ O objetivo ideal de qualquer design é atingir CBO igual a zero.

**Resposta:** Falso

**Justificativa:** CBO=0 significa nenhuma conexão com nenhuma outra classe — um objeto assim não colabora com nada e não pode cumprir nenhum papel útil no sistema. A meta não é eliminar conexões, é manter cada conexão o mais fraca possível (assunto do próximo bloco, a Escala de Myers).

### Acoplamento de Conteúdo e Comum — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se o atributo `itens` do `Carrinho` fosse declarado `private` em vez de `public`, o método `aplicarDescontoManual` de `Pedido` ainda conseguiria fazer `c.itens.clear()` diretamente, sem nenhuma mudança adicional de design.

**Resposta:** Falso

**Justificativa:** Com `itens` privado, `c.itens` simplesmente não compila fora da classe `Carrinho` — o próprio compilador Java bloqueia o Acoplamento de Conteúdo nesse caso. A visibilidade do atributo é exatamente o que decide se essa violação é possível ou não.

### Acoplamento de Conteúdo e Comum — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Atributos `public` favorecem diretamente o Acoplamento de Conteúdo.

**Resposta:** Verdadeiro

**Justificativa:** Um atributo público remove a barreira que impediria outra classe de alterar o estado interno diretamente — é a pré-condição estrutural para o "pecado original" da Escala de Myers.

### Acoplamento de Conteúdo e Comum — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ O Acoplamento Comum via métodos estáticos facilita a substituição por mocks em testes automatizados.

**Resposta:** Falso

**Justificativa:** É o oposto: uma chamada estática (como `Notificacao.enviarEmailConfirmacao(...)`) está embutida diretamente no corpo do método, sem nenhum ponto de injeção — não há como substituí-la por um mock sem alterar o próprio código de produção, tornando o teste isolado muito mais difícil, não mais fácil.

### Acoplamento de Conteúdo e Comum — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Uma chamada estática oculta no corpo de um método é uma dependência mais difícil de enxergar do que uma no construtor.

**Resposta:** Verdadeiro

**Justificativa:** Uma dependência recebida pelo construtor aparece na assinatura da classe, visível para qualquer leitor. Uma chamada estática enterrada dentro do corpo de um método só aparece para quem lê o código-fonte inteiro — daí o acoplamento comum ser mais "invisível" que o acoplamento por associação.

### Acoplamento de Estampa e de Dados — item (a)

**Heurística:** Transferência

**Afirmação:** ✔ Num sistema de RH que passa um objeto `Funcionario` inteiro para um método que só precisa calcular o desconto do INSS a partir do salário, isso é o mesmo padrão de Acoplamento de Estampa visto no exemplo de `NotificacaoEmail`/`Cliente` desta aula.

**Resposta:** Verdadeiro

**Justificativa:** O mecanismo é idêntico: um método recebe um objeto inteiro (`Funcionario`) mas usa só uma fração dele (o salário), herdando uma dependência transitiva a toda a estrutura de `Funcionario` sem necessidade — exatamente como `NotificacaoEmail` dependia de `Cliente` inteiro só para ler o e-mail.

### Acoplamento de Estampa e de Dados — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Renomear a classe passada por Estampa pode quebrar o receptor, mesmo sem mudança na lógica de negócio.

**Resposta:** Verdadeiro

**Justificativa:** Como o receptor depende do *tipo* inteiro (não só do dado que usa), qualquer mudança estrutural nesse tipo — inclusive um simples `rename` — quebra a compilação do receptor, mesmo que a lógica de e-mail em si não tenha mudado uma linha.

### Acoplamento de Estampa e de Dados — item (c)

**Heurística:** Limite

**Afirmação:** ✔ No limite em que um serviço `Notificacao` recebe cada vez mais parâmetros primitivos individuais (não um objeto), manter o Acoplamento de Dados se torna, na prática, cada vez mais difícil de gerenciar, mesmo sem nenhuma perda de reutilização.

**Resposta:** Verdadeiro

**Justificativa:** O Acoplamento de Dados continua sendo o nível ideal em termos de desacoplamento, mas tem um custo real quando levado ao extremo: uma lista longa de parâmetros primitivos posicionais é difícil de ler e propensa a erro (trocar a ordem de dois `String`, por exemplo) — um trade-off que a aula não nega, só não aprofunda.

### Acoplamento de Estampa e de Dados — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Refatorar de Estampa para Dados torna o serviço menos reutilizável, pois perde contexto.

**Resposta:** Falso

**Justificativa:** É o oposto do observado no exemplo: ao deixar de exigir um `Cliente` inteiro e passar a aceitar só o e-mail (`String`), `Notificacao` ganha reutilização — pode notificar clientes, fornecedores ou administradores sem carregar a bagagem de nenhum tipo específico.

### GRASP: Especialista na Informação — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se duas classes, `Pedido` e `Cliente`, tivessem acesso igual aos dados de endereço de entrega, mas `Cliente` fosse quem originalmente recebe esse dado do usuário, o GRASP recomendaria colocar a lógica de validação de endereço em `Pedido`, e não em `Cliente`.

**Resposta:** Falso

**Justificativa:** O Especialista na Informação é definido por quem *possui* (ou, aqui, originalmente recebe) os dados necessários — nesse cenário, `Cliente`. Ter "acesso igual" não muda quem é o especialista; GRASP recomendaria manter a validação em `Cliente`, não movê-la para `Pedido`.

### GRASP: Especialista na Informação — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Segundo o GRASP, o `Pedido` deveria calcular o total, já que ele "contém" o `Carrinho`.

**Resposta:** Falso

**Justificativa:** Conter (associação) não é o mesmo que ser o Especialista na Informação. O critério do GRASP é quem *possui os dados* necessários para a tarefa — no caso, `Carrinho`, que tem a lista de itens e preços, não `Pedido`, que só tem uma referência a ele.

### GRASP: Especialista na Informação — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Num sistema onde o cálculo de imposto de um `Produto` está espalhado em três classes diferentes que só "pegam" o preço via getter, aplicar o Especialista na Informação implicaria mover essa lógica para dentro da própria classe `Produto`.

**Resposta:** Verdadeiro

**Justificativa:** É a mesma lógica de `Carrinho`/`calcularCustoTotal()` aplicada a um cenário novo: se as três classes só extraem o preço via getter para calcular o imposto por fora, isso é Feature Envy em relação a `Produto`; o Especialista na Informação (quem tem o preço) deveria assumir o cálculo.

### GRASP: Especialista na Informação — item (d)

**Heurística:** Limite

**Afirmação:** ✗ No limite em que uma única classe do sistema concentra toda a informação de todos os domínios de negócio, o GRASP do Especialista na Informação recomendaria centralizar ainda mais responsabilidades nela, já que ela já detém os dados.

**Resposta:** Falso

**Justificativa:** Esse cenário-limite é exatamente a Classe Deus discutida na Aula 4 — o GRASP não anula os critérios de coesão e SRP; "ter os dados" não é licença para acumular responsabilidades de domínios completamente diferentes. O Especialista na Informação pressupõe um design já razoavelmente coeso, não justifica concentração ilimitada.

### O Limite da Composição — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ `Cliente` com `private Cartao cartao` acoplado a uma classe concreta é um exemplo do limite da composição básica.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente o código de abertura do bloco: mesmo com composição bem-feita (atributo privado, associação correta), `Cliente` continua acoplado à implementação concreta `Cartao`, o limite que o bloco se propõe a resolver.

### O Limite da Composição — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Adicionar `Pix` e `Boleto` como novos atributos opcionais em `Cliente`, com `if/else`, respeita o OCP.

**Resposta:** Falso

**Justificativa:** É precisamente o "pesadelo da expansão" descrito na aula: cada novo meio de pagamento exige reabrir e recompilar `Cliente`, violando o Princípio Aberto/Fechado (fechado para modificação).

### O Limite da Composição — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ A explosão de complexidade ciclomática por `if/else` é um sintoma de acoplamento a classes concretas.

**Resposta:** Verdadeiro

**Justificativa:** A cadeia de `if/else` só existe porque `Cliente` precisa distinguir manualmente entre `Cartao`, `Pix` e `Boleto` — tipos concretos. Se `Cliente` dependesse de uma abstração comum, não haveria necessidade de checar qual implementação está em uso.

### O Limite da Composição — item (d)

**Heurística:** Transferência

**Afirmação:** ✔ O acoplamento a implementações concretas impede a extensão *Plug-and-Play* do sistema.

**Resposta:** Verdadeiro

**Justificativa:** Retoma o conceito de Plug-and-Play da Aula 3: um sistema só aceita novos componentes "no encaixe" quando depende de contratos/abstrações, não de classes concretas específicas — exatamente o que o DIP, no bloco seguinte, resolve.

### Inversão de Dependência (DIP) — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se, em vez de uma interface `Pagavel`, `Cliente` dependesse de uma classe abstrata `FormaDePagamentoAbstrata` com métodos concretos parciais, isso ainda seria uma aplicação válida do DIP, desde que `Cliente` não referenciasse `Cartao` ou `Pix` diretamente.

**Resposta:** Verdadeiro

**Justificativa:** O DIP exige que módulos de alto e baixo nível dependam de uma *abstração* — não especifica que essa abstração precise ser uma interface. Uma classe abstrata bem desenhada, sem referências diretas a implementações concretas de pagamento, cumpre o mesmo papel estrutural.

### Inversão de Dependência (DIP) — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Abstrações devem depender dos detalhes técnicos das implementações concretas.

**Resposta:** Falso

**Justificativa:** É o inverso exato do DIP: são os detalhes concretos (`Cartao`, `Pix`) que devem se adequar e depender da abstração (`Pagavel`); a abstração nunca deve conhecer ou depender de nenhuma implementação específica.

### Inversão de Dependência (DIP) — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ O DIP permite erguer um "Muro de Fronteira" entre o núcleo do negócio e a infraestrutura.

**Resposta:** Verdadeiro

**Justificativa:** É a metáfora usada nesta aula para descrever o resultado prático do DIP: o núcleo de negócio (`Cliente`) fica isolado por trás da abstração, e a infraestrutura (`Cartao`, `Pix`, futuros meios de pagamento) muda livremente sem atravessar esse muro.

### Inversão de Dependência (DIP) — item (d)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se, em vez de depender de `Pagavel`, `Cliente` continuasse com um único atributo `Cartao cartao`, mas todo acesso a ele passasse por blocos `try/catch` genéricos, isso já seria suficiente para dizer que `Cliente` aplicou o DIP.

**Resposta:** Falso

**Justificativa:** Tratamento de exceção não resolve acoplamento estrutural. `Cliente` continuaria fisicamente amarrado à classe concreta `Cartao`; qualquer novo meio de pagamento ainda exigiria reabrir `Cliente`. O DIP exige trocar a dependência concreta por uma abstração, não envolvê-la em `try/catch`.

### O Princípio Aberto/Fechado (OCP) e o DIP — item (a)

**Heurística:** Limite

**Afirmação:** ✔ No limite em que um sistema nunca precisa de nenhuma extensão futura (o conjunto de comportamentos é fixo para sempre), a distinção entre respeitar ou violar o Princípio Aberto/Fechado deixa de ter qualquer consequência prática.

**Resposta:** Verdadeiro

**Justificativa:** O custo do OCP só se manifesta quando o sistema precisa crescer — é aí que reabrir classes antigas se torna um problema. Num sistema hipotético congelado para sempre, violar o OCP nunca geraria retrabalho, porque nunca haveria extensão a ser feita.

### O Princípio Aberto/Fechado (OCP) e o DIP — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ A cadeia de `if/else` sobre tipos concretos de pagamento é compatível com o OCP.

**Resposta:** Falso

**Justificativa:** É exatamente o exemplo de violação do OCP usado nesta aula: cada novo meio de pagamento força a reabertura e recompilação de `Cliente`, o oposto de "fechado para modificação".

### O Princípio Aberto/Fechado (OCP) e o DIP — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Depender de uma interface como `Pagavel`, em vez de classes concretas, favorece o cumprimento do OCP.

**Resposta:** Verdadeiro

**Justificativa:** Ao depender da abstração, novos meios de pagamento podem ser adicionados implementando `Pagavel`, sem tocar em `Cliente` — extensão sem modificação, exatamente o que o OCP exige.

### O Princípio Aberto/Fechado (OCP) e o DIP — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ O DIP e o OCP trabalham juntos: abstrações estáveis permitem estender o sistema sem modificar o núcleo.

**Resposta:** Verdadeiro

**Justificativa:** É a síntese dos dois princípios apresentada no fim do bloco: o DIP fornece o mecanismo (dependência de abstrações), e o OCP é o benefício resultante (extensão sem modificação do núcleo).

### Barreira da Tipagem e o Gancho para Polimorfismo — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Em Java, uma variável do tipo `Pagavel` pode referenciar `Pix` ou `Cartao`, desde que ambos implementem o contrato.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente o mecanismo que o gancho da aula anuncia: o compilador aceita a substituição porque ambas as classes concretas cumprem o mesmo contrato de tipo (`Pagavel`), ainda que o mecanismo exato (Polimorfismo) só seja explicado na Aula 6.

### Barreira da Tipagem e o Gancho para Polimorfismo — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ A composição pura, sem nenhum mecanismo de contrato, já é suficiente para essa substituição em tempo de execução.

**Resposta:** Falso

**Justificativa:** Sem um contrato compartilhado (interface ou superclasse comum), o compilador Java rejeitaria uma variável que ora recebe `Pix`, ora `Cartao` — são tipos incompatíveis do ponto de vista do sistema de tipos sem esse elo formal.

### Barreira da Tipagem e o Gancho para Polimorfismo — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Num sistema escrito numa linguagem de tipagem dinâmica, como Python sem *type hints*, a mesma capacidade de aceitar `Pix` ou `Cartao` através de uma única variável existiria por *duck typing*, sem nenhum mecanismo de contrato exigido em tempo de compilação.

**Resposta:** Verdadeiro

**Justificativa:** Em linguagens dinamicamente tipadas, qualquer objeto que responda aos métodos esperados pode ser usado no lugar de outro, sem nenhuma verificação prévia de contrato — a flexibilidade existe, mas sem a garantia estática que Java oferece via interfaces.

### Barreira da Tipagem e o Gancho para Polimorfismo — item (d)

**Heurística:** Limite

**Afirmação:** ✔ No limite em que existisse só uma única forma de pagamento em todo o sistema (sem `Pix`, `Boleto` ou futuros métodos), a necessidade de Polimorfismo para resolver o problema de "múltiplas identidades" desapareceria por completo.

**Resposta:** Verdadeiro

**Justificativa:** O Polimorfismo resolve o problema de uma mesma variável precisar aceitar tipos concretos diferentes. Se só existisse um único tipo concreto possível, não haveria "múltiplas identidades" a conciliar, e o problema que motiva o gancho para a Aula 6 nunca teria surgido.

### Cirurgia de Espingarda e Efeito Cascata — item (a)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se a lógica de soma do carrinho estivesse centralizada num único método de uma única classe (*Move Method* já aplicado), uma mudança na regra de desconto ainda exigiria caçar e repetir a alteração em quatro classes diferentes.

**Resposta:** Falso

**Justificativa:** É exatamente o oposto do que a centralização promete: com a lógica de soma/desconto morando num único lugar, uma mudança de regra é feita uma vez só, ali — não há mais "quatro classes" para caçar, porque a duplicação que causava a Cirurgia de Espingarda já foi eliminada.

### Cirurgia de Espingarda e Efeito Cascata — item (b)

**Heurística:** Limite

**Afirmação:** ✔ No limite em que um sistema tem uma única classe responsável por toda a lógica de negócio, sem nenhuma duplicação de regra em outro lugar, o risco de Cirurgia de Espingarda desaparece por definição, mesmo que o CBO dessa única classe seja extremamente alto.

**Resposta:** Verdadeiro

**Justificativa:** Cirurgia de Espingarda é sobre ter que alterar *vários lugares* para uma única mudança de regra; sem duplicação nenhuma, não existem "vários lugares". CBO é uma métrica diferente (quantas classes externas uma classe conhece), independente de haver ou não duplicação de lógica de negócio — os dois problemas não se implicam.

### Cirurgia de Espingarda e Efeito Cascata — item (c)

**Heurística:** Transferência

**Afirmação:** ✔ Num sistema de e-commerce onde a lógica de cálculo de frete está duplicada em `Pedido`, `NotaFiscal` e `RelatorioVendas`, uma mudança na tabela de frete exigiria caçar e repetir a alteração nos três lugares — o mesmo Efeito Cascata/Cirurgia de Espingarda visto no exemplo de soma do carrinho.

**Resposta:** Verdadeiro

**Justificativa:** É o mesmo padrão estrutural do exemplo de soma do carrinho (lógica espalhada em `Pedido`, `Fatura`, `Checkout`, `RelatorioFinanceiro`), só transportado para o domínio de cálculo de frete — a duplicação, não o domínio, é o que causa a Cirurgia de Espingarda.

### Cirurgia de Espingarda e Efeito Cascata — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Reduzir o CBO de uma classe para 1 (uma única dependência externa) já garante, por si só, que a lógica de negócio que ela usa não está duplicada em outras classes do sistema, prevenindo a Cirurgia de Espingarda.

**Resposta:** Falso

**Justificativa:** CBO mede quantas classes externas *uma* classe conhece — não diz nada sobre se a mesma regra de negócio foi implementada de forma independente em *outras* classes do sistema. É perfeitamente possível ter CBO=1 em várias classes que, cada uma, reimplementa a mesma lógica de desconto por conta própria.

### Síntese: do Acoplamento ao Contrato — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Coesão, CBO, Escala de Myers e GRASP são ferramentas complementares para diagnosticar e melhorar o design.

**Resposta:** Verdadeiro

**Justificativa:** Cada ferramenta ataca um ângulo diferente do mesmo problema: coesão (Aula 4) mede o quão unificada é uma classe por dentro; CBO conta quantas dependências existem; a Escala de Myers julga a qualidade de cada uma; GRASP decide onde colocar cada responsabilidade. Nenhuma substitui as outras.

### Síntese: do Acoplamento ao Contrato — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Resolver Feature Envy automaticamente resolve também o acoplamento a classes concretas do Bloco de DIP.

**Resposta:** Falso

**Justificativa:** São dois problemas independentes. Feature Envy é sobre extrair e processar dados de um colaborador por fora (resolvido por *Move Method*); o acoplamento a classes concretas é sobre depender de uma implementação específica em vez de uma abstração (resolvido pelo DIP). Um `Pedido` sem Feature Envy ainda pode estar rigidamente acoplado a `Cartao`.

### Síntese: do Acoplamento ao Contrato — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ Um sistema bem desenhado combina baixo CBO, acoplamento de dados, especialistas corretos e abstrações estáveis.

**Resposta:** Verdadeiro

**Justificativa:** É a síntese apresentada na conclusão da aula: as quatro ideias (CBO, Escala de Myers, GRASP, DIP) não competem entre si — um design maduro busca as quatro propriedades simultaneamente.

### Síntese: do Acoplamento ao Contrato — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✔ A jornada desta aula termina exatamente onde a próxima começa: como impor contratos de verdade no compilador.

**Resposta:** Verdadeiro

**Justificativa:** É o gancho explícito da conclusão: o DIP introduz a ideia de depender de uma abstração (`Pagavel`), mas deixa em aberto o mecanismo de linguagem que torna essa abstração real e exigível pelo compilador — o assunto da Aula 6 (Interfaces).
