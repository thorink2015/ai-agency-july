# Content Workflow

**Purpose:** The single, repeatable pipeline for producing a new page or section on this foundation — brief → copy → tokens/components → SEO + schema → a11y → perf → QA → publish — so every page ships on-brand, accessible, fast, and findable.
**Status:** v1 foundation — adjustable.

---

> **Use this for every new page or major section.** It sequences the foundation docs into an order of operations and gates each stage on a checklist. Don't skip stages; each one catches a class of defect the next stage can't.

---

## 0. Pipeline at a glance

```text
1 BRIEF ─▶ 2 COPY ─▶ 3 BUILD ─▶ 4 SEO+SCHEMA ─▶ 5 A11Y ─▶ 6 PERF ─▶ 7 QA ─▶ 8 PUBLISH
 (define)  (write)  (tokens/    (meta, JSON-LD,   (WCAG   (CWV +   (final  (ship +
           on-voice  components)  llms.txt)         2.2 AA) budgets) gate)   verify)
```

Each stage has: **inputs** (what you read), **outputs** (what you produce), and a **gate** (the checklist that must pass to proceed). Checklists live in [`../../checklists/`](../../checklists/) — reference the named file per stage.

---

## 1. Brief — define the page

**Inputs:** [`../00-foundations/project-brief.md`](../00-foundations/project-brief.md), [`brand-strategy.md`](../00-foundations/brand-strategy.md), [`principles.md`](../00-foundations/principles.md).

**Produce a one-screen brief:**

| Field | Fill with |
| --- | --- |
| Page & URL | e.g. `/med-spa-lead-response` |
| Primary audience | which segment (med spa / dental / home services / real estate / coach / clinic / agency) |
| Job-to-be-done | the visitor's goal in their words |
| Primary conversion | book a demo / start setup / call {{PHONE}} |
| Core promise angle | how "never miss a lead… 24/7, humans on call" applies here |
| Primary keyword + intent | for title/H1/meta |
| Proof/E-E-A-T assets | stats (cited), testimonials, integrations |
| Schema type(s) | from ADR-0008 (Service, FAQPage, Breadcrumb, …) |
| Sections outline | H1 + section H2s in order |

**Gate:** brief answers all rows; conversion + primary keyword are unambiguous; single H1 defined.

---

## 2. Copy — write on-voice

**Inputs:** [`brand-guidelines.md`](../brand/brand-guidelines.md) (voice), [`principles.md`](../00-foundations/principles.md), the brief.

**Voice rules (non-negotiable):** clear, direct, benefit-led, jargon-light, reassuring; **second person**; short sentences; **confidence without hype**. Trustworthy/fast/competent/human+AI. NOT hypey, NOT cold-robotic.

**Do / Don't**

| Do | Don't |
| --- | --- |
| Lead with the visitor's outcome | Lead with our feature list |
| "You never lose a lead to slow follow-up." | "Revolutionary AI-powered synergy!" |
| Cite real, sourced stats | Invent numbers or over-claim |
| One idea per short paragraph | Wall-of-text; buried CTA |
| Use `{{BRAND_NAME}}`, `{{PHONE}}` etc. | Hardcode a real brand/contact value |

**Produce:** H1 (one), section headings (logical order, no skipped levels), body copy at prose measure ≤ 68ch, CTA labels, FAQ Q&A pairs (feed schema in stage 4), extractable one-sentence answers near the top of key sections (for AI/GEO).

**Gate:** voice check passes; exactly one H1; heading levels sequential; every claim sourced; CTA present above the fold.

---

## 3. Build — apply tokens & components

**Inputs:** [`../design-system/components.md`](../design-system/components.md), [`layout-and-grid.md`](../design-system/layout-and-grid.md), [`interactive-elements.md`](../design-system/interactive-elements.md), [`motion.md`](../design-system/motion.md), [`../responsive/responsive-standards.md`](../responsive/responsive-standards.md); values from [`../../tokens/`](../../tokens/).

**Rules:**
- [ ] Consume **tokens by name** (`--color-brand-600`, `--space-4`, radii, type scale). Never hardcode hex or arbitrary px (ADR-0010).
- [ ] Primary CTA = brand indigo 600, hover 700. Teal 500 = INK text only — never white on teal 500 (ADR-0001).
- [ ] Use existing components/patterns; extend the system rather than one-off styles.
- [ ] Layout on the grid; content max-width 1200px; generous whitespace; responsive across sm→2xl.
- [ ] Motion 100–500ms, `ease-standard`; gate non-essential motion behind `prefers-reduced-motion`.
- [ ] Interactive controls: 44px target, ≥ 8px spacing, visible focus, keyboard operable.
- [ ] Images: `<picture>` AVIF+WebP, `srcset`/`sizes`, explicit `width`/`height`, lazy below fold, `fetchpriority="high"` on LCP (ADR-0006).

**Gate:** no hardcoded values; renders correctly at all breakpoints; components reused; reduced-motion honored.

---

## 4. SEO meta + structured data

**Inputs:** [`../seo/onsite-seo.md`](../seo/onsite-seo.md), [`technical-seo.md`](../seo/technical-seo.md), [`structured-data.md`](../seo/structured-data.md), [`ai-seo-geo.md`](../seo/ai-seo-geo.md); templates in [`../../schema/`](../../schema/) and [`../../public-templates/`](../../public-templates/).

