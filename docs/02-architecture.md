# 02 — Platform Architecture Overview

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                        VISITOR                              │
│              (browser: Chrome, Safari, Firefox)             │
└──────────────────────────┬──────────────────────────────────┘
                           │ HTTPS
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                   CLOUDFLARE / DNS                          │
│         abhiprakash.com → GitHub Pages IPs                  │
│    185.199.108–111.153 (A records) + CNAME www              │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│               GITHUB PAGES (Fastly CDN)                     │
│         AbhiPrakash10/AbhiPrakash10.github.io               │
│              Static file serving — NO backend               │
│   index.html │ styles.css │ script.js │ article.js │ *.html  │
└──────┬───────────────────┬──────────────────────────────────┘
       │                   │
       ▼                   ▼
┌─────────────┐   ┌────────────────────────────────────────────┐
│ GOOGLE      │   │           THIRD-PARTY SERVICES             │
│ FONTS CDN   │   │                                            │
│ Inter       │   │  Formspree (xojbkeeb)                      │
│ Inter Tight │   │    Form submissions → Gmail                │
│ Great Vibes │   │    FREE tier: 250/month                    │
└─────────────┘   │                                            │
                  │  Google Analytics GA4 (G-6EWRLB434Y)       │
                  │    Page views, sessions, events            │
                  │    FREE tier                               │
                  └────────────────────────────────────────────┘
```

---

## Frontend Architecture

**Stack:** Vanilla HTML5 + CSS3 + Vanilla JavaScript  
**Build tool:** None  
**Package manager:** None  
**Framework:** None  

### Why Vanilla?

No framework was chosen deliberately:
- Zero build complexity — edit a file, push, done
- Zero dependency risk — no npm vulnerabilities, no breaking changes
- Maximum browser compatibility — runs everywhere without transpilation
- Instant load — no JS bundle overhead
- Easy handoff — any developer can read and edit HTML/CSS/JS

### HTML Structure

Each page is a self-contained HTML file. The homepage (`index.html`) contains all sections as a single-page experience. Article pages (`lightside.html`, etc.) are separate files sharing the same nav/footer pattern.

### CSS Architecture

All styles live in `styles.css` (~1,120 lines), organized into 22 numbered sections:

```
1.  Variables & Reset
2.  Typography
3.  Layout Utilities
4.  Navigation
5.  Hero Section
6.  Manifesto Band
7.  Story Section
8.  Ventures Section
9.  Thinking / Articles Section
10. Speaking Section
11. Contact Section
12. Footer
13. Article Hero
14. Article Prose
15. Article Footer Band
16. Buttons
17. Forms
18. Animations & Reveal
19. Article accessibility overrides (specificity trick)
20. Reading progress bar
21. Coming-soon card states
22. Page fade-in transition
```

**Design tokens** (CSS custom properties) are defined in `:root` and used throughout. Never hardcode color or font values — always reference a token.

### JavaScript Architecture

**script.js** (main, loaded on all pages):
- Nav scroll behavior
- Mobile nav toggle
- Smooth scroll
- IntersectionObserver scroll reveal (staggered, 90ms delay per sibling)
- Active nav link tracking
- Contact form (validation + Formspree fetch)

**article.js** (article pages only):
- Reading progress bar (`id="readingProgress"`)
- Passive scroll listener
- Updates `aria-valuenow` for accessibility

---

## Backend Architecture

**There is no backend.** This is a fully static site.

All "dynamic" behavior is handled client-side:
- Form submission → Formspree API (external service)
- Analytics → Google Analytics (external service)
- Fonts → Google Fonts CDN (external service)

---

## Database Structure

**There is no database.**

Content is stored as HTML within the HTML files themselves. If a database is ever added, see [Section 15](./15-not-built.md) for the recommended path.

---

## Authentication

**There is no authentication.** The entire site is publicly accessible.

---

## Hosting Infrastructure

| Layer | Provider | Details |
|-------|----------|---------|
| Hosting | GitHub Pages | Free, static, auto-deploy on push |
| CDN | Fastly (via GitHub Pages) | Global edge caching, HTTPS enforced |
| Domain | Custom registrar | abhiprakash.com |
| DNS | Domain registrar | A records → GitHub Pages IPs |
| SSL/TLS | GitHub Pages (Let's Encrypt) | Auto-renewed, enforced HTTPS |

**GitHub Pages DNS configuration:**
```
A    @    185.199.108.153
A    @    185.199.109.153
A    @    185.199.110.153
A    @    185.199.111.153
CNAME www  AbhiPrakash10.github.io
```

---

## Analytics Stack

| Tool | Purpose | ID |
|------|---------|-----|
| Google Analytics GA4 | Page views, sessions, user behavior, traffic sources | G-6EWRLB434Y |

GA4 is loaded via `gtag.js` in the `<head>` of every page. Events tracked automatically: page_view, session_start, first_visit.

**Custom events to add in future:** form_submit, article_read_complete, venture_link_click.

---

## Third-Party Services

| Service | Purpose | Cost | Tier |
|---------|---------|------|------|
| GitHub Pages | Hosting | Free | Public repo |
| Google Fonts | Typography (Inter, Inter Tight, Great Vibes) | Free | — |
| Google Analytics GA4 | Analytics | Free | Standard |
| Formspree | Contact form backend | Free | 250 submissions/month |

---

## Design System Structure

```
styles.css (:root)
├── Color tokens (--midnight, --red, --red-dark, --off-white, etc.)
├── Typography tokens (--font-display, --font-body, --font-signature)
├── Layout tokens (--nav-h, --container)
└── Animation tokens (--ease)
```

**Color Palette:**

| Token | Hex | Usage | Contrast |
|-------|-----|-------|---------|
| `--midnight` | `#111827` | Primary dark bg | — |
| `--graphite` | `#1E2530` | Secondary dark | — |
| `--off-white` | `#F3F0E8` | Primary light bg | — |
| `--red` | `#C41E3A` | Primary accent | 5.3:1 on off-white |
| `--red-dark` | `#E5677C` | Accent on dark bg | 5.6:1 on midnight |
| `--gray-500` | `#6B6762` | Body text | 4.5:1 on white |

---

## How Failures Propagate

| Failure | Impact | Fallback |
|---------|--------|---------|
| GitHub Pages down | Site unreachable | None (no fallback hosting) |
| Google Fonts blocked | System fonts render (Arial, Helvetica) | Acceptable degradation |
| Formspree down | Contact form shows error message | Direct email link visible |
| GA4 blocked (ad blocker) | No analytics for that visitor | Acceptable — privacy respecting |
| DNS misconfiguration | Site unreachable | Restore DNS records (see runbooks) |

---

## Architecture Tradeoffs

| Decision | Tradeoff Made | Why |
|----------|--------------|-----|
| No framework | Less component reusability | Simplicity, speed, zero deps |
| No CMS | Manual HTML editing for content | Complexity not justified yet |
| No staging | All changes go directly to prod | Low-risk static site |
| No database | Can't store dynamic data | Not needed for current scope |
| No build pipeline | Can't use TypeScript, Sass, etc. | Matches team size (solo) |
| GitHub Pages hosting | Limited control over CDN, no server | Free, zero ops overhead |
