import re

with open("teaching/optimization-linear-algebra/aula12/index.qmd", "r", encoding="utf-8") as f:
    text = f.read()

lines = text.splitlines()

# 1. Div balance
div_depth = 0
for idx, line in enumerate(lines, start=1):
    opens = len(re.findall(r'^:::\s*\{', line))
    closes = 1 if re.match(r'^:::\s*$', line) else 0
    div_depth += (opens - closes)
    if div_depth < 0:
        print(f"Error: negative div depth at line {idx}: {line}")
        break

print(f"1. Final div depth: {div_depth} (expected 0)")

# 2. Check dash lists
dash_errors = []
for i in range(1, len(lines)):
    line = lines[i]
    prev = lines[i-1]
    is_dash = re.match(r'^\s*-\s+', line)
    prev_is_dash = re.match(r'^\s*-\s+', prev)
    if is_dash and not prev_is_dash and prev.strip() != "":
        dash_errors.append((i+1, prev.rstrip(), line.rstrip()))

print(f"2. Total dash list errors: {len(dash_errors)} (expected 0)")

# 3. Check revealjs slide callout boxes count
in_reveal = False
current_slide = None
slide_callouts = {}

for idx, line in enumerate(lines, start=1):
    if 'content-visible when-format="revealjs"' in line:
        in_reveal = True
    elif in_reveal and '::: {.content-visible' in line:
        in_reveal = False
    
    if in_reveal:
        if line.startswith("## "):
            current_slide = line[3:].strip()
            slide_callouts[current_slide] = 0
        elif ".callout-" in line:
            if current_slide:
                slide_callouts[current_slide] += 1

over_callout_slides = {s: c for s, c in slide_callouts.items() if c > 1 and "Pausa" not in s}
print(f"3. Non-Pausa slides with >1 callout box: {len(over_callout_slides)}")
for s, c in over_callout_slides.items():
    print(f"   Slide: '{s}' has {c} callouts")

print("\nPausa slides callouts:")
for s, c in slide_callouts.items():
    if "Pausa" in s:
        print(f"   Slide: '{s}' has {c} callout(s)")

