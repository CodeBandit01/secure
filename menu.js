// Hamburger menu logic for mobile navigation

document.addEventListener('DOMContentLoaded', function () {
    const menuBtn = document.getElementById('mobile-menu-button');
    const menu = document.getElementById('mobile-menu');
    const closeBtn = document.getElementById('mobile-menu-close');
    if (menuBtn && menu && closeBtn) {
        menuBtn.addEventListener('click', () => {
            menu.classList.remove('hidden');
        });
        closeBtn.addEventListener('click', () => {
            menu.classList.add('hidden');
        });
        // Optional: close menu when clicking outside
        menu.addEventListener('click', (e) => {
            if (e.target === menu) menu.classList.add('hidden');
        });
    }
});
