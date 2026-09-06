import glob
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('href="/know-about-the-founder.html"', 'href="/know-about-the-founder"')
    c = c.replace('href="/know-about-us.html"', 'href="/know-about-us"')
    with open(file, 'w', encoding='utf-8') as f:
        f.write(c)
