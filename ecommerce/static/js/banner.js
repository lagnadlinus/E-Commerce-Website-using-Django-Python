// JavaScript for auto-changing banner slides
let slideIndex = 0;

function showSlide(index) {
    const slides = document.querySelectorAll(".slides img");
    const dots = document.querySelectorAll(".nav-dot");

    slides.forEach((slide, i) => {
        slide.style.display = i === index ? "block" : "none";
        dots[i].classList.toggle("active", i === index);
    });
}

function currentSlide(index) {
    slideIndex = index - 1; // Adjust for 0-based indexing
    showSlide(slideIndex);
}

function autoSlide() {
    const slides = document.querySelectorAll(".slides img");
    slideIndex = (slideIndex + 1) % slides.length;
    showSlide(slideIndex);
}

// Start the slideshow
setInterval(autoSlide, 5000); // Change slide every 5 seconds
document.addEventListener("DOMContentLoaded", () => showSlide(slideIndex));
