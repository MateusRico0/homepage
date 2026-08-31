# Respostas das Pausas Ativas — Aula 1

> Arquivo de apoio, não publicado (prefixo `_`). Discute as perguntas
> motivadoras das pausas ativas do `index.qmd` e dá a solução dos
> respectivos V/F. O `index.qmd` publicado só contém a pergunta em
> cada pausa ativa, nunca a resolução.

## Cruzamento de condicionais vs. conjuntas

O corte no cruzamento das condicionais ignora a frequência relativa das
classes — ele responde "onde os dois formatos se parecem", não "de onde
este ponto realmente veio". Como B é 19 vezes mais rara, o corte
correto (no cruzamento das conjuntas) precisa se deslocar bem para a
direita, tornando muito mais difícil declarar B.

- ✗ Só coincidem exatamente quando as prioris são exatamente iguais;
  uma diferença pequena desloca o cruzamento das conjuntas por uma
  quantidade pequena, mas não nula.
- ✗ Enquanto houver sobreposição das densidades, existe erro
  irredutível (erro de Bayes); nenhum $t$ zera as duas áreas.
- ✔ Se B fica mais frequente, é preciso *menos* evidência relativa a
  favor de B para declará-la, então a fronteira se desloca para a
  esquerda, tomando território de A.
- ✔ Cortar no cruzamento das condicionais é exatamente agir como se
  as duas classes fossem igualmente prováveis.

## Por que a evidência some da comparação

$p(x)$ é o mesmo número para qualquer classe $k$ num ponto fixo $x$ —
por isso comparar $p(\mathcal{C}_k\mid x)$ entre classes é equivalente
a comparar só o numerador $p(x\mid\mathcal{C}_k)\pi_k$. Isso não
significa que $p(x)$ seja inútil em geral: ele é a densidade marginal,
e volta a importar quando não há mais uma segunda classe para
comparar (Bloco 6, detecção de anomalias).

- ✗ Se $p(x)$ dependesse de $k$, comparar só as conjuntas deixaria de
  ser válido — é exatamente por ela **não** depender de $k$ que dá
  para ignorá-la.
- ✔ Priori zero $\Rightarrow$ posteriori zero, não importa a
  verossimilhança.
- ✔ Mesma estrutura (priori/verossimilhança/conjunta/posteriori),
  outro domínio.
- ✗ $p(x)$ não carrega informação *para a comparação entre classes*,
  mas continua sendo a densidade marginal — informativa em outros
  usos.

## Teorema de Bayes: priori, verossimilhança e evidência

No exemplo da triagem médica, a intuição costuma errar justamente nos
casos extremos de prevalência — uma doença muito rara "puxa" a
posteriori para baixo mesmo com um teste sensível, porque a maioria
dos positivos do teste vem de falsos positivos entre a enorme população
sã, não de verdadeiros positivos entre os poucos doentes.

- ✔ Com prevalência quase total, o numerador (verdadeiros positivos)
  domina o denominador, não importa quão ruim seja o falso positivo.
- ✗ Sem somar sobre todas as classes, o denominador se torna igual ao
  próprio numerador para aquela classe, e a "posteriori" viraria
  trivialmente $1$ só para ela — quebrando a soma-$1$ entre classes.
- ✗ Sem a proporção real de defeituosas (a priori), o Teorema de Bayes
  não pode ser aplicado; sensibilidade e falso-positivo sozinhos não
  bastam.
- ✗ Dobrar a priori de uma classe muda também o denominador (a
  evidência), que soma sobre todas as classes; a posteriori final
  geralmente aumenta por um fator menor que $2$.

## A distribuição Beta

O método de momentos e a máxima verossimilhança respondem perguntas
matematicamente diferentes (uma tem fórmula, não é eficiente; a outra é
eficiente, não tem fórmula), e a armadilha de zeros/uns exatos é sobre
o **suporte** dos dados observados, não sobre os parâmetros $a,b$
estimados.

- ✔ Toda a Uniforme tem densidade constante; não há um único ponto de
  máximo, a moda não é bem definida.
- ✗ Uma única equação (a média) não basta para dois parâmetros
  desconhecidos; o método precisa de pelo menos dois momentos (média e
  variância).
- ✔ A armadilha é sobre observações exatamente iguais a $0$ ou $1$,
  não sobre o valor de $a$ ou $b$ em si; sem zeros/uns exatos nos
  dados, a verossimilhança continua bem definida e finita.
- ✗ Mais dados reduzem a probabilidade de uma estimativa degenerada
  (é um argumento assintótico), mas não eliminam completamente o risco
  em nenhuma amostra finita.

## Das três saídas honestas para o Tipo II indefinido

