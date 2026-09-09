# Gabarito — Aula 9

Gabarito consolidado: justificativa analítica de cada item de V/F dos
exercícios finais (`index.qmd`) e a solução discutida de cada pausa
ativa da aula. Nunca publicado no site (prefixo `_`).

## Pausas Ativas

### Pausa 1 — Late Binding, VTable e o Contrato de Sobrescrita

**Pergunta motivadora:** Se o compilador só enxerga o tipo declarado
(`Pagavel`), por que a chamada ainda "sabe" executar o código certo de
`Pix` ou `Boleto` em tempo de execução?

**Discussão:** A resposta separa duas fases inteiramente distintas. Em
tempo de compilação, o compilador só verifica que `Pagavel` declara o
método `pagamentoConfirmado(String)` — ele não sabe, e não precisa
saber, qual classe concreta vai ocupar aquela referência em produção.
Em tempo de execução, a JVM assume o trabalho: segue o ponteiro da
referência até o objeto real no Heap, consulta a VTable *daquela classe
concreta* (não da classe declarada da variável) e despacha para a
implementação correspondente. Por isso o mesmo trecho de código —
`p.pagamentoConfirmado(id)` — pode disparar comportamentos totalmente
diferentes conforme o objeto que ocupa `p` no Heap, sem que uma única
linha do código chamador precise mudar. `@Override`, por sua vez, entra
como rede de segurança sintática (evita erro de digitação na
assinatura), mas não é garantia semântica — nada no compilador impede
que o filho reescreva a lógica interna do método de um jeito
incompatível com o que o pai prometia; essa garantia semântica é
exatamente o que o LSP formaliza no bloco seguinte.

**V/F resolvido:**
- ✔ A VTable consultada pela JVM pertence à classe concreta do objeto no Heap, não ao tipo declarado da referência.
- ✔ Em Early Binding, a decisão de qual código executar é tomada pelo compilador; em Late Binding, pela JVM em tempo de execução.
- ✗ A anotação `@Override` garante, por si só, que a semântica do método sobrescrito é preservada, independente do que o código do filho faça.
- ✔ Se `Boleto` e `Pix` implementam `pagamentoConfirmado` com a mesma assinatura, o método efetivamente executado depende só da identidade real do objeto, nunca do tipo da variável usada para chamá-lo.

---

### Pausa 2 — O Paradoxo Círculo-Elipse e a Falácia do "É-UM"

**Pergunta motivadora:** Por que um Quadrado "ser" um Retângulo no
mundo real não garante que ele seja um subtipo válido de Retângulo no
código?

**Discussão:** A confusão nasce de misturar dois critérios diferentes
de "ser um X": a taxonomia do mundo real (geometricamente, todo
quadrado tem quatro lados retos e ângulos de 90°, logo é um caso
particular de retângulo) e a subtipagem de software (o comportamento
observável de uma instância precisa respeitar todas as promessas do
tipo base). O primeiro critério é estático — descreve uma propriedade
do objeto num instante. O segundo é dinâmico — precisa valer para toda
sequência de operações que o cliente possa realizar, incluindo mutações
depois da criação. `setAxes(a, b)` é justamente uma dessas operações: se
o `Retangulo` a permite alterar eixos de forma independente, e o
`Quadrado` só pode existir com `a == b`, então qualquer chamada com
`a != b` sobre um objeto que é realmente um `Quadrado` força uma escolha
sem saída honesta. A raiz do problema é a mutabilidade combinada com uma
pré-condição estrutural (`a == b`) que o tipo base não tem — remover a
mutabilidade (tornar os objetos imutáveis) ou remover a herança em favor
de uma interface comportamental mais genérica são as duas correções
legítimas, porque ambas eliminam exatamente o ponto de atrito.

