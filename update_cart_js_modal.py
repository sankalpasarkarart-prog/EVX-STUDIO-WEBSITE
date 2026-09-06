with open('cart.js', 'r', encoding='utf-8') as f:
    js = f.read()

old = 'window.open(whatsappUrl, "_blank");'
new = 'if (window.openWhatsAppWithTerms) { window.openWhatsAppWithTerms(whatsappUrl); } else { window.open(whatsappUrl, "_blank"); }'
js = js.replace(old, new)

with open('cart.js', 'w', encoding='utf-8') as f:
    f.write(js)
print('cart.js updated')
