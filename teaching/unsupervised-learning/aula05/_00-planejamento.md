## Resumo — Aula 5

Esta aula é uma reescrita completa (substitui a versão anterior, focada
em BIC/aproximação de Laplace/prova formal de que o EM é subida de
coordenadas no ELBO). O novo eixo: como escolher a **estrutura** de um
modelo não supervisionado (número de componentes $K$, hiperparâmetros
de uma priori, $\epsilon$/`min_samples` de vizinhança) quando não existe
rótulo de gabarito para comparar contra. Parte da Aula 4 (EM clássico,
GMM) e mostra que maximizar a verossimilhança de treino sempre prefere
$K=N$; introduz a injeção de uma **priori** sobre os parâmetros,
chegando a uma forma do ELBO com $\theta$ **dentro** do tratamento
variacional (não como ponto fixo) — a versão corrigida, com
propriedade de Occam de verdade, da ideia de "ELBO como critério de
seleção" que a versão anterior desta aula tratava de forma incompleta.
A partir daí, a aula desloca o problema (trocamos $K$ por
hiperparâmetros de priori — mesmo tipo de escolha, sem gabarito) e
desenvolve três formas de **validação empírica** com conjunto de
validação, já que não há métrica de erro supervisionada disponível:
(a) estabilidade/coesão topológica (Silhueta, Davies-Bouldin) para
clusterização "dura"; (b) verossimilhança preditiva/ELBO em validação
para modelos probabilísticos; (c) *Posterior Predictive Checks* (PPC)
como teste definitivo de adequação do modelo generativo, além de
qualquer métrica escalar. Pré-requisitos: EM e GMM (Aula 4), a
definição básica de KL e da decomposição
$\ln p(\mathbf{X})=\mathcal{L}(q)+\mathrm{KL}(q\|p)$ (já construída na
versão anterior desta própria aula, reaproveitada aqui em versão mais
enxuta).

**Estratégia Pedagógica:** Estratégia A (*Outside-In*) — o fio da aula
é um framework de **decisão prática** (como escolher e validar um
modelo/hiperparâmetro sem rótulo), não uma nova linguagem matemática
autocontida; a lógica é prático → necessidade teórica → formalização →
síntese, com a validação empírica (Blocos 3–5) claramente mais próxima
de "modelo mental aplicado" do que de fundamentação matemática pura.

## Plano de aula — Aula 5 (carga horária: ~115 min)

1. **Abertura — Revisão e Introdução** (~12 min) — revisão cuidadosa do
   Algoritmo EM e do GMM (Aula 4): variável latente $z_n$, responsabilidade
   $\gamma(z_{nk})$ via Bayes, Passo E/Passo M, por que não tem solução
   fechada. Reencena o teste que fecha a versão anterior desta aula: GMM
   ajustado para $K=1,\dots,10$ no mesmo dataset (Breast Cancer
   Wisconsin, `radius_worst`/`concave points_worst`), log-verossimilhança
   de treino nunca cai — se o critério fosse maximizar isso, a resposta
   seria sempre "use o maior $K$", inútil na prática. Ideia central: a
   pergunta certa não é "que $\theta$ explica melhor os dados", é "que
   **estrutura** de modelo é razoável à luz dos dados — e como validar
   essa escolha sem rótulo?". Roteiro explícito (as 4 perguntas do
   roteiro do usuário, adaptadas): (1) como uma priori sobre $\theta$
   conserta o problema de $K=N$? (2) trocar $K$ por hiperparâmetros de
   priori elimina a subjetividade, ou só a desloca? (3) sem rótulo, como
   validar clusterização "dura" (K-Means/DBSCAN)? (4) e modelos
   probabilísticos — e existe um teste mais definitivo que qualquer
   métrica escalar?

2. **Intuição** (~8 min) — sem equações: se penalizarmos $\theta$ com
   uma priori, a "distância" entre a priori e a posterior aprendida vira
   uma penalidade natural de complexidade (quanto mais o modelo precisa
   se afastar da priori para explicar os dados, mais caro); esse mesmo
   princípio de "pagar para se afastar de uma crença inicial" reaparece,
   de formas diferentes, em todo hiperparâmetro de estrutura (um $K$ de
   k-means, um $\epsilon$ de DBSCAN); quando não dá para calcular isso
   analiticamente, validamos empiricamente, olhando o comportamento do
   modelo em dados nunca usados no ajuste — o panorama inteiro da aula.

