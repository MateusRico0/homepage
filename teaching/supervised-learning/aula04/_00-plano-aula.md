## Resumo — Aula 4

Esta aula muda o objeto de estudo: em vez de um modelo específico, o assunto é o *procedimento* de avaliar e escolher um modelo. A tese central: o erro medido nos próprios dados de treino é uma estimativa **otimista** e **enviesada** do erro de generalização — não porque o modelo "trapaceia", mas porque ele foi ajustado exatamente para minimizar esse número. Cross-validation é apresentada não como uma receita de bolo ("separe em k pedaços"), mas como uma **simulação de amostragem repetida** da conjunta $P(X,Y)$: cada fold aproxima o que aconteceria se pudéssemos, de verdade, coletar uma nova amostra de teste. O Bootstrap resolve um problema relacionado, mas diferente — não "qual é o erro esperado do modelo", e sim "quão incerta é uma estatística calculada a partir da minha amostra".

**Pré-requisitos:** Aulas 1–3 completas (teoria da decisão, ajuste por máxima verossimilhança, CART e a poda por custo-complexidade — cujo parâmetro de regularização, deixado em aberto na Aula 3, é resolvido aqui).

**Dataset-fio:** Breast Cancer Wisconsin (`scikit-learn/breast-cancer-wisconsin`, 569 pacientes, diagnóstico binário) — mesmo domínio de classificação binária médica já familiar da Aula 1, mas com múltiplos atributos contínuos, adequado para treinar as árvores de decisão da Aula 3 e reaproveitar a mesma `cost_complexity_pruning_path` já usada lá, agora escolhendo o parâmetro por validação cruzada em vez de inspeção visual.

## Plano de aula — Aula 4 (carga horária estimada: ~135min)

1. **Bloco 0 — Abertura: o problema que a Aula 3 deixou em aberto** (~10
   min) — A Aula 3 podou uma árvore "olhando o gráfico" do
   custo-complexidade. Pergunta de abertura: como escolher esse parâmetro
   sem espiar o conjunto de teste? Roteiro explícito: (i) por que o erro
   de treino engana, (ii) o que exatamente a validação cruzada estima,
   (iii) como escolher o número de folds, (iv) o que o Bootstrap estima
   que a CV não estima.

2. **O erro de treino é uma estimativa otimista** (~15 min) — Treinar
   árvores de profundidade crescente no Breast Cancer Wisconsin; mostrar
   a acurácia de treino subindo monotonicamente até ~100%, enquanto uma
   fatia de dados nunca vista no ajuste conta uma história diferente.
   Formalizar: o erro empírico $\hat{R}(\theta)$ é enviesado para baixo
   como estimador do risco esperado $R(\theta) = \mathbb{E}_{(X,Y)\sim
   P}[\mathcal{L}(Y, f_\theta(X))]$, porque $\theta$ foi escolhido
   observando os mesmos dados usados para medir $\hat{R}$.

3. **Train/validation/test: three-way split e vazamento** (~15 min) —
   Por que um único split não parametriza bem "quão boa é a estimativa";
   a diferença entre usar o conjunto de validação para escolher
   hiperparâmetros e usar o conjunto de teste para reportar o número
   final; o pecado de "espiar" o teste mais de uma vez.

4. **k-fold Cross-Validation como simulação de amostragem** (~20 min) —
   O argumento central da aula: cada fold de validação é, sob a
   suposição de amostra i.i.d. de $P(X,Y)$, uma aproximação de "coletar
   uma nova amostra de teste". A média das $k$ estimativas de erro
   converge para $\mathbb{E}_{\mathcal{D}}[\hat{R}]$, uma aproximação do
   risco esperado. Estratificação (`StratifiedKFold`) para preservar a
   proporção de diagnóstico (benigno/maligno) em cada fold — ponte com o
   cuidado de classes desbalanceadas já visto na Aula 1.

5. **Escolhendo k: viés e variância do próprio estimador de CV** (~15
   min) — LOOCV ($k=N$): quase sem viés, mas alta variância e caro
   computacionalmente (e as $N$ estimativas ficam correlacionadas entre
   si). $k$ pequeno (5–10): mais viesado (treina com menos dados por
   fold), mas bem mais barato e com estimativa mais estável. $k=5$ ou
   $k=10$ como escolha prática padrão, não arbitrária.

6. **Aplicação: escolhendo a poda da Aula 3 por CV** (~20 min) — Reusar
   `cost_complexity_pruning_path` (já introduzida na Aula 3) sobre o
   Breast Cancer Wisconsin; para cada candidato a $\alpha_{ccp}$, medir o
   erro médio de 5-fold CV; escolher o $\alpha$ que minimiza esse erro
   (ou a regra "1 desvio-padrão", mencionada como refinamento). Fecha o
   gancho deixado pela Aula 3 com uma resposta procedimental, não visual.

7. **O Bootstrap: incerteza de um estimador** (~20 min) — Reamostragem
   com reposição da amostra original; cada réplica bootstrap treina (ou
   avalia) o mesmo procedimento, gerando uma distribuição empírica de
   uma estatística (ex: acurácia de teste, ou AUC). Diferença central com
   CV: CV estima o risco esperado de um procedimento; Bootstrap estima a
   variabilidade amostral de uma estatística já calculada. Construir um
   intervalo de confiança percentílico para a acurácia do modelo podado
   da Aula 3.

8. **Armadilhas comuns** (~15 min) — Vazamento de informação ao normalizar
   ou selecionar atributos usando a base inteira antes do split (a
   transformação "vê" dados que deveriam ser invisíveis); reamostragem
   ingênua em dados com estrutura de grupo/tempo (fora do escopo desta
   aula, mas mencionado); reportar a média de CV sem o desvio-padrão
   (dá uma falsa sensação de precisão).

9. **Fechamento e ponte** (~5 min) — Recapitular as quatro perguntas do
   roteiro; ponte para a Aula 5 (Regressão Linear e Máxima
   Verossimilhança): a ideia de "erro de treino enganosamente otimista"
   reaparecerá formalizada como o viés introduzido pela complexidade do
   modelo, quando a decomposição viés-variância for construída na Aula
   8 — este bloco de seleção de modelo é o alicerce prático sobre o qual
   aquela teoria será construída.

### Nota de dados

Diferente das Aulas 1–3 desta disciplina (que usaram dados sintéticos
gerados via `numpy.random`), esta aula usa dados reais
(`scikit-learn/breast-cancer-wisconsin`, Hugging Face Hub), seguindo a
diretriz do `CLAUDE.md` de preferir dados reais ao problema-fio de uma
aula. Fica registrado como uma mudança de padrão desta aula em diante,
não uma correção retroativa das Aulas 1–3 (que permanecem como estão,
já aprovadas).
