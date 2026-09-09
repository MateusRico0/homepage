## Resumo — Aula 11

Fontes: (a) `_fontes/material/Teoria/Aula 8.tex`, linhas 806–944 (as
duas seções finais do arquivo, deliberadamente deferidas pela Aula 10:
`\section{Padrões de Projeto}` e `\section{Conclusão}`) — o vocabulário
geral de Padrões de Projeto: origem histórica (Christopher Alexander,
arquitetura civil), o marco GoF de 1994 (Gamma/Helm/Johnson/Vlissides,
23 padrões, os dois pilares Composição+Polimorfismo), o que um padrão
de projeto explicitamente **não** é (não é *framework*, não é
algoritmo estrutural, não cura código procedural), o vocabulário
arquitetural como linguagem ubíqua, e as três famílias (Comportamento,
Estrutural, Criação); (b) `_fontes/material/Teoria/Aula 9.tex` (1180
linhas, lida por completo) — cobre três blocos reais:
`\section{Imutabilidade e o Padrão Value Object}` (mutabilidade como
fonte de bugs, *aliasing*, Entidade vs. Value Object, operacionalização
da imutabilidade, Obsessão por Primitivos, benefícios arquiteturais),
`\section{State Pattern}` (deixado para a Aula 12 — ver decisão de
escopo abaixo) e `\section{Criação Segura - Builder e Factory Method}`
(o problema do construtor sujo, o padrão Builder com interface fluente,
o padrão Factory Method, e a Inversão de Dependência na criação via
fábrica abstrata).

Esta aula usa deliberadamente **dois** trechos-fonte em sequência: o
vocabulário geral de padrões (Aula 8.tex) serve de "mapa" antes de
mergulhar em três padrões concretos e novos (Value Object, Builder,
Factory Method), todos do lado Criacional/Estrutural da taxonomia
recém-apresentada — o mesmo mapa que classificou o Strategy (Aula 10)
como o primeiro representante Comportamental agora recebe seus
primeiros representantes Criacionais.

**Pré-requisitos:** Aula 10 (padrão Strategy — interface, injeção de
dependência, delegação, topologia Context/Strategy/ConcreteStrategy,
OCP); Aula 9 (Fail-Fast do construtor, invariantes, `equals()`/
`hashCode()`); Aula 2 (CQS, construtor como base de indução). O
dicionário de notações já traz Late Binding/VTable, `Pagavel`/`Pix`/
`Cartao`/`Boleto` (agora reaproveitados como Strategy), e o vocabulário
de acoplamento/coesão.

