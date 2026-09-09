# Gabarito — Aula 10

Gabarito consolidado: justificativa analítica de cada item de V/F dos
exercícios finais (`index.qmd`) e a solução discutida de cada pausa
ativa da aula. Nunca publicado no site (prefixo `_`).

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

---

## Exercícios de V/F

### Fusão Estrutural e o Custo da Herança de Estado — item (a)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Se uma subclasse não acessa nenhum atributo `protected` herdado do pai, ainda assim ela carrega esses atributos fisicamente alocados na Heap para cada instância criada.

**Resposta:** Verdadeiro

**Justificativa:** A alocação de memória para um campo declarado na classe base é incondicional — a JVM reserva espaço para cada atributo herdado em toda instância da linhagem, independentemente de o código da subclasse jamais ler ou escrever naquele campo. "Nunca acessar" é uma decisão de código; "não alocar" exigiria que o campo simplesmente não existisse naquela hierarquia — é exatamente o fenômeno da Subclasse Gorda.

### Fusão Estrutural e o Custo da Herança de Estado — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Herdar de uma classe unicamente para reutilizar métodos prontos, sem que exista uma relação de identidade real entre as duas classes, reduz o acoplamento do sistema porque elimina duplicação de código.

**Resposta:** Falso

**Justificativa:** É a "Ilusão da Produtividade" às avessas: eliminar duplicação de código não é o mesmo que reduzir acoplamento — na verdade, herdar sem relação de identidade real **aumenta** o acoplamento estrutural (a subclasse passa a depender de toda a superfície pública e das mudanças futuras do construtor/estrutura da base), trocando um problema barato de resolver (duplicação) por um caro (acoplamento estrutural rígido).

### Fusão Estrutural e o Custo da Herança de Estado — item (c)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se `PedidoInternacional` dependesse de `Pedido` por composição em vez de herança, uma mudança no formato interno de armazenamento de itens dentro de `Pedido` teria maior chance de permanecer invisível para `PedidoInternacional`, contanto que a interface pública de `Pedido` não mudasse.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente o argumento de "Encapsulamento Preservado" da Era da Composição: por composição, `PedidoInternacional` só interage com `Pedido` através de seus métodos públicos, então qualquer refatoração interna de `Pedido` (como o formato de armazenamento de itens) fica oculta, desde que a interface pública seja mantida. Por herança, o acesso a detalhes via `protected` cria justamente o tipo de dependência que uma mudança "inocente" na base pode quebrar sem aviso.

### Fusão Estrutural e o Custo da Herança de Estado — item (d)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um sistema de RH que cria `FuncionarioTerceirizado` estendendo `Funcionario` apenas para reaproveitar o método `calcularHorasTrabalhadas()`, sem que o terceirizado deva ser tratado polimorficamente como um `Funcionario` em folha de pagamento, comete o mesmo erro semântico do `PedidoInternacional`.

**Resposta:** Verdadeiro

**Justificativa:** É a mesma estrutura de erro transportada para outro domínio: herdar por conveniência de método (ganhar `calcularHorasTrabalhadas()` de graça) sem que exista a necessidade real de tratar `FuncionarioTerceirizado` como um `Funcionario` em todo lugar do sistema (por exemplo, na geração da folha de pagamento) é exatamente a "Ilusão da Produtividade" — reuso de código sem relação de identidade genuína.

---

### O Peso Físico na Heap: a Subclasse Gorda — item (a)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Uma classe `ArquivoDeVideo` que estende uma classe base `ArquivoDeMidia` contendo o atributo `duracaoDeExibicaoEmSala` (relevante só para filmes de cinema) carregaria esse atributo desperdiçado em cada instância, mesmo sendo um vídeo doméstico.

**Resposta:** Verdadeiro

**Justificativa:** É a mesma estrutura do exemplo `Ebook`/`ProdutoBase` transportada para outro domínio: um atributo semanticamente relevante só para uma parte da hierarquia (filmes de cinema), declarado na base, é alocado para toda instância descendente — inclusive as que nunca usarão aquele dado.

