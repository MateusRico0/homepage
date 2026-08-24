# Soluções — Questões de Verdadeiro/Falso (Aula 4)

> Arquivo de apoio, não publicado (prefixo `_`). Contém a resposta e a
> justificativa de cada item das 12 questões de V/F do `index.qmd`. O
> `index.qmd` publicado continua sem solução — este arquivo existe só
> para conferência do professor/monitor, seguindo a metodologia de
> criação de questões definida em `../../CLAUDE.md`.

## O Viés do Erro de Treino

**a.** [ ] No limite em que a profundidade da árvore não é limitada e há um ponto de treino distinto por folha, o erro de treino tende a $0\%$, independentemente de quão complexa seja a fronteira real entre as classes.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Uma folha por ponto memoriza o treino perfeitamente, não importa a complexidade real do problema — é exatamente o que se vê no experimento desta aula (treino chega a $100\%$ a partir da profundidade 6), e memorização não exige que a fronteira real seja simples.

**b.** [ ] Se a árvore de profundidade 15 tem a mesma acurácia de teste que a árvore de profundidade 6, isso prova que a árvore mais profunda é necessariamente pior no teste do que uma menos profunda.

**Heurística:** Contrafactual
**Resposta:** Falso
**Justificativa:** Empatar em acurácia de teste não é "ser pior" — é empatar. A pergunta da pausa ativa desta seção não é sobre qual é pior, mas sobre por que, MESMO empatando, ainda se prefere a mais rasa (parcimônia, estabilidade) — o enunciado inverte a premissa.

**c.** [ ] Num modelo de previsão de preços de imóveis ajustado com um polinômio de grau muito alto (que passa exatamente por todos os pontos de treino), o erro de treino seria próximo de zero, mas isso não garante nada sobre o erro em imóveis não vistos.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** É o mesmo fenômeno de overfitting (memorizar o treino sem generalizar) transferido para regressão polinomial — um exemplo clássico da literatura de aprendizado de máquina, reforçando que a mecânica não é exclusiva de árvores.

**d.** [ ] Como o erro de treino tende a subestimar o erro de generalização, conclui-se que um modelo com erro de treino alto necessariamente generaliza melhor do que um com erro de treino baixo.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** Viés otimista do erro de treino não inverte a relação entre as duas quantidades — um modelo que ajusta mal até o próprio treino (erro de treino alto, *underfitting*) não é automaticamente melhor generalizador; a relação entre as duas taxas de erro é mais sutil do que uma simples inversão.

---

## Train/Validation/Test

**a.** [ ] No limite em que o conjunto de teste é consultado repetidas vezes durante o ajuste de hiperparâmetros, a estimativa final de desempenho no teste se torna tão otimista quanto medir no próprio conjunto de treino.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Espiar o teste repetidamente para ajustar decisões é, em essência, incorporá-lo ao processo de ajuste — no limite de infinitas consultas, o teste deixa de ser "não visto" e a estimativa herda o mesmo otimismo do erro de treino.

**b.** [ ] Se o conjunto de validação, em vez do de teste, fosse consultado repetidamente para escolher hiperparâmetros, isso não teria custo estatístico algum, pois validação existe exatamente para ser consultada quantas vezes for preciso.

**Heurística:** Contrafactual
**Resposta:** Falso
**Justificativa:** Consultar a validação repetidamente TEM custo — o hiperparâmetro escolhido pode se ajustar ao ruído específico daquela validação (uma forma mais branda do mesmo problema do teste), motivo pelo qual um conjunto de teste final, nunca usado nessa escolha, continua sendo necessário.

**c.** [ ] Numa competição de ciência de dados, o "*leaderboard* público" funciona como um conjunto de validação consultável repetidamente; competidores que otimizam demais para ele costumam piorar no *leaderboard* privado (o teste verdadeiro) — o *overfitting ao leaderboard*.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** É um fenômeno real e bem documentado em competições como o Kaggle: o *leaderboard* público funciona exatamente como uma validação espiada repetidamente, e o *leaderboard* privado revela o custo estatístico dessa espiada.

