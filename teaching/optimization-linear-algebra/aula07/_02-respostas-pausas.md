# Respostas das Pausas Ativas — Aula 7

Discussão das perguntas abertas e resolução dos itens de Verdadeiro/Falso das Pausas Ativas da Aula 7 (Convexidade e a Hessiana). Arquivo de apoio docente, não publicado.

---

## Pausa Ativa 1 — Coeficientes que Empatam

### Discussão da pergunta aberta
Nenhum dos $\boldsymbol\beta^\star+t\mathbf{n}$, com $\mathbf{n}=(0,0,-1,1,1)$, é "o certo" do ponto de vista dos dados. A perda só depende de $X_5\boldsymbol\beta$, e $X_5\mathbf{n}=\mathbf{0}$, então todos dão as mesmas predições e a mesma perda. A leitura usual de um coeficiente ("um quarto a mais, mantidas as demais colunas fixas") perde o sentido: com `AveOtherRooms = AveRooms − AveBedrms`, não dá para mudar `AveBedrms` e manter as outras duas fixas. O que os dados determinam é a combinação $X_5\boldsymbol\beta$, não os coeficientes individuais. Escolher um dos $\boldsymbol\beta$ exige um critério externo à perda, que é o que a Ridge faz no Bloco 4.

### Resolução dos itens
- ✗ **Item 1 (Falso):** gradiente nulo caracteriza pontos críticos, que incluem máximos e selas (por exemplo, $f(x_1,x_2)=x_1^2-x_2^2$ na origem). Concluir que é mínimo exige convexidade (Bloco 1) ou informação de segunda ordem (Bloco 2).
- ✔ **Item 2 (Verdadeiro):** as duas colunas são proporcionais, então existe $\mathbf{n}\ne\mathbf{0}$ com $X\mathbf{n}=\mathbf{0}$, e os minimizadores formam $\boldsymbol\beta^\star+\mathcal{N}(X)$. Como $X(\boldsymbol\beta^\star+\mathbf{v})=X\boldsymbol\beta^\star$ para $\mathbf{v}\in\mathcal{N}(X)$, as predições coincidem.
- ✗ **Item 3 (Falso):** em ponto flutuante, uma matriz singular raramente produz um pivô exatamente nulo. O arredondamento a torna "invertível" com número de condição da ordem de $10^{17}$, e o solver devolve uma das infinitas soluções, escolhida pelo ruído numérico.
- ✗ **Item 4 (Falso):** uma coluna que é combinação linear das outras não muda o espaço-coluna $\mathcal{C}(X)$. A perda mínima é a distância de $\mathbf{y}$ a $\mathcal{C}(X)$ (projeção, Aula 3), logo não muda.

---

## Pausa Ativa 2 — Dois Minimizadores?

### Discussão da pergunta aberta
Pode. Sejam $\mathbf{a}\ne\mathbf{b}$ minimizadores globais, com valor mínimo $m$. Para qualquer $\theta\in[0,1]$, a convexidade dá
$$f(\theta\mathbf{a}+(1-\theta)\mathbf{b})\le\theta m+(1-\theta)m=m,$$
e nenhum ponto do domínio tem valor abaixo de $m$. Logo todo o segmento $[\mathbf{a},\mathbf{b}]$ é formado por minimizadores, e o conjunto dos minimizadores é convexo (é o fundo do vale plano da Intuição). O que impede dois minimizadores é a convexidade **estrita**: com ela, o ponto médio teria valor $<m$, uma contradição. Esse é o lema de unicidade usado na Ridge (Bloco 4).

### Resolução dos itens
- ✔ **Item 1 (Verdadeiro):** para $f(\mathbf{x})=\mathbf{a}^T\mathbf{x}+b$, a desigualdade da definição vale com igualdade, logo vale para $f$ e para $-f$ (Boyd, §3.1.1, p. 67).
- ✗ **Item 2 (Falso):** se $\mathbf{x},\mathbf{y}\in\mathrm{dom}\,f$, os pontos $(\mathbf{x},f(\mathbf{x}))$ e $(\mathbf{y},f(\mathbf{y}))$ estão na epígrafe; a combinação convexa deles também está, e pertencer a $\mathrm{epi}\,f$ exige $\theta\mathbf{x}+(1-\theta)\mathbf{y}\in\mathrm{dom}\,f$. É o Passo 3 do sentido ($\Leftarrow$) do teorema da epígrafe.
- ✔ **Item 3 (Verdadeiro):** soma de convexas é convexa (Boyd, §3.2.1, p. 79); é por isso que perda quadrática mais penalidade $\lambda\|\boldsymbol\beta\|^2$ continua convexa.
- ✗ **Item 4 (Falso):** é o Corolário do bloco. Com $\nabla f(\mathbf{x}^\star)=\mathbf{0}$, a condição de primeira ordem dá $f(\mathbf{y})\ge f(\mathbf{x}^\star)$ para todo $\mathbf{y}$.

---

## Pausa Ativa 3 — Lendo a Hessiana num Ponto Crítico

### Discussão da pergunta aberta
Para a quadrática, $f(\mathbf{x}^\star+\varepsilon\mathbf{u}_i)=f(\mathbf{x}^\star)+\tfrac12\varepsilon^2\mathbf{u}_i^TP\mathbf{u}_i=f(\mathbf{x}^\star)+\tfrac12\lambda_i\varepsilon^2$. Ao longo de $\mathbf{u}_1$ ($\lambda_1=3$), $f$ sobe $\tfrac32\varepsilon^2$; ao longo de $\mathbf{u}_2$ ($\lambda_2=-1$), desce $\tfrac12\varepsilon^2$. O ponto crítico é uma **sela**: não é mínimo nem máximo, e o autovetor do autovalor negativo é uma direção de fuga. Para $f$ não quadrática, a expansão de Taylor de segunda ordem leva à mesma conclusão para $\varepsilon$ pequeno (teste da segunda derivada, citado sem prova na aula). Selas desse tipo são comuns em perdas de redes neurais, e um método que usa só o gradiente pode desacelerar perto delas.

