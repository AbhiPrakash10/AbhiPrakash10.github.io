# 03 — Product Structure & User Experience Architecture

## Site Map

```
abhiprakash.com/
├── index.html (Homepage — single-page, all sections)
│   ├── #hero
│   ├── #story
│   ├── #ventures
│   ├── #thinking
│   ├── #speaking
│   └── #contact
│
├── intelligent-execution.html   (Article — White Paper)
├── lightside.html               (Article — Philosophy Essay)
├── athletic-edge.html           (Article — Sports & Leadership)
├── fusion-energy.html           (Article — Energy & Investing)
└── cloud-secret.html            (Article — Technology)
```

---

## Navigation Hierarchy

```
ABHI PRAKASH [logo/home]
├── Story          → #story
├── Ventures       → #ventures
├── Thinking       → #thinking
├── Speaking       → #speaking
└── Connect [CTA]  → #contact
```

**Mobile:** Desktop links collapse into hamburger menu → slide-down drawer with same links.

**Article pages:** Nav links scroll to homepage sections (smooth scroll with anchor offset). "Back to Thinking" link returns to #thinking.

---

## Homepage Section Breakdown

### 1. Hero
**Business purpose:** Immediate brand positioning. A visitor who bounces here should leave knowing exactly who Abhi is and what he does.

| Element | Content | Purpose |
|---------|---------|---------|
| Eyebrow | Los Angeles · Phoenix · Sacramento | Geographic presence signals |
| Headline | "Building enduring systems across technology, finance, and education." | Value proposition |
| Descriptor | Operator · Investor · Educator · Builder | Role clarity |
| CTA Primary | Explore Ventures → #ventures | Drive to commercial proof |
| CTA Secondary | Read the Story → #story | Drive to personal connection |
| Scroll indicator | Animated line + "SCROLL" | Encourages continued engagement |

---

### 2. Manifesto Band
**Business purpose:** Reinforces the brand philosophy in a single memorable line. Creates visual rhythm between Hero and Story.

> "Build with disciplined execution."

---

### 3. Story
**Business purpose:** Builds personal trust and emotional connection. This is the "why I should care about this person" section.

| Element | Purpose |
|---------|---------|
| Professional photo | Humanizes, builds trust |
| Handwritten signature PNG | Premium personal brand signal |
| "Disciplined. Ambitious. Long-term." | Immediate character positioning |
| 4 bio paragraphs | Full background — education, career, philosophy |
| Great Vibes cursive signature | Authenticity, craft |
| Stats (6 ventures, 3 degrees, 1 state title, 5+ industries) | Social proof in numbers |

---

### 4. Ventures
**Business purpose:** Commercial credibility. Shows Abhi builds real things, not just talks about them.

| Venture | Category | Link Type | Signal |
|---------|---------|-----------|--------|
| Lightbear.AI | Technology & AI | External visit | AI infrastructure company |
| Lightside Ventures | Venture Capital | External visit | Active fund |
| Aer West | Real Estate | Inquire (contact) | Investment arm |
| Peak Basketball | Sports & Education | Connect (contact) | Community/impact |
| Asearis Data Systems | Data & Technology | External visit | Data infrastructure company |
| RightsOS | Sports, Media & Entertainment | External visit | Partnership platform |

**Hover behavior:** Cardinal red line animates across the top of each row. Name brightens to white. Arrow shifts right on the Visit/Inquire link.

---

### 5. Thinking
**Business purpose:** Intellectual authority. Long-form writing is the highest-leverage brand asset — it compounds over time through search and sharing.

**Featured Article:** Always shows the most important/recent white paper at full width.

**Article Grid (3-column):**

| Article | Category | Status |
|---------|---------|--------|
| Ideas Matter. Operators Win. | Leadership | Coming Soon (dimmed) |
| What the Lightside Is. | Philosophy | Read Now |
| The Athletic Edge in Business. | Sports & Leadership | Read Now |
| Nuclear Fusion: The New Energy Frontier. | Energy & Investing | Read Now |
| The Cloud's Secret. | Technology & Infrastructure | Read Now |
| The Long Game. | Leadership & Strategy | Coming Soon (dimmed) |

**Coming Soon cards** are dimmed to 55% opacity and non-interactive, signaling work-in-progress without looking broken.

---

### 6. Speaking
**Business purpose:** Establishes Abhi as a recognized voice — someone worth inviting. Signals that others have already made the bet.

| Engagement | Organization | Year |
|-----------|-------------|------|
| UCLA Anderson Leadership Series | Anderson School of Management | 2026 |
| Peak Basketball Coaching Clinic | Peak Basketball | 2025 |
| Early-Stage Investing in the AI Era | Lightside Ventures | 2025 |
| Building AI Infrastructure for Operators | Lightbear.AI | 2025 |

**CTA:** "Interested in having Abhi speak at your event or join your panel? Get in Touch →"

---

### 7. Contact
**Business purpose:** Lead capture. Every qualified visitor who reaches this section should have a frictionless path to initiating a conversation.

**Left column:** Direct contact channels (Email, LinkedIn, Instagram, GitHub)  
**Right column:** Contact form with Name, Email, Message fields

**Form behavior:**
1. Client-side validation (required fields, email format)
2. Submit → Formspree API (`xojbkeeb`)
3. Success: "Message received. I'll be in touch."
4. Error: Inline error message
5. Honeypot field (`_gotcha`) blocks bots

---

## Article Page Structure

All 5 article pages share the same template:

```
[Reading Progress Bar — fixed red line, top of viewport]
[Nav — same as homepage]
[Article Hero — dark bg]
  ← Back to Thinking
  CATEGORY | READ TIME | DATE
  LARGE HEADLINE
  Subtitle / subheadline
[Author Block]
  [AP avatar] Abhi Prakash — Operator · Investor · Educator
[Prose Content — article-specific]
[Footer Band — "Written by Abhi Prakash"]
[Footer — same as homepage]
```

---

## User Flows

### Investor Flow
Homepage → Hero (positioning) → Ventures (Lightside Ventures link) → Thinking (white paper) → Contact (inquire)

### Recruiter Flow
Homepage → Hero → Story (full bio, stats) → Speaking (credibility) → Contact (connect)

### Founder / Operator Flow
Homepage → Hero → Ventures (Lightbear.AI or Asearis) → Thinking (Intelligent Execution article) → Contact

### Media / Speaking Flow
Homepage → Story (bio) → Speaking (track record) → Thinking (article depth) → Contact

---

## Conversion Funnel

```
100% — Landing (any page)
 70% — Scroll past Hero
 50% — Engage with Story or Ventures
 30% — Read a Thinking article
 15% — Reach Contact section
  5% — Submit contact form
```

*Estimates based on typical personal brand site benchmarks. Validate with GA4.*
