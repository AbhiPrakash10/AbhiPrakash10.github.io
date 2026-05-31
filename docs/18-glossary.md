# 18 — Glossary

## Technical Terms

**A Record**  
A DNS record that maps a domain name to an IPv4 address. Used to point `abhiprakash.com` to GitHub Pages servers.

**aria-controls**  
An HTML accessibility attribute that identifies the element an interactive element (like a button) controls. Used on the hamburger menu button to reference the nav drawer it opens.

**aria-expanded**  
An HTML accessibility attribute that indicates whether a collapsible element is currently open or closed. Updated dynamically by script.js when the mobile nav opens/closes.

**Cardinal Red**  
The primary brand accent color: `#C41E3A`. Named after the deep red used by cardinal birds and several sports teams. Maintains 5.3:1 contrast ratio on off-white — WCAG AA compliant.

**CDN (Content Delivery Network)**  
A network of servers distributed globally that cache and serve static files from locations near the user. GitHub Pages uses Fastly as its CDN, ensuring fast load times worldwide.

**CNAME**  
A DNS record that maps one domain name (alias) to another. Used for `www.abhiprakash.com` → `AbhiPrakash10.github.io`.

**CSS Custom Properties (Design Tokens)**  
Variables defined in CSS with the `--` prefix (e.g., `--red: #C41E3A`). Referenced throughout the stylesheet with `var(--red)`. Changing one token updates every usage site-wide.

**Fastly**  
The CDN provider bundled with GitHub Pages. Serves cached files from edge nodes globally, providing fast load times without any configuration required.

**focus-visible**  
A CSS pseudo-class (`:focus-visible`) that applies focus styles only when the element was reached via keyboard navigation — not mouse clicks. Prevents distracting outlines for mouse users while maintaining accessibility for keyboard users.

**Formspree**  
A form backend service. When the contact form is submitted, it POSTs to `https://formspree.io/f/xojbkeeb`, which validates and forwards the submission to `abhiprakash20@gmail.com`.

**GA4 (Google Analytics 4)**  
The current generation of Google Analytics. Uses an event-based data model. Measurement ID `G-6EWRLB434Y` identifies the Abhi Prakash property. Data flows via the `gtag.js` script tag in each page's `<head>`.

**GitHub Actions**  
GitHub's built-in CI/CD system. GitHub Pages uses Actions internally to build and deploy the site on every push to `main`. No configuration required for static sites.

**GitHub Pages**  
A free static website hosting service provided by GitHub. Hosts the repository as a website, auto-deploys on push, provides HTTPS via Let's Encrypt, and uses Fastly CDN.

**Great Vibes**  
A Google Fonts typeface used for the handwritten signature in the Story section and the cursive "Abhi Prakash" signature element. CSS token: `--font-signature`.

**Honeypot Field**  
A hidden form field (`<input name="_gotcha" style="display:none">`) that bots fill in automatically but humans never see. If the field is filled on submission, the message is rejected as spam. Formspree recognizes `_gotcha` specifically.

**IntersectionObserver**  
A browser API that fires a callback when an element enters or exits the viewport. Used in `script.js` for scroll reveal animations (elements fade in as they scroll into view) and active nav link tracking.

**Inter / Inter Tight**  
Google Fonts typefaces used throughout the site. Inter is the body/UI font; Inter Tight is the display/headline font (used at weights 700, 800, 900). CSS tokens: `--font-body`, `--font-display`.

**Measurement ID**  
The unique identifier for a Google Analytics 4 property. Format: `G-XXXXXXXXXX`. For this site: `G-6EWRLB434Y`. Appears in the `gtag.js` script tag.

**Midnight**  
The primary dark background color: `#111827`. Named for its near-black depth. CSS token: `--midnight`.

**mix-blend-mode: multiply**  
A CSS property that blends an element's pixels with the background using multiplication. Used on `signature.png` to make the white background of the PNG transparent while keeping the dark ink strokes visible on the off-white site background.

**Off-white**  
The primary light background color: `#F3F0E8`. A warm, slightly cream white used for light sections (Story, Thinking). CSS token: `--off-white`.

**OG Image (Open Graph Image)**  
The image displayed when a URL is shared on social platforms (LinkedIn, Twitter/X, iMessage, Slack). Must be 1200×630px. This site's OG image is `og-image.jpg`, generated with Python Pillow.

**Open Graph Tags**  
HTML meta tags (`<meta property="og:*">`) that control how URLs appear when shared on social media. Include title, description, image, and URL.

**prefers-reduced-motion**  
A CSS media query (`@media (prefers-reduced-motion: reduce)`) that detects if the user has enabled the "Reduce Motion" accessibility setting on their OS. When enabled, all animations and transitions are disabled site-wide.

**Reading Progress Bar**  
The thin cardinal red line at the top of article pages that grows from 0% to 100% as the user scrolls through an article. Implemented via `article.js` and the `.reading-progress` CSS class.

**robots.txt**  
A file at the root of a website that tells search engine crawlers which pages they can and cannot access. This site's `robots.txt` allows all crawlers and references the `sitemap.xml`.

**Scroll Reveal**  
The animation pattern where elements are initially invisible (opacity 0, translated 24px down) and fade/slide into view as the user scrolls them into the viewport. Implemented via `IntersectionObserver` with staggered sibling delays (90ms per item).

**sitemap.xml**  
An XML file listing all pages on the site with their URLs and priority weights. Submitted to Google Search Console to help search engines discover and index all pages.

**Skip Nav (Skip Navigation Link)**  
A visually hidden link that becomes visible on keyboard focus. Allows keyboard and screen reader users to skip the navigation and jump directly to the main content. Required for WCAG 2.1 compliance.

**Static Site**  
A website that serves pre-built HTML, CSS, and JavaScript files — with no server-side processing per request. All content is fixed at deploy time. Opposite of a dynamic site (which generates pages from a database on each request).

**WCAG AA**  
Web Content Accessibility Guidelines, Level AA. The industry standard for web accessibility. Requires minimum contrast ratios of 4.5:1 for normal text and 3:1 for large text. All color combinations on this site meet or exceed these ratios.

---

## Internal Terminology

**Design Token**  
A CSS custom property that stores a design decision (color, font, spacing). Example: `--red: #C41E3A`. Changing the token value updates all usages site-wide.

**Reveal Element**  
Any HTML element with the class `reveal`. These elements start invisible and animate into view when they enter the viewport. The `.visible` class is added by the IntersectionObserver when triggered.

**Specificity Trick**  
A CSS technique used in `styles.css` Section 19. Article pages have inline `<style>` blocks that come after the `<link>` to `styles.css` in cascade order, making them hard to override. Using 2-class selectors (`.article-hero .article-hero__cat`) in `styles.css` gives higher specificity than the 1-class selectors in the inline blocks, winning the cascade regardless of order.
