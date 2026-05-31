# 04 — Repository Structure and Key Files

## Repository

**URL:** https://github.com/AbhiPrakash10/AbhiPrakash10.github.io  
**Visibility:** Public  
**Default branch:** `main`  
**Auto-deploy:** Yes — every push to `main` triggers GitHub Pages deployment

---

## Complete File Structure

```
AbhiPrakash10.github.io/          ← repository root = site root
│
├── index.html                    ← Homepage (single-page app structure)
├── styles.css                    ← Central design system (~1,120 lines)
├── script.js                     ← Main JavaScript (nav, scroll, form)
├── article.js                    ← Article-only JS (reading progress bar)
│
├── favicon.svg                   ← AP monogram, cardinal red (#C41E3A) bg
├── og-image.jpg                  ← Social share card (1200×630px, Pillow-generated)
├── signature.png                 ← Handwritten signature image
├── Prakash_Abhi-015.jpg          ← Profile photo (story section)
│
├── sitemap.xml                   ← XML sitemap (all 6 pages)
├── robots.txt                    ← Search crawler permissions
│
├── lightside.html                ← Article: "What the Lightside Is"
├── cloud-secret.html             ← Article: "The Cloud's Secret"
├── athletic-edge.html            ← Article: "The Athletic Edge in Business"
├── intelligent-execution.html    ← Article: "Intelligent Execution"
├── fusion-energy.html            ← Article: "Nuclear Fusion: The New Energy Frontier"
│
└── docs/                         ← This documentation folder
    ├── README.md
    ├── 01-executive-summary.md
    ├── 02-architecture.md
    ├── 03-product-structure.md
    ├── 04-repository-structure.md   ← You are here
    ├── 05-environment-setup.md
    ├── 06-local-development.md
    ├── 07-git-deployment.md
    ├── 08-infrastructure.md
    ├── 09-iteration.md
    ├── 10-runbooks.md
    ├── 11-maintenance.md
    ├── 12-monitoring.md
    ├── 13-security.md
    ├── 14-scaling.md
    ├── 15-not-built.md
    ├── 16-ownership.md
    ├── 17-onboarding.md
    └── 18-glossary.md
```

---

## Key Files — Detailed Reference

### `index.html`
The homepage. Contains all 10 sections of the single-page experience. Every section uses a `<section id="sectionname">` anchor for smooth scroll navigation.

**Key structure:**
```html
<head>
  <!-- GA4, meta tags, OG tags, favicon, fonts -->
</head>
<body>
  <a class="skip-link">               <!-- Accessibility: skip nav -->
  <header class="nav">               <!-- Fixed navigation -->
  <section class="hero" id="hero">   <!-- Hero -->
  <div class="manifesto">            <!-- Quote band -->
  <section class="story" id="story"> <!-- Bio + photo -->
  <section class="ventures">         <!-- 6 ventures -->
  <section class="thinking">         <!-- Articles -->
  <section class="speaking">         <!-- Speaking -->
  <section class="contact">          <!-- Form -->
  <footer class="footer">            <!-- Footer -->
  <script src="script.js">           <!-- JS last -->
</body>
```

---

### `styles.css`
The single source of truth for all visual design. **Never add inline styles to HTML pages** — always add to styles.css.

**22 sections (numbered in comments):**

```css
/* ── 1. Variables & Reset ── */   ← CSS custom properties (design tokens)
/* ── 2. Typography ── */
/* ── 3. Skip Link ── */
/* ── 4. Navigation ── */
/* ── 5. Hero ── */
/* ── 6. Manifesto Band ── */
/* ── 7. Story ── */
/* ── 8. Ventures ── */
/* ── 9. Thinking / Articles ── */
/* ── 10. Speaking ── */
/* ── 11. Contact ── */
/* ── 12. Footer ── */
/* ── 13. Article Hero ── */
/* ── 14. Article Prose ── */
/* ── 15. Article Footer Band ── */
/* ── 16. Buttons ── */
/* ── 17. Forms ── */
/* ── 18. Animations & Reveal ── */
/* ── 19. Article accessibility overrides ── */
/* ── 20. Reading progress bar ── */
/* ── 21. Coming-soon article cards ── */
/* ── 22. Page fade-in transition ── */
```

---

### `script.js`
Loaded on all pages. Contains 7 independent modules:

```javascript
// Module 1: Nav scroll background
// Module 2: Mobile nav toggle
// Module 3: Mobile nav auto-close
// Module 4: Smooth scroll (anchor links)
// Module 5: Scroll reveal (IntersectionObserver)
// Module 6: Active nav link tracking
// Module 7: Contact form (validation + Formspree)
```

---

### `article.js`
Loaded only on article pages. Single responsibility: reading progress bar.

```javascript
// Updates #readingProgress bar width based on scroll position
// Passive scroll listener for performance
// Sets aria-valuenow for screen reader accessibility
```

---

### `favicon.svg`
SVG favicon — renders crisply at all sizes (16px, 32px, 180px). Cardinal red `#C41E3A` background with white "AP" monogram in Arial Black.

```svg
<svg viewBox="0 0 32 32">
  <rect width="32" height="32" rx="5" fill="#C41E3A"/>
  <text x="16" y="23" font-weight="900" fill="#FFFFFF">AP</text>
</svg>
```

---

### `og-image.jpg`
1200×630px social share card. Generated with Python Pillow using system fonts. Used as `og:image` and `twitter:image` across all pages.

**To regenerate:**
```bash
python3 -c "
from PIL import Image, ImageDraw, ImageFont
# See original generation script in session history
"
```

---

### `signature.png`
Handwritten signature extracted from a Word document using `python-docx`. Black ink on white background. Rendered with `mix-blend-mode: multiply` in CSS so the white background becomes transparent against the off-white site background.

---

### `sitemap.xml`
Lists all 6 pages with priority weights. Submit to Google Search Console at:  
https://search.google.com/search-console

---

### `robots.txt`
```
User-agent: *
Allow: /
Sitemap: https://abhiprakash.com/sitemap.xml
```

---

## Naming Conventions

| Type | Convention | Example |
|------|-----------|---------|
| HTML pages | kebab-case | `cloud-secret.html` |
| CSS classes | BEM-inspired, kebab-case | `.venture-item__left` |
| CSS variables | kebab-case with `--` prefix | `--red-dark` |
| JS variables | camelCase | `navToggle`, `formNote` |
| Image files | descriptive, original name acceptable | `Prakash_Abhi-015.jpg` |
| Doc files | numbered kebab-case | `02-architecture.md` |

---

## What NOT to Put in This Repo

- `.env` files or any file containing secrets
- API keys, tokens, or passwords in any file
- Large video or audio files (use external hosting)
- Build artifacts or `node_modules`
