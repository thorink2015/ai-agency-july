# Design Tokens

**Purpose:** Human-readable companion to [`tokens/design-tokens.json`](../../tokens/design-tokens.json) — explains the token architecture (primitive → semantic/role), naming rules, how to consume tokens in CSS and Tailwind, the change/governance process, and a full reference table so any developer or future Claude session applies design values correctly and never hardcodes.
**Status:** v1 foundation — adjustable.

---

> **Source of truth:** [`tokens/design-tokens.json`](../../tokens/design-tokens.json). Everything else — [`tokens/tokens.css`](../../tokens/tokens.css) (CSS custom properties) and [`tokens/tailwind.tokens.js`](../../tokens/tailwind.tokens.js) (Tailwind theme) — is a **generated mirror**. Edit the JSON, regenerate the mirrors, re-validate. Never edit a mirror by hand.
>
> **Raw hex/px belong in the JSON and in the canonical colour doc only.** In product code and every other doc, reference tokens **by name** (`var(--color-brand-600)`, `--space-4`), never by literal value.

---

## 0. TL;DR — the rules you will break by accident

- [ ] **The JSON is canonical.** `tokens.css` and `tailwind.tokens.js` are downstream. If they disagree with the JSON, the JSON wins and the mirror is stale.
- [ ] **Never hardcode** a hex, px, ms, or cubic-bezier in a component. Consume a token.
- [ ] **Prefer ROLE tokens over primitives** in components. Use `var(--cta-bg)`, not `var(--color-brand-600)`, when the intent is "this is a CTA."
- [ ] **Primitives are the palette; roles are the decisions.** Changing a role remaps every consumer at once — that is the point.
- [ ] **Colour pairings are contrast-validated.** Do not invent new colour combinations; use the validated roles. See [`../brand/color-system.md`](../brand/color-system.md).
- [ ] **Every value change is a governed change**: edit JSON → regenerate → validate → commit all three files together.

---

## 1. Token architecture — two tiers

Tokens are organised in **two tiers**. This separation is the whole reason the system is maintainable.

```
Tier 1 — PRIMITIVES  (the raw palette / scale)
   color.brand.600  = #4F46E5
   space.4          = 1rem
   radius.lg        = 0.75rem
        │
        │  referenced by  { … }  aliases
        ▼
Tier 2 — SEMANTIC / ROLE  (the design decisions)
   color.role.ctaBg = {color.brand.600}
   color.role.text  = {color.neutral.ink}
```

| Tier | What it is | Example | Consume in components? |
|---|---|---|---|
| **Primitive** | Context-free raw values. A palette swatch or a step on a scale. Named by _what it is_. | `color.brand.600`, `space.8`, `radius.lg`, `motion.duration.fast` | Layout/spacing/radius/motion: **yes**. Colour: **prefer roles.** |
| **Semantic / Role** | A named _decision_ that points at a primitive via a `{reference}`. Named by _what it does_. | `color.role.ctaBg`, `color.role.text`, `color.role.focusRing` | **Yes — prefer these**, especially for colour. |

**Why two tiers?** A primitive answers "what colour is indigo 600?" A role answers "what colour is a primary button?" When the brand shifts, you re-point one role (`ctaBg`) and every button updates — without hunting through components. Roles also enable **theming**: `.surface-dark` in `tokens.css` re-binds `--text`, `--bg`, `--link` for dark sections without touching a single component.

### Current role map (colour)

Only colour has a formal role tier today. These are the aliases you should reach for first:

