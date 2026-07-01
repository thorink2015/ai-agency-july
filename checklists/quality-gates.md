# Quality Gates (Definition of Done)

**Purpose:** The machine-checkable definition-of-done for {{BRAND_NAME}} — the CI/pre-merge gates (Lighthouse, axe, HTML validity, links, budgets, schema) with exact pass/fail thresholds, so "done" is objective and regressions fail the build instead of shipping.
**Status:** v1 foundation — adjustable.

---

> **How to use:** These are hard gates. A change is **not done** until every P0 gate passes on the affected pages. Wire them into CI so they run on every PR; where CI can't (field data, manual a11y), run them in the release check. Lab tools (Lighthouse/axe) gate the build; **field CWV (CrUX)** is monitored post-deploy on a ~28-day lag and cannot block a PR.

## Gate summary

| # | Gate | Threshold (fail below) | Tool | When | Level |
|---|---|---|---|---|---|
| 1 | Lighthouse Performance | **>= 95** | Lighthouse CI (mobile) | CI / PR | P0 |
| 2 | Lighthouse Accessibility | **>= 95** | Lighthouse CI | CI / PR | P0 |
| 3 | Lighthouse SEO | **>= 95** | Lighthouse CI | CI / PR | P0 |
| 4 | Lighthouse Best Practices | **>= 95** | Lighthouse CI | CI / PR | P0 |
| 5 | Accessibility violations | **0 critical / 0 serious** | axe-core | CI / PR | P0 |
| 6 | HTML validity | **0 errors** | Nu Html Checker (`vnu`) | CI / PR | P0 |
| 7 | Broken links | **0 broken (4xx/5xx)** internal | link checker | CI / PR | P0 |
| 8 | Performance budgets | **all budgets met** | Lighthouse CI `budget.json` / bundlesize | CI / PR | P0 |
| 9 | Structured data | **0 errors** | Rich Results Test / schema validator | CI or manual | P0 |
| 10 | Core Web Vitals (field) | **LCP<=2.5s · INP<=200ms · CLS<=0.1 @ p75** | CrUX / RUM | post-deploy | P0 (monitor) |

## 1–4. Lighthouse (lab) — all four categories **>= 95**

- [ ] Run against the **mobile** profile with throttling on every key template (home, service, industry, location, pricing, contact, blog post).
- [ ] Lighthouse Performance is weighted TBT 30% · LCP 25% · CLS 25% · FCP 10% · Speed Index 10%. Note: **Lighthouse cannot measure INP** — use TBT as the lab proxy and confirm real INP in the field (gate 10).
- [ ] Any category **< 95** fails the gate. Do not "score-chase" the lab while ignoring field data.

## 5. Accessibility — axe: 0 critical / 0 serious

- [ ] axe-core (CI) reports **0 critical and 0 serious** violations on every template. Automated tools catch ~57% of issues by volume — a manual keyboard + screen-reader pass (per [`../docs/accessibility/accessibility-standards.md`](../docs/accessibility/accessibility-standards.md)) is a required release check even though it can't gate CI.
- [ ] Contrast conforms to WCAG 2.2 AA (4.5:1 / 3:1 / 3:1 non-text) per [`../docs/accessibility/contrast-matrix.md`](../docs/accessibility/contrast-matrix.md).

## 6. HTML validity — 0 errors

- [ ] Nu Html Checker (`vnu --errors-only`) returns **0 errors** on built pages. Warnings triaged (WCAG 2.2 dropped 4.1.1 Parsing, so valid-nesting is quality, not a WCAG SC).
- [ ] Exactly one `<h1>`; no duplicate `id`s; landmarks present.

## 7. Broken links — 0 broken

- [ ] Internal-link crawl: **0** internal 4xx/5xx and **0** broken anchors/assets.
- [ ] External links checked (flag 4xx/5xx; allow transient); no links to staging/localhost; no redirect chains on internal links.

## 8. Performance budgets — all met

Enforce via Lighthouse CI `budget.json` / bundlesize. See [`../docs/performance/performance-budget.md`](../docs/performance/performance-budget.md).

| Budget | Limit |
|---|---|
| Initial JS (gzipped) | **< 150 KB** |
| CSS | **< 100 KB** |
| Hero / LCP image | **< 150 KB** |
| Total initial transfer | **< 1 MB** |
| HTML document | **< 50 KB** |

- [ ] No budget exceeded. A regression that pushes any category over its limit **fails the build**.
- [ ] LCP image is not lazy-loaded and carries `fetchpriority="high"`; all media have explicit dimensions (CLS guard).

## 9. Structured data — 0 errors

- [ ] JSON-LD on changed pages validates with **0 errors** (Google Rich Results Test + [Schema.org validator](https://validator.schema.org/)). See [`../docs/seo/structured-data.md`](../docs/seo/structured-data.md).
- [ ] Correct type per page (Organization/WebSite, LocalBusiness subtype, Service, BreadcrumbList, FAQPage, Article); NAP consistent across site/schema/GBP; no schema for absent content.

## 10. Core Web Vitals (field) — monitor, don't block

- [ ] Post-deploy, **all three CWV "good" at p75** in CrUX/RUM: **LCP <= 2.5s · INP <= 200ms · CLS <= 0.1**. (Thresholds unchanged in 2026; ignore blog myths of a 2.0s LCP.)
- [ ] INP is the most-failed vital in 2026 — track main-thread long tasks (`<= 50ms`) and third-party JS in RUM. Field data lags ~28 days; schedule the re-check.

## Static-file validity gates (config files)

- [ ] `robots.txt`: parses, `< 500 KiB`, allows CSS/JS/images, valid `Sitemap:` line. See [`../public-templates/robots.txt`](../public-templates/robots.txt).
- [ ] `sitemap.xml`: valid XML, absolute canonical https `<loc>`s, real `<lastmod>`, `<= 50,000` URLs / `<= 50 MB`. See [`../public-templates/sitemap.xml`](../public-templates/sitemap.xml).
- [ ] `site.webmanifest`: valid JSON, `theme_color` `#4F46E5`, 192 + 512 + maskable icons, `display: standalone`. See [`../public-templates/site.webmanifest`](../public-templates/site.webmanifest).
- [ ] `security.txt`: at `/.well-known/`, valid `Contact` + **future** `Expires` + matching `Canonical`. See [`../public-templates/security.txt`](../public-templates/security.txt).

---

## Suggested CI wiring (illustrative)

```yaml
# .github/workflows/quality-gates.yml (sketch — adapt to your stack)
jobs:
  quality:
    steps:
      - run: npx lhci autorun                 # gates 1-4, 8 (assert >= 0.95, budget.json)
      - run: npx @axe-core/cli $URLS          # gate 5 (fail on critical/serious)
      - run: npx vnu-jar --errors-only build/ # gate 6
      - run: npx linkinator build/ --silent   # gate 7
      # gate 9 schema: validate JSON-LD in CI or via Rich Results Test pre-release
```

---

## Related

- [`pre-launch.md`](./pre-launch.md)
- [`new-page.md`](./new-page.md)
- [`content-publish.md`](./content-publish.md)
- [`../docs/performance/performance-budget.md`](../docs/performance/performance-budget.md)
- [`../docs/accessibility/accessibility-standards.md`](../docs/accessibility/accessibility-standards.md)
- [`../docs/seo/technical-seo.md`](../docs/seo/technical-seo.md)
- [`../docs/seo/structured-data.md`](../docs/seo/structured-data.md)
