# 10 — Operational Runbooks

## Runbook: Deploy a Content Update

```
□ 1. git pull origin main
□ 2. Make changes in editor
□ 3. python3 -m http.server 3456 → verify locally
□ 4. git diff → review all changes
□ 5. git add <specific files>
□ 6. git commit -m "content: description"
□ 7. git push origin main
□ 8. Wait 2-5 minutes
□ 9. abhiprakash.com → hard refresh → verify live
```

---

## Runbook: Add a New Article

```
□ 1. cp athletic-edge.html new-article-name.html
□ 2. Update <head>: title, description, og:title, og:description, og:url
□ 3. Update article-hero: category, read time, date, headline, subtitle
□ 4. Replace prose content (keep author block + footer band)
□ 5. In index.html: add article card to .thinking__grid
□ 6. In sitemap.xml: add <url> block for new page
□ 7. Test locally: all links, reading progress bar, nav
□ 8. Commit: git add new-article.html index.html sitemap.xml
□ 9. Push and verify live
```

---

## Runbook: Fix a Broken Link

```
□ 1. Identify broken link (URL or anchor)
□ 2. Search index.html (or article file) for the href value
□ 3. Update href to correct URL
□ 4. Verify locally (click the link)
□ 5. Commit and push
```

---

## Runbook: Update Contact Form Endpoint

If Formspree endpoint needs to change:

```
□ 1. Log in at formspree.io
□ 2. Create new form or copy existing endpoint
□ 3. In script.js, find:
      fetch('https://formspree.io/f/xojbkeeb'
□ 4. Replace endpoint URL with new one
□ 5. Test form locally (submit a test message)
□ 6. Verify submission arrives in Gmail
□ 7. Commit and push
```

---

## Runbook: Site is Down / Unreachable

```
□ 1. Check https://www.githubstatus.com (GitHub Pages outage?)
□ 2. Check DNS: dig abhiprakash.com
      Should return: 185.199.108.153, 185.199.109.153, etc.
□ 3. Check GitHub Pages settings:
      github.com/AbhiPrakash10/AbhiPrakash10.github.io/settings/pages
      - Source: Deploy from branch (main)
      - Custom domain: abhiprakash.com
      - Enforce HTTPS: enabled
□ 4. Check for recent commits that may have broken something:
      git log --oneline -5
□ 5. If a bad commit: git revert HEAD && git push origin main
□ 6. If DNS issue: restore A records at domain registrar:
      185.199.108.153
      185.199.109.153
      185.199.110.153
      185.199.111.153
□ 7. DNS changes take up to 24 hours to propagate
```

---

## Runbook: Contact Form Not Receiving Submissions

```
□ 1. Check formspree.io dashboard (log in, view submissions)
□ 2. Check Gmail spam folder (abhiprakash20@gmail.com)
□ 3. Submit a test form on abhiprakash.com
□ 4. Open DevTools → Network → look for POST to formspree.io
□ 5. Check response: should be 200 with {"ok":true}
□ 6. If 429 (rate limited): free tier limit (250/month) hit — upgrade Formspree plan
□ 7. If endpoint error: check script.js for correct URL
□ 8. If honeypot triggered (false positive): check _gotcha field is truly hidden
```

---

## Runbook: Update Analytics Property

```
□ 1. Go to analytics.google.com
□ 2. Create new GA4 property if needed
□ 3. Copy new Measurement ID (G-XXXXXXXXXX)
□ 4. In all 6 HTML files, find: G-6EWRLB434Y
□ 5. Replace with new Measurement ID (use Python batch script)
□ 6. Commit and push all 6 files
□ 7. Verify in GA4 Real-time report: visit site, confirm event appears
```

---

## Runbook: Add a New Third-Party Script

```
□ 1. Evaluate: is this script necessary?
□ 2. Check performance impact (use WebPageTest or Lighthouse)
□ 3. Add script to <head> with async or defer attribute
□ 4. Add to ALL pages that need it (index.html + article pages if relevant)
□ 5. Test locally (no console errors)
□ 6. Test on mobile (no layout shift)
□ 7. Commit with clear message explaining what/why
```

---

## Runbook: Renew the Domain

```
□ 1. Log in to domain registrar (where abhiprakash.com is registered)
□ 2. Renew for 1-5 years
□ 3. Confirm auto-renew is enabled (recommended)
□ 4. Verify DNS records are still correct:
      A @ 185.199.108.153
      A @ 185.199.109.153
      A @ 185.199.110.153
      A @ 185.199.111.153
      CNAME www AbhiPrakash10.github.io
□ 5. Verify HTTPS still works after renewal
```