**Decisão de escopo (aula11 recebe vocabulário + Value Object + Builder
+ Factory Method; State Pattern fica para a Aula 12):** o material
combinado (vocabulário geral de padrões + quatro padrões densos: Value
Object, State, Builder, Factory Method) é claramente denso demais para
uma única aula de 90–140 min — seria preciso comprimir cada padrão a
ponto de perder as derivações principiadas que o `CLAUDE.md` exige
(anunciar premissas, desenvolver passo a passo). A divisão natural seg
ue exatamente a fronteira que o próprio esboço da disciplina já havia
sinalizado (`index.qmd`, Parte 4: "Padrões de Criação e Estruturais"
vs. "Padrões de Comportamento"): **Aula 11** cobre o vocabulário geral
(que não depende de nada ainda não visto) mais três padrões que giram
em torno da **gênese e da forma do objeto** — Value Object (imutabili-
dade como blindagem de dado), Builder e Factory Method (blindagem da
criação) —, todos de espírito Criacional/Estrutural; **Aula 12** cobre
o **State Pattern**, que é genuinamente Comportamental (mesma família
do Strategy já visto) e se apoia num contraste direto e deliberado com
o Strategy da Aula 10 (o próprio `.tex` da Aula 9 já convida a esse
contraste: "Embora possuam topologias estruturais [...] virtualmente
idênticas, os padrões Strategy e State resolvem intenções arquitetu-
rais completamente distintas"). Cortar exatamente no fim da seção de
Value Object e no início da seção de State Pattern (linha 353 do
`Aula 9.tex`) preserva um arco fechado nesta aula (vocabulário → dado
imutável → objeto que nasce validado) sem deixar nenhuma dependência
pendente: Builder e Factory Method não citam nem pressupõem State.

Com esse corte, a estimativa de carga horária desta aula fica em
~120–130 min (abertura ~10 + vocabulário ~23 + mutabilidade/aliasing
~15 + Value Object ~23 + Builder ~25 + Factory Method/DIP ~23 +
fechamento ~8), dentro da faixa 90–140 já calibrada. **Nada do trecho
usado nesta aula fica pendente** — o arco Vocabulário→Value
Object→Builder→Factory Method de `Aula 9.tex` (até a linha 353) e as
duas seções finais de `Aula 8.tex` estão totalmente cobertos aqui. O
que fica pendente para a **Aula 12**: o State Pattern completo
(`Aula 9.tex`, linhas 353–590) e a `\section{Conclusão}` de
`Aula 9.tex` (linhas 992–1005, que resume os "três pilares" incluindo
State — sua reafirmação cabe melhor no fechamento da Aula 12, quando o
terceiro pilar finalmente também tiver sido construído). `Aula 10.tex`
e `Revisão.tex` permanecem não lidos, reservados para depois da Aula
12.

**Estratégia Pedagógica:** Estratégia A (*Outside-In*) — cada um dos
três padrões novos (Value Object, Builder, Factory Method) é
apresentado a partir de um problema prático e "doloroso" já vivido
pelo aluno em código (o *aliasing* silencioso, o construtor telescó-
pico ilegível, o `new` espalhado que acopla o domínio à infraestrutura)
antes de nomear e formalizar a solução — o mesmo molde já usado com
sucesso nas Aulas 8–10 para Herança, LSP e Strategy. Não é uma aula de
fundamentação matemática/notacional (o que pediria Estratégia B); é uma
aula de "modelos" de solução recorrente (os próprios padrões de
projeto), cada um resolvendo um problema concreto de engenharia.

## Plano de aula — Aula 11 (carga horária estimada: ~127 min)

1. **Abertura: Revisão e Introdução** (~10 min) — revisão da Aula 10
   (Strategy como primeiro padrão nomeado: interface, injeção,
   delegação, OCP); ideia-ponte: o Strategy não foi um golpe de sorte —
   é um representante de uma família de 23 soluções catalogadas, cada
   uma batizada e documentada. Roteiro explícito (4 perguntas);
   problema motivador: "se Strategy resolveu o pagamento, quem resolve
   a criação seguraça de um `Pedido` complexo, ou a proteção de um
   valor monetário contra mutação por trás das costas?"

2. **O Vocabulário dos Padrões de Projeto** (~23 min) — a origem na
   arquitetura civil (Christopher Alexander, *A Pattern Language*, anos
   1970); o marco GoF de 1994 (Gamma/Helm/Johnson/Vlissides, 23
   padrões, os dois pilares técnicos Composição+Polimorfismo); o que um
   padrão **não** é (não é *framework* — quem chama o código é o
   framework, não o padrão; não é algoritmo estrutural — não ordena
   nem busca; não cura código procedural — pressupõe encapsulamento já
   estabelecido); a força oculta do vocabulário como linguagem ubíqua
   ("implemente um Strategy aqui" substitui um parágrafo inteiro de
   especificação); as três famílias (Comportamento/Estrutural/
   Criação), com o Strategy já classificado como o primeiro
   representante Comportamental visto; diagrama TikZ da taxonomia (a
   árvore GoF → 3 famílias → exemplos, com Strategy destacado).
   **Pausa ativa 1** (classificar um padrão hipotético em sua família
   pelo propósito, não pelo nome).

3. **O Problema da Mutabilidade e o Fenômeno de** *Aliasing* (~15 min)
   — por que mutabilidade é fonte de bugs (efeitos colaterais,
   acoplamento oculto via referências compartilhadas na Heap,
   dificuldade de rastreio, invariantes violadas); o exemplo do
   `Retangulo` (`r2 = r1` não copia, corrompe `r1` "pelas costas");
   diagrama TikZ da Heap mostrando duas referências na Stack apontando
   para o mesmo objeto mutável antes/depois da mutação; a Cópia
   Defensiva como paliativo caro (sobrecarrega o GC, polui o código).

4. **O Padrão Value Object** (~23 min) — a distinção Entidade
   (identidade persistente, ex.: `Aluno`/RA, naturalmente mutável) vs.
   Value Object (identidade por atributo, imutabilidade absoluta,
   substituibilidade via `equals()` por valor); operacionalizando a
   imutabilidade (campos `final`, classe `final`, ausência de
   *setters*, defesa na cópia de referências mutáveis internas);
   `Dinheiro` como VO completo (construtor Fail-Fast + `equals()`);
   como a imutabilidade neutraliza o *aliasing* do bloco anterior
   (compartilhar deixa de ser perigo); a Obsessão por Primitivos como
   antipadrão gêmeo (`double`/`String` para conceitos de domínio —
   Anemia Semântica, erro de compilação virando erro de runtime);
   benefícios arquiteturais (thread-safety inerente, raciocínio local,
   Flyweight). **Pausa ativa 2** (Entidade vs. VO e o que muda na
   igualdade).

5. **Criação Segura: o Problema do Construtor Sujo e o Padrão Builder**
   (~25 min) — revisão rápida de Fail-Fast no construtor (Aula 2);
   o "Construtor Sujo" (lista longa de parâmetros do mesmo tipo,
   objeto que nasce "mancando" via *setters* pós-construção, `new`
   espalhado acoplando negócio a infraestrutura); o padrão Builder
   como objeto intermediário mutável que acumula estado e só produz o
   objeto final imutável no `build()`; a interface fluente (`return
   this`, encadeamento legível); `build()` como "juiz" da validação
   *cross-field* (desconto > total); a blindagem do construtor privado
   de `Pedido`, só acessível pelo `PedidoBuilder`; diagrama TikZ do
   fluxo passo a passo (Builder acumulando campos → `build()` valida →
   `Pedido` imutável nasce pronto).

6. **Factory Method e a Inversão de Dependência na Criação** (~23 min)
   — o problema da dependência direta (o cliente não deveria precisar
   saber qual classe concreta instanciar); a Factory Method como
   interface de criação que decide a classe concreta e devolve sempre
   a abstração (`NotificacaoFactory`/`Notificacao`, adaptado para o
   fio condutor do e-commerce como notificações de status de pedido —
   Email/SMS); os três benefícios (ponto único de manutenção,
   encapsulamento de parâmetros de infraestrutura, polimorfismo real);
   o `new` como "a cola mais forte do código" e a Inversão de
   Dependência (DIP) na criação — um serviço de alto nível que só
   conhece a abstração `Repositorio`, recebendo uma fábrica abstrata em
   vez de instanciar diretamente uma implementação concreta.
   **Pausa ativa 3** (Factory Method vs. acoplamento direto).

7. **Fechamento** (~8 min) — retomar as 4 perguntas da abertura; ponte
   para a Aula 12: o terceiro pilar da "Aula do Tríptico" original
   (Gênese segura, hoje coberta; Dado protegido, hoje coberto; Fluxo
   sem `if` algemado, ainda pendente) — o State Pattern, contrastado
   deliberadamente com o Strategy já dominado.

## Fontes usadas — Aula 11

### Fonte 1: `Teoria/Aula 8.tex`, linhas 808–813 e 883 (o que é um Padrão de Projeto)

**Uso pretendido:** abrir o Bloco 2, definindo com precisão o que é um
padrão antes de contrastar com o que não é.

**Trecho:**
> "Definição Formal: Padrões de Projeto (Design Patterns) são soluções
> arquiteturais testadas e documentadas para problemas recorrentes no
> design de software orientado a objetos. A Natureza do Padrão: Eles
> não são bibliotecas de código ou trechos prontos para copiar e
> colar. São gabaritos, templates conceituais que orientam como
> resolver uma classe de problemas."

---

### Fonte 2: `Teoria/Aula 8.tex`, linhas 816–830 e 885–889 (a origem em Christopher Alexander e o marco GoF)

**Uso pretendido:** contar a origem histórica dos padrões e o marco
zero de 1994.

**Trecho:**
> "A Inspiração de Christopher Alexander: Nos anos 1970, o arquiteto
> civil Christopher Alexander publicou 'A Pattern Language', catalogando
> padrões urbanos e arquitetônicos [...] O Marco Zero (1994): Quatro
> autores (Gamma, Helm, Johnson e Vlissides) publicaram o livro seminal
> 'Design Patterns: Elements of Reusable Object-Oriented Software'.
> [...] a esmagadora maioria desses 23 padrões é construída utilizando
> duas mecânicas fundamentais que acabamos de estudar: a Composição e o
> Polimorfismo."

---

### Fonte 3: `Teoria/Aula 8.tex`, linhas 832–837 (o que os padrões NÃO são)

**Uso pretendido:** delimitar o conceito antes de aplicá-lo, evitando o
erro comum de tratar padrão como biblioteca ou algoritmo.

**Trecho:**
> "Não são Frameworks: Um framework (como Spring ou React) chama o seu
> código. O Padrão de Projeto é uma organização que você dá ao seu
> próprio código. Não são Algoritmos Estruturais: Eles não resolvem
> problemas de ordenação, criptografia ou busca [...] Eles resolvem
> problemas de acoplamento e coesão. Não curam Código Procedural: [...]
> Aplicar um padrão em um sistema de variáveis globais e funções
> estruturadas apenas mascara o problema."

---

### Fonte 4: `Teoria/Aula 8.tex`, linhas 840–845 e 902 (o vocabulário arquitetural)

**Uso pretendido:** justificar por que vale a pena aprender o
vocabulário mesmo antes de dominar cada padrão em profundidade.

**Trecho:**
> "Densidade de Comunicação: O maior benefício prático dos Padrões de
> Projeto no mercado não é apenas a estrutura, mas a linguagem ubíqua
> que eles fornecem. [...] em vez de um engenheiro sênior dizer: 'Crie
> uma interface comum para essas variações, isole a execução e injete
> a instância no construtor do orquestrador', ele apenas diz:
> 'Implemente um Strategy aqui.'"

---

### Fonte 5: `Teoria/Aula 8.tex`, linhas 848–880 e 906–912 (as três famílias)

**Uso pretendido:** núcleo do Bloco 2 — a taxonomia que organiza os 23
padrões, com o Strategy já classificado.

**Trecho:**
> "Padrões de Comportamento: O foco é a comunicação. Como os objetos
> interagem e distribuem obrigações no tempo. [...] Padrões
> Estruturais: O foco é a topologia. Como objetos e classes podem ser
> compostos para formar estruturas maiores e flexíveis. [...] Padrões
> de Criação: O foco é a gênese. Como isolar a complexidade do operador
> new e gerenciar o ciclo de vida na Heap."

**Trecho — Padrões de Criação, o gancho para esta aula:**
> "O Paradoxo da Criação: Vimos que garantir o 'Fail-Fast' e preservar
> as Invariantes é vital. Mas quem é responsável por executar essa
> lógica de validação complexa? [...] O Objetivo Creacional: Centralizar
> e encapsular a lógica de instanciação. O sistema pede um objeto e a
> fábrica entrega ele pronto e validado. (Ex: Factory Method, Builder,
> Singleton)."

---

### Fonte 6: `Teoria/Aula 9.tex`, linhas 46–50 e 54 (o problema da mutabilidade)

**Uso pretendido:** abrir o Bloco 3, motivando por que a mutabilidade
descontrolada é perigosa antes de nomear o Value Object.

**Trecho:**
> "Efeitos Colaterais: Como a alteração de um atributo em um ponto
> isolado reverbera em comportamentos inesperados em outras partes do
> sistema. O Acoplamento Oculto: Objetos que compartilham referências
> para o mesmo dado mutável na Heap. [...] Invariantes Violadas: O
> risco de um objeto entrar em um estado logicamente inválido durante
> sua execução."

**Trecho — aliasing bug:**
> "Se dois objetos, A e B, possuem uma referência para o mesmo objeto
> C, e A altera o estado de C, B pode falhar ao assumir que C ainda
> possui os valores originais. Esse fenômeno, conhecido como aliasing
> bug, é particularmente perigoso em sistemas multithread."

---

### Fonte 7: `Teoria/Aula 9.tex`, linhas 57–62 (o perigo da mutação na Heap)

**Uso pretendido:** o exemplo concreto do `Retangulo`/aliasing que
ancora o diagrama de memória do Bloco 3.

**Trecho:**
> "Referências Partilhadas: Múltiplos ponteiros na Stack apontando para
> o mesmo endereço de memória na Heap. Efeito Colateral Silencioso: Uma
> alteração feita através da referência A corrompe a lógica de quem
> utiliza a referência B, sem qualquer aviso do compilador."

---

### Fonte 8: `Teoria/Aula 9.tex`, linhas 91–95 e 138–142 (Entidade vs. Value Object)

**Uso pretendido:** núcleo do Bloco 4 — a distinção conceitual central
do Value Object.

**Trecho — Entidade:**
> "Identidade Persistente: Definida por um identificador único (ID,
> CPF, RA) que não muda, independentemente das alterações nos
> atributos. [...] Igualdade por ID: Dois objetos são a mesma entidade
> se possuírem o mesmo ID, mesmo que todos os outros campos sejam
> diferentes."