**d.** [ ] Como o conjunto de treino é usado para ajustar os parâmetros do modelo, conclui-se que o conjunto de validação é usado para ajustar os dados do modelo (limpá-los ou transformá-los), não seus hiperparâmetros.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** É uma falsa paralela: o conjunto de validação serve para escolher HIPERPARÂMETROS (ou tomar decisões de modelo), não para "ajustar os dados" — essa segunda função nem corresponde a nenhum papel padrão de validação.

---

## O Procedimento k-fold

**a.** [ ] No limite em que $k=N$ (LOOCV), cada fold de validação contém exatamente um único ponto.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** É a própria definição de LOOCV: com $k=N$ folds, cada fold necessariamente contém $N/k=1$ ponto.

**b.** [ ] Se, em vez de treinar $k$ modelos diferentes, k-fold CV usasse um único modelo treinado com todos os dados para avaliar cada fold de validação, a estimativa resultante deixaria de simular uma amostra de teste verdadeiramente independente do ajuste.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** Se o modelo já viu os pontos do fold "de validação" durante o ajuste, avaliá-lo ali é medir erro de treino disfarçado, não uma simulação de dado novo — o ponto central de k-fold é justamente excluir cada fold do ajuste do modelo que o avalia.

**c.** [ ] Num estudo médico com pacientes de 10 hospitais diferentes, se cada fold de uma 5-fold CV misturar aleatoriamente pacientes de todos os hospitais, a CV pode superestimar o desempenho num hospital totalmente novo.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** Misturar hospitais nos folds permite que o modelo "veja" características de todos os hospitais durante o treino, mesmo que não veja aqueles pacientes específicos — uma forma de vazamento em nível de grupo, distinta mas relacionada à seleção de atributos discutida mais adiante na aula.

**d.** [ ] Como cada fold de treino em k-fold usa quase os mesmos dados que o treino completo, o modelo ajustado em cada fold é praticamente idêntico ao ajustado com a amostra inteira, então CV mede essencialmente a mesma coisa que o erro de treino.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** Por mais parecidos que sejam os conjuntos de treino entre folds, cada modelo é AVALIADO em pontos que não usou para se ajustar — a diferença crucial em relação ao erro de treino, que avalia exatamente nos mesmos pontos usados no ajuste.

---

## Estratificação

**a.** [ ] No limite em que uma das classes representa menos de $1\%$ da amostra, a ausência de estratificação aumenta substancialmente o risco de algum fold não conter nenhum exemplo dessa classe rara.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Com uma classe muito rara, uma partição puramente aleatória tem chance real de, por azar, deixar algum fold pequeno sem nenhum representante dela — exatamente o cenário em que a estratificação (que força a proporção em cada fold) é mais valiosa.

**b.** [ ] Se as classes já estivessem perfeitamente balanceadas ($50\%/50\%$) na amostra completa, usar `StratifiedKFold` em vez de `KFold` comum produziria sempre exatamente os mesmos folds, sem nenhuma diferença possível.

**Heurística:** Contrafactual
**Resposta:** Falso
**Justificativa:** Mesmo com a população global balanceada, uma partição aleatória comum ainda pode gerar, por acaso, um fold pequeno com proporção diferente de $50\%/50\%$; `StratifiedKFold` força a proporção em CADA fold individualmente, o que não é garantido automaticamente só porque o total é balanceado.

**c.** [ ] Num problema de imagens médicas com 3 classes muito desbalanceadas ($90\%/9\%/1\%$), a estratificação se torna proporcionalmente mais importante do que num problema balanceado de 2 classes.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** Quanto mais desbalanceadas as classes (e mais classes existirem), maior o risco de uma partição aleatória deixar alguma classe minoritária mal representada nalgum fold — a estratificação escala em importância com o grau de desbalanceamento.

**d.** [ ] Como a estratificação muda quais pontos específicos caem em cada fold, ela também altera o valor esperado da estimativa de CV, tornando-a enviesada.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** Estratificação é uma técnica de REDUÇÃO DE VARIÂNCIA entre folds (torna as partições mais parecidas com a população, fold a fold), não uma fonte de viés no valor esperado — mudar quais pontos caem em cada fold não é o mesmo que mudar a expectativa da estimativa resultante.

---

## LOOCV vs. k-fold Pequeno

