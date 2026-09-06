import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update font families
# We want to replace the font definitions in :root
root_pattern = r'(:root\s*\{.*?\})'
def root_repl(match):
    m = match.group(1)
    # Backgrounds
    m = re.sub(r'--bg-primary:\s*#[0-9a-fA-F]+;', '--bg-primary: #0a0a0c;', m)
    m = re.sub(r'--bg-secondary:\s*#[0-9a-fA-F]+;', '--bg-secondary: #111116;', m)
    
    # Fonts
    m = re.sub(r"--font-heading:\s*'[^']+',\s*sans-serif;", '--font-heading: "SF Pro Display", "SF Pro", -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Grotesk", "Futura", sans-serif;', m)
    m = re.sub(r"--font-body:\s*'[^']+',\s*sans-serif;", '--font-body: "Inter", "SF Pro Text", -apple-system, BlinkMacSystemFont, "Helvetica Neue", sans-serif;', m)
    
    # Glass blur & backgrounds
    m = re.sub(r'--glass-blur:\s*\d+px;', '--glass-blur: 30px;', m)
    m = re.sub(r'--glass-blur-strong:\s*\d+px;', '--glass-blur-strong: 50px;', m)
    m = re.sub(r'--glass-bg:\s*rgba\([^)]+\);', '--glass-bg: rgba(255, 255, 255, 0.03);', m)
    m = re.sub(r'--glass-bg-strong:\s*rgba\([^)]+\);', '--glass-bg-strong: rgba(255, 255, 255, 0.06);', m)
    m = re.sub(r'--glass-border:\s*rgba\([^)]+\);', '--glass-border: rgba(255, 255, 255, 0.08);', m)
    m = re.sub(r'--glass-border-strong:\s*rgba\([^)]+\);', '--glass-border-strong: rgba(255, 255, 255, 0.15);', m)
    
    return m

css = re.sub(root_pattern, root_repl, css, flags=re.DOTALL)

# 2. Update .glass and .glass-strong styles to be more premium
# Add inner shadow
glass_pattern = r'(\.glass\s*\{[^}]*?-webkit-backdrop-filter[^}]*\})'
def glass_repl(match):
    block = match.group(1)
    if 'box-shadow:' not in block:
        block = block.replace('}', '  box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.1), 0 4px 20px rgba(0, 0, 0, 0.2);\n}')
    return block
css = re.sub(glass_pattern, glass_repl, css)

glass_strong_pattern = r'(\.glass-strong\s*\{[^}]*?-webkit-backdrop-filter[^}]*\})'
def glass_strong_repl(match):
    block = match.group(1)
    if 'box-shadow:' not in block:
        block = block.replace('}', '  box-shadow: inset 0 1px 2px rgba(255, 255, 255, 0.15), 0 8px 30px rgba(0, 0, 0, 0.3);\n}')
    return block
css = re.sub(glass_strong_pattern, glass_strong_repl, css)

# 3. Mobile Menu Side Panel (in media max-width 768px)
# We want to find .nav-links inside @media (max-width: 768px) and update it
nav_links_mobile_pattern = r'(\.nav-links\s*\{\s*position:\s*fixed;\s*top:\s*0;\s*left:\s*0;\s*width:\s*)50vw(;\s*height:\s*100vh;.*?)background:\s*rgba\([^)]+\)(.*?padding:\s*)100px 2rem 2rem(.*?)\}'
def nav_links_repl(match):
    return (match.group(1) + '80vw' + match.group(2) +
            'background: rgba(15, 15, 20, 0.65)' + match.group(3) +
            '120px 2.5rem 3rem' + match.group(4) + 
            '  border-right: 1px solid rgba(255, 255, 255, 0.1);\n  box-shadow: 20px 0 50px rgba(0, 0, 0, 0.8), inset -1px 0 0 rgba(255,255,255,0.05);\n}')

