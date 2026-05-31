# 11 — Maintenance Responsibilities

## Weekly

```
□ Check Google Analytics for traffic spikes or drops
  → analytics.google.com → Realtime + Last 7 days

□ Check Formspree for new submissions
  → formspree.io dashboard OR check Gmail (abhiprakash20@gmail.com)

□ Respond to contact form submissions within 48 hours
```

---

## Monthly

```
□ Review GA4 — top pages, traffic sources, user behavior
  → Identify which articles are driving traffic
  → Identify where users drop off

□ Check all external links still work
  → Lightbear.ai, lightside.vc, asearis.com, partneros.xyz
  → LinkedIn, Instagram, GitHub profile links

□ Review Formspree submission volume
  → If approaching 250/month limit, upgrade plan

□ Check site on mobile (real device, not just DevTools)
  → Nav opens and closes
  → Form submits
  → Articles readable

□ Review Google Search Console (if set up)
  → Any crawl errors?
  → Any pages deindexed?
  → Any manual actions?
```

---

## Quarterly

```
□ Update bio and speaking section with new engagements
  → Any new speaking invitations or media appearances?

□ Refresh stats (Active Ventures count, etc.)
  → Any new ventures launched or closed?

□ Review venture descriptions — are they still accurate?
  → Company pivots, name changes, new products?

□ Publish new Thinking article (target: 1-2 per quarter)

□ Update sitemap.xml with any new pages

□ Audit OG image — does it still reflect current brand?

□ Run Lighthouse audit
  → google.com/lighthouse or DevTools → Lighthouse
  → Target: Performance 90+, Accessibility 95+, SEO 95+

□ Check if any new CSS/JS patterns need to be documented
```

---

## Annual

```
□ Renew domain registration (abhiprakash.com)
  → Set auto-renew if available

□ Review and update full bio

□ Reassess architecture — is static site still sufficient?
  → Is a CMS needed yet?
  → Are form submissions growing beyond Formspree free tier?

□ Review all article content — is it still accurate and relevant?

□ Audit all third-party services — any alternatives to evaluate?

□ Update documentation (this docs folder)
```

---

## Dependency Management

There are **no npm dependencies** to update. This is intentional.

The only "dependencies" are:
- Google Fonts (versioned by Google, stable)
- Formspree endpoint (stable, managed by Formspree)
- GA4 gtag.js script (stable, managed by Google)

No action required for routine dependency updates.

---

## Content Freshness Guidelines

| Content | Staleness Threshold | Action |
|---------|--------------------|---------| 
| Bio paragraphs | 6+ months with major life changes | Update |
| Speaking section | After each new engagement | Add new item |
| Venture descriptions | If product/focus changes | Update desc |
| Article prose | If facts become outdated | Add update note or revise |
| Stats (venture count, etc.) | When numbers change | Update immediately |
| OG image | If name, title, or brand positioning changes | Regenerate |
