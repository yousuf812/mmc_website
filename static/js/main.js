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



/* Homepage Hero Background Slider */
document.addEventListener("DOMContentLoaded", function () {
    const hero = document.getElementById("homepage-hero");

    if (!hero) return;

    const slides = hero.querySelectorAll(".hero-background-slide");

    // No slider or only one image: nothing to rotate.
    if (slides.length <= 1) return;

    const interval = Number(hero.dataset.slideInterval) || 6000;
    let currentIndex = 0;

    window.setInterval(function () {
        slides[currentIndex].classList.remove("opacity-100");
        slides[currentIndex].classList.add("opacity-0");

        currentIndex = (currentIndex + 1) % slides.length;

        slides[currentIndex].classList.remove("opacity-0");
        slides[currentIndex].classList.add("opacity-100");
    }, interval);
});
