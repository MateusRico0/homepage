# Respostas das Pausas Ativas — Aula 2

> Arquivo de apoio, não publicado (prefixo `_`). Discute as perguntas
> motivadoras das pausas ativas do `index.qmd` e dá a solução dos
> respectivos V/F. O `index.qmd` publicado só contém a pergunta e os
> quatro itens de V/F em cada pausa ativa, nunca a resolução.

## A Máquina de Estados Encapsulada

Tornar `estoque` público não deixaria a máquina de estados "mais
rápida" — deixaria de existir como máquina de estados. O ganho de
velocidade seria irrelevante (acesso a um campo `public` não é
mensuravelmente mais rápido que passar por um método simples,
especialmente com o JIT inlinando chamadas triviais); o custo real é
estrutural: qualquer código externo passaria a poder escrever
`produto.estoque = -50` diretamente, pulando por completo o método
`vender()` e as duas guardas que ele impõe (`quantidade <= 0` e
`estoque < quantidade`). Isso equivale a "teletransportar" o objeto
para um estado que o DFA nunca permitiria alcançar por nenhuma
transição válida — o equivalente, num autômato, a desenhar uma seta
nova direto para um estado qualquer, ignorando as regras do grafo.

- ✔ Os atributos privados materializam os "nós" do grafo de estados do
  objeto — o conjunto de valores dos atributos privados é o estado
  atual da máquina.
- ✔ Os métodos públicos são os únicos gatilhos autorizados a processar
  uma mudança de estado — é exatamente essa a garantia que o
  encapsulamento protege.
- ✗ Tornar o atributo `estoque` público tornaria as transições mais
  rápidas, sem custo arquitetural — tornaria o atributo público,
  permitindo que qualquer código "teletransporte" o objeto para um
  estado ilegal, pulando a validação.
- ✔ Um DFA bem definido garante que, para cada estado e evento, exista
  exatamente uma transição válida — é a definição de determinismo de
  um DFA.

## CQS e Design by Contract

Sim, viola o CQS (*Command-Query Separation*). O nome `getSaldoLiquido()`
sinaliza, pela própria convenção `get`, que o método é uma **Consulta**:
o chamador espera poder invocá-lo livremente, quantas vezes quiser,
sem consequência nenhuma além de receber um valor de volta. Ao
atualizar um contador interno a cada chamada, o método ganha um efeito
colateral escondido — deixa de ser idempotente. Um desenvolvedor que
só queria *exibir* o saldo líquido na tela, talvez chamando o método
várias vezes em testes ou em um log de depuração, estaria alterando
silenciosamente o estado do objeto sem nenhuma intenção de fazê-lo —
exatamente o mesmo risco estrutural do exemplo de `verificarSaldo()`
cobrando taxa a cada chamada, discutido no bloco anterior.

- ✔ Um Comando deve, em geral, retornar `void`, sinalizando que sua
  função é mutar o estado, não devolver dado — é a convenção que
  sinaliza "isto muda o mundo".
- ✗ Uma Consulta pode alterar o estado interno do objeto, desde que
  devolva o valor correto ao chamador — é exatamente a violação de
  CQS; uma consulta deve ser idempotente.
- ✔ Se uma pré-condição falha, a responsabilidade recai sobre quem
  chamou o método fora de hora ou com dado inválido — pré-condição é o
  contrato de entrada, sob responsabilidade do chamador.
- ✔ Se uma pós-condição falha após pré-condições válidas, o bug é do
  autor da classe, não de quem a chamou — pós-condição é o contrato de
  saída, sob responsabilidade de quem escreveu o método.

## Identidade Física e Lógica

Reescrever só `equals()` é mais perigoso do que não reescrever nenhum
dos dois porque quebra a **coerência** entre os dois métodos, em vez
de simplesmente deixá-los ambos ingênuos. Sem sobrescrever nada, tanto
`equals()` quanto `hashCode()` usam `==`/o endereço físico por baixo —
inconsistentes com o negócio, mas consistentes *entre si*: dois objetos
"diferentes" para `equals()` também caem, quase certamente, em
posições diferentes de uma `HashMap`, sem provocar corrupção estrutural
na coleção (só o problema já conhecido de não achar duplicatas de
negócio). Já se `equals()` é sobrescrito para comparar o SKU mas
`hashCode()` continua usando o endereço físico, dois objetos que
`equals()` diz serem iguais podem calcular hashes diferentes — violando
o contrato que toda `HashMap`/`HashSet` assume. O resultado é pior e
mais sutil: um item pode ser inserido, e uma busca por uma chave
"igual" (mesmo SKU, instância diferente) falha silenciosamente, porque
o hash levou a busca para outro balde da tabela. É um bug mais difícil
de detectar do que o problema original, porque às vezes o item "está lá"
e às vezes "não está", dependendo de qual instância específica foi
usada para inserir e qual para buscar.

- ✔ O operador `==` em Java compara sempre a identidade física — o
  endereço na Heap — `==` nunca considera conteúdo, só endereço.
- ✗ O `equals()` herdado de `Object`, sem sobrescrita, já entende qual
  atributo define a igualdade de negócio — o `equals()` padrão de
  `Object` também usa `==` por baixo; não conhece o domínio.
- ✔ Se dois objetos são iguais por `equals()`, seus `hashCode()` devem
  obrigatoriamente coincidir — é o contrato inseparável de
  `equals`/`hashCode`.
- ✔ Um `HashSet` pode aceitar "duplicatas" de negócio se `equals()` não
  foi sobrescrito para refletir a identidade lógica correta — sem
  `equals()` correto, dois objetos "iguais" para o negócio são tratados
  como distintos.