**a.** [ ] No limite em que $k\to N$ (o maior valor possível de $k$), cada modelo de LOOCV é treinado com $N-1$ pontos — o máximo de dados de treino possível dentro do esquema de k-fold.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Com $k=N$, cada fold de validação tem 1 ponto, deixando $N-1$ para o treino — a maior fração de dados de treino que qualquer escolha de $k$ permite dentro do esquema de k-fold.

**b.** [ ] Se repetíssemos o cálculo de LOOCV várias vezes no mesmo conjunto de dados, obteríamos valores diferentes a cada repetição, assim como acontece com 5-fold e 10-fold quando a partição é sorteada de novo.

**Heurística:** Contrafactual
**Resposta:** Falso
**Justificativa:** LOOCV é determinístico — ele usa TODAS as $N$ divisões possíveis de "deixar um de fora", não uma amostra aleatória de divisões, então repetir o cálculo sempre reproduz o mesmo valor. É exatamente o oposto do que acontece com 5-fold/10-fold, cuja partição é sorteada.

**c.** [ ] Num conjunto de apenas 20 pacientes, LOOCV se torna proporcionalmente mais atraente do que 10-fold, porque deixar de fora 2 pacientes (10%) já é uma perda relativamente maior de dados de treino do que deixar de fora 1.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** Com amostras pequenas, cada ponto de treino vale proporcionalmente mais; LOOCV maximiza os dados de treino por fold, uma vantagem que fica mais valiosa quanto menor for $N$ — o oposto do regime de $N$ grande, em que o custo computacional de LOOCV se torna a preocupação dominante.

**d.** [ ] Como o ESL descreve o estimador de LOOCV como aproximadamente não-enviesado, conclui-se que LOOCV é sempre a melhor estimativa possível do erro de generalização, superando 5-fold e 10-fold em qualidade.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** Baixo viés não é a mesma coisa que baixa variância — o próprio ESL destaca que o LOOCV paga esse baixo viés com alta variância. O achado honesto desta aula (LOOCV em $89{,}4\%$, abaixo da média repetida de 5-fold e 10-fold em torno de $92$–$93\%$) mostra na prática que "menos enviesado" não significa "melhor estimativa" de forma automática.

---

## Custo Computacional e Variância de k

**a.** [ ] No limite em que $N$ é muito grande (milhões de pontos), o custo de LOOCV ($N$ ajustes completos) se torna proibitivo mesmo com ajustes individuais rápidos, tornando $k=5$ ou $10$ escolhas praticamente necessárias.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Mesmo um ajuste individual barato, multiplicado por milhões de repetições (uma por ponto), se torna computacionalmente inviável — o custo de LOOCV escala linearmente com $N$, tornando $k$ pequeno a escolha prática dominante em escala.

**b.** [ ] Se os $N$ conjuntos de treino do LOOCV fossem, ao contrário do que o ESL descreve, bem diferentes entre si, a alta variância do estimador de LOOCV deixaria de ser explicada por esse mecanismo.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** A explicação do ESL para a alta variância do LOOCV é especificamente a alta SIMILARIDADE entre os $N$ conjuntos de treino (cada um difere do outro por só 1 ponto); se essa similaridade não existisse, essa explicação causal específica não se aplicaria (ainda que outras causas de variância pudessem existir).

**c.** [ ] Se um outro pesquisador repetisse o experimento desta aula com uma semente aleatória diferente para a partição de 10-fold, a média obtida provavelmente seria ligeiramente diferente, mas dentro da ordem de grandeza do desvio-padrão entre repetições já medido.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** Uma nova semente é só mais um sorteio da mesma distribuição de partições possíveis já caracterizada pelo desvio-padrão entre repetições medido nesta aula — espera-se que o novo valor caia dentro dessa faixa de variação típica.

**d.** [ ] Como $k=5$ e $k=10$ são mais baratos computacionalmente que LOOCV, conclui-se que eles também produzem, necessariamente, uma estimativa de erro menos precisa do que LOOCV.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** Custo computacional e qualidade estatística são eixos diferentes — de fato, o achado desta aula mostra o oposto do que a intuição "mais caro, portanto melhor" sugeriria: o LOOCV (mais caro) teve o valor mais distante da média repetida de 5/10-fold neste dataset específico.

---

## Aplicação: Poda por Validação Cruzada

