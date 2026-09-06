import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Increase padding-top of premium-bar-chart to allow tooltips room
css = css.replace('padding: 2rem 1rem 0;', 'padding: 4rem 1rem 0;')

# ensure flex-direction is column if it wasn't
if 'flex-direction: column;' not in css.split('.growth-chart-wrapper {')[1].split('}')[0]:
    css = css.replace('.growth-chart-wrapper {\n  margin: 4rem auto;', '.growth-chart-wrapper {\n  margin: 4rem auto;\n  flex-direction: column;')

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)


with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove inline margin, max-width, width from growthChart so styles.css handles it cleanly
# The element looks like: <div class="growth-chart-wrapper glass-strong animate-in" id="growthChart" style="padding: 3rem; margin: 4rem auto; max-width: 1000px; width: 100%;">
html = re.sub(r'id="growthChart"\s*style="[^"]*"', 'id="growthChart"', html)

# Make sure it's 300% ROI, and add some styling to it so it doesn't wrap or clip
# We already set white-space: nowrap in CSS.

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Fixed padding and inline styles.')
