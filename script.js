'use strict';

// ── Nav: scroll-aware background ──
const nav = document.getElementById('nav');
function updateNav() {
  nav.classList.toggle('scrolled', window.scrollY > 60);
}
window.addEventListener('scroll', updateNav, { passive: true });
updateNav();

// ── Nav: mobile toggle ──
const navToggle = document.getElementById('navToggle');
const navDrawer = document.getElementById('navDrawer');

navToggle.addEventListener('click', () => {
  const open = navDrawer.classList.toggle('open');
  navToggle.classList.toggle('open', open);
  navToggle.setAttribute('aria-expanded', open);
});

navDrawer.querySelectorAll('.nav__drawer-link').forEach(link => {
  link.addEventListener('click', () => {
    navDrawer.classList.remove('open');
    navToggle.classList.remove('open');
    navToggle.setAttribute('aria-expanded', false);
  });
});

// ── Smooth scroll for all anchor links ──
document.querySelectorAll('a[href^="#"]').forEach(link => {
  link.addEventListener('click', e => {
    const target = document.querySelector(link.getAttribute('href'));
    if (!target) return;
    e.preventDefault();
    const offset = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--nav-h')) || 68;
    const top = target.getBoundingClientRect().top + window.scrollY - offset;
    window.scrollTo({ top, behavior: 'smooth' });
  });
});

// ── Scroll reveal ──
const revealObs = new IntersectionObserver((entries) => {
  entries.forEach((entry, i) => {
    if (!entry.isIntersecting) return;
    const el = entry.target;
    const delay = el.dataset.delay || 0;
    setTimeout(() => el.classList.add('visible'), delay);
    revealObs.unobserve(el);
  });
}, { threshold: 0.1, rootMargin: '0px 0px -48px 0px' });

// Stagger siblings within parent containers
document.querySelectorAll('.reveal').forEach((el, i) => {
  const siblings = [...el.parentElement.querySelectorAll('.reveal')];
  const idx = siblings.indexOf(el);
  el.dataset.delay = idx * 90;
  revealObs.observe(el);
});

// ── Active nav link on scroll ──
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav__link');

const sectionObs = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    const id = entry.target.id;
    navLinks.forEach(link => {
      const active = link.getAttribute('href') === '#' + id;
      link.style.color = active ? 'rgba(255,255,255,1)' : '';
    });
  });
}, { rootMargin: '-40% 0px -50% 0px' });

sections.forEach(s => sectionObs.observe(s));

// ── Contact form (Web3Forms) ──
const form     = document.getElementById('contactForm');
const formNote = document.getElementById('formNote');

form.addEventListener('submit', async e => {
  e.preventDefault();

  const name    = form.elements['name'].value.trim();
  const email   = form.elements['email'].value.trim();
  const message = form.elements['message'].value.trim();

  // Clear previous state
  [form.elements['name'], form.elements['email'], form.elements['message']]
    .forEach(f => f.classList.remove('error'));
  formNote.textContent = '';
  formNote.className = 'form-note';

  // Validate
  let valid = true;
  if (!name)    { form.elements['name'].classList.add('error');    valid = false; }
  if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    form.elements['email'].classList.add('error'); valid = false;
  }
  if (!message) { form.elements['message'].classList.add('error'); valid = false; }
  if (!valid) {
    formNote.textContent = 'Please fill in all fields correctly.';
    return;
  }

  const submitBtn = form.querySelector('[type="submit"]');
  submitBtn.textContent = 'Sending…';
  submitBtn.disabled = true;

  try {
    const res = await fetch('https://api.web3forms.com/submit', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify({
        access_key: 'fa014cd4-74c9-4252-bb45-7ef6c3dbd830',
        name, email, message,
        subject: 'New message from abhiprakash.com'
      })
    });
    const data = await res.json();
    if (data.success) {
      form.reset();
      formNote.textContent = 'Message received. I\'ll be in touch.';
      formNote.classList.add('success');
    } else {
      formNote.textContent = data.message || 'Something went wrong. Please try again.';
    }
  } catch {
    formNote.textContent = 'Network error — please check your connection.';
  } finally {
    submitBtn.textContent = 'Send Message';
    submitBtn.disabled = false;
  }
});
