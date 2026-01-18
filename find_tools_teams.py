
with open(r'd:/resume/resume projects/figmenta/linear.app/index.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if "tools and teams" in line:
            print(f"Found on line {i+1}: {line.strip()[:100]}...")
