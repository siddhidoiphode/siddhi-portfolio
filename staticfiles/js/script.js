// Get all images in the gallery
var images = document.querySelectorAll('.gallery img');

// Add click event for zooming
images.forEach(function(image) {
    image.addEventListener('click', function(event) {
        // If the image is already zoomed, remove the zoom
        if (image.classList.contains('zoomed')) {
            image.classList.remove('zoomed');
        } else {
            // Zoom the image
            images.forEach(function(img) {
                img.classList.remove('zoomed');  // Remove zoom from all images
            });
            image.classList.add('zoomed');
        }
        event.stopPropagation();  // Prevent click event from bubbling up to the window
    });
});

// Close zoom effect when clicking anywhere else
window.addEventListener('click', function() {
    images.forEach(function(image) {
        image.classList.remove('zoomed');  // Remove zoom effect from all images
    });
});





document.addEventListener("DOMContentLoaded", function () {
    let navbar = document.querySelector(".navbar");

    // Ensure background is always visible
    navbar.classList.remove("bg-transparent");
    navbar.style.background = "rgb(219, 204, 38)";

    // Override Bootstrap's scroll behavior
    window.addEventListener("scroll", function () {
        navbar.style.background = "rgb(195, 31, 31)";
    });
});



document.addEventListener("DOMContentLoaded", function () {
    let navbarToggler = document.querySelector(".navbar-toggler");
    let navbarCollapse = document.querySelector(".navbar-collapse");

    navbarToggler.addEventListener("click", function () {
        navbarCollapse.classList.toggle("show");
    });
});
