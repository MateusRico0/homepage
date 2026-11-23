# Respostas e Guia Docente — Pausas da Aula 12

Respostas das quatro Pausas da **Aula 12: Fundamentos do Aprendizado de Representação Contrastivo**, com um roteiro de tempo para a aula de 1 hora.

## Roteiro de tempo (60 min)

| Seção | Tempo | Ponto a fixar |
| :--- | :---: | :--- |
| Revisão e Introdução | 6 min | Variância $\neq$ semântica: PCA/AE gastam capacidade no *nuisance*; contraste aprende invariância sem rótulos |
| Bloco 1 (com Pausa 1) | 14 min | Invariância pura colapsa para constante; InfoNCE = classificação $(K+1)$-ária entre 1 positivo e $K$ negativos |
| Bloco 2 (com Pausa 2) | 16 min | Crítico ótimo estima $\ln\frac{p(\mathbf{x}'\mid\mathbf{x})}{p(\mathbf{x}')}$; $I(\mathbf{x};\mathbf{x}^+)\ge \ln(K+1)-\mathcal{L}_{\text{InfoNCE}}$ |
| Bloco 3 (com Pausa 3) | 12 min | Na hiperesfera $\mathbb{S}^{M-1}$: alinhamento (positivos juntos) + uniformidade (kernel Gaussiano); papel de $\tau$ |
| Bloco 4 (com Pausa 4) | 9 min | Cabeça de projeção $g_{\boldsymbol\psi}$ protege $\mathbf{h}$; aumentações definem o que é *nuisance* (InfoMin) |
| Fechamento | 3 min | Quadro comparativo (PCA/AE vs VAE vs InfoNCE) e síntese das 12 aulas |

**Se faltar tempo:** nos slides, pular a passagem intermediária da Lei dos Grandes Números na cota de MI (está completa nas notas) e os itens V/F das Pausas 3 e 4 (manter apenas a pergunta aberta).

---

## Pausa 1: Invariância, Colapso e InfoNCE

### Pergunta aberta
Com um lote de tamanho $B = 64$, geramos $2B = 128$ visões. Para cada visão âncora, há $1$ visão positiva (a outra aumentação da mesma imagem) e $K = 2B - 2 = 126$ visões negativas (as duas visões de cada uma das outras $63$ imagens). Se um codificador mapeasse todas as imagens para o mesmo vetor constante $\mathbf{z}(\mathbf{x}) \equiv \mathbf{c}$ com $\|\mathbf{c}\|_2 = 1$, todas as similaridades cosseno valeriam $1$. A perda de alinhamento pura seria $0$, mas a InfoNCE valeria:
$$\mathcal{L}_{\text{InfoNCE}} = -\ln \frac{\exp(1/\tau)}{\exp(1/\tau) + 126\,\exp(1/\tau)} = \ln(127) \approx 4{,}84,$$
que é exatamente o valor de um chute aleatório entre $127$ opções — portanto o codificador constante não minimiza a InfoNCE.

*Condução:* pedir primeiro quantos negativos existem para cada âncora no lote ($2B-2$, não $B-1$), e só depois substituir na fórmula com $\text{sim}=1$.

### V/F — Colapso e Formulação Contrastiva
- **(1) Falso.** A MSE de reconstrução em PCA/AE prioriza as direções de maior variância; se a maior variância for ruído de fundo ou iluminação (*nuisance*), a representação descarta o sinal semântico de baixa variância.
- **(2) Verdadeiro.** Sem termo repulsivo (ou restrição arquitetural/estatística), uma função constante $\mathbf{z}(\mathbf{x})=\mathbf{c}$ zera $\mathbb{E}[\|\mathbf{z}(\mathbf{x})-\mathbf{z}(\mathbf{x}^+)\|^2]$.
- **(3) Falso.** No lote do SimCLR, as demais imagens podem por acaso pertencer à mesma classe semântica (falsos negativos), pois o algoritmo não usa rótulos.
- **(4) Verdadeiro.** A perda InfoNCE tem exatamente a forma da entropia cruzada de um classificador $(K+1)$-ário que deve apontar qual candidato é o par positivo.

---

## Pausa 2: Razão de Densidades e Informação Mútua

### Pergunta aberta
Não é possível garantir que o modelo atingiu a Informação Mútua real quando $\mathcal{L}_{\text{InfoNCE}} \approx 0{,}01$ com $K = 15$. A cota garante apenas que $I(\mathbf{x};\mathbf{x}^+) \ge \ln(16) - 0{,}01 \approx 2{,}77 - 0{,}01 = 2{,}76$ nats. Como $\mathcal{L}_{\text{InfoNCE}} \ge 0$, a estimativa da InfoNCE nunca pode ultrapassar $\ln(K+1) \approx 2{,}77$ nats, mesmo que a Informação Mútua verdadeira seja $10$ nats: a cota está saturada pelo número pequeno de negativos $K$. Para distinguir valores mais altos de $I(\mathbf{x};\mathbf{x}^+)$, é preciso aumentar $K$.

*Condução:* pedir aos alunos que calculem $\ln(15+1) \approx 2{,}77$ antes de interpretar o $0{,}01$.

