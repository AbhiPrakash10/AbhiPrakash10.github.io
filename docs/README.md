# abhiprakash.com — Platform Documentation

**Version:** 1.0 · **Last Updated:** May 2026 · **Owner:** Abhi Prakash

> A competent team should be able to independently operate, maintain, improve, and scale this platform without relying on founder knowledge.

---

## What This Is

This is the engineering and operations reference for **abhiprakash.com** — a personal brand hub, venture showcase, recruiting tool, content engine, and growth platform spanning technology, investing, sports, entrepreneurship, leadership, and media.

---

## Documentation Index

| # | Section | Description |
|---|---------|-------------|
| 01 | [Executive Summary](./01-executive-summary.md) | Purpose, audiences, philosophy, value creation |
| 02 | [Platform Architecture](./02-architecture.md) | Frontend, hosting, integrations, diagrams |
| 03 | [Product Structure & UX](./03-product-structure.md) | Site map, page types, user flows, conversion funnels |
| 04 | [Repository Structure](./04-repository-structure.md) | File structure, key files, naming conventions |
| 05 | [Environment Setup](./05-environment-setup.md) | Prerequisites, accounts, Day 1 checklist |
| 06 | [Local Development](./06-local-development.md) | Running locally, workflow, commands |
| 07 | [Git Workflow & Deployment](./07-git-deployment.md) | Branching, deployment, rollback, release checklist |
| 08 | [Infrastructure & Integrations](./08-infrastructure.md) | All services, costs, failure modes |
| 09 | [How Iteration Works](./09-iteration.md) | Adding pages, features, content, AI workflows |
| 10 | [Operational Runbooks](./10-runbooks.md) | Step-by-step guides for common operations |
| 11 | [Maintenance Schedule](./11-maintenance.md) | Weekly, monthly, quarterly responsibilities |
| 12 | [Monitoring & Debugging](./12-monitoring.md) | Error detection, top 10 failure points, fix procedures |
| 13 | [Security & Secrets](./13-security.md) | Environment variables, access, what never to commit |
| 14 | [Scaling & Future Architecture](./14-scaling.md) | Growth assumptions, technical debt, what to rebuild |
| 15 | [Not Built Yet](./15-not-built.md) | Deferred decisions, missing features, roadmap |
| 16 | [Ownership Model](./16-ownership.md) | Who owns what, transfer procedures |
| 17 | [New Contributor Onboarding](./17-onboarding.md) | Day 1 checklist, first tasks, how decisions get made |
| 18 | [Glossary](./18-glossary.md) | Technical terms, internal terminology, acronyms |

---

## Quick Reference

```bash
# Run locally
cd portfolio && python3 -m http.server 3456
# Open: http://localhost:3456

# Deploy (all changes auto-deploy via GitHub Pages)
git add .
git commit -m "description of change"
git push origin main
# Live in 1-5 minutes at abhiprakash.com
```

**Repository:** https://github.com/AbhiPrakash10/AbhiPrakash10.github.io  
**Live Site:** https://abhiprakash.com  
**Analytics:** https://analytics.google.com (G-6EWRLB434Y)  
**Form Submissions:** https://formspree.io (xojbkeeb)  
