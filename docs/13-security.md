# 13 — Security & Secrets Management

## What Secrets Exist

| Secret | Value | Where Stored | Who Has Access |
|--------|-------|-------------|----------------|
| GA4 Measurement ID | G-6EWRLB434Y | In HTML (public — expected) | Anyone (not sensitive) |
| Formspree Endpoint | xojbkeeb | In script.js (public — expected) | Anyone (not sensitive) |
| GitHub credentials | Abhi's personal GitHub account | GitHub.com | Abhi only |
| Gmail account | abhiprakash20@gmail.com | Not in code | Abhi only |
| Domain registrar login | N/A | Not in code | Abhi only |

**This is a public static site. There are genuinely no backend secrets to protect at this stage.**

The GA4 ID and Formspree endpoint are intentionally public — they appear in browser source code and are expected to. They cannot be misused meaningfully (GA4 IDs are tied to a domain, Formspree endpoints are rate-limited).

---

## What Should NEVER Be Committed

```
❌ .env files of any kind
❌ Private API keys (even for future integrations)
❌ OAuth tokens or bearer tokens
❌ Database credentials
❌ Private SSH keys
❌ Payment processor secrets (Stripe secret key, etc.)
❌ Service account credentials (Google Cloud, AWS, etc.)
❌ Admin passwords of any kind
```

**Rule:** If a key is labeled "secret" by the service providing it — it never goes in a file that gets committed to git.

---

## Access Management

### GitHub Repository
- **Owner:** AbhiPrakash10 (Abhi's personal account)
- **Collaborators:** Added via Settings → Collaborators
- **Default:** Repository is public (read access to anyone, write access to collaborators only)

### Service Accounts
| Service | Login | Who Controls |
|---------|-------|-------------|
| GitHub | abhi's Google/GitHub account | Abhi |
| Google Analytics | abhi's Google account | Abhi |
| Formspree | abhiprakash20@gmail.com | Abhi |
| Domain Registrar | Registrar account | Abhi |

---

## Security Checklist

```
□ HTTPS enforced (GitHub Pages does this automatically)
□ No secrets in committed code
□ Contact form honeypot field present (_gotcha)
□ External links use rel="noopener" (prevents tab hijacking)
□ No user-generated content stored (static site)
□ No authentication system (no auth to secure)
□ No database (no SQL injection surface)
□ Dependencies: only Google Fonts, GA4, Formspree (all reputable)
```

---

## If a Secret Is Accidentally Committed

```
□ 1. Immediately rotate the secret (revoke old key, generate new one)
□ 2. Do NOT try to rewrite git history (ineffective — secret is already exposed)
□ 3. Check if the secret was used maliciously (service dashboard logs)
□ 4. Update all places the secret was used with the new value
□ 5. Commit and push the fix
□ 6. Document the incident
```

---

## Future Security Considerations

When the platform grows to include:
- **Backend/API:** Use environment variables, never hardcode secrets
- **Authentication:** Use an established provider (Auth0, Clerk, Supabase Auth)
- **Database:** Use row-level security, principle of least privilege
- **CMS:** Ensure editor access is role-based
- **Payment processing:** Never handle card data directly — use Stripe.js
