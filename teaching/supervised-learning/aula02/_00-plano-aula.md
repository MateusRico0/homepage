## Resumo — Aula 2: Distribuições Condicionais e Modelos Generativos

*(Aula 2 começou do zero nesta rodada — o `02-aula.qmd` anterior foi
descartado a pedido do usuário; recuperável do histórico do git, commit
`a66e239`, se algum dia necessário.)*

### Posição no curso

A Aula 1 fechou com uma pergunta em aberto: a receita de classificar por
densidades ponderadas pela priori funciona em alta dimensão, só trocando $x$
por $\mathbf{x}$? A Aula 2 responde que a regra continua válida, mas o objeto
do qual ela depende — a densidade condicional de classe em $\mathbb{R}^d$ —
deixa de ser estimável sem uma suposição estrutural. Naive Bayes é essa
suposição: independência condicional entre atributos dado a classe. A aula
também retoma teoria da decisão (introduzida de forma ad-hoc na Aula 1, só
para duas classes com perda 0-1 e um custo escalar) e a formaliza como
ferramenta geral — função de perda, risco posterior, risco de Bayes — que
recupera tudo que já foi usado como caso particular.

### Pré-requisitos

Aula 1 completa (densidades condicionais por classe, regra do posterior
máximo, teorema de Bayes em uma dimensão, teoria da decisão binária informal
com matriz de perda $2\times2$, ROC e matriz de confusão). Álgebra linear
básica (produto interno, autovalores/autovetores de matrizes simétricas, para
covariância compartilhada vs. diagonal no Bloco 4). Probabilidade
multivariada elementar.

### Objetivos de aprendizagem

- **ML Concept:** Multidimensional classification under the assumption of feature independence (Naive Bayes).
- **Statistical Concept:** Bayes' theorem decomposto em priori/verossimilhança/posteriori; distinção conjunta vs. condicional; independência condicional como simplificação deliberada para mitigar a maldição da dimensionalidade.
- **Objectives:** Entender a abordagem generativa à classificação e o custo-benefício da suposição de independência em alta dimensão.
- **Expected Competencies:** Derivar o classificador Naive Bayes a partir do Teorema de Bayes; explicar quando a suposição de independência degrada — ou não — o desempenho preditivo.

*(fonte dos objetivos: `../index.md`, Lesson 2 — planejamento fixo do
semestre)*

### Estratégia Pedagógica

**Estratégia A (Outside-In)** — Naive Bayes é um modelo/algoritmo
concreto (mesma categoria de K-Means/Árvores citada em
`../../CLAUDE.md`), não um idioma matemático de fundação. A aula abre
de fato com um "Modelo Mental/Catchy" — a demonstração generativa
("jogue fora os dados": ajusta por MLE, descarta os 900 pontos
originais, regenera dados novos só com os parâmetros ajustados) — antes
de a maldição da dimensionalidade aparecer como a "Necessidade
Teórica" que motiva a suposição de independência do Naive Bayes, que
então é formalizada, com síntese/limitações (o preço da suposição) ao
final. **Adicionado nesta revisão (2026-08-26)** para conformidade com
a nova política de `../../CLAUDE.md`; sem mudança de conteúdo no
`index.qmd`.

### Compromissos herdados da Aula 1 (já aprovada)

A ponte de fechamento da Aula 1 promete três coisas que travam a abertura
desta aula:

1. Abrir com a maldição da dimensionalidade ($M^d$ células, inestimável sem
   estrutura).
2. Apresentar Naive Bayes como a suposição estrutural:
   $p(\mathbf{x}\mid\mathcal{C}_k) = \prod_i p(x_i\mid\mathcal{C}_k)$.
3. Cobrir o preço da suposição — quando é inofensiva, quando é desastrosa,
   por que classifica bem mesmo com probabilidades ruins — e formalizar a
   razão de verossimilhanças no caso multidimensional.

## Plano de aula — Aula 2 (carga horária: ~130min)

**Aviso de conta (atualizado após escrever `02-aula.qmd`).** Com o Bloco 1
encurtado e os antigos Blocos 5+6 fundidos (o usuário notou que os dois
cobriam o mesmo objeto sob duas formas: razão de verossimilhanças e regra
de Bayes), a estimativa antes de escrever era ~105 min. Na escrita real, o
Bloco 5 fundido saiu mais longo do que os ~38 min estimados (a formalização
completa de teoria da decisão, com a ressalva ligando ao Bloco 4, precisou
de mais espaço) — o total final ficou em **~130 min**, igual à Aula 1.
**Aprovado pelo usuário** aceitar aulas mais longas em vez de cortar mais.

### Bloco 0 — Abertura (5 min)

Recapitular a pergunta que fechou a Aula 1: "a receita funciona em alta
dimensão? É só trocar $x$ por $\mathbf{x}$?" — sem responder ainda.

### Bloco 1 — A maldição da dimensionalidade (10 min, encurtado)

Por que estimar $p(\mathbf{x}\mid\mathcal{C}_k)$ sem estrutura é inviável:
histograma com $M$ células por eixo exige $M^d$ células — a promessa exata
que a Aula 1 fez. Uma figura, uma conta, sem se demorar: é motivação para o
resto da aula, não o assunto dela.