**V/F resolvido:**
- ✔ Se `Retangulo` tiver um método `setAxes(a, b)` que altera largura e altura de forma independente, forçar `Quadrado extends Retangulo` cria uma chamada sem resposta honesta.
- ✔ O paradoxo desaparece completamente se `Retangulo` e `Quadrado` forem tornados imutáveis, sem nenhum método que altere os eixos depois da criação.
- ✔ Uma classe `FormaGeometrica` mais genérica, sem o método `setAxes`, resolveria o mesmo problema sem forçar uma relação de herança inválida.
- ✗ Toda relação de taxonomia do mundo real ("todo X é um Y") pode ser traduzida diretamente para uma relação `extends` no código, sem risco de violar o LSP.

---

### Pausa 3 — Checked, Unchecked e as Três Estratégias de Erro

**Pergunta motivadora:** Um método precisa lidar com um valor inválido
do chamador e, separadamente, com uma falha de rede do banco. Por que
essas duas situações não deveriam usar a mesma estratégia de
tratamento?

**Discussão:** As duas falhas têm responsáveis completamente diferentes.
Um valor inválido (por exemplo, um valor negativo passado para
`realizarPagamento`) é um erro de lógica de quem chamou o método — o
contrato foi violado antes mesmo de a operação começar. Não existe
"tratamento em tempo de execução" que conserte isso: a única correção
real está no código que fez a chamada errada, e por isso a resposta
correta é falhar imediato (Fail-Fast) com uma exceção Unchecked, nunca
capturar e tentar seguir em frente. Já uma falha de rede é uma
característica do ambiente externo, não um bug de quem chamou o método
— o mesmo código, chamado do mesmo jeito, pode funcionar perfeitamente
na próxima tentativa. Por isso ela é modelada como uma exceção Checked,
com duas saídas legítimas: tratar (buscar uma rota alternativa, como o
gateway de backup) ou reembalar (traduzir para uma exceção de domínio,
preservando a causa original como no exemplo de `FalhaComunicacaoException`).
Tratar as duas situações da mesma forma — por exemplo, engolindo um
`IllegalArgumentException` num `try/catch` "de segurança" — não resolve
nada: o bug de quem chamou continua lá, só fica mais difícil de
encontrar, porque o sintoma (comportamento incorreto) aparece longe da
causa real.

**V/F resolvido:**
- ✔ Um valor inválido passado pelo chamador é uma violação de contrato — a resposta correta é Fail-Fast, não um `try/catch` que tenta "seguir em frente".
- ✔ Uma falha de rede é uma contingência do mundo externo, que o método pode tentar contornar (rota alternativa) ou reembalar numa exceção de domínio.
- ✗ Se um desenvolvedor captura `IllegalArgumentException` só para evitar que o sistema pare, ele elimina o bug de origem, não apenas adia sua manifestação.
- ✔ Ao reembalar uma `IOException` numa exceção de domínio, é uma boa prática preservar a exceção original como causa, em vez de descartá-la.

---

## Exercícios de V/F

### Late Binding e VTable — item (a)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Se um método for marcado como `static`, a JVM ainda assim consulta a VTable da classe real do objeto para decidir qual código executar.

**Resposta:** Falso

**Justificativa:** Métodos `static` não participam de Late Binding — eles são resolvidos estaticamente pelo compilador, associados à classe declarada da referência, não à classe real do objeto no Heap. Só métodos de instância não-privados e não-`final` passam pelo mecanismo de VTable. Confundir "todo método sofre despacho polimórfico" é o erro estrutural que este item testa.

### Late Binding e VTable — item (b)

**Heurística:** Cenário contrafactual

**Afirmação:** ✔ Em um sistema que usasse Early Binding em vez de Late Binding, adicionar uma nova subclasse de `Pagavel` exigiria recompilar o código que já chamava métodos de `Pagavel`.

**Resposta:** Verdadeiro

**Justificativa:** Com Early Binding, a decisão de qual código executar é tomada em tempo de compilação, olhando o tipo estático. Isso significa que o compilador precisaria conhecer, no momento da compilação do código cliente, todas as classes concretas que algum dia ocupariam aquela referência — uma subclasse nova exigiria recompilar (ou, na prática, seria impossível de despachar corretamente sem essa recompilação). É exatamente o oposto do desacoplamento temporal que o Late Binding garante.

