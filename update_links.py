
import os

files = [
    {
        "path": "customers/index.html",
        "replacements": {
            'href="customers/': 'href="',
            'href="customers.1"': 'href="."',
            'href="blog.1"': 'href="../now"',
            'href="contact.1"': 'href="../contact"',
            'href="index.html"': 'href="../index.html"',
        }
    },
    {
        "path": "contact/index.html",
        "replacements": {
            'href="contact/': 'href="',
            'href="contact.1"': 'href="."',
            'href="customers.1"': 'href="../customers"',
            'href="customers/': 'href="../customers/',
            'href="blog.1"': 'href="../now"',
            'href="index.html"': 'href="../index.html"',
        }
    },
    {
        "path": "now/index.html",
        "replacements": {
            'href="blog.1"': 'href="."',
            'href="customers.1"': 'href="../customers"',
            'href="customers/': 'href="../customers/',
            'href="contact.1"': 'href="../contact"',
            'href="contact/': 'href="../contact/',
            'href="index.html"': 'href="../index.html"',
        }
    }
]

# Common root links to update (prepend ../)
# Note: longer paths (features/) should be processed before shorter ones if overlapping, but here href="features/ handles it.
root_links = [
    'href="homepage"', 'href="about"', 'href="pricing"', 'href="docs"', 
    'href="login"', 'href="signup"', 'href="mobile"', 'href="build"', 
    'href="readme"', 'href="quality"', 'href="brand"', 'href="developers"', 
    'href="startups"', 'href="dpa"', 'href="privacy"', 'href="terms"', 
    'href="customer-requests"', 'href="join-slack"', 'href="download"',
    'href="features/', 'href="security/', 
    'href="switch.1"', 'href="security.1"', 'href="integrations.1"', 
    'href="changelog.1"', 'href="linear-method"'
]

for file_info in files:
    path = file_info["path"]
    if not os.path.exists(path):
        print(f"Skipping {path}, file not found.")
        continue
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Apply file specific replacements first
    for old, new in file_info["replacements"].items():
        content = content.replace(old, new)
        
    # Apply common root replacements
    # Check if the link hasn't been modified (e.g. href="../features/" already?)
    # A simple replace 'href="X"' -> 'href="../X"' works if X matches exact start.
    for link in root_links:
        # Avoid double replacing if I mistakenly included it in specific
        # But specific ones handled prefixes mainly.
        # Example: link='href="homepage"'. replace with 'href="../homepage"'.
        content = content.replace(link, link.replace('href="', 'href="../'))

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {path}")
