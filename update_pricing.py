import re
with open('pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_pricing_html = '''    <!-- ======== SINGLE VIDEOS ======== -->
    <section class="section" id="pricing-single" style="padding-top: 150px; padding-bottom: 2rem;">
        <div class="section-header animate-in">
            <span class="section-tag glass">SINGLE VIDEOS</span>
            <h2 class="section-title">Short Video <span class="gradient-text">Pricing</span></h2>
            <p class="section-subtitle">Prices below are for short videos, calculated per minute. Minimum chargeable duration is 1 minute.</p>
        </div>
        
        <div class="pricing-grid-single animate-in">
            <div class="pricing-card-single glass tilt-card">
                <h3>Normal Clean Editing</h3>
                <p class="price-desc">Minimal cuts, captions, and transitions</p>
                <div class="price-amt">
                    <span class="currency">₹</span>600 <span class="usd-approx">/ ~$6.35</span>
                </div>
            </div>
            
            <div class="pricing-card-single glass tilt-card">
                <h3>Shorts with Motion Graphics</h3>
                <p class="price-desc">Engaging visuals and standard motion graphics</p>
                <div class="price-amt">
                    <span class="currency">₹</span>900 <span class="usd-approx">/ ~$9.52</span>
                </div>
            </div>
            
            <div class="pricing-card-single glass tilt-card">
                <h3>Documentary Style</h3>
                <p class="price-desc">Story-driven editing with b-roll and sound design</p>
                <div class="price-amt">
                    <span class="currency">₹</span>1,100 <span class="usd-approx">/ ~$11.64</span>
                </div>
            </div>
            
            <div class="pricing-card-single glass tilt-card">
                <h3>Real Estate Shorts</h3>
                <p class="price-desc">Stunning property showcases and walkthroughs</p>
                <div class="price-amt">
                    <span class="currency">₹</span>1,500 <span class="usd-approx">/ ~$15.87</span>
                </div>
            </div>
            
            <div class="pricing-card-single glass-strong tilt-card highlight">
                <h3>Advanced Motion Graphics</h3>
                <p class="price-desc">Complex animations and high-end visual effects</p>
                <div class="price-amt">
                    <span class="currency" style="color: var(--accent);">₹</span>1,700 <span class="usd-approx">/ ~$17.99</span>
                </div>
            </div>
        </div>
        
        <div style="text-align: center; margin-top: 3rem;" class="animate-in">
            <p style="color: var(--text-secondary); font-size: 1.1rem;">For detailed pricing, you can <a href="/#contact" class="gradient-text" style="font-weight: 600;">contact us</a>.</p>
        </div>
    </section>

    <!-- ======== CALCULATOR SECTION ======== -->
    <section class="section section-alt" id="pricing-calculator">
        <div class="section-header animate-in">
            <span class="section-tag glass">MONTHLY RETAINER</span>
            <h2 class="section-title">Price <span class="gradient-text">Calculator</span></h2>
            <p class="section-subtitle">Choose the amount of videos per month to estimate your retainer.</p>
        </div>
        
        <div class="calculator-container glass-strong animate-in">
            <div class="calculator-controls">
                <label for="videoCount">Videos per month: <span id="videoCountDisplay" class="gradient-text">3</span></label>
                <input type="range" id="videoCount" min="3" max="20" value="3" class="pricing-slider">
                <div class="slider-labels">
                    <span>3</span>
                    <span>20</span>
                </div>
            </div>
            
            <div class="calculator-results">
                <div class="price-display">
                    <span class="price-currency">₹</span>
                    <span class="price-amount" id="priceINR">5,000</span>
                    <span class="price-period">/mo</span>
                </div>
                <div class="price-display-usd">
                    <span>≈ $</span>
                    <span id="priceUSD">52.91</span>
                    <span>/mo</span>
                </div>
                <div class="per-video-breakdown glass">
                    <i class="ri-pie-chart-2-line"></i>
                    <span>Per video cost: <strong id="perVideoINR" style="color: var(--accent);">₹1,666</strong> (≈ $<span id="perVideoUSD">17.63</span>)</span>
                </div>
            </div>
            
            <div class="calculator-disclaimer">
                <p><i class="ri-information-line"></i> * This is only the starting price. The main pricing and the original pricing may vary on the complexity of the work.</p>
            </div>
        </div>
    </section>

    <!-- ======== FOOTER ======== -->'''

html = re.sub(r'<!-- ======== PRICING PAGE HEADER ======== -->.*?<!-- ======== FOOTER ======== -->', new_pricing_html, html, flags=re.DOTALL)

# Let's also inject the javascript for the calculator at the bottom of the body
script = '''
<script>
    document.addEventListener("DOMContentLoaded", () => {
        const slider = document.getElementById("videoCount");
        const countDisplay = document.getElementById("videoCountDisplay");
        const priceINR = document.getElementById("priceINR");
        const priceUSD = document.getElementById("priceUSD");
        const perVideoINR = document.getElementById("perVideoINR");
        const perVideoUSD = document.getElementById("perVideoUSD");
        
        const conversionRate = 94.5;
        
        function updatePricing() {
            const count = parseInt(slider.value);
            countDisplay.textContent = count;
            
            let totalINR = 5000;
            if (count > 3) {
                totalINR += (count - 3) * 1100;
            }
            
            const totalUSD = totalINR / conversionRate;
            const perVidINR = Math.round(totalINR / count);
            const perVidUSD = perVidINR / conversionRate;
            
            priceINR.textContent = totalINR.toLocaleString('en-IN');
            priceUSD.textContent = totalUSD.toFixed(2);
            
            perVideoINR.textContent = "₹" + perVidINR.toLocaleString('en-IN');
            perVideoUSD.textContent = perVidUSD.toFixed(2);
            
            // Update slider gradient fill
            const percentage = ((count - 3) / (20 - 3)) * 100;
            slider.style.background = `linear-gradient(to right, var(--accent) 0%, var(--tertiary) ${percentage}%, rgba(255, 255, 255, 0.1) ${percentage}%, rgba(255, 255, 255, 0.1) 100%)`;
        }
        
        if(slider) {
            slider.addEventListener("input", updatePricing);
            updatePricing();
        }
    });
</script>
'''

if 'id="videoCount"' not in html:
    pass # Wait, I just injected it. It will be there.

if 'const conversionRate = 94.5;' not in html:
    html = html.replace('</body>', script + '\n</body>')

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(html)
