# Respostas das Pausas Ativas — Aula 4

> Arquivo de apoio, não publicado (prefixo `_`). Discute as perguntas
> motivadoras das pausas ativas do `index.qmd` e dá a solução dos
> respectivos V/F. O `index.qmd` publicado só contém a pergunta em
> cada pausa ativa, nunca a resolução (mesmo padrão já estabelecido em
> `aula02`).
>
> (Os 12 blocos de V/F da seção Exercícios do `index.qmd` não são
> discutidos aqui — ficam para o aluno resolver por conta, com
> justificativa disponível só ao professor em `_02-solucoes.md`.)

## 1. O Viés do Erro de Treino

**Pergunta motivadora:** Se a árvore de profundidade 15 tem a mesma
acurácia de teste da árvore de profundidade 6, por que ainda
preferimos uma árvore mais rasa?

A resposta não é estatística no sentido de "generaliza melhor" — as
duas empatam no teste. É uma resposta de **parcimônia e robustez**: a
árvore mais rasa chegou ao mesmo resultado com menos capacidade de
memorizar ruído específico da amostra de treino, então há menos risco
de que o empate observado seja coincidência desta amostra em
particular; ela também é mais simples de auditar e mais estável a
pequenas mudanças nos dados. O ponto pedagógico central: acurácia de
treino alta (ou empatada) nunca é evidência de generalização — só a
acurácia medida em dados não usados no ajuste conta essa história.

- ✔ É o extremo de memorização total: treino perfeito, sem qualquer garantia sobre o teste.
- ✗ Acurácia de TREINO igual nada diz sobre generalização; é preciso olhar o desempenho no teste.
- ✔ Mesma assinatura do overfitting desta aula, num domínio diferente.
- ✗ No nosso experimento, o teste sobe até a profundidade 5 e depois só estagna, não piora sempre.

## 2. O Pecado de Espiar o Teste

**Pergunta motivadora:** Um colega ajusta hiperparâmetros usando só a
validação, mas de vez em quando "espia rapidinho" o teste para decidir
se vale a pena continuar tentando profundidades maiores. Ele nunca
usou o teste para *ajustar* nada — o que exatamente ele perdeu ao
fazer isso?

O que se perde não é um parâmetro do modelo (nenhum peso foi tocado),
e sim o **significado estatístico do número final**. Cada consulta ao
teste, mesmo só para "decidir se vale a pena continuar", é uma decisão
humana informada por aquele número — e decisões repetidas guiadas pelo
mesmo conjunto finito de pontos tendem a convergir para o que funciona
bem *nesses pontos específicos*, não necessariamente na população. O
teste deixa de significar "desempenho nunca visto" e passa a
significar "desempenho depois de várias rodadas de ajuste indireto
guiado por ele" — a mesma lógica de vazamento do bloco de Armadilhas,
só que pela porta humana em vez da porta do código.

- ✔ Com dados infinitos, cada consulta poderia usar uma fatia nova e independente; o vazamento nasce da escassez, não da simples existência de um teste.
- ✔ Um teste de 1% ainda estima o mesmo risco esperado sem viés, só que com muito mais ruído amostral — o mesmo padrão que o intervalo largo do Bootstrap confirma mais adiante nesta aula.
- ✔ É o "overfitting ao benchmark" da comunidade: nenhum artigo isolado reusa o teste, mas a busca coletiva e repetida por melhorias nele tem o mesmo efeito agregado.
- ✗ CV torna a *validação* mais barata, mas não substitui o papel do teste — reportar o número final ainda exige uma fatia nunca usada nem para treinar, nem para escolher hiperparâmetros.

## 3. Validação Cruzada

**Pergunta motivadora:** Por que a média de $k$ avaliações de
validação é uma estimativa melhor do erro esperado do que um único
split treino/validação?

Um único split é uma única amostra de "qual seria o desempenho numa
amostra de teste nova" — sujeita inteiramente ao acaso de quais pontos
caíram na validação daquela vez. $k$-fold repete essa simulação $k$
vezes, com partições diferentes e sem desperdiçar dados (todo ponto
serve de treino em $k-1$ rodadas e de validação em exatamente uma), e
a média sobre $k$ rodadas reduz a variância da estimativa em relação a
uma única rodada — o mesmo argumento estatístico de "média de várias
medidas é mais estável que uma medida isolada", aplicado à estimação
do risco esperado.

- ✔ Com $k=2$, cada metade dos dados serve de treino uma vez; é o caso mais "econômico" em dados de treino por fold.
- ✔ Folds disjuntos garantem que cada ponto seja validado exatamente uma vez; sobreposição quebraria essa contabilidade.
- ✔ Mesma lógica de "não confiar numa única amostra", transferida para testes A/B.
- ✗ O valor de CV varia (pouco, mas varia) conforme a partição aleatória escolhida, como o bloco seguinte mostra.

## 4. Viés e Variância do Estimador de CV

**Pergunta motivadora:** Se LOOCV é "quase sem viés", por que ele não
é sempre a escolha certa — e por que, nesta amostra específica, ele
produziu uma estimativa MENOR do que 5-fold e 10-fold, em vez de
simplesmente "mais precisa"?

