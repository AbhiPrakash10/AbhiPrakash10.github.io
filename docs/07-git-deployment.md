# 07 — Git Workflow, Branching Strategy & Deployment

## Deployment Architecture

```
Developer edits files locally
         ↓
git commit + git push origin main
         ↓
GitHub receives push
         ↓
GitHub Pages auto-builds (30-60 seconds)
         ↓
Fastly CDN propagates (~1-5 minutes total)
         ↓
Live at abhiprakash.com
```

**There is no CI/CD pipeline, no test suite, no staging environment.** Every push to `main` deploys directly to production.

---

## Branching Strategy

### Current (Solo/Small Team)
All changes go directly to `main`. This is appropriate for the current team size and site risk level.

### Recommended (When Team Grows)
```
main         ← production (always deployable)
dev          ← integration branch
feature/*    ← individual features (feature/add-newsletter)
fix/*        ← bug fixes (fix/form-validation)
content/*    ← content-only changes (content/new-article-fusion)
```

**Branch naming convention:**
```
feature/short-description
fix/what-is-broken
content/article-or-section-name
```

---

## Commit Message Convention

```
<type>: <short description>

Types:
  feat     — new feature or section
  fix      — bug fix
  content  — content update (articles, bio, ventures)
  style    — CSS/design changes only
  refactor — code restructure, no behavior change
  docs     — documentation updates
  chore    — maintenance (dependencies, config)

Examples:
  feat: add RightsOS to ventures section
  fix: correct active ventures stat from 4 to 6
  content: publish Athletic Edge article
  style: increase hero headline weight on mobile
  docs: add architecture diagram to docs/02
```

---

## Step-by-Step Production Deployment

```bash
# 1. Pull latest (always start here)
git pull origin main

# 2. Make your changes
# (edit files)

# 3. Review what changed
git diff
git status

# 4. Stage specific files (never use git add -A blindly)
git add index.html styles.css

# 5. Commit with a clear message
git commit -m "feat: add reading progress bar to article pages"

# 6. Push to main (triggers deployment)
git push origin main

# 7. Verify deployment
# Wait 1-5 minutes, then check:
open https://abhiprakash.com
# Hard refresh: Cmd+Shift+R

# 8. Confirm the change is live
# (visual check on the specific area you changed)
```

---

## Rollback Procedure

If a deployment causes a problem:

```bash
# Option A: Revert the last commit (creates a new commit)
git revert HEAD
git push origin main

# Option B: Reset to a previous known-good commit (destructive)
git log --oneline       # find the good commit hash
git reset --hard <hash>
git push --force origin main   # use with extreme caution
```

**Option A is always preferred.** Option B force-push should only be used for critical emergencies.

---

## Pre-Deploy Checklist

```
□ Pulled latest from main before starting
□ Tested locally (python3 -m http.server 3456)
□ No console errors in DevTools
□ Visual check on desktop and mobile
□ Relevant links still work
□ Contact form still renders correctly
□ No secrets or API keys in committed files
□ Commit message is clear and follows convention
```

---

## Post-Deploy Verification

```
□ abhiprakash.com loads (hard refresh)
□ Specific change is visible/working
□ No visual regressions on other sections
□ GA4 receiving events (check real-time in analytics.google.com)
□ No 404s for linked resources (DevTools → Network)
```

---

## GitHub Pages Settings

To verify/configure GitHub Pages:
1. Go to https://github.com/AbhiPrakash10/AbhiPrakash10.github.io/settings/pages
2. Source: **Deploy from a branch**
3. Branch: **main** / **/ (root)**
4. Custom domain: **abhiprakash.com**
5. Enforce HTTPS: **✅ Enabled**
