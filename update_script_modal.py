import re
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

new_modal_html = '''
    modal.innerHTML = `
        <h3>Notice</h3>
        <p>If you take our service, you agree to our <a href="/terms.html" style="color: var(--accent); text-decoration: underline;">Terms and Conditions</a>.</p>
        <div class="terms-modal-actions">
            <button class="terms-modal-btn terms-modal-btn-cancel">Cancel</button>
            <button class="terms-modal-btn terms-modal-btn-agree">OK, Continue</button>
        </div>
    `;
'''

js = re.sub(r'modal\.innerHTML = `.*?`;', new_modal_html.strip(), js, flags=re.DOTALL)

# Now expose a function
expose_func = '''
    // Expose globally for cart.js
    window.openWhatsAppWithTerms = function(url) {
        pendingWhatsAppUrl = url;
        overlay.classList.add('active');
    };
'''

js = js.replace('// Handle cancel', expose_func + '\n    // Handle cancel')

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
print('script.js updated.')
