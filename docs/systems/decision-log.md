# Decision Log

**Purpose:** The append-only, ADR-style record of every foundational decision on this brand/website program — so no session re-litigates a settled choice and every standard traces to a documented rationale.
**Status:** v1 foundation — adjustable.

---

> **How this log works.** Each decision is one **ADR** (Architecture Decision Record): a numbered, dated, immutable entry. You never edit an accepted ADR's meaning — you supersede it with a new one. Retrieve the "why" behind any standard by searching this file for the ADR title.

---

## How to add an ADR

1. Copy the template below.
2. Give it the next number (`ADR-NNNN` — monotonic, never reused).
3. Fill Context → Decision → Consequences. Be concrete: numbers, thresholds, trade-offs.
4. Set `Status: Accepted` (or `Proposed` if pending sign-off).
5. If it replaces an earlier ADR, set the old one's status to `Superseded by ADR-NNNN` and add a note.
6. Link the ADR from the doc it governs.

### ADR template

```md
## ADR-NNNN — <short decision title>

- **Date:** YYYY-MM-DD
- **Status:** Proposed | Accepted | Superseded by ADR-XXXX | Deprecated
- **Owners:** <role/name or {{BRAND_NAME}} owner>
- **Relates to:** <doc paths / other ADRs>

**Context.** <The forces at play: problem, constraints, options considered, why now.>

**Decision.** <The choice, stated as a rule. Include the specific values/thresholds.>

**Consequences.** <What becomes easier, what becomes harder, follow-up work, risks accepted.>
```

**Status legend:** `Proposed` = drafted, not ratified · `Accepted` = in force · `Superseded` = replaced, kept for history · `Deprecated` = withdrawn, not replaced.

---

## Index

