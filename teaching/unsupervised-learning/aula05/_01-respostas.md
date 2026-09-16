# Respostas da Aula 5 — Pausas Ativas

> Arquivo de apoio, não publicado (prefixo `_`). Discussão em prosa das
> 5 pausas ativas do `index.qmd` (a pergunta motivadora + a resolução
> do V/F, que no `index.qmd` só aparece nos slides RevealJS, nunca nas
> notas HTML).
>
> Reescrito do zero junto com a Aula 5 inteira (2026-09-16) — o
> conteúdo, o roteiro e as pausas ativas anteriores (sobre BIC/Laplace)
> não existem mais nesta versão.
>
> (O gabarito dos 8 blocos de V/F da seção Exercícios **não** é
> discutido aqui — vive em `exercicios.qmd`/`soluções.qmd`, páginas
> públicas e separadas desta aula.)

### Pausa 1 — Verossimilhança de treino e a singularidade do Passo M

A pergunta pede para conectar "um componente do GMM pode encolher sua
covariância sobre um único ponto de treino" com "usar a
log-verossimilhança de treino para escolher $K$". A conexão é direta: se
essa singularidade pode inflar a log-verossimilhança de forma
arbitrária (levando-a a $+\infty$ no limite), então o "melhor" $\theta$
segundo esse critério, para $K$ grande, pode ser um artefato numérico
sem sentido estatístico — não uma estrutura real da população. Isso já
antecipa por que qualquer forma de validação em dados nunca vistos
(seja log-verossimilhança de validação, seja Silhueta) quebra essa
monotonicidade: o artefato de colapso beneficia só os pontos específicos
de treino que sofreram o colapso, e desaparece quando o modelo é
avaliado em pontos diferentes.

- ✔ Um componente pode encolher sua covariância sobre um único ponto de
  treino, levando a densidade naquele ponto (e a log-verossimilhança
  total) a divergir — logo o "melhor" $\theta$ para $K$ grande pode nem
  ser um ponto interessante, só um artefato numérico.
- ✔ Se, em vez de comparar $K$ por log-verossimilhança de treino,
  comparássemos por log-verossimilhança medida num conjunto de
  validação nunca usado no ajuste, mais componentes deixaria de
  garantir uma melhora monotônica.
- ✗ Como a log-verossimilhança de treino nunca piora ao acrescentar
  componentes, um GMM com $K=10$ sempre generaliza melhor que um com
  $K=2$ no Breast Cancer Wisconsin — falso: "nunca piora no treino" é
  sobre ajuste, nunca sobre generalização; é exatamente essa confusão
  que motiva toda a aula.
- ✔ O mesmo fenômeno — erro de treino não-crescente conforme a
  complexidade do modelo aumenta — aparece em árvores de decisão sem
  profundidade máxima, cujo erro de treino pode chegar a zero isolando
  cada ponto num nó-folha próprio.

### Pausa 2 — A priori certa é sobre π, não sobre μ,Σ (nem sobre Z)

A pergunta tenta uma armadilha: já que o GMM tem, desde a Aula 4, uma
priori $\pi_k$ sobre a variável latente $z_n$, será que o que falta é
dar uma priori de verdade a **outra** coisa — especificamente,
$\mu_k,\Sigma_k$ (mantendo $\pi$ fixo, como sempre)? Não é isso, e o
Passo 4 da derivação mostra exatamente por quê: o termo de ajuste do
ELBO virou uma esperança só sobre $\mathbf{Z}$ justamente porque a
verossimilhança de $\mathbf{X}$ não depende de $\pi$ dado $\mathbf{Z}$
e $\phi=\{\mu_k,\Sigma_k\}$ — ou seja, $\pi$ não entra no termo de
ajuste de jeito nenhum, só no termo de KL (Passo 5). Dar priori a
$\mu_k,\Sigma_k$, mantendo $\pi$ fora do tratamento variacional, não
introduz nenhum termo de KL novo — a penalidade de Occam continuaria
zero, e o problema de $K=N$ persistiria. A peça que faltava é
literalmente a priori sobre **$\pi$**: sem ela, $\pi$ é só um número
fixo (como no EM clássico); com ela, $\pi$ vira uma variável do próprio
ELBO, com uma distribuição $q(\pi)$ que paga um custo de KL para se
afastar de $p(\pi)$ — e é esse custo que penaliza componentes
supérfluos. Vale notar também que a validade da decomposição $\ln
p(\mathbf{X}\mid\phi)=\mathcal{L}(q,\phi)+\mathrm{KL}(q\|p)$ não
depende de $q$ ser fatorada em campo médio ou não — a fatoração afeta
só o quão apertada é a cota, nunca sua validade como cota inferior.

