# Respostas das Pausas Ativas — Aula 08

## Pausa Ativa 1: O Dilema da Projeção 2D

### Pergunta Aberta
**Pergunta:** Se tivermos 4 pontos mutuamente equidistantes em $\mathbb{R}^3$ (os vértices de um tetraedro regular), é geometricamente possível posicioná-los em um plano $\mathbb{R}^2$ de modo que as 6 distâncias entre pares permaneçam exatamente iguais? O que isso nos diz sobre tentar projetar dados de 30 ou 784 dimensões em um gráfico 2D?

**Discussão e Condução:**
No plano $\mathbb{R}^2$, o número máximo de pontos mutuamente equidistantes é 3 (um triângulo equilátero). O quarto ponto teria de estar equidistante dos três vértices, o que só é possível no baricentro do triângulo; porém, a distância do baricentro aos vértices no plano é menor ($1/\sqrt{3} \approx 0{,}577$) do que o lado do triângulo ($1$). Logo, é matematicamente impossível preservar todas as distâncias euclidianas de um espaço dimensional maior em um espaço menor.
Em dimensões como $D=30$ ou $D=784$, podemos ter até $D+1$ pontos mutuamente equidistantes (um simplex regular). Ao forçar esses pontos em 2D, qualquer método que tente preservar distâncias globais será obrigado a distorcer drasticamente as relações. Isso nos obriga a fazer uma escolha de projeto: ou preservamos algumas distâncias privilegiadas (como as locais, de vizinhança) ou sacrificamos a resolução de tudo ao tentar agradar a todas as distâncias simultaneamente.

### Bloco V/F
1. **Afirmação:** Em qualquer espaço métrico euclidiano de dimensão $d$, o número máximo de pontos mutuamente equidistantes é $d+1$.
   - **Gabarito: V**.
   - **Justificativa:** Trata-se do simplex regular de dimensão $d$ (em 1D são 2 pontos; em 2D, 3 pontos de um triângulo equilátero; em 3D, 4 vértices do tetraedro; em dimensão $d$, $d+1$ vértices).
2. **Afirmação:** A PCA em 2 componentes preserva perfeitamente as distâncias de vizinhança local entre pontos próximos, pois maximiza a variância total projetada.
   - **Gabarito: F**.
   - **Justificativa:** A PCA busca os eixos de maior dispersão global; ao projetar em 2D, pares de pontos que estavam distantes no espaço original em dimensões ortogonais ao subespaço principal podem ser projetados exatamente sobrepostos, colapsando vizinhanças.
3. **Afirmação:** Quando reduzimos a dimensionalidade de $D$ para $d \ll D$, a perda de informação geométrica é inevitável a menos que todos os pontos estejam contidos em uma variedade linear ou afim de dimensão no máximo $d$.
   - **Gabarito: V**.
   - **Justificativa:** Pela própria geometria euclidiana, se a dimensão intrínseca dos dados for estritamente maior que $d$, distâncias serão distorcidas ou projeções se sobreporão.
4. **Afirmação:** O objetivo principal de técnicas de visualização em 2D (como t-SNE) é permitir a reconstrução precisa dos atributos originais $\mathbf{x} \in \mathbb{R}^D$ a partir das coordenadas $\mathbf{y} \in \mathbb{R}^2$.
   - **Gabarito: F**.
   - **Justificativa:** O objetivo do t-SNE é estritamente a exploração visual da estrutura de vizinhanças e agrupamentos; ele não é um modelo de reconstrução (não possui decodificador nem inverso paramétrico).

---

## Pausa Ativa 2: MDS e o Critério de Stress

### Pergunta Aberta
**Pergunta:** A função de custo *Stress* do MDS calcula a soma dos quadrados das diferenças entre as distâncias originais e as distâncias no mapa: $\sum_{i<j} (d_{ij}(X) - d_{ij}(Y))^2$. Se um par de pontos distantes tiver erro de $10$ unidades e dez pares de pontos vizinhos próximos tiverem cada um erro de $2$ unidades, qual erro contribuirá mais para a perda do MDS? Que consequência isso traz para a visualização de clusters?

**Discussão e Condução:**
O par distante contribui com $(10)^2 = 100$. Os dez pares próximos contribuem com $10 \times (2)^2 = 40$. Mesmo havendo dez vezes mais pares locais sofrendo distorção, o erro do par distante domina o custo.
Consequência: o MDS gasta quase todo o seu "orçamento" de otimização tentando manter as distâncias entre pontos e aglomerados distantes aproximadamente corretas. Em contrapartida, permite que distâncias pequenas (que definem se dois pontos pertencem ou não ao mesmo subgrupo ou cluster) sejam esmagadas e misturadas, resultando frequentemente em aglomerados fundidos no centro da projeção.

