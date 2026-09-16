# Gabarito — Aula 9

Gabarito consolidado: a solução discutida de cada pausa ativa da aula.
O gabarito das questões de Verdadeiro/Falso dos exercícios finais é
público, em `soluções.qmd`. Nunca publicado no site (prefixo `_`).

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
