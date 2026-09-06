import re

with open('pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the broken unicode sequence
html = re.sub(r'perVideoINR\.textContent = ".*? \+ perVidINR\.toLocaleString\(\'en-IN\'\);', 
              'perVideoINR.textContent = "₹" + perVidINR.toLocaleString(\'en-IN\');', 
              html)

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(html)
