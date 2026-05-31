'use strict';

// ── Reading progress bar ──
(function () {
  const bar = document.getElementById('readingProgress');
  if (!bar) return;
  function update() {
    const el    = document.documentElement;
    const top   = el.scrollTop || document.body.scrollTop;
    const total = el.scrollHeight - el.clientHeight;
    const pct   = total > 0 ? Math.min(top / total * 100, 100) : 0;
    bar.style.width = pct + '%';
    bar.setAttribute('aria-valuenow', Math.round(pct));
  }
  window.addEventListener('scroll', update, { passive: true });
  update();
})();
