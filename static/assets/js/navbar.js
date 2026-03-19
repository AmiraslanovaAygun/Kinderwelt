function toggleMenu() {
    const mobileMenu = document.getElementById('mobile-menu');
    const overlay = document.querySelector('.mobile-overlay');
    const hamburger = document.getElementById('hamburger');
    const icon = hamburger.querySelector('i');

    const isActive = mobileMenu.classList.contains('active');

    if (isActive) {
        mobileMenu.classList.remove('active');
        overlay.classList.remove('active');
        icon.className = 'fas fa-bars';
        document.body.style.overflow = '';
    } else {
        mobileMenu.classList.add('active');
        overlay.classList.add('active');
        icon.className = 'fa-solid fa-xmark';
        document.body.style.overflow = 'hidden';
    }
}

document.addEventListener("DOMContentLoaded", function () {
    const currentPath = window.location.pathname;
    const allLinks = document.querySelectorAll('.nav-list a, .mobile-nav-list a');

    allLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPath || href === currentPath + '/' || href + '/' === currentPath) {
            link.classList.add('active');
        }
    });

    const hamburger = document.getElementById('hamburger');
    if (hamburger) {
        let overlay = document.querySelector('.mobile-overlay');
        if (!overlay) {
            overlay = document.createElement('div');
            overlay.className = 'mobile-overlay';
            document.body.appendChild(overlay);
        }

        hamburger.addEventListener('click', (e) => {
            e.stopPropagation();
            toggleMenu();
        });
        overlay.addEventListener('click', toggleMenu);
    }

   document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');

        if (href !== "#") {
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });

                history.pushState(null, null, href);

                const mobileMenu = document.getElementById('mobile-menu');
                if (mobileMenu && mobileMenu.classList.contains('active')) {
                    toggleMenu();
                }
            }
        }
    });
});
});

// Legal Modalları Açmaq
function openLegalModal(type) {
    const modal = document.getElementById('modal-' + type);
    if (modal) {
        modal.style.display = "block";
        document.body.style.overflow = "hidden"; // Arxa fonun sürüşməsini bağlayır
    }
}

// Legal Modalları Bağlamaq
function closeLegalModal(type) {
    const modal = document.getElementById('modal-' + type);
    if (modal) {
        modal.style.display = "none";
        document.body.style.overflow = "auto"; // Scroll-u bərpa edir
    }
}

// Modalın kənarına (boşluğa) kliklədikdə bağlanması
window.addEventListener('click', function(event) {
    if (event.target.classList.contains('legal-modal')) {
        event.target.style.display = "none";
        document.body.style.overflow = "auto";
    }
});