**a.** [ ] No limite em que $\lambda=0$ (sem nenhuma penalidade), a árvore escolhida seria a árvore completa, sem poda — o extremo oposto da árvore escolhida por CV nesta aula.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Com $\lambda=0$, o critério de custo-complexidade $C(T)=\sum_\tau Q_\tau(T)+\lambda|T|$ se reduz a só $\sum_\tau Q_\tau(T)$, que é sempre minimizado (ou empatado) pela árvore mais completa possível — o oposto do $\lambda$ escolhido por CV nesta aula, que produziu uma árvore de só 4 folhas.

**b.** [ ] Se a árvore escolhida por CV (4 folhas) tivesse tido uma acurácia de teste muito pior do que a árvore completa (19 folhas), em vez do empate observado nesta aula, isso enfraqueceria o argumento de preferir a árvore mais simples.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** O argumento da aula para preferir a árvore simples se apoia no fato de que a simplicidade "não custou nada" (empate de acurácia); se a simplicidade tivesse custado acurácia real, o argumento ficaria mais fraco — teria que ser justificado por outros critérios (interpretabilidade, custo computacional), não mais "de graça".

**c.** [ ] Num sistema de aprovação de crédito auditado por reguladores, uma árvore de 4 folhas escolhida por CV seria mais fácil de justificar do que uma de 19 folhas, mesmo com a mesma acurácia.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** Interpretabilidade e auditabilidade são vantagens práticas reais de modelos mais simples, independentes de qualquer ganho de acurácia — um cenário regulatório concreto em que "empatar em acurácia, preferir o mais simples" tem valor tangível, não só didático.

**d.** [ ] Como `cost_complexity_pruning_path` gera os candidatos de $\lambda$ de forma determinística a partir do treino, escolher $\lambda$ por inspeção visual de um único gráfico treino/validação já garante a mesma reprodutibilidade que escolher por CV com múltiplos folds.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** Os CANDIDATOS a $\lambda$ vêm de forma determinística dos dados, mas a ESCOLHA de qual candidato é "o melhor" com base numa única divisão treino/validação depende de qual divisão específica saiu no sorteio — CV com múltiplos folds reduz essa dependência ao médiar sobre várias divisões, uma vantagem que a inspeção de um único gráfico não tem.

---

## A Regra de 1 Desvio-Padrão

**a.** [ ] No limite em que o desvio-padrão entre folds de CV tende a zero, a regra de 1-SE tende a escolher praticamente o mesmo modelo que a regra de máxima média de CV.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** A faixa de tolerância da regra de 1-SE tem largura proporcional ao próprio erro-padrão; se esse erro-padrão vai a zero, a faixa colapsa para um único ponto — o modelo de máxima média — eliminando a diferença entre as duas regras.

**b.** [ ] Se a árvore escolhida pela regra de 1-SE tivesse, por coincidência, exatamente a mesma acurácia de teste que a árvore de máxima média de CV, isso provaria que a regra de 1-SE está correta em geral, não só neste experimento.

**Heurística:** Contrafactual
**Resposta:** Falso
**Justificativa:** Um resultado coincidente em UM experimento específico não prova uma propriedade GERAL da regra — seria uma generalização apressada a partir de uma única observação. (E, de fato, no experimento real desta aula, a coincidência nem ocorreu: a árvore 1-SE teve acurácia de teste pior.)

**c.** [ ] Num cenário em que o custo de deploy de um modelo complexo é alto (por exemplo, um dispositivo com pouca memória), a regra de 1-SE seria mais atraente do que neste experimento didático, mesmo custando um pouco de acurácia.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** É exatamente o tipo de cenário que a Questão Discursiva 3 desta aula pede para considerar: quando restrições práticas de deploy tornam a simplicidade valiosa por si só, vale mais a pena pagar um pouco de acurácia por ela do que num contexto sem essa restrição.

**d.** [ ] Como a regra de 1-SE reconhece que a estimativa de CV tem incerteza amostral, conclui-se que ela elimina completamente essa incerteza ao escolher o modelo mais simples dentro da faixa.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** A regra 1-SE INCORPORA a incerteza numa decisão (qual modelo escolher entre os "empatados dentro do ruído"), mas não faz a incerteza da estimativa de CV desaparecer — a própria estimativa de CV continua tendo o mesmo erro-padrão de antes.

---

## O Bootstrap

