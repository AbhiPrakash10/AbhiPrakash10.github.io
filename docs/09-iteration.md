# 09 — How Iteration Works

## Adding a New Article

```bash
# Step 1: Copy an existing article as your template
cp athletic-edge.html your-new-article.html

# Step 2: Update the <head> section
# - Change <title>
# - Change <meta name="description">
# - Change og:title, og:description, og:url

# Step 3: Update article-hero section
# - Category, read time, date
# - Headline and subtitle

# Step 4: Replace all prose content
# (keep the author block and footer band)

# Step 5: Add to index.html Thinking section
# Copy an existing article card, update title/excerpt/link

# Step 6: Add to sitemap.xml
# Add a new <url> block

# Step 7: Test locally, then push
git add your-new-article.html index.html sitemap.xml
git commit -m "content: publish [Article Title] article"
git push origin main
```

---

## Adding a New Venture

In `index.html`, find `<!-- ── VENTURES ── -->` and copy this block:

```html
<div class="venture-item reveal">
  <div class="venture-item__left">
    <span class="venture-cat">CATEGORY NAME</span>
  </div>
  <div class="venture-item__center">
    <h3 class="venture-name">COMPANY NAME</h3>
    <p class="venture-desc">One sentence description of what the company does.</p>
  </div>
  <div class="venture-item__right">
    <a href="https://company.com" target="_blank" rel="noopener" class="venture-link">
      Visit <span class="venture-arrow">→</span>
    </a>
  </div>
</div>
```

**For ventures without a public website**, use `href="#contact"` and change the link text to `Inquire` or `Connect`.

**Also update:** the story stat `<span class="story__stat-n">6</span> Active Ventures` to reflect the new count.

---

## Modifying the Design System

**Always modify tokens, not individual styles.**

```css
/* ✅ Right way — change the token */
:root {
  --red: #D42040;   /* Updated cardinal red */
}
/* All 50+ uses of var(--red) update automatically */

/* ❌ Wrong way — hardcode individual elements */
.nav__logo { color: #D42040; }
.btn--red { background: #D42040; }
/* Misses 48 other places */
```

---

## Updating Content (Bio, Stats, Speaking)

All content is directly in `index.html`. Use your editor's Find (Cmd+F) to locate text:

| Content to Update | Search for |
|------------------|------------|
| Bio paragraphs | `class="story__bio"` |
| Stats | `class="story__stat-n"` |
| Speaking items | `class="speaking-item"` |
| Nav links | `class="nav__links"` |
| Footer copy | `class="footer"` |

---

## AI-Assisted Development Workflow

This site is maintained with Claude Code. Best practices for AI-assisted work:

```
1. Describe what you want to change in plain English
   "Add a new venture called Acme Corp in the Technology category"

2. Let the AI generate the HTML block

3. Review the output before it's committed
   (check the diff: git diff)

4. Test locally (python3 -m http.server 3456)

5. Approve and push

Never let AI push directly without reviewing the diff first.
```

**Things AI does well on this codebase:**
- Adding new HTML blocks (following existing patterns)
- Batch updates across multiple files (font imports, meta tags, etc.)
- CSS additions that follow the existing design system
- Writing new article content in the established prose style

**Things to be careful about:**
- Global find/replace across CSS (can break other elements)
- Removing CSS classes (may be used elsewhere)
- Changing design tokens (affects all uses)

---

## Safe Experimentation Guidelines

```
Rule 1: Always start from main
  git pull origin main

Rule 2: Test locally before pushing
  python3 -m http.server 3456

Rule 3: Check the diff before committing
  git diff

Rule 4: Make one change at a time
  Easier to debug, easier to revert

Rule 5: Rollback is easy
  git revert HEAD && git push origin main
```

---

## Content Update Frequency Recommendations

| Content | Recommended Frequency |
|---------|----------------------|
| New articles | 1-2 per quarter |
| Speaking section | Update after each engagement |
| Venture descriptions | Update when product/focus changes |
| Bio paragraphs | Update after major milestones |
| Stats (ventures, degrees, etc.) | Update when numbers change |
| OG image | Update if brand positioning changes |