**Trecho — Value Object:**
> "Identidade por Atributo: Não possui ID. O objeto é o conjunto dos
> seus valores. Se um valor muda, o objeto deixa de existir e surge um
> novo. Imutabilidade Absoluta: Uma vez criado, o seu estado nunca
> muda. [...] Substituibilidade: Dois VOs são considerados iguais se o
> seu conteúdo for idêntico (equals() baseado em campos)."

---

### Fonte 9: `Teoria/Aula 9.tex`, linhas 189–192 e 209 (operacionalizando a imutabilidade)

**Uso pretendido:** as regras práticas de implementação de um VO em
Java.

**Trecho:**
> "Campos final: Garantia de que a referência ou o valor primitivo não
> será reatribuído após o construtor. Ausência de Setters: O objeto é
> uma 'caixa preta' inalterável após sua gênese. Defesa na Cópia: Se o
> VO contém referências a objetos mutáveis [...], deve-se cloná-los no
> construtor e no retorno."

**Trecho — article:**
> "Não basta apenas marcar os campos como final; é preciso garantir que
> a classe seja final (para evitar que subclasses adicionem estado
> mutável) e que nenhum objeto interno mutável 'vaze' para fora da
> classe."

---

### Fonte 10: `Teoria/Aula 9.tex`, linhas 264–269 e 281 (Obsessão por Primitivos)