### Bloco V/F
1. **Afirmação:** O MDS clássico aplicado a distâncias euclidianas fornece uma configuração 2D matematicamente idêntica à projeção nos dois primeiros componentes principais da PCA.
   - **Gabarito: V**.
   - **Justificativa:** Pelo teorema de Young-Householder e Torgerson, o MDS clássico baseado em centralização dupla da matriz de produtos internos $X X^T$ equivale exatamente à decomposição espectral que recupera os scores da PCA.
2. **Afirmação:** No MDS com função *Stress* quadrática, errar a distância entre dois pontos distantes de $100$ para $90$ gera exatamente a mesma penalidade que errar a distância entre dois vizinhos de $11$ para $1$.
   - **Gabarito: V**.
   - **Justificativa:** Ambos os desvios absolutos são de $|100-90| = 10$ e $|1-11| = 10$. Ao quadrado, ambos contribuem com $(10)^2 = 100$, ignorando o fato de que um erro relativo de $10$ sobre $1$ destrói completamente a vizinhança local, enquanto sobre $100$ é apenas uma variação de 10%.
3. **Afirmação:** O MDS exige acesso explícito à matriz de coordenadas $\mathbf{X}$; ele não pode ser aplicado se tivermos apenas uma matriz de dissimilaridades arbitrárias entre pares.
   - **Gabarito: F**.
   - **Justificativa:** O MDS (especialmente o MDS não métrico ou generalizado) opera diretamente sobre a matriz de distâncias/dissimilaridades $D_{N \times N}$, sem precisar conhecer as coordenadas originais.
4. **Afirmação:** Ao minimizar o *Stress*, o MDS tende a priorizar a preservação da estrutura de vizinhança local em detrimento das distâncias de longa escala.
   - **Gabarito: F**.
   - **Justificativa:** É o oposto: os termos quadráticos associados a distâncias grandes dominam a soma, sacrificando as distâncias pequenas.

---

## Pausa Ativa 3: Vizinhanças Probabilísticas e a Assimetria da KL

### Pergunta Aberta
**Pergunta:** A divergência de Kullback-Leibler usada no SNE é definida como $\mathrm{KL}(P \parallel Q) = \sum_{i \ne j} p_{ij} \ln \frac{p_{ij}}{q_{ij}}$. Analise o que acontece com a perda nos dois cenários:
(A) Dois pontos são vizinhos próximos em alta dimensão ($p_{ij} \approx 0{,}15$), mas são mapeados distantes no mapa 2D ($q_{ij} \approx 0{,}0001$).
(B) Dois pontos estão distantes em alta dimensão ($p_{ij} \approx 0{,}00001$), mas são mapeados perto no mapa 2D ($q_{ij} \approx 0{,}15$).
Qual dos dois cenários é severamente punido pelo algoritmo? O que isso implica para o mapa final?

**Discussão e Condução:**
No cenário (A), o termo $p_{ij} \ln(p_{ij}/q_{ij})$ vale $0{,}15 \times \ln(0{,}15 / 0{,}0001) = 0{,}15 \times \ln(1500) \approx 0{,}15 \times 7{,}31 = +1{,}097$ (uma penalidade enorme para um único par).
No cenário (B), o termo vale $0{,}00001 \times \ln(0{,}00001 / 0{,}15) = 0{,}00001 \times \ln(1/15000) \approx 0{,}00001 \times (-9{,}6) \approx -0{,}000096$ (praticamente zero na soma).
Implicação: a divergência $\mathrm{KL}(P \parallel Q)$ penaliza com força extrema a quebra de vizinhanças (falsos afastamentos). Se dois pontos eram vizinhos na alta dimensão, o algoritmo é forçado a colocá-los juntos no mapa. Por outro lado, ele é muito leniente com pontos distantes que acabam caindo moderadamente próximos no mapa, desde que isso ajude a manter os verdadeiros vizinhos coesos.

### Bloco V/F
1. **Afirmação:** A variância $\sigma_i^2$ do kernel gaussiano de cada ponto $\mathbf{x}_i$ no SNE é fixada com um valor universal único para todo o conjunto de dados.
   - **Gabarito: F**.
   - **Justificativa:** $\sigma_i^2$ é ajustada individualmente para cada ponto $\mathbf{x}_i$ via busca binária, de modo que a entropia da distribuição condicional $P_i$ satisfaça a Perplexidade pré-especificada ($\text{Perp} = 2^{H(P_i)}$).