### Late Binding e VTable — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ A VTable consultada numa chamada `p.pagamentoConfirmado(id)` é determinada pela classe declarada da variável `p`, não pela classe do objeto apontado por ela.

**Resposta:** Falso

**Justificativa:** É exatamente o inverso do mecanismo de Late Binding: a VTable consultada é sempre a da classe concreta do objeto no Heap (a "realidade do Heap"), nunca a do tipo declarado da referência (a "lente do compilador"). Essa inversão de responsabilidade é o próprio motivo de o polimorfismo funcionar.

### Late Binding e VTable — item (d)

**Heurística:** Transferência de domínio

**Afirmação:** ✗ Se duas classes não relacionadas por herança ou interface comum implementarem um método com a mesma assinatura, a JVM ainda assim pode fazer Late Binding entre elas ao chamar esse método através de uma referência comum.

**Resposta:** Falso

**Justificativa:** Late Binding pressupõe uma referência de um tipo comum (uma superclasse ou interface) através da qual o código cliente enxerga o método. Sem herança ou interface compartilhada, não existe uma "referência comum" cujo tipo declare o método — o compilador simplesmente não aceitaria uma variável desse tipo comum chamando o método em questão. Duas classes soltas com o mesmo nome de método não formam polimorfismo, só uma coincidência de nomenclatura (a diferença entre "mesmo nome" e "mesmo contrato de tipo").

---

### Sobrescrita como Contrato (`@Override`) — item (a)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Se um método sobrescrito muda a semântica do método original (por exemplo, de "validar" para "excluir o registro"), o compilador não impede essa mudança, mesmo com `@Override` presente.

**Resposta:** Verdadeiro

**Justificativa:** `@Override` é uma checagem puramente sintática — ela confirma que a assinatura corresponde a um método existente no supertipo, nada mais. O compilador não tem como avaliar a semântica de negócio de um método (o que "validar" ou "excluir" significam no domínio), então uma mudança de significado radical compila normalmente. É essa lacuna — sintaxe correta, semântica quebrada — que o LSP existe para cobrir.

### Sobrescrita como Contrato (`@Override`) — item (b)

**Heurística:** Cenário contrafactual

**Afirmação:** ✔ Se a classe pai remover o método que uma subclasse originalmente sobrescrevia (renomeando-o), o compilador acusa erro na subclasse graças à anotação `@Override`.

**Resposta:** Verdadeiro

**Justificativa:** É exatamente o propósito de `@Override`: se o método anotado deixar de corresponder a nenhum método do supertipo (porque foi renomeado, teve a assinatura alterada, ou removido), o compilador rejeita a compilação da subclasse. Sem a anotação, esse erro passaria despercebido — o método "sobrescrito" viraria silenciosamente um método novo e independente.

### Sobrescrita como Contrato (`@Override`) — item (c)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Um método sobrescrito que devolve um subtipo mais específico do tipo de retorno original (covariância de retorno) ainda é uma sobrescrita válida.

**Resposta:** Verdadeiro

**Justificativa:** Java permite covariância de retorno desde o Java 5: o método sobrescrito pode devolver um subtipo do tipo de retorno declarado no pai, porque isso só *fortalece* a pós-condição (o cliente que esperava o tipo mais genérico ainda recebe algo compatível) — coerente com a Regra 2 do LSP vista nesta aula (pós-condições podem ser fortalecidas, nunca enfraquecidas).

### Sobrescrita como Contrato (`@Override`) — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ `@Override` transforma automaticamente qualquer alteração de comportamento do método em uma violação de compilação, independente da assinatura.

**Resposta:** Falso

**Justificativa:** `@Override` só valida assinatura (nome, parâmetros, tipo de retorno compatível). Alterações de comportamento — desde que a assinatura seja mantida — compilam sem problema algum; é justamente por isso que violações semânticas do LSP não são pegas pelo compilador, precisando de disciplina de design (e não de uma anotação) para serem evitadas.

