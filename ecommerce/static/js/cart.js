



// Function to render the cart
function renderCart() {
    const cartItemsContainer = document.querySelector('.cart-items');
    const cartSummaryContainer = document.querySelector('.cart-summary');
    
    // Clear previous items
    cartItemsContainer.innerHTML = '';
    cartSummaryContainer.innerHTML = '';

    // Retrieve cart from localStorage
    const cart = JSON.parse(localStorage.getItem('cart')) || [];

    if (cart.length === 0) {
        cartItemsContainer.innerHTML = '<p>Your cart is empty.</p>';
        return;
    }

    // Populate cart items
    let totalPrice = 0;

    cart.forEach(item => {
        totalPrice += item.price * item.quantity;

        const cartItemHTML = `
            <div class="cart-item">
                <img src="${item.image}" alt="${item.name}">
                <h3>${item.name}</h3>
                <input type="number" value="${item.quantity}" min="1" data-id="${item.id}" class="quantity-input">
                <p>$${(item.price * item.quantity).toFixed(2)}</p>
                <button class="remove-item" data-id="${item.id}">Remove</button>
            </div>
        `;
        cartItemsContainer.innerHTML += cartItemHTML;
    });

    // Add cart summary
    const summaryHTML = `
        <h2>Total: $${totalPrice.toFixed(2)}</h2>
        <button class="btn checkout-btn">Proceed to Checkout</button>
    `;
    cartSummaryContainer.innerHTML = summaryHTML;

    // Add event listeners for quantity update and remove actions
    setupCartActions();
}

// Function to set up cart actions
function setupCartActions() {
    // Update quantity
    document.querySelectorAll('.quantity-input').forEach(input => {
        input.addEventListener('change', function () {
            const newQuantity = parseInt(this.value) || 1;
            const productId = this.dataset.id;

            const cart = JSON.parse(localStorage.getItem('cart'));
            const product = cart.find(item => item.id === productId);
            if (product) {
                product.quantity = newQuantity;
            }

            localStorage.setItem('cart', JSON.stringify(cart));
            renderCart();
        });
    });

    // Remove item
    document.querySelectorAll('.remove-item').forEach(button => {
        button.addEventListener('click', function () {
            const productId = this.dataset.id;

            let cart = JSON.parse(localStorage.getItem('cart'));
            cart = cart.filter(item => item.id !== productId);

            localStorage.setItem('cart', JSON.stringify(cart));
            renderCart();
        });
    });
}

// Render the cart on page load
document.addEventListener('DOMContentLoaded', renderCart);
