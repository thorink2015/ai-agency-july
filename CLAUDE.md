# CLAUDE.md — Root Memory & Index

**Purpose:** The single entry point for any Claude session or teammate working in this repo. Start here, then follow the links. This file is the map; the docs are the territory.
**Status:** v1 foundation — adjustable.

---

## What this repo is

This is the **foundation and operating system** for {{BRAND_NAME}} — an AI appointment-setting & lead-response agency website. It is a **knowledge base, not an app**: every brand, design, SEO, performance, accessibility, and process decision lives here as a retrievable doc, token, template, or checklist so the next session can *apply* it without re-deriving it.

> **Scope guard (read before you build).** This repo intentionally contains **no page markup and no marketing copy yet**. The work here is the *foundation*: design tokens, brand system, SEO/AI-SEO systems, performance budgets, accessibility standards, structured-data templates, legal-page scaffolding, and the memory/troubleshooting systems. Do **not** start building pages or writing final copy unless the owner asks — extend the foundation instead.

## Prime directives

1. **Retrieve, don't re-derive.** If a doc or token already specifies a value, use it. Never invent a hex, breakpoint, threshold, or NAP.
2. **One source of truth per fact.** Design values → `tokens/design-tokens.json`. Colour/contrast → the canonical colour docs. Decisions → `docs/systems/decision-log.md`. If two places disagree, the source of truth wins and the other is a bug to fix.
3. **Every change updates memory.** New decision → append an ADR. Standard changed → edit the owning doc and bump the token version. Never leave a decision only in chat.
4. **Reference tokens by name.** Use `--color-brand-600`, `--space-4` in docs and code — raw hex only in the canonical colour/contrast docs.
5. **Accessible + fast by default.** Every choice must satisfy WCAG 2.2 AA (ADR-0004) and the performance budget (ADR-0005). These are non-negotiable, not later polish.

## Start here (cold-start reading order)

1. This file — the map.
2. [`docs/00-foundations/project-brief.md`](docs/00-foundations/project-brief.md) — what the business is, who it serves, the offer, conversion goals.
3. [`docs/00-foundations/principles.md`](docs/00-foundations/principles.md) — the checkable rulebook every decision must satisfy.
4. [`docs/systems/decision-log.md`](docs/systems/decision-log.md) — the 10 settled decisions (ADRs); don't re-litigate them.
5. [`docs/systems/memory-system.md`](docs/systems/memory-system.md) — how to retrieve and update this knowledge base.
6. Keep [`tokens/design-tokens.json`](tokens/design-tokens.json) open — it settles every value dispute.

## Directory map

```text
ai-agency-july/
├── CLAUDE.md                 # ← you are here. Root index.
├── README.md                 # Human-facing overview; defers to this file.
├── tokens/                   # ★ SOURCE OF TRUTH for all design values.
│   ├── design-tokens.json    #   Canonical values (W3C DTCG) + $meta.version.
│   ├── tokens.css            #   CSS custom properties for product code.
│   └── tailwind.tokens.js    #   Same tokens as a Tailwind theme.
├── docs/
│   ├── 00-foundations/       # Why we exist: brief, brand strategy, principles.
│   ├── brand/                # Colour, typography, logo, imagery, icons, voice.
│   ├── design-system/        # Applied tokens, components, layout, motion, interaction.
│   ├── accessibility/        # WCAG 2.2 AA standards + the contrast matrix (evidence).
│   ├── performance/          # Core Web Vitals budgets, image + asset efficiency.
│   ├── responsive/           # Breakpoints and responsive standards.
│   ├── seo/                  # Strategy, on-site, technical, off-site, GEO, structured data.
│   ├── legal/                # Privacy/terms/cookie/SMS-consent page scaffolding.
│   ├── systems/              # ★ How this repo operates (memory, decisions, workflow).
│   └── troubleshooting/      # Symptom → cause → fix runbooks.
├── schema/                   # JSON-LD structured-data templates + README.
├── public-templates/         # Ship-as-is files: robots.txt, sitemap, llms.txt, manifest, <head>.
├── checklists/               # Acceptance checklists: new-page, content, pre-launch, quality-gates.
├── assets/brand/             # Source art: logo SVGs, image sources, exports.
└── scripts/                  # Repo tooling: verify-contrast.py, check-links.py.
```

## Where do I look? (task → doc)

