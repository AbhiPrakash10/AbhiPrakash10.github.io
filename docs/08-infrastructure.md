# 08 — Infrastructure, Integrations & External Services

## Complete Service Inventory

| Service | Role | URL | Cost | Free Tier Limit |
|---------|------|-----|------|----------------|
| **GitHub Pages** | Hosting + CDN | github.com/AbhiPrakash10 | Free | 1GB storage, 100GB/month bandwidth |
| **Google Fonts** | Typography | fonts.googleapis.com | Free | Unlimited |
| **Google Analytics GA4** | Analytics | analytics.google.com | Free | Unlimited hits |
| **Formspree** | Contact form backend | formspree.io/f/xojbkeeb | Free | 250 submissions/month |
| **Custom Domain** | Brand URL | Domain registrar | ~$12/yr | — |
| **Fastly CDN** | CDN (via GitHub Pages) | fastly.com | Free (bundled) | — |

**Total monthly cost: $0** (excluding ~$1/month amortized domain cost)

---

## Service Details

### GitHub Pages
- **Purpose:** Hosts all static files, serves the website globally
- **Auto-deploy:** Every push to `main` branch triggers a build
- **CDN:** Fastly CDN is bundled — files served from edge nodes globally
- **HTTPS:** Automatically managed via Let's Encrypt
- **Failure mode:** If GitHub is down, site is unreachable. No fallback.
- **Vendor lock-in risk:** Low — standard static files work on any host (Netlify, Vercel, Cloudflare Pages)
- **Migration path:** Copy files to new host, update DNS records

### Google Fonts
- **Purpose:** Inter, Inter Tight, Great Vibes fonts loaded from Google CDN
- **Failure mode:** If blocked, browser falls back to system fonts (Arial, Helvetica). Acceptable degradation.
- **Performance note:** Fonts are loaded with `display=swap` by default — text visible immediately with fallback font
- **Privacy note:** Google Fonts logs IP addresses. For maximum privacy, fonts could be self-hosted.

### Google Analytics GA4
- **Measurement ID:** G-6EWRLB434Y
- **Purpose:** Track page views, sessions, traffic sources, user behavior
- **Access:** analytics.google.com (Abhi's Google account)
- **Failure mode:** If blocked by ad blocker, that visitor is not tracked. This is normal and acceptable.
- **Data retention:** 14 months by default in GA4
- **Key reports to monitor:**
  - Realtime (live visitors)
  - Acquisition (traffic sources)
  - Engagement (pages, scroll depth)
  - Demographics (who's visiting)

### Formspree
- **Endpoint:** https://formspree.io/f/xojbkeeb
- **Purpose:** Receives contact form submissions, forwards to abhiprakash20@gmail.com
- **Free tier:** 250 submissions/month (more than sufficient)
- **Dashboard:** formspree.io (log in to view submissions)
- **Failure mode:** If Formspree is down, form shows "Network error" message. Direct email is listed on the page as fallback.
- **Future upgrade:** Connect Formspree → Airtable via Formspree Integrations dashboard (no code required)
- **Spam protection:** Honeypot field (`_gotcha`) in form HTML. Formspree also has reCAPTCHA option.
- **Vendor lock-in risk:** Low — endpoint URL is in `script.js`, easily changed to any form backend

---

## Dependency Map

```
abhiprakash.com
├── GitHub Pages (required — hosting)
│   └── Fastly CDN (bundled)
├── Google Fonts (optional — graceful degradation)
│   ├── Inter
│   ├── Inter Tight
│   └── Great Vibes
├── Google Analytics (optional — analytics only)
└── Formspree (required for contact form)
    └── Gmail (form submissions forwarded here)
```

---

## Cost Scaling Analysis

| Scenario | Monthly Cost | Notes |
|----------|-------------|-------|
| Current (0-250 form submissions) | $0 | All free tiers |
| Growing (250-1000 form submissions) | ~$19 | Formspree Basic plan |
| High traffic (>100GB bandwidth) | ~$0 | GitHub Pages is still free |
| Adding email newsletter | $15-30/mo | Mailchimp, ConvertKit, or similar |
| Adding CRM (Airtable) | $0-20/mo | Free tier covers early stage |

---

## Future Services (Not Yet Integrated)

| Service | Purpose | When to Add |
|---------|---------|------------|
| Airtable | CRM — store and manage contacts | When form submissions need tracking |
| Make.com or n8n | Workflow automation | When CRM automation is needed |
| Mailchimp / ConvertKit | Email newsletter | When building an email list |
| Cloudflare | DNS + additional CDN/security | When wanting more control over CDN |
| Sentry | Error monitoring | When adding more JS complexity |
| Plausible | Privacy-respecting analytics | If replacing GA4 |