| Role token (JSON `color.role.*`) | CSS var | Points at | Meaning |
|---|---|---|---|
| `text` | `--text` | `neutral.ink` | Default body/heading text |
| `textSecondary` | `--text-secondary` | `neutral.600` | Secondary/supporting text |
| `textMuted` | `--text-muted` | `neutral.500` | Muted text (minimum for real text) |
| `textOnDark` | `--text-on-dark` | `neutral.0` | Text on dark surfaces |
| `textMutedOnDark` | `--text-muted-on-dark` | `neutral.300` | Muted text on dark surfaces |
| `link` | `--link` | `brand.600` | Inline links |
| `linkHover` | `--link-hover` | `brand.700` | Link hover/active |
| `bg` | `--bg` | `neutral.0` | Default page background |
| `bgSubtle` | `--bg-subtle` | `neutral.50` | Alternating/subtle section background |
| `bgDark` | `--bg-dark` | `neutral.ink` | Dark section background |
| `border` | `--border` | `neutral.200` | Decorative divider only |
| `borderInteractive` | `--border-interactive` | `neutral.500` | Inputs/controls (3:1 non-text) |
| `focusRing` | `--focus-ring` | `brand.600` | Focus-visible outline |
| `ctaBg` / `ctaBgHover` / `ctaText` | `--cta-bg` / `--cta-bg-hover` / `--cta-text` | `brand.600` / `brand.700` / `neutral.0` | Primary button |

> Spacing, radius, typography, motion, z-index, and layout are currently **single-tier primitives** consumed directly (`--space-4`, `--radius-lg`). That is intentional — they are stable scales, not brand decisions. If a future need arises (e.g. `--space-section`), add a role alias rather than a new magic number.

---

## 2. Naming rules

### Primitives
- **Colour:** `color.<family>.<step>` — family ∈ `brand | accent | neutral | semantic`; step is a numeric ramp `50…900` (higher = darker) plus named outliers (`neutral.ink`, `neutral.0`).
- **Scales:** the token _key_ often maps to a value or T-shirt size — `space.4` = 16px (4 × 4px base), `radius.md`, `fontSize.lg`, `motion.duration.fast`.

### Roles
- `color.role.<intent>` in **camelCase** — named by function (`ctaBg`, `focusRing`, `textOnDark`), never by colour.

### Generated names (what code actually sees)
The build flattens JSON paths into flat names. **Learn the transform**, don't guess:

| JSON path | CSS custom property | Tailwind key |
|---|---|---|
| `color.brand.600` | `--color-brand-600` | `brand.600` (`bg-brand-600`) |
| `color.neutral.ink` | `--color-ink` | `ink` (`text-ink`) |
| `color.role.ctaBg` | `--cta-bg` | _(roles are not mirrored to Tailwind; use CSS vars)_ |
| `space.8` | `--space-8` | `spacing.8` (`p-8`) |
| `radius.lg` | `--radius-lg` | `borderRadius.lg` (`rounded-lg`) |
| `typography.fontSize.lg` | `--text-lg` | `fontSize.lg` (`text-lg`) |
| `typography.fluid.h1` | `--fluid-h1` | `fontSize.fluid-h1` |
| `motion.duration.fast` | `--duration-fast` | `transitionDuration.fast` |
| `container.content` | `--container-content` | `maxWidth.content` |

> **Note the two deliberate irregularities:** `color.neutral.ink` → `--color-ink` (not `--color-neutral-ink`), and `color.role.*` flatten to short semantic names (`--cta-bg`, `--text`, `--focus-ring`). These match [`tokens.css`](../../tokens/tokens.css); follow it as the naming authority for edge cases.

---

## 3. How to consume tokens

### 3.1 CSS (framework-agnostic) — the default

Import once, globally, then use `var(--token)` everywhere.

```css
/* app entry, before any component styles */
@import "../tokens/tokens.css";

.cta {
  background: var(--cta-bg);
  color: var(--cta-text);
  padding: var(--space-3) var(--space-6);
  border-radius: var(--radius-md);
  min-height: var(--target-min);            /* 44px touch target */
  font: var(--fw-semibold) var(--text-base)/var(--lh-normal) var(--font-body);
  transition: background var(--duration-fast) var(--ease-standard);
}
.cta:hover { background: var(--cta-bg-hover); }
```

**Do / Don't:**

