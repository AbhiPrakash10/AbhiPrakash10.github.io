# 14 — Scaling, Technical Debt & Future Architecture

## Expected Growth Assumptions

| Metric | Current | 1 Year | 3 Years |
|--------|---------|--------|---------|
| Monthly visitors | ~500 | ~5,000 | ~25,000 |
| Articles | 5 | 15 | 40 |
| Form submissions | <50/mo | ~200/mo | ~500/mo |
| Ventures | 6 | 8 | 12 |
| Team size | 1 | 2-3 | 4-6 |

---

## Current Bottlenecks

| Bottleneck | Impact | Threshold | Solution |
|-----------|--------|-----------|---------|
| Formspree 250/mo limit | Forms stop sending | ~250 submissions/month | Upgrade to Formspree Basic ($19/mo) |
| Manual HTML editing | Slow content updates | When publishing >4 articles/quarter | Add a CMS |
| No staging environment | All errors go live | When team grows beyond 1 | Add Netlify or Vercel preview deploys |
| No search | Visitors can't find articles | When >15 articles exist | Add Pagefind or Algolia DocSearch |

---

## Technical Debt

| Debt | Risk Level | When to Address |
|------|-----------|-----------------|
| No CMS | Medium | When content frequency increases |
| No automated testing | Low | When making frequent JS changes |
| No staging environment | Low | When team size > 2 |
| Images not WebP | Low | Performance optimization pass |
| OG image uses system fonts | Low | When brand refresh is due |
| No article search | Low | When >15 articles published |
| No newsletter signup | Medium | When email list becomes a priority |

---

## Intentionally Over-Engineered

- **Accessibility (WCAG AA):** More thorough than typical personal sites. Worth it — signals craft and professionalism.
- **CSS design system:** More structured than necessary for a single person. Worth it — makes scaling to a team easier.
- **Documentation (this folder):** More than most personal sites have. Worth it — enables delegation without founder bottleneck.

---

## Intentionally Under-Engineered

- **No CMS:** Direct HTML editing is fine for current publish frequency. Adding a CMS before it's needed creates complexity with no benefit.
- **No build process:** Unnecessary for a static site with vanilla code. Adds tooling overhead for zero gain at this scale.
- **No testing:** A personal brand site has minimal logic. Visual QA before each push is sufficient.
- **No staging:** Risk of a bad deployment is low and rollback is instant. Not worth the operational overhead yet.

---

## Future Architecture Roadmap

### Phase 2: CRM Integration (3-6 months)
```
Contact Form → Formspree → Airtable (CRM database)
                         → Make.com (automation)
                         → Email auto-reply (Gmail/SendGrid)
```

### Phase 3: Content Management (6-12 months)
```
Option A: Notion as CMS → NotionAPI → Static site generator
Option B: Contentful CMS → Next.js frontend → Vercel hosting
Option C: Write articles in Markdown → 11ty or Astro → GitHub Pages
```

### Phase 4: Community/Newsletter (12-18 months)
```
Email capture → ConvertKit/Beehiiv
Newsletter publishing
Subscriber-only content (requires auth)
```

### Phase 5: Product Integration (18+ months)
```
Lightbear.AI product demos embedded
PartnerOS partnership portal
Private investor portal (requires auth + database)
```

---

## What Should Be Rebuilt Later

| Component | Rebuild When | Rebuild Into |
|-----------|-------------|-------------|
| Contact form | Formspree limit hit | Custom Next.js API route + Airtable |
| Content management | >4 articles/quarter | Notion CMS or Contentful |
| Hosting | Outgrowing GitHub Pages | Vercel or Netlify (more control) |
| Analytics | Need custom events | Keep GA4, add custom event tracking |

## What Should Remain Simple

| Component | Keep Simple Because |
|-----------|--------------------| 
| HTML structure | Maximum readability for any contributor |
| CSS design tokens | Global changes via one variable |
| Navigation | Smooth scroll works perfectly for this site type |
| Footer | Static — no dynamic data needed |
