import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the Wistia script
html = re.sub(r'\s*<!-- Wistia Video Player Script -->\s*<script src="https://fast\.wistia\.net/assets/external/E-v1\.js" async></script>', '', html)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