**Uso pretendido:** o antipadrão gêmeo do Value Object, fechando o
Bloco 4.

**Trecho:**
> "A Fragilidade: Confiar em double, int ou String para conceitos de
> domínio (Dinheiro, CPF, Email). Anemia Semântica: O tipo diz como o
> dado é guardado na memória, mas não o que ele significa para o
> negócio. O Risco: O compilador aceita qualquer valor. Um int de idade
> aceita -500 ou 2.000.000.000."

**Trecho — article:**
> "O seu código deixa de ser 'Stringly Typed' (tipado por strings) para
> ser verdadeiramente orientado a objetos."

---

### Fonte 11: `Teoria/Aula 9.tex`, linhas 628–631 e 640 (o Construtor Sujo)

**Uso pretendido:** abrir o Bloco 5, motivando o Builder a partir de um
problema concreto de legibilidade e segurança na instanciação.

**Trecho:**
> "Lista de Parâmetros Longa: Dificuldade em distinguir a ordem de
> múltiplos argumentos do mesmo tipo [...] Estado Inconsistente: O
> perigo de instanciar um objeto e só depois configurar os seus campos
> via setters (o objeto nasce 'mancando'). Acoplamento Rígido: O uso do
> new espalhado pelo código vincula a lógica de negócio a
> implementações concretas."