3. **Bloco 1 — Do EM Clássico ao ELBO (EM + Priori)** (~20 min) —
   desenvolvimento *principled*: (i) reaproveita a decomposição geral
   $\ln p(\mathbf{X})=\mathcal{L}(q)+\mathrm{KL}(q\|p)$ e a
   não-negatividade do KL, já demonstradas na versão anterior desta
   aula (reaproveitar a prova via Jensen, de forma mais enxuta — não
   precisa redemonstrar do zero, só recordar o resultado com 1-2 frases
   do porquê, no espírito da regra de Revisão); (ii) mostra que manter
   $\theta$ **fora** de $\mathbf{Z}$ (como a Aula 4 fez) devolve o EM
   comum, cujo ELBO no ótimo colapsa a $\ln p(\mathbf{X}\mid
   \theta_{\mathrm{ML}})$ — sem penalidade de complexidade nenhuma,
   mesma falha do Bloco de Abertura; (iii) constrói a alternativa: dar
   uma priori $p(\theta)$ a $\theta$ e tratá-lo também como variável do
   tratamento variacional, $q(\mathbf{Z},\theta)\approx q(\mathbf{Z})
   q(\theta)$, chegando a
   $$\mathrm{ELBO} = \mathbb{E}_q[\ln p(\mathbf{X}\mid\mathbf{Z},\theta)]
   - \mathrm{KL}\big(q(\mathbf{Z},\theta)\,\|\,p(\mathbf{Z},\theta)\big),$$
   com o termo de ajuste tentando "decorar" os dados e o KL agindo como
   Navalha de Occam. Demonstração numérica: `BayesianGaussianMixture`
   do scikit-learn (Dirichlet Process/priori de Dirichlet truncada) no
   mesmo dataset, mostrando componentes "sobrando" terem seu peso
   empurrado a quase zero automaticamente — a poda automática do PRML
   §10.2, conectando de volta à correção feita informalmente no
   documento `_nota-variacional-e-selecao-de-modelos.md` desta sessão.

4. **Bloco 2 — O Dilema dos Hiperparâmetros** (~12 min) — a troca de
   problemas: sair de "escolher $K$" para "calibrar hiperparâmetros de
   priori" desloca a subjetividade, não a remove. Exemplos concretos:
   $\alpha_0$ da priori de Dirichlet (Bloco 1), $K$ do K-Means (sem
   priori nenhuma — parâmetro de estrutura "nu"), $\epsilon$/`min_samples`
   do DBSCAN (já visto na Aula 3, via HDBSCAN — reconectar brevemente).
   Fecha nomeando o problema central que os Blocos 3–5 resolvem: como
   calibrar e validar essas escolhas sem métrica supervisionada?

5. **Bloco 3 — Validação Empírica em Clusterização "Dura"** (~18 min) —
   redefine "validação" no não supervisionado: não é acerto contra
   gabarito, é estabilidade topológica/capacidade de generalização.
   Métricas intrínsecas calculadas no conjunto de **validação** (nunca
   visto no ajuste) a partir das regras/centroides aprendidos no treino:
   Coeficiente de Silhueta (Rousseeuw, 1987) e Índice de Davies-Bouldin
   (Davies & Bouldin, 1979) — definição de cada uma, com fórmula.
   Técnica de perturbação/consistência: ajustar no treino, aplicar na
   validação, verificar se a estrutura se mantém — estruturas de
   sobreajuste desaparecem em dados novos. Demonstração: K-Means com
   vários $K$ no dataset-fio, treino/validação, Silhueta e
   Davies-Bouldin calculados na validação.

6. **Bloco 4 — Validação por Verossimilhança (Modelos Probabilísticos)**
   (~18 min) — para GMM (e, por extensão, VAEs — ponte futura), a
   métrica migra de topologia para probabilidade direta: congelar
   $q(\theta)$/$\theta$ aprendido no treino, avaliar log-verossimilhança
   preditiva (ou o próprio ELBO) nas amostras de validação. Diagnóstico
   de sub/sobreajuste: modelo complexo demais concentra densidade quase
   infinita nos pontos de treino, mas a probabilidade de validação
   despenca — permite comparar empiricamente, por exemplo, $\alpha_0=0{,}1$
   vs. $\alpha_0=1{,}0$ na priori de Dirichlet do Bloco 1. Demonstração:
   curva de log-verossimilhança de treino vs. validação por $K$/por
   $\alpha_0$, mostrando a divergência entre as duas curvas quando o
   modelo generaliza mal.