### O Peso Físico na Heap: a Subclasse Gorda — item (b)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Se uma classe base abstrata não declarar nenhum atributo próprio, apenas métodos abstratos, suas subclasses não sofrem o fenômeno da Subclasse Gorda relacionado a esses atributos, mesmo herdando de uma hierarquia profunda.

**Resposta:** Verdadeiro

**Justificativa:** A Subclasse Gorda é especificamente sobre **atributos de estado** desperdiçados na Heap — se a base não declara nenhum campo, não há nada para alocar desnecessariamente por causa dela, independentemente da profundidade da hierarquia. O fenômeno pode ainda existir por causa de atributos declarados em outras classes intermediárias, mas não por causa dessa base específica sem estado.

### O Peso Físico na Heap: a Subclasse Gorda — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ O desperdício de memória da Subclasse Gorda é resolvido simplesmente tornando os atributos da classe base `private` em vez de `protected`, já que isso impede o acesso indevido por parte das subclasses.

**Resposta:** Falso

**Justificativa:** Confunde dois problemas distintos: visibilidade (quem pode acessar o campo) e alocação de memória (se o campo existe fisicamente na instância). Trocar `protected` por `private` restringe o acesso direto pelas subclasses, mas não impede que a JVM aloque espaço para aquele campo em toda instância da linhagem — o campo continua existindo fisicamente, só fica inacessível por nome de fora da própria classe.

### O Peso Físico na Heap: a Subclasse Gorda — item (d)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se `pesoFisico` e `dimensoesPacote` fossem movidos de `ProdutoBase` para uma classe `DadosLogisticosFisicos` usada por composição apenas nos produtos que realmente precisam de envio físico, um `Ebook` deixaria de alocar espaço para esses dois atributos.

**Resposta:** Verdadeiro

**Justificativa:** É a correção por composição sugerida na aula: ao mover os campos logísticos para uma classe separada, só as classes que realmente compõem uma instância de `DadosLogisticosFisicos` (produtos físicos) pagam o custo de memória associado — um `Ebook`, que nunca precisaria dessa composição, deixa de carregar esses bytes desperdiçados.

---

### Explosão Combinatória e Eixos Ortogonais — item (a)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Em uma hierarquia de herança pura que já modela três eixos binários de variação independentes (totalizando 8 subclasses-folha), a adição de um quarto eixo binário eleva esse número para 16.

**Resposta:** Verdadeiro

**Justificativa:** O crescimento é multiplicativo: $2^3 = 8$ com três eixos, $2^4 = 16$ com quatro — cada eixo binário adicional dobra o número de combinações possíveis, o mesmo padrão exponencial discutido na Pausa Ativa 1.

### Explosão Combinatória e Eixos Ortogonais — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ A explosão combinatória só ocorre quando os eixos de variação envolvidos são eixos técnicos de infraestrutura (como logística); eixos puramente de regra de negócio, como categorias promocionais, não geram o mesmo efeito.

**Resposta:** Falso

**Justificativa:** A explosão combinatória é uma propriedade **estrutural** da tentativa de modelar múltiplos eixos independentes por herança — não depende da natureza do eixo (técnico ou de negócio). O próprio `.tex` da aula usa "Categorias Promocionais" como exemplo de terceiro eixo que dispararia a mesma explosão; qualquer eixo verdadeiramente ortogonal aos já existentes produz o mesmo efeito multiplicativo.

### Explosão Combinatória e Eixos Ortogonais — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um sistema de seguros que precisa combinar Tipo de Veículo (Carro/Moto) com Perfil de Risco (Baixo/Alto) através de subclasses como `CarroBaixoRisco` e `MotoAltoRisco` está sujeito ao mesmo padrão de explosão combinatória visto no e-commerce.

**Resposta:** Verdadeiro

**Justificativa:** Dois eixos binários independentes (Tipo de Veículo × Perfil de Risco) modelados por herança pura geram exatamente $2 \times 2 = 4$ subclasses-folha, com o mesmo risco de duplicação de regra e mesma inviabilidade de escalar para um terceiro eixo — a estrutura do problema é idêntica à do e-commerce, só o domínio muda.

