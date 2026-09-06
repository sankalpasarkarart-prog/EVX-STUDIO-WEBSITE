import re
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css = '''
/* ============================================================
   SHOPPING CART DRAWER
   ============================================================ */
.cart-overlay {
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0,0,0,0.5);
    backdrop-filter: blur(5px);
    z-index: 1000;
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.3s ease;
}
.cart-overlay.active {
    opacity: 1;
    visibility: visible;
}
.cart-drawer {
    position: fixed;
    top: 0; right: -450px; width: 450px; height: 100%;
    max-width: 100vw;
    background: rgba(10,10,12,0.95);
    border-left: 1px solid rgba(255,255,255,0.1);
    box-shadow: -10px 0 30px rgba(0,0,0,0.5);
    z-index: 1001;
    display: flex;
    flex-direction: column;
    transition: right 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}
.cart-drawer.active {
    right: 0;
}
.cart-header {
    padding: 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(255,255,255,0.1);
}
.cart-header h3 {
    font-size: 1.5rem;
    font-family: var(--font-heading);
    margin: 0;
}
.cart-close {
    background: none; border: none; color: white;
    font-size: 1.5rem; cursor: pointer;
    transition: color 0.2s;
}
.cart-close:hover { color: var(--accent); }
.cart-items {
    flex-grow: 1;
    padding: 2rem;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}
.cart-empty-msg {
    text-align: center; color: var(--text-muted); margin-top: 2rem;
}
.cart-item {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: var(--radius-card);
    padding: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.cart-item-info h4 {
    margin: 0 0 0.5rem 0;
    font-size: 1rem;
}
.cart-item-info p {
    margin: 0; color: var(--accent); font-weight: 600;
}
.cart-item-qty {
    display: flex; align-items: center; gap: 0.5rem;
    background: rgba(0,0,0,0.3); padding: 0.2rem 0.5rem; border-radius: var(--radius-sm);
}
.cart-item-qty button {
    background: none; border: none; color: white; cursor: pointer;
    font-size: 1.2rem;
}
.cart-item-qty span { font-weight: 600; width: 15px; text-align: center;}
.cart-item-remove {
    background: none; border: none; color: #ff4757; cursor: pointer;
    margin-left: 1rem; font-size: 1.2rem;
}
.cart-footer {
    padding: 2rem;
    background: rgba(0,0,0,0.5);
    border-top: 1px solid rgba(255,255,255,0.1);
}
.cart-subtotal {
    display: flex; justify-content: space-between; font-weight: 600; font-size: 1.1rem; margin-bottom: 1rem;
}
.cart-coupon {
    display: flex; gap: 0.5rem; margin-top: 1rem;
}
.cart-coupon input {
    flex-grow: 1; padding: 0.8rem; border-radius: var(--radius-sm);
    border: 1px solid rgba(255,255,255,0.1); background: rgba(0,0,0,0.3); color: white;
}
.cart-coupon button {
    padding: 0 1.5rem;
}
.cart-floating-btn {
    position: fixed; bottom: 2rem; right: 2rem;
    width: 60px; height: 60px; border-radius: 50%;
    background: linear-gradient(135deg, var(--accent), var(--tertiary));
    color: white; font-size: 1.5rem; border: none;
    box-shadow: 0 10px 20px rgba(var(--accent-rgb), 0.4);
    cursor: pointer; z-index: 999;
    display: flex; justify-content: center; align-items: center;
    transition: transform 0.3s;
}
.cart-floating-btn:hover {
    transform: scale(1.1);
}
.cart-badge {
    position: absolute; top: -5px; right: -5px;
    background: #ff4757; color: white; font-size: 0.8rem; font-weight: 700;
    width: 24px; height: 24px; border-radius: 50%;
    display: flex; justify-content: center; align-items: center;
    box-shadow: 0 2px 5px rgba(0,0,0,0.5);
}
'''

if 'SHOPPING CART DRAWER' not in css:
    css = css + '\n' + new_css

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
print('styles updated.')
