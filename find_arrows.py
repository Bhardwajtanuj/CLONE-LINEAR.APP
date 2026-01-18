
with open(r'd:/resume/resume projects/figmenta/linear.app/index.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i > 7000: break
        if any(x in line for x in ["arrow", "chevron", "prev", "next"]):
            if "script" not in line and "link" not in line:
                print(f"Line {i+1}: {line.strip()[:100]}")
