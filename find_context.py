
with open(r'd:/resume/resume projects/figmenta/linear.app/index.html', 'r', encoding='utf-8') as f:
    content = f.read()
    index = content.find("Collaborate across tools and teams")
    if index != -1:
        print(f"Found at index {index}")
        start = max(0, index - 500)
        end = min(len(content), index + 500)
        print(content[start:end])
    else:
        print("Not found")
