document.addEventListener("DOMContentLoaded", function () {
    // 1. Əsas Swiper (Header)
    if (document.querySelector(".mySwiper")) {
        var swiper = new Swiper(".mySwiper", {
            loop: true,
            speed: 1000,
            autoplay: {
                delay: 3000,
                disableOnInteraction: false,
            },
            on: {
                click: function () {
                    this.slideNext();
                },
            },
        });
    }

    // 2. Məhsul Slayderi Başlat
    initProductSlider();

    // 3. Sortiment Bölməsi üçün Animasiya (Intersection Observer)
    const observerOptions = {
        threshold: 0.2
    };

    const sortimentObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                const items = entry.target.querySelectorAll('.sortiment-item');
                items.forEach((item, index) => {
                    setTimeout(() => {
                        item.classList.add('reveal');
                    }, index * 200); // 200ms gecikmə ilə bir-bir açılır
                });
                sortimentObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const sortimentBox = document.querySelector('.sortiment-box');
    if (sortimentBox) {
        sortimentObserver.observe(sortimentBox);
    }

      const swiperGallery = new Swiper(".gallery-section .labSwiper", {
    slidesPerView: 2.5,
    centeredSlides: true,
    spaceBetween: 20,
    loop: true,
    speed: 800,
    navigation: {
      nextEl: ".gallery-section .swiper-button-next",
      prevEl: ".gallery-section .swiper-button-prev",
    },
    breakpoints: {
      320: {
        slidesPerView: 1.3,
        spaceBetween: 15,
      },
      640: {
        slidesPerView: 1.8,
        spaceBetween: 15,
      },
      1024: {
        slidesPerView: 2.2,
        spaceBetween: 20,
      },
    },
    on: {
      init: function () {
        updateSlideScaling();
      },
      slideChange: function () {
        updateSlideScaling();
      },
    },
  });

  function updateSlideScaling() {
    const slides = document.querySelectorAll(".gallery-section .swiper-slide");

    slides.forEach((slide) => {
      slide.classList.remove("active-slide");
    });

    setTimeout(() => {
      const activeSlide = document.querySelector(
        ".gallery-section .swiper-slide-active"
      );
      if (activeSlide) {
        activeSlide.classList.add("active-slide");
      }
    }, 50);
  }

});

// Məhsul Slayderi Funksiyası
function initProductSlider() {
    const sliderContainer = document.querySelector('.featured-section .slider-container');
    const productCards = document.querySelectorAll('.featured-section .product-card');
    const prevBtn = document.querySelector('.featured-section .prev-btn');
    const nextBtn = document.querySelector('.featured-section .next-btn');

    if (!sliderContainer || productCards.length === 0) return;

    const originalProductCount = productCards.length;
    let autoplayInterval;

    function createInfiniteLoop() {
        for (let i = originalProductCount - 1; i >= 0; i--) {
            const clone = productCards[i].cloneNode(true);
            sliderContainer.insertBefore(clone, sliderContainer.firstChild);
        }
        for (let i = 0; i < originalProductCount; i++) {
            const clone = productCards[i].cloneNode(true);
            sliderContainer.appendChild(clone);
        }
    }

    createInfiniteLoop();

    const allCards = document.querySelectorAll('.featured-section .product-card');
    const totalCards = allCards.length;
    let currentIndex = originalProductCount + 1;

    function updateSlider() {
        allCards.forEach((card) => {
            card.classList.remove('visible', 'active');
        });

        const prevIndex = currentIndex - 1;
        const nextIndex = currentIndex + 1;

        if (allCards[prevIndex]) allCards[prevIndex].classList.add('visible');
        if (allCards[currentIndex]) allCards[currentIndex].classList.add('visible', 'active');
        if (allCards[nextIndex]) allCards[nextIndex].classList.add('visible');
    }

    function nextSlide() {
        currentIndex++;
        if (currentIndex >= totalCards - originalProductCount) {
            currentIndex = originalProductCount;
        }
        updateSlider();
    }

    function prevSlide() {
        currentIndex--;
        if (currentIndex < originalProductCount) {
            currentIndex = totalCards - originalProductCount - 1;
        }
        updateSlider();
    }

    function startAutoplay() {
        autoplayInterval = setInterval(nextSlide, 3000);
    }

    function stopAutoplay() {
        clearInterval(autoplayInterval);
    }

    if(prevBtn) prevBtn.addEventListener('click', () => { prevSlide(); stopAutoplay(); startAutoplay(); });
    if(nextBtn) nextBtn.addEventListener('click', () => { nextSlide(); stopAutoplay(); startAutoplay(); });

    updateSlider();
    startAutoplay();

    // Touch/Swipe dəstəyi
    let touchStartX = 0;
    sliderContainer.addEventListener('touchstart', (e) => {
        touchStartX = e.changedTouches[0].screenX;
        stopAutoplay();
    }, {passive: true});

    sliderContainer.addEventListener('touchend', (e) => {
        let touchEndX = e.changedTouches[0].screenX;
        if (touchEndX < touchStartX - 50) nextSlide();
        if (touchEndX > touchStartX + 50) prevSlide();
        startAutoplay();
    }, {passive: true});
}