## Resumo — Aula 5

Esta aula não introduz nenhum modelo novo: é uma aula de **revisão
integrada** das Aulas 1–4, pedida explicitamente pelo professor com foco
nos conceitos de probabilidade que atravessam todas elas, não nos
algoritmos em si. A tese que a aula existe para deixar explícita: Beta +
limiar (Aula 1), Naive Bayes + teoria da decisão (Aula 2), árvores CART
(Aula 3) e validação cruzada/Bootstrap (Aula 4) parecem quatro técnicas
distintas, mas são quatro instâncias da mesma estrutura de três peças —
uma **distribuição** assumida sobre os dados, uma **verossimilhança**
usada para ajustá-la, e uma **decisão** fundamentada num risco (esperado
ou estimado). A aula usa um único fio condutor novo — o dataset real
*Pima Indians Diabetes* — atravessando as quatro lentes em sequência, com
chamadas explícitas de volta aos números e exemplos concretos que cada
aula original usou (Beta(2,5)/Beta(6,3) sintéticos e a triagem médica de
23% na Aula 1; a correlação 0,64/0,22 do Breast Cancer Wisconsin na Aula
2; a árvore de 5 folhas do California Housing e o contraexemplo
Gini/entropia na Aula 3; os números 92,98%/92,97%±2,43%/91,8%/90,1% da
validação cruzada e do Bootstrap na Aula 4).

**Pré-requisitos:** Aulas 1–4 completas e aprovadas (teoria da decisão
bayesiana, Naive Bayes, CART/impureza, validação cruzada e Bootstrap).
Nenhum conteúdo novo é assumido além do que essas quatro aulas já
cobriram.

**Dataset-fio novo:** *Pima Indians Diabetes*
(`khoaguin/pima-indians-diabetes-database`, Hugging Face Hub, 768
pacientes, alvo binário `y`), recomendado pelo `CLAUDE.md` da disciplina
e ainda não usado nas Aulas 1–4 (que usaram, respectivamente: dados
sintéticos Beta; Breast Cancer Wisconsin; California Housing; Breast
Cancer Wisconsin de novo). Como as quatro aulas originais não convergem
num único dataset real, esta revisão constrói **um** exemplo novo e
comum às quatro lentes (Glicose 1D → Beta/limiar; Glicose+IMC →
Naive Bayes; mesma dupla → árvore; a árvore resultante → CV/Bootstrap),
sinalizando com clareza, a cada bloco, onde o resultado de hoje
**generaliza** o que a aula original mostrou (ex.: razão de prioris
65/35 real, bem menos extrema que os 95/5 sintéticos da Aula 1) e onde é
genuinamente a mesma conta, só que com dado real no lugar do sintético.

**Estratégia Pedagógica:** Estratégia B (Inside-Out com Problema-Fio) —
esta é uma aula de fundamentação/linguagem (revisão do vocabulário
probabilístico comum às quatro aulas anteriores), não a apresentação de
um modelo novo; a lógica de exposição segue o problema-fio (Pima Indians
Diabetes) atravessando mecanismo → diagnóstico teórico → ponte, em vez de
abrir com um modelo mental "catchy" de um algoritmo específico.

## Plano de aula — Aula 5 (carga horária estimada: ~100min)

1. **Abertura — Amarrando os Quatro Fios** (~8 min) — Organizador prévio
   que retoma a promessa de fechamento da Aula 4 (a próxima aula seria
   regressão linear como MLE) e explica por que esta aula de revisão se
   insere antes dela. Roteiro explícito em 5 perguntas: (i) o que as
   quatro aulas tinham em comum por trás da fachada de "algoritmos
   diferentes"; (ii) como a mesma pergunta ("qual é o formato dos
   dados?") aparece disfarçada em Beta, Naive Bayes e árvore; (iii) por
   que "maximizar verossimilhança" e "minimizar impureza/erro" são,
   estruturalmente, a mesma operação; (iv) por que nunca observamos o
   risco de verdade, só o estimamos, e o que a Aula 4 fez sobre isso; (v)
   que peça ainda falta completar o quadro. Problema motivador: apresentar
   o Pima Indians Diabetes como o fio que vai atravessar as quatro
   lentes.

2. **Bloco 1 — Distribuição e Decisão (revisão da Aula 1)** (~13 min) —
   Recall dos números sintéticos de Aula 1 (Beta(2,5)/Beta(6,3), prioris
   95/5, o "corte no cruzamento das condicionais está errado", a triagem
   médica de 23%). Pivô: ajustar Beta à Glicose real do Pima (por classe
   diabético/não-diabético), comparar o cruzamento das condicionais com o
   cruzamento das conjuntas usando as prioris reais (~65/35), e mostrar
   que o princípio geométrico é idêntico ainda que o ganho absoluto seja
   mais modesto que no experimento controlado de Aula 1. Termina em
   Pausa Ativa 1.

3. **Bloco 2 — Independência e Teoria da Decisão (revisão da Aula 2)**
   (~15 min) — Recall do Naive Bayes e da teoria da decisão geral de
   Aula 2 (fatoração por independência condicional, correlação
   intra-classe 0,64/0,22 no Breast Cancer Wisconsin, ρ(a|x), risco de
   Bayes). Pivô: acrescentar IMC à Glicose no Pima, comparar Gaussiana de
   covariância plena vs. diagonal (Naive Bayes), e mostrar que aqui a
   correlação intra-classe é bem mais baixa — o preço da suposição de
   independência é quase nulo, ao contrário do Breast Cancer Wisconsin —
   evidenciando que esse preço é uma propriedade dos *dados*, não do
   método. Termina em Pausa Ativa 2.

4. **Bloco 3 — Partição Gulosa e Verossimilhança Categórica (revisão da
   Aula 3)** (~15 min) — Recall do argumento "reduzir impureza = MLE
   categórica" e da árvore de 5 folhas do California Housing em Aula 3.
   Pivô: crescer uma árvore pequena (4 folhas) de classificação em
   Glicose+IMC no Pima, percorrer a redução de entropia/Gini do primeiro
   split explicitamente, e contrastar a fronteira axis-aligned da árvore
   com a fronteira Gaussiana (elipses) do Bloco 2 sobre os mesmos dois
   atributos. Termina em Pausa Ativa 3.

5. **Bloco 4 — Estimando o Risco que Nunca Observamos (revisão da Aula
   4)** (~15 min) — Recall dos números de CV/Bootstrap de Aula 4 no
   Breast Cancer Wisconsin (92,98% pico de teste, 92,97%±2,43% de CV,
   empate 4 folhas/19 folhas em 91,8%, regra de 1 desvio-padrão). Pivô:
   avaliar honestamente a árvore do Bloco 3 via CV de 5 folds e Bootstrap
   (duas aplicações: reamostrar o teste vs. reamostrar+reajustar o
   treino), mostrando que a acurácia de um único split (75,2%) cai perto
   do topo da faixa revelada pela CV — o mesmo lembrete de Aula 4 sobre
   não confiar num único número. Termina em Pausa Ativa 4.

6. **Bloco 5 — Síntese: as Quatro Peças, Uma Estrutura** (~12 min) —
   Diagrama TikZ unificador (Distribuição → Verossimilhança →
   Decisão/Risco, com uma linha por aula) e tabela-síntese comparando as
   quatro aulas nessas três colunas. Ponto meta-explícito: sinalizar os
   dois casos de reuso notacional que podem confundir ($k$ como índice de
   classe em Aulas 1–3 vs. número de *folds* em Aula 4; $\lambda$/custo
   como multiplicador de custo em Aula 1 vs. penalidade de
   custo-complexidade em Aulas 3–4) — honestidade de notação, não um erro
   a esconder. Termina em Pausa Ativa 5 (nível síntese, atravessando as
   quatro aulas de uma vez).

7. **Fechamento e ponte** (~7 min) — Retomar as 5 perguntas do roteiro,
   respondendo cada uma em uma frase. Nomear o que ficou em aberto: toda
   verossimilhança maximizada hoje era sobre densidades/frequências
   categóricas ou tabulares; ainda não vimos o que muda quando o alvo é
   contínuo e a relação é linear. Ponte para a Aula 6 (Regressão Linear e
   Máxima Verossimilhança): mínimos quadrados como MLE sob ruído
   gaussiano — o mesmo princípio unificador desta aula, agora aplicado a
   um modelo paramétrico contínuo em vez de uma densidade/árvore/esquema
   de reamostragem.

### Nota de dados

Nenhuma fonte bibliográfica nova é citada nesta aula — é uma síntese do
que já foi ensinado e aprovado nas Aulas 1–4, não uma aula baseada em
literatura externa nova. Por isso, a etapa de `_01-fontes.md` (citação
literal de fonte) foi explicitamente dispensada pelo professor para esta
aula. O dataset novo (*Pima Indians Diabetes*) é usado só como fio
condutor experimental comum às quatro lentes revisadas, não como fonte
teórica.
