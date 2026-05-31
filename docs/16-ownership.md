# 16 — Ownership Model

## Ownership Matrix

| Domain | Owner | Backup | Access Required |
|--------|-------|--------|----------------|
| **Frontend (HTML/CSS/JS)** | Lead contributor | Any contributor | GitHub write access |
| **Design system (styles.css)** | Lead contributor | Abhi approval for token changes | GitHub write access |
| **Content (articles, bio, ventures)** | Abhi Prakash | Lead contributor for formatting | GitHub write access |
| **Analytics (GA4)** | Abhi Prakash | — | Google account access |
| **Form submissions (Formspree)** | Abhi Prakash | — | Formspree account access |
| **Domain registration** | Abhi Prakash | — | Domain registrar account |
| **GitHub repository** | AbhiPrakash10 | — | GitHub account (owner) |
| **Documentation (this folder)** | Lead contributor | Abhi Prakash | GitHub write access |

---

## Decision Authority

| Decision Type | Who Decides | Process |
|--------------|-------------|---------|
| Brand positioning, voice, tone | Abhi Prakash | Abhi decides, contributor implements |
| Design system changes (colors, fonts) | Abhi Prakash | Abhi approves before merge |
| New article content | Abhi Prakash | Abhi writes, contributor formats/publishes |
| Bug fixes | Any contributor | Fix, test, push |
| New features / pages | Abhi Prakash | Discuss first, implement after approval |
| Infrastructure changes | Abhi Prakash | High-impact — always discuss first |
| Minor content edits | Any contributor | Fix and push |

---

## Contributor Roles

### Abhi Prakash (Owner)
- Content strategy and voice
- Brand decisions
- All published article content
- Venture descriptions and business context
- Analytics access and interpretation
- Final approval on design or architecture changes

### Lead Contributor (Engineer/Designer)
- Day-to-day code changes
- Feature implementation
- Bug fixes
- Documentation updates
- Performance monitoring
- Deployment

### Content Contributor
- Article formatting and HTML markup
- Proofreading
- sitemap.xml updates when new content is added

---

## Ownership Transfer Procedure

If the lead contributor changes:

```
□ 1. New contributor reads all docs in /docs folder (1-2 hours)
□ 2. Abhi adds new contributor as GitHub collaborator
□ 3. New contributor clones repo, runs locally, verifies site works
□ 4. Outgoing contributor does a 1-hour walkthrough:
      - Key files (index.html, styles.css, script.js)
      - Recent changes (git log)
      - Any in-progress work
□ 5. New contributor makes a minor test change (e.g., update a date)
      Commits, pushes, verifies live — confirms deployment access
□ 6. Update this ownership table
□ 7. Outgoing contributor's GitHub access revoked after 2-week overlap
```

---

## Service Account Transfer

If Abhi needs to transfer service ownership:

| Service | Transfer Method |
|---------|----------------|
| GitHub repo | Transfer repo ownership in GitHub Settings |
| Google Analytics | Add new owner in GA4 Admin → Account Access |
| Formspree | Change notification email in Formspree settings |
| Domain | Transfer at domain registrar (involves auth code) |
