# Contrast Matrix

**Purpose:** The definitive, machine-verified contrast reference for every approved foreground/background colour pair — measured ratio, WCAG grade, and allowed usage — so no page ever ships a failing pairing.
**Status:** v1 foundation — adjustable.

---

> **This is a canonical contrast doc, so raw hex values ARE allowed here.** Everywhere else, reference colours by token name (`--color-brand-600`, not `#4F46E5`).
> **Source of truth for values:** [`tokens/design-tokens.json`](../../tokens/design-tokens.json). **Operating rules:** [`docs/accessibility/accessibility-standards.md`](./accessibility-standards.md).
> All ratios below were computed and validated **2026-07-01**. If a token value changes, re-run the script (§ Method) and update this file.

---

## 0. TL;DR — the rules you will break by accident

- [ ] **Text needs ≥4.5:1** (normal) or **≥3:1** (large: ≥18pt/24px regular, ≥14pt/18.66px bold). We target **AAA (7:1)** for body/secondary text — the palette already delivers it.
- [ ] **UI/non-text needs ≥3:1** (borders, focus rings, toggles, meaningful icons).
- [ ] **Never white text on teal `#06B6D4` (accent-500)** — 2.43:1, FAILS. Use **ink on teal-500** or **white on teal-700**.
- [ ] **Never white text on warning `#D97706`** for normal text — 3.19:1. Use **ink on warning**.
- [ ] **`neutral-400 #94A3B8` is disabled/hint ONLY** — 2.56:1 on white, never real text.
- [ ] **`success #16A34A` white text is large/UI only** — 3.30:1. Use **`success-strong #15803D`** (5.02:1) for normal white text.

---

## 1. Method (how these numbers are produced)

- Ratios use the **WCAG 2.x relative-luminance formula**: linearize each sRGB channel, compute `L = 0.2126R + 0.7152G + 0.0722B`, then `(L_light + 0.05) / (L_dark + 0.05)`.
- Grades: **AA** = 4.5:1 normal / 3:1 large; **AAA** = 7:1 normal / 4.5:1 large; **UI/non-text** threshold = 3:1 (1.4.11).
- **Re-verify any time a colour token changes:** run [`scripts/verify-contrast.py`](../../scripts/verify-contrast.py) (stdlib only, no dependencies). `--strict` exits non-zero if any required pair drops below threshold. Keep this file in sync with its output.

```bash
python3 scripts/verify-contrast.py            # human-readable table
python3 scripts/verify-contrast.py --strict   # CI gate: fail on regression
```

---

## 2. Text on light (white `#FFFFFF`) backgrounds

| Foreground | Hex | Ratio | Grade | Allowed usage |
| --- | --- | --- | --- | --- |
| neutral-ink | `#0B1120` | **18.83** | AAA | Primary text / headings. Default text colour. |
| neutral-900 | `#0F172A` | **17.85** | AAA | Headings. |
| neutral-700 | `#334155` | **10.35** | AAA | **Body text** (default paragraph colour). |
| neutral-600 | `#475569` | **7.58** | AAA | **Secondary text**, captions, meta. |
| neutral-500 | `#64748B` | **4.76** | AA | **Minimum muted text** on white. Do not go lighter for text. |
| neutral-400 | `#94A3B8` | **2.56** | **FAIL** | **Disabled / placeholder hint ONLY.** Never meaningful text. |
| brand-600 | `#4F46E5` | **6.29** | AA | **Links / primary-text accent** on light. |
| brand-700 | `#4338CA` | **7.90** | AAA | **Link hover/active** on light. |

## 3. White text on brand / semantic buttons (light-on-colour)

| Background | Hex | Ratio (white FG) | Grade | Allowed usage |
| --- | --- | --- | --- | --- |
| brand-600 | `#4F46E5` | **6.29** | AA | **PRIMARY button** background (white label). Default CTA. |
| brand-700 | `#4338CA` | **7.90** | AAA | Primary button **hover/active**. |
| accent-700 (teal) | `#0E7490` | **5.36** | AA | White-safe teal button/badge with **white** text. |
| success | `#16A34A` | **3.30** | AA (large/UI only) | White text only on **large text or UI** (icons, ≥24px). |
| success-strong | `#15803D` | **5.02** | AA | **Normal white text** success state. |
| danger | `#DC2626` | **4.83** | AA | Destructive button / error banner, white text. |
| info | `#2563EB` | **5.17** | AA | Info button / banner, white text. |
| warning | `#D97706` | **3.19** | **FAIL (normal text)** | White text only for large/UI; **use ink for normal text** (see §5). |

