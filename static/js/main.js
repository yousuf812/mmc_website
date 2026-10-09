document.addEventListener("DOMContentLoaded", () => {
    const menuButton = document.querySelector("[data-mobile-menu-button]");
    const mobileMenu = document.querySelector("[data-mobile-menu]");

    if (menuButton && mobileMenu) {
        menuButton.addEventListener("click", () => {
            const isOpen = mobileMenu.classList.toggle("is-open");

            menuButton.setAttribute(
                "aria-expanded",
                isOpen ? "true" : "false"
            );

            menuButton.setAttribute(
                "aria-label",
                isOpen ? "Close navigation menu" : "Open navigation menu"
            );
        });

        const mobileLinks = mobileMenu.querySelectorAll("a");

        mobileLinks.forEach((link) => {
            link.addEventListener("click", () => {
                mobileMenu.classList.remove("is-open");

                menuButton.setAttribute("aria-expanded", "false");
                menuButton.setAttribute(
                    "aria-label",
                    "Open navigation menu"
                );
            });
        });
    }
});