---

### Fonte 12: `Teoria/Aula 9.tex`, linhas 653–658, 668–671 e 703–706 (o padrão Builder)

**Uso pretendido:** núcleo do Bloco 5 — mecânica do Builder e da
interface fluente.

**Trecho:**
> "Separação de Responsabilidades: A lógica de como construir é isolada
> da classe do objeto final. [...] Padrão Builder introduz um objeto
> intermediário (o construtor) que acumula os dados necessários e,
> apenas no final, produz a instância do objeto alvo."

**Trecho — interface fluente:**
> "Legibilidade: O uso de métodos encadeados que se assemelham a uma
> frase. Imutabilidade: O Builder é mutável, mas o objeto que ele
> entrega no final (.build()) é estritamente imutável. Validação Final:
> O método build() é o local ideal para verificar se a combinação de
> parâmetros fornecida é logicamente consistente."

**Trecho — mecânica do encadeamento:**
> "Cada método de configuração retorna a própria instância do Builder
> (return this). O estado é acumulado temporariamente no Builder. O
> objeto final só nasce no build()."

---

### Fonte 13: `Teoria/Aula 9.tex`, linhas 738 e 814 (o construtor privado como blindagem)

**Uso pretendido:** fechar o Bloco 5 mostrando como o Builder impede
objetos "meio prontos".

