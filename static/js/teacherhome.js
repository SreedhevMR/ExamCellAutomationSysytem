// If you want a custom time control for your slider, you can add a basic JavaScript loop for automatic sliding.
let currentIndex = 0;
const slides = document.querySelectorAll('.slider img');
const totalSlides = slides.length;

function showNextSlide() {
    slides[currentIndex].classList.remove('active');
    currentIndex = (currentIndex + 1) % totalSlides;
    slides[currentIndex].classList.add('active');
}

setInterval(showNextSlide, 5000); // Change slide every 5 seconds
