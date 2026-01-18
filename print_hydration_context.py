
with open(r'd:/resume/resume projects/figmenta/linear.app/index.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i == 7341: # Line 7342 (0-indexed 7341)
            index = line.find("tools and teams")
            if index != -1:
                start = max(0, index - 200)
                end = min(len(line), index + 200)
                print(line[start:end])
            else:
                print("Not found in line 7342")
