import re

with open("teaching/optimization-linear-algebra/aula13/index.qmd", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i in range(1, len(lines)):
    line = lines[i]
    prev = lines[i-1]
    is_dash = re.match(r'^\s*-\s+', line)
    prev_is_dash = re.match(r'^\s*-\s+', prev)
    if is_dash and not prev_is_dash and prev.strip() != "":
        print(f"Line {i+1}: prev='{prev.rstrip()}' | curr='{line.rstrip()}'")
