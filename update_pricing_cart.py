import re
with open('pricing.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix typo
html = html.replace('1₹00', '1,100')

# 2. Fix Contact Us Link
old_contact = '<a href="/#contact" class="gradient-text" style="font-weight: 600;">contact us</a>'
new_contact = '<a href="https://wa.me/+919239048684?text=can%20I%20get%20more%20information%20about%20the%20pricing%3F" target="_blank" class="gradient-text" style="font-weight: 600;">contact us</a>'
html = html.replace(old_contact, new_contact)

# 3. Add to Cart buttons for single videos
button_html = '''
                <button class="btn-primary add-to-cart-btn" style="margin-top: 1.5rem; width: 100%; padding: 0.8rem; font-size: 0.95rem;" data-id="{id}" data-name="{name}" data-price="{price}">
                    <i class="ri-shopping-cart-2-line"></i> Add to Cart
                </button>'''

names_prices = [
    ('single-clean', 'Normal Clean Editing', 600),
    ('single-motion', 'Shorts with Motion Graphics', 900),
    ('single-doc', 'Documentary Style', 1100),
    ('single-realestate', 'Real Estate Shorts', 1500),
    ('single-advanced', 'Advanced Motion Graphics', 1700)
]

for vid_id, name, price in names_prices:
    pattern = rf'(<h3>{name}</h3>.*?<div class="price-amt">.*?</div>)'
    replacement = r'\g<1>' + button_html.format(id=vid_id, name=name, price=price)
    html = re.sub(pattern, replacement, html, flags=re.DOTALL)

# 4. Add to Cart button for Calculator
calc_btn_html = '''
            <div style="margin-top: 2rem;">
                <button class="btn-primary" id="addRetainerBtn" style="padding: 1rem 2.5rem; font-size: 1.1rem;">
                    <i class="ri-shopping-cart-2-line"></i> Add Retainer to Cart
                </button>
            </div>'''
html = html.replace('<div class="calculator-disclaimer">', calc_btn_html + '\n            <div class="calculator-disclaimer" style="margin-top: 2rem;">')

# 5. Add Cart UI at the end of body
cart_html = '''
    <!-- ======== SHOPPING CART ======== -->
    <div class="cart-overlay" id="cartOverlay"></div>
    <div class="cart-drawer glass-strong" id="cartDrawer">
        <div class="cart-header">
            <h3>Your Cart</h3>
            <button class="cart-close" id="cartClose"><i class="ri-close-line"></i></button>
        </div>
        <div class="cart-items" id="cartItems">
            <!-- Items injected by JS -->
        </div>
        <div class="cart-footer">
            <div class="cart-subtotal">
                <span>Subtotal</span>
                <span id="cartSubtotal">₹0</span>
            </div>
            <div class="cart-coupon">
                <input type="text" id="couponInput" placeholder="Coupon code (e.g. PAYWITHWISE)">
                <button id="applyCouponBtn" class="btn-secondary">Apply</button>
            </div>
            <p id="couponMessage" style="font-size: 0.8rem; color: #ff4757; margin-top: 0.5rem; display: none;"></p>
            <div class="cart-discount" id="cartDiscountRow" style="display: none; justify-content: space-between; margin-top: 1rem; color: #00e676; font-weight: 600;">
                <span>Discount (<span id="appliedCouponName"></span>)</span>
                <span id="cartDiscount">-₹0</span>
            </div>
            <div class="cart-total" style="display: flex; justify-content: space-between; align-items: flex-end; margin-top: 1.5rem; padding-top: 1.5rem; border-top: 1px solid rgba(255,255,255,0.1);">
                <span style="font-size: 1.2rem; font-weight: 600;">Net Amount</span>
                <div style="text-align: right;">
                    <span id="cartTotalINR" style="display: block; font-size: 1.8rem; font-weight: 800; color: var(--accent);">₹0</span>
                    <span id="cartTotalUSD" style="font-size: 1rem; color: var(--text-muted);">≈ $0.00</span>
                </div>
            </div>
            <button class="btn-primary checkout-btn" id="checkoutBtn" style="width: 100%; margin-top: 1.5rem; padding: 1rem; font-size: 1.1rem; justify-content: center;">
                <i class="ri-whatsapp-line" style="font-size: 1.4rem;"></i> Checkout via WhatsApp
            </button>
        </div>
    </div>
    <button class="cart-floating-btn" id="cartFloatingBtn">
        <i class="ri-shopping-cart-2-line"></i>
        <span class="cart-badge" id="cartBadge">0</span>
    </button>
    <script src="cart.js"></script>
'''
if '<!-- ======== SHOPPING CART ======== -->' not in html:
    html = html.replace('</body>', cart_html + '\n</body>')

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('pricing.html updated.')