7. **Bloco 5 — A Prova Final: Posterior Predictive Checks (PPC)** (~15
   min) — limitação de números únicos (ELBO, Silhueta): podem esconder
   falha estrutural (o modelo pode ter um bom escore e ainda assim não
   ter entendido o processo gerador). PPC: amostrar parâmetros da
   posterior aprendida, gerar dados sintéticos $\mathbf{X}_{\text{sim}}$,
   comparar estatísticas/formato contra $\mathbf{X}_{\text{real}}$
   (Gelman & Rubin, 1996 — conceito, sem trecho literal de um PDF desta
   disciplina). Demonstração: amostrar do GMM ajustado no dataset-fio,
   sobrepor a dispersão sintética à real.

8. **Fechamento — Síntese e Ponte para a Aula 6** (~12 min) — retomar as
   4 perguntas do roteiro (uma frase cada). Síntese: seleção de modelo
   não supervisionado é sempre uma combinação de penalidade analítica
   (ELBO/BIC) **e** validação empírica — nenhuma sozinha basta. Ponte
   para a Aula 6: a Parte 2 do curso troca a variável latente categórica
   (Aulas 3–5) por uma contínua (PCA/PPCA) — a mesma pergunta de
   validação ("este hiperparâmetro de estrutura — aqui, a dimensão
   latente — é razoável?") reaparece lá, e o ELBO volta a aparecer de
   forma central na Aula 7 (VAE), agora sem posterior de forma fechada.

## Fontes usadas — Aula 5

### Fonte 1: PRML, §9.4 (decomposição $\ln p(\mathbf{X})=\mathcal{L}(q)+\mathrm{KL}(q\|p)$) e §1.6.1 (desigualdade de Gibbs/KL$\ge0$)
**Uso pretendido:** recordar (não redemonstrar do zero) a decomposição
geral e a não-negatividade do KL, base do Bloco 1. Reaproveita a
demonstração já aprovada na versão anterior desta aula — trecho literal
a confirmar contra o PDF na Etapa 3, se for citar de novo.

### Fonte 2: PRML, §10.1–10.2 (Inferência Variacional; GMM Variacional com priori de Dirichlet)
**Uso pretendido:** base formal do Bloco 1 (ELBO com $\theta$ dentro do
tratamento variacional) e da demonstração de poda automática de
componentes via `BayesianGaussianMixture`, citada no Bloco 1/2.
**Trecho a extrair na Etapa 3** (ainda não lido nesta etapa de
planejamento — sinalizar se a citação literal mudar o enunciado
proposto acima).

### Fonte 3: Rousseeuw, P.J. (1987), "Silhouettes: a graphical aid to the interpretation and validation of cluster analysis" — fora dos PDFs de `_fontes/`
**Uso pretendido:** definição formal do Coeficiente de Silhueta, Bloco 3.
Citado por nome/ano, sem trecho literal (artigo não disponível em
`_fontes/`) — a fórmula em si é reproduzida diretamente, é matemática
padrão, não uma citação de prosa.

### Fonte 4: Davies, D.L. & Bouldin, D.W. (1979), "A Cluster Separation Measure" — fora dos PDFs de `_fontes/`
**Uso pretendido:** definição formal do Índice de Davies-Bouldin, Bloco 3.
Mesmo tratamento da Fonte 3 (fórmula direta, sem trecho literal).

### Fonte 5: Gelman, A. & Rubin, D.B. (1996), conceito de *Posterior Predictive Check* — fora dos PDFs de `_fontes/`
**Uso pretendido:** fundamentação conceitual do Bloco 5. Citado por
nome/ano, explicado com palavras próprias (não há PDF desta obra em
`_fontes/` para extrair trecho literal).

**Observação sobre fontes 3–5:** diferente das aulas anteriores desta
disciplina (que citam PRML/DLFC/ESL quase exclusivamente), estas três
técnicas não constam nos três livros-texto do curso — são citadas por
nome/ano/artigo original, com a fórmula/ideia reproduzida diretamente
em vez de um trecho de prosa traduzido. Sinalizando isso explicitamente
para aprovação, já que foge um pouco do padrão de citação já
estabelecido nas Aulas 1–4.

---

**Peça explícita de aprovação:** este plano risca e substitui o
`_00-planejamento.md` anterior (aprovado em 2026-09-15) — a aula final
também vai substituir o `index.qmd`, `exercicios.qmd` e `soluções.qmd`
atuais por completo. Pode seguir para a Etapa 3 (montar `index.qmd`
completo) com esta estrutura, ou prefere ajustar algo no plano antes
(tempos por bloco, dataset, as fontes 3–5 fora do padrão, ou a ordem dos
blocos)?
