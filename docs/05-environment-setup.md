# 05 — Environment Setup & Prerequisites

## Required Software

| Software | Version | Purpose | Install |
|----------|---------|---------|---------|
| Git | Any modern | Version control, deployment | https://git-scm.com |
| Python 3 | 3.8+ | Local dev server | Pre-installed on macOS |
| Web browser | Any modern | Testing | Chrome recommended |
| Code editor | Any | Editing files | VS Code recommended |

**That's it.** No Node.js, no npm, no package manager required.

---

## Required Accounts

| Account | Purpose | URL | Cost |
|---------|---------|-----|------|
| GitHub (AbhiPrakash10) | Repository access, deployment | github.com | Free |
| Google Analytics | View analytics data | analytics.google.com | Free |
| Formspree | View form submissions | formspree.io | Free |
| Domain registrar | Domain renewal (~annual) | Wherever domain is registered | ~$12/yr |

---

## No API Keys Required for Local Dev

The site runs entirely without API keys locally. Third-party services (GA4, Formspree) only activate in the browser on the live site.

**For contributors:** You can develop and preview all UI changes locally without any account access.

---

## Day 1 Setup Checklist

```
□ 1. Install Git (if not already installed)
      git --version   ← verify: should show version number

□ 2. Configure Git identity
      git config --global user.name "Your Name"
      git config --global user.email "your@email.com"

□ 3. Clone the repository
      git clone https://github.com/AbhiPrakash10/AbhiPrakash10.github.io.git
      cd AbhiPrakash10.github.io

□ 4. Start local dev server
      python3 -m http.server 3456

□ 5. Open in browser
      http://localhost:3456

□ 6. Verify site loads correctly
      ← Hero section visible
      ← Navigation links work
      ← Story section loads with photo
      ← Ventures section shows 6 items
      ← Contact form renders

□ 7. Request GitHub repo access from Abhi (if writing access needed)
      ← Abhi grants collaborator access via GitHub Settings

□ 8. Verify push access (if applicable)
      git push   ← should succeed without errors
```

**Estimated setup time:** 10–15 minutes

---

## Common Setup Failures

| Problem | Cause | Fix |
|---------|-------|-----|
| `python3: command not found` | Python not installed or named differently | Try `python --version`; install from python.org |
| Port 3456 already in use | Another process using the port | Use a different port: `python3 -m http.server 4000` |
| Fonts not loading | CORS restrictions on file:// protocol | Must use http.server (not file://) |
| Images not loading | Same CORS issue | Same — use http.server |
| `git clone` fails | No internet or GitHub is down | Check github.com status |
| Push rejected | No write access | Request collaborator access from Abhi |
| Site looks wrong | Browser cache | Hard refresh: Cmd+Shift+R (Mac) / Ctrl+Shift+R (Windows) |

---

## VS Code Recommended Extensions

```
- Live Server (optional, alternative to python3 http.server)
- Prettier (code formatting)
- CSS Variable Autocomplete (for --red, --midnight, etc.)
- GitLens (git history inline)
```