### Explosão Combinatória e Eixos Ortogonais — item (d)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se dois eixos de variação de um sistema não forem realmente independentes — por exemplo, se todo produto Importado for necessariamente Físico por regra de negócio —, modelar essa relação por herança direta (`ImportadoFisico extends ProdutoFisico`) não gera o mesmo problema de explosão combinatória.

**Resposta:** Verdadeiro

**Justificativa:** A explosão combinatória nasce especificamente da **ortogonalidade** dos eixos — cada combinação das opções de um eixo com as do outro sendo um cenário de negócio válido e necessário. Se uma regra de negócio elimina metade das combinações a priori (todo Importado já é Físico), o espaço de casos deixa de crescer multiplicativamente, e uma única subclasse extra pode bastar sem reabrir o problema.

---

### A Proibição da Herança Múltipla em Java (Diamante) — item (a)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Mesmo que duas superclasses candidatas a uma herança múltipla não compartilhem nenhum método com o mesmo nome, ainda pode haver ambiguidade se ambas herdarem, por caminhos diferentes, de uma mesma superclasse comum mais alta na árvore.

**Resposta:** Verdadeiro

**Justificativa:** É a forma clássica do Problema do Diamante: se `ProdutoFisico` e `ProdutoImportado` herdassem ambos, por caminhos distintos, de uma mesma classe `Produto`, uma hipotética `FisicoImportado` herdaria duas "cópias" conceituais do estado de `Produto` através de cada caminho — ambiguidade que existe independentemente de haver ou não colisão de nomes de método entre `ProdutoFisico` e `ProdutoImportado` diretamente.

### A Proibição da Herança Múltipla em Java (Diamante) — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Java resolve completamente o Problema do Diamante ao permitir que uma classe implemente múltiplas interfaces, porque interfaces nunca podem gerar nenhum tipo de conflito entre implementações.

**Resposta:** Falso

**Justificativa:** Interfaces com métodos `default` (Aula 6) **podem** gerar conflito: se duas interfaces implementadas pela mesma classe declararem um método `default` com a mesma assinatura, o compilador exige que a classe resolva explicitamente a ambiguidade (sobrescrevendo o método). Múltiplas interfaces evitam o problema mais grave — ambiguidade de **estado** (campos duplicados) — mas não eliminam toda possibilidade de conflito de comportamento.

### A Proibição da Herança Múltipla em Java (Diamante) — item (c)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se Java permitisse `class FisicoImportado extends ProdutoFisico, ProdutoImportado`, e as duas superclasses declarassem um atributo `protected` com o mesmo nome mas valores diferentes, o compilador precisaria de alguma regra de desempate para decidir qual valor prevalece em cada acesso.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente a ambiguidade de estado que motiva a proibição: sem uma regra de desempate clara (qual `desconto`, de qual superclasse, um acesso `this.desconto` dentro de `FisicoImportado` deveria retornar?), o comportamento do programa se tornaria imprevisível ou exigiria uma sintaxe de desambiguação explícita a cada acesso — complexidade que o Java optou por nunca introduzir para herança de classes.

### A Proibição da Herança Múltipla em Java (Diamante) — item (d)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ A ausência de herança múltipla de classes em Java é a razão fundamental pela qual a linguagem introduziu métodos `default` em interfaces, permitindo simular parte do reaproveitamento de comportamento sem os riscos de ambiguidade de estado.

**Resposta:** Verdadeiro

**Justificativa:** Métodos `default` (vistos na Aula 6) permitem que uma interface forneça uma implementação padrão de comportamento, algo que só herança de classes oferecia antes — mas interfaces nunca carregam estado (campos de instância), então a ambiguidade mais perigosa do Diamante (conflito de campos duplicados) simplesmente não tem como ocorrer nesse mecanismo, mesmo quando um conflito de método `default` precisa ser resolvido explicitamente.

---

