# Dispatch — Copy Review Notes

**Purpose:** Record of the full-copy review (owner-requested second pass) so future sessions don't re-litigate settled lines. The page itself (`index.html`) is the copy source of truth.
**Status:** Reviewed 2026-07-02 · verdict: copy holds — no rewrites applied · 3 items flagged for owner decision.

---

## Review verdicts (section by section)

| Section | Verdict | Note |
| --- | --- | --- |
| Hero H1 + sub | **Keep** | Names the mechanism (answer first → win) + the promise; beats the "Never miss another lead" pattern common in the AI-receptionist space. Owner-approved. |
| Quick strip / guarantee | **Keep** | Guarantee is Hormozi-grade risk reversal, stated plainly. |
| What You Get | **Keep** | "nothing gets weird" is deliberate voice — humanizes; keep. |
| How It Works | **Keep** | Step 4's "do the work you're actually good at" is the emotional payoff — don't touch. |
| Why Speed Wins | **Keep** | Stats + cited sources; the "we didn't invent this" intro pre-empts skepticism. |
| Who We Help | **Keep** (see Flag 1) | Each line in the vertical's own language — strong. |
| Testimonials | **Keep** | Fictional but styled as real (badge removed, SVG logo lockups) per owner request 2026-07-02 — swap names/quotes/logos when real ones exist; the HTML comment marks them. |
| Pricing | **Keep** (see Flag 2) | "Plain plans, no lock-in" heading matches the compliance-honesty positioning. |
| Voice AI | **Keep** | Premium/custom framing as intended. |
| What We Don't Do | **Keep** | Credibility engine of the page. Bold leads now mirror the brief exactly. |
| FAQ (added 2026-07-02) | **Keep** | 8 objections in brand voice; JSON-LD mirrors visible text — keep in sync if edited. |
| Funnel microcopy | **Keep** (see Flag 3) | "Four quick questions. About thirty seconds." sets cost honestly. |
| Works With Your Stack (added 2026-07-02) | **Fixed 2026-07-02** | Owner's external copy review flagged unconfirmed integration claims. Now confirmed-only: GoHighLevel (native), SMS/A2P, WhatsApp Business, Instagram DMs, Facebook Messenger, website forms, webhooks & API. Google Calendar/Outlook/Calendly/HubSpot/Zapier/Facebook Lead Ads removed until each is actually tested — re-add individually as they're confirmed. |

## Flags for the owner (decisions, not defects)

1. **Pay-per-show wording vs flat pricing.** Med Spa ("…or you don't pay") and Auto Detailing ("You only pay when the customer shows") promise performance-based pricing, but the pricing section is flat monthly. If those verticals really get per-show deals, keep; otherwise align to the 30-day guarantee wording to avoid a "wait, which is it?" moment at the pricing table.
2. **Implied setup fee.** "Setup waived your first month" implies a setup fee that is never stated anywhere. State the number (e.g. in the FAQ) or drop the implication — unstated fees read as a dark pattern to careful buyers.
3. **Contact capture.** The funnel collects 4 answers but no name/email/phone; the confirmation says "Check your email for details." Fine for the preview — the production calendar embed (Calendly/GHL/etc.) collects contact info at booking. Revisit when wiring the real calendar.

## Changes applied

**Pass 3 (2026-07-02, owner's external copy review — claims must match confirmed reality):**
- Integrations section rewritten to confirmed-only stack (see table); lede now leads with "natively on GoHighLevel"; note line: "We'll confirm before you pay, not after."
- Pricing flag "Most chosen" → "Recommended" (no customer data exists yet — opinion, not fabricated behavior).
- FAQ Q2 answer aligned with the integrations fix ("Not usually. We run on GoHighLevel natively…"), JSON-LD kept in sync.
- "see Section 8" in the Voice AI add-on now links to the Voice section (kept the words, made them functional).
- Chip labeled "WhatsApp Business" (not "WhatsApp") so it can't be misread against the "No personal WhatsApp" rule.

**Pass 2 (2026-07-02, owner request):**
- Working brand name: **Dispatch** (logomark: lime tile + » chevrons, header/footer/favicon; © Dispatch). ⚠ Verify domain + trademark before launch — one find-and-replace swaps it. Foundation docs keep `{{BRAND_NAME}}` until the name is final.
- Testimonials styled as real: placeholder badge removed, six per-company SVG logo lockups added (still fictional — see table note).
- New "Works with your stack" integrations section (eyebrow 03; later sections renumbered 04–10).

**Pass 1:**
- Desktop nav: added Voice AI (was mobile-only — inconsistent).
- Header breakpoint 960 → 1100px (6 links wrapped to two lines at 960–1024; burger now covers that range).

**Pass 4 (2026-07-02, owner-provided legal content):**
- privacy.html + terms.html filled with the owner's Privacy Policy (12 sections) and Terms of Service (14 sections), word-for-word, in the Dispatch document style (numbered sections, table of contents, 72ch measure).
- Fill-in tokens `[EFFECTIVE DATE]`, `[LEGAL ENTITY NAME]`, `[STATE OF INCORPORATION]`, `[CONTACT EMAIL]`, `[BUSINESS ADDRESS]` styled as visible dashed-accent chips so they can't be missed before publishing.
- `[BUSINESS ADDRESS]` was in the owner's fill-in list but appeared nowhere in the provided text — added as a "Mailing address:" line in both Contact sections (disclosed to owner).
- Main-page FAQ Q8: "Details will live in the Privacy Policy." → "Details live in the Privacy Policy." (now true), linked; JSON-LD synced.
- ⚠ Owner's own note, preserved here: this legal copy follows standard SMB SaaS/agency structure but needs a real lawyer review before launch — especially SMS/A2P wording (regulatory risk) and health-adjacent conversations (med spas, chiropractors).

**Pass 5 (2026-07-02, launch prep for instant33.com):**
- Domain purchased: **instant33.com** (on Cloudflare). Deploy root = `designs/01-dispatch/` via Cloudflare Pages (owner connects GitHub in dashboard — cannot be done headlessly).
- Added production files to the deploy root: robots.txt, sitemap.xml (3 URLs), llms.txt, 404.html (noindex), `_headers` (security headers), `_redirects` (www → apex 301), og-image.png (1200×630, real brand fonts embedded at render).
- index.html: canonical + Open Graph + Twitter-card tags for https://instant33.com/; privacy/terms: canonical tags.
- ⚠ Open question: site brand says **Dispatch**, domain says **instant33.com** — owner to decide whether to rebrand the page to Instant33 (one find-and-replace + new mark) or keep Dispatch-on-instant33.

## Deferred by owner decision

- Live AI chat demo widget (test-drive the agent on-page) — deliberately later; no placeholder.
- Real testimonials + logos, real brand name, demo video.
