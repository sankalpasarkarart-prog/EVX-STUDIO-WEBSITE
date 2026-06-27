/* ============================================================
   EVX STUDIO — Apple Liquid Glass UI Interactive Script
   Production-quality vanilla JS with smooth animations,
   mouse tracking, and full DOM interactivity.
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {
  'use strict';

  // ──────────────────────────────────────────────────────────
  // 1. MOUSE TRACKING SYSTEM FOR GLASS ELEMENTS
  //    Every .glass element responds to the cursor via
  //    --mouse-x / --mouse-y custom properties that drive
  //    radial-gradient light reflections in CSS.
  // ──────────────────────────────────────────────────────────

  const glassElements = document.querySelectorAll('.glass');

  if (glassElements.length) {
    document.addEventListener('mousemove', (e) => {
      glassElements.forEach((el) => {
        const rect = el.getBoundingClientRect();
        const x = ((e.clientX - rect.left) / rect.width) * 100;
        const y = ((e.clientY - rect.top) / rect.height) * 100;
        el.style.setProperty('--mouse-x', `${x}%`);
        el.style.setProperty('--mouse-y', `${y}%`);
      });
    });
  }

  // ──────────────────────────────────────────────────────────
  // 2. 3D TILT EFFECT ON CARDS
  //    .tilt-card elements rotate subtly (±5°) following the
  //    cursor and reset smoothly on mouse leave.
  // ──────────────────────────────────────────────────────────

  const tiltCards = document.querySelectorAll('.tilt-card');

  tiltCards.forEach((card) => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const centerX = rect.left + rect.width / 2;
      const centerY = rect.top + rect.height / 2;
      const rotateX = ((e.clientY - centerY) / (rect.height / 2)) * -5;
      const rotateY = ((e.clientX - centerX) / (rect.width / 2)) * 5;
      card.style.transform =
        `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-5px)`;
    });

    card.addEventListener('mouseenter', () => {
      // Snappy response while the cursor is over the card
      card.style.transition = 'transform 0.1s ease';
    });

    card.addEventListener('mouseleave', () => {
      // Smooth spring-back when the cursor leaves
      card.style.transition = 'transform 0.5s ease';
      card.style.transform =
        'perspective(1000px) rotateX(0) rotateY(0) translateY(0)';
    });
  });

  // ──────────────────────────────────────────────────────────
  // 3. SCROLL-TRIGGERED ANIMATIONS (Intersection Observer)
  //    .animate-in elements fade/slide up when they enter the
  //    viewport. Grid children are staggered automatically.
  // ──────────────────────────────────────────────────────────

  const animateInElements = document.querySelectorAll('.animate-in');

  if (animateInElements.length) {
    const animObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            animObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.1, rootMargin: '0px 0px -50px 0px' }
    );

    animateInElements.forEach((el) => animObserver.observe(el));
  }

  // ──────────────────────────────────────────────────────────
  // 4. ANIMATED NUMBER COUNTERS
  //    .counter elements with data-target animate from 0 to
  //    the target value over ~2 s using ease-out cubic easing.
  // ──────────────────────────────────────────────────────────

  function animateCounter(el) {
    const target = parseInt(el.getAttribute('data-target'), 10);
    if (isNaN(target)) return;

    const suffix = el.getAttribute('data-suffix') || '';
    const duration = 2000;
    const start = performance.now();

    function update(currentTime) {
      const elapsed = currentTime - start;
      const progress = Math.min(elapsed / duration, 1);
      // Ease-out cubic
      const eased = 1 - Math.pow(1 - progress, 3);
      const current = Math.floor(eased * target);
      el.textContent = current + suffix;
      if (progress < 1) requestAnimationFrame(update);
    }

    requestAnimationFrame(update);
  }

  const counterElements = document.querySelectorAll('.counter');

  if (counterElements.length) {
    const counterObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            animateCounter(entry.target);
            counterObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.5 }
    );

    counterElements.forEach((el) => counterObserver.observe(el));
  }

  // ──────────────────────────────────────────────────────────
  // 5. NAVBAR SCROLL EFFECT
  //    Adds .scrolled class to .navbar after 50 px of scroll
  //    to intensify the glass backdrop.
  // ──────────────────────────────────────────────────────────

  const navbar = document.querySelector('.navbar');
  const povBanner = document.querySelector('.pov-banner');

  if (navbar) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }

      // Hide POV banner after scrolling past hero
      if (povBanner) {
        if (window.scrollY > 300) {
          povBanner.style.opacity = '0';
          povBanner.style.pointerEvents = 'none';
          povBanner.style.transform = 'translateY(-20px)';
        } else {
          povBanner.style.opacity = '1';
          povBanner.style.pointerEvents = 'auto';
          povBanner.style.transform = 'translateY(0)';
        }
      }
    }, { passive: true });
  }

  // ──────────────────────────────────────────────────────────
  // 6. SMOOTH SCROLL FOR NAVIGATION LINKS
  //    Anchor links beginning with '#' scroll smoothly to
  //    their target and close the mobile menu if open.
  // ──────────────────────────────────────────────────────────

  document.querySelectorAll('a[href^="#"]').forEach((link) => {
    link.addEventListener('click', (e) => {
      const href = link.getAttribute('href');
      if (!href || href === '#') return;

      e.preventDefault();
      const target = document.querySelector(href);
      if (target) {
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });

        // Close mobile menu if it's open
        document.querySelector('.nav-links')?.classList.remove('active');
        document.querySelector('.mobile-menu-btn')?.classList.remove('active');
      }
    });
  });

  // ──────────────────────────────────────────────────────────
  // 7. MOBILE MENU TOGGLE
  // ──────────────────────────────────────────────────────────

  const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
  const navLinks = document.querySelector('.nav-links');

  if (mobileMenuBtn && navLinks) {
    mobileMenuBtn.addEventListener('click', () => {
      navLinks.classList.toggle('active');
      mobileMenuBtn.classList.toggle('active');
    });
  }

  // ──────────────────────────────────────────────────────────
  // 8. HERO PARALLAX EFFECT
  //    .hero-orb elements shift subtly based on cursor
  //    position to create depth.
  // ──────────────────────────────────────────────────────────

  const heroOrbs = document.querySelectorAll('.hero-orb');

  if (heroOrbs.length) {
    document.addEventListener('mousemove', (e) => {
      const x = (e.clientX / window.innerWidth - 0.5) * 2;
      const y = (e.clientY / window.innerHeight - 0.5) * 2;

      heroOrbs.forEach((orb, i) => {
        const speed = (i + 1) * 15;
        orb.style.transform = `translate(${x * speed}px, ${y * speed}px)`;
      });
    });
  }

  // ──────────────────────────────────────────────────────────
  // 9. ACTIVE NAV LINK HIGHLIGHTING
  //    On scroll, the nav link matching the currently visible
  //    section receives an .active class.
  // ──────────────────────────────────────────────────────────

  const sections = document.querySelectorAll('section[id]');

  if (sections.length) {
    window.addEventListener('scroll', () => {
      let current = '';

      sections.forEach((section) => {
        const sectionTop = section.offsetTop - 100;
        if (window.scrollY >= sectionTop) {
          current = section.getAttribute('id');
        }
      });

      document.querySelectorAll('.nav-links a').forEach((link) => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
          link.classList.add('active');
        }
      });
    }, { passive: true });
  }
});
