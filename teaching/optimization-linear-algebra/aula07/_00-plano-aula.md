## Resumo — Aula 7

A Aula 7 introduz a noção de convexidade, movendo a análise de "onde a função cresce" (Gradiente) para "como a inclinação muda" (Hessiana). O objetivo é fornecer as ferramentas matemáticas para garantir que um ponto crítico encontrado por um algoritmo de otimização é, de fato, um mínimo global, e não apenas um local ou um ponto de sela. Focaremos na relação entre a semidefinitude positiva da Hessiana e a convexidade de funções de perda comuns em ML, como a Regressão Ridge.

**Estratégia Pedagógica:** Estratégia B (Inside-Out com Problema-Fio) — Justificativa: Trata-se de fundamentação matemática de análise de superfícies de erro, onde a intuição geométrica deve preceder o formalismo da Hessiana.

## Plano de aula — Aula 7 (carga horária: 70min)

1. **Revisão e Introdução** (~10 min) — Revisão do Gradiente (Aula 6), a ideia de "curvatura" e o Problema-Fio: "Como saber se o mínimo da Regressão Ridge é único e global?".
2. **Intuição: O Mapa do Tesouro** (~10 min) — Visualização de superfícies convexas vs. não-convexas. A diferença entre "estar no fundo de um pote" e "estar em um vale entre montanhas".
3. **Mecanismo I: Conjuntos e Funções Convexas** (~15 min) — Definição formal de conjuntos convexos, a desigualdade de Jensen e a condição de primeira ordem para convexidade (o gradiente como cota inferior).
4. **Mecanismo II: A Matriz Hessiana** (~15 min) — Definição de $\nabla^2 f(x)$, simetria (Teorema de Clairaut) e a condição de segunda ordem: a relação entre a Hessiana ser Semidefinida Positiva (PSD) e a convexidade.
5. **Mecanismo III: Prova de Convexidade em ML** (~15 min) — Aplicação prática: derivando a Hessiana da Regressão Linear e da Regressão Ridge para provar que são problemas convexos.
6. **Fechamento** (~5 min) — Retomada do Problema-Fio e ponte para a Aula 8 (Descida do Gradiente), onde usaremos essa garantia de convexidade para iterar com segurança.

## Fontes usadas — Aula 7

### Fonte 1: Boyd & Vandenberghe, "Convex Optimization", Cap. 3
**Uso pretendido:** Definições formais de conjuntos convexos e funções convexas, além da condição de primeira e segunda ordem.

**Trecho:**
> "A function $f : \mathbb{R}^n \to \mathbb{R}$ is convex if its domain $\text{dom } f$ is a convex set and if $f(\theta x + (1-\theta)y) \le \theta f(x) + (1-\theta)f(y)$ for all $x, y \in \text{dom } f$ and $\theta \in [0, 1]$."

---

### Fonte 2: Goodfellow et al., "Deep Learning", Cap. 4
**Uso pretendido:** Discussão sobre a importância da convexidade para a convergência de algoritmos de otimização em ML.

**Trecho:**
> "A convex function is one where the line segment between any two points on the graph of the function lies above or on the graph... This property is crucial because any local minimum of a convex function is also a global minimum."
