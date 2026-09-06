with open('pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Just replace the specific broken characters
html = html.replace(',11,666', '₹1,666')
html = html.replace('%^ $', '≈ $')
html = html.replace(',1" + perVidINR', '₹" + perVidINR')

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(html)