2. **Afirmação:** Em regiões de alta densidade no espaço original, o valor de $\sigma_i$ encontrado pelo SNE para uma dada perplexidade fixa será menor do que em regiões esparsas.
   - **Gabarito: V**.
   - **Justificativa:** Como há muitos vizinhos acumulados perto de $\mathbf{x}_i$, um raio $\sigma_i$ pequeno já basta para englobar a massa de probabilidade requerida pela perplexidade.
3. **Afirmação:** A perda $\mathrm{KL}(P \parallel Q)$ penaliza com igual rigor o erro de afastar pontos que eram vizinhos e o erro de aproximar pontos que estavam distantes.
   - **Gabarito: F**.
   - **Justificativa:** A KL é estritamente assimétrica; quando $p_{ij} \approx 0$, o fator que multiplica o logaritmo anula o custo, tolerando aproximações espúrias.
4. **Afirmação:** A Perplexidade pode ser interpretada operacionalmente como o número efetivo de vizinhos próximos que cada ponto tenta acomodar em sua vizinhança probabilística.
   - **Gabarito: V**.
   - **Justificativa:** Por ser $2^{H(P_i)}$, para uma distribuição uniforme sobre $K$ vizinhos a entropia seria $\log_2 K$ e a perplexidade seria exatamente $K$.

---

## Pausa Ativa 4: O "Crowding Problem" e a Cauda Pesada de Student-$t$

### Pergunta Aberta
**Pergunta:** No SNE original, a distribuição de probabilidades no mapa 2D também usava um kernel gaussiano: $q_{ij} \propto \exp(-\|\mathbf{y}_i - \mathbf{y}_j\|^2)$. Por que essa escolha levava ao "crowding problem" (colapso de todos os agrupamentos no centro do mapa)? De que forma trocar a Gaussiana pela distribuição $t$-Student ($1$ grau de liberdade) alivia a pressão e cria espaço no mapa?

**Discussão e Condução:**
Em alta dimensão, o volume de uma esfera de raio $r$ escala como $r^D$. Em torno de um ponto $\mathbf{x}_i$, cabem muitos pontos a uma distância moderada $r$ que não são vizinhos imediatos, mas têm probabilidades $p_{ij}$ não nulas. Em 2D, o volume escala apenas com $r^2$.
Se usarmos uma Gaussiana tanto no espaço original quanto no mapa 2D, para reproduzir a mesma probabilidade $q_{ij} = p_{ij}$, a distância $\|\mathbf{y}_i - \mathbf{y}_j\|$ teria de ser proporcional à distância original. Como o plano 2D não possui área suficiente para acomodar tantos pontos a distâncias moderadas, a atração mútua de centenas de pares distantes soma uma força resultante enorme que empurra todos os pontos para o centro do mapa.
A distribuição $t$-Student ($1$ grau de liberdade) decresce muito mais lentamente que a Gaussiana para distâncias moderadas e longas ($1/(1+d^2)$ contra $\exp(-d^2)$). Logo, para gerar uma probabilidade $q_{ij}$ pequena ou moderada, os pontos $\mathbf{y}_i$ e $\mathbf{y}_j$ podem ficar **muito mais afastados** no mapa 2D sem sofrer penalidade. Isso "empurra" os clusters não relacionados para longe uns dos outros, abrindo espaço no mapa para que cada cluster organize internamente seus verdadeiros vizinhos.

### Bloco V/F
1. **Afirmação:** A distribuição $t$-Student com $1$ grau de liberdade coincide matematicamente com a distribuição de Cauchy padrão.
   - **Gabarito: V**.
   - **Justificativa:** A densidade da $t$-Student com $\nu=1$ é $f(t) \propto (1 + t^2)^{-1}$, que é exatamente o núcleo da distribuição de Cauchy.
2. **Afirmação:** Para distâncias $d = \|\mathbf{y}_i - \mathbf{y}_j\| \gg 1$, a probabilidade não normalizada sob o kernel do t-SNE decai com $1/d^2$, enquanto sob um kernel gaussiano ela decai exponencialmente com $\exp(-d^2)$.
   - **Gabarito: V**.
   - **Justificativa:** $(1 + d^2)^{-1} \approx d^{-2}$ para $d$ grande, o que confere caudas pesadas (lei de potência) em vez de decaimento subgaussiano super-rápido.
3. **Afirmação:** O t-SNE usa a distribuição $t$-Student tanto no espaço de alta dimensão ($p_{ij}$) quanto no espaço de baixa dimensão ($q_{ij}$).
   - **Gabarito: F**.
   - **Justificativa:** O espaço de alta dimensão utiliza o kernel gaussiano para definir $p_{ij}$; a distribuição $t$-Student é usada **apenas** no espaço de baixa dimensão (mapa 2D/3D) para definir $q_{ij}$.
