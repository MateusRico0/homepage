## Resumo — Aula 3: Projeções Ortogonais e Subespaços

A Aula 2 terminou com um problema propositalmente sem resposta: o
sistema $X\mathbf{w}=\mathbf{y}$ da Regressão Linear Múltipla é, em
praticamente todo problema real ($N\gg d$), sobredeterminado —
genericamente sem solução exata. Esta aula responde "qual é a melhor
aproximação possível", com uma ideia geométrica, não algorítmica: entre
todos os $\mathbf{w}$ possíveis, o melhor é aquele cujo $X\mathbf{w}$
fica o mais **próximo** possível de $\mathbf{y}$ — e "mais próximo"
tem uma resposta exata quando o candidato é obrigado a viver dentro de
um subespaço (o espaço-coluna de $X$, já nomeado na Aula 2). Essa
resposta é a **projeção ortogonal**, e o mecanismo que a calcula são as
**Equações Normais**, $X^TX\hat{\mathbf{w}} = X^T\mathbf{y}$ — o
fechamento algébrico da Regressão Linear Múltipla, e a peça que faltava
desde a Aula 1.

**Pré-requisitos:** Aula 2 completa — em particular, a Leitura 2 de
$A\mathbf{x}$ (combinação linear das colunas), o espaço-coluna como o
conjunto de tudo que $A\mathbf{x}$ alcança, o critério de solvabilidade
$\text{rk}(A)=\text{rk}(A|\mathbf{b})$, e o exemplo real de
multicolinearidade (exata e quase-exata) em `AveRooms`/`AveBedrms`.

**Estratégia Pedagógica:** Estratégia B (Inside-Out com Problema-Fio)
— aula de fundação matemática de representação/geometria (projeções,
subespaços), guiada pela necessidade do idioma matemático que a Aula 2
deixou em aberto, não por um modelo/algoritmo específico a desmontar.

**Dataset-fio:** California Housing (o mesmo das Aulas 1–2) — o mesmo
subconjunto de 4 atributos (`MedInc`, `HouseAge`, `AveRooms`,
`AveBedrms`) e o mesmo par quase-colinear (`AveRooms`/`AveBedrms`,
correlação $0{,}865$), agora usado para calcular o $\hat{\mathbf{w}}$
de verdade via projeção, não só para diagnosticar se ele existiria.

## Plano de aula — Aula 3 (carga horária: ~100min)

1. **Abertura — O Problema Que a Aula 2 Deixou em Aberto** (~12 min)
   — Organizador prévio/revisão rápida: $X\mathbf{w}=\mathbf{y}$
   sobredeterminado, sem solução exata, para o subconjunto real de
   California Housing. Roteiro explícito: (i) o que significa
   geometricamente "a melhor aproximação possível"; (ii) o que é
   projetar um vetor sobre um subespaço, e por que isso resolve o
   problema; (iii) como isso vira uma fórmula calculável (Equações
   Normais); (iv) quando essa fórmula falha, e por quê. Problema
   motivador: perguntar, sem resolver, "se $X\mathbf{w}$ nunca alcança
   $\mathbf{y}$ exatamente, qual $X\mathbf{w}$ alcançável está mais
   perto?" — discussão. Pausa ativa fechando o bloco.

2. **Intuição — Sombra no Chão, Não no Ar** (~10 min) — Preview
   geométrico concreto em $\mathbb{R}^2$/$\mathbb{R}^3$, antes de
   qualquer álgebra: projetar um ponto sobre uma reta e sobre um plano
   — a "sombra" do ponto quando a luz vem perpendicular ao subespaço.
   Visualizar que a menor distância do ponto ao subespaço é sempre
   alcançada nessa sombra, nunca em outro ponto do subespaço — e que o
   segmento (ponto → sombra) é perpendicular ao subespaço. Isso já
   entrega a ideia geométrica inteira; falta generalizar para
   $\mathbb{R}^d$ e nomear os passos.

