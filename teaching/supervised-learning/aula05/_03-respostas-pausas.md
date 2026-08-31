# Respostas das Pausas Ativas — Aula 5

> Arquivo de apoio, não publicado (prefixo `_`). Discute as perguntas
> motivadoras das pausas ativas do `index.qmd` e dá a solução dos
> respectivos V/F. Nesta aula, a Pergunta provocadora e o bloco de V/F
> aparecem publicados de forma compartilhada nas notas e nos slides
> (decisão específica desta aula de revisão); só a resolução (glifos
> ✔/✗ e a justificativa) fica de fora do `index.qmd` publicado, aqui
> registrada.
>
> (Os 12 blocos de V/F da seção Exercícios do `index.qmd` não são
> discutidos aqui — ficam para o aluno resolver por conta, com
> justificativa disponível só ao professor em `_02-solucoes.md`.)

## 1. Prevalência de 50% e os Dois Cruzamentos (Bloco 1 — revisão da Aula 1)

**Pergunta motivadora:** Se a prevalência de diabetes nesta população
fosse exatamente $50\%$, o que aconteceria com a distância entre o
cruzamento das condicionais e o cruzamento das conjuntas?

A distância desapareceria por completo. A conjunta é $p(x,\mathcal{C}_k)
= p(x\mid\mathcal{C}_k)\,\pi_k$; com $\pi_A=\pi_B=0{,}5$, os dois
fatores de ponderação são idênticos, e comparar conjuntas volta a ser
exatamente comparar condicionais — os dois cruzamentos colapsam num só
ponto. Isso explica, de forma direta, por que a distância observada hoje
($134{,}2$ contra $148{,}3$ mg/dL, um gap moderado) é menor que a da
Aula 1 ($0{,}47$ contra $0{,}72$ na escala normalizada, um gap bem
maior): a prevalência real do Pima ($65\%/35\%$) está mais perto de
$50/50$ do que a prevalência sintética da Aula 1 ($95\%/5\%$). O
mecanismo é sempre o mesmo — só a magnitude do efeito muda com a
assimetria das prioris.

- ✔ Com $\pi_A=\pi_B$, a ponderação $p(x\mid\mathcal{C}_k)\,\pi_k$ vira só um fator comum, e comparar conjuntas volta a ser exatamente comparar condicionais — os dois cruzamentos coincidem.
- ✔ A magnitude do deslocamento depende da razão de prioris; o mecanismo é idêntico em qualquer razão.
- ✔ Prevalência ainda menor implica probabilidade pós-teste ainda mais distante da sensibilidade nominal, na mesma direção do exemplo dos $23\%$.
- ✗ O corte pela conjunta trocou alarmes falsos por escapes; só o total caiu, não as duas parcelas individualmente.

## 2. Correlação Perfeita e o Preço da Independência (Bloco 2 — revisão da Aula 2)

**Pergunta motivadora:** Se Glicose e IMC fossem perfeitamente
correlacionados dentro de cada classe ($\rho=1$), a Gaussiana de
covariância plena e o Naive Bayes ainda coincidiriam?

Não. A covariância diagonal do Naive Bayes descarta, por construção,
toda a informação fora da diagonal da matriz de covariância — ela
assume que essa informação é zero. Quando a correlação real é próxima
de zero (como Glicose/IMC no Pima, $0{,}123$ e $0{,}057$), essa
suposição custa muito pouco, porque não há quase nada de real para
descartar — foi exatamente o que a comparação do Bloco 2 mostrou
($76{,}46\%$ em ambos os casos, literalmente idênticos). Mas se
$\rho=1$, existe o máximo possível de estrutura real sendo ignorada: as
duas variáveis, condicionadas à classe, se tornam essencialmente uma
única fonte de informação vista duas vezes, e a covariância diagonal
trataria isso como duas fontes independentes — a Gaussiana de
covariância plena capturaria essa dependência corretamente, e as duas
abordagens deixariam de coincidir. O preço da independência é uma
função contínua da correlação real: zero quando $\rho\approx0$, máximo
quando $|\rho|\to1$.

- ✔ Com $\rho=1$, a covariância diagonal ignora toda a estrutura de dependência real — o preço seria máximo, não nulo como no caso de hoje.
- ✗ O preço de correlação ignorada concentra-se nos atributos correlacionados; atributos irrelevantes adicionais não amplificam nem diluem esse preço específico.
- ✔ Mesma estrutura (independência condicional assumida), fora do domínio médico — a mecânica se transfere.
- ✗ O caso desta aula (Glicose/IMC) é a contraprova direta: correlação quase nula produz preço de acurácia zero, não "pequeno mas sempre presente".

## 3. A Regra Manual do Médico é uma Árvore? (Bloco 3 — revisão da Aula 3)

**Pergunta motivadora:** Um médico usa a regra manual "Glicose acima de
$140$ mg/dL $\Rightarrow$ suspeita de diabetes" — isso é, estruturalmente,
uma árvore de decisão? Se for, por que a árvore do algoritmo é "melhor"
(ou não é)?

