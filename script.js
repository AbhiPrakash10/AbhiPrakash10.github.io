'use strict';

// ── Nav: scroll-aware styling ──
const nav = document.getElementById('nav');
function updateNav() {
  nav.classList.toggle('scrolled', window.scrollY > 40);
}
window.addEventListener('scroll', updateNav, { passive: true });
updateNav();

// ── Nav: mobile hamburger ──
const hamburger = document.getElementById('hamburger');
const mobileMenu = document.getElementById('mobileMenu');
hamburger.addEventListener('click', () => {
  const open = mobileMenu.classList.toggle('open');
  hamburger.classList.toggle('open', open);
  hamburger.setAttribute('aria-expanded', open);
});
mobileMenu.querySelectorAll('.nav__mobile-link').forEach(link => {
  link.addEventListener('click', () => {
    mobileMenu.classList.remove('open');
    hamburger.classList.remove('open');
    hamburger.setAttribute('aria-expanded', false);
  });
});

// ── Scroll reveal ──
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('visible');
      revealObserver.unobserve(e.target);
    }
  });
}, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

document.querySelectorAll(
  '.section__header, .about__text, .about__card, .project-card, .contact__info, .contact__form'
).forEach(el => {
  el.classList.add('reveal');
  revealObserver.observe(el);
});

// ── Animated counters ──
const counterObserver = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (!e.isIntersecting) return;
    const el = e.target;
    const target = parseInt(el.dataset.target, 10);
    const duration = 1200;
    const start = performance.now();
    function tick(now) {
      const t = Math.min((now - start) / duration, 1);
      el.textContent = Math.floor(easeOut(t) * target);
      if (t < 1) requestAnimationFrame(tick);
      else el.textContent = target;
    }
    requestAnimationFrame(tick);
    counterObserver.unobserve(el);
  });
}, { threshold: 0.5 });

document.querySelectorAll('.stat__num[data-target]').forEach(el => {
  counterObserver.observe(el);
});

function easeOut(t) { return 1 - Math.pow(1 - t, 3); }

// ── Project filter ──
const filterBtns = document.querySelectorAll('.filter-btn');
const projectCards = document.querySelectorAll('.project-card');

filterBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    filterBtns.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const filter = btn.dataset.filter;
    projectCards.forEach(card => {
      const match = filter === 'all' || card.dataset.category === filter;
      card.classList.toggle('hidden', !match);
    });
  });
});

// ── Contact form (Web3Forms) ──
const form = document.getElementById('contactForm');
const note = document.getElementById('formNote');

form.addEventListener('submit', async e => {
  e.preventDefault();
  const name    = form.elements['name'].value.trim();
  const email   = form.elements['email'].value.trim();
  const message = form.elements['message'].value.trim();

  // Clear previous errors
  [form.elements['name'], form.elements['email'], form.elements['message']]
    .forEach(f => f.classList.remove('error'));
  note.textContent = '';
  note.className = 'form__note';

  // Validate
  let valid = true;
  if (!name)    { form.elements['name'].classList.add('error');    valid = false; }
  if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    form.elements['email'].classList.add('error'); valid = false;
  }
  if (!message) { form.elements['message'].classList.add('error'); valid = false; }
  if (!valid) {
    note.textContent = 'Please fill in all fields correctly.';
    return;
  }

  const submitBtn = form.querySelector('[type="submit"]');
  submitBtn.textContent = 'Sending…';
  submitBtn.disabled = true;

  try {
    const payload = {
      access_key: 'fa014cd4-74c9-4252-bb45-7ef6c3dbd830',
      name,
      email,
      message,
      subject: 'New message from abhiprakash.com contact form'
    };

    const res = await fetch('https://api.web3forms.com/submit', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify(payload)
    });

    const data = await res.json();

    if (data.success) {
      form.reset();
      note.textContent = 'Thanks! I\'ll get back to you soon.';
      note.classList.add('success');
    } else {
      note.textContent = data.message || 'Something went wrong. Please try again.';
    }
  } catch {
    note.textContent = 'Network error — please check your connection and try again.';
  } finally {
    submitBtn.textContent = 'Send Message';
    submitBtn.disabled = false;
  }
});

// ── Active nav link on scroll ──
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav__links a');

const sectionObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      navLinks.forEach(link => {
        link.style.color = link.getAttribute('href') === '#' + entry.target.id
          ? 'rgba(255,255,255,1)'
          : '';
      });
    }
  });
}, { rootMargin: '-40% 0px -50% 0px' });

sections.forEach(s => sectionObserver.observe(s));