### Bloco 2 — Bayes formal para $K$ classes (10 min)

Extensão direta do que já foi construído na Aula 1 (soma/produto/Bayes) para
$K>2$ classes — não rederivar do zero, só generalizar a notação:
$p(\mathcal{C}_k\mid\mathbf{x}) \propto p(\mathbf{x}\mid\mathcal{C}_k)\,\pi_k$.

### Bloco 3 — Naive Bayes: a suposição estrutural (15 min)

$p(\mathbf{x}\mid\mathcal{C}_k) = \prod_i p(x_i\mid\mathcal{C}_k)$ — a
promessa da Aula 1. Torna o problema linear em $d$ em vez de exponencial.
Exemplo motivador: **spam**, $\mathbf{x}\in\{0,1\}^d$ (presença/ausência de
palavras de vocabulário) — clássico de Naive Bayes, e já citado na ponte da
Aula 1.

### Bloco 4 — O preço da suposição (22 min)

O bloco mais importante pedagogicamente: geometria de covariância
compartilhada vs. diagonal (Naive Bayes = fronteira que ignora correlação
entre atributos); mostrar com atributos correlacionados que a fronteira de
decisão pode continuar boa mesmo com densidades condicionais erradas —
"classifica bem, estima mal" (Domingos & Pazzani — citado na Aula 1 como
leitura complementar, usado de fato aqui).

### Bloco 5 — Teoria da decisão geral, e quando ela é linear em $\mathbf{x}$ (38 min, fusão dos antigos Blocos 5+6)

O usuário notou, revisando o rascunho, que "razão de verossimilhanças
multidimensional" e "teoria da decisão para $K$ classes" são o mesmo objeto
visto de duas formas — exatamente como a Aula 1 percebeu que matriz de
confusão e ROC eram o mesmo sweep replotado. Fundidos numa sequência só:

1.  **O objeto geral.** Espaço de decisões $\mathcal{A}$ (não precisa
    coincidir com o espaço de classes — a opção de rejeição já é o primeiro
    exemplo de $\mathcal{A} \neq \mathcal{Y}$), função de perda
    $L: \mathcal{Y}\times\mathcal{A} \to \mathbb{R}$, regra de decisão
    $\delta(\mathbf{x}) \in \mathcal{A}$. Risco posterior
    $\rho(a\mid\mathbf{x}) = \sum_k L(k,a)\,p(\mathcal{C}_k\mid\mathbf{x})$;
    regra de Bayes $\delta^\star(\mathbf{x}) = \arg\min_a \rho(a\mid\mathbf{x})$
    — o nome formal do que a Aula 1 já fez informalmente para $K=2$.
2.  **O caso binário recupera exatamente a razão de verossimilhanças da
    Aula 1.** Perda 0-1 vs. matriz $2\times2$: a regra de Bayes se escreve
    como um teste $p(\mathbf{x}\mid\mathcal{C}_B)/p(\mathbf{x}\mid\mathcal{C}_A)
    \gtrless$ limiar, onde o limiar depende só de custo e priori — nunca de
    $\mathbf{x}$. Esta é a ponte: toda regra de decisão binária *é* um teste
    de razão de verossimilhanças contra um limiar.
3.  **Pergunta que emerge naturalmente daqui — antigo Bloco 5:** sob que
    suposições sobre $p(\mathbf{x}\mid\mathcal{C}_k)$ esse log-razão é
    **linear** em $\mathbf{x}$? Duas respostas que o curso já preparou,
    lado a lado: (a) Gaussianas com covariância $\Sigma$ **compartilhada**
    entre classes (os termos quadráticos cancelam — liga direto ao Bloco 4);
    (b) Naive Bayes com atributos **binários** (cada log da razão
    condicional soma linearmente). Ligação com a Aula 6 (regressão
    logística), que vai construir esse mesmo discriminante linear por outro
    caminho.
4.  **Generalização para $K$ classes e matriz de perda $K\times K$;** opção
    de rejeição como $\mathcal{A} = \mathcal{Y}\cup\{\text{recusar}\}$ com
    perda $\lambda$.
5.  **Risco de Bayes** $R^\star = \mathbb{E}_X[\min_a \rho(a\mid X)]$ —
    generaliza o erro de Bayes da Aula 1 para perda arbitrária. Nenhuma
    regra de decisão faz melhor, *dado o modelo verdadeiro*.
6.  **A ressalva que fecha o loop com o Bloco 4:** a regra de Bayes é ótima
    **se** a posteriori estiver certa. O Bloco 4 mostrou Naive Bayes
    estimando posteriori errado e ainda classificando bem sob perda 0-1 —
    teoria da decisão dá a regra ótima *dado* o modelo; não protege contra
    erro de modelo.

### Bloco 6 — Fechamento e ponte (5 min)

Naive Bayes funciona bem e é barato, mas a fronteira ainda é limitada pela
suposição; ponte para a Aula 3 (árvores, que não impõem essa suposição e
particionam o espaço de outro jeito).