Sim, estruturalmente é uma árvore degenerada: uma única pergunta de
corte, duas folhas, cada uma com uma predição fixa. O que falta é o
*processo de ajuste*: a regra do médico foi escolhida por experiência
clínica acumulada e um número "redondo", não por minimizar impureza
sobre dados observados. A árvore do algoritmo (Bloco 3) percorre
sistematicamente todos os cortes possíveis em todas as variáveis
disponíveis e escolhe o que reduz mais a entropia/Gini — encontrou
$123{,}5$ como o primeiro corte, não $140$, porque é o que realmente
separa melhor as duas classes nesta amostra, considerando também o IMC
como segunda variável. Isso não torna a árvore do algoritmo infalível:
ela ainda sofre da mesma miopia gulosa que qualquer árvore sofre
(Bloco 3) — mas dentro dessa limitação, ela otimiza sistematicamente o
que a regra manual só aproxima por intuição.

- ✔ A regra manual é o caso degenerado de uma árvore com uma única folha de decisão, ajustada à mão, sem otimizar impureza sobre dados.
- ✗ É exatamente a miopia gulosa: o algoritmo escolhe o melhor split imediato, sem garantir que a combinação de splits futura seria capturada.
- ✔ Mesma limitação estrutural (corte único, sem interação entre atributos), transferida para outro domínio.
- ✗ Um split com $IG>0$ na raiz é ótimo localmente, não necessariamente parte da árvore globalmente ótima.

## 4. CV Abaixo do Split Único — Isso é um Erro? (Bloco 4 — revisão da Aula 4)

**Pergunta motivadora:** A média de CV ($71{,}3\%$) ficou abaixo da
acurácia do nosso split único de teste ($75{,}2\%$). Isso significa que
o split de teste foi "escolhido a dedo" ou está errado de algum jeito?

Não é evidência de erro em nenhum dos dois números. A CV de $5$ folds
produz cinco sorteios independentes de "qual seria a acurácia numa
amostra de validação nova", e o split único de teste é, essencialmente,
um sexto sorteio independente da mesma distribuição subjacente — só que
feito uma vez só. Os cinco folds variaram entre $69{,}5\%$ e $75{,}5\%$;
o split de teste ($75{,}2\%$) caiu dentro dessa faixa, perto do topo,
mas ainda dentro dela — um resultado favorável, não impossível nem
suspeito. É precisamente por essa variabilidade natural entre sorteios
que a Aula 4 insistiu em reportar CV como média$\pm$desvio-padrão, e
não confiar num único split como se fosse "o" número verdadeiro: um
único split pode, por acaso, calhar de estar em qualquer ponto da
distribuição — inclusive num dos extremos favoráveis.

- ✔ Estar dentro da faixa observada é compatível com "não foi escolhido a dedo" — é a assinatura de um sorteio comum da mesma distribuição.
- ✔ Com teste infinito, a variância do estimador de teste vai a zero e ele converge para $R(\theta)$.
- ✔ Mesma mecânica estatística (ruído de amostragem finita), fora do domínio de aprendizado de máquina.
- ✗ Mais medições reduzem a variância da média de CV em geral, mas não garantem que, nesta amostra específica, a média de CV esteja mais próxima da verdade do que qualquer split único.

## 5. Mesma Estrutura, Técnicas Intercambiáveis? (Bloco 5 — Síntese)

**Pergunta motivadora:** A Aula 6 vai construir regressão linear com sua
própria distribuição, verossimilhança e decisão. Isso significa que
regressão linear "é a mesma coisa" que uma árvore de decisão, só escrita
com notação diferente?

Não — e esse é o ponto mais importante de toda a síntese. Compartilhar a
estrutura de três peças (distribuição, verossimilhança, decisão) é
compartilhar os *ingredientes* do raciocínio, não o *prato* final. A
distribuição assumida por uma regressão linear (ruído gaussiano em torno
de uma relação linear) é completamente diferente da assumida por uma
árvore (categórica por folha) ou por um Naive Bayes (fatoração de
independência) — e essa escolha específica é exatamente a peça que, se
errada, faz o modelo falhar, mesmo que o processo de maximizar a
verossimilhança esteja matematicamente impecável. Reconhecer o padrão
comum é o que permite, ao chegar numa técnica nova, perguntar
imediatamente "qual é a distribuição assumida aqui, e o que acontece se
ela estiver errada?" — não elimina a necessidade de aprender a técnica
específica, só torna esse aprendizado mais rápido e mais crítico.

- ✗ Compartilhar a estrutura não implica compartilhar a distribuição, a verossimilhança específica, ou a regra de decisão — os "ingredientes" são análogos, o "prato" final é diferente.
- ✔ É o erro de "qual das três peças está errada?" desde o slide 1 do curso: maximização correta não garante resultado bom se a suposição distributiva for ruim.
- ✔ Reconhecer a estrutura antes do conteúdo específico é exatamente a competência que esta aula pretende deixar.
- ✗ A escolha da distribuição assumida é a peça mais crítica, não um detalhe secundário — é "quase sempre a que está errada" quando um modelo falha.
