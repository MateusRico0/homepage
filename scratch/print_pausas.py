with open("teaching/optimization-linear-algebra/aula12/index.qmd", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if "## Pausa 1:" in l:
        print("".join(lines[i:i+60]))
        print("="*60)
    elif "## Pausa 2:" in l:
        print("".join(lines[i:i+60]))
        print("="*60)
    elif "## Pausa 3:" in l:
        print("".join(lines[i:i+60]))
        print("="*60)
    elif "## Pausa 4:" in l:
        print("".join(lines[i:i+60]))
        print("="*60)