| Do | Don't |
|---|---|
| `color: var(--text-secondary)` | `color: #475569` |
| `gap: var(--space-6)` | `gap: 24px` |
| `border-color: var(--border-interactive)` | `border-color: var(--color-neutral-200)` on an input (fails 3:1) |
| Prefer role vars (`--cta-bg`) | Reach for a primitive (`--color-brand-600`) when a role exists |

### 3.2 Dark sections

Wrap the section in `.surface-dark` (defined in `tokens.css`). It re-binds the colour roles; components inside need no changes.

```html
<section class="surface-dark">
  <!-- --text, --bg, --link now resolve to their dark-surface values -->
</section>
```

### 3.3 Tailwind

Extend the theme from the generated mirror — do not paste values into `tailwind.config.js`.

```js
// tailwind.config.js
const tokens = require('./tokens/tailwind.tokens.js');
module.exports = {
  content: ['./src/**/*.{html,js,ts,jsx,tsx}'],
  theme: { extend: tokens },
};
```

Then use utilities backed by tokens:

```html
<button class="bg-brand-600 hover:bg-brand-700 text-white
               rounded-md px-6 py-3 font-semibold
               transition-colors duration-fast ease-standard">
  Book a demo
</button>
```

> **Roles are not exposed to Tailwind** (Tailwind mirrors primitives only). For role-driven or theme-aware styling (`--cta-bg`, `.surface-dark`), use CSS custom properties. A common hybrid: `class="bg-[var(--cta-bg)]"`.

### 3.4 Choosing the right consumer

| Situation | Use |
|---|---|
| Any app, minimal deps, theme-aware (dark sections) | **CSS vars** (`tokens.css`) |
| Tailwind project, utility-first authoring | **Tailwind** (`tailwind.tokens.js`) for primitives + CSS vars for roles |
| JS needs a value (canvas, chart lib, inline style) | Read the CSS var: `getComputedStyle(el).getPropertyValue('--color-brand-600')` |

---

## 4. Governance — the change process

Tokens are a shared contract. Changing one ripples across the whole site, so changes are **governed, not casual**.

### The pipeline (every value change)

```
1. EDIT      tokens/design-tokens.json         (the ONLY hand-edited file)
2. REGENERATE  tokens/tokens.css  +  tokens/tailwind.tokens.js   (mirror the JSON)
3. VALIDATE  JSON parses · references resolve · contrast re-checked · no orphans
4. COMMIT    all three files together, in one commit, with rationale
```

- [ ] **Step 1 — Edit JSON only.** Add/adjust in `design-tokens.json`. Update the `comment` field with intent and any contrast ratio.
- [ ] **Step 2 — Regenerate mirrors.** Update `tokens.css` and `tailwind.tokens.js` to match. Until an automated generator exists, do this by hand and diff carefully — the flat names must follow the transform in §2.
- [ ] **Step 3 — Validate** (see checklist below).
- [ ] **Step 4 — Commit together.** JSON + both mirrors in one commit so they never drift. Bump `$meta.version` (semver, see below) and `$meta.lastValidated`.

### Validation checklist

- [ ] `design-tokens.json` is valid JSON (parses clean).
- [ ] Every `{reference}` resolves to an existing primitive (no dangling aliases).
- [ ] **Any colour touched → re-run the contrast matrix.** Update [`../accessibility/contrast-matrix.md`](../accessibility/contrast-matrix.md) and [`../brand/color-system.md`](../brand/color-system.md). No pairing may drop below its required ratio.
- [ ] `tokens.css` and `tailwind.tokens.js` names + values match the JSON (spot-diff the changed keys).
- [ ] No orphan tokens (defined, never consumed) and no hardcoded values that _should_ be tokens.
- [ ] `$meta.version` and `$meta.lastValidated` bumped.

### Versioning (`$meta.version`, semver)

| Change | Bump | Example |
|---|---|---|
| **Major** | Remove/rename a token, or re-point a role so meaning changes | Drop `space.5`; repurpose `ctaBg` |
| **Minor** | Add a new token (backward-compatible) | Add `radius.3xl`, add a `bgMuted` role |
| **Patch** | Tweak a value, comment, or fix a mirror with no API change | Nudge `shadow.md` opacity |

