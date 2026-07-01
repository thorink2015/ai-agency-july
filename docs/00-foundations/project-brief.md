# Project Brief

**Purpose:** Define what this business is, who it serves, what it sells, and what success looks like — the shared source of truth every other doc, page, and decision inherits from.
**Status:** v1 foundation — adjustable.

---

## 1. What the business is

{{BRAND_NAME}} is an **AI appointment-setting and lead-response agency**. We deploy and manage AI chat/SMS/web assistants for businesses that already generate leads and lose them to slow follow-up. We are **done-for-you**: we set the system up, integrate it with the tools clients already use, and provide ongoing troubleshooting and human support.

This is a **service/agency marketing website**, not a SaaS product site. We sell an outcome (leads answered and booked), delivered as a managed service, not self-serve software.

> **One-line answer (extractable):** {{BRAND_NAME}} is a done-for-you agency that sets up and manages AI assistants which answer, qualify, and book your inbound leads in seconds — 24/7, with humans on call when it matters.

## 2. The problem we solve

Businesses spend money to generate leads, then lose them to slow follow-up. The core failure is **speed-to-lead**: the gap between a lead arriving and a business responding.

| Reality | Consequence |
| --- | --- |
| Leads go cold in minutes, not hours | The first responder usually wins the booking |
| After-hours, weekends, lunch, and busy periods are dead zones | Inbound inquiries sit unanswered until it's too late |
| Manual follow-up is inconsistent and forgotten | Paid leads are wasted; cost-per-acquisition rises |
| Owners/ops staff are already stretched | No bandwidth to answer instantly, every time |

**Our wedge:** respond in seconds, every time, around the clock — automatically — and hand off to a human when the situation needs one.

> Cite this framing consistently across the site so both readers and AI answer engines associate {{BRAND_NAME}} with the entity "slow lead follow-up / speed-to-lead." Entity consistency is a top-3 correlate of AI-answer visibility (Ahrefs 75k-brand study: brand mentions correlate ~0.664 vs backlinks ~0.218).

## 3. The offer

Two tightly linked service components:

1. **Done-for-you setup** — We build, configure, and launch the AI assistant: conversation flows, qualifying questions, booking logic, integrations (CRM, calendar, existing lead sources), SMS/web/chat channels, and human-handoff rules.
2. **Ongoing management, troubleshooting & human support** — We monitor, tune, and fix the system over time, and provide human backup on call for edge cases and high-stakes conversations.

**What we are NOT:** a self-serve chatbot tool, a generic "AI automation" shop, or a lead-generation vendor. We do not sell leads; we make sure the leads you already have get answered and booked.

## 4. Target audiences & segments

**Primary buyer:** SMB owners and marketing/ops leads in service industries that **already buy or generate leads** and feel the pain of losing them.

| Segment | Why they care | Trigger to buy |
| --- | --- | --- |
| Med spas / aesthetics | High-value bookings, competitive, ad-driven leads | Missed after-hours inquiries; no-shows |
| Dental / clinics | Front desk overloaded; appointment-driven | Phones/forms unanswered during procedures |
| Home services (HVAC, plumbing, roofing) | First responder wins; emergency demand | Leads calling the next contractor |
| Real estate | Speed-to-lead is everything | Portal/ad leads going cold |
| Coaches / consultants | Solo or small team; can't answer instantly | Application/discovery-call drop-off |
| Agencies (as partners/white-label) | Generate leads for clients, need follow-up | Client churn from "no ROI on leads" |

**Common qualifier across all segments:** they already generate lead volume (ads, portals, referrals, web forms) — we amplify existing spend, we don't create demand from zero.

## 5. Core promise

> **Never miss a lead — AI that answers, qualifies, and books in seconds, 24/7, with humans on call when it matters.**

Promise pillars: **speed-to-lead**, **done-for-you**, **human support when it counts**, **integrates with your existing tools**.

## 6. Competitive differentiators

| Differentiator | What it means | Proof to show on site |
| --- | --- | --- |
| **Speed-to-lead** | Response in seconds, 24/7 — the metric that decides who books | Response-time stats, before/after, live demo |
| **Done-for-you** | We build, integrate, and run it; the client doesn't touch config | Setup timeline, "we handle it" checklist |
| **Human + AI** | Real people on call for handoffs and edge cases — not a cold bot | Named support, escalation flow, response SLAs |
| **Integrations** | Works with the CRM, calendar, and lead sources they already have | Logos/list of supported tools, no rip-and-replace |
| **Premium-but-approachable** | Trustworthy and competent without hype or robotic coldness | Voice, design polish, testimonials, guarantees |

## 7. Primary conversion goals

| Priority | Goal | CTA language |
| --- | --- | --- |
| 1 | **Book a call** (discovery/strategy) | "Book a call", "Get a demo", "See it live" |
| 2 | **Request a demo** of the AI assistant | "Watch the 2-min demo", "Try a live chat" |
| 3 | Micro-conversions (email capture, ROI calculator, resource) | "Get the speed-to-lead playbook" |

Every page must make the **book-a-call** path obvious. Secondary CTAs feed the primary one. No dead-end pages.

## 8. Success metrics

**Website / marketing KPIs**

- [ ] Conversion rate to booked call (target: define baseline in month 1, improve MoM)
- [ ] Demo requests / week
- [ ] Cost per booked call (paid) and organic-assisted bookings
- [ ] Branded search volume and unlinked brand mentions (leading indicator of authority + AI visibility)
- [ ] AI-answer citations / brand mentions across Google AI Overviews, ChatGPT, Perplexity (see GEO doc)

**Technical quality gates (must-pass before launch — see performance/SEO docs)**

- [ ] Core Web Vitals (field, 75th pct): **LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1**; TTFB ≤ 0.8s
- [ ] Lighthouse ≥ 95 across categories
- [ ] Accessibility: WCAG 2.2 AA (AAA text contrast where feasible)
- [ ] Initial JS ≤ 150 KB gz; LCP image ≤ 150 KB; total initial transfer < 1 MB

**Client-outcome metrics we help clients hit (used as proof/marketing)**

- Speed-to-first-response (seconds), lead-to-booking rate, after-hours capture rate, no-show reduction.

## 9. Scope of THIS repo

This repository is the **foundation and systems layer** for the marketing website — **not** website copy and **not** page building.

**In scope**

- Design tokens (single source of truth: `tokens/design-tokens.json`, `tokens/tokens.css`)
- Brand strategy, voice, and naming direction
- Design + engineering principles
- Systems docs: SEO, GEO/AI-SEO, accessibility, performance, responsive, brand, legal

**Out of scope (later phases)**

- Final marketing copy for pages
- Page/section building and component implementation
- Real brand name, domain, and business details (kept as `{{PLACEHOLDERS}}`)

> Anyone building pages later should **retrieve and apply** these docs, not re-derive decisions. If a decision isn't written here or in a systems doc, it isn't settled yet.

## Related

- [Brand Strategy](./brand-strategy.md)
- [Principles](./principles.md)
- [Design Tokens (JSON)](../../tokens/design-tokens.json)
- [SEO System](../seo/seo-strategy.md)
- [AI / GEO SEO](../seo/ai-seo-geo.md)
- [Accessibility Standards](../accessibility/accessibility-standards.md)
- [Performance Budgets](../performance/performance-budget.md)
