# Gabarito — Aula 11

Gabarito consolidado: a solução discutida de cada pausa ativa da aula.
O gabarito das questões de Verdadeiro/Falso dos exercícios finais é
público, em `soluções.qmd`. Nunca publicado no site (prefixo `_`).

## Pausas Ativas

### Pausa 1 — O Vocabulário dos Padrões e as Três Famílias

**Pergunta motivadora:** Se um colega descrever uma solução como "uma
classe que traduz chamadas de uma biblioteca externa incompatível para
o formato que meu sistema espera", a que família de padrões essa
solução pertence — e por que classificá-la pela família certa importa
mais do que decorar o nome "Adapter"?

**Discussão:** A solução descrita — harmonizar duas interfaces
incompatíveis sem alterar o comportamento interno de nenhuma delas —
tem como foco a **topologia** da comunicação entre as partes, não a
distribuição de obrigações no tempo (isso seria Comportamental) nem a
gênese de objetos (isso seria Criação). É exatamente a definição de
família Estrutural. Saber a família antes do nome importa porque o
propósito arquitetural é o que orienta a decisão de projeto: um
engenheiro que reconhece "isto é um problema de topologia entre duas
interfaces" já sabe que a solução vai envolver compor objetos numa
nova fronteira comum, mesmo antes de lembrar que esse padrão específico
se chama Adapter. O nome vem depois, como atalho de comunicação — mas
o raciocínio estrutural que leva até ele é o que realmente importa.

**V/F resolvido:**
- ✔ Uma solução cujo objetivo é permitir que duas interfaces incompatíveis conversem entre si, sem alterar o comportamento interno de nenhuma das duas, se classifica na família Estrutural, não na Comportamental.
- ✗ Se um engenheiro aplicar rigorosamente a estrutura de classes de um Padrão de Projeto sobre um sistema que ainda usa variáveis globais e funções soltas (sem nenhum encapsulamento), o padrão resolverá o problema de coesão do sistema da mesma forma que resolveria num sistema já orientado a objetos.
- ✗ Uma biblioteca como o Spring, que instancia os objetos da aplicação e invoca os métodos do desenvolvedor em momentos que ela mesma decide, exemplifica a mesma relação de controle de fluxo que um Padrão de Projeto estabelece com o código do desenvolvedor.
- ✔ Dois padrões pertencentes a famílias diferentes (por exemplo, um Estrutural e um Comportamental) podem, ainda assim, ser aplicados na mesma classe simultaneamente, resolvendo problemas arquiteturais distintos e não conflitantes.

---

### Pausa 2 — Entidade vs. Value Object

**Pergunta motivadora:** Se um sistema de biblioteca representasse cada
exemplar físico de um livro como um Value Object (sem ID, igualdade por
atributo), o que quebraria no momento em que dois exemplares idênticos
do mesmo título precisassem ser rastreados separadamente (um
emprestado, outro na prateleira)?

**Discussão:** O rastreio individual quebraria porque um Value Object
é, por definição, indistinguível de outro com o mesmo conteúdo —
`equals()` compara valores, não identidade. Dois exemplares físicos com
título, autor e edição idênticos produziriam VOs "iguais" mesmo sendo
objetos físicos diferentes no mundo real, um emprestado e outro na
prateleira. A pergunta de negócio aqui — "este exemplar específico está
disponível?" — exige uma identidade persistente que sobrevive a
qualquer mudança de estado (por exemplo, de "disponível" para
"emprestado"), o que é exatamente a definição de Entidade. A correção
é modelar cada exemplar físico como uma Entidade com um identificador
próprio (um número de patrimônio, por exemplo), reservando o Value
Object para os metadados do título (nome, autor, ISBN) que de fato são
compartilhados por todos os exemplares daquela edição.

**V/F resolvido:**
- ✔ Se dois exemplares físicos de um mesmo título tiverem exatamente os mesmos atributos de valor (título, autor, edição), modelá-los como Value Objects tornaria `equals()` incapaz de distinguir qual exemplar específico está emprestado e qual está na prateleira.
- ✔ Um `Dinheiro` de R$ 50 criado numa parte do sistema é sempre `equals()` a outro `Dinheiro` de R$ 50 criado em outra parte completamente diferente do sistema, mesmo sem nenhuma relação de criação entre os dois.
- ✗ Se a classe `Aluno` permitisse alterar o valor do campo `ra` através de um método público após a construção, isso não comprometeria a modelagem de `Aluno` como Entidade, desde que `curso` continuasse mutável.
- ✔ Um sistema de reservas de assento de cinema que precisa saber se o assento B12 da sessão das 20h (especificamente aquele, não outro assento idêntico em atributos) já foi reservado se beneficia de modelar o assento como Entidade, não como Value Object.

---

### Pausa 3 — Factory Method e Acoplamento Direto

**Pergunta motivadora:** Se um novo requisito pedir notificação por
WhatsApp, por que a resposta correta nunca deveria envolver abrir e
editar os 50 pontos do sistema que hoje disparam
`NotificacaoPedidoFactory.criar(...)`?

**Discussão:** Porque nenhum desses 50 pontos conhece uma classe
concreta de notificação — todos conversam apenas com a abstração
`NotificacaoPedido`, obtida através da fábrica. Toda a decisão de "qual
classe instanciar" está confinada a um único lugar:
`NotificacaoPedidoFactory`. Para acomodar o WhatsApp, basta escrever
uma nova classe `NotificacaoPedidoWhatsApp` implementando
`NotificacaoPedido` e adicionar um novo caso no `switch` da fábrica —
nenhum dos 50 pontos de disparo muda uma linha, porque nenhum deles
jamais dependeu da classe concreta. Se a arquitetura fosse a oposta —
cada ponto de disparo decidindo por si mesmo qual classe instanciar —,
o mesmo requisito exigiria caçar e editar os 50 lugares, cada edição
sendo uma nova chance de esquecer um deles ou introduzir uma
inconsistência.

**V/F resolvido:**
- ✗ Se `ServicoDePedidos` chamasse diretamente `new NotificacaoPedidoEmail()` em vez de pedir a `NotificacaoPedidoFactory`, adicionar um novo meio de notificação ainda seria possível sem alterar nenhum código que já dispara notificações.
- ✔ Um sistema de geração de relatórios que decide, em tempo de execução, se deve instanciar `RelatorioPDF` ou `RelatorioExcel` a partir de uma preferência do usuário, centralizando essa decisão numa única classe fábrica, aplica a mesma lógica estrutural do Factory Method visto em aula.
- ✗ Se `RepositorioPedidosFactory` sempre devolvesse a mesma implementação concreta (`RepositorioPedidosMySQL`), injetar essa fábrica em vez de instanciar diretamente `RepositorioPedidosMySQL` não traria nenhum benefício arquitetural, mesmo pensando em testes automatizados futuros.
- ✗ Um `ServicoDePedidos` que recebe uma `RepositorioPedidosFactory` no construtor, mas depois usa `instanceof RepositorioPedidosMySQL` para decidir se aplica uma otimização específica daquele banco, preserva integralmente a Inversão de Dependência que a injeção da fábrica pretendia estabelecer.