### Add vs. reuse — decision rule
Before adding a token, ask: **does an existing step already cover this?** The scales are intentionally coarse. Prefer reusing `space.10` over inventing `space.11`. Add a token only when a value recurs and has a clear, named purpose. One-off values are a smell — usually the design should snap to the existing scale.

### Deprecation
Don't hard-delete a token in active use. Mark it deprecated in the JSON `comment`, migrate consumers, then remove in the next **major** bump.

---

## 5. Full token reference

Grouped by category. **Raw values shown here are the JSON source values** (this is a token-reference doc; a hex/px table is its job). In code, always use the name.

### 5.1 Colour — primitives

**Brand (indigo) — primary identity**

| Token | CSS var | Value | Note |
|---|---|---|---|
| `color.brand.50` | `--color-brand-50` | `#EEF2FF` | Tint bg, hover on light |
| `color.brand.100` | `--color-brand-100` | `#E0E7FF` | |
| `color.brand.200` | `--color-brand-200` | `#C7D2FE` | |
| `color.brand.300` | `--color-brand-300` | `#A5B4FC` | Accent/link text **on dark** (9.45:1 on ink) |
| `color.brand.400` | `--color-brand-400` | `#818CF8` | |
| `color.brand.500` | `--color-brand-500` | `#6366F1` | |
| `color.brand.600` | `--color-brand-600` | `#4F46E5` | **PRIMARY** · white text 6.29:1 AA |
| `color.brand.700` | `--color-brand-700` | `#4338CA` | Primary hover · white text 7.90:1 AAA |
| `color.brand.800` | `--color-brand-800` | `#3730A3` | |
| `color.brand.900` | `--color-brand-900` | `#312E81` | |

**Accent (teal) — highlight, use with care**

| Token | CSS var | Value | Note |
|---|---|---|---|
| `color.accent.400` | `--color-accent-400` | `#22D3EE` | Decorative/highlight only |
| `color.accent.500` | `--color-accent-500` | `#06B6D4` | **ACCENT** · INK text (7.76:1); **white FAILS (2.43:1)** |
| `color.accent.600` | `--color-accent-600` | `#0891B2` | |
| `color.accent.700` | `--color-accent-700` | `#0E7490` | Use for **white-text** teal buttons (5.36:1 AA) |

**Neutral — text, surfaces, borders**

| Token | CSS var | Value | Note |
|---|---|---|---|
| `color.neutral.0` | `--color-white` | `#FFFFFF` | |
| `color.neutral.50` | `--color-neutral-50` | `#F8FAFC` | Subtle section bg |
| `color.neutral.100` | `--color-neutral-100` | `#F1F5F9` | |
| `color.neutral.200` | `--color-neutral-200` | `#E2E8F0` | Decorative divider only |
| `color.neutral.300` | `--color-neutral-300` | `#CBD5E1` | Decorative divider only |
| `color.neutral.400` | `--color-neutral-400` | `#94A3B8` | **Disabled/hint ONLY** (2.56:1) |
| `color.neutral.500` | `--color-neutral-500` | `#64748B` | Min muted text (4.76:1) · min interactive border (3:1) |
| `color.neutral.600` | `--color-neutral-600` | `#475569` | Secondary text (7.58:1 AAA) |
| `color.neutral.700` | `--color-neutral-700` | `#334155` | Body text (10.35:1 AAA) |
| `color.neutral.800` | `--color-neutral-800` | `#1E293B` | |
| `color.neutral.900` | `--color-neutral-900` | `#0F172A` | Headings (17.85:1 AAA) |
| `color.neutral.ink` | `--color-ink` | `#0B1120` | Primary text / dark sections (18.83:1 AAA) |

**Semantic — status colours**

