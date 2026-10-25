document.addEventListener("DOMContentLoaded", function () {
    const menuButton = document.getElementById("mobile-menu-button");
    const mobileMenu = document.getElementById("mobile-menu");
    const openIcon = document.getElementById("menu-open-icon");
    const closeIcon = document.getElementById("menu-close-icon");

    if (!menuButton || !mobileMenu) {
        return;
    }

    function setMenuOpen(isOpen) {
        mobileMenu.classList.toggle("hidden", !isOpen);

        menuButton.setAttribute(
            "aria-expanded",
            String(isOpen)
        );

        menuButton.setAttribute(
            "aria-label",
            isOpen ? "Close navigation menu" : "Open navigation menu"
        );

        if (openIcon) {
            openIcon.classList.toggle("hidden", isOpen);
        }

        if (closeIcon) {
            closeIcon.classList.toggle("hidden", !isOpen);
        }
    }

    menuButton.addEventListener("click", function () {
        const isOpen =
            menuButton.getAttribute("aria-expanded") === "true";

        setMenuOpen(!isOpen);
    });

    mobileMenu.querySelectorAll("a").forEach(function (link) {
        link.addEventListener("click", function () {
            setMenuOpen(false);
        });
    });

    document.addEventListener("keydown", function (event) {
        if (event.key === "Escape") {
            setMenuOpen(false);
        }
    });

    window.addEventListener("resize", function () {
        if (window.innerWidth >= 1280) {
            setMenuOpen(false);
        }
    });
});




/* Homepage Hero Background Slider with Arrows and Dots */
document.addEventListener("DOMContentLoaded", function () {
    const hero = document.getElementById("homepage-hero");

    if (!hero) return;

    const slides = Array.from(
        hero.querySelectorAll(".hero-background-slide")
    );

    const dots = Array.from(
        hero.querySelectorAll(".hero-slide-dot")
    );

    const previousButton = hero.querySelector("#hero-prev");
    const nextButton = hero.querySelector("#hero-next");

    if (slides.length <= 1) return;

    const interval = Number(hero.dataset.slideInterval) || 6000;
    let currentIndex = 0;
    let autoplay;

    function showSlide(index) {
        currentIndex = (index + slides.length) % slides.length;

        slides.forEach(function (slide, i) {
            const isActive = i === currentIndex;

            slide.classList.toggle("opacity-100", isActive);
            slide.classList.toggle("opacity-0", !isActive);
        });

        dots.forEach(function (dot, i) {
            const isActive = i === currentIndex;

            dot.classList.toggle("bg-white", isActive);
            dot.classList.toggle("bg-white/40", !isActive);
            dot.classList.toggle("scale-110", isActive);

            dot.setAttribute("aria-current", String(isActive));
        });
    }

    function startAutoplay() {
        window.clearInterval(autoplay);

        autoplay = window.setInterval(function () {
            showSlide(currentIndex + 1);
        }, interval);
    }

    function goToSlide(index) {
        showSlide(index);
        startAutoplay();
    }

    if (previousButton) {
        previousButton.addEventListener("click", function () {
            goToSlide(currentIndex - 1);
        });
    }

    if (nextButton) {
        nextButton.addEventListener("click", function () {
            goToSlide(currentIndex + 1);
        });
    }

    dots.forEach(function (dot, index) {
        dot.addEventListener("click", function () {
            goToSlide(index);
        });
    });

    showSlide(currentIndex);
    startAutoplay();
});



// dropdown menu

   
    document.addEventListener('click', function(e) {
        document.querySelectorAll('details').forEach(function(detail) {
            if (!detail.contains(e.target)) {
                detail.removeAttribute('open');
            }
        });
    });
