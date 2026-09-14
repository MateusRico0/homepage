# Respostas da Aula 5 — Pausas Ativas

> Arquivo de apoio, não publicado (prefixo `_`). Discussão em prosa das
> 5 pausas ativas do `index.qmd` (a pergunta motivadora + a resolução
> do V/F, que no `index.qmd` só aparece nos slides RevealJS, nunca nas
> notas HTML).
>
> (O gabarito dos 7 blocos de V/F da seção Exercícios **não** é
> discutido aqui — vive em `exercicios.qmd`/`soluções.qmd`, páginas
> públicas e separadas desta aula.)

### Pausa 1 — Mais componentes sempre aumenta (ou nunca piora) a log-verossimilhança de treino?

A suspeita que fechou a Aula 4 é confirmada de forma literal pelo teste
numérico: a log-verossimilhança de treino do GMM sobe de $-1339{,}45$
($K=1$) a $-1169{,}66$ ($K=10$), sem nenhuma queda ao longo do
caminho. Isso é consequência direta de dois fatos: (1) o modelo com
$K+1$ componentes **contém** toda solução de $K$ componentes como caso
particular (basta um peso $\to0$ no componente extra), então maximizar
sobre um espaço maior nunca produz máximo menor; (2) com covariâncias
livres, um componente pode encolher sobre um único ponto de treino e
levar a log-verossimilhança a divergir — a mesma singularidade já
avisada no Passo M da Aula 4. Nenhuma dessas duas propriedades vale para
a log-verossimilhança medida num conjunto de **validação**: um modelo
que se ajustou demais ao ruído específico do treino (incluindo o caso
degenerado de um componente sobre um único ponto) tende a explicar
pior dados novos, que não têm por que repetir esse ruído específico.

- ✔ Log-verossimilhança de validação não tem por que crescer com $K$ —
  a diferença entre ajuste e generalização é exatamente o que motiva
  esta aula.
- ✔ Com covariâncias livres, um componente pode colapsar sobre um único
  ponto de treino, levando a densidade (e a log-verossimilhança total)
  a divergir.
- ✗ "Nunca piora no treino" é sobre ajuste, não sobre generalização —
  confundir as duas é exatamente o erro estrutural que motiva toda a
  aula.
- ✔ Árvores sem profundidade máxima também podem levar o erro de treino
  a zero — o mesmo padrão de complexidade sem penalidade.

### Pausa 2 — Restringir a covariância a isotrópica eliminaria a divergência?

Não. A forma da matriz de covariância ($\Sigma_k$ livre, diagonal, ou
isotrópica $\sigma_k^2I$) muda **quantos** parâmetros livres o modelo
tem — o que importa para o BIC, no Bloco 4 — mas não elimina a
**direção degenerada** do espaço de parâmetros: mesmo com $\Sigma_k=
\sigma_k^2I$, ainda é possível levar $\sigma_k^2\to0$ com $\mu_k$
centrado sobre um único ponto de treino, e a densidade nesse ponto
ainda diverge. A construção do Bloco 3 (replicar um GMM de $K$
componentes dentro do espaço de $K+1$, com um peso $\to0$) é, na
verdade, mais forte que só um argumento de plausibilidade: ela mostra
que a log-verossimilhança máxima de $K+1$ componentes **nunca** fica
abaixo da de $K$ componentes, para qualquer $K$ — inclusive no caso
degenerado em que dois componentes coincidem exatamente. Restringir a
covariância a diagonal reduz o número de graus de liberdade que podem
colapsar (de $d(d+1)/2$ para $d$ por componente), mas cada um desses
$d$ graus ainda pode individualmente ir a zero. O paralelo com regressão
polinomial de grau alto (erro de treino levado a zero por
interpolação perfeita) é o mesmo fenômeno de sobreajuste sem
penalidade, fora do contexto de misturas.

- ✗ Isotrópica ainda permite $\sigma_k^2\to0$ com $\mu_k$ sobre um único
  ponto — a divergência não depende da forma da matriz, só da direção
  "colapsar sobre um ponto" continuar disponível.
- ✔ Consequência direta da construção do Bloco 3: um modelo de $K$
  componentes é replicável exatamente por um de $K-1$ quando dois
  componentes coincidem — logo o máximo do maior nunca fica abaixo do
  menor.
- ✗ Covariância diagonal ainda tem $d$ graus de liberdade que podem ir a
  zero individualmente — reduz parâmetros livres, não elimina a direção
  degenerada.
- ✔ Mesmo padrão de sobreajuste sem penalidade: mais graus de liberdade,
  melhor ajuste ao treino garantido, sem nenhuma garantia sobre dados
  novos.

### Pausa 3 — O BIC depende de premissas específicas: o que acontece nos casos-limite?

