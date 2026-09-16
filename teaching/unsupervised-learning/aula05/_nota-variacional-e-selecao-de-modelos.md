# Nota — Como o variacional (ELBO) ajuda na seleção de modelos

> Documento intermediário (prefixo `_`, não publicado). Escrito para
> esclarecer uma tensão aparente na Aula 5 de Aprendizado Não
> Supervisionado, entre duas afirmações que a aula faz e que parecem se
> contradizer:
>
> 1. A Síntese diz que a decomposição `ln p(X) = L(q) + KL(q‖p)` "serve
>    para selecionar e ajustar" modelos.
> 2. A Pausa Ativa (Bloco 5/6) avisa que "comparar ELBOs de modelos
>    diferentes exige cuidado", já que a folga (o KL) pode não ser
>    comparável entre eles.
>
> Este documento resolve a tensão e propõe uma "receita prática" que a
> aula hoje não deixa explícita. Se for incorporado ao `index.qmd`,
> o lugar natural é a seção "Síntese, Fechamento e Ponte para a Aula 6",
> ou como uma expansão do Bloco 6.

## O objetivo original: a evidência do modelo

Para escolher entre modelos concorrentes (ex.: GMM com $K=2$ vs.
$K=3$), o critério "certo" é a **evidência** $p(\mathbf{X}\mid
\mathcal{M})$ — a verossimilhança marginal, depois de integrar sobre
**todos** os parâmetros possíveis do modelo, não só o melhor ajuste.
Essa integral já penaliza complexidade excessiva automaticamente: um
modelo mais flexível espalha sua massa de probabilidade por um espaço
de parâmetros maior, então cada configuração específica de parâmetros
"vale" menos evidência — é a versão bayesiana da navalha de Occam,
embutida na própria matemática, sem precisar de um termo de penalização
ad-hoc.

O problema prático: essa integral quase sempre é intratável.

## Duas rotas para aproximar essa integral intratável

### 1. BIC — aproximação de Laplace

Expande a log-verossimilhança em torno de $\theta_{\mathrm{ML}}$ (série
de Taylor de segunda ordem), assume posterior aproximadamente
Gaussiana, prior amplo, e Hessiana de posto completo. O resultado é uma
**fórmula fechada**, rápida de calcular — mas cega às particularidades
do modelo: só funciona bem quando essas premissas de fato valem.

### 2. ELBO — otimização variacional

Em vez de aproximar a integral analiticamente, escolha uma família
tratável de distribuições $q(\mathbf{Z})$ e otimize o **ELBO**
$\mathcal{L}(q)$ sobre essa família:
$$
\ln p(\mathbf{X}) = \mathcal{L}(q) + \mathrm{KL}\big(q\,\|\,
p(\mathbf{Z}\mid\mathbf{X})\big) \;\ge\; \mathcal{L}(q)
\quad\text{(para toda $q$ normalizada)}.
$$
Nenhuma das premissas de Laplace é necessária. **Atenção:** isso só
funciona para seleção se $\theta$ também estiver dentro de $q$ (com um
prior) — o Algoritmo EM da Aula 4 é um caso especial que NÃO faz isso
(mantém $\theta$ como ponto fixo, sem prior); ver a correção mais
abaixo, que existe exatamente por causa dessa distinção.

## A receita prática de seleção via ELBO

Para cada modelo candidato $\mathcal{M}_k$ (ex.: cada valor de $K$):

1. Ajuste o melhor $q$ dentro da mesma família variacional (otimize
   $\mathcal{L}(q)$ até convergência — de novo, é literalmente o EM).
2. Registre o valor ótimo, $\mathcal{L}_k^{*} := \max_q \mathcal{L}(q
   \mid \mathcal{M}_k)$.
3. Compare $\mathcal{L}_k^{*}$ entre os candidatos $k$ e escolha o
   maior — exatamente como se faria comparando valores de BIC, só que
   trocando a fórmula fechada por um número obtido numericamente.

## Onde mora o cuidado (por que a Pausa Ativa avisa)

$$
\mathcal{L}_k^{*} = \ln p(\mathbf{X}\mid\mathcal{M}_k) -
\mathrm{KL}_k^{*}
$$

onde $\mathrm{KL}_k^{*}$ é o quão longe o melhor $q$ **daquela
família** ficou da posterior verdadeira **daquele modelo específico**.

Se a família $q$ aproxima bem a posterior do modelo com $K=2$ mas mal a
do modelo com $K=5$ (por exemplo, porque a posterior do segundo é
estruturalmente mais complicada — mais modos, mais correlação entre
variáveis latentes), os dois $\mathrm{KL}^{*}$ são diferentes, e
comparar $\mathcal{L}_2^{*}$ com $\mathcal{L}_5^{*}$ diretamente pode
enganar: a diferença observada pode vir do **viés da aproximação**, não
de uma diferença real na evidência dos dois modelos.

