with open("teaching/optimization-linear-algebra/aula13/index.qmd", "r", encoding="utf-8") as f:
    text = f.read()

# Fix 1: line 210
text = text.replace(
    '  $$W_{ij} \\leftarrow W_{ij} - \\frac{\\alpha}{\\sqrt{v_{ij}}+\\epsilon} m_{ij}$$\n- Descarta',
    '  $$W_{ij} \\leftarrow W_{ij} - \\frac{\\alpha}{\\sqrt{v_{ij}}+\\epsilon} m_{ij}$$\n\n- Descarta'
)

# Fix 2 & 3: line 521, 523
text = text.replace(
    '  $$\\sigma_1(U) = \\sigma_2(U) = \\dots = \\sigma_n(U) = 1$$\n- **Norma espectral controlada:**\n  $$\\|U\\|_2 = 1$$\n- **Prevenção',
    '  $$\\sigma_1(U) = \\sigma_2(U) = \\dots = \\sigma_n(U) = 1$$\n\n- **Norma espectral controlada:**\n  $$\\|U\\|_2 = 1$$\n\n- **Prevenção'
)

# Fix 4 & 5: line 624, 627
text = text.replace(
    'Analisando a função $f(\\sigma)$:\n- Pontos fixos:',
    'Analisando a função $f(\\sigma)$:\n\n- Pontos fixos:'
)
text = text.replace(
    '  $$f\'(\\sigma) = \\frac{3}{2} - \\frac{3}{2}\\sigma^2 \\implies f\'(1) = 0$$\n- Análise do erro',
    '  $$f\'(\\sigma) = \\frac{3}{2} - \\frac{3}{2}\\sigma^2 \\implies f\'(1) = 0$$\n\n- Análise do erro'
)

# Fix 6: line 730
text = text.replace(
    'Em benchmarks de treinamento do NanoGPT e modelos estilo LLaMA:\n- **Redução',
    'Em benchmarks de treinamento do NanoGPT e modelos estilo LLaMA:\n\n- **Redução'
)

# Fix 7 & 8: line 841, 845
text = text.replace(
    'No entanto, problemas centrais de Machine Learning exigem penalidades **não-suaves (não-diferenciáveis)**:\n- Como induzir',
    'No entanto, problemas centrais de Machine Learning exigem penalidades **não-suaves (não-diferenciáveis)**:\n\n- Como induzir'
)
text = text.replace(
    'Na **Aula 14: Otimização Não-Suave, Subgradientes e Operadores Proximais**, daremos o passo definitivo para o cálculo não-diferenciável:\n- O conceito',
    'Na **Aula 14: Otimização Não-Suave, Subgradientes e Operadores Proximais**, daremos o passo definitivo para o cálculo não-diferenciável:\n\n- O conceito'
)

with open("teaching/optimization-linear-algebra/aula13/index.qmd", "w", encoding="utf-8") as f:
    f.write(text)

print("Fixes applied!")