**a.** [ ] No limite em que o número de réplicas $B\to\infty$, a distribuição empírica das réplicas se aproxima de uma aproximação estável da verdadeira distribuição amostral, mas o tamanho de CADA réplica continua sendo $N$, não crescendo com $B$.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** $B$ controla quantas réplicas de tamanho $N$ são geradas — mais $B$ dá uma aproximação Monte Carlo mais precisa da distribuição amostral do estimador, mas cada réplica individual continua do mesmo tamanho da amostra original; $B$ e $N$ são parâmetros independentes.

**b.** [ ] Se o Bootstrap reamostrasse SEM reposição, cada réplica gerada seria idêntica à amostra original (mesmos pontos), tornando a técnica inútil para medir variabilidade.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** Reamostrar $N$ pontos de uma população de $N$ SEM reposição só pode devolver uma permutação de todos os pontos originais — nenhum ponto é omitido, nenhum se repete, então não há variação real entre "réplicas" para medir. É a reposição que permite que pontos se repitam ou fiquem de fora, criando a variabilidade que o método explora.

**c.** [ ] Num estudo que mede a mediana (não a média) do tempo de resposta de um sistema, o Bootstrap ainda poderia estimar um intervalo de confiança para essa mediana, mesmo sem fórmula analítica fechada para seu erro-padrão.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** É uma das grandes vantagens do Bootstrap: ele se aplica a qualquer estatística, não só à média ou à acurácia — não depende de uma fórmula fechada para o erro-padrão, já que a incerteza é estimada empiricamente pela reamostragem.

**d.** [ ] Como o Bootstrap e a validação cruzada usam ambos técnicas de reamostragem sobre os mesmos dados, conclui-se que respondem exatamente à mesma pergunta estatística.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** CV estima o risco esperado de generalização; Bootstrap, na formulação clássica, estima a variabilidade amostral de uma estatística — perguntas relacionadas, mas diferentes, como o próprio ESL registra explicitamente.

---

## Duas Aplicações do Bootstrap

**a.** [ ] No limite em que o conjunto de teste tivesse um número enorme de pacientes (não só 171), o intervalo de confiança da acurácia tenderia a ficar mais estreito do que o observado nesta aula.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Mais dados de teste reduzem o ruído amostral na medição da acurácia; o próprio texto da aula já atribui a largura do intervalo observado ($[87{,}7\%,95{,}9\%]$) ao tamanho modesto do conjunto de teste ($171$ pacientes) — um teste maior estreitaria essa faixa.

**b.** [ ] Se, em vez de reajustar a árvore em cada réplica bootstrap do treino, apenas reavaliássemos a MESMA árvore original em cada réplica, essa variante mediria a mesma coisa que "reamostrar o treino e reajustar".

**Heurística:** Contrafactual
**Resposta:** Falso
**Justificativa:** Sem reajustar, o modelo nunca muda — não há como medir a instabilidade do PROCEDIMENTO DE AJUSTE se o ajuste nunca é repetido. Essa variante mediria outra coisa (talvez nada de muito informativo), não a instabilidade do ajuste que a aplicação original mede.

**c.** [ ] Numa empresa que quer saber tanto a taxa de erro real do seu modelo de fraude implantado quanto o quanto seu processo de treino é sensível à amostra histórica usada, essas duas perguntas exigiriam as duas aplicações distintas do Bootstrap desta aula.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** A primeira pergunta corresponde a reamostrar o TESTE (incerteza de medição); a segunda, a reamostrar o TREINO e reajustar (instabilidade do procedimento) — exatamente o mapeamento das duas aplicações desta aula para duas perguntas de negócio reais e distintas.

**d.** [ ] Como as duas aplicações do Bootstrap desta aula usam a mesma técnica de reamostragem com reposição, elas produzem, necessariamente, o mesmo intervalo de confiança.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** Mesma técnica, perguntas diferentes — não há razão para esperar o mesmo intervalo quando se está medindo incerteza de medição num caso e instabilidade de ajuste no outro.

---

## Vazamento de Dados (Data Leakage)

