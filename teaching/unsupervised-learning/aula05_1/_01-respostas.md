# Respostas da Aula 5.1 — Pausas Ativas

> Arquivo de apoio, não publicado (prefixo `_`). Discussão em prosa das
> 6 pausas ativas do `index.qmd` (a pergunta motivadora + a resolução
> do V/F, que no `index.qmd` só aparece nos slides RevealJS, nunca nas
> notas HTML).
>
> (O gabarito dos 8 blocos de V/F da seção Exercícios **não** é
> discutido aqui — vive em `exercicios.qmd`/`soluções.qmd`, páginas
> públicas e separadas desta aula.)

### Pausa 1 — O papel legítimo da log-verossimilhança de treino

A pergunta tenta uma dicotomia falsa: já que a log-verossimilhança de
treino nunca pune complexidade, seria ela inútil? Não — o ponto da
Abertura é que ela continua sendo o **termo de ajuste** correto, só
não é suficiente **sozinha** para decidir $K$. Toda a aula constrói,
sobre essa mesma quantidade, um segundo termo (a KL) que soma uma
penalidade de complexidade genuína — a log-verossimilhança nunca é
descartada, é complementada.

- ✔ A log-verossimilhança de treino mede corretamente o quão bem os
  parâmetros ajustados explicam os dados que os ajustaram — o
  problema é usá-la sozinha para comparar complexidades diferentes.
- ✗ Um critério bem fundamentado tipicamente reaproveita a
  log-verossimilhança como um termo, somado a uma penalidade — não a
  descarta por completo.
- ✔ Sim — é exatamente a lógica do ELBO: termo de ajuste (relacionado
  à verossimilhança) menos um termo de penalidade (KL).
- ✔ Sim — é o mesmo fenômeno de sobreajuste por máxima verossimilhança
  de qualquer modelo suficientemente flexível.

### Pausa 2 — O ELBO não inventa Occam, ele viabiliza calculá-la

Essa pausa testa se o aluno confunde "de onde vem a penalidade de
complexidade" com "o que o ELBO faz". A Navalha de Occam já mora na
integral da evidência $p(\mathbf{X}\mid\mathcal{M}_m)=\int
p(\mathbf{X},\mathbf{H}\mid\mathcal{M}_m)\,\mathrm{d}\mathbf{H}$, antes
de qualquer aproximação variacional. O ELBO resolve um problema
diferente — calculabilidade —, ao custo de uma aproximação cuja
qualidade (a folga de KL) precisa ser levada a sério.

- ✔ O ELBO resolve calculabilidade, não a ausência de penalidade — essa
  já está na integral da evidência, antes de qualquer aproximação.
- ✗ Se a evidência já fosse calculável exatamente, não haveria motivo
  para aproximá-la — a Navalha de Occam já estaria lá, sem precisar
  de $q$.
- ✔ Quanto mais apertada a KL residual, mais o ranqueamento por
  $\mathcal{L}_m$ se aproxima do ranqueamento pela evidência verdadeira.
- ✗ Mesma família $q$ não garante gaps iguais entre modelos diferentes
  — a distância de $q$ à posterior real pode variar bastante mesmo com
  a mesma forma funcional (a "folga variacional" do Bloco 4).

### Pausa 3 — Poda com $\alpha_0$ fixo: o contraste é com $N_k$, não entre rodadas

Essa é a pausa mais fácil de responder errado por analogia superficial
com a Aula 5 original (que variava $\alpha_0$). O mecanismo de poda
não depende de comparar $\alpha_0$ entre valores diferentes — depende
do **contraste interno**, componente a componente, entre $\alpha_0$
(fixo, igual para todos) e $N_k$ (varia por componente, vindo dos
dados). Um componente com $N_k\approx0$ já fica "preso" perto da
priori, não importa o valor de $\alpha_0$ escolhido, desde que ele seja
o mesmo para todos os componentes.

- ✔ A poda vem do contraste entre $\alpha_0$ (fixo) e $N_k$ (varia por
  componente): $N_k\approx0$ já basta para a concentração posterior
  ficar perto de $\alpha_0$.
