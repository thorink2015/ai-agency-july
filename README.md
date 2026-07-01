# {{BRAND_NAME}} — Website Foundation

The brand, design, SEO, performance, accessibility, and process **foundation** for {{BRAND_NAME}}, an AI appointment-setting & lead-response agency. This repository is a **knowledge base and design system, not the website itself** — it holds the tokens, standards, templates, and systems that the site is built on so everything ships fast, accessible, and on-brand.

> **New here?** Start with **[`CLAUDE.md`](CLAUDE.md)** — the root memory index that maps everything below.

## What's inside

| Area | Where | What it gives you |
| --- | --- | --- |
| **Design tokens** | [`tokens/`](tokens/) | Single source of truth for colour, type, spacing, motion (JSON + CSS + Tailwind). All colour pairings WCAG-validated. |
| **Brand** | [`docs/brand/`](docs/brand/) | Colour, typography, logo spec, imagery, iconography, and the [voice & copy system](docs/brand/voice-and-tone.md). |
| **Design system** | [`docs/design-system/`](docs/design-system/README.md) | Component contracts, layout/grid, interactive elements, motion. |
| **Accessibility** | [`docs/accessibility/`](docs/accessibility/) | WCAG 2.2 AA standards + the contrast matrix (evidence). |
| **Performance** | [`docs/performance/`](docs/performance/) | Core Web Vitals budgets, image & asset optimization. |
| **Responsive** | [`docs/responsive/`](docs/responsive/) | Breakpoints and cross-device standards. |
| **SEO / AI-SEO** | [`docs/seo/`](docs/seo/) | Strategy, on-site, technical, off-site, GEO (AI answer engines), structured data. |
| **Structured data** | [`schema/`](schema/) | Ready-to-fill JSON-LD templates (Organization, LocalBusiness, Service, FAQ, Review, Breadcrumb, WebSite). |
| **Legal** | [`docs/legal/`](docs/legal/) | Privacy / terms / cookie / SMS-consent page scaffolding (structure, not legal advice). |
| **Systems** | [`docs/systems/`](docs/systems/) | The [memory system](docs/systems/memory-system.md), [decision log](docs/systems/decision-log.md), and [content workflow](docs/systems/content-workflow.md). |
| **Troubleshooting** | [`docs/troubleshooting/`](docs/troubleshooting/README.md) | Symptom → cause → fix runbooks. |
| **Ship-as-is templates** | [`public-templates/`](public-templates/) | `robots.txt`, `sitemap.xml`, `llms.txt`, web manifest, `<head>` meta. |
| **Checklists** | [`checklists/`](checklists/) | New-page, content-publish, pre-launch, and quality-gate acceptance checklists. |
| **Tooling** | [`scripts/`](scripts/) | `verify-contrast.py` (WCAG check) and `check-links.py` (relative-link check). |

## Quick start

```bash
# Verify every colour pairing still meets WCAG (run after any token change)
python3 scripts/verify-contrast.py --strict

# Check for broken relative links across the docs
python3 scripts/check-links.py
```

## Conventions

- **Consume tokens, never hardcode values.** Reference by name (`--color-brand-600`, `--space-4`).
- **Placeholders** like `{{BRAND_NAME}}`, `{{DOMAIN}}`, `{{EMAIL}}`, `{{PHONE}}` mark business-specific values to find-and-replace at launch.
- **Every decision is logged** as an ADR in [`docs/systems/decision-log.md`](docs/systems/decision-log.md).

## Status

`v1 foundation` — the systems above are in place and adjustable. Page markup, final marketing copy, and the real brand name/logo/NAP are intentionally **not** built yet; they come once the foundation is confirmed. See [`CLAUDE.md`](CLAUDE.md) for the full picture.