**Trecho:**
> "Note que o construtor de Pedido é privado, forçando o uso do Builder
> e garantindo que nenhum objeto 'meio pronto' ou inválido seja
> instanciado na Heap. [...] a classe Pedido torna-se extremamente
> limpa, focada apenas em armazenar os dados finais de forma imutável,
> enquanto toda a 'sujeira' da lógica de construção fica confinada ao
> Builder."

---

### Fonte 14: `Teoria/Aula 9.tex`, linhas 822–825 e 834 (Factory Method)

**Uso pretendido:** abrir o Bloco 6, motivando a fábrica a partir do
problema de dependência direta de classes concretas.

**Trecho:**
> "O Problema da Dependência: O cliente não deve precisar de saber qual
> classe concreta instanciar. Interface de Criação: Define um método
> para criar um objeto, mas deixa as subclasses decidirem qual classe
> instanciar."

**Trecho — article:**
> "O Factory Method é sobre adiar a decisão de qual classe concreta
> utilizar. Imagine um sistema de logística: o código principal pede um
> 'Transporte'. [...] O código cliente trata ambos apenas como a
> interface Transporte, ignorando os detalhes de criação."

---

### Fonte 15: `Teoria/Aula 9.tex`, linhas 880–883 (os três benefícios da Factory)

**Uso pretendido:** consolidar por que centralizar a criação compensa,
antes de conectar com DIP.

**Trecho:**
> "Ponto Único de Manutenção: Se amanhã o sistema passar a suportar
> notificações via WhatsApp, alteramos apenas a Factory, e não os 50
> locais onde notificações são enviadas. Encapsulamento de Parâmetros:
> [...] Polimorfismo Real: O código cliente torna-se agnóstico à
> implementação."

---

### Fonte 16: `Teoria/Aula 9.tex`, linhas 925–926 e 960 (DIP na criação)

**Uso pretendido:** fechar o Bloco 6 conectando Factory Method à
Inversão de Dependência.

**Trecho:**
> "O Problema: O new é a 'cola' mais forte do código. Se você
> instancia, você depende da implementação. Fronteiras: Módulos de alto
> nível não devem saber como objetos de baixo nível nascem."

**Trecho — article:**
> "Quando um módulo de alto nível (como um serviço de negócio) utiliza
> o operador new, ele está a violar a fronteira arquitetural ao assumir
> a responsabilidade de conhecer uma implementação concreta de baixo
> nível."

---

**Nota sobre reaproveitamento/adaptação de nomes:** o exemplo de
Factory Method do `.tex` usa `NotificacaoFactory`/`Notificacao`
(SMS/Email) e, separadamente, `Servico`/`Database`/`DBFactory` para
DIP — ambos genéricos, sem ligação ao fio condutor de e-commerce já
maduro nas Aulas 8–10. Esta aula adapta os nomes ao domínio já
estabelecido (`Pedido`, notificações de status de pedido) mantendo a
mecânica do `.tex` inalterada — mesma decisão já tomada na Aula 10 ao
reaproveitar `Pagavel`/`Pix`/`Cartao`/`Boleto`. O Value Object usa
`Dinheiro` diretamente do `.tex` (já encaixa naturalmente no domínio:
o total de um `Pedido`). O Builder usa `PedidoBuilder`/`Pedido`
diretamente do `.tex`, sem nenhuma adaptação — o próprio material de
origem já usa o domínio do curso aqui.

**Questões de fixação do próprio `Aula 9.tex` (linhas 1013–1173):** o
`\section*{Exercícios de Fixação}` do `.tex` contém 25 blocos de V/F
(formato `( )`, três itens cada) e 15 discursivas — majoritariamente
definicionais ("X é caracterizado por..."), formato que o `CLAUDE.md`
desta disciplina proíbe para os exercícios publicados. Servem aqui só
de inventário temático (todos os temas de Value Object, Builder e
Factory Method já cobertos nos blocos 3–6 acima); nenhum item será
reaproveitado verbatim — os 6 a 10 blocos de V/F desta aula serão
originais, nascidos das 4 heurísticas exigidas.
