import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

def generate_grid(videos):
    grid_html = '<div class="portfolio-grid">\n'
    for v in videos:
        is_horizontal = v.get('horizontal', False)
        vid_id = v['id']
        title = v.get('title', 'video')
        horizontal_class = ' horizontal' if is_horizontal else ''
        grid_html += f'''            <div class="portfolio-item{horizontal_class} glass animate-in">
                <iframe src="https://player.vimeo.com/video/{vid_id}?title=0&amp;byline=0&amp;portrait=0&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" class="portfolio-video" style="border:none;" title="{title}"></iframe>
            </div>\n'''
    grid_html += '        </div>'
    return grid_html

# 1. Motion Graphics
motion_vids = [
    {'id': '1224453733', 'title': '3'},
    {'id': '1224453784', 'title': '6'},
    {'id': '1224453732', 'title': 'Copy of Saas portfolio_WI_SOUND', 'horizontal': True}
]
motion_grid = generate_grid(motion_vids)
html = re.sub(
    r'(<h2>Motion Graphics</h2>\s*</div>\s*)<div class="portfolio-grid">.*?(?=\s*</section>)',
    r'\g<1>' + motion_grid,
    html,
    flags=re.DOTALL
)

# 2. Commercial Ads
ads_vids = [
    {'id': '1224453731', 'title': 'ADS'},
    {'id': '1224453775', 'title': 'REAL-ESTATE-REEL-2'},
    {'id': '1224453734', 'title': 'RealEstateReel3'}
]
ads_grid = generate_grid(ads_vids)
html = re.sub(
    r'(<h2>Commercial Ads</h2>\s*</div>\s*)<div class="portfolio-grid">.*?(?=\s*</section>)',
    r'\g<1>' + ads_grid,
    html,
    flags=re.DOTALL
)

# 3. Social Media Informational Shorts
social_vids = [
    {'id': '1224454252', 'title': 'AI Motion controlFINAL2'},
    {'id': '1224454234', 'title': 'CC-CORRECTED-YASH'},
    {'id': '1224454450', 'title': 'OpusClip(FInal-Startup-Seekho)'},
    {'id': '1224454452', 'title': 'MSE-final-'},
    {'id': '1224454448', 'title': 'Ai Bubble Brust(fixed caption)'},
    {'id': '1224454451', 'title': 'Anthropic'}
]
social_grid = generate_grid(social_vids)
html = re.sub(
    r'(<h2>Social Media Informational Shorts</h2>\s*</div>\s*)<div class="portfolio-grid">.*?(?=\s*</section>)',
    r'\g<1>' + social_grid,
    html,
    flags=re.DOTALL
)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('portfolio.html updated with Vimeo videos.')