css = re.sub(nav_links_mobile_pattern, nav_links_repl, css, flags=re.DOTALL)

# Add clear liquid glass animation for side panel items
if '.nav-links a' in css and '@keyframes menu-item-slide' not in css:
    menu_animation_css = '''
  .nav-links.active a {
    animation: menu-item-slide 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
    opacity: 0;
    transform: translateX(-20px);
  }
  .nav-links.active li:nth-child(1) a { animation-delay: 0.1s; }
  .nav-links.active li:nth-child(2) a { animation-delay: 0.15s; }
  .nav-links.active li:nth-child(3) a { animation-delay: 0.2s; }
  .nav-links.active li:nth-child(4) a { animation-delay: 0.25s; }
  .nav-links.active li:nth-child(5) a { animation-delay: 0.3s; }
  .nav-links.active li:nth-child(6) a { animation-delay: 0.35s; }

@keyframes menu-item-slide {
  to {
    opacity: 1;
    transform: translateX(0);
  }
}
'''
    # Insert right after the .nav-links a rule in the media query
    css = re.sub(r'(\.nav-links a\s*\{[^}]*\})', r'\1' + menu_animation_css, css, count=1)


# 4. Graph Redesign CSS
# Remove old SVG chart CSS and add new Bar Chart CSS
old_chart_css_pattern = r'/\* Animated state — triggered by JS adding \.chart-animate \*/.*?\.chart-tooltip\s*\{.*?\s*\}'

new_chart_css = '''/* Premium Bar Chart */
.premium-bar-chart {
  display: flex;
  align-items: flex-end;
  justify-content: space-around;
  height: 300px;
  padding: 2rem 1rem 0;
  gap: 1rem;
}

.bar-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 100%;
  flex: 1;
  max-width: 100px;
  position: relative;
}

.bar-label {
  font-size: 0.85rem;
  color: var(--text-muted);
  margin-bottom: 1rem;
  font-weight: 600;
  letter-spacing: 1px;
  text-transform: uppercase;
}

.bar-track {
  width: 100%;
  height: 100%;
  border-radius: var(--radius-sm);
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: flex-end;
}

.bar-fill {
  width: 100%;
  background: linear-gradient(to top, rgba(var(--accent-rgb), 0.2), var(--accent));
  border-radius: var(--radius-sm);
  height: 0; /* Animated */
  position: relative;
  transition: height 1.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  box-shadow: inset 0 2px 4px rgba(255,255,255,0.4);
}

.bar-fill::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
  animation: bar-shimmer 3s infinite linear;
}

.bar-fill.highlight {
  background: linear-gradient(to top, rgba(var(--tertiary-rgb), 0.2), var(--tertiary), var(--accent));
  box-shadow: inset 0 2px 4px rgba(255,255,255,0.4), 0 0 20px rgba(var(--tertiary-rgb), 0.5);
}

.bar-value {
  position: absolute;
  top: -30px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(255,255,255,0.1);
  backdrop-filter: blur(10px);
  padding: 4px 10px;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 700;
  color: #fff;
  border: 1px solid rgba(255,255,255,0.2);
  opacity: 0;
  transition: opacity 0.5s ease 1.5s;
}

.bar-title {
  margin-top: 1rem;
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--text-primary);
  text-align: center;
}

.chart-animate .bar-fill {
  height: var(--target-height);
}

.chart-animate .bar-value {
  opacity: 1;
}

@keyframes bar-shimmer {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(100%); }
}

@media (max-width: 768px) {
  .premium-bar-chart {
    height: 250px;
  }
  .bar-title {
    font-size: 0.8rem;
  }
  .bar-label {
    font-size: 0.7rem;
  }
  .bar-value {
    font-size: 0.75rem;
    padding: 2px 6px;
  }
}
'''
css = re.sub(old_chart_css_pattern, new_chart_css, css, flags=re.DOTALL)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('styles.css updated successfully.')
