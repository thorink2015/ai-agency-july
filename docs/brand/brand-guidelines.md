# Brand Guidelines

**Purpose:** The master brand overview and index — the one page that orients any human or future Claude session to the {{BRAND_NAME}} brand system, then routes to the deep-dive docs for colour, type, imagery, iconography, voice, and logo.
**Status:** v1 foundation — adjustable.

---

## What this is (and is not)

This is the **brand-in-one-page** summary plus an index of the system docs. It is not website copy, and it is not the source of truth for raw values — [`tokens/design-tokens.json`](../../tokens/design-tokens.json) is. When a value here disagrees with the tokens, the tokens win; fix this doc.

Use this doc to:

- [ ] Get oriented fast (personality, palette, fonts, do/don'ts) before building anything.
- [ ] Find the right deep-dive doc for the decision you're making.
- [ ] Sanity-check that a page, asset, or piece of copy is "on-brand" before it ships.

---

## The brand in one line

> **{{BRAND_NAME}} — Never miss a lead. AI that answers, qualifies, and books in seconds, 24/7, with humans on call when it matters.**

We are a done-for-you AI appointment-setting & lead-response agency. We deploy and manage AI chat/SMS/web assistants for businesses that already generate leads and lose them to slow follow-up.

---

## Positioning snapshot

| Field | Value |
|---|---|
| **Category** | AI appointment-setting & lead-response agency (service/agency, not SaaS) |
| **Audience** | SMB owners & marketing/ops leads in service industries — med spas, dental, home services, real estate, coaches, clinics, agencies — who already buy or generate leads |
| **Core promise** | Never miss a lead — AI answers, qualifies, and books in seconds, 24/7, with humans on call |
| **Differentiators** | Speed-to-lead · Done-for-you setup & management · Human support on call · Integrates with existing tools |
| **Primary job we solve** | Slow follow-up losing hot leads |
| **Proof themes** | Response time in seconds, booked appointments, revenue recovered, hours saved |

---

## Brand personality

Six traits, in priority order. When two pull against each other, the higher one wins.

| # | Trait | Means we... | Never... |
|---|---|---|---|
| 1 | **Trustworthy** | Back claims with numbers, show the humans, keep NAP consistent | Over-promise or hide the AI |
| 2 | **Fast** | Lead with speed-to-lead; UI and copy feel instant | Feel sluggish or bury the value |
| 3 | **Competent** | Precise, specific, no filler | Sound vague or generic |
| 4 | **Human + AI** | Pair automation with "humans on call when it matters" | Feel cold or fully robotic |
| 5 | **Premium but approachable** | Generous whitespace, crisp geometry, plain language | Feel cheap, busy, or elitist |
| 6 | **Calm confidence** | State outcomes plainly, no exclamation-mark energy | Hype, hard-sell, or fear-bait |

**Personality dial:** modern-tech **with warmth**. Think "the calm, competent operator who already handled it" — not a loud growth-hacker, not a sterile enterprise tool.

---

## Voice at a glance

Full rules live in [`voice-and-tone.md`](./voice-and-tone.md). The essentials:

- **Clear, direct, benefit-led.** Say what the reader gets, then how.
- **Second person, present tense.** "You never miss a lead." Not "Clients can leverage..."
- **Short sentences.** One idea each. Jargon-light.
- **Reassuring, confident, no hype.** Confidence without exclamation marks.

| Do | Don't |
|---|---|
| "Answers every lead in seconds." | "Revolutionary AI that will 10x your business!!!" |
| "Humans on call when it matters." | "Fully autonomous, zero human needed." |
| "Books appointments while you sleep." | "Leverage synergistic omnichannel paradigms." |
| "Set up for you in days, not months." | "Easy self-serve onboarding" (we are done-for-you) |

---

## Palette at a glance

Canonical colour rules, pairings, and the full contrast matrix live in [`color-system.md`](./color-system.md). Never hardcode hex in product code — consume tokens (`--color-*`). Reference tokens by name everywhere except the canonical colour doc.

| Role | Token | Hex | Use |
|---|---|---|---|
| **Primary / brand** | `--color-brand-600` | `#4F46E5` | Default CTA, links, brand marks. White text = 6.29:1 AA. |
| **Primary hover** | `--color-brand-700` | `#4338CA` | CTA hover/active. White text = 7.90:1 AAA. |
| **Accent (teal)** | `--color-accent-500` | `#06B6D4` | Highlights, decorative. **INK text only** (7.76:1). **Never white** (2.43:1 FAILS). |
| **Accent for white text** | `--color-accent-700` | `#0E7490` | The only teal you may put white text on. |
| **Ink / primary text** | `--color-neutral-ink` | `#0B1120` | Body & heading text, dark sections. 18.83:1 AAA. |
| **Body text** | `--color-neutral-700` | `#334155` | Long-form body. 10.35:1 AAA. |
| **Secondary text** | `--color-neutral-600` | `#475569` | Supporting text. 7.58:1 AAA. |
| **Muted text (min)** | `--color-neutral-500` | `#64748B` | Smallest allowed muted text (4.76:1 AA); min interactive border. |
| **Surfaces** | `--color-neutral-0/50` | `#FFFFFF` / `#F8FAFC` | Page & subtle section backgrounds. |

**Semantic:** success `#16A34A` (white on large/UI only; use `success-strong` `#15803D` for normal white text), warning `#D97706` (**INK text**), danger `#DC2626` (white AA), info `#2563EB` (white AA).

**Three colour rules you will break by accident:**

1. **Never put white text on `accent-500` teal.** It fails contrast. Use ink on teal, or use `accent-700` for white text.
2. **`neutral-400` (`#94A3B8`) is disabled/hint only** — never meaningful text or borders.
3. **`neutral-200/300` are decorative dividers only** — not real borders; use `neutral-500` for anything that must be perceivable.

---

## Type at a glance

Full scale, pairings, and loading strategy live in [`typography.md`](./typography.md).

| Role | Font | Token | Notes |
|---|---|---|---|
| **Display / headings** | Sora (variable) | `--font-display` | Geometric, modern-tech. h1–h3 use fluid `clamp()`. |
| **Body / UI** | Inter (variable) | `--font-body` | Best-in-class legibility. Base 16px, never smaller for body. |
| **Mono / technical** | JetBrains Mono | `--font-mono` | Code, metrics, technical accents — optional. |

- Base size **16px**; modular scale; **line-height ≥ 1.5** for body (WCAG).
- Prose measure capped at **68ch** (`--container-prose`).
- Fonts subset, `font-display: swap`, preload critical weights (see typography doc + performance budget).

---

## Visual direction at a glance

Imagery rules live in [`imagery.md`](./imagery.md); icon rules in [`iconography.md`](./iconography.md).

- **Layout:** generous whitespace, `1200px` max content, section rhythm on the 4px spacing scale.
- **Geometry:** rounded-but-crisp. Cards `--radius-lg` (12px), controls `--radius-md` (8px), hero panels `--radius-2xl` (24px), pills `--radius-full`.
- **Depth:** subtle, layered shadows (`--shadow-sm`→`--shadow-xl`) using ink at low alpha — never harsh black drop-shadows.
- **Motion:** responsive, not decorative. 100–500ms, `ease-standard` `cubic-bezier(0.4,0,0.2,1)`. **Gate all non-essential motion behind `prefers-reduced-motion`.**
- **Imagery:** real people + product moments over stock-y "robot" clichés. AVIF+WebP, responsive `srcset`, explicit `width`/`height`, lazy-load below fold.
- **Icons:** consistent SVG line set, 24px grid, `1.5px`–`2px` stroke, rounded joins.

---

## Master do / don't

| Do | Don't |
|---|---|
| Lead with speed-to-lead and booked appointments | Lead with "AI" as the hero — AI is the how, not the promise |
| Show the humans (support, team, real photos) | Imply zero humans or hide who's behind it |
| Use numbers and specifics ("in seconds", "24/7") | Use vague superlatives ("best", "cutting-edge") |
| Keep whitespace generous and layouts calm | Crowd sections or stack competing CTAs |
| Use brand indigo for primary actions | Use teal for primary CTAs with white text |
| Cite real, consistent NAP everywhere | Vary business name/phone/address between pages |
| Respect `prefers-reduced-motion` | Ship autoplaying or decorative motion by default |
| Consume design tokens by name | Hardcode hex, px, or font stacks in components |

---

## Naming, entity & NAP consistency

Use the mustache placeholders verbatim so the owner can find-and-replace later. Consistency here is an E-E-A-T and local-SEO signal — the **same** values must appear in footer, contact page, schema (JSON-LD), and business listings.

| Placeholder | Use for |
|---|---|
| `{{BRAND_NAME}}` | Public brand name (e.g. in logo, titles) |
| `{{LEGAL_ENTITY}}` | Legal/registered name (contracts, footer copyright) |
| `{{DOMAIN}}` | Primary domain (`example.com` in examples) |
| `{{EMAIL}}` / `{{PHONE}}` | Contact — identical everywhere |
| `{{ADDRESS}}`, `{{CITY}}`, `{{REGION}}`, `{{POSTAL}}`, `{{COUNTRY}}` | Postal address / NAP |
| `{{SOCIAL_*}}` | Social profile URLs (e.g. `{{SOCIAL_LINKEDIN}}`) |

Do **not** invent real values. Do **not** abbreviate the brand name in one place and spell it out in another.

---

## Document map

The brand system is split into focused docs. Start here, then go deep.

| Doc | Owns | Path |
|---|---|---|
| **Brand Guidelines** (this doc) | One-page overview + index | `docs/brand/brand-guidelines.md` |
| **Colour System** | Canonical palette, contrast matrix, pairing rules | [`color-system.md`](./color-system.md) |
| **Typography** | Font stack, scale, loading, pairings | [`typography.md`](./typography.md) |
| **Imagery & Photography** | Photo/illustration direction, treatments, formats | [`imagery.md`](./imagery.md) |
| **Iconography** | Icon set, grid, stroke, usage | [`iconography.md`](./iconography.md) |
| **Voice & Tone** | Writing rules, vocabulary, examples | [`voice-and-tone.md`](./voice-and-tone.md) |
| **Logo & Usage** | Logo variants, clear space, favicon/OG matrix, creation brief | [`logo-and-usage.md`](./logo-and-usage.md) |

**Upstream sources of truth:**

- [`tokens/design-tokens.json`](../../tokens/design-tokens.json) — all raw values.
- [`tokens/tokens.css`](../../tokens/tokens.css) — CSS custom properties consumed by code.

---

## How to keep this doc honest

- [ ] When you change a token, re-check the "at a glance" tables here.
- [ ] When you add a brand doc, add it to the **Document map** and to a sibling **Related** section.
- [ ] Every colour pairing you introduce must be validated against `docs/accessibility/contrast-matrix.md`.
- [ ] Bump the **Status** line date if the brand meaningfully shifts.

---

## Related

- [`color-system.md`](./color-system.md) — canonical colour & contrast.
- [`typography.md`](./typography.md) — type system.
- [`imagery.md`](./imagery.md) — photography & illustration direction.
- [`iconography.md`](./iconography.md) — icon system.
- [`voice-and-tone.md`](./voice-and-tone.md) — writing voice.
- [`logo-and-usage.md`](./logo-and-usage.md) — logo system & creation brief.
- [`../../tokens/design-tokens.json`](../../tokens/design-tokens.json) — source of truth for values.
- [`../../tokens/tokens.css`](../../tokens/tokens.css) — CSS custom properties.
