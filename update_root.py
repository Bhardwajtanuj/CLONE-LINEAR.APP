
import os

path = "index.html"
replacements = {
    'href="customers.1"': 'href="customers"',
    'href="contact.1"': 'href="contact"',
    'href="blog.1"': 'href="now"',
}

if os.path.exists(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {path}")
else:
    print(f"{path} not found")
