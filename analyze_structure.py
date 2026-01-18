
with open(r'd:/resume/resume projects/figmenta/linear.app/index.html', 'r', encoding='utf-8') as f:
    content = f.read()
    # Find the text in the whole file
    index = content.find("Collaborate across tools and teams")
    if index != -1:
        # Look backwards for "className"
        sub = content[max(0, index-1000):index]
        # Find the last "className"
        last_class = sub.rfind("className")
        if last_class != -1:
            print(f"ClassName context: {sub[last_class:last_class+100]}")
        else:
            print("ClassName not found nearby")
        
        # Look forwards for "button" or "svg"
        sub_forward = content[index:min(len(content), index+1000)]
        print(f"Forward context: {sub_forward}")
