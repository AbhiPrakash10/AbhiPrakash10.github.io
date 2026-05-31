# 12 — Monitoring, Logging & Debugging

## Monitoring Stack

| Tool | What It Monitors | Access |
|------|----------------|--------|
| Google Analytics GA4 | Traffic, behavior, conversions | analytics.google.com |
| Formspree Dashboard | Form submissions, spam | formspree.io |
| GitHub Actions | Deployment status | github.com/AbhiPrakash10/.../actions |
| Browser DevTools | Client-side errors, performance | F12 in any browser |

**There is no server-side logging** (static site — no server).

---

## Top 10 Things Most Likely to Break

| # | Problem | Detection | Fix |
|---|---------|-----------|-----|
| 1 | Domain expires | Site unreachable | Renew at registrar |
| 2 | GitHub Pages deployment fails | Site shows old version | Check Actions tab |
| 3 | Formspree endpoint hits rate limit | Form returns error | Upgrade Formspree plan |
| 4 | External venture link goes dead | Visitor gets 404 | Update href in index.html |
| 5 | Google Fonts blocked by browser | System fonts render | Acceptable degradation |
| 6 | DNS misconfiguration | Site unreachable | Restore A records |
| 7 | Bad commit breaks layout | Visual regression on site | git revert HEAD, push |
| 8 | JS error in script.js | Form or nav broken | Check DevTools console |
| 9 | Mobile nav stuck open | UX broken on mobile | Check navToggle event listener |
| 10 | Reading progress bar missing | JS error in article.js | Check article.js is linked |

---

## Debugging Workflow

### Step 1: Reproduce the problem
```
- What exactly is broken?
- On which page?
- On which device/browser?
- Did it work before? When did it break?
- Check git log for recent changes: git log --oneline -10
```

### Step 2: Check browser DevTools
```
F12 → Console tab
- Any red errors? → Fix the JS error
- Any yellow warnings? → Lower priority

F12 → Network tab
- Any 404s? → Missing file or wrong path
- Any failed API calls? → Formspree or GA4 issue

F12 → Elements tab
- Is the HTML correct?
- Are the CSS classes applied?
- Are CSS variables resolving?
```

### Step 3: Check recent commits
```bash
git log --oneline -10
git diff HEAD~1 HEAD     # what changed in last commit
git show HEAD            # full diff of last commit
```

### Step 4: Test locally
```bash
python3 -m http.server 3456
# Reproduce the bug locally
# If not reproducible locally → likely a deployment or CDN issue
```

### Step 5: Fix and verify
```bash
# Make fix
# Test locally
# Commit and push
# Verify on abhiprakash.com
```

---

## Key Analytics Checks

### Weekly (5 minutes)
- Users (last 7 days vs prior 7 days)
- Top traffic sources (organic, direct, social)
- Top pages (which articles are popular)

### Monthly (15 minutes)
- User acquisition trends
- Engagement rate (are people scrolling/reading?)
- Contact form events (if custom events configured)
- Geographic distribution (where are visitors from?)

---

## Performance Monitoring

Run Lighthouse audit monthly or after major changes:

```
Chrome DevTools → Lighthouse → Generate report

Target scores:
  Performance:   90+
  Accessibility: 95+
  Best Practices: 95+
  SEO:           95+
```

**Known performance considerations:**
- Google Fonts add ~200ms to render time (network request)
- Large hero image (Prakash_Abhi-015.jpg) — consider WebP conversion
- No lazy loading on images (low impact, few images)

---

## Deployment Status Check

```
github.com/AbhiPrakash10/AbhiPrakash10.github.io/actions
→ Should show green checkmark on latest commit
→ If red X: click to see error details
→ Most common: syntax error in HTML (unclosed tag)
```
