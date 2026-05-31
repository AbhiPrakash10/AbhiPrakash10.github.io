# 17 — New Contributor Onboarding Guide

## Before Day 1

Abhi should provide:
- [ ] GitHub collaborator invitation (Settings → Collaborators)
- [ ] Brief on current priorities and any in-progress work
- [ ] Access to relevant service accounts (if needed for the role)

---

## Day 1 Checklist (2-3 hours)

### Setup (30 min)
```
□ Read docs/README.md — get the lay of the land
□ Clone the repository:
    git clone https://github.com/AbhiPrakash10/AbhiPrakash10.github.io.git
□ Start local server:
    cd AbhiPrakash10.github.io
    python3 -m http.server 3456
□ Open http://localhost:3456 — scroll through the entire site
□ Open DevTools (F12) — confirm zero console errors
```

### Read the Code (60 min)
```
□ Read index.html from top to bottom (30 min)
    — understand every section
    — notice how the design patterns repeat
□ Skim styles.css — read the 22 section headers (5 min)
□ Read script.js — understand the 7 modules (15 min)
□ Read article.js — simple, 20 lines (2 min)
□ Open lightside.html — compare structure to index.html (8 min)
```

### Read the Docs (30 min)
```
□ 01-executive-summary.md — why this exists
□ 02-architecture.md — how it's built
□ 07-git-deployment.md — how to deploy
□ 10-runbooks.md — common operations
□ 13-security.md — what not to do
```

### First Action (20 min)
```
□ Make a trivial change (e.g., fix a typo or update the copyright year)
□ Commit it: git commit -m "chore: verify contributor access"
□ Push it: git push origin main
□ Verify it appears live on abhiprakash.com within 5 minutes
□ Revert if needed: git revert HEAD && git push origin main
```

---

## Day 7 Expectations

By the end of your first week, you should be able to:

- [ ] Deploy a content update without assistance
- [ ] Add a new venture item to index.html
- [ ] Fix a broken link
- [ ] Identify where in `styles.css` to make a visual change
- [ ] Run Lighthouse and interpret the results
- [ ] Explain the site's architecture to a non-technical person

---

## First Recommended Tasks (By Role)

### Engineer
1. Fix any open issues tagged `bug` in GitHub Issues
2. Implement WebP image optimization for the profile photo
3. Add a custom Formspree → Airtable integration
4. Set up Google Search Console and submit sitemap

### Designer
1. Review the site on 5+ devices/screen sizes
2. Run a full Lighthouse accessibility audit
3. Identify any spacing or typography inconsistencies
4. Propose improvements to the article reading experience

### Content Contributor
1. Proofread all 5 published articles
2. Verify all external links are live
3. Draft outline for the next article (coordinate with Abhi)

---

## How Communication Works

| Topic | Channel |
|-------|---------|
| Technical questions | GitHub Issues |
| Content decisions | Direct with Abhi |
| Design feedback | GitHub Issues or direct |
| Urgent issues (site down) | Text Abhi directly |

---

## How Decisions Get Made

```
1. Small changes (bug fixes, typos, minor CSS): 
   → Just do it, push, notify Abhi

2. Medium changes (new section, content update):
   → Discuss with Abhi before implementing
   → Implement, show locally, get approval
   → Then push

3. Large changes (architecture, new services, redesign):
   → Write a proposal (even a brief Notion doc)
   → Discuss with Abhi
   → Get explicit sign-off before touching code
```

---

## Where Everything Lives

| Resource | Location |
|----------|----------|
| Code | github.com/AbhiPrakash10/AbhiPrakash10.github.io |
| Documentation | github.com/AbhiPrakash10/AbhiPrakash10.github.io/tree/main/docs |
| Analytics | analytics.google.com |
| Form submissions | formspree.io |
| Live site | abhiprakash.com |