---

### LSP: a Definição Formal — item (a)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Se $\phi(x)$ representa que "o método nunca retorna null", e existe um subtipo $S$ de $T$ cujas instâncias podem retornar null nesse mesmo método, a fórmula $\forall x{:}T,\phi(x) \implies \forall y{:}S,\phi(y)$ é violada por esse subtipo.

**Resposta:** Verdadeiro

**Justificativa:** É a aplicação direta da fórmula: se $\phi$ vale para todo $x$ do tipo $T$ (nunca retorna null), mas existe um $y$ do subtipo $S$ para o qual $\phi(y)$ é falso (retorna null), a implicação universal quantificada falha — e é exatamente essa falha que caracteriza uma violação de LSP (nesse caso, uma violação de pós-condição).

### LSP: a Definição Formal — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ O LSP é satisfeito sempre que o subtipo compila corretamente contra a interface do tipo base, independentemente do comportamento em tempo de execução.

**Resposta:** Falso

**Justificativa:** É a distinção central da aula entre sintaxe e semântica — compilar corretamente garante apenas que as assinaturas são compatíveis (subtyping estrutural), não que o comportamento observável (as propriedades $\phi$) se mantenha. `PagamentoCartaoBloqueado` compila perfeitamente contra `Pagavel` e ainda assim viola o LSP ao lançar uma exceção inesperada.

### LSP: a Definição Formal — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Um sistema de testes automatizados que roda a mesma bateria de testes contra `Pagavel`, trocando só a implementação concreta injetada, está aplicando na prática a intuição do "cliente cego" usada para explicar o LSP.

**Resposta:** Verdadeiro

**Justificativa:** Esse padrão de teste (às vezes chamado de "contract test" ou "teste de substituição") é exatamente a intuição do cliente cego posta em prática: o código de teste não sabe (nem precisa saber) qual implementação concreta está recebendo, e espera que todas passem pelos mesmos testes — se uma implementação falha nos testes que as demais passam, ela provavelmente viola o LSP em relação às outras.

### LSP: a Definição Formal — item (d)

**Heurística:** Cenário contrafactual

**Afirmação:** ✗ Se um subtipo $S$ satisfaz o LSP em relação a $T$, isso implica necessariamente que $T$ também satisfaz o LSP em relação a $S$.

**Resposta:** Falso

**Justificativa:** O LSP é uma relação assimétrica por definição — ela diz respeito à substituição de $T$ por $S$ (o subtipo assume o lugar do supertipo), não o contrário. $T$ não é sequer, em geral, um subtipo de $S$, então a pergunta "$T$ satisfaz o LSP em relação a $S$" nem está bem formada na direção inversa — inverter a relação de subtipagem livremente é o erro estrutural deste item.

---

### Pré-condições no LSP — item (a)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Se a base aceita valores de 0 a 1000, e uma subclasse aceita valores de -1000 a 2000 (um domínio maior), essa subclasse respeita a regra de pré-condições do LSP.

**Resposta:** Verdadeiro

**Justificativa:** Enfraquecer (ampliar) uma pré-condição é permitido pela Regra 1 do LSP — a subclasse fica *mais* tolerante, nunca menos, então todo cliente que já enviava valores dentro de 0–1000 continua funcionando exatamente como antes, e ainda passa a aceitar mais casos. Não há surpresa possível para o cliente existente.

### Pré-condições no LSP — item (b)

**Heurística:** Contrafactual (já coberta no corpo da aula, adaptada)

**Afirmação:** ✔ Uma subclasse pode enfraquecer uma pré-condição do pai (aceitar mais entradas do que ele aceitava) sem violar o LSP.

**Resposta:** Verdadeiro

**Justificativa:** É a formulação direta da Regra 1: pré-condições podem ser mantidas ou enfraquecidas, nunca fortalecidas. Aceitar mais entradas do que o pai aceitava nunca surpreende um cliente que já respeitava o contrato original — o risco só aparece quando a subclasse restringe (fortalece) o domínio de entradas válidas.

