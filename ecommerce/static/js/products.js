



// Initialize cart in localStorage if not present
if (!localStorage.getItem('cart')) {
    localStorage.setItem('cart', JSON.stringify([]));
}

// Utility functions
function getCart() {
    return JSON.parse(localStorage.getItem('cart')) || [];
}

function saveCart(cart) {
    localStorage.setItem('cart', JSON.stringify(cart));
}

function updateCartInfo() {
    const cart = getCart();
    const cartBadge = document.querySelector('.cart-badge');
    const totalQuantity = cart.reduce((sum, item) => sum + item.quantity, 0);
    if (cartBadge) {
        cartBadge.textContent = totalQuantity;
    }
}

// Add event listener for Add to Cart buttons
document.querySelectorAll('.add-to-cart').forEach(button => {
    button.addEventListener('click', function () {
        const productId = this.dataset.id;
        const productName = this.dataset.name;
        const productPrice = parseFloat(this.dataset.price); // Ensure price is a number
        const productImage = this.dataset.image;
        const quantityInput = document.getElementById(`quantity-${productId}`);
        const quantity = quantityInput ? Math.max(1, parseInt(quantityInput.value) || 1) : 1;

        const cart = getCart();

        // Check if product exists in the cart
        const existingProduct = cart.find(item => item.id === productId);
        if (existingProduct) {
            existingProduct.quantity += quantity;
        } else {
            cart.push({
                id: productId,
                name: productName,
                price: productPrice,
                image: productImage,
                quantity: quantity,
            });
        }

        saveCart(cart);

        // Animation logic
        const productImageElement = this.closest('.product-item').querySelector('img');
        const cartIcon = document.querySelector('.cart-button');

        const flyingImage = productImageElement.cloneNode(true);
        flyingImage.style.position = 'fixed';
        flyingImage.style.width = '50px';
        flyingImage.style.height = '50px';
        flyingImage.style.transition = 'all 0.8s ease-out';
        flyingImage.style.pointerEvents = 'none';

        const productRect = productImageElement.getBoundingClientRect();
        const cartRect = cartIcon.getBoundingClientRect();

        flyingImage.style.left = `${productRect.left}px`;
        flyingImage.style.top = `${productRect.top}px`;
        document.body.appendChild(flyingImage);

        setTimeout(() => {
            flyingImage.style.left = `${cartRect.left + cartRect.width / 2}px`;
            flyingImage.style.top = `${cartRect.top + cartRect.height / 2}px`;
            flyingImage.style.opacity = '0';
        }, 10);

        setTimeout(() => {
            flyingImage.remove();
            updateCartInfo();
        }, 800);
    });
});

// Initialize cart badge on page load
updateCartInfo();
