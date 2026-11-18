# Respostas e Guia Docente — Pausas da Aula 11

Respostas das quatro Pausas da **Aula 11: Detecção de Drift e Alinhamento de Distribuições: Teste de Duas Amostras e MMD**, com um roteiro de tempo para a aula de 1 hora.

## Roteiro de tempo (60 min)

| Seção | Tempo | Ponto a fixar |
| :--- | :---: | :--- |
| Revisão e Introdução | 6 min | Sem rótulos em produção; decidir se $P=Q$ só com as leituras |
| As comparações mais simples | 5 min | Cada estatística simples detecta um tipo de mudança; nenhuma detecta o caso (d) |
| Intuição | 3 min | Testemunha: a função cujas médias mais diferem; a MMD é essa diferença |
| Bloco 1 (com Pausa 1) | 10 min | A permutação garante o nível para qualquer estatística; o poder vem da estatística |
| Bloco 2 (com Pausa 2) | 15 min | $\mathrm{MMD}^2=\mathbb{E}k(\mathbf{x},\mathbf{x}')-2\mathbb{E}k(\mathbf{x},\mathbf{y})+\mathbb{E}k(\mathbf{y},\mathbf{y}')$; testemunha = diferença de dois KDEs |
| Bloco 3 (com Pausa 3) | 10 min | Estimador não viesado pode ser negativo; a largura define a escala da comparação |
| Bloco 4 (com Pausa 4) | 9 min | A rejeição indica mudança em $p(\mathbf{x})$, não perda de acurácia; alinhar supõe proporção de classes igual |
| Fechamento | 3 min | Teste por classificador como ponte para a Aula 12 |

**Se faltar tempo:** pular o Passo 4 da demonstração do teorema do Bloco 2 (está nas notas), o slide do efeito da dimensão e os V/F das Pausas (fazer só a pergunta aberta). A demonstração completa do nível do teste de permutação está só nas notas; nos slides há a ideia em três passos.

---

## Pausa 1: Teste de Permutação

### Pergunta aberta
Com $B=19$ e nenhum valor permutado maior ou igual a $T_0$: $\hat p=(1+0)/(19+1)=0{,}05$. É possível rejeitar no nível $0{,}05$, e esse é o menor p-valor que $B=19$ produz. No nível $0{,}01$ não é possível rejeitar com esse $B$: é preciso $1/(B+1)\le0{,}01$, ou seja, $B\ge99$.

*Condução:* pedir a conta do p-valor primeiro e só depois perguntar pelo nível $0{,}01$. O objetivo é fixar que o número de permutações limita o menor p-valor.

### V/F — Nível, Poder e Permutação
- **(1) Falso.** A demonstração do nível não usa nenhuma propriedade de $T$. Uma estatística sem relação com os dados tem nível $\alpha$ e poder igual ao nível.
- **(2) Falso.** Mais permutações tornam o p-valor mais preciso, mas $T_0$ continua sendo um valor típico entre os permutados, porque no caso (d) as médias das duas distribuições são iguais. Falta poder à estatística.
- **(3) Falso.** Não rejeitar indica ausência de evidência com essa estatística e esse tamanho de amostra. O caso (d) também não foi rejeitado pela diferença de médias, e nele $P\ne Q$.
- **(4) Verdadeiro.** Leituras consecutivas são dependentes, e a ordem passa a alterar a distribuição conjunta. A hipótese do Passo 1 da demonstração deixa de valer.

---

## Pausa 2: A MMD

### Pergunta aberta
$\mathbb{E}_P[\phi]=(\mathbb{E}[x],\mathbb{E}[x^2])=(0,1)$ para $P=\mathcal{N}(0,1)$, e $\mathbb{E}_Q[\phi]=(1,\,1+1^2)=(1,2)$ para $Q=\mathcal{N}(1,1)$. Logo $\mathrm{MMD}=\|(0,1)-(1,2)\|=\|(-1,-1)\|=\sqrt2$. A testemunha é $f^\star(x)=\mathbf{w}^{\star T}\phi(x)$ com $\mathbf{w}^\star\propto(-1,-1)$, isto é, $f^\star(x)\propto-(x+x^2)$. Ela é negativa onde $x$ e $x^2$ são grandes, região em que $Q$ tem mais massa.