### Composição, Agregação e Associação — item (a)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Se o objeto "Todo" de uma relação de Agregação for destruído, mas os objetos "Parte" continuarem acessíveis e utilizáveis por outras partes do sistema, essa é uma evidência de que a relação realmente era uma Agregação, e não uma Composição estrita.

**Resposta:** Verdadeiro

**Justificativa:** O critério que distingue Agregação de Composição estrita é justamente a sobrevivência da parte à destruição do todo — se as partes continuam vivas e utilizáveis, a relação não tinha a posse exclusiva de vida característica da Composição estrita, encaixando-se na definição de Agregação (Todo-Parte sem dono absoluto da existência da parte).

### Composição, Agregação e Associação — item (b)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se um `CartaoDeCredito` só pudesse ser instanciado a partir de um `Cliente` já existente e fosse automaticamente destruído quando esse `Cliente` fosse removido do sistema, a relação entre eles deixaria de se encaixar na definição de Associação apresentada na aula.

**Resposta:** Verdadeiro

**Justificativa:** A definição de Associação usada na aula exige vidas **completamente autônomas** — nenhum dos dois lados depende da existência do outro. Amarrar a criação e a destruição do cartão ao ciclo de vida específico de um cliente introduz exatamente a dependência que a Associação, por definição, não tem; a relação descrita passaria a se parecer com Composição estrita (a "parte" só existe através do "todo" e morre com ele), não mais com a colaboração livre entre `Cliente` e `CartaoDeCredito` vista na aula.

### Composição, Agregação e Associação — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Toda relação de composição de objetos em que um objeto guarda uma referência a outro deve, por definição, ser classificada como Agregação, nunca como Associação.

**Resposta:** Falso

**Justificativa:** Guardar uma referência é a mecânica comum a Agregação **e** Associação — a diferença entre as duas não está em "ter uma referência", mas no grau de autonomia dos ciclos de vida envolvidos. Classificar toda referência como Agregação ignora exatamente a distinção que a aula estabeleceu (Todo-Parte com posse parcial vs. colaboração totalmente livre).

### Composição, Agregação e Associação — item (d)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Uma classe `Equipe` que mantém uma lista de `Jogador`, onde os jogadores continuam existindo no sistema (podem ser transferidos para outra equipe) mesmo se a `Equipe` for extinta, é um exemplo de Agregação e não de Composição estrita.

**Resposta:** Verdadeiro

**Justificativa:** É a mesma estrutura do `CarrinhoDeCompras`/`Produto` aplicada a outro domínio: o "Todo" (`Equipe`) agrupa as partes (`Jogador`), mas a extinção do todo não implica a destruição das partes — elas seguem existindo e podem, inclusive, ser realocadas, exatamente o comportamento que caracteriza Agregação.

---

### Quase-Decomponibilidade e Sistemas Modulares — item (a)

**Heurística:** Caso limite/extremo

**Afirmação:** ✗ Segundo a teoria de Herbert Simon, um sistema perfeitamente decomponível — onde não existe absolutamente nenhuma dependência entre os subsistemas — ainda seria considerado estável e evolutivo, mesmo sem nenhuma coesão interna em cada peça.

**Resposta:** Falso

**Justificativa:** A "quase-decomponibilidade" de Simon exige **ambos** os lados da comparação: elos internos fortes (coesão) **e** dependências externas fracas — não apenas a ausência de dependência externa. Um sistema sem nenhuma coesão interna em suas peças não seria estável mesmo com zero acoplamento entre elas, porque cada peça, isoladamente, já seria frágil e desorganizada; e um sistema com dependência zero entre partes também deixaria de funcionar como um sistema coeso, incapaz de colaborar para um objetivo comum.

### Quase-Decomponibilidade e Sistemas Modulares — item (b)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um monólito de software onde módulos de autenticação, pagamento e notificação compartilham as mesmas variáveis globais e estruturas de dados internas viola o princípio de quase-decomponibilidade, mesmo que a interface externa do sistema pareça organizada em módulos.

**Resposta:** Verdadeiro