| I need to… | Go to |
| --- | --- |
| Understand the business / audience / offer | [`docs/00-foundations/project-brief.md`](docs/00-foundations/project-brief.md) |
| Get positioning, voice, naming, taglines | [`docs/00-foundations/brand-strategy.md`](docs/00-foundations/brand-strategy.md) |
| Write copy / microcopy the right way | [`docs/brand/voice-and-tone.md`](docs/brand/voice-and-tone.md) |
| Use a colour (and know what's allowed) | [`docs/brand/color-system.md`](docs/brand/color-system.md) + [`tokens/design-tokens.json`](tokens/design-tokens.json) |
| Set type / fonts / scale | [`docs/brand/typography.md`](docs/brand/typography.md) |
| Use the logo / make favicons / OG images | [`docs/brand/logo-and-usage.md`](docs/brand/logo-and-usage.md) |
| Choose imagery / icons | [`docs/brand/imagery.md`](docs/brand/imagery.md) · [`docs/brand/iconography.md`](docs/brand/iconography.md) |
| Build or style a component / CTA / form | [`docs/design-system/`](docs/design-system/README.md) |
| Lay out a page / grid / section | [`docs/design-system/layout-and-grid.md`](docs/design-system/layout-and-grid.md) |
| Animate something | [`docs/design-system/motion.md`](docs/design-system/motion.md) |
| Make it work on all screens | [`docs/responsive/responsive-standards.md`](docs/responsive/responsive-standards.md) |
| Check contrast / keyboard / ARIA | [`docs/accessibility/accessibility-standards.md`](docs/accessibility/accessibility-standards.md) · [`docs/accessibility/contrast-matrix.md`](docs/accessibility/contrast-matrix.md) |
| Hit performance budgets | [`docs/performance/performance-budget.md`](docs/performance/performance-budget.md) |
| Optimize an image / asset | [`docs/performance/image-optimization.md`](docs/performance/image-optimization.md) · [`docs/performance/asset-efficiency.md`](docs/performance/asset-efficiency.md) |
| Do on-page / technical SEO | [`docs/seo/onsite-seo.md`](docs/seo/onsite-seo.md) · [`docs/seo/technical-seo.md`](docs/seo/technical-seo.md) |
| Get cited by AI answer engines (GEO) | [`docs/seo/ai-seo-geo.md`](docs/seo/ai-seo-geo.md) |
| Do off-site / local SEO (GBP, reviews) | [`docs/seo/offsite-seo.md`](docs/seo/offsite-seo.md) |
| Add JSON-LD structured data | [`docs/seo/structured-data.md`](docs/seo/structured-data.md) + [`schema/`](schema/README.md) |
| Scaffold privacy / terms / cookie / SMS pages | [`docs/legal/legal-pages.md`](docs/legal/legal-pages.md) |
| Ship a new page end-to-end | [`docs/systems/content-workflow.md`](docs/systems/content-workflow.md) + [`checklists/`](checklists/new-page.md) |
| Fix a recurring problem | [`docs/troubleshooting/README.md`](docs/troubleshooting/README.md) |
| Know *why* we chose something | [`docs/systems/decision-log.md`](docs/systems/decision-log.md) |

## Source-of-truth precedence (highest first)

1. [`tokens/design-tokens.json`](tokens/design-tokens.json) — any numeric/colour design value.
2. [`docs/brand/color-system.md`](docs/brand/color-system.md) + [`docs/accessibility/contrast-matrix.md`](docs/accessibility/contrast-matrix.md) — the only docs allowed to state raw hex + contrast ratios.
3. [`docs/systems/decision-log.md`](docs/systems/decision-log.md) — *why* a standard is what it is.
4. The domain doc that owns the topic (task table above).
5. Everything else references the above by name/path.

## Standards at a glance (pointers, not the source of truth)

| Domain | The bar | Source |
| --- | --- | --- |
| **Colour** | Indigo `--color-brand-600` primary · teal `--color-accent-500` accent (ink text only) · all pairings WCAG-validated | [color-system.md](docs/brand/color-system.md) · ADR-0001 |
| **Type** | Sora (display) + Inter (body) + JetBrains Mono · 16px base · body line-height ≥ 1.5 · 68ch measure | [typography.md](docs/brand/typography.md) · ADR-0002 |
| **Spacing/scale** | 4px base · modular type scale · fluid `clamp()` for h1–h3 | ADR-0003 |
| **Breakpoints** | sm 640 · md 768 · lg 1024 · xl 1280 · 2xl 1536 · min supported width 320px · content max 1200px | [responsive-standards.md](docs/responsive/responsive-standards.md) |
| **Accessibility** | WCAG 2.2 **AA** (AAA text where feasible) · visible focus · 44px targets · reduced-motion | [accessibility-standards.md](docs/accessibility/accessibility-standards.md) · ADR-0004 |
| **Performance** | LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 · TTFB ≤ 0.8s · Lighthouse ≥ 95 · JS < 150KB gz · LCP img < 150KB · total < 1MB | [performance-budget.md](docs/performance/performance-budget.md) · ADR-0005 |
| **Images** | AVIF + WebP fallback · responsive `srcset` · explicit `width`/`height` · lazy below fold · `fetchpriority` on LCP | [image-optimization.md](docs/performance/image-optimization.md) · ADR-0006 |
| **Rendering** | Static-first (Astro or Next static export) · minimal client JS | ADR-0007 |
| **SEO** | Title ≤ 60 · meta description ≤ 155 · one H1 · canonical · OG/Twitter · sitemap · robots | [onsite-seo.md](docs/seo/onsite-seo.md) · [technical-seo.md](docs/seo/technical-seo.md) |
| **Structured data** | Organization · LocalBusiness (ProfessionalService) · Service · FAQPage · Review · BreadcrumbList · WebSite | [structured-data.md](docs/seo/structured-data.md) · ADR-0008 |
| **AI/GEO** | `llms.txt` · extractable answers · entity clarity · consistent NAP · cited stats | [ai-seo-geo.md](docs/seo/ai-seo-geo.md) · ADR-0009 |

## Decisions (ADR index)

The 10 foundational decisions are recorded in [`docs/systems/decision-log.md`](docs/systems/decision-log.md): ADR-0001 palette · 0002 typography · 0003 spacing/type scale · 0004 accessibility target · 0005 performance budgets · 0006 image strategy · 0007 rendering · 0008 structured data · 0009 llms.txt · 0010 tokens-as-source-of-truth. **Do not re-litigate an Accepted ADR — supersede it with a new one if it must change.**

## Placeholders (never invent real values)

Business/brand specifics use mustache placeholders the owner find-and-replaces at launch:
`{{BRAND_NAME}}`, `{{DOMAIN}}` (use `example.com` in examples), `{{LEGAL_ENTITY}}`, `{{EMAIL}}`, `{{PHONE}}`, `{{ADDRESS}}`, `{{CITY}}`, `{{REGION}}`, `{{POSTAL}}`, `{{COUNTRY}}`, `{{SOCIAL_*}}`. Keep NAP (name/address/phone) identical across `schema/`, `public-templates/llms.txt`, and the eventual site footer.

## Working rules & verification

- **Consume tokens, never hardcode.** Import [`tokens/tokens.css`](tokens/tokens.css) or [`tokens/tailwind.tokens.js`](tokens/tailwind.tokens.js).
- **After any colour change:** run `python3 scripts/verify-contrast.py --strict` and update [`docs/accessibility/contrast-matrix.md`](docs/accessibility/contrast-matrix.md) + `$meta.lastValidated`.
- **After editing docs:** run `python3 scripts/check-links.py` to catch broken relative links before committing.
- **Adding a doc:** use the standard header + `## Related` footer, put it in the right domain folder, and link it from this file and one sibling.
- **Made a non-obvious decision:** append an ADR to the decision log.

## Status

**Done (v1 foundation):** design tokens (contrast-validated) · brand system (colour, type, logo spec, imagery, icons, voice) · design system (components, layout, motion, interaction) · responsive · accessibility (WCAG 2.2 AA + matrix) · performance budgets + image/asset optimization · SEO (strategy, on-site, technical, off-site, GEO) · structured-data templates · legal-page scaffolding · memory/decision/workflow systems · troubleshooting runbooks · ship-as-is templates + checklists · tooling (contrast + link verifiers).

**Not started (by design):** page markup, final marketing copy, real brand name/logo art, real business NAP. These come after the owner confirms the foundation.

---

## Related

- [`README.md`](README.md) — human-facing overview.
- [`docs/systems/memory-system.md`](docs/systems/memory-system.md) — retrieve/update protocol.
- [`docs/systems/decision-log.md`](docs/systems/decision-log.md) — the ADRs.
- [`docs/systems/content-workflow.md`](docs/systems/content-workflow.md) — brief → publish workflow.
- [`tokens/design-tokens.json`](tokens/design-tokens.json) — design value source of truth.
