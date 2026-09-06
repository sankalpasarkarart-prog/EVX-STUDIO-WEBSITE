document.addEventListener("DOMContentLoaded", () => {
    // ---- State ----
    let cart = []; // Array of { id, name, price, qty, isRetainer }
    let appliedCoupon = null; // { code, discountPercent }

    const coupons = {
        "PAYWITHWISE": 3,
        "2NDORDERR": 5,
        "3RDORDER": 7,
        "4THORDER": 10
    };

    // ---- Elements ----
    const cartOverlay = document.getElementById("cartOverlay");
    const cartDrawer = document.getElementById("cartDrawer");
    const cartClose = document.getElementById("cartClose");
    const cartFloatingBtn = document.getElementById("cartFloatingBtn");
    const cartBadge = document.getElementById("cartBadge");
    const cartItemsDiv = document.getElementById("cartItems");
    
    const cartSubtotalEl = document.getElementById("cartSubtotal");
    const cartDiscountRow = document.getElementById("cartDiscountRow");
    const appliedCouponNameEl = document.getElementById("appliedCouponName");
    const cartDiscountEl = document.getElementById("cartDiscount");
    const cartTotalINREl = document.getElementById("cartTotalINR");
    const cartTotalUSDEl = document.getElementById("cartTotalUSD");
    
    const couponInput = document.getElementById("couponInput");
    const applyCouponBtn = document.getElementById("applyCouponBtn");
    const couponMessage = document.getElementById("couponMessage");
    const checkoutBtn = document.getElementById("checkoutBtn");
    
    // Add to Cart Buttons
    const singleAddBtns = document.querySelectorAll('.add-to-cart-btn');
    const addRetainerBtn = document.getElementById('addRetainerBtn');

    // ---- Functions ----
    function openCart() {
        cartOverlay.classList.add("active");
        cartDrawer.classList.add("active");
    }

    function closeCart() {
        cartOverlay.classList.remove("active");
        cartDrawer.classList.remove("active");
    }

    function renderCart() {
        cartItemsDiv.innerHTML = "";
        let totalQty = 0;
        let subtotal = 0;

        if (cart.length === 0) {
            cartItemsDiv.innerHTML = "<div class='cart-empty-msg'>Your cart is empty.</div>";
        } else {
            cart.forEach((item, index) => {
                totalQty += item.qty;
                subtotal += (item.price * item.qty);

                const div = document.createElement("div");
                div.className = "cart-item";
                
                // Qty controls logic
                let qtyControls = "";
                if (item.isRetainer) {
                    // Retainer is single item (price is already calculated dynamically), no qty adjustments in cart
                    qtyControls = `<div style="font-size: 0.9rem; color: var(--text-muted);">1x Retainer</div>`;
                } else {
                    qtyControls = `
                        <div class="cart-item-qty">
                            <button onclick="updateQty(${index}, -1)">-</button>
                            <span>${item.qty}</span>
                            <button onclick="updateQty(${index}, 1)">+</button>
                        </div>
                    `;
                }

                div.innerHTML = `
                    <div class="cart-item-info">
                        <h4>${item.name}</h4>
                        <p>₹${item.price.toLocaleString('en-IN')}</p>
                    </div>
                    <div style="display: flex; align-items: center;">
                        ${qtyControls}
                        <button class="cart-item-remove" onclick="removeItem(${index})"><i class="ri-delete-bin-line"></i></button>
                    </div>
                `;
                cartItemsDiv.appendChild(div);
            });
        }

        cartBadge.textContent = totalQty;
        cartSubtotalEl.textContent = `₹${subtotal.toLocaleString('en-IN')}`;

        // Apply discount if any
        let discountAmt = 0;
        if (appliedCoupon && subtotal > 0) {
            discountAmt = subtotal * (appliedCoupon.discountPercent / 100);
            cartDiscountRow.style.display = "flex";
            appliedCouponNameEl.textContent = appliedCoupon.code;
            cartDiscountEl.textContent = `-₹${Math.round(discountAmt).toLocaleString('en-IN')}`;
        } else {
            cartDiscountRow.style.display = "none";
        }

        const netTotal = subtotal - discountAmt;
        cartTotalINREl.textContent = `₹${Math.round(netTotal).toLocaleString('en-IN')}`;
        cartTotalUSDEl.textContent = `≈ $${(netTotal / 94.5).toFixed(2)}`;
    }

    // Expose window functions for inline onclick in renderCart
    window.updateQty = function(index, delta) {
        if (!cart[index] || cart[index].isRetainer) return;
        const newQty = cart[index].qty + delta;
        if (newQty > 0 && newQty <= 3) {
            cart[index].qty = newQty;
            renderCart();
        } else if (newQty === 0) {
            removeItem(index);
        } else if (newQty > 3) {
            alert("Maximum quantity for a single service is 3.");
        }
    };

    window.removeItem = function(index) {
        cart.splice(index, 1);
        renderCart();
    };

    // ---- Event Listeners ----
    cartFloatingBtn.addEventListener("click", openCart);
    cartClose.addEventListener("click", closeCart);
    cartOverlay.addEventListener("click", closeCart);

    // Single video add
    singleAddBtns.forEach(btn => {
        btn.addEventListener("click", () => {
            const id = btn.getAttribute("data-id");
            const name = btn.getAttribute("data-name");
            const price = parseInt(btn.getAttribute("data-price"));

            const existing = cart.find(item => item.id === id);
            if (existing) {
                if (existing.qty < 3) {
                    existing.qty += 1;
                } else {
                    alert("Maximum quantity for a single service is 3.");
                    openCart();
                    return;
                }
            } else {
                cart.push({ id, name, price, qty: 1, isRetainer: false });
            }
            renderCart();
            openCart();
        });
    });

    // Retainer add
    if (addRetainerBtn) {
        addRetainerBtn.addEventListener("click", () => {
            const videoCount = document.getElementById("videoCount").value;
            const priceStr = document.getElementById("priceINR").textContent.replace(/,/g, '');
            const price = parseInt(priceStr);
            
            // Remove existing retainer if any, replace with new calculation
            cart = cart.filter(item => !item.isRetainer);
            
            cart.push({
                id: 'retainer',
                name: `Monthly Retainer (${videoCount} videos)`,
                price: price,
                qty: 1,
                isRetainer: true
            });
            renderCart();
            openCart();
        });
    }

    // Apply Coupon
    applyCouponBtn.addEventListener("click", () => {
        const code = couponInput.value.trim().toUpperCase();
        if (!code) {
            appliedCoupon = null;
            couponMessage.style.display = "none";
            renderCart();
            return;
        }

        if (coupons[code]) {
            appliedCoupon = { code: code, discountPercent: coupons[code] };
            couponMessage.style.display = "block";
            couponMessage.style.color = "#00e676";
            couponMessage.textContent = `Coupon applied! ${coupons[code]}% off.`;
            couponInput.value = "";
        } else {
            appliedCoupon = null;
            couponMessage.style.display = "block";
            couponMessage.style.color = "#ff4757";
            couponMessage.textContent = "Invalid coupon code.";
        }
        renderCart();
    });

    // Checkout
    checkoutBtn.addEventListener("click", () => {
        if (cart.length === 0) {
            alert("Your cart is empty.");
            return;
        }

        let message = "Hi EVX STUDIO, I would like to place an order:\n\n";
        
        let subtotal = 0;
        cart.forEach(item => {
            subtotal += (item.price * item.qty);
            message += `- ${item.qty}x ${item.name} = ₹${(item.price * item.qty).toLocaleString('en-IN')}\n`;
        });
        
        message += `\nSubtotal: ₹${subtotal.toLocaleString('en-IN')}`;
        
        if (appliedCoupon) {
            const discountAmt = Math.round(subtotal * (appliedCoupon.discountPercent / 100));
            const netTotal = subtotal - discountAmt;
            message += `\nCoupon Applied: ${appliedCoupon.code} (${appliedCoupon.discountPercent}% off)`;
            message += `\nDiscount: -₹${discountAmt.toLocaleString('en-IN')}`;
            message += `\n*Net Amount: ₹${netTotal.toLocaleString('en-IN')} (approx $${(netTotal/94.5).toFixed(2)})*`;
        } else {
            message += `\n*Net Amount: ₹${subtotal.toLocaleString('en-IN')} (approx $${(subtotal/94.5).toFixed(2)})*`;
        }
        
        message += "\n\nPlease let me know how to proceed with the payment and next steps.";

        const whatsappUrl = `https://wa.me/+919239048684?text=${encodeURIComponent(message)}`;
        if (window.openWhatsAppWithTerms) { window.openWhatsAppWithTerms(whatsappUrl); } else { window.open(whatsappUrl, "_blank"); }
    });

    // Init empty
    renderCart();
});