## 4. Ink text on accent / semantic fills (dark-on-colour)

| Background | Hex | Ratio (ink FG `#0B1120`) | Grade | Allowed usage |
| --- | --- | --- | --- | --- |
| accent-500 (teal) | `#06B6D4` | **7.76** | AAA | **Correct teal usage** — ink label on teal fill. |
| warning | `#D97706` | **5.91** | AA | **Correct warning usage** — ink text on amber. |

## 5. Text on dark surfaces (ink `#0B1120` background)

| Foreground | Hex | Ratio | Grade | Allowed usage |
| --- | --- | --- | --- | --- |
| white | `#FFFFFF` | **18.83** | AAA | Primary text on dark sections. |
| neutral-300 | `#CBD5E1` | **12.68** | AAA | **Muted text on dark** (default secondary on dark). |
| neutral-400 | `#94A3B8` | **7.34** | AAA | Secondary muted text on dark (note: on dark it passes; on white it does NOT). |
| brand-300 | `#A5B4FC` | **9.45** | AAA | **Brand accent text on dark** (links/highlights on ink). |

## 6. Non-text / UI component contrast (1.4.11 AA, ≥3:1)

| Element | Colour | Against | Ratio | Grade | Note |
| --- | --- | --- | --- | --- | --- |
| Interactive border (inputs/controls) | neutral-500 `#64748B` | white | **4.76** | Pass (≥3:1) | **Minimum** interactive border. neutral-200/300 are decorative only, not meaningful borders. |
| Focus ring | brand-600 `#4F46E5` | white | **6.29** | Pass (≥3:1) | Focus indicator vs adjacent light bg; pair with 2px offset. |

---

## 7. Never-do list (forbidden pairings)

| ❌ Never | Ratio | Why | ✅ Do instead |
| --- | --- | --- | --- |
| White text on **accent-500 teal** `#06B6D4` | 2.43:1 | Fails all text contrast | **Ink** on teal-500, or **white on accent-700** `#0E7490` (5.36:1). |
| White text on **warning** `#D97706` (normal text) | 3.19:1 | Fails normal-text 4.5:1 | **Ink** on warning (5.91:1); white only for large/UI. |
| **neutral-400** `#94A3B8` as body/meaningful text on white | 2.56:1 | Fails; disabled/hint only | Use **neutral-500** (4.76:1) min, **neutral-700** for body. |
| White text on **success** `#16A34A` for normal text | 3.30:1 | Large/UI only | **success-strong** `#15803D` (5.02:1) for normal text. |
| **neutral-200/300** as a meaningful/visible border | ~1.2:1 | Decorative divider only, not perceivable as a control edge | **neutral-500** for interactive borders (≥3:1). |
| Any colour-only meaning (no icon/text) | n/a | Fails 1.4.1 Use of Color | Pair colour with icon + text. |

---

## 8. Quick-reference cheat sheet

| Need | Use |
| --- | --- |
| Body text on white | `--color-neutral-700` (10.35 AAA) |
| Secondary text on white | `--color-neutral-600` (7.58 AAA) |
| Min muted text on white | `--color-neutral-500` (4.76 AA) — never lighter |
| Link on white / hover | `--color-brand-600` (6.29) / `--color-brand-700` (7.90) |
| Primary button | white on `--color-brand-600` (6.29); hover `--color-brand-700` (7.90) |
| Teal with white text | `--color-accent-700` (5.36) — **not** accent-500 |
| Teal with ink text | `--color-accent-500` (7.76) |
| Success (normal white text) | `--color-semantic-successStrong` (5.02) |
| Warning text | ink on `--color-semantic-warning` (5.91) |
| Danger / Info button | white on `--color-semantic-danger` (4.83) / `--color-semantic-info` (5.17) |
| Text on dark (ink) section | white (18.83), muted `--color-neutral-300` (12.68), brand accent `--color-brand-300` (9.45) |
| Interactive border / focus ring | `--color-neutral-500` (4.76) / `--color-brand-600` (6.29) — both ≥3:1 |

---

## Related

- [`docs/accessibility/accessibility-standards.md`](./accessibility-standards.md) — WCAG 2.2 AA operating standard and per-page checklist.
- [`docs/brand/color-system.md`](../brand/color-system.md) — canonical colour usage and pairing rules.
- [`tokens/design-tokens.json`](../../tokens/design-tokens.json) — source of truth for all colour values.
- [`scripts/verify-contrast.py`](../../scripts/verify-contrast.py) — re-verify this matrix after any token change.