*Condução:* lembrar que $\mathbb{E}[x^2]=\text{variância}+\text{média}^2$. Quem responder $\mathrm{MMD}=1$ considerou só a diferença de médias: a mudança de média também altera o segundo momento.

### V/F — Kernels, Médias e Testemunha
- **(1) Verdadeiro.** Com kernel linear, $\phi(\mathbf{x})=\mathbf{x}$ e a MMD é $\|\boldsymbol\mu_P-\boldsymbol\mu_Q\|$, que só depende das médias.
- **(2) Falso.** A expressão final só usa $k(\cdot,\cdot)$ entre pares de pontos. O vetor $\phi$ nunca é calculado.
- **(3) Verdadeiro.** A testemunha é proporcional à diferença entre os dois KDEs de largura $\sigma$, referência menos produção.
- **(4) Falso.** O termo que vale 1 é $k(\mathbf{x},\mathbf{x})$. Em $\mathbb{E}[k(\mathbf{x},\mathbf{x}')]$ os pontos são cópias independentes, e o valor depende da concentração de $P$ em relação a $\sigma$.

---

## Pausa 3: Estimação e Largura do Kernel

### Pergunta aberta
Não necessariamente. O estimador não viesado $\widehat{\mathrm{MMD}}_u^2$ tem esperança zero sob $H_0$ e assume valores negativos com frequência (na simulação da aula, em cerca de 61% das repetições). O valor $-0{,}0009$ indica ausência de evidência de diferença. Se o estimador usado fosse o viesado, um valor negativo indicaria erro, porque ele é o quadrado de uma norma. O valor $-0{,}0009$ é o obtido nesta aula para as duas luas contra a mistura de Gaussianas com a largura mediana.

*Condução:* perguntar primeiro qual é a esperança do estimador quando $P=Q$.

### V/F — Viés, Custo e Largura
- **(1) Falso.** O viés vem dos termos com $i=i'$ dentro de cada amostra, em que um ponto é comparado consigo mesmo. Os termos cruzados envolvem sempre pares independentes.
- **(2) Verdadeiro.** A matriz tem $(n+m)^2$ entradas, e $(2n+2m)^2=4(n+m)^2$.
- **(3) Falso.** O menor de 20 p-valores fica abaixo de $\alpha$ com frequência maior que $\alpha$. A estatística deixa de ser a mesma função nos dados observados e nos permutados.
- **(4) Verdadeiro.** A mediana das distâncias na amostra conjunta não depende das atribuições dos pontos e é a mesma em todas as permutações.

---

## Pausa 4: Interpretação do Teste e Alinhamento

### Pergunta aberta
Três verificações, nesta ordem:

1. **Tamanho:** comparar o valor de $\widehat{\mathrm{MMD}}_u^2$ com o histórico do sistema. Com amostras grandes, o p-valor mínimo ocorre mesmo para diferenças pequenas.
2. **Localização:** examinar a testemunha ou os atributos individualmente (por exemplo, com o teste KS por atributo) para identificar onde está a mudança.
3. **Efeito na tarefa:** repetir o teste nas saídas do classificador e comparar a proporção das classes previstas com a do treino. Se a mudança altera as respostas do modelo, rotular uma amostra pequena antes de alinhar ou retreinar. O alinhamento só é adequado se a proporção das classes não mudou.

### V/F — Tipos de Mudança e Alinhamento
- **(1) Falso.** Em um *concept shift*, $p(c\mid\mathbf{x})$ muda com $p(\mathbf{x})$ igual, e a acurácia diminui sem que um teste nas entradas detecte.
- **(2) Verdadeiro.** O poder cresce com $n$ para qualquer diferença fixa. O p-valor não mede o tamanho da diferença.
- **(3) Falso.** Nesse caso a diferença entre as distribuições não deve ser removida. No experimento com etanol e etileno, a padronização reduziu a acurácia de 98,9% para 51,6%.
- **(4) Falso.** A desigualdade $\Pr(\cup_k A_k)\le\sum_k\Pr(A_k)$ vale com qualquer dependência entre os testes.
