import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

def generate_grid(videos):
    grid_html = '<div class="portfolio-grid">\n'
    for v in videos:
        is_horizontal = v.get('horizontal', False)
        vid_id = v['id']
        horizontal_class = ' horizontal' if is_horizontal else ''
        grid_html += f'''            <div class="portfolio-item{horizontal_class} glass animate-in">
                <iframe src="https://fast.wistia.net/embed/iframe/{vid_id}" allow="autoplay; fullscreen" allowtransparency="true" class="portfolio-video" style="border:none;"></iframe>
            </div>\n'''
    grid_html += '        </div>'
    return grid_html

# 1. Real Estate Shorts
real_estate_vids = [
    {'id': 'ut2udo9xicd813u'},
    {'id': 'fns41bbvlaqcxc2'}
]
re_grid = generate_grid(real_estate_vids)
html = re.sub(
    r'(<h2>Real Estate Shorts</h2>\s*</div>\s*)<div class="portfolio-grid">.*?(?=\s*</section>)',
    r'\g<1>' + re_grid,
    html,
    flags=re.DOTALL
)

# 2. Motion Graphics
motion_vids = [
    {'id': '6r4259ozhhahrae'},
    {'id': '9npml9kstwmohvj'},
    {'id': 'lvsbrhbse1sin53'},
    {'id': 'lvsbrhbse1sin53', 'horizontal': True}
]
motion_grid = generate_grid(motion_vids)
html = re.sub(
    r'(<h2>Motion Graphics</h2>\s*</div>\s*)<div class="portfolio-grid">.*?(?=\s*</section>)',
    r'\g<1>' + motion_grid,
    html,
    flags=re.DOTALL
)

# 3. Commercial Ads
ads_vids = [
    {'id': 'mhcabyu7vw52fu8'},
    {'id': 'id1vmjclzmdogg8'},
    {'id': '2xzu6b4g3yl6amq'}
]
ads_grid = generate_grid(ads_vids)
html = re.sub(
    r'(<h2>Commercial Ads</h2>\s*</div>\s*)<div class="portfolio-grid">.*?(?=\s*</section>)',
    r'\g<1>' + ads_grid,
    html,
    flags=re.DOTALL
)

# 4. Social Media Informational Shorts
social_vids = [
    {'id': 'a9pceh6dryfy95s'},
    {'id': '0w50ksxnreqw55j'},
    {'id': 'o3v23kw0kr827da'},
    {'id': '01hlqyj5xxa1kaz'},
    {'id': 'z6v2f64axh1f51x'},
    {'id': 'vyplwa9ce1zgc5i'}
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
print('portfolio.html updated with Wistia videos.')