### V/F — Razão de Densidades e Cota de MI
- **(1) Verdadeiro.** Quando $X$ e $Y$ são independentes, $p(x,y) = p(x)p(y)$, logo $\mathrm{KL}(p(x,y)\|p(x)p(y)) = 0$.
- **(2) Falso.** O ótimo de Bayes estima a razão de densidades $\frac{p(\mathbf{x}'\mid \mathbf{x})}{p(\mathbf{x}')}$ (a menos de uma constante multiplicativa em $\mathbf{x}'$), que é a informação mútua pontual exponenciada — não a densidade $p(\mathbf{x})$ isolada.
- **(3) Verdadeiro.** Se $I(\mathbf{x};\mathbf{x}^+) > \ln(K+1)$, a cota $\ln(K+1) - \mathcal{L}_{\text{InfoNCE}}$ é frouxa mesmo no ótimo global, pois $\mathcal{L}_{\text{InfoNCE}} \ge 0$.
- **(4) Falso.** $I(\mathbf{x};\mathbf{x}^+)$ depende apenas da distribuição conjunta das duas visões; com aumentações fortes demais que destroem o objeto compartilhado, $I(\mathbf{x};\mathbf{x}^+)$ cai para perto de zero.

---

## Pausa 3: Geometria na Hiperesfera e Temperatura

### Pergunta aberta
Com $\tau$ muito pequeno (ex. $\tau = 0{,}02$), o gradiente da *softmax* concentra quase todo o peso nos negativos mais próximos da âncora (*hard negatives*). Isso força o codificador a empurrar esses pontos para longe, maximizando a uniformidade local, mas também empurra para longe amostras que pertencem à **mesma classe** (falsos negativos no lote), fragmentando os agrupamentos semânticos na hiperesfera — o chamado dilema *uniformidade-tolerância* (Wang & Liu, 2021). Por isso, um $\tau$ intermediário (como $0{,}2$) equilibra melhor a separação entre classes e a coesão intraclasse.

*Condução:* relacionar com a curva empírica de `load_digits` vista no bloco: $\tau=0{,}02$ perde acurácia no *linear probe* em $\mathbf{z}$ mesmo tendo perda baixa.

### V/F — Alinhamento, Uniformidade e Temperatura
- **(1) Falso.** Sem normalização $\ell_2$, o modelo pode aumentar $\|\mathbf{z}\|$ arbitrariamente para reduzir a perda via escala dos *logits*, sem melhorar a separação angular entre classes.
- **(2) Verdadeiro.** No limite $K \to \infty$, o termo repulsivo converge para $\ln \mathbb{E}_{\mathbf{x},\mathbf{x}'}[\exp(-2\|\mathbf{z}(\mathbf{x})-\mathbf{z}(\mathbf{x}')\|^2)]$, que é o logaritmo da média do kernel Gaussiano na esfera — minimizado pela distribuição uniforme na hiperesfera.
- **(3) Falso.** Quando $\tau$ aumenta, os pesos da *softmax* ficam mais próximos de $1/K$, suavizando a penalização sobre negativos difíceis e reduzindo a força repulsiva local.
- **(4) Verdadeiro.** Como $\mathbf{z}_1, \mathbf{z}_2 \in \mathbb{S}^{M-1}$, vale $\|\mathbf{z}_1 - \mathbf{z}_2\|^2 = 2 - 2\mathbf{z}_1^T\mathbf{z}_2$, relação linear decrescente com a similaridade cosseno.

---

## Pausa 4: Arquitetura, Aumentações e Prática

### Pergunta aberta
Se escolhermos apenas ruído gaussiano mínimo ($\sigma = 0{,}01$), as duas visões são quase idênticas: o codificador consegue identificar o par positivo comparando detalhes superficiais ou ruído de fundo sem precisar extrair a forma do dígito (*atalho* / *shortcut*), e $I(\mathbf{v}_1;\mathbf{v}_2)$ fica alta às custas de informação irrelevante. Já se escolhermos corte/apagamento extremo ($p = 0{,}95$), quase todo o dígito desaparece em ambas as visões, destruindo a informação semântica compartilhada ($I(\mathbf{v}_1;\mathbf{v}_2) \to 0$). Pelo princípio **InfoMin** (Tian et al., 2020), boas aumentações preservam apenas a informação necessária para a tarefa alvo e descartam todo o resto.

### V/F — Cabeça de Projeção, Aumentações e *Linear Probe*
- **(1) Verdadeiro.** A cabeça $\mathbf{g}_{\boldsymbol\psi}$ absorve a invariância estrita exigida pela InfoNCE em $\mathbf{z}$, permitindo que $\mathbf{h}$ retenha atributos úteis (como brilho, espessura ou orientação) para tarefas *downstream*.
- **(2) Falso.** A avaliação por *linear probe* congela os pesos de $\mathbf{f}_{\boldsymbol\phi}$ e treina apenas uma camada linear (como regressão logística) sobre $\mathbf{h}$ usando rótulos de teste/validação, justamente para medir a separabilidade linear já presente em $\mathbf{h}$.
- **(3) Falso.** Aumentações extremas destroem o conteúdo semântico compartilhado entre as duas visões ($I(\mathbf{v}_1;\mathbf{v}_2)\to 0$).
- **(4) Verdadeiro.** Com visões quase idênticas, estatísticas triviais de pixels ou fundo já bastam para identificar o par positivo (*shortcuts*).
