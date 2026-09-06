import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the old POV banner
old_pov_pattern = r'\s*<!-- ======== POV BANNER ======== -->\s*<div class="pov-banner" id="pov-banner">.*?</div>\s*</div>'
content = re.sub(old_pov_pattern, '', content, flags=re.DOTALL)

# 2. Add the new POV banner above the services section
services_pattern = r'(\s*<!-- ======== SERVICES SECTION ======== -->\s*<section class="section" id="services">)'
new_pov = '''
    <!-- ======== POV BANNER ======== -->
    <div class="pov-text-banner glass animate-in" style="max-width: 900px; margin: 2rem auto 4rem; padding: 3rem 2rem; text-align: center; border-radius: var(--radius-card); position: relative; z-index: 10;">
        <h2 style="font-size: clamp(1.8rem, 4vw, 2.5rem); font-family: var(--font-heading); font-weight: 800; line-height: 1.3; color: var(--text-primary); letter-spacing: -0.5px;">
            <span style="color: var(--accent);">POV:</span> You just reclaimed <strong style="color: #fff; text-shadow: 0 0 10px rgba(255,255,255,0.3);">20 hours</strong> of your week because you outsourced your editing to <strong style="color: #fff; text-shadow: 0 0 10px rgba(255,255,255,0.3);">us</strong>.
        </h2>
    </div>
'''
content = re.sub(services_pattern, new_pov + r'\1', content)

# 3. Replace the graph with a new responsive HTML/CSS graph
old_graph_pattern = r'<div class="growth-chart-wrapper glass animate-in" id="growthChart">.*?</div>\s*</div>'

new_graph = '''<div class="growth-chart-wrapper glass-strong animate-in" id="growthChart" style="padding: 3rem; margin: 4rem 0;">
            <div class="chart-header" style="text-align: center; margin-bottom: 3rem;">
                <h3 style="font-size: 2.2rem; margin-bottom: 0.5rem;">Grow your business <span class="gradient-text">300% faster</span> with us</h3>
                <p style="color: var(--text-secondary); font-size: 1.1rem;">Consistent, high-quality video content is the ultimate lever for scalable growth.</p>
            </div>
            
            <div class="premium-bar-chart">
                <div class="bar-container">
                    <div class="bar-label">Month 1</div>
                    <div class="bar-track glass">
                        <div class="bar-fill" style="--target-height: 25%; animation-delay: 0.2s;">
                            <div class="bar-value">25%</div>
                        </div>
                    </div>
                    <div class="bar-title">Initial</div>
                </div>
                
                <div class="bar-container">
                    <div class="bar-label">Month 2</div>
                    <div class="bar-track glass">
                        <div class="bar-fill" style="--target-height: 45%; animation-delay: 0.4s;">
                            <div class="bar-value">45%</div>
                        </div>
                    </div>
                    <div class="bar-title">Optimization</div>
                </div>
                
                <div class="bar-container">
                    <div class="bar-label">Month 3</div>
                    <div class="bar-track glass">
                        <div class="bar-fill" style="--target-height: 70%; animation-delay: 0.6s;">
                            <div class="bar-value">70%</div>
                        </div>
                    </div>
                    <div class="bar-title">Scaling</div>
                </div>
                
                <div class="bar-container">
                    <div class="bar-label">Month 4</div>
                    <div class="bar-track glass">
                        <div class="bar-fill highlight" style="--target-height: 100%; animation-delay: 0.8s;">
                            <div class="bar-value">300% ROI</div>
                        </div>
                    </div>
                    <div class="bar-title">Viral Growth</div>
                </div>
            </div>
        </div>'''

content = re.sub(old_graph_pattern, new_graph, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Index.html updated successfully.')
