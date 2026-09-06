import re
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css = '''
/* ============================================================
   SINGLE VIDEO PRICING GRID
   ============================================================ */
.pricing-grid-single {
    display: flex;
    flex-wrap: wrap;
    gap: 1.5rem;
    justify-content: center;
    max-width: 1200px;
    margin: 0 auto 3rem;
}

.pricing-card-single {
    flex: 1 1 300px;
    padding: 2.5rem 2rem;
    border-radius: var(--radius-card);
    text-align: center;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 250px;
    transition: transform var(--transition-base), box-shadow var(--transition-base);
}

.pricing-card-single:hover {
    transform: translateY(-10px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.4), inset 0 1px 2px rgba(255,255,255,0.2);
}

.pricing-card-single.highlight {
    border: 1px solid rgba(var(--accent-rgb), 0.5);
    box-shadow: 0 10px 30px rgba(var(--accent-rgb), 0.15), inset 0 1px 2px rgba(255,255,255,0.2);
}

.pricing-card-single.highlight::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 4px;
    background: linear-gradient(90deg, var(--accent), var(--tertiary));
}

.pricing-card-single h3 {
    font-size: 1.5rem;
    font-family: var(--font-heading);
    margin-bottom: 0.5rem;
    color: var(--text-primary);
}

.price-desc {
    color: var(--text-secondary);
    font-size: 0.95rem;
    margin-bottom: 1.5rem;
    flex-grow: 1;
}

.price-amt {
    font-size: 2.5rem;
    font-weight: 800;
    font-family: var(--font-heading);
    color: var(--text-primary);
    display: flex;
    align-items: baseline;
    justify-content: center;
    gap: 0.25rem;
}

.price-amt .currency {
    font-size: 1.5rem;
    font-weight: 600;
    color: var(--text-secondary);
}

.price-amt .usd-approx {
    font-size: 1rem;
    font-weight: 500;
    color: var(--text-muted);
    margin-left: 0.5rem;
}

/* ============================================================
   CALCULATOR SECTION
   ============================================================ */
.calculator-container {
    max-width: 800px;
    margin: 4rem auto;
    padding: 4rem 3rem;
    border-radius: calc(var(--radius-card) * 1.5);
    text-align: center;
    position: relative;
    overflow: hidden;
}

.calculator-controls {
    margin-bottom: 3rem;
}

.calculator-controls label {
    display: block;
    font-size: 1.4rem;
    font-family: var(--font-heading);
    margin-bottom: 2rem;
    color: var(--text-secondary);
}

.pricing-slider {
    -webkit-appearance: none;
    width: 100%;
    height: 12px;
    border-radius: 10px;
    background: rgba(255, 255, 255, 0.1);
    outline: none;
    transition: background 0.3s;
    cursor: pointer;
}

.pricing-slider::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background: #fff;
    box-shadow: 0 0 20px rgba(var(--accent-rgb), 0.8), inset 0 -2px 5px rgba(0,0,0,0.2);
    cursor: grab;
    transition: transform 0.2s;
    border: 3px solid var(--accent);
}

.pricing-slider::-webkit-slider-thumb:active {
    cursor: grabbing;
    transform: scale(1.15);
}

.slider-labels {
    display: flex;
    justify-content: space-between;
    margin-top: 1rem;
    color: var(--text-muted);
    font-weight: 600;
    font-size: 0.9rem;
}

.calculator-results {
    background: rgba(0,0,0,0.2);
    padding: 3rem;
    border-radius: var(--radius-card);
    border: 1px solid rgba(255,255,255,0.05);
    margin-bottom: 2rem;
}

.price-display {
    display: flex;
    align-items: baseline;
    justify-content: center;
    gap: 0.5rem;
    margin-bottom: 0.5rem;
}

.price-display .price-currency {
    font-size: 2.5rem;
    font-weight: 600;
    color: var(--accent);
}

.price-display .price-amount {
    font-size: 5rem;
    font-weight: 900;
    font-family: var(--font-heading);
    line-height: 1;
    background: linear-gradient(to right, #fff, rgba(255,255,255,0.7));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -2px;
}

.price-display .price-period {
    font-size: 1.5rem;
    color: var(--text-muted);
    font-weight: 500;
}

.price-display-usd {
    font-size: 1.4rem;
    color: var(--text-secondary);
    font-weight: 500;
    margin-bottom: 2.5rem;
}

.per-video-breakdown {
    display: inline-flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.8rem 1.5rem;
    border-radius: var(--radius-pill);
    font-size: 1rem;
    color: var(--text-secondary);
    border: 1px solid rgba(255,255,255,0.1);
}

.calculator-disclaimer {
    color: var(--text-muted);
    font-size: 0.85rem;
    text-align: left;
    max-width: 600px;
    margin: 0 auto;
    line-height: 1.5;
}

@media (max-width: 768px) {
    .calculator-container {
        padding: 3rem 1.5rem;
    }
    .price-display .price-amount {
        font-size: 3.5rem;
    }
    .price-display .price-currency {
        font-size: 2rem;
    }
    .calculator-results {
        padding: 2rem 1rem;
    }
}
'''
if 'SINGLE VIDEO PRICING GRID' not in css:
    css = css + '\n' + new_css

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('styles updated.')