**Justificativa:** A quase-decomponibilidade é sobre a força relativa dos elos **internos vs. externos** de fato, não sobre a aparência superficial da organização do código. Compartilhar variáveis globais e estruturas internas entre módulos cria dependências externas fortes exatamente onde deveriam ser fracas — a "modularidade" nesse caso é só uma fachada de nomenclatura, não uma propriedade estrutural real do sistema.

### Quase-Decomponibilidade e Sistemas Modulares — item (c)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se a API dos Correios mudasse e o sistema estivesse estruturado por herança (`Pedido` estendendo uma classe `LogisticaCorreios`), a substituição da lógica de logística exigiria uma intervenção estruturalmente mais invasiva do que se o sistema estivesse estruturado por composição.

**Resposta:** Verdadeiro

**Justificativa:** Por herança, a lógica de logística estaria fundida na própria identidade de `Pedido` — substituir a transportadora exigiria alterar a hierarquia de tipos de `Pedido` (potencialmente afetando todo código que dependia daquele tipo). Por composição, basta trocar a implementação da interface de logística injetada, mantendo `Pedido` e seu tipo intocados — exatamente o argumento da analogia do eletrodoméstico modular.

### Quase-Decomponibilidade e Sistemas Modulares — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ A resiliência de um sistema modular decorre exclusivamente do número de classes em que ele foi dividido, independentemente de como essas classes se comunicam entre si.

**Resposta:** Falso

**Justificativa:** Simplesmente dividir um sistema em muitas classes não garante resiliência se essas classes permanecerem fortemente acopladas entre si (por exemplo, todas dependendo de detalhes internas umas das outras). A quase-decomponibilidade — e a resiliência que dela decorre — depende da **qualidade** das interações (elos externos fracos, via contratos estáveis), não apenas da quantidade de divisões.

---

### Identidade vs. Papel: a Falha da Herança no Checkout — item (a)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Se um sistema garantisse que o meio de pagamento de um `Pedido` nunca muda depois de criado (é definido uma única vez, na instanciação, e nunca mais alterado), o problema do aprisionamento estático deixaria de ser um argumento decisivo contra modelar `PedidoPix` como subclasse de `Pedido`.

**Resposta:** Verdadeiro

**Justificativa:** O aprisionamento estático é especificamente sobre a impossibilidade de **trocar** o meio de pagamento depois de instanciado o objeto — se essa troca nunca fosse necessária por regra de negócio, esse argumento específico perderia força (embora o problema de identidade-vs-papel e o risco de explosão da árvore, discutidos na aula, ainda permaneçam como razões independentes para preferir composição).

### Identidade vs. Papel: a Falha da Herança no Checkout — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Colocar toda a lógica de processamento de Pix, Cartão e Boleto dentro de um único método `processarPagamento()` do `Pedido`, usando `if/else`, melhora a coesão do sistema porque centraliza toda a responsabilidade de pagamento em um único lugar.

**Resposta:** Falso

**Justificativa:** "Centralizar em um único método" não é o mesmo que "coeso" — pelo contrário, o método passa a acumular responsabilidades de domínios completamente diferentes (antifraude de cartão, geração de QR Code Pix, código de barras de boleto), o oposto de coesão. É o *code smell* clássico discutido na aula: `Pedido` passa a conhecer detalhes de infraestrutura alheios ao seu domínio.

### Identidade vs. Papel: a Falha da Herança no Checkout — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um sistema de streaming que cria classes `AssinaturaMensal extends Usuario` e `AssinaturaAnual extends Usuario` para representar o plano de cobrança atual do usuário comete o mesmo erro de confundir identidade com papel visto no `PedidoPix`.

**Resposta:** Verdadeiro

**Justificativa:** O plano de cobrança de um usuário, assim como o meio de pagamento de um pedido, é um **papel temporário** (pode mudar de mensal para anual), não uma característica que define permanentemente o que o `Usuario` *é*. Modelar essa variação por herança gera o mesmo aprisionamento estático: trocar de plano exigiria trocar a classe do objeto, o que Java não permite em tempo de execução.

