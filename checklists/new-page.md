# New Page Checklist

**Purpose:** The per-page build gate for {{BRAND_NAME}} — one checklist that ties design tokens, SEO, accessibility, performance, and schema together so every new page (service, industry, location, pricing, contact, landing) ships correct and consistent, not just "done."
**Status:** v1 foundation — adjustable.

---

> **How to use:** Run this for each new page **before** it merges. It assumes the foundations (tokens, components, head-meta template) already exist — you are applying them, not reinventing them. Build and check the **mobile** rendering first. Location/industry pages MUST be genuinely differentiated (real local proof), not city-swapped clones.

## 1. Structure & semantics (design tokens + a11y)

- [ ] Page uses the standard layout: `header` > `main` > `footer`, content within `--container-content` (1200px), gutters via `--container-gutter`.
- [ ] Exactly **one `<h1>`** stating the page's core topic; `h2`/`h3` form a logical hierarchy with no skipped levels.
- [ ] All colors, spacing, radii, type come from **tokens** (`--color-*`, `--space-*`, `--radius-*`, font families Sora/Inter) — no raw hex or magic numbers. See [`../docs/design-system/design-tokens.md`](../docs/design-system/design-tokens.md).
- [ ] Reused components come from [`../docs/design-system/components.md`](../docs/design-system/components.md); no one-off restyled buttons/cards.
- [ ] Prose blocks constrained to `--container-prose` (68ch); body line-height `>= 1.5`.
- [ ] Landmarks and a working "skip to content" link present; reading/`tab` order is logical.

## 2. Content & voice

- [ ] Copy matches brand voice: clear, direct, benefit-led, second person, short sentences, confidence without hype. See [`../docs/00-foundations/brand-strategy.md`](../docs/00-foundations/brand-strategy.md).
- [ ] Primary CTA is obvious above the fold (book a call / start) and repeated logically; secondary CTA does not compete.
- [ ] One primary topic per page; no thin/duplicate content. Location/industry pages include **real local/vertical proof** (reviews, specifics, service-area detail) — not a city find-replace.
- [ ] NAP (if shown) is plain crawlable text and **identical** to site/schema/GBP.

## 3. SEO — on-page (P0)

See [`../docs/seo/onsite-seo.md`](../docs/seo/onsite-seo.md). Use [`../public-templates/head-meta.html`](../public-templates/head-meta.html) as the `<head>` base.

- [ ] `<title>` unique, **<= ~60 chars**, primary keyword in first ~30 chars, includes {{BRAND_NAME}}.
- [ ] Meta description unique, **<= ~155 chars**, accurate and compelling.
- [ ] Self-referencing `rel=canonical` (absolute https), placed early in `<head>`; not conflicting with sitemap.
- [ ] Robots meta correct: `index,follow` for public pages; `noindex,follow` (on a **crawlable** page) for thank-you/utility pages.
- [ ] Clean, lowercase, keyword-relevant, stable URL slug; no tracking params in the canonical.
- [ ] Descriptive internal links in + out (2–5 contextual links/1,000 words); no orphan; added to nav/related where relevant.
- [ ] Added to `sitemap.xml` (or auto-picked up); slug reflected in breadcrumb.

## 4. Social / share metadata

- [ ] OG `type/title/description/url/image` set; Twitter `summary_large_image`; image **1200×630**, absolute URL, with `og:image:alt`.
- [ ] Share preview visually checked (LinkedIn/Slack/X) — no truncation or missing image.

## 5. Structured data (P0 where applicable)

See [`../docs/seo/structured-data.md`](../docs/seo/structured-data.md) and [`../schema/README.md`](../schema/README.md).

- [ ] Correct schema for the page type:
  - Service page → `Service` ([`../schema/service.jsonld`](../schema/service.jsonld))
  - Location page → `LocalBusiness` (specific subtype) ([`../schema/localbusiness.jsonld`](../schema/localbusiness.jsonld))
  - Any nested page → `BreadcrumbList` ([`../schema/breadcrumb.jsonld`](../schema/breadcrumb.jsonld))
  - Visible FAQ → `FAQPage` ([`../schema/faqpage.jsonld`](../schema/faqpage.jsonld))
- [ ] JSON-LD validates with **0 errors** (Rich Results Test + Schema.org validator); reflects only content actually on the page.

## 6. Accessibility (P0)

See [`../docs/accessibility/accessibility-standards.md`](../docs/accessibility/accessibility-standards.md).

- [ ] axe scan: **0 critical/serious**.
- [ ] Contrast >= 4.5:1 text / 3:1 large & UI, checked against [`../docs/accessibility/contrast-matrix.md`](../docs/accessibility/contrast-matrix.md); meaning never conveyed by color alone.
- [ ] Keyboard-only pass: everything reachable/operable, visible focus, no trap, focus not obscured by sticky/chat elements.
- [ ] All images have correct `alt` (decorative = `alt=""`); icon-only controls have accessible names.
- [ ] Form fields (if any) have real `<label>`s, associated error messaging, and don't block paste on sensitive fields.
- [ ] Interactive targets **>= 24×24 CSS px** (target 44×44) with `>= 8px` spacing; any animation respects `prefers-reduced-motion`.

## 7. Performance (P0)

See [`../docs/performance/performance-budget.md`](../docs/performance/performance-budget.md).

- [ ] LCP element identified; hero image `fetchpriority="high"`, correct `srcset`/`sizes`, **never** lazy-loaded; preloaded if needed.
- [ ] Every image/embed has explicit `width`/`height` or `aspect-ratio` (zero CLS); below-fold images `loading="lazy"`.
- [ ] Images shipped AVIF + WebP; each within budget (hero < 150 KB, content < 100 KB).
- [ ] No new render-blocking or heavy third-party JS; page-specific JS deferred; page stays within the site JS budget (< 150 KB gz initial).
- [ ] Lighthouse (mobile) on this page: **Performance & Accessibility >= 95, SEO >= 95, Best Practices >= 95**.

## 8. Final verification

- [ ] Renders correctly at 320 / 768 / 1024 / 1280 px; no horizontal scroll; mobile HTML contains full content + headings + schema.
- [ ] All links resolve (200), no console errors, forms/CTAs tested end-to-end.
- [ ] Cross-checked against [`quality-gates.md`](./quality-gates.md) definition-of-done before merge.

---

## Related

- [`pre-launch.md`](./pre-launch.md)
- [`content-publish.md`](./content-publish.md)
- [`quality-gates.md`](./quality-gates.md)
- [`../docs/design-system/design-tokens.md`](../docs/design-system/design-tokens.md)
- [`../docs/design-system/components.md`](../docs/design-system/components.md)
- [`../docs/seo/onsite-seo.md`](../docs/seo/onsite-seo.md)
- [`../docs/seo/structured-data.md`](../docs/seo/structured-data.md)
- [`../public-templates/head-meta.html`](../public-templates/head-meta.html)
