with open("teaching/optimization-linear-algebra/aula13/index.qmd", "r", encoding="utf-8") as f:
    lines = f.readlines()

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
print(f"Non-Pausa slides with >1 callout box: {len(over_callout_slides)}")
for s, c in over_callout_slides.items():
    print(f"   Slide: '{s}' has {c} callouts")

print("\nPausa slides callouts:")
for s, c in slide_callouts.items():
    if "Pausa" in s:
        print(f"   Slide: '{s}' has {c} callout(s)")