| Token | CSS var | Value | Note |
|---|---|---|---|
| `color.semantic.success` | `--color-success` | `#16A34A` | White = large/UI only |
| `color.semantic.successStrong` | `--color-success-strong` | `#15803D` | White text 5.02:1 AA |
| `color.semantic.warning` | `--color-warning` | `#D97706` | **INK text** (5.91:1); white FAILS |
| `color.semantic.danger` | `--color-danger` | `#DC2626` | White text 4.83:1 AA |
| `color.semantic.info` | `--color-info` | `#2563EB` | White text 5.17:1 AA |

> Colour roles (`color.role.*`) are listed in §1. Full pairing evidence: [`../accessibility/contrast-matrix.md`](../accessibility/contrast-matrix.md).

### 5.2 Typography

**Font families**

| Token | CSS var | Value (family) |
|---|---|---|
| `typography.fontFamily.display` | `--font-display` | Sora → system-ui fallback |
| `typography.fontFamily.body` | `--font-body` | Inter → system-ui fallback |
| `typography.fontFamily.mono` | `--font-mono` | JetBrains Mono → ui-monospace |

**Weights**

| Token | CSS var | Value |
|---|---|---|
| `typography.fontWeight.regular` | `--fw-regular` | 400 |
| `typography.fontWeight.medium` | `--fw-medium` | 500 |
| `typography.fontWeight.semibold` | `--fw-semibold` | 600 |
| `typography.fontWeight.bold` | `--fw-bold` | 700 |

**Font sizes (fixed steps)**

| Token | CSS var | Value | px |
|---|---|---|---|
| `typography.fontSize.xs` | `--text-xs` | `0.75rem` | 12 |
| `typography.fontSize.sm` | `--text-sm` | `0.875rem` | 14 |
| `typography.fontSize.base` | `--text-base` | `1rem` | 16 — never smaller for body |
| `typography.fontSize.lg` | `--text-lg` | `1.125rem` | 18 |
| `typography.fontSize.xl` | `--text-xl` | `1.25rem` | 20 |
| `typography.fontSize.2xl` | `--text-2xl` | `1.5rem` | 24 |
| `typography.fontSize.3xl` | `--text-3xl` | `1.875rem` | 30 |
| `typography.fontSize.4xl` | `--text-4xl` | `2.25rem` | 36 |
| `typography.fontSize.5xl` | `--text-5xl` | `3rem` | 48 |
| `typography.fontSize.6xl` | `--text-6xl` | `3.75rem` | 60 |
| `typography.fontSize.7xl` | `--text-7xl` | `4.5rem` | 72 |

**Fluid sizes (responsive `clamp()`)** — use for h1–h3 and lead; they scale with the viewport.

| Token | CSS var | Value |
|---|---|---|
| `typography.fluid.h1` | `--fluid-h1` | `clamp(2.25rem, 1.4rem + 4.25vw, 4.5rem)` |
| `typography.fluid.h2` | `--fluid-h2` | `clamp(1.875rem, 1.3rem + 2.9vw, 3rem)` |
| `typography.fluid.h3` | `--fluid-h3` | `clamp(1.5rem, 1.2rem + 1.5vw, 2.25rem)` |
| `typography.fluid.lead` | `--fluid-lead` | `clamp(1.125rem, 1.05rem + 0.4vw, 1.375rem)` |

**Line-height / letter-spacing / measure**

| Token | CSS var | Value | Note |
|---|---|---|---|
| `typography.lineHeight.tight` | `--lh-tight` | `1.1` | Display headings |
| `typography.lineHeight.snug` | `--lh-snug` | `1.25` | |
| `typography.lineHeight.normal` | `--lh-normal` | `1.5` | Body — WCAG min |
| `typography.lineHeight.relaxed` | `--lh-relaxed` | `1.65` | Long-form prose |
| `typography.letterSpacing.tighter` | `--ls-tighter` | `-0.02em` | Large display |
| `typography.letterSpacing.tight` | `--ls-tight` | `-0.01em` | |
| `typography.letterSpacing.normal` | `--ls-normal` | `0em` | |
| `typography.letterSpacing.wide` | `--ls-wide` | `0.02em` | Eyebrows/labels |
| `typography.measure.prose` | `--measure-prose` | `68ch` | Max line length (45–75ch) |