O BIC (eq. 4.139) é derivado sob duas premissas extras, além das da
aproximação de Laplace em si: prior amplo (quase constante) e Hessiana
de posto completo. Sem posto completo, a aproximação
$\ln|A|\approx M\ln N$ perde sua justificativa (parâmetros "não bem
determinados" não contribuem um fator de curvatura pleno à Hessiana), e
o próprio PRML assinala essa ressalva explicitamente — o BIC deixa de
ser confiável nesse regime. Algebricamente, o termo de penalidade
$\tfrac12 M\ln N$ se anula exatamente quando $N=1$ (pois $\ln 1=0$),
não quando $N=M$ (não há cancelamento algébrico entre $M$ e $\ln N$).
Sobre o efeito de $N$ crescer: a penalidade cresce apenas como $\ln N$
(devagar), enquanto o termo de ajuste
$\ln p(\mathcal{D}\mid\theta_{\mathrm{ML}})$ tipicamente cresce quase
linearmente em $N$ (é uma soma de $N$ termos) — na prática, portanto,
mais dados tendem a tornar o BIC **mais tolerante** a modelos
complexos, não mais conservador; a intuição de "mais dados, critério
mais rigoroso" inverte a direção real do efeito. Por fim, o BIC não
depende de variável latente nenhuma — é um resultado geral de
comparação de modelos por máxima verossimilhança penalizada, aplicável
também, por exemplo, à comparação de modelos de regressão logística com
diferentes conjuntos de variáveis.

- ✗ O PRML assinala essa ressalva explicitamente: sem posto completo, a
  aproximação de $\ln|A|\approx M\ln N$ perde a justificativa.
- ✔ Álgebra direta: $\tfrac12 M\ln(1)=\tfrac12 M\cdot0=0$ — a
  penalidade desaparece exatamente quando $N=1$.
- ✗ A penalidade cresce só como $\ln N$ (devagar), enquanto o ajuste
  cresce quase linearmente em $N$ — mais dados tornam o BIC mais
  tolerante a modelos complexos, não mais conservador.
- ✔ O BIC é um resultado geral de comparação por MLE penalizada — não
  depende de variável latente, só de $N$, $M$ e do ajuste ótimo.

### Pausa 4 — Se KL pudesse ser negativa, o que aconteceria com o papel do ELBO?

A decomposição $\ln p(\mathbf{X})=\mathcal{L}(q)+\mathrm{KL}(q\|p)$
vale identicamente, para qualquer $q$ — é a não-negatividade do KL
(Teorema de Gibbs, Bloco 5) que transforma essa identidade numa
**desigualdade útil**, $\mathcal{L}(q)\le\ln p(\mathbf{X})$. Se o KL
pudesse ser negativo, essa mesma identidade permitiria
$\mathcal{L}(q) > \ln p(\mathbf{X})$ — o ELBO deixaria de ser uma cota
inferior confiável, e otimizar $\mathcal{L}(q)$ não garantiria mais
nada sobre $\ln p(\mathbf{X})$. A condição de igualdade do mesmo
teorema (KL$=0$ sse $q=p$) já garante o caso-limite oposto: se a família
de $q$ contém a posterior exata, o máximo de $\mathcal{L}(q)$ sobre essa
família é exatamente $\ln p(\mathbf{X})$. Onde a intuição costuma
falhar é ao comparar **dois modelos diferentes** pelo ELBO: a cota é
sempre válida para o mesmo $\mathbf{X}$/modelo, mas o quão "apertada"
ela é (o próprio KL) pode diferir muito entre dois modelos — não há
garantia de que o modelo com maior $\mathcal{L}(q)$ observado tenha
realmente maior $\ln p(\mathbf{X})$, se um dos dois KLs for muito mais
folgado que o outro. A decomposição em si não usa nenhuma propriedade
específica de misturas gaussianas — vale para qualquer modelo de
variável latente, GMM, Rede Bayesiana, ou outro.

- ✔ Segue diretamente da decomposição: se $\mathrm{KL}<0$ fosse
  possível, $\mathcal{L}(q)=\ln p(\mathbf{X})-\mathrm{KL}(q\|p)$ ficaria
  maior que $\ln p(\mathbf{X})$.
- ✔ Exatamente a condição de igualdade do Teorema da decomposição.
- ✗ A cota vale para o mesmo modelo/mesmo $\mathbf{X}$ — comparando
  dois modelos diferentes, a folga (o próprio KL) pode diferir muito
  entre eles, podendo inverter a comparação.
- ✔ A derivação usa só regra do produto e normalização de $q$ — nenhuma
  hipótese específica de mistura gaussiana.

### Pausa 5 — O Passo E sempre fecha o KL a zero: isso garante o máximo global?

Não — e a distinção é exatamente a mesma que já apareceu na Aula 4 ao
justificar múltiplos reinícios. O Teorema desta aula prova só que cada
iteração completa do EM (Passo E seguido de Passo M) **não piora** a
log-verossimilhança — subida de coordenadas garante não-decréscimo
monotônico, nunca otimalidade global. A prova depende crucialmente de o
Passo M **maximizar completamente** $\mathcal{L}(q^\star,\theta)$ sobre
$\theta$; um passo parcial (por exemplo, um único passo de gradiente)
não garante $\mathcal{L}(q^\star,\theta^{\text{new}})\ge
\mathcal{L}(q^\star,\theta^{\text{old}})$ pela mesma prova — é a base do
chamado "EM Generalizado", que exige só não-decréscimo, não maximização
completa, e por isso precisa de uma justificativa própria (mais fraca)
para a mesma conclusão. No caso-limite em que o KL já é $0$ antes do
Passo E, o passo simplesmente não muda $q$ — trivial. E o mesmo
argumento de subida de coordenadas (alternar uma distribuição sobre
variáveis ocultas e os parâmetros do modelo) é exatamente a estrutura do
algoritmo de Baum-Welch para HMMs — outra instância de EM, fora do
contexto de misturas gaussianas.

- ✔ A prova usada depende de o Passo M **maximizar** $\mathcal{L}$ sobre
  $\theta$ — um passo parcial não garante a desigualdade pela mesma
  prova (base do "EM Generalizado").
- ✔ Consequência trivial: se $\mathrm{KL}$ já é $0$, o Passo E encontra
  $q$ igual ao que já tinha.
- ✗ Subida de coordenadas garante só não-decréscimo monotônico, nunca
  otimalidade global — por isso a Aula 4 já recomendava múltiplos
  reinícios.
- ✔ Baum-Welch é exatamente uma instância do EM para HMMs — mesma
  estrutura de subida de coordenadas, fora do contexto de GMM.