### Pré-condições no LSP — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Se um método do pai não documenta explicitamente nenhuma pré-condição, uma subclasse está livre para adicionar qualquer restrição de entrada sem risco de violar o LSP.

**Resposta:** Falso

**Justificativa:** A ausência de documentação explícita não significa ausência de pré-condição implícita — o comportamento observado pelos clientes existentes (todo valor que já funcionava) define, na prática, o contrato real. Adicionar uma restrição nova quebra qualquer cliente que já passava um valor agora rejeitado, independentemente de essa pré-condição estar ou não escrita num Javadoc — é o mesmo problema de "invariante invisível" já visto na Aula 8, agora aplicado a pré-condições.

### Pré-condições no LSP — item (d)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Fortalecer uma pré-condição é equivalente, na prática, a remover funcionalidade que o cliente já esperava ter disponível através do tipo base.

**Resposta:** Verdadeiro

**Justificativa:** Do ponto de vista do cliente, "meu valor de R\$50 antes era aceito e agora é rejeitado" tem o mesmo efeito observável de uma funcionalidade removida — não importa que a assinatura do método não tenha mudado, o conjunto de operações que funcionavam através do tipo base encolheu. É esse efeito, não a mudança sintática, que caracteriza a violação.

---

### Pós-condições e Invariantes no LSP — item (a)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Se o pai promete retornar um objeto nunca nulo, e o filho retorna um objeto "vazio" (um objeto real, mas sem dado útil) em vez de null, isso ainda pode violar a regra de pós-condições dependendo do que o cliente faz com o resultado.

**Resposta:** Verdadeiro

**Justificativa:** Retornar um objeto não-nulo tecnicamente cumpre "nunca retornar null", mas a pós-condição real que o cliente espera geralmente é mais rica do que isso — um "ID de cobrança válido", por exemplo, implica um ID que pode ser usado para consultar o pagamento depois. Um objeto vazio ou um ID sem sentido evita a `NullPointerException` só na superfície, mas ainda entrega "menos do que o prometido" seja qual for a operação seguinte do cliente — a mesma lição do exemplo `return "";` do bloco de pós-condições.

### Pós-condições e Invariantes no LSP — item (b)

**Heurística:** Contrafactual (aplicação da Regra 2)

**Afirmação:** ✔ Uma subclasse que sempre retorna um resultado mais específico e mais completo do que o pai prometia está fortalecendo a pós-condição, o que é permitido pelo LSP.

**Resposta:** Verdadeiro

**Justificativa:** É a formulação direta da Regra 2: pós-condições podem ser mantidas ou fortalecidas, nunca enfraquecidas. Entregar mais do que o prometido nunca surpreende negativamente um cliente que já esperava o mínimo garantido pelo pai — o risco só existe na direção contrária (entregar menos).

### Pós-condições e Invariantes no LSP — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Uma subclasse que herda um atributo `protected` responsável por uma invariante crítica pode alterar esse atributo livremente, desde que não sobrescreva nenhum método do pai.

**Resposta:** Falso

**Justificativa:** O acesso `protected` dá ao filho a capacidade técnica de alterar o atributo diretamente, mas a Regra 3 (preservação de invariantes) não depende de "sobrescrever um método" — é uma obrigação sobre o *estado* do objeto em qualquer ponto observável, independente de qual código (herdado ou próprio) o alterou. Alterar `saldo` diretamente para um valor negativo, sem passar por nenhum método sobrescrito, ainda quebra a invariante `saldo >= 0` da mesma forma destrutiva.

### Pós-condições e Invariantes no LSP — item (d)

**Heurística:** Caso limite/extremo

**Afirmação:** ✗ Preservar uma invariante herdada significa apenas que o valor do atributo nunca muda depois da construção do objeto.

**Resposta:** Falso