**a.** [ ] No limite em que o número de atributos irrelevantes $p$ cresce (mantendo $N=50$ fixo), o vazamento por seleção antes do split se torna ainda mais grave, pois há mais chances de achar, por acaso, atributos aparentemente correlacionados com o rótulo.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Com mais atributos candidatos totalmente irrelevantes, a chance de encontrar, por puro acaso, alguns com correlação amostral alta com o rótulo aumenta — mais "tiros na loteria" para o vazamento explorar, piorando o otimismo da estimativa.

**b.** [ ] Se a seleção dos 100 atributos mais correlacionados fosse feita usando só os dados de treino de cada fold, o erro estimado por CV se aproximaria do valor real de $50\%$, em vez do ${\sim}1{,}5\%$ observado no jeito errado.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** É exatamente o resultado numérico do "jeito certo" reproduzido nesta aula: selecionar dentro de cada fold recupera uma estimativa honesta (${\sim}48\%$), muito mais próxima dos $50\%$ reais do que o ${\sim}1{,}5\%$ enviesado do jeito errado.

**c.** [ ] Um pipeline que aplica um redutor de dimensionalidade (como PCA) ajustado com a base inteira, antes de particionar em folds, sofre do mesmo tipo de vazamento do experimento de seleção de atributos desta aula, mesmo sem nenhuma seleção explícita.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** Ajustar qualquer transformação (PCA, normalização, seleção) usando dados que depois aparecerão na validação de algum fold vaza informação da validação para o treino — o mecanismo é o mesmo, independente de a transformação específica ser seleção de atributos ou redução de dimensionalidade.

**d.** [ ] Como o vazamento de dados infla artificialmente a estimativa de CV para cima, conclui-se que vazamento de dados sempre faz a estimativa de CV parecer PIOR do que o desempenho real do modelo.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** É o oposto exato: vazamento faz a estimativa parecer MELHOR (mais otimista) do que o desempenho real, não pior — no experimento desta aula, o "jeito errado" reportou ${\sim}1{,}5\%$ de erro quando o real era $50\%$, ou seja, um desempenho aparentemente muito melhor do que o real.

---

## Reportando Resultados de Validação Cruzada

**a.** [ ] No limite em que o desvio-padrão entre folds de CV tende a zero, reportar só a média já comunica virtualmente toda a informação relevante sobre a incerteza da estimativa.

**Heurística:** Limite
**Resposta:** Verdadeiro
**Justificativa:** Se não há variabilidade real entre os folds, não há informação relevante escondida ao omitir o desvio-padrão — a crítica a "reportar só a média" perde força exatamente na medida em que a variabilidade real se aproxima de zero.

**b.** [ ] Se o ESL não tivesse feito nenhuma recomendação explícita sobre reportar o erro-padrão, ainda assim seria estatisticamente correto reportá-lo, pois a variabilidade entre folds é uma propriedade real da estimativa, independente de qualquer recomendação de livro-texto.

**Heurística:** Contrafactual
**Resposta:** Verdadeiro
**Justificativa:** A correção estatística de reportar incerteza não depende da autoridade de nenhum livro específico — é uma propriedade da própria estimativa (ela TEM variabilidade amostral, quer alguém reporte isso ou não); a citação do ESL é evidência/reforço, não a fonte da correção.

**c.** [ ] Ao comparar dois modelos num artigo científico, reportar "modelo A: 85% de acurácia, modelo B: 84%" sem nenhuma medida de variabilidade não permite ao leitor avaliar se essa diferença é estatisticamente significativa ou só ruído de amostragem.

**Heurística:** Transferência
**Resposta:** Verdadeiro
**Justificativa:** Sem uma medida de variabilidade (desvio-padrão, intervalo de confiança), um ponto percentual de diferença pode estar completamente dentro do ruído esperado de amostragem — exatamente o motivo pelo qual a prática de reportar só médias, criticada nesta aula, também é problemática na publicação científica.

**d.** [ ] Como um desvio-padrão alto entre os folds de CV significa que a métrica varia bastante de fold para fold, conclui-se que um desvio-padrão alto indica uma estimativa mais estável e confiável do desempenho do modelo.

**Heurística:** Falsa equivalência
**Resposta:** Falso
**Justificativa:** É exatamente o oposto: quanto maior a variabilidade entre folds, MENOS estável e confiável é a estimativa — um desvio-padrão alto é um sinal de alerta sobre a precisão do número reportado, não uma virtude.