**Mitigação padrão:** usar a mesma estrutura de família variacional
(ex.: sempre mean-field com a mesma parametrização) em todos os
candidatos, para não introduzir um viés sistemático a favor de um nível
de complexidade específico. Isso não elimina o problema — só evita que
ele seja pior para um candidato do que para outro por uma razão
artificial (escolha de família, não de modelo).

Vale notar o paralelo: o erro do BIC também varia caso a caso (as
premissas de Laplace valem melhor para uns modelos que para outros) —
na prática, ambos os critérios são aceitos como aproximações
imperfeitas, mas úteis, da mesma quantidade intratável.

## Correção importante: o ELBO do EM **não** é o ELBO que serve para seleção

*(Adicionado depois de uma pergunta certeira: "para usar o ELBO como
seleção, precisamos da posteriori verdadeira?" A resposta é não — mas a
razão revela um erro na primeira versão deste documento, que dizia que
"o mesmo cálculo do EM já serve para selecionar". Não serve, e vale
entender por quê.)*

A aula (Bloco 6) é explícita: a decomposição do Bloco 5 foi escrita na
forma **Bayesiana plena**, com $\theta$ absorvido dentro de
$\mathbf{Z}$ — ou seja, $\mathbf{Z}$ ali pode significar "tudo que não é
observado", **inclusive os parâmetros**. Para recuperar o Algoritmo EM
exatamente como a Aula 4 apresentou, o Bloco 6 faz o oposto de
propósito: **tira $\theta$ de dentro de $\mathbf{Z}$** e o trata como
parâmetro fixo (um ponto, sem prior, sem incerteza) — não como variável
aleatória.

Isso muda o que o ELBO do EM significa. No Passo E, o KL sobre
$\mathbf{Z}$ fecha a exatamente zero — mas $\theta$ continua sendo só
um ponto, $\theta_{\mathrm{ML}}$, nunca integrado. No ótimo do EM,

$$
\mathcal{L}(q^{*},\theta_{\mathrm{ML}}) = \ln p(\mathbf{X}\mid
\theta_{\mathrm{ML}}),
$$

que é exatamente a verossimilhança **no melhor ponto** — a mesma
quantidade que a Abertura da aula já rejeitou como critério de seleção
("nunca piora com mais componentes"). **O ELBO do EM não tem a
propriedade de Occam que a evidência verdadeira tem**, porque nunca
integra sobre $\theta$: usá-lo para comparar candidatos $K$ teria o
mesmo problema da log-verossimilhança crua.

**O que de fato seria necessário:** manter $\theta$ **dentro** do
tratamento variacional — dar um prior $p(\theta)$ a $\theta$ e
aproximar $q(\mathbf{Z},\theta)\approx q(\mathbf{Z})\,q(\theta)$, não só
$q(\mathbf{Z})$. O ELBO resultante,
$$
\mathcal{L}(q) = \iint q(\mathbf{Z})q(\theta)\ln
\frac{p(\mathbf{X},\mathbf{Z},\theta)}{q(\mathbf{Z})q(\theta)}\,
\mathrm{d}\mathbf{Z}\,\mathrm{d}\theta \;\le\; \ln p(\mathbf{X}),
$$
é cota da evidência **de verdade** (integrando $\theta$, não
condicionando nele) — e carrega a penalização automática de
complexidade, porque um parâmetro supérfluo custa
$\mathrm{KL}(q(\theta)\|p(\theta))$ sem ajudar a explicar os dados.
Isso é **Inferência Bayesiana Variacional** (*Variational Bayes*) — um
procedimento **diferente** do EM, não o mesmo cálculo do Bloco 6. É o
que o PRML faz no capítulo seguinte (§10.2, GMM variacional): trata
pesos, médias e precisões todos variacionalmente, e componentes
desnecessários têm seu peso empurrado a quase zero — uma forma de
"poda automática" que resolve seleção de $K$ sem nem precisar comparar
$\mathcal{L}^{*}_k$ entre rodadas separadas.

**Conclusão revisada:** a "receita prática" da seção anterior
(maximizar $\mathcal{L}(q)$ família a família e comparar) só é válida
se $\theta$ também estiver dentro de $q$, com um prior — isto é, se for
Variational Bayes de verdade. Aplicada ao ELBO do EM puro (Bloco 6,
$\theta$ como parâmetro), a receita não funciona, pelo motivo acima.