Nenhuma das três saídas "resolve" o problema de não ter dados de
anomalia — cada uma só torna explícita, de um jeito diferente, uma
suposição que teria de ser feita de qualquer forma. Assumir um modelo
de anomalia esconde uma suposição de forma (frequentemente ruim);
estimar com amostra contaminada herda viés de seleção; aceitar e
declarar é honesto, mas incompleto.

- ✗ Uma amostra rotulada ainda herda o viés de como foi coletada — ter
  *algum* número não elimina o viés, só o torna calculável.
- ✔ Duas uniformes $\Rightarrow$ razão de verossimilhanças constante
  $\Rightarrow$ nenhum limiar discrimina — o teste degenera.
- ✔ Mesmo problema estrutural (só dados de uma classe), outro domínio.
- ✗ Assumir um modelo de anomalia ruim pode ser pior do que declarar
  honestamente que só o Tipo I é conhecido — nenhuma das três é
  universalmente melhor.

## Custo assimétrico

Quando a razão de custos cancela exatamente a razão de prioris, as
duas fontes de assimetria (frequência e custo) se anulam mutuamente, e
o corte volta a ser o cruzamento ingênuo das condicionais — não porque
o custo "não importe" nesse caso, mas porque as duas forças empurram
o corte em direções opostas com magnitudes iguais.

- ✔ $C_{II}/C_I=\pi_A/\pi_B$ cancela exatamente a ponderação pela
  priori, recuperando $T_{COND}$.
- ✔ $C_I\to 0$: qualquer alarme falso "vale a pena" para evitar um
  escape que ainda custa algo — o corte migra para o extremo.
- ✔ Mesma lógica de ponderação por custo, outro domínio.
- ✗ Não conhecer os custos exatos não é evidência de que eles sejam
  iguais — é só incerteza; a perda 0-1 é uma suposição raramente
  justificada, não uma escolha segura por omissão.

## A curva ROC não escolhe o limiar por você

A curva ROC descreve o que é *possível* variando o limiar $t$, e é uma
propriedade só das condicionais $f_A,f_B$ — não da priori. Ela resume
"quão separáveis" as classes são (via AUC), mas nunca diz onde cortar;
essa decisão depende do custo relativo dos dois erros, discutido no
bloco anterior.

- ✗ A curva ROC **não depende da priori** — mudar a prevalência move o
  ponto de operação *sobre* a curva, não a curva em si.
- ✔ AUC $=0{,}5$: curva na diagonal, nenhum limiar discrimina melhor
  que o acaso.
- ✔ AUC compara discriminabilidade entre modelos sem comprometer
  nenhum custo.
- ✗ AUC alta diz que a separação é boa; não diz onde cortar.

## Acurácia, desbalanceamento e o paradoxo da acurácia

Com classes muito desbalanceadas, um classificador ingênuo (sempre
prever a classe majoritária) já atinge acurácia alta sem discriminar
nada — é por isso que a acurácia sozinha é uma métrica traiçoeira
quando $\pi_B\to 0$, e por que precisão/recall/matriz de confusão
existem.

- ✗ Um classificador que sempre prevê a classe majoritária tem
  acurácia igual à prevalência dessa classe — alta, mas sem nenhum
  poder discriminativo.
- ✔ Com $\pi_B\to 0$, o classificador "sempre A" erra cada vez menos
  em proporção, mesmo nunca identificando B.
- ✗ $T_{CONJ}$ minimiza o erro *ponderado pela frequência* das
  classes, não a acurácia ingênua — os dois objetivos podem apontar
  para cortes diferentes.
- ✔ É exatamente o mecanismo do paradoxo: a classe rara pode ser
  ignorada quase inteiramente sem que a acurácia global sofra muito.

## Opção de rejeição

A faixa de rejeição existe porque, perto da fronteira de decisão, a
posteriori vencedora não é muito maior que $0{,}5$ — decidir ali com
"confiança baixa" pode custar mais do que admitir a dúvida e encaminhar
para revisão humana. Mas essa opção só compensa quando o custo da
revisão é, de fato, menor que o custo esperado do erro que ela evita.

- ✔ $\theta=0{,}5$: como $\max_k p(\mathcal{C}_k\mid x)\ge 0{,}5$
  sempre (duas classes somam 1), nada nunca é rejeitado — faixa nula.
- ✔ $\theta\to 1$: exige quase certeza total — quase tudo vira
  rejeição.
- ✔ Mesmo raciocínio de custo (revisão vs. erro evitado), outro
  domínio.
- ✗ Disponibilidade matemática não é garantia de benefício — rejeitar
  só compensa quando a conta de custo favorece a rejeição.
