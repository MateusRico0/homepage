with open("teaching/optimization-linear-algebra/aula12/index.qmd", "r", encoding="utf-8") as f:
    lines = f.readlines()

def print_range(start_str, end_str):
    recording = False
    for idx, line in enumerate(lines, start=1):
        if start_str in line:
            recording = True
        if recording:
            print(f"{idx}: {line}", end="")
            if end_str in line and idx > 10:
                break

print("=== PAUSA 1 ===")
print_range("## Pausa 1: O Dilema das Oscilações", "# Bloco 2")

print("\n=== PAUSA 2 ===")
print_range("## Pausa 2: Aceleradores de Nesterov", "# Bloco 3")

print("\n=== PAUSA 3 ===")
print_range("## Pausa 3: A Síntese do Adam", "# Bloco 4")

print("\n=== PAUSA 4 ===")
print_range("## Pausa 4: A Cirurgia do AdamW", "## O Que Fica em Aberto")