- ✔ O termo de KL do Passo 5 é sobre $(\mathbf{Z},\pi)$, não sobre
  $(\mu_k,\Sigma_k)$ — dar priori a $\mu_k,\Sigma_k$ mantendo $\pi$
  fixo não cria nenhuma penalidade de complexidade nesta derivação; o
  problema de $K=N$ persistiria.
- ✔ No caso-limite em que a priori $p(\pi)$ é extremamente concentrada
  (quase um ponto único), a decomposição com $\pi$ dentro de
  $\mathbf{H}$ se aproxima da decomposição do EM clássico, já que
  $q(\pi)$ tem pouquíssima liberdade para se afastar desse ponto.
- ✗ Como o campo médio $q(\mathbf{Z},\pi)\approx q(\mathbf{Z})q(\pi)$ é
  só uma conveniência computacional, o ELBO resultante deixa de ser uma
  cota inferior válida de $\ln p(\mathbf{X}\mid\phi)$ sempre que essa
  fatoração não corresponde à dependência real — falso: a desigualdade
  $\mathcal{L}(q,\phi)\le\ln p(\mathbf{X}\mid\phi)$ vale para qualquer
  $q$ normalizada; a fatoração só piora o quão apertada é a cota.
- ✔ O mesmo princípio de poda automática via priori esparsa também
  aparece em regressão linear regularizada por LASSO, onde uma priori
  Laplaciana sobre os coeficientes empurra muitos deles exatamente a
  zero.

### Pausa 3 — Métricas de treino vs. validação em clusterização dura

A pergunta pede para separar "medir a qualidade da partição nos mesmos
pontos que a definiram" de "medir numa amostra independente" — o mesmo
erro conceitual da Pausa 1, agora aplicado a métricas geométricas em vez
de verossimilhança. Calcular Silhueta/Davies-Bouldin no próprio conjunto
de treino mediria só o quão bem o K-Means otimizou sua função objetivo
ali (por construção, o K-Means já minimiza a distorção interna que a
Silhueta/DB recompensam) — não diz nada sobre generalização. Vale notar
também um caso-limite matemático interessante: com $K=N$ no treino (um
cluster por ponto), a Silhueta fica indefinida, porque $a(i)$ (distância
média aos **outros** pontos do mesmo cluster) não tem nenhum outro ponto
para calcular a média — o conceito de "coesão interna" perde sentido
quando não há "interno" nenhum além do próprio ponto.

- ✔ Calcular Silhueta/Davies-Bouldin no próprio conjunto de treino
  mediria só o quão bem o K-Means otimizou sua função objetivo ali —
  não diria nada sobre se essa estrutura generaliza, o mesmo problema
  estrutural da log-verossimilhança de treino na Abertura.
- ✔ No caso-limite $K=N$ (um cluster por ponto de treino), a Silhueta
  calculada no próprio treino fica matematicamente indefinida, pois
  cada cluster teria um único ponto e $a(i)$ não seria calculável.
- ✗ Como a Silhueta e o Davies-Bouldin são métricas puramente
  geométricas (não usam verossimilhança), elas são igualmente
  confiáveis calculadas no treino ou na validação, diferente do que
  acontece com log-verossimilhança — falso: qualquer métrica calculada
  nos dados que definiram a partição tende a favorecer partições mais
  ajustadas àquele conjunto específico, geométrica ou não.
- ✔ A mesma lógica de "ajustar num conjunto, validar estabilidade em
  outro" se aplica a escolher o número de fatores latentes de uma
  Análise de Componentes Principais (PCA) por variância explicada
  reconstruída em dados de validação.

### Pausa 4 — O que o descolamento treino/validação prova (e o que não prova)

