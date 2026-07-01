# Colour System

**Purpose:** The definitive, WCAG-2.2-validated colour usage guide — full palette, ROLE tokens, strict pairing rules, and a copy-paste cheat-sheet — so any developer or future Claude session applies colour correctly and never ships a failing contrast.
**Status:** v1 foundation — adjustable.

---

> **Source of truth:** raw values live in [`tokens/design-tokens.json`](../../tokens/design-tokens.json) and are exposed to code as CSS custom properties in [`tokens/tokens.css`](../../tokens/tokens.css). Full pairing evidence lives in [`docs/accessibility/contrast-matrix.md`](../accessibility/contrast-matrix.md).
>
> **This is a canonical colour doc, so raw hex values ARE allowed here.** Everywhere else (components, other docs), reference colours by **token name** (`--color-brand-600`, not `#4F46E5`). Never hardcode hex in product code.
>
> All ratios below are computed against the WCAG 2.x relative-luminance formula and validated `2026-07-01`. If a token value changes, re-run the matrix and update this file.

---

## 0. TL;DR — the rules you will break by accident

- [ ] **Primary is brand indigo `--color-brand-600` (`#4F46E5`).** White text on it = 6.29:1 (AA). Hover is `--color-brand-700` (7.90:1, AAA).
- [ ] **Teal `--color-accent-500` (`#06B6D4`) is INK-text-only (7.76:1).** White on it FAILS (2.43:1). For white-text teal, use `--color-accent-700` (`#0E7490`, 5.36:1).
- [ ] **Minimum muted text = `--color-neutral-500` (`#64748B`, 4.76:1).** Never go lighter for real text.
- [ ] **`--color-neutral-400` (`#94A3B8`) is disabled/hint ONLY** (2.56:1 — fails as text; that's allowed only because disabled controls are exempt).
- [ ] **`--color-neutral-200/300` are decorative dividers ONLY** (1.23:1 / 1.48:1 — not perceivable borders).
- [ ] **Minimum interactive/meaningful border = `--color-neutral-500`** (3:1 non-text contrast). Inputs, control outlines, focus rings.
- [ ] **Warning `--color-warning` (`#D97706`) uses INK text** (5.91:1). White on it FAILS normal text (3.19:1).
- [ ] **Success with white text uses `--color-success-strong` (`#15803D`, 5.02:1).** Plain `--color-success` (`#16A34A`) + white = 3.30:1 → large text / non-text UI only.
- [ ] **Never convey meaning by colour alone** (WCAG 1.4.1). Errors, statuses, links-in-body get an icon, underline, or text label too.

---

## 1. Full palette (with hex)

### Brand — indigo (primary identity)

| Token | Hex | Role |
|---|---|---|
| `--color-brand-50` | `#EEF2FF` | Tint background, hover on light surfaces |
| `--color-brand-100` | `#E0E7FF` | Subtle fills, badges |
| `--color-brand-200` | `#C7D2FE` | Accent text **on dark** (12.62:1 on ink) |
| `--color-brand-300` | `#A5B4FC` | Link/accent text **on dark** (9.45:1 on ink) |
| `--color-brand-400` | `#818CF8` | Decorative, gradients |
| `--color-brand-500` | `#6366F1` | Decorative, gradients (do **not** use for white-text buttons) |
| **`--color-brand-600`** | **`#4F46E5`** | **PRIMARY.** Default CTA, links on light, brand marks. White text = 6.29:1 AA |
| `--color-brand-700` | `#4338CA` | Primary hover/active. White text = 7.90:1 AAA |
| `--color-brand-800` | `#3730A3` | Pressed, dark accents |
| `--color-brand-900` | `#312E81` | Deep brand backgrounds |

### Accent — teal (highlight, secondary)

| Token | Hex | Role |
|---|---|---|
| `--color-accent-400` | `#22D3EE` | Decorative / highlight only |
| **`--color-accent-500`** | **`#06B6D4`** | **ACCENT.** Highlights, chips, underlines. **INK text only (7.76:1). NEVER white (2.43:1 FAIL).** |
| `--color-accent-600` | `#0891B2` | Hover for ink-on-teal fills |
| `--color-accent-700` | `#0E7490` | **The only teal you may put white text on** (5.36:1 AA) |

### Neutral — slate ramp (text, surfaces, borders)

| Token | Hex | Role | On-white ratio |
|---|---|---|---|
| `--color-white` | `#FFFFFF` | Page background, text-on-dark | — |
| `--color-neutral-50` | `#F8FAFC` | Subtle section background | — |
| `--color-neutral-100` | `#F1F5F9` | Cards on white, hover fills | — |
| `--color-neutral-200` | `#E2E8F0` | **Decorative divider ONLY** | 1.23:1 |
| `--color-neutral-300` | `#CBD5E1` | **Decorative divider ONLY** | 1.48:1 |
| `--color-neutral-400` | `#94A3B8` | **Disabled / placeholder hint ONLY** | 2.56:1 |
| `--color-neutral-500` | `#64748B` | **MIN muted text; MIN interactive border** | 4.76:1 |
| `--color-neutral-600` | `#475569` | Secondary text | 7.58:1 |
| `--color-neutral-700` | `#334155` | Body text | 10.35:1 |
| `--color-neutral-800` | `#1E293B` | Strong text, dark UI | — |
| `--color-neutral-900` | `#0F172A` | Headings | 17.85:1 |
| `--color-ink` | `#0B1120` | Primary text / dark sections | 18.83:1 |

### Semantic — status colours

| Token | Hex | White-text ratio | Text rule |
|---|---|---|---|
| `--color-success` | `#16A34A` | 3.30:1 | **White = large text / UI only.** Icon fills, badges ≥18px bold. |
| `--color-success-strong` | `#15803D` | 5.02:1 | **Use this for normal white text** on success surfaces. |
| `--color-warning` | `#D97706` | 3.19:1 (FAIL) | **INK text only** (5.91:1). Never white on normal text. |
| `--color-danger` | `#DC2626` | 4.83:1 | White text AA. Errors, destructive actions. |
| `--color-info` | `#2563EB` | 5.17:1 | White text AA. Informational banners. |

---

## 2. ROLE tokens (use these in components, not raw scales)

Prefer semantic role aliases; they encode the correct pairing and let `.surface-dark` remap without touching component code.

| Role token (CSS) | Resolves to | Ratio vs its background | Use |
|---|---|---|---|
| `--text` | `--color-ink` `#0B1120` | 18.83:1 on white | Primary body & heading text |
| `--text-secondary` | `--color-neutral-600` `#475569` | 7.58:1 on white | Supporting / secondary text |
| `--text-muted` | `--color-neutral-500` `#64748B` | 4.76:1 on white | **Smallest allowed muted text** — captions, meta |
| `--text-on-dark` | `--color-white` | 18.83:1 on ink | Text on dark sections |
| `--text-muted-on-dark` | `--color-neutral-300` `#CBD5E1` | 12.68:1 on ink | Muted text on dark |
| `--link` | `--color-brand-600` `#4F46E5` | 6.29:1 on white | Inline links on light |
| `--link-hover` | `--color-brand-700` `#4338CA` | 7.90:1 on white | Link hover/active |
| `--bg` | `--color-white` | — | Page background |
| `--bg-subtle` | `--color-neutral-50` `#F8FAFC` | — | Alternating sections |
| `--bg-dark` | `--color-ink` `#0B1120` | — | Dark hero / footer |
| `--border` | `--color-neutral-200` `#E2E8F0` | 1.23:1 | **Decorative** dividers only |
| `--border-interactive` | `--color-neutral-500` `#64748B` | 3:1+ vs white | Inputs, controls, meaningful boundaries |
| `--focus-ring` | `--color-brand-600` `#4F46E5` | 6.29:1 vs white | Focus indicator (pair with 2px offset) |
| `--cta-bg` | `--color-brand-600` `#4F46E5` | — | Primary button fill |
| `--cta-bg-hover` | `--color-brand-700` `#4338CA` | — | Primary button hover |
| `--cta-text` | `--color-white` | 6.29:1 on cta-bg | Primary button label |

> **Border tiers, do not confuse them:**
> - `--border` (`neutral-200`) = **decorative only**. Card edges where the boundary is cosmetic and reinforced by shadow/fill.
> - `--border-interactive` (`neutral-500`) = **required** for anything that must be *perceived* as an edge or state: text inputs, checkboxes, selects, segmented controls, focus outlines. Meets WCAG 1.4.11 Non-text Contrast (3:1).

---

## 3. Strict usage rules (derived from contrast validation)

These are non-negotiable. Each maps to a WCAG 2.2 AA success criterion.

| # | Rule | Why (WCAG) |
|---|---|---|
| R1 | **Muted text ≥ `--color-neutral-500`** (`#64748B`, 4.76:1). Never `neutral-400` or lighter for text a user must read. | 1.4.3 Contrast (Min) 4.5:1 |
| R2 | **`--color-neutral-400` (`#94A3B8`) is disabled/placeholder-hint ONLY.** Disabled controls are contrast-exempt; do not exploit that for active text. | 1.4.3 exception (inactive) |
| R3 | **`--color-neutral-200/300` are decorative dividers ONLY.** If a border must be perceived, it's `--color-neutral-500` or darker. | 1.4.11 Non-text 3:1 |
| R4 | **Teal `--color-accent-500` carries INK text only.** White on `accent-500` = 2.43:1 → banned. | 1.4.3 |
| R5 | **White text on teal must use `--color-accent-700`** (`#0E7490`, 5.36:1). | 1.4.3 |
| R6 | **Interactive/meaningful borders ≥ `--color-neutral-500`** (3:1). Inputs, toggles, control outlines, dividers that convey grouping. | 1.4.11 |
| R7 | **Warning uses INK text** (`#0B1120` on `#D97706` = 5.91:1). White on warning = 3.19:1 → banned for normal text. | 1.4.3 |
| R8 | **Success + white text uses `--color-success-strong`** (5.02:1). Plain `--color-success` + white (3.30:1) is large-text / icon-UI only. | 1.4.3 / 1.4.11 |
| R9 | **Primary CTA is brand indigo, never teal-with-white.** Do not use `brand-500` for white-text buttons (fails). | Brand + 1.4.3 |
| R10 | **Never rely on colour alone.** Links get underline or clear affordance; statuses get icon + text; errors get text, not just red. | 1.4.1 Use of Colour |
| R11 | **Focus is always visible.** Never `outline: none` without a replacement ≥3:1 vs adjacent. | 2.4.7 / 2.4.13 |
| R12 | **Focus must not be fully obscured** by sticky headers, cookie/chat widgets — add `scroll-margin`. | 2.4.11 Focus Not Obscured (Min) AA |

---

## 4. Colour pairing cheat-sheet

Foreground on background → measured ratio → what it's cleared for. **PASS AA** = ≥4.5:1 normal / ≥3:1 large or non-text. **AAA** = ≥7:1 normal.

### Text on light surfaces (white `#FFFFFF`)

| Foreground | Ratio | Allowed use |
|---|---|---|
| `--color-ink` `#0B1120` | 18.83:1 | ✅ AAA — all text, any size |
| `--color-neutral-900` `#0F172A` | 17.85:1 | ✅ AAA — headings, all text |
| `--color-neutral-700` `#334155` | 10.35:1 | ✅ AAA — body text |
| `--color-neutral-600` `#475569` | 7.58:1 | ✅ AAA — secondary text |
| `--color-neutral-500` `#64748B` | 4.76:1 | ✅ AA — **min muted text**, captions, meta |
| `--color-brand-600` `#4F46E5` | 6.29:1 | ✅ AA — links, brand text |
| `--color-brand-700` `#4338CA` | 7.90:1 | ✅ AAA — link hover, emphasis |
| `--color-neutral-400` `#94A3B8` | 2.56:1 | ❌ FAIL — **disabled/hint only**, never real text |
| `--color-accent-500` `#06B6D4` | 2.43:1 | ❌ FAIL — never text on white (decorative fills only) |

### White text on coloured fills

| Background | Ratio (white fg) | Allowed use |
|---|---|---|
| `--color-brand-600` `#4F46E5` | 6.29:1 | ✅ AA — **primary CTA**, any text size |
| `--color-brand-700` `#4338CA` | 7.90:1 | ✅ AAA — CTA hover |
| `--color-accent-700` `#0E7490` | 5.36:1 | ✅ AA — the only white-text teal |
| `--color-info` `#2563EB` | 5.17:1 | ✅ AA — info banners |
| `--color-success-strong` `#15803D` | 5.02:1 | ✅ AA — success normal text |
| `--color-danger` `#DC2626` | 4.83:1 | ✅ AA — errors, destructive |
| `--color-success` `#16A34A` | 3.30:1 | ⚠️ Large text (≥24px / ≥18.66px bold) & UI icons only |
| `--color-warning` `#D97706` | 3.19:1 | ❌ FAIL for normal text → **use ink text instead** |
| `--color-accent-500` `#06B6D4` | 2.43:1 | ❌ FAIL — never white on teal-500 |

### Ink text on coloured fills

| Background | Ratio (ink fg) | Allowed use |
|---|---|---|
| `--color-accent-500` `#06B6D4` | 7.76:1 | ✅ AAA — **teal chips/badges carry ink text** |
| `--color-warning` `#D97706` | 5.91:1 | ✅ AA — **warning badges carry ink text** |
| `--color-brand-50/100/200` | ≥12:1 | ✅ AAA — tint backgrounds |

### Text on dark surfaces (ink `#0B1120`)

| Foreground | Ratio | Allowed use |
|---|---|---|
| `--color-white` `#FFFFFF` | 18.83:1 | ✅ AAA — primary text on dark |
| `--color-neutral-300` `#CBD5E1` | 12.68:1 | ✅ AAA — muted text on dark |
| `--color-neutral-400` `#94A3B8` | 7.34:1 | ✅ AAA — smallest muted-on-dark (note: on dark, 400 is safe; on light it is NOT) |
| `--color-brand-200` `#C7D2FE` | 12.62:1 | ✅ AAA — accent/emphasis on dark |
| `--color-brand-300` `#A5B4FC` | 9.45:1 | ✅ AAA — **links on dark** |
| `--color-neutral-500` `#64748B` | 3.96:1 | ⚠️ Large text / UI only on dark |

### Non-text (borders, icons, focus) — needs ≥3:1

| Element | On | Colour | Ratio | Verdict |
|---|---|---|---|---|
| Input / control border | white | `--color-neutral-500` | 4.76:1 | ✅ PASS 1.4.11 |
| Focus ring | white | `--color-brand-600` | 6.29:1 | ✅ PASS |
| Decorative divider | white | `--color-neutral-200` | 1.23:1 | ✅ OK (decorative, exempt) |
| "Border" as real edge | white | `--color-neutral-200/300` | ≤1.48:1 | ❌ FAIL — use `neutral-500` |

---

## 5. Component quick-reference (correct pairings)

| Component | Background | Text | Border | Notes |
|---|---|---|---|---|
| Primary button | `--cta-bg` (brand-600) | white | none | Hover → `--cta-bg-hover` (brand-700) |
| Secondary button | white | `--color-brand-600` | `--color-brand-600` (1.5px) | Border is the affordance |
| Teal accent chip | `--color-accent-500` | **ink** | none | Never white text |
| Text input | white | `--color-ink` | `--border-interactive` (neutral-500) | Placeholder = `neutral-400` |
| Disabled control | `--color-neutral-100` | `--color-neutral-400` | `--color-neutral-300` | Exempt from contrast |
| Success toast | `--color-success-strong` | white | none | Plain success only for icon badges |
| Warning toast | `--color-warning` | **ink** | none | White text banned |
| Error toast | `--color-danger` | white | none | Add error icon + text (R10) |
| Info banner | `--color-info` | white | none | — |
| Link (inline, light) | inherit | `--color-brand-600` | — | Underline or clear affordance |
| Link (inline, dark) | inherit | `--color-brand-300` | — | 9.45:1 on ink |

---

## 6. Light & dark surface guidance

### Light (default)

Page `--bg` (white) or `--bg-subtle` (`neutral-50`) for alternating sections. Text uses `--text` / `--text-secondary` / `--text-muted`. This is the primary surface for the whole site.

### Dark sections — `.surface-dark`

Apply the `.surface-dark` class (defined in [`tokens/tokens.css`](../../tokens/tokens.css)) to a section to remap role tokens for a dark background **without editing component internals**. It rebinds:

```css
.surface-dark {
  --text: var(--color-white);            /* 18.83:1 on ink */
  --text-secondary: var(--color-neutral-300); /* 12.68:1 */
  --text-muted: var(--color-neutral-400);     /* 7.34:1 — safe on dark, NOT on light */
  --link: var(--color-brand-300);        /* 9.45:1 on ink */
  --link-hover: var(--color-brand-200);  /* 12.62:1 on ink */
  --bg: var(--color-ink);
  --border: rgb(255 255 255 / 0.12);     /* subtle divider */
  color: var(--text);
  background-color: var(--bg);
}
```

**Dark-surface rules:**

- [ ] **`neutral-400` flips meaning by surface.** On light it's disabled-only (2.56:1). On dark (`.surface-dark`) it's valid muted text (7.34:1). Only trust it inside `.surface-dark`.
- [ ] **Links on dark use `brand-300`, not `brand-600`.** `brand-600` on ink is too low-contrast.
- [ ] **Primary CTAs stay brand-600 with white text** on dark too (the button fills its own background; contrast is button-internal, 6.29:1).
- [ ] **Teal on dark:** `accent-500` fills still carry **ink** text; for teal text on a dark background use `accent-400` decoratively, not as body text.
- [ ] **Meaningful borders on dark** need ≥3:1 vs the dark bg — use `rgb(255 255 255 / 0.24)` or `--color-neutral-500`, not the 0.12 decorative divider.

---

## 7. Do / Don't

| Do | Don't |
|---|---|
| Use `--color-brand-600` for primary CTAs | Use teal `accent-500` with white text |
| Put **ink** text on teal chips/badges | Put white text on `accent-500` (2.43:1) |
| Use `--color-accent-700` when you need white-on-teal | Use `accent-500` and hope it passes |
| Stop muted text at `--color-neutral-500` | Use `neutral-400` for readable text |
| Use `--color-neutral-500`+ for real borders | Use `neutral-200/300` as perceivable borders |
| Give warning surfaces **ink** text | Put white text on `--color-warning` |
| Use `--color-success-strong` for white text | Use plain `--color-success` for normal white text |
| Reinforce status with icon + text | Rely on colour alone (fails 1.4.1) |
| Keep a visible focus ring ≥3:1 | `outline: none` with no replacement |
| Reference tokens by name in code | Hardcode hex outside this canonical doc |

---

## 8. Verification checklist (before shipping any colour)

- [ ] Every text/background pair meets **4.5:1** (normal) or **3:1** (large ≥24px / ≥18.66px bold) — check against §4.
- [ ] Every meaningful border, icon, and focus ring meets **3:1** (1.4.11).
- [ ] No white text on `accent-500` or `warning`; no `neutral-400` as real text on light.
- [ ] Status/meaning is never colour-only (icon, label, or underline present).
- [ ] Focus indicator is visible and not obscured by sticky UI (2.4.11).
- [ ] Dark sections use `.surface-dark` remapped roles, not hand-picked hex.
- [ ] Pairing is recorded in [`docs/accessibility/contrast-matrix.md`](../accessibility/contrast-matrix.md) if it's new.

---

## Related

- [`brand-guidelines.md`](./brand-guidelines.md) — brand overview & index.
- [`typography.md`](./typography.md) — type system (colour × text pairings).
- [`imagery.md`](./imagery.md) — imagery direction & treatments.
- [`iconography.md`](./iconography.md) — icon colour & stroke.
- [`logo-and-usage.md`](./logo-and-usage.md) — logo colourways.
- [`../accessibility/contrast-matrix.md`](../accessibility/contrast-matrix.md) — full validated contrast evidence.
- [`../../tokens/design-tokens.json`](../../tokens/design-tokens.json) — source of truth for values.
- [`../../tokens/tokens.css`](../../tokens/tokens.css) — CSS custom properties consumed by code.