### 5.3 Spacing (4px base)

| Token | CSS var | Value | px |
|---|---|---|---|
| `space.0` | `--space-0` | `0` | 0 |
| `space.1` | `--space-1` | `0.25rem` | 4 |
| `space.2` | `--space-2` | `0.5rem` | 8 |
| `space.3` | `--space-3` | `0.75rem` | 12 |
| `space.4` | `--space-4` | `1rem` | 16 |
| `space.5` | `--space-5` | `1.25rem` | 20 |
| `space.6` | `--space-6` | `1.5rem` | 24 |
| `space.8` | `--space-8` | `2rem` | 32 |
| `space.10` | `--space-10` | `2.5rem` | 40 |
| `space.12` | `--space-12` | `3rem` | 48 |
| `space.16` | `--space-16` | `4rem` | 64 |
| `space.20` | `--space-20` | `5rem` | 80 |
| `space.24` | `--space-24` | `6rem` | 96 |
| `space.32` | `--space-32` | `8rem` | 128 — section rhythm |

### 5.4 Radius

| Token | CSS var | Value | Note |
|---|---|---|---|
| `radius.sm` | `--radius-sm` | `0.375rem` | 6px |
| `radius.md` | `--radius-md` | `0.5rem` | 8px — default control |
| `radius.lg` | `--radius-lg` | `0.75rem` | 12px — cards |
| `radius.xl` | `--radius-xl` | `1rem` | 16px |
| `radius.2xl` | `--radius-2xl` | `1.5rem` | 24px — hero panels |
| `radius.full` | `--radius-full` | `9999px` | Pills / avatars |

### 5.5 Shadow

| Token | CSS var | Value |
|---|---|---|
| `shadow.xs` | `--shadow-xs` | `0 1px 2px 0 rgb(11 17 32 / 0.05)` |
| `shadow.sm` | `--shadow-sm` | `0 1px 3px …, 0 1px 2px -1px …` |
| `shadow.md` | `--shadow-md` | `0 4px 6px -1px …, 0 2px 4px -2px …` |
| `shadow.lg` | `--shadow-lg` | `0 10px 15px -3px …, 0 4px 6px -4px …` |
| `shadow.xl` | `--shadow-xl` | `0 20px 25px -5px …, 0 8px 10px -6px …` |
| `shadow.focus` | `--shadow-focus` | `0 0 0 3px rgb(79 70 229 / 0.45)` |

### 5.6 Breakpoints & layout

| Token | CSS var | Value | Note |
|---|---|---|---|
| `breakpoint.sm` | _(Tailwind `screens.sm`)_ | `640px` | Large phone / small tablet |
| `breakpoint.md` | | `768px` | Tablet portrait |
| `breakpoint.lg` | | `1024px` | Tablet landscape / small laptop |
| `breakpoint.xl` | | `1280px` | Desktop |
| `breakpoint.2xl` | | `1536px` | Large desktop |
| `container.prose` | `--measure-prose` / `maxWidth.prose` | `68ch` | Prose measure |
| `container.content` | `--container-content` | `1200px` | Max content width |
| `container.wide` | `--container-wide` | `1440px` | Wide/edge layouts |
| `container.gutter` | `--gutter` | `clamp(1rem, 5vw, 2rem)` | Page side padding |

> Breakpoints are exposed to Tailwind as `screens.*` and used in CSS media queries. See [`layout-and-grid.md`](./layout-and-grid.md) for how these are applied.

### 5.7 z-index