"Quase sem viés" e "mais precisa" não são sinônimos. LOOCV treina com
quase toda a amostra em cada rodada, então o viés (a diferença entre o
que se espera medir em média e o risco verdadeiro) é pequeno — mas os
$N$ conjuntos de treino do LOOCV são quase idênticos entre si, o que
infla a variância do estimador. O número que o LOOCV produziu aqui
(89,4%) não é "mais correto" que os de 5-fold/10-fold (~92–93%): é uma
estimativa diferente, de uma quantidade correlata mas não idêntica,
com seu próprio ruído de amostra finita. Baixo viés e baixa variância
são propriedades independentes de um estimador, e essa aula mostra um
caso concreto em que otimizar uma não otimiza automaticamente a outra.

- ✗ Deixar de fora metade dos dados usa muito menos dados de treino por rodada (~50% em vez de ~99,7%) — isso reintroduz viés; o nome do esquema não preserva a propriedade.
- ✔ Sem variação nos dados, nenhum esquema de reamostragem consegue gerar variabilidade — a diferença de variância entre os esquemas vem da heterogeneidade real da amostra.
- ✔ É exatamente o achado desta aula (10-fold variou mais que 5-fold aqui) transportado para outro domínio — uma tendência estatística, não uma garantia caso a caso.
- ✗ LOOCV não é "incorreto" — é uma estimativa válida, só mais cara e potencialmente mais variável; a recomendação prática de $k=5/10$ é sobre custo-benefício, não sobre correção estatística.

## 5. Seleção de Modelo por CV

**Pergunta motivadora:** Se a árvore de 4 folhas e a árvore de 19
folhas empatam na acurácia de teste, o que exatamente a validação
cruzada "comprou" ao escolher a mais simples?

Não foi acurácia — foi **parcimônia sem custo**. As 15 folhas extras
da árvore completa não contribuíram para generalização (o teste
empata), então elas existem só para memorizar padrões específicos do
conjunto de treino que não se repetem na população. A CV identificou
isso comparando candidatos de $\lambda$ em dados nunca vistos em cada
fold, e escolheu o ponto em que crescer mais a árvore deixa de ajudar
— um modelo mais simples, mais rápido de treinar/avaliar, mais fácil
de interpretar e auditar, com o mesmo desempenho esperado.

- ✔ Se não há diferença de folhas, não há nada para a poda ter mudado.
- ✔ Seria um sinal de que o $\lambda$ escolhido podou demais, sacrificando desempenho real.
- ✔ Restrição de hardware soma às vantagens de simplicidade que, no experimento médico, eram "de graça".
- ✗ No experimento real, a árvore 1-SE teve acurácia de teste MENOR (90,1% contra 91,8%) — simplicidade custou desempenho aqui.

## 6. O Bootstrap

**Pergunta motivadora:** Por que reamostrar o conjunto de teste e
reamostrar+reajustar no conjunto de treino respondem perguntas
diferentes, mesmo usando a mesma técnica de reamostragem com
reposição?

A técnica (sortear com reposição, recalcular a estatística, repetir
$B$ vezes) é idêntica nos dois casos — o que muda é **o que está
sendo variado a cada réplica**. Reamostrar o teste varia só quais
acertos/erros já observados entram em cada réplica, isolando a
incerteza de *medir* a acurácia com um teste de tamanho finito (o
modelo em si nunca muda). Reamostrar o treino e reajustar varia quais
pacientes entram no treino de cada réplica e treina uma árvore nova a
cada vez, isolando a instabilidade do *procedimento de ajuste* —
quanto a árvore final teria sido diferente com uma amostra de treino
ligeiramente diferente. Mesma ferramenta, duas fontes de incerteza
distintas.

- ✔ Com poucos pontos, há poucas reamostragens distintas possíveis; a aproximação fica grosseira.
- ✔ $B$ controla a precisão *Monte Carlo* da aproximação, não a validade do método em si.
- ✔ O Bootstrap não se limita a médias; qualquer estatística (inclusive diferenças de proporções) pode ser reamostrada.
- ✗ CV estima o risco esperado; Bootstrap estima a variabilidade amostral — perguntas diferentes, tipicamente complementares, não redundantes.

## 7. Vazamento de Dados

**Pergunta motivadora:** Por que selecionar os atributos mais
correlacionados usando a amostra inteira, antes do split de CV, é uma
forma de vazamento de dados mesmo que o classificador final só veja os
dados de treino de cada fold?

O vazamento não está na etapa de treino do classificador — está na
etapa anterior, de **seleção**. Quando os 100 atributos "mais
correlacionados" são escolhidos olhando também os rótulos do fold que
depois será usado para validar, esses atributos já foram informados
(mesmo que indiretamente) pelos próprios pontos que deveriam medir a
generalização. O classificador nunca vê os rótulos de validação
diretamente, mas o *espaço de atributos* que ele recebe já foi
desenhado sob medida para aquele fold específico — a independência
entre treino e validação, que é o que dá sentido à CV, já foi
quebrada antes do classificador entrar em cena.

- ✔ Sem atributos candidatos, não há seleção possível, e portanto não há esse mecanismo de vazamento.
- ✗ Normalizar com estatísticas da amostra inteira (incluindo validação) também é vazamento, mesmo sem tocar nos rótulos — é exatamente o cenário da Questão Discursiva 2 desta aula.
- ✔ A informação da própria distribuição dos dados de validação vaza para o treino através da normalização compartilhada.
- ✗ Vazamento pode ocorrer sem nunca usar rótulos, como os itens (b) e (c) acabaram de mostrar.