A pergunta separa "o critério aponta para $K=3$" de "existem, de fato,
três populações distintas". A log-verossimilhança de validação, como
qualquer estatística calculada sobre uma amostra finita, tem variância
de amostragem: o $K$ vencedor numa divisão específica treino/validação é
a melhor aposta **sob essa divisão**, não uma garantia da estrutura
populacional verdadeira. É por isso que, na prática, é comum repetir o
procedimento com várias divisões diferentes (validação cruzada) e
observar se o mesmo $K$ continua vencendo — um único resultado, sozinho,
não distingue "sinal real" de "ruído daquela amostra específica". Note
também que essa incerteza não desaparece nem no caso-limite de um
conjunto de validação minúsculo: mesmo com um único ponto, modelos
diferentes ainda atribuem densidades diferentes a ele, então a
comparação continua, em princípio, possível — só fica mais ruidosa.

- ✔ A log-verossimilhança de validação, como qualquer critério estimado
  a partir de uma amostra finita, tem variância de amostragem — um
  valor máximo em $K=3$ indicaria que $K=3$ generalizou melhor **nesta**
  divisão treino/validação específica, não uma garantia de que $3$ é o
  número "verdadeiro" de populações latentes.
- ✗ No caso-limite em que o conjunto de validação tem um único ponto, a
  log-verossimilhança de validação para qualquer $K\ge1$ se torna
  idêntica, pois um único ponto não permite distinguir modelos — falso:
  modelos diferentes ainda atribuem densidades diferentes a esse ponto;
  a comparação fica mais ruidosa, não impossível.
- ✗ Como a validação usa dados nunca vistos no ajuste, o $K$ que
  maximiza a log-verossimilhança de validação é, por construção, a
  estrutura verdadeira da população, sem nenhuma incerteza residual —
  falso: validação reduz o risco de sobreajuste, não elimina variância
  de amostragem.
- ✔ O mesmo cuidado (não confundir "o critério aponta para X" com "X é
  a verdade") se aplica a escolher o grau de um polinômio de regressão
  pelo erro quadrático mínimo num conjunto de validação.

### Pausa 5 — Por que boas métricas agregadas não garantem forma correta

O exemplo das duas luas mostrou algo desconfortável: um GMM elíptico
pode ter log-verossimilhança "razoável" e ainda gerar dados sintéticos
visivelmente incompatíveis com a forma real dos dados. A pergunta pede
para generalizar essa observação: seria coincidência do exemplo, ou um
limite estrutural de qualquer métrica agregada (log-verossimilhança,
Silhueta, Davies-Bouldin)? É estrutural — todas essas métricas resumem
a relação entre pontos e modelo a números que dependem de
densidade/distância agregada, nunca da forma geométrica da região que o
modelo cobre. Duas luas perfeitamente separadas (sem sobreposição
nenhuma na fronteira) ainda teriam esse problema: a elipse de cada
componente Gaussiano continuaria preenchendo a região côncava entre as
luas, simplesmente porque uma elipse não consegue ter a forma de um
crescente, independente de quão bem separados os dois grupos estejam.
Validação em dados nunca vistos (Blocos 3 e 4) protege contra
sobreajuste ao ruído específico do treino, mas não contra esse tipo de
incompatibilidade estrutural de forma — os pontos de validação das
luas seriam mal explicados pela mesma elipse, e a métrica agregada
continuaria sem denunciar isso diretamente.

- ✔ Não necessariamente — tanto a log-verossimilhança quanto a Silhueta
  são agregados que dependem de densidade/distância entre pontos, não
  da forma geométrica do cluster; um modelo pode obter bons valores
  agregados e ainda assim gerar dados com formato visivelmente
  incompatível com o real, como no exemplo das luas.
- ✗ No caso-limite em que os dois clusters do formato de lua estão
  perfeitamente separados (sem sobreposição alguma na fronteira), o PPC
  de um GMM elíptico necessariamente coincide pixel a pixel com os
  dados reais — falso: a elipse de cada componente ainda preenche a
  região côncava entre as luas, independente do grau de separação.
- ✗ Como a Silhueta e a log-verossimilhança de validação já são
  calculadas em dados nunca vistos no ajuste, elas automaticamente
  capturam qualquer incompatibilidade de forma entre o modelo gerador e
  os dados reais — falso: validação protege contra sobreajuste ao
  treino, não contra incompatibilidade estrutural de forma entre família
  de modelo e processo gerador.
- ✔ A mesma limitação — métricas agregadas escondendo incompatibilidade
  de forma — motiva, em modelos generativos de imagens, o uso de
  inspeção visual das amostras geradas além de métricas escalares como
  FID (*Fréchet Inception Distance*).
