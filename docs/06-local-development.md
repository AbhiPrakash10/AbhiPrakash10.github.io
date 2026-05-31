# 06 — Local Development Workflow

## Starting the Local Server

```bash
# Navigate to the portfolio directory
cd /path/to/AbhiPrakash10.github.io

# Start the server
python3 -m http.server 3456

# Open in browser
open http://localhost:3456
```

The server serves files from the current directory. It has no hot-reload — **manually refresh the browser** after every file change.

---

## Development Workflow

```
1. Pull latest changes from main
   git pull origin main

2. Start local server
   python3 -m http.server 3456

3. Open http://localhost:3456 in browser

4. Edit file in your code editor (VS Code, etc.)

5. Save file

6. Refresh browser (Cmd+R / F5)

7. Verify change looks correct

8. Commit and push
   git add filename.html
   git commit -m "what and why"
   git push origin main

9. Wait 1-5 minutes, verify on abhiprakash.com
```

---

## Common Development Tasks

### Editing homepage content
```bash
# Open index.html, find the section you want
# All sections are commented:
# <!-- ── HERO ── -->
# <!-- ── STORY ── -->
# <!-- ── VENTURES ── -->
# etc.
```

### Editing styles
```bash
# All styles are in styles.css
# Find the section by number (e.g., "8. Ventures")
# Always use CSS variables — never hardcode colors
# ✅ color: var(--red);
# ❌ color: #C41E3A;
```

### Adding a new article
```bash
# 1. Copy an existing article as template
cp athletic-edge.html new-article.html

# 2. Update the head section
#    - <title>
#    - <meta name="description">
#    - og:title, og:description, og:url

# 3. Update the article-hero section
#    - category, read time, date, title, subtitle

# 4. Replace the prose content

# 5. Add a card in index.html (Thinking section)

# 6. Add the URL to sitemap.xml
```

### Updating a venture
```bash
# In index.html, find <!-- ── VENTURES ── -->
# Each venture follows this pattern:
<div class="venture-item reveal">
  <div class="venture-item__left">
    <span class="venture-cat">CATEGORY</span>
  </div>
  <div class="venture-item__center">
    <h3 class="venture-name">NAME</h3>
    <p class="venture-desc">DESCRIPTION</p>
  </div>
  <div class="venture-item__right">
    <a href="URL" target="_blank" rel="noopener" class="venture-link">
      Visit <span class="venture-arrow">→</span>
    </a>
  </div>
</div>
```

---

## Testing Checklist Before Pushing

```
□ Does the page load without console errors?
  (Open DevTools → Console tab)

□ Does the change look correct on desktop?
  (1200px+ width)

□ Does the change look correct on tablet?
  (DevTools → Toggle device toolbar → iPad)

□ Does the change look correct on mobile?
  (DevTools → Toggle device toolbar → iPhone)

□ Do all links still work?

□ Does the contact form still submit?
  (Test with real data — submissions go to Gmail)

□ Are there any obvious visual regressions?
  (Scroll through the full page)
```

---

## Browser DevTools Quick Reference

| Task | DevTools Location |
|------|------------------|
| Check console errors | F12 → Console |
| Inspect element styles | F12 → Elements → Computed |
| Test mobile layout | F12 → Toggle device toolbar (Ctrl+Shift+M) |
| Check network requests | F12 → Network |
| Test accessibility | F12 → Lighthouse → Accessibility |
| Check contrast | F12 → Elements → Color picker |

---

## No Build Step

There is intentionally no build step. What you edit is what ships. This means:

- ✅ No `npm install` required
- ✅ No `npm run build` required
- ✅ No compilation step
- ✅ No transpilation
- ❌ No TypeScript (use plain JavaScript)
- ❌ No Sass/SCSS (use plain CSS with custom properties)
- ❌ No JSX or template languages