- [ ] **Title ≤ 60 chars**, includes primary keyword + brand.
- [ ] **Meta description ≤ 155 chars**, benefit-led, with the conversion.
- [ ] **Canonical** URL set; single H1 confirmed; semantic heading order.
- [ ] **Open Graph + Twitter** card tags (title, description, image with dimensions).
- [ ] **JSON-LD** from `schema/` for the page's types (ADR-0008): fill `{{...}}`, keep **NAP identical** to `llms.txt` and footer; validate the JSON-LD.
- [ ] **FAQ schema** from the stage-2 Q&A if the page has FAQs.
- [ ] Add/confirm the URL in [`../../public-templates/sitemap.xml`](../../public-templates/sitemap.xml); confirm not blocked by [`robots.txt`](../../public-templates/robots.txt); update [`llms.txt`](../../public-templates/llms.txt) if this page is key.
- [ ] Extractable concise answers present (GEO); cited stats; consistent entity naming.

**Gate:** titles/meta within limits; valid JSON-LD; NAP consistent; sitemap/canonical correct.

---

## 5. Accessibility pass

**Inputs:** [`../accessibility/accessibility-standards.md`](../accessibility/accessibility-standards.md), [`contrast-matrix.md`](../accessibility/contrast-matrix.md). **Gate checklist:** `checklists/a11y-checklist.md`.

Target **WCAG 2.2 Level AA** (AAA text where feasible — ADR-0004):
- [ ] Every text/UI pairing traces to a validated token combo (no ad-hoc colours).
- [ ] Keyboard: all interactive elements reachable and operable; logical focus order; visible focus.
- [ ] Semantics: landmarks, labelled controls/inputs, alt text on meaningful images (empty alt on decorative).
- [ ] Target size 44px, ≥ 8px spacing; hit areas not overlapping.
- [ ] `prefers-reduced-motion` respected; no motion-only information.
- [ ] Zoom to 200% without loss of content/function; no horizontal scroll at 320px.

**Gate:** a11y checklist fully passes; no known AA violation.

---

## 6. Performance pass

**Inputs:** [`../performance/performance-budget.md`](../performance/performance-budget.md), [`image-optimization.md`](../performance/image-optimization.md), [`asset-efficiency.md`](../performance/asset-efficiency.md). **Gate checklist:** `checklists/performance-checklist.md`.

Measure against ADR-0005 budgets:
- [ ] **LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1**, TTFB ≤ 0.8s, **Lighthouse ≥ 95**.
- [ ] **Initial JS < 150 KB gz**; **LCP image < 150 KB**; **total initial transfer < 1 MB**.
- [ ] LCP image has `fetchpriority="high"`; critical fonts preloaded; fonts subset + `font-display: swap`.
- [ ] All images explicit dimensions (no CLS); below-fold lazy-loaded; AVIF+WebP served.
- [ ] No unused JS/CSS shipped; static-first render preserved (ADR-0007).

**Gate:** all budgets met in a Lighthouse/field check; no CLS regressions.

---

## 7. QA — final gate

**Gate checklist:** `checklists/qa-checklist.md` (plus `checklists/launch-checklist.md` for a new site/section).

- [ ] Content proofed; no placeholder text left un-intended; `{{...}}` placeholders intentional and consistent.
- [ ] Links resolve; forms submit; CTA goes to the correct conversion.
- [ ] Cross-browser + real-device spot check; responsive sm→2xl.
- [ ] Stages 4–6 gates re-confirmed on the built page (not just in review).
- [ ] Analytics/consent, 404/redirects, and canonical verified.

**Gate:** QA checklist passes; owner sign-off.

---

## 8. Publish & verify

- [ ] Deploy (static build — ADR-0007).
- [ ] Post-deploy: confirm live URL, canonical, JSON-LD (rich-results test), sitemap ping, robots access.
- [ ] Run field/Lighthouse check on production; confirm CWV budgets hold live.
- [ ] If anything non-obvious was decided during the build, **log an ADR** in [`decision-log.md`](./decision-log.md).
- [ ] If a recurring problem surfaced, add a runbook to [`../troubleshooting/`](../troubleshooting/).

**Done when:** page is live, all gates hold in production, and memory (ADRs/troubleshooting) is updated.

---

## Stage → checklist map

| Stage | Gate checklist (`checklists/`) |
| --- | --- |
| 5 Accessibility | `a11y-checklist.md` |
| 6 Performance | `performance-checklist.md` |
| 4 SEO + schema | `seo-checklist.md` |
| 7 QA | `qa-checklist.md` |
| 8 Publish (new site) | `launch-checklist.md` |

> If a referenced checklist file does not yet exist in [`../../checklists/`](../../checklists/), create it from this stage's task list — then this workflow and the checklist stay in sync.

---

## Related

- [`memory-system.md`](./memory-system.md) — retrieve the docs this workflow references; update memory after publish.
- [`decision-log.md`](./decision-log.md) — the ADRs (0001–0010) each stage enforces.
- [`../00-foundations/project-brief.md`](../00-foundations/project-brief.md) — source for the stage-1 brief.
- [`../brand/brand-guidelines.md`](../brand/brand-guidelines.md) — voice rules for stage 2.
- [`../seo/onsite-seo.md`](../seo/onsite-seo.md) — meta + on-page rules for stage 4.
- [`../../checklists/`](../../checklists/) — the gate checklists per stage.
- [`../../schema/`](../../schema/) & [`../../public-templates/`](../../public-templates/) — JSON-LD, robots, sitemap, llms.txt.