3. **Subespaços e Complemento Ortogonal** (~12 min) — Recuperar
   rapidamente subespaço (Aula 1) e espaço-coluna (Aula 2). Definir o
   **complemento ortogonal** $U^\perp = \{\mathbf{v} :
   \mathbf{v}^T\mathbf{u}=0 \ \forall \mathbf{u}\in U\}$; o resultado
   citado de que $\mathbb{R}^N = U \oplus U^\perp$ para qualquer
   subespaço $U$ — todo vetor se decompõe de forma única numa parte
   dentro de $U$ e outra dentro de $U^\perp$.

4. **O Teorema da Projeção: Premissas e Passo a Passo** (~20 min) — O
   bloco central. Premissas: um subespaço $U=\text{col}(X)$, um vetor
   $\mathbf{y}$ fora dele. Passo a passo: (i) definir $\hat{\mathbf{y}}$
   como o ponto de $U$ mais próximo de $\mathbf{y}$ (menor
   $\|\mathbf{y}-\hat{\mathbf{y}}\|$); (ii) provar que essa condição de
   mínimo é equivalente a $(\mathbf{y}-\hat{\mathbf{y}})\perp U$ (o
   resíduo é ortogonal a todo o subespaço); (iii) escrever
   $\hat{\mathbf{y}}=X\hat{\mathbf{w}}$ (todo ponto de $U$ é uma
   combinação das colunas de $X$ — Leitura 2 da Aula 2) e usar a
   ortogonalidade coluna a coluna, $X^T(\mathbf{y}-X\hat{\mathbf{w}})=
   \mathbf{0}$; (iv) isolar $\hat{\mathbf{w}}$, chegando nas
   **Equações Normais** $X^TX\hat{\mathbf{w}}=X^T\mathbf{y}$ e, quando
   $X^TX$ é invertível, $\hat{\mathbf{w}}=(X^TX)^{-1}X^T\mathbf{y}$.

5. **Aplicação e Verificação no Dado Real** (~15 min) — Calcular
   $\hat{\mathbf{w}}$ para o California Housing pela fórmula fechada;
   comparar com um solver de referência (`numpy.linalg.lstsq`) como
   conferência independente; verificar numericamente que o resíduo
   $\mathbf{y}-X\hat{\mathbf{w}}$ é (aproximadamente) ortogonal a cada
   coluna de $X$ — a promessa do Passo (iii) do bloco anterior,
   checável com números reais.

6. **Quando a Fórmula Falha, ou Fica Frágil** (~13 min) — Conectar de
   volta à Aula 2: $X^TX$ é invertível se, e somente se, $X$ tem posto
   completo (Bloco 5 da Aula 2). Com a coluna exatamente duplicada
   (`2×AveRooms`, já fabricada na Aula 2), $X^TX$ deixa de ser
   invertível — $\hat{\mathbf{y}}$ continua único (é a mesma sombra),
   mas $\hat{\mathbf{w}}$ deixa de ser único. Com quase-multicolinearidade
   real (`AveRooms`/`AveBedrms`, $r=0{,}865$), $X^TX$ é tecnicamente
   invertível mas mal-condicionada — reaproveitar a instabilidade
   numérica já demonstrada na Aula 2 (perturbação de 1% em
   `MedHouseVal` girando o peso de `AveBedrms` em ~30%), agora
   explicada como sintoma de $X^TX$ quase-singular.

7. **Fechamento e Ponte para a Aula 4** (~10 min) — Retomar as quatro
   perguntas da abertura. O que fica em aberto: calcular
   $(X^TX)^{-1}$ diretamente é a forma mais simples de descrever a
   solução, mas não a mais estável numericamente quando $X^TX$ está
   mal-condicionada — a Aula 4 (autovalores, autovetores) dá a
   ferramenta exata para medir esse mal-condicionamento (número de
   condição) e motiva os métodos numéricos mais estáveis (QR, SVD) que
   o curso usa depois.