4. **Afirmação:** O gradiente da perda do t-SNE pode ser interpretado como um balanço entre forças de atração ao longo das arestas de vizinhos ($p_{ij}$) e forças de repulsão entre todos os pares de pontos ($q_{ij}$).
   - **Gabarito: V**.
   - **Justificativa:** O gradiente $\frac{\partial C}{\partial \mathbf{y}_i} = 4 \sum_j (p_{ij} - q_{ij}) q_{ij}^{\text{sem norm}} (\mathbf{y}_i - \mathbf{y}_j)$ decompõe-se exatamente em atração quando $p_{ij} > q_{ij}$ e repulsão quando $q_{ij} > p_{ij}$.

---

## Pausa Ativa 5: As 4 Armadilhas de Interpretação do t-SNE

### Pergunta Aberta
**Pergunta:** Um pesquisador roda o t-SNE em um conjunto de dados genômicos e observa no gráfico 2D dois agrupamentos: o Cluster A tem diâmetro visual de $4\text{ cm}$ e o Cluster B tem diâmetro de $1\text{ cm}$. A distância visual entre os dois clusters no gráfico é de $15\text{ cm}$. Ele conclui: "O Cluster A é quatro vezes mais disperso que o Cluster B, e ambos são geneticamente muito distantes". Essa conclusão é fundamentada? Quais são os erros conceituais cometidos?

**Discussão e Condução:**
A conclusão é completamente equivocada e incorre em duas das clássicas armadilhas do t-SNE:
1. **Falácia do tamanho/dispersão relativa:** O t-SNE calibra a variância $\sigma_i^2$ localmente em cada ponto de acordo com a densidade via perplexidade. Regiões muito densas em alta dimensão são "infladas" para acomodar seus vizinhos no mapa, enquanto regiões esparsas são contraídas. A área ocupada por um cluster no mapa 2D não reflete a sua variância original em alta dimensão.
2. **Falácia da distância entre clusters:** A força de atração do t-SNE só opera quando $p_{ij} > 0$. Para pares de clusters distantes no espaço original, $p_{ij} \approx 0$ para todos os pontos cruzados. Uma vez que os clusters se separam no mapa, a única força que atua entre eles é a repulsão global uniforme de $q_{ij}$. Assim, se a distância visual é $5\text{ cm}$, $15\text{ cm}$ ou $30\text{ cm}$, isso é determinado pela dinâmica aleatória da otimização e repulsão eletrostática no plano, não pela distância euclidiana real entre as duas subpopulações no espaço original.

### Bloco V/F
1. **Afirmação:** Se executarmos o t-SNE com perplexidade extremamente baixa (ex.: $\text{Perp} = 2$) em dados com agrupamentos reais, o algoritmo tenderá a fragmentar os clusters em dezenas de pequenos subgrupos artificiais desconexos.
   - **Gabarito: V**.
   - **Justificativa:** Com perplexidade 2, cada ponto só tenta manter contato com seus 1 ou 2 vizinhos imediatos, quebrando a coesão global dos clusters em ilhas lineares ou pares isolados.
2. **Afirmação:** Dado um novo ponto de teste $\mathbf{x}_{\text{novo}} \in \mathbb{R}^D$, podemos projetá-lo no mapa 2D do t-SNE aplicando diretamente uma função matemática explícita $\mathbf{y}_{\text{novo}} = f(\mathbf{x}_{\text{novo}})$.
   - **Gabarito: F**.
   - **Justificativa:** O t-SNE padrão é um método não paramétrico baseado em otimização direta das posições $\mathbf{y}_1, \dots, \mathbf{y}_N$; ele não aprende uma função de mapeamento indutivo $\mathbb{R}^D \to \mathbb{R}^2$.
3. **Afirmação:** Ao rodar o t-SNE sobre ruído branco puramente gaussiano e uniforme sem qualquer estrutura de agrupamento, é garantido que o mapa 2D exibirá uma nuvem homogênea e jamais formará agrupamentos visíveis.
   - **Gabarito: F**.
   - **Justificativa:** Flutuações estocásticas em amostras finitas combinadas com perplexidades intermediárias/baixas podem fazer o t-SNE agrupar pontos aleatórios e criar aglomerados aparentes totalmente espúrios.
4. **Afirmação:** Executar o t-SNE múltiplas vezes com sementes aleatórias distintas ou inicializações diferentes pode gerar configurações rotacionadas, espelhadas ou com posições relativas de clusters alteradas, embora as vizinhanças locais sejam preservadas.
   - **Gabarito: V**.
   - **Justificativa:** A função de custo da divergência KL sobre coordenadas é altamente não convexa e invariante a rotações e translações globais, além de possuir múltiplos mínimos locais equivalentes em termos de vizinhanças.