| Token | CSS var | Value |
|---|---|---|
| `zIndex.base` | _(0, implicit)_ | `0` |
| `zIndex.dropdown` | `--z-dropdown` | `1000` |
| `zIndex.sticky` | `--z-sticky` | `1100` |
| `zIndex.overlay` | `--z-overlay` | `1200` |
| `zIndex.modal` | `--z-modal` | `1300` |
| `zIndex.toast` | `--z-toast` | `1400` |
| `zIndex.tooltip` | `--z-tooltip` | `1500` |

### 5.8 Motion

| Token | CSS var | Value | Note |
|---|---|---|---|
| `motion.duration.instant` | `--duration-instant` | `100ms` | |
| `motion.duration.fast` | `--duration-fast` | `150ms` | Hovers, small state |
| `motion.duration.base` | `--duration-base` | `200ms` | |
| `motion.duration.slow` | `--duration-slow` | `300ms` | Enter/exit |
| `motion.duration.slower` | `--duration-slower` | `500ms` | Large transitions |
| `motion.easing.standard` | `--ease-standard` | `cubic-bezier(0.4, 0, 0.2, 1)` | Default |
| `motion.easing.decelerate` | `--ease-decelerate` | `cubic-bezier(0, 0, 0.2, 1)` | Entering |
| `motion.easing.accelerate` | `--ease-accelerate` | `cubic-bezier(0.4, 0, 1, 1)` | Exiting |
| `motion.easing.spring` | `--ease-spring` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | Overshoot — use sparingly |

> `motion.reducedMotion` is a **note token**, not a value: all non-essential motion MUST be gated behind `@media (prefers-reduced-motion: no-preference)`. `tokens.css` ships a global reduce-motion reset.

### 5.9 Opacity & targets

| Token | CSS var | Value | Note |
|---|---|---|---|
| `opacity.disabled` | `--opacity-disabled` | `0.5` | |
| `opacity.muted` | `--opacity-muted` | `0.7` | |
| `opacity.backdrop` | `--opacity-backdrop` | `0.6` | Modal scrim |
| `target.minTouch` | `--target-min` | `44px` | Comfortable touch target (WCAG min 24px) |
| `target.minTouchSpacing` | `--target-spacing` | `8px` | Min spacing between targets |

---

## 6. Quick reference — the everyday tokens

- [ ] **Primary button:** `--cta-bg` / `--cta-bg-hover` / `--cta-text`; `--radius-md`; `min-height: var(--target-min)`.
- [ ] **Body text:** `--text` (or `--text-secondary`); `--font-body`; `--text-base`; `--lh-normal`.
- [ ] **Headings:** `--font-display`; `--fluid-h1/2/3`; `--lh-tight`; `--ls-tight`.
- [ ] **Card:** `--bg`; `--radius-lg`; `--shadow-md`; padding `--space-6`.
- [ ] **Section rhythm:** vertical padding `--space-24`/`--space-32`; inner max `--container-content`; side `--gutter`.
- [ ] **Muted text floor:** never lighter than `--text-muted` (`neutral-500`) for real text.
- [ ] **Input border:** `--border-interactive` (never `--border`, which fails 3:1).
- [ ] **Transition:** `var(--duration-fast) var(--ease-standard)`; gate anything decorative behind reduced-motion.

---

## Related

- [`layout-and-grid.md`](./layout-and-grid.md) — how containers, grid, and spacing tokens are applied to page layout.
- [`../brand/color-system.md`](../brand/color-system.md) — canonical colour & contrast rules (raw hex allowed there).
- [`../brand/typography.md`](../brand/typography.md) — type scale application, pairing, and specimens.
- [`../accessibility/contrast-matrix.md`](../accessibility/contrast-matrix.md) — validated colour pairings and ratios.
- [`../00-foundations/principles.md`](../00-foundations/principles.md) — the design principles these tokens encode.
- [`../../tokens/design-tokens.json`](../../tokens/design-tokens.json) — **source of truth** for all values.
- [`../../tokens/tokens.css`](../../tokens/tokens.css) — generated CSS custom properties.
- [`../../tokens/tailwind.tokens.js`](../../tokens/tailwind.tokens.js) — generated Tailwind theme extension.