| ADR | Decision | Status |
| --- | --- | --- |
| [0001](#adr-0001--brand-colour-palette-indigo--teal-contrast-validated) | Brand palette: indigo + teal, contrast-validated | Accepted |
| [0002](#adr-0002--typography-sora-display--inter-body--jetbrains-mono) | Typography: Sora + Inter + JetBrains Mono | Accepted |
| [0003](#adr-0003--spacing--type-scale-4px-base--modular-scale) | 4px spacing base + modular type scale (fluid clamp) | Accepted |
| [0004](#adr-0004--accessibility-target-wcag-22-level-aa-aaa-text-where-feasible) | Accessibility target: WCAG 2.2 AA | Accepted |
| [0005](#adr-0005--core-web-vitals--front-end-performance-budgets) | Core Web Vitals + performance budgets | Accepted |
| [0006](#adr-0006--image-strategy-avif-primary--webp-fallback-responsive) | Image strategy: AVIF + WebP fallback, responsive | Accepted |
| [0007](#adr-0007--rendering-static-site-generation-astro-or-nextstatic) | Rendering: static-first (Astro or Next static export) | Accepted |
| [0008](#adr-0008--structured-data-schemaorg-types-selected) | Structured data: schema.org types selected | Accepted |
| [0009](#adr-0009--adopt-llmstxt-for-ai-crawlers) | Adopt `llms.txt` for AI crawlers | Accepted |
| [0010](#adr-0010--tokens-as-single-source-of-truth-dtcg-json) | Design tokens as single source of truth (DTCG JSON) | Accepted |

---

## ADR-0001 — Brand colour palette: indigo + teal, contrast-validated

- **Date:** 2026-07-01
- **Status:** Accepted
- **Owners:** {{BRAND_NAME}} owner / design system
- **Relates to:** [`../brand/color-system.md`](../brand/color-system.md), [`../accessibility/contrast-matrix.md`](../accessibility/contrast-matrix.md), [`../../tokens/design-tokens.json`](../../tokens/design-tokens.json)

**Context.** The brand is "modern-tech with warmth; premium-but-approachable; calm confidence" for SMB service-industry buyers. We needed a primary that reads trustworthy/competent, a supporting accent with energy (speed), and a neutral ramp — all provably accessible, since a11y is a default (ADR-0004) and a slow/broken-contrast site would contradict the pitch.

**Decision.** Primary = **brand indigo 600 `#4F46E5`** (white text 6.29:1 AA; hover 700 `#4338CA` 7.90:1 AAA). Accent = **teal 500 `#06B6D4`, INK text only** (7.76:1); **never white on teal 500** (2.43:1 FAILS) — use teal 700 `#0E7490` for white-text teal. Neutrals: ink `#0B1120` text, 700 body, 600 secondary, 500 min muted / min interactive border, 400 disabled/hint only, 200/300 decorative dividers only. Semantic: success `#16A34A` (white large/UI; success-strong `#15803D` for normal white text), warning `#D97706` (INK text), danger `#DC2626` (white AA), info `#2563EB`. Every pairing is WCAG-validated and recorded in the contrast matrix.

**Consequences.** Colour is safe-by-default when consumed via ROLE tokens; designers can't accidentally ship a failing pairing if they follow the doc. Cost: teal is constrained (INK-only at 500), so CTAs default to indigo. Any value change requires re-running `scripts/verify-contrast.py`, updating the matrix, and a token version bump (ADR-0010).

---

## ADR-0002 — Typography: Sora (display) + Inter (body) + JetBrains Mono

- **Date:** 2026-07-01
- **Status:** Accepted
- **Owners:** {{BRAND_NAME}} owner / design system
- **Relates to:** [`../brand/typography.md`](../brand/typography.md), [`../../tokens/design-tokens.json`](../../tokens/design-tokens.json)

**Context.** We needed a heading face that feels geometric/modern-tech with warmth and a body face optimized for legibility across long-form and UI, both variable (for weight range + subsetting/perf), with an optional mono for technical accents. Fonts must support `font-display: swap`, preloading, and subsetting to hit the performance budget (ADR-0005).

**Decision.** Display/headings = **Sora** (variable). Body/UI = **Inter** (variable). Mono/technical = **JetBrains Mono** (optional). Base size 16px; body line-height ≥ 1.5; prose measure 68ch. Ship subset + `font-display: swap`; preload the critical (LCP) font. Fallback stacks are defined in tokens (`Sora Fallback` / `Inter Fallback` → system-ui) to minimize CLS.

**Consequences.** Two variable families cover the full weight range with few files. Clear display/body split reinforces hierarchy. Cost: two families to subset and self-host; discipline required to keep fallback metrics tuned so font-swap doesn't shift layout (CLS ≤ 0.1, ADR-0005).

---

## ADR-0003 — Spacing + type scale: 4px base + modular scale (fluid clamp)

- **Date:** 2026-07-01
- **Status:** Accepted
- **Owners:** {{BRAND_NAME}} owner / design system
- **Relates to:** [`../design-system/layout-and-grid.md`](../design-system/layout-and-grid.md), [`../design-system/design-tokens.md`](../design-system/design-tokens.md), [`../../tokens/design-tokens.json`](../../tokens/design-tokens.json)

**Context.** Generous whitespace and rhythmic hierarchy are core to the "premium-but-approachable" direction. We needed a spacing system that composes predictably and a type scale that reads as a deliberate hierarchy while staying fluid across breakpoints.

**Decision.** **Spacing: 4px base unit**, all spacing tokens are multiples (`--space-1`=4px …). **Type: a modular scale** with **fluid `clamp()` for h1–h3** so large headings shrink gracefully on small viewports without media-query churn. Radii: sm 6 / md 8 / lg 12 / xl 16 / 2xl 24 / full. Breakpoints: sm 640 / md 768 / lg 1024 / xl 1280 / 2xl 1536. Content max-width 1200px. Touch target 44px (WCAG min 24px) with ≥ 8px spacing.

**Consequences.** Spacing and sizing are token-driven and consistent; fluid headings remove a class of responsive bugs. Cost: authors must use spacing tokens, not arbitrary px; `clamp()` bounds must be chosen so text never drops below legible/contrast-safe sizes.

---

## ADR-0004 — Accessibility target: WCAG 2.2 Level AA (AAA text where feasible)

- **Date:** 2026-07-01
- **Status:** Accepted
- **Owners:** {{BRAND_NAME}} owner / accessibility
- **Relates to:** [`../accessibility/accessibility-standards.md`](../accessibility/accessibility-standards.md), [`../accessibility/contrast-matrix.md`](../accessibility/contrast-matrix.md), [`../00-foundations/principles.md`](../00-foundations/principles.md)

**Context.** Audience includes clinics, med spas, and dental/real-estate SMBs where accessibility is both an ethical baseline and a legal risk area. "Accessible by default" is a stated principle. We needed a concrete, checkable bar.

**Decision.** Target **WCAG 2.2 Level AA** across all pages, and **AAA text contrast where feasible** (our neutral ramp already delivers AAA for body/headings). Concretely: text contrast ≥ 4.5:1 (large ≥ 3:1), non-text/UI ≥ 3:1, visible focus states, full keyboard operability, correct semantics/ARIA, target size 44px, and gate non-essential motion behind `prefers-reduced-motion`.

**Consequences.** Every colour pairing is pre-validated (ADR-0001) and every interactive control has a defined focus/hit-target spec. Cost: constrains colour/spacing/motion choices; each page requires an a11y pass before publish (see content workflow).

---

## ADR-0005 — Core Web Vitals + front-end performance budgets

- **Date:** 2026-07-01
- **Status:** Accepted
- **Owners:** {{BRAND_NAME}} owner / performance
- **Relates to:** [`../performance/performance-budget.md`](../performance/performance-budget.md), [`../performance/asset-efficiency.md`](../performance/asset-efficiency.md), [`../00-foundations/principles.md`](../00-foundations/principles.md)

**Context.** The product promise is speed-to-lead; a slow site directly contradicts the pitch. We needed field-measurable targets and hard budgets, not aspirations.

**Decision.** Field CWV targets: **LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1**; **TTFB ≤ 0.8s**; **Lighthouse ≥ 95**. Budgets: **initial JS < 150 KB gz**, **hero/LCP image < 150 KB**, **total initial transfer < 1 MB**. `fetchpriority="high"` on the LCP image; preload critical fonts; lazy-load below the fold.

**Consequences.** Forces static-first rendering (ADR-0007), aggressive image optimization (ADR-0006), and font subsetting (ADR-0002). Cost: every page needs a perf pass against the budget; rich/interactive features must justify their bytes.

---

## ADR-0006 — Image strategy: AVIF primary + WebP fallback, responsive

- **Date:** 2026-07-01
- **Status:** Accepted
- **Owners:** {{BRAND_NAME}} owner / performance
- **Relates to:** [`../performance/image-optimization.md`](../performance/image-optimization.md), [`../performance/performance-budget.md`](../performance/performance-budget.md)

**Context.** Images are the usual LCP element and the biggest byte risk against the < 1 MB / < 150 KB LCP budgets (ADR-0005). We needed a format + delivery policy that maximizes compression without dropping support.

**Decision.** Serve **AVIF as primary** with **WebP fallback** (via `<picture>`), responsive `srcset`/`sizes`, **explicit `width`/`height`** on every image (no CLS), **lazy-load below the fold**, and **`fetchpriority="high"`** on the LCP image. Icons/logo are optimized SVG. Fonts are subset with `font-display: swap` and critical fonts preloaded.

**Consequences.** Meets LCP/CLS budgets with minimal bytes. Cost: build pipeline must emit AVIF+WebP variants and correct dimensions; authors must set `sizes` accurately or lose the srcset benefit.

---

## ADR-0007 — Rendering: static site generation (Astro or Next/static)

- **Date:** 2026-07-01
- **Status:** Accepted
- **Owners:** {{BRAND_NAME}} owner / engineering
- **Relates to:** [`../performance/performance-budget.md`](../performance/performance-budget.md), [`../seo/technical-seo.md`](../seo/technical-seo.md)

**Context.** This is a marketing/agency site: mostly content pages, few dynamic surfaces, hard performance + SEO targets (ADR-0005, ADR-0008). SSR/CSR frameworks add JS and TTFB risk we don't need. Note: this is a **recommendation** for whoever implements the build.

**Decision.** Render **static-first**: prebuilt HTML with minimal/zero client JS by default. Recommended stack: **Astro** (islands for the rare interactive component) or **Next.js in static-export mode**. Ship JS only where it earns its place (ADR-0005 budget). Any dynamic behaviour (form submit, chat widget) is progressively enhanced.

**Consequences.** Best-in-class TTFB/LCP, trivial CDN hosting, strong crawlability. Cost: dynamic features need an explicit island/endpoint decision; framework choice is deferred to implementation but must respect the JS budget regardless.

---

## ADR-0008 — Structured data: schema.org types selected

- **Date:** 2026-07-01
- **Status:** Accepted
- **Owners:** {{BRAND_NAME}} owner / SEO
- **Relates to:** [`../seo/structured-data.md`](../seo/structured-data.md), [`../../schema/README.md`](../../schema/README.md), [`../../schema/`](../../schema/)

**Context.** We need machine-readable entity data for rich results and for AI answer engines (E-E-A-T, entity clarity, consistent NAP). We had to pin the exact schema.org types up front so templates and NAP stay consistent everywhere.

**Decision.** Adopt these JSON-LD types, templated in `schema/`: **Organization**, **LocalBusiness** (`ProfessionalService`), **Service** (with `OfferCatalog`/`Offer`), **FAQPage**, **Review**/`AggregateRating`, **BreadcrumbList**, and **WebSite** (with `SearchAction`). All use `{{...}}` placeholders and must keep NAP identical to `llms.txt` and site footer.

**Consequences.** Consistent, reusable structured data across pages; eligible for FAQ/breadcrumb/review rich results. Cost: every page picks the right subset and keeps placeholders/NAP in sync; invalid JSON-LD must be validated before publish.

---

## ADR-0009 — Adopt `llms.txt` for AI crawlers

- **Date:** 2026-07-01
- **Status:** Accepted
- **Owners:** {{BRAND_NAME}} owner / SEO
- **Relates to:** [`../seo/ai-seo-geo.md`](../seo/ai-seo-geo.md), [`../../public-templates/llms.txt`](../../public-templates/llms.txt)

**Context.** Buyers increasingly discover services through AI answer engines. We want a concise, authoritative, extractable entity summary at a predictable path — without over-claiming benefits (llms.txt does not "multiply" citations; it's a clarity/convenience signal).

**Decision.** Publish **`llms.txt` at the site root** (`{{DOMAIN}}/llms.txt`) with a concise business summary, key pages, and consistent NAP matching the JSON-LD (ADR-0008). Pair it with extractable on-page answers, FAQ schema, and cited stats. Treat it as a supplement to — not a replacement for — solid technical SEO.

**Consequences.** Cleaner entity representation for AI crawlers with low maintenance cost. Cost: must be kept in sync with structured data and site copy; no reliance on it as a ranking silver bullet.

---

## ADR-0010 — Tokens as single source of truth (DTCG JSON)

- **Date:** 2026-07-01
- **Status:** Accepted
- **Owners:** {{BRAND_NAME}} owner / design system
- **Relates to:** [`memory-system.md`](./memory-system.md), [`../design-system/design-tokens.md`](../design-system/design-tokens.md), [`../../tokens/design-tokens.json`](../../tokens/design-tokens.json)

**Context.** Values duplicated across docs and code drift. We needed one authoritative store that both humans and code consume, so a colour/spacing/type change propagates by reference and stays contrast-safe.

**Decision.** `tokens/design-tokens.json` (W3C DTCG format, semver in `$meta.version`) is the **single source of truth** for all design values. It is exposed to code as `tokens/tokens.css` (CSS custom properties) and `tokens/tailwind.tokens.js`. **Docs and product code reference tokens by name** (`--color-brand-600`, `--space-4`) — raw hex only in the canonical colour/contrast docs. Any value change bumps the version and re-runs `scripts/verify-contrast.py`.

**Consequences.** Zero-drift design values; changes are auditable and versioned. Cost: contributors must consume tokens rather than hardcode, and value changes carry a versioning + re-validation ritual.

---

## Related

- [`memory-system.md`](./memory-system.md) — how to retrieve/update memory (this log is the "why" store).
- [`content-workflow.md`](./content-workflow.md) — where these decisions get applied per page.
- [`../00-foundations/principles.md`](../00-foundations/principles.md) — the principles these decisions operationalize.
- [`../../tokens/design-tokens.json`](../../tokens/design-tokens.json) — the values ADR-0001/0002/0003/0010 govern.
- [`../accessibility/contrast-matrix.md`](../accessibility/contrast-matrix.md) — evidence for ADR-0001/0004.