- ✗ Colapso de $\Sigma_k$ (EM clássico) e $N_k\approx0$ (GMM Bayesiano)
  são fenômenos relacionados mas distintos — um componente pode ter
  $N_k$ moderado e ainda colapsar sobre um subconjunto pequeno de
  pontos muito próximos.
- ✔ $\alpha_0$ alto deixa a priori mais rígida em torno de pesos
  iguais — dificulta, não facilita, a poda.
- ✔ $W_0^{-1}$ (Normal-Wishart) e $\alpha_0$ (Dirichlet) são ambos
  "pesos" da priori que persistem na atualização posterior, cada um
  impedindo um extremo diferente.

### Pausa 4 — Um acerto do ELBO não é garantia geral

Essa pausa prepara terreno para o Bloco 4 inteiro. O ELBO ter acertado
$K=2$ neste dataset específico não prova nada sobre outros datasets,
nem sobre a folga variacional ser sempre pequena, nem sobre a forma
gaussiana sempre ser adequada. É importante que o aluno não generalize
de "funcionou uma vez" para "sempre funciona" — o mesmo erro de
raciocínio que motivou desconfiar da log-verossimilhança de treino na
Pausa 1.

- ✔ O ELBO de treino é uma cota sob a família $q$ escolhida — nada
  garante que a folga seja igualmente apertada para qualquer estrutura
  de dados.
- ✗ O ELBO penalizar complexidade dentro da família variacional não o
  isenta do viés de otimismo geral de qualquer quantidade avaliada só
  no treino.
- ✔ Má especificação de forma é um problema diferente de excesso de
  parâmetros — um GMM bem penalizado ainda pode "escolher" mal se a
  forma real não é gaussiana.
- ✗ K-Means e DBSCAN não ficam fora de comparação — é exatamente o
  papel da Silhueta/Dunn numa validação comum.

### Pausa 5 — Discordância entre métricas não é erro

O ponto pedagógico aqui é distinguir "discordância" de "erro". Silhueta
e Dunn formalizam noções diferentes de qualidade de partição (médias
vs. extremos); um aluno que conclui "uma delas está bugada" perdeu o
ponto — a lição é usar as duas, cientes de que respondem perguntas
ligeiramente diferentes, e que uma discordância é, ela mesma,
informação (não ruído a ser descartado).

- ✔ As duas métricas formalizam noções diferentes de "boa partição" —
  podem legitimamente discordar sem erro de implementação.
- ✔ Uma métrica de extremos é, por construção, mais sensível a um
  único ponto atípico do que uma métrica de médias.
- ✗ Não assumir forma esférica é uma vantagem conceitual, mas não
  torna o Dunn imune a ruído estatístico em amostra finita.
- ✔ É o mesmo tipo de tensão entre critério agregado (média) e critério
  de pior-caso, presente também em métricas supervisionadas
  (acurácia média vs. pior recall entre classes).

### Pausa 6 — Um teste não rejeitar não é "sem discrepância nenhuma"

A pausa final fecha o círculo da aula: nenhuma ferramenta de validação,
sozinha e numa única configuração, é definitiva. O MMD com largura de
banda da mediana não rejeitar para as duas luas não significa "sem
discrepância" — significa "sem discrepância **na escala que essa
configuração consegue enxergar**". Testar em mais de uma escala (ou
usar mais de uma ferramenta, como o KS via projeções) é a prática
cuidadosa que a aula modela.

- ✔ Não é falha do MMD como família de teste — é a largura de banda
  específica que estava insensível àquela escala; $4\gamma$ revelou a
  mesma diferença sem trocar de teste.
- ✗ KS via projeções e MMD capturam discrepâncias por caminhos
  diferentes; a aula usou os dois porque um pode pegar algo que o
  outro não pega.
- ✔ Um PPC quantitativo honesto não deveria reportar um único teste
  com uma única configuração sem justificar a escolha, sobretudo de
  largura de banda.
- ✔ A largura de banda $h$ do KDE (Aula 2) tem o mesmo papel — a mesma
  tensão de escala revisitada aqui.