**Justificativa:** Confunde invariante com imutabilidade. Uma invariante como `saldo >= 0` permite — e espera — que o valor mude ao longo da vida do objeto (depósitos, saques); o que ela proíbe é que o valor saia de uma região válida em qualquer momento observável. Uma classe pode ter atributos totalmente mutáveis e ainda assim preservar rigorosamente suas invariantes, desde que toda transição respeite a regra.

---

### O Paradoxo Círculo-Elipse — item (a)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ O paradoxo Círculo-Elipse só aparece porque `Elipse` expõe um método mutável (`setAxes`) que permite alterar os eixos de forma independente depois da criação do objeto.

**Resposta:** Verdadeiro

**Justificativa:** Sem mutabilidade pós-construção, nunca existiria a chamada `elipse.setAxes(10, 20)` que força a escolha impossível — o objeto nasceria já com seus eixos definitivos, e um `Circulo` (com `a == b` desde a criação) seria um `Elipse` perfeitamente substituível para qualquer operação de leitura. É a mutação de estado depois da construção que introduz o risco.

### O Paradoxo Círculo-Elipse — item (b)

**Heurística:** Contrafactual

**Afirmação:** ✔ Se `Circulo` e `Elipse` fossem ambos imutáveis (sem nenhum `setAxes`, só construtores), a herança entre eles deixaria de gerar a mesma violação de LSP.

**Resposta:** Verdadeiro

**Justificativa:** Removendo a mutação, não existe mais nenhuma operação que force um `Circulo` a escolher entre violar sua própria natureza matemática ou a expectativa do cliente — todo objeto já nasce com seu formato definitivo e correto. É exatamente a saída "objetos imutáveis" apontada na aula como uma das duas correções honestas.

### O Paradoxo Círculo-Elipse — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ O paradoxo prova que herança geométrica sempre deve ser evitada em qualquer sistema orientado a objetos, mesmo quando os objetos são imutáveis.

**Resposta:** Falso

**Justificativa:** O paradoxo é uma consequência específica da combinação mutabilidade + pré-condição estrutural adicional do subtipo (`a == b`), não uma condenação geral de qualquer hierarquia que modele formas geométricas. Com objetos imutáveis, como o item (b) já estabelece, a mesma hierarquia deixa de violar o LSP — generalizar "evitar sempre" é o exagero que este item testa.

### O Paradoxo Círculo-Elipse — item (d)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Substituir a herança `Circulo extends Elipse` por uma interface comum `FormaGeometrica`, sem o método `setAxes`, é uma forma válida de evitar o paradoxo.

**Resposta:** Verdadeiro

**Justificativa:** É a segunda saída honesta discutida na aula: se o comportamento mutável de $S$ não condiz com $T$, a correção pode ser abandonar a relação de herança problemática e usar uma abstração mais genérica (uma interface comportamental, como calcular área ou perímetro) que não inclua o método causador do conflito — sem `setAxes` na interface comum, não há mais nenhuma chamada que force a escolha impossível.

---

### Contratos de Exceção e o LSP — item (a)

**Heurística:** Caso limite/extremo

**Afirmação:** ✗ Uma subclasse que lança uma exceção verificada (`checked`) não declarada pelo método do pai obriga o código cliente já existente a ser recompilado ou reescrito para tratar essa nova exceção.

**Resposta:** Falso

**Justificativa:** Pelo contrário: o compilador Java *impede* essa situação diretamente — se o método do pai não declara uma exceção checked, a subclasse não pode declarar (nem lançar sem capturar internamente) uma checked nova que não seja subtipo de alguma já declarada, exatamente para proteger o código cliente de precisar mudar. É por isso que a violação real do LSP com exceções costuma vir de exceções *unchecked* novas (`RuntimeException` e subtipos), que o compilador não bloqueia.

### Contratos de Exceção e o LSP — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Lançar `UnsupportedOperationException` para "pular" um método herdado que a subclasse não quis implementar é uma prática recomendada quando a subclasse é uma especialização legítima.

**Resposta:** Falso

