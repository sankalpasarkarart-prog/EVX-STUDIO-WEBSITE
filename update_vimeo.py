import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the Real Estate grid with the Vimeo iframes.
new_real_estate_html = '''<div class="portfolio-grid">
            <div class="portfolio-item glass animate-in">
                <iframe src="https://player.vimeo.com/video/1224453199?title=0&amp;byline=0&amp;portrait=0&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" class="portfolio-video" style="border:none;" title="final12345"></iframe>
            </div>
            <div class="portfolio-item glass animate-in">
                <iframe src="https://player.vimeo.com/video/1224453198?title=0&amp;byline=0&amp;portrait=0&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" class="portfolio-video" style="border:none;" title="2-2"></iframe>
            </div>
        </div>'''

html = re.sub(
    r'(<h2>Real Estate Shorts</h2>\s*</div>\s*)<div class="portfolio-grid">.*?(?=\s*</section>)',
    r'\g<1>' + new_real_estate_html,
    html,
    flags=re.DOTALL
)

# 2. Add the vimeo script to the head if it's not already there.
if 'player.vimeo.com/api/player.js' not in html:
    html = html.replace('</head>', '    <!-- Vimeo Player Script -->\n    <script src="https://player.vimeo.com/api/player.js" async></script>\n</head>')

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Real estate videos updated with Vimeo.')
