import os
import glob

html_files = glob.glob('*.html')

buttons_html = '''
                <div style="margin-top: 1.5rem; display: flex; flex-direction: column; gap: 1rem; max-width: 250px;">
                    <a href="/know-about-the-founder.html" class="btn-primary" style="text-align: center; padding: 0.8rem; font-size: 0.95rem;">Know About the Founder</a>
                    <a href="/know-about-us.html" class="btn-primary" style="text-align: center; padding: 0.8rem; font-size: 0.95rem; background: rgba(var(--accent-rgb), 0.1); border: 1px solid var(--accent); box-shadow: none;">Know About Us</a>
                </div>
'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We find:
    # <div class="footer-brand">
    #     <p>Premium media production company crafting visual stories for brands worldwide.</p>
    
    if 'know-about-the-founder.html' not in content:
        target = '<p>Premium media production company crafting visual stories for brands worldwide.</p>'
        if target in content:
            content = content.replace(target, target + '\n' + buttons_html)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)

print('Footers updated.')