**Justificativa:** É exatamente o padrão apontado na aula como violação quase invariável do LSP — se uma subclasse precisa "pular" um método herdado lançando uma exceção que o cliente do tipo base não esperava, isso é sinal de que ela não deveria ser um subtipo daquele pai (talvez nem seja uma especialização legítima, já que não consegue honrar toda a interface). "Especialização legítima" não perdoa esse padrão — ao contrário, o padrão costuma ser evidência de que a especialização não é, de fato, legítima.

### Contratos de Exceção e o LSP — item (c)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Se `Pagavel.criarCobranca()` não declara nenhuma exceção, uma subclasse que lança uma `RuntimeException` inesperada em condições normais de uso ainda pode violar o espírito do LSP, mesmo sem quebrar a compilação.

**Resposta:** Verdadeiro

**Justificativa:** Exceções unchecked não são bloqueadas pelo compilador mesmo quando não declaradas — é por isso que `PagamentoCartaoBloqueado` lançando `SecurityException` compila normalmente e ainda assim viola o LSP: o comportamento observável surpreende um cliente que nunca previu aquele erro em condições normais. A proteção do compilador cobre só exceções checked; a proteção contra exceções unchecked inesperadas depende inteiramente da disciplina de design.

### Contratos de Exceção e o LSP — item (d)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Um subtipo que lança um subtipo mais específico de uma exceção já esperada pelo pai (por exemplo, `SaldoInsuficienteException extends PagamentoException`, quando o pai já declarava lançar `PagamentoException`) respeita o contrato de exceção do LSP.

**Resposta:** Verdadeiro

**Justificativa:** Um cliente que já captura (ou declara) `PagamentoException` continua funcionando sem qualquer mudança, porque `SaldoInsuficienteException` é capturada pelo mesmo `catch (PagamentoException e)` — é a mesma lógica de covariância já vista para tipos de retorno, aplicada a exceções: especializar dentro da hierarquia já esperada nunca surpreende o cliente.

---

### Taxonomia do Erro e Captura Polimórfica — item (a)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Organizar exceções como uma hierarquia de tipos (em vez de uma lista de mensagens de texto) permite que o mesmo bloco `catch` trate corretamente subtipos de exceção criados depois que aquele código já foi escrito.

**Resposta:** Verdadeiro

**Justificativa:** É a mesma vantagem de desacoplamento temporal do polimorfismo comum: um `catch (PagamentoException e)` escrito hoje automaticamente também captura qualquer subtipo de `PagamentoException` criado meses depois (uma nova `PixRecusadoException`, por exemplo), sem que o código de tratamento precise ser tocado — a captura é por tipo, não por identificador de mensagem.

### Taxonomia do Erro e Captura Polimórfica — item (b)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Se um bloco `catch (PagamentoException e)` vier antes de um bloco `catch (CartaoExpiradoException e)` no mesmo `try`, sendo `CartaoExpiradoException` subtipo de `PagamentoException`, o código não compila.

**Resposta:** Verdadeiro

**Justificativa:** Em Java, blocos `catch` são avaliados em ordem, e o primeiro cujo tipo corresponde captura a exceção. Se o bloco mais genérico (`PagamentoException`) vier antes do mais específico (`CartaoExpiradoException`), o segundo bloco se torna código inalcançável — nenhuma exceção chegaria até ele, já que qualquer `CartaoExpiradoException` já teria sido capturada pelo `catch` genérico anterior. O compilador Java detecta essa situação e recusa a compilação ("exception CartaoExpiradoException has already been caught"), exatamente porque a hierarquia de exceções permite múltiplos níveis de generalidade compilarem contra o mesmo objeto lançado, e a ordem determina qual nível efetivamente reage.

### Taxonomia do Erro e Captura Polimórfica — item (c)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Capturar `Exception` de forma genérica no nível mais alto do sistema é sempre uma boa prática, pois garante que nenhum erro, de nenhum tipo, escape sem tratamento.

**Resposta:** Falso

