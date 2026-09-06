import re

with open('pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the script block entirely
script_block = '''<script>
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
</script>'''

html = re.sub(r'<script>.*?</script>', script_block, html, flags=re.DOTALL)

# Also fix the initial HTML values
html = re.sub(r'id="perVideoINR" style="color: var\(--accent\);">.*?</strong>', 'id="perVideoINR" style="color: var(--accent);">₹1,666</strong>', html)
html = html.replace('(%^ $<span', '(≈ $<span')
html = html.replace('( $<span', '(≈ $<span')
html = html.replace('(? $<span', '(≈ $<span')
html = html.replace('(≈ $<span', '(≈ $<span') # in case there are weird characters before ≈

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(html)