### Identidade vs. Papel: a Falha da Herança no Checkout — item (d)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se o meio de pagamento de um `Pedido` fosse tratado como um papel (uma referência substituível) em vez de uma identidade fixada por herança, um cliente poderia trocar de Pix para Cartão no último segundo do checkout sem que o objeto `Pedido` precisasse ser recriado.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente a solução que o padrão Strategy oferece: tratando o meio de pagamento como uma referência substituível (`Pagavel`) injetada via `set`, a troca de Pix para Cartão se resume a trocar o objeto apontado pela referência — o `Pedido` permanece o mesmo objeto na Heap durante toda a operação.

---

### O Padrão Strategy e o Princípio Aberto/Fechado — item (a)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Se uma única implementação concreta de `Pagavel` existisse no sistema (por exemplo, apenas `Pix`), o padrão Strategy ainda traria benefício arquitetural relevante, mesmo sem nenhuma estratégia alternativa em uso.

**Resposta:** Verdadeiro

**Justificativa:** Mesmo com uma única implementação hoje, o Strategy já entrega encapsulamento (a lógica de `Pix` fica isolada e testável sem instanciar `Pedido`) e desacoplamento (`Pedido` não conhece detalhes internos de `Pix`) — os dois primeiros benefícios da composição discutidos na aula não dependem de já existir mais de uma estratégia em uso; a "intercambiabilidade" é um benefício adicional, não o único.

### O Padrão Strategy e o Princípio Aberto/Fechado — item (b)

**Heurística:** Contrafactual

**Afirmação:** ✗ Se o `Pedido` chamasse diretamente `new Pix()` dentro do método `processarPagamento()`, em vez de receber uma instância de `Pagavel` injetada, adicionar um novo meio de pagamento ainda seria possível sem modificar a classe `Pedido`.

**Resposta:** Falso

**Justificativa:** Instanciar a classe concreta diretamente dentro de `Pedido` reintroduz exatamente o acoplamento que a injeção de dependência elimina — qualquer novo meio de pagamento exigiria editar `processarPagamento()` para decidir quando instanciar a classe nova, violando o Princípio Aberto/Fechado que a interface `Pagavel` e a injeção via `set`/construtor foram desenhadas para garantir.

### O Padrão Strategy e o Princípio Aberto/Fechado — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ O Princípio Aberto/Fechado, quando aplicado ao Strategy, significa que a classe `Pedido` nunca mais poderá ser modificada por nenhum motivo, incluindo correção de bugs em sua própria lógica de orquestração.

**Resposta:** Falso

**Justificativa:** O OCP é especificamente sobre não precisar modificar `Pedido` **para acomodar uma nova variação de comportamento intercambiável** (um novo meio de pagamento) — não uma proibição geral de qualquer edição futura. Corrigir um bug genuíno na lógica de orquestração de `Pedido` (por exemplo, uma condição mal escrita em `finalizarPedido()`) é manutenção normal do código, categoricamente diferente de precisar reabrir o arquivo toda vez que a loja aceita um novo meio de pagamento.

### O Padrão Strategy e o Princípio Aberto/Fechado — item (d)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um sistema de cálculo de frete que aceita diferentes transportadoras (Correios, Transportadora Privada, Retirada em Loja) através de uma interface comum `CalculadoraFrete`, injetada no objeto `Pedido`, aplica a mesma topologia Context/Strategy/ConcreteStrategy vista no processamento de pagamento.

**Resposta:** Verdadeiro

**Justificativa:** É a mesma topologia formal do GoF aplicada a um eixo de variação diferente do mesmo domínio: `Pedido` (Context) mantém uma referência a `CalculadoraFrete` (Strategy), e cada transportadora (Correios, Transportadora Privada, Retirada em Loja) é uma ConcreteStrategy intercambiável — a estrutura é idêntica à de `Pagavel`/`Pix`/`Cartao`/`Boleto`, só o algoritmo variável muda (cálculo de frete em vez de processamento de pagamento).
