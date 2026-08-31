# Respostas das Pausas Ativas — Aula 6

> Arquivo de apoio, não publicado (prefixo `_`). Discute as perguntas
> motivadoras das pausas ativas do `index.qmd` e dá a solução dos
> respectivos V/F. O `index.qmd` publicado só contém a pergunta e os 4
> itens de V/F em cada pausa ativa (idênticos nas notas e nos slides);
> a resolução, nos slides, aparece no slide seguinte — mas nunca nas
> notas em HTML.

## Interfaces Modernas e o Mutador Cego

Não — a interface continua tão sem estado quanto sempre foi. O que o
método `default aplicarJuros` faz é *orquestrar* uma mudança, não
*armazená-la*: ele chama `getSaldo()` para ler o valor atual e
`setSaldo()` para escrever o novo valor, mas os dois métodos abstratos
são implementados pela classe concreta (`Pix`, no exemplo), que é
quem de fato guarda `saldoReal` num atributo de instância. A interface
sabe *a regra* (multiplicar pela taxa de juros, validar que a taxa não
é negativa) sem saber *onde* o dado mora fisicamente — daí o nome
"Mutador Cego": ela muta o estado do objeto às cegas, confiando que a
classe concreta implementou `getSaldo`/`setSaldo` corretamente. Essa
divisão de trabalho — interface como "cérebro" da regra, classe
concreta como "músculos" do armazenamento — é o que permite que
`Pix`, `Boleto` e `Cartao` sigam exatamente a mesma regra de juros sem
duplicar uma linha de código (DRY), mesmo cada um guardando o saldo de
um jeito completamente diferente por dentro.

- ✔ Um método `default` pode chamar outros métodos abstratos da mesma
  interface, confiando que a classe concreta os implementa — é
  exatamente assim que `aplicarJuros` chama `getSaldo()`/`setSaldo()`
  sem saber como cada um foi implementado.
- ✗ O método `aplicarJuros` armazena o novo saldo dentro da própria
  interface, num atributo privado — falso: interfaces continuam
  proibidas de ter atributos de instância; o estado real mora
  inteiramente na classe concreta (`saldoReal` em `Pix`).
- ✔ O padrão Mutador Cego funciona porque a interface conhece o
  "cérebro" (regra) e delega o armazenamento aos "músculos" (classe
  concreta) — é a definição exata do padrão apresentado nesta aula.
- ✔ Um método `static` de interface pode ser chamado sem nenhuma
  instância de uma classe concreta — métodos `static` pertencem ao
  tipo (à interface), não a uma instância, por isso `Pagavel.isValorValido(v)`
  funciona sem nenhum objeto `Pagavel` na mão.

## Interfaces e o Contrato de Tipo

Não — e o que impede isso é, de novo, a proibição de estado. Métodos
`default` (e `static`, e `private`) trazem *comportamento* para dentro
da interface, mas nunca trazem *dados próprios*: mesmo um método
`default` sofisticado como `aplicarJuros` não tem onde guardar nada,
porque a interface nunca ganhou um atributo de instância. Essa é
precisamente a fronteira entre interface e classe: uma classe (mesmo
abstrata) pode ter estado protegido compartilhado por todas as
subclasses; uma interface, por mais rica que seja em métodos
`default`, nunca pode. É isso que permite que `Pix` (com lógica
complexa de QR Code) e `CartaoDeCredito` (com lógica de criptografia
de chip) — duas classes sem absolutamente nada em comum em termos de
dados — sejam tratadas como exatamente o mesmo tipo `Pagavel` pelo
`CheckoutController`: o tipo, aqui, é definido pelo comportamento
prometido, não pela estrutura interna.

- ✔ Uma interface define o que um objeto faz, sem exigir
  compartilhamento de estrutura interna ("DNA") — é a definição de
  Tipo Puro apresentada nesta aula.
- ✗ Métodos `default` e `static` tornam a interface equivalente a uma
  classe comum, incluindo suporte a atributos de instância — falso:
  mesmo com `default`/`static`, a interface permanece proibida de ter
  qualquer atributo de instância; só ganha comportamento, nunca dado
  próprio.
- ✔ Duas classes sem nenhum atributo em comum podem, ainda assim, ser
  do mesmo tipo se implementarem a mesma interface — é exatamente o
  caso de `Pix` e `CartaoDeCredito` nesta aula.
- ✔ Esquecer de implementar um método do contrato de uma interface é
  um erro detectado em tempo de compilação — o Java simplesmente não
  compila enquanto o contrato não for cumprido por inteiro.

## Exceções como Guardas de Contrato

Lançar uma exceção é um ato de honestidade porque o objeto de baixo
nível, no exato momento em que percebe que não pode cumprir o que foi
pedido (um valor de pagamento negativo, por exemplo), admite isso
imediatamente em vez de fingir sucesso — retornar `null`, `0` ou
`false` só posterga a descoberta do problema, empurrando-o para uma
linha distante do sistema que não tem relação óbvia com a causa real
(o "erro de silenciar"). Tratar a exceção, por outro lado, é um ato de
resiliência do sistema como um todo: o componente de alto nível (o
`CheckoutController`, por exemplo) recebe o aviso honesto do nível
baixo e decide como reagir — mostrar uma mensagem ao usuário, registrar
o erro, tentar de novo — sem deixar a falha derrubar o fluxo inteiro.
As duas metades dependem uma da outra: a honestidade de quem lança só
tem valor se existir, em algum ponto acima, alguém preparado para
tratá-la; e o tratamento só é possível porque quem lançou avisou
explicitamente, via `throws`, que aquele contrato podia falhar.

- ✗ O compilador é suficiente para impedir que um preço negativo seja
  aceito por um método que recebe `double` — falso: o compilador só
  garante o tipo sintático (`double`), não a validade semântica do
  valor; um `-50.0` é um `double` perfeitamente válido para o
  compilador.
- ✔ Retornar `null` ou `0` para sinalizar um erro é uma prática que só
  adia a descoberta do problema real — é o "erro de silenciar"
  descrito nesta aula, que troca uma falha imediata e rastreável por
  uma falha tardia e sem relação aparente com a causa.
- ✔ Segundo a diretriz desta aula, componentes de baixo nível devem
  lançar exceções, e componentes de alto nível devem decidir como
  reagir — é a diretriz explícita de responsabilidade que fecha o
  bloco.
- ✔ Um `throws NotificationException` na assinatura de um método é uma
  forma de tornar explícita uma possível falha do contrato — é
  exatamente a ideia de "exceção como cláusula do contrato" desta
  aula.