**Justificativa:** É exatamente o cuidado simétrico apontado na aula: capturar `Exception` (ou `Throwable`) indiscriminadamente esconde erros de lógica genuínos — como um `NullPointerException` por um bug de inicialização — que deveriam interromper a execução para correção, não ser silenciados junto com falhas de negócio esperadas. "Nenhum erro escapa" soa seguro, mas na prática troca bugs visíveis por comportamento incorreto silencioso.

### Taxonomia do Erro e Captura Polimórfica — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Tratar o erro como uma transição de estado prevista (por exemplo, de "Processando" para "Falha de Pagamento") é incompatível com o uso de uma hierarquia de exceções para organizar essas falhas.

**Resposta:** Falso

**Justificativa:** As duas ideias são complementares, não concorrentes: a "transição de estado prevista" é o papel *conceitual* do erro na máquina de estados do objeto (Aula 2); a hierarquia de exceções é o *mecanismo técnico* usado para representar e reagir a cada tipo de transição de falha. Uma máquina de estados bem desenhada usa justamente uma taxonomia de exceções para diferenciar os motivos pelos quais a transição para "Falha" ocorreu.

---

### Checked vs. Unchecked e Wrapping — item (a)

**Heurística:** Transferência de domínio

**Afirmação:** ✔ Se um método interno de baixo nível lança `SQLException` e essa exceção se propaga sem tradução até um controlador de alto nível, o `CheckoutController` passa a depender de um detalhe de implementação (o uso de SQL) que deveria estar oculto.

**Resposta:** Verdadeiro

**Justificativa:** É o problema central que motiva o wrapping: se `SQLException` vaza até o controlador, qualquer código que capture ou trate esse erro no nível de negócio precisa "saber" que a persistência usa SQL — trocar o banco de dados por um NoSQL, mais tarde, quebraria esse código de tratamento. Traduzir para uma exceção de domínio isola exatamente essa dependência.

### Checked vs. Unchecked e Wrapping — item (b)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Reembalar uma exceção técnica numa exceção de domínio, descartando a exceção original em vez de passá-la como causa, preserva completamente a capacidade de depuração técnica do erro.

**Resposta:** Falso

**Justificativa:** É o oposto do que a aula recomenda: descartar a exceção original apaga o *stack trace* técnico (onde exatamente a `IOException` ocorreu, qual linha, qual causa de mais baixo nível) — a depuração técnica fica impossível a partir daquele ponto. Preservar a causa original (o segundo argumento do construtor, como em `FalhaComunicacaoException("...", e)`) é o que mantém a rastreabilidade sem vazar o detalhe técnico para a interface pública.

### Checked vs. Unchecked e Wrapping — item (c)

**Heurística:** Caso limite/extremo

**Afirmação:** ✔ Um valor de entrada inválido detectado logo no início de um método é um exemplo típico de erro que deve ser tratado com uma exceção Unchecked, seguindo o princípio Fail-Fast.

**Resposta:** Verdadeiro

**Justificativa:** É a aplicação direta do critério Unchecked/DNA: um valor inválido na entrada é uma violação de contrato de quem chamou o método, não uma contingência do ambiente externo — a resposta correta é falhar imediatamente (Fail-Fast), não esperar que o erro se manifeste de forma confusa mais adiante no fluxo.

### Checked vs. Unchecked e Wrapping — item (d)

**Heurística:** Falsa dicotomia

**Afirmação:** ✗ Capturar uma `IllegalArgumentException` lançada por uma validação de contrato, só para permitir que a execução continue silenciosamente com um valor padrão, resolve o problema de origem que gerou a exceção.

**Resposta:** Falso

**Justificativa:** É o mesmo erro discutido na Pausa Ativa 3: capturar um erro de DNA (violação de contrato) e seguir em frente com um valor padrão não corrige o código que chamou o método com um argumento inválido — só esconde o sintoma, trocando uma falha visível e rastreável por um comportamento silenciosamente incorreto que vai se manifestar, sem explicação aparente, em algum ponto mais distante do sistema.
