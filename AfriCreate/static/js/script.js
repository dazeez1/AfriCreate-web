$(document).ready(function(){
    // toggle menu/navbar script
    $('.menu-btn').click(function(){
        $('.navbar .menu').toggleClass("active");
        $('.menu-btn i').toggleClass("active");
    });
});

 // Array of image file paths to be used in the image slider
        let images = [
            "{% static 'images/Art-1.jpg' %}", // 0 
            "{% static 'images/Art-2.jpeg' %}", // 1
            "{% static 'images/Art-3.jpeg' %}", // 2
            "{% static 'images/Art-4.jpeg' %}", // 3
            "{% static 'images/Art-5.jpeg' %}", // 4
        ];



        // Variable to keep track of the index of the current image in the images array
        let currentIndex = 0;

        // Function to show the next image in the slider
        function nextSlide() {
            currentIndex = (currentIndex + 1) % images.length;
            // Set the src attribute of the image element to the new image URL
            document.getElementById("slider-image").src= images[currentIndex];
        }

        // Function to show the previous image in the slider
        function prevSlide() {
            currentIndex = (currentIndex + 1 + images.length) % images.length;
            document.getElementById("slider-image").src= images[currentIndex];
        }

        // Change slide every 5 seconds
        setInterval(nextSlide, 6000); // 6000 milliseconds = 6 seconds

/*  Blog Section */
$(document).ready(function(){
    $('.carousels').owlCarousel({
        margin: 20,
        loop: true,
        autoplay: true,
        autoplayTimeout: 2000,
        autoplayHoverPause: true,
        responsive: {
            0: {
                items: 1,
                nav: false
            },
            600: {
                items: 2,
                nav: false
            },
            1000: {
                items: 3, /* This makes 3 items show on larger screens */
                nav: false
            }
        }
    });
});

    // scroll-up button show/hide script
    if(this.scrollY > 500){
            $('.scroll-up-btn').addClass("show");
        }else{
            $('.scroll-up-btn').removeClass("show");
        }

    // slide-up script
    $('.scroll-up-btn').click(function(){
        $('html').animate({scrollTop: 0});
        // removing smooth scroll on slide-up button click
        $('html').css("scrollBehavior", "auto");
    });

    $('.navbar .menu li a').click(function(){
        // applying again smooth scroll on menu items click
        $('html').css("scrollBehavior", "smooth");
    });


    //Form Toggle
document.addEventListener("DOMContentLoaded", function() {
    const getStartedBtn = document.getElementById("getStartedBtn");
    const formContainer = document.getElementById("formContainer");

    getStartedBtn.addEventListener("click", function() {
        formContainer.style.display = formContainer.style.display === "none" ? "block" : "none";
    });

        cancelIcon.addEventListener("click", function() {
        formContainer.style.display = "none"; // Hide the form
        overlay.style.display = "none"; // Hide the overlay
    });
});