### Resolução dos itens
- ✗ **Item 1 (Falso):** a condição de segunda ordem exige $\nabla^2f(\mathbf{x})\succeq0$ em **todo** ponto do domínio. Num único ponto, no máximo se conclui algo local. Por exemplo, $f(x)=x^4-2{,}5x^2$ tem $f''>0$ perto de $x=\pm1{,}1$ e não é convexa.
- ✔ **Item 2 (Verdadeiro):** é o contraexemplo do Boyd (§3.1.4, p. 71). Hessiana definida positiva em todo ponto é suficiente para convexidade estrita, mas não é necessária.
- ✔ **Item 3 (Verdadeiro):** $\nabla f(\mathbf{x})=\mathbf{x}^TP+\mathbf{q}^T$ (gradiente-linha, com $P$ simétrica), e derivar de novo dá $P$, sem dependência de $\mathbf{x}$.
- ✗ **Item 4 (Falso):** com derivadas segundas contínuas, vale a simetria $\partial^2f/\partial x_i\partial x_j=\partial^2f/\partial x_j\partial x_i$ (Schwarz; MathML, eq. 5.146). A Hessiana não depende da ordem.

---

## Pausa Ativa 4 — Curvatura Constante

### Discussão da pergunta aberta
Como $\nabla^2L=2X^TX$ não depende de $\boldsymbol\beta$, basta verificar $2X^TX\succeq0$ uma vez, e isso sempre vale, pois $\mathbf{v}^T(2X^TX)\mathbf{v}=2\|X\mathbf{v}\|^2\ge0$. A convexidade vale em todo $\mathbb{R}^d$ sem precisar olhar ponto a ponto. Numa rede com camadas ocultas, a saída depende dos pesos de forma não linear (produtos de pesos, ativações). A Hessiana passa a depender do ponto: pode ser PSD perto de um ponto e indefinida perto de outro. Verificar num ponto não diz nada sobre os outros, e em geral a perda não é convexa. Por isso redes profundas não herdam as garantias desta aula.

### Resolução dos itens
- ✔ **Item 1 (Verdadeiro):** $\mathbf{v}^T(2X^TX)\mathbf{v}=2\|X\mathbf{v}\|^2$, que é zero se, e somente se, $X\mathbf{v}=\mathbf{0}$.
- ✗ **Item 2 (Falso):** o que importa é o posto, não a forma da matriz. $X_5$ tem $N=16\,640$ linhas e 5 colunas, e $X_5^TX_5$ é singular porque uma coluna é combinação das outras.
- ✗ **Item 3 (Falso):** os minimizadores formam o conjunto **afim** $\boldsymbol\beta^\star+\mathcal{N}(X)$, uma translação do núcleo. Ele só contém $\mathbf{0}$ se $\mathbf{0}$ já for minimizador, isto é, se $X^T\mathbf{y}=\mathbf{0}$.
- ✔ **Item 4 (Verdadeiro):** com as camadas anteriores congeladas, as ativações da penúltima camada formam uma matriz fixa $H$. A perda $\|H\mathbf{w}-\mathbf{y}\|^2$ é uma perda quadrática nos pesos $\mathbf{w}$, com Hessiana $2H^TH\succeq0$.

---

## Pausa Ativa 5 — O Que a Ridge Escolhe

### Discussão da pergunta aberta
Não. Todos os $\boldsymbol\beta^\star+t\mathbf{n}$ dão as mesmas predições; os dados não os distinguem. A Ridge desempata com um critério nosso, o de menor $\|\boldsymbol\beta\|^2$. Esse critério ajuda na estabilidade numérica (autovalores $\ge\lambda$, número de condição limitado) e evita coeficientes enormes que se cancelam, mas não tem relação com o significado das colunas. Se as colunas fossem medidas em outras unidades, a solução Ridge mudaria. A convexidade estrita garante que o problema tem **uma** resposta; não garante que essa resposta tem significado causal.

### Resolução dos itens
- ✔ **Item 1 (Verdadeiro):** se $X^TX\mathbf{u}=\mu\mathbf{u}$, então $(X^TX+\lambda I)\mathbf{u}=(\mu+\lambda)\mathbf{u}$. Os autovetores são os mesmos e os autovalores são deslocados em $\lambda$.
- ✔ **Item 2 (Verdadeiro):** com $d>N$, $X^TX$ tem posto no máximo $N<d$ e é singular. Ainda assim, $X^TX+\lambda I$ tem autovalores $\ge\lambda>0$, logo a Hessiana $2(X^TX+\lambda I)\succ0$ e o minimizador existe e é único.
- ✗ **Item 3 (Falso):** a perda de treino não diminui com $\lambda$; ela aumenta ou fica igual. A Ridge troca ajuste de treino por norma menor, como mostra a tabela do Bloco 4. O minimizador da perda de treino sozinha é o caso $\lambda=0$.
- ✗ **Item 4 (Falso):** $|\beta_j|$ não é diferenciável em $\beta_j=0$ e, fora de $0$, tem segunda derivada nula. A penalidade $L_1$ continua convexa, mas não acrescenta curvatura: a Hessiana, onde existe, é a mesma da perda sem penalidade, e a unicidade não é garantida.
