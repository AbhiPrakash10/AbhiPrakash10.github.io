# 15 — What We Intentionally Did NOT Build Yet

## Feature Gaps by Category

### Content Management
| Feature | Status | Why Deferred |
|---------|--------|-------------|
| CMS (Notion, Contentful, etc.) | ❌ Not built | Publish frequency doesn't justify complexity |
| Article version history | ❌ Not built | Git history serves this purpose |
| Draft/preview workflow | ❌ Not built | Preview locally before pushing |
| Content scheduling | ❌ Not built | Publish manually when ready |
| Article tagging / filtering | ❌ Not built | <10 articles — not needed |
| Search | ❌ Not built | <10 articles — nav is sufficient |

### User Experience
| Feature | Status | Why Deferred |
|---------|--------|-------------|
| Dark mode toggle | ❌ Not built | Site has distinct light/dark sections already |
| Article comments | ❌ Not built | Increases moderation burden, not aligned with brand |
| Social sharing buttons | ❌ Not built | OG tags handle social sharing at link level |
| Newsletter signup | ❌ Not built | No email list strategy yet |
| Podcast player | ❌ Not built | No podcast yet |
| Video embeds | ❌ Not built | No video content yet |
| Multi-language | ❌ Not built | English-only audience at this stage |

### Infrastructure
| Feature | Status | Why Deferred |
|---------|--------|-------------|
| Staging environment | ❌ Not built | Low-risk static site, instant rollback |
| Automated testing | ❌ Not built | Minimal dynamic logic to test |
| CI/CD pipeline | ❌ Not built | GitHub Pages auto-deploy is sufficient |
| Error monitoring (Sentry) | ❌ Not built | Low JS complexity, manual monitoring sufficient |
| Image optimization (WebP) | ❌ Not built | Performance acceptable without it |
| CDN purge control | ❌ Not built | GitHub Pages handles automatically |

### Business Features
| Feature | Status | Why Deferred |
|---------|--------|-------------|
| CRM / contact database | ❌ Not built | Ready for Airtable integration via Formspree |
| Email automation | ❌ Not built | No email list yet |
| Lead scoring | ❌ Not built | Volume too low to need scoring |
| Authentication | ❌ Not built | No private content yet |
| Payment processing | ❌ Not built | No commerce yet |
| Calendar booking | ❌ Not built | Calendly link could be added simply |
| Portfolio metrics dashboard | ❌ Not built | GA4 provides sufficient analytics |

---

## Deferred Architecture Decisions

### "Should we use a static site generator?"
**Decision:** No — for now. Raw HTML is more readable and requires no tooling.  
**Revisit when:** Article count exceeds 20 and manually copying templates becomes painful.

### "Should we use Next.js or a React framework?"
**Decision:** No — the current complexity does not justify a framework.  
**Revisit when:** Dynamic data (user accounts, real-time content, personalization) is needed.

### "Should we self-host fonts instead of using Google Fonts?"
**Decision:** No — Google Fonts is reliable, fast, and free.  
**Revisit when:** Privacy regulations require it, or Google Fonts becomes unreliable.

---

## Known Constraints

- **No server-side logic** — everything is client-side or delegated to third-party services
- **No database** — content lives in HTML files
- **No user accounts** — no personalization possible
- **GitHub Pages bandwidth limit** — 100GB/month (virtually unlimited for this site's traffic)
- **Formspree free tier** — 250 submissions/month hard limit

---

## The Intentional Simplicity Principle

> Every feature not built is a maintenance burden avoided, a security surface not exposed, and a complexity not inherited by the next contributor.

The goal is to add complexity only when the problem it solves is demonstrably larger than the cost of maintaining it.
