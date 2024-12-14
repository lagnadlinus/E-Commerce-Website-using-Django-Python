



document.addEventListener("DOMContentLoaded", function () {
    const cartPriceElement = document.querySelector(".cart-price");
    const cartCountElement = document.querySelector(".cart-count");
    const hamburgerMenu = document.getElementById("hamburger-menu");
    const navBar = document.querySelector(".nav-bar");
    

    // Function to update the cart icon and price in the header
    function updateCartInfo() {
        const cart = JSON.parse(localStorage.getItem('cart')) || [];

        // Calculate total price and total item count
        const total = cart.reduce((sum, item) => sum + item.price * item.quantity, 0);
        const itemCount = cart.reduce((sum, item) => sum + item.quantity, 0);

        // Update the cart price and item count
        cartPriceElement.textContent = `$${total.toFixed(2)}`;
        cartCountElement.textContent = itemCount; // Update item count on cart icon

        // Add bounce effect to the cart badge
        cartCountElement.classList.add('bounce');
        setTimeout(() => {
            cartCountElement.classList.remove('bounce');
        }, 500);
    }

    // Fetch cart info on page load to initialize header data
    updateCartInfo();

    // Toggle mobile menu
    hamburgerMenu.addEventListener("click", function () {
        hamburgerMenu.classList.toggle("open");
        navBar.classList.toggle("open");
    });

    // Ensure menu visibility is correct on page reload
    function handleResize() {
        if (window.innerWidth > 768) {
            // Show navigation bar for desktop
            navBar.classList.add("open");
            hamburgerMenu.classList.remove("open");
        } else {
            // Hide navigation bar for mobile
            navBar.classList.remove("open");
        }
    }

    // Call handleResize on page load
    handleResize();

    // Adjust menu visibility on window resize
    window.addEventListener("resize", handleResize);

    // Rebind cart update functionality on adding items (if needed in the future)
    document.querySelectorAll('.add-to-cart').forEach(button => {
        button.addEventListener('click', updateCartInfo);
    });
});
