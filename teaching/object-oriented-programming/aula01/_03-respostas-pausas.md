# Respostas das Pausas Ativas — Aula 1

> Arquivo de apoio, não publicado (prefixo `_`). Discute as perguntas
> motivadoras das pausas ativas do `index.qmd` e dá a solução dos
> respectivos V/F. O `index.qmd` publicado só contém a pergunta e os
> quatro itens de V/F em cada pausa ativa, nunca a resolução.

## Encapsulamento e Ocultamento de Informação

A pergunta pede para separar dois motivos possíveis para "esconder"
dados de um objeto — segurança contra invasores, ou engenharia contra
a fragilidade do próprio código — e o segundo é o correto. Ocultar
informação não impede que alguém "leia" um valor em tempo de execução
(um invasor com acesso à JVM ainda pode inspecionar memória, usar um
debugger, etc.); o que o encapsulamento impede é que **outro código do
próprio sistema** crie uma dependência física com a estrutura interna
do objeto. Se `Produto` expõe `preco` diretamente, qualquer classe que
o manipule passa a depender de `preco` ser um `double`, guardado
daquele jeito específico — e se amanhã a representação mudar (por
exemplo, para armazenar em centavos como `long`, evitando erro de
ponto flutuante), todo código externo que tocou `preco` diretamente
quebra. A "caixa preta" do motor do carro (Bloco 2) e o "Information
Hiding" de Parnas descrevem exatamente o mesmo mecanismo por dois
ângulos: um fala em termos de interface/implementação, o outro em
termos de dados protegidos.

- ✔ Encapsulamento e Ocultamento de Informação são, na prática, o
  mesmo mecanismo de engenharia visto de dois ângulos — a "caixa
  preta" e o "Information Hiding" descrevem a mesma separação entre o
  quê e o como.
- ✗ O objetivo do Ocultamento de Informação é impedir que hackers
  leiam os dados do objeto em tempo de execução — é uma medida de
  engenharia contra a fragilidade e o acoplamento, não uma medida de
  segurança contra invasão.
- ✔ Um objeto sem encapsulamento perde autonomia e volta a se
  comportar como uma estrutura procedural — sem a membrana, o objeto é
  só uma estrutura de dados manipulada de fora.
- ✔ O princípio *Tell, Don't Ask* propõe delegar decisões para dentro
  do objeto, em vez de extrair seus dados para decidir por fora — é
  exatamente essa a definição de *Tell, Don't Ask*.

## Memória, GC e Recursos do Sistema

O `Map` `static` do exemplo (`cacheInfinito`) nunca fica vazio sozinho
porque ele próprio é uma **GC Root**: atributos `static` são, por
definição, uma das raízes seguras de onde o Garbage Collector começa a
navegar o grafo de referências. Isso significa que o mapa está *sempre*
alcançável, do início ao fim da execução do programa — e, por
transitividade, todo objeto que ele referencia (cada `Pedido` inserido)
também está sempre alcançável, mesmo que a lógica de negócio já tenha
terminado com aquele pedido há muito tempo. O GC não tem como "saber"
que o pedido é logicamente obsoleto — ele só sabe que existe um caminho
de ponteiros desde uma raiz até aquele objeto, e isso basta para
declará-lo vivo. É por isso que a retenção obsoleta é um problema tão
insidioso: não é um bug de ponteiro perdido (não existe em Java), é um
bug de *ponteiro demais*, guardado por tempo demais.

- ✗ O fim do escopo de um método destrói automaticamente os objetos
  instanciados dentro dele, junto com a variável local — destrói só o
  ponteiro na Stack; o objeto continua na Heap até ficar inalcançável.
- ✔ Um objeto se torna elegível para coleta quando nenhuma GC Root
  consegue alcançá-lo através do grafo de referências — é exatamente a
  definição de inalcançabilidade.
- ✔ Uma coleção `static` pode reter objetos indefinidamente, mesmo que
  a lógica de negócio já não precise mais deles — é a retenção
  obsoleta: a coleção estática age como GC Root eterna.
- ✗ O Garbage Collector é a ferramenta adequada para fechar arquivos e
  conexões de rede — o GC só libera memória RAM; recursos do S.O.
  exigem `try-with-resources` (fechamento determinístico).

## Passagem de Parâmetros

A aparente contradição desaparece quando se separa "o que é copiado"
de "o que é alterado". Java sempre copia o **valor** da variável — para
um objeto, esse valor é o endereço de memória (o "controle remoto"),
nunca o objeto físico (a "TV") em si. Quando o método executa
`prod.setPreco(999.0)`, ele está usando sua cópia do endereço para
acessar e mutar o **mesmo** objeto físico na Heap que a variável do
chamador também aponta — por isso a mudança é visível fora do método:
não há dois objetos, há um objeto e dois "controles remotos" apontando
para ele. Já quando o método executa `prod = new Produto(...)`, ele não
está mutando objeto nenhum — está reatribuindo sua própria cópia local
da variável `prod` para apontar para um endereço novo. Essa reatribuição
só existe na Stack do método chamado; a variável do chamador, que vive
em outro quadro de pilha, nunca é tocada. É a diferença entre "mudar o
que está dentro da casa" (visível para quem tem a chave) e "trocar de
casa" (só afeta quem trocou).

- ✗ Em Java existe passagem por referência estrita para objetos, assim
  como em C++ com `&` — Java só tem passagem por valor; para objetos, o
  valor copiado é o endereço.
- ✔ Ao passar um objeto para um método, o parâmetro recebe uma cópia do
  endereço de memória, não do objeto físico — é a "cópia do controle
  remoto", não da "TV".
- ✔ Alterar o estado interno de um objeto por dentro de um método (ex.:
  `prod.setPreco(999.0)`) é visto por quem chamou o método — as duas
  variáveis apontam para o mesmo objeto físico na Heap.
- ✗ Reatribuir o parâmetro (`prod = new Produto(...)`) dentro do método
  altera a variável original de quem chamou — a reatribuição só troca o
  endereço guardado na cópia local; a variável original nunca é
  afetada.
