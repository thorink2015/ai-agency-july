# Iconography

**Purpose:** The icon system for {{BRAND_NAME}} — which open-source set to use, the exact stroke/grid/colour rules, how to render icons (inline SVG vs sprite), sizing, accessibility (decorative vs meaningful), the emoji rule, and an SVGO optimization checklist so every icon ships tiny and consistent.
**Status:** v1 foundation — adjustable.

---

## TL;DR (extractable answer)

Use **[Lucide](https://lucide.dev)** (MIT, ~1,600 icons, actively maintained). Every icon: **24×24 grid, 1.5–2px stroke, rounded caps/joins, `stroke="currentColor"`, `fill="none"`, `viewBox="0 0 24 24"`.** Colour comes from CSS text colour — never hardcoded. Decorative icons get `aria-hidden="true"` + `focusable="false"`; meaningful icons get `role="img"` + `aria-label`. Render as **inline SVG** (icons are tiny, <1KB) or an **SVG sprite** for large repeated sets. **No emoji in product UI, marketing copy, or brand assets.** Optimize every SVG with **SVGO** (`removeViewBox: false`, `multipass: true`, `floatPrecision: 2`).

---

## 1. The set: Lucide

**Recommendation: [Lucide](https://lucide.dev)** — the community fork/successor of Feather, ISC/MIT-licensed, actively maintained, ~1,600 icons.

| Why Lucide | Detail |
|---|---|
| **On-brand geometry** | Rounded-but-crisp, consistent 24px grid, even stroke — matches our "modern-tech with warmth" direction. |
| **Consistent stroke** | Native 2px stroke, rounded caps and joins; easy to retune to 1.5px. |
| **License** | ISC (permissive, MIT-compatible). Safe for a commercial agency site. |
| **Delivery** | Ships as raw SVG, plus React/Vue/Svelte/web-component packages and a tree-shakeable icon-per-module build. |
| **currentColor by default** | Icons inherit text colour out of the box. |

**Rule: one set only.** Do not mix Lucide with Heroicons, Font Awesome, Material Symbols, or ad-hoc SVGs — mixed stroke weights and grids look cheap and break trust. If Lucide lacks an icon, **draw a new one on the 24px grid at the same stroke** (see §2) rather than importing a foreign set.

**Acceptable alternates** (if the team already standardizes on one — pick ONE, not several): Heroicons (MIT, 24px, outline/solid) or Phosphor (MIT, flexible weights). Lucide is the default.

---

## 2. Construction rules

Every icon — Lucide or custom — must satisfy these:

| Property | Value |
|---|---|
| Grid / canvas | **24 × 24** (`viewBox="0 0 24 24"`) |
| Stroke width | **1.5–2px** (default 2; use 1.5 for dense/small UI — be consistent per surface) |
| Stroke caps | `stroke-linecap="round"` |
| Stroke joins | `stroke-linejoin="round"` |
| Fill | `fill="none"` (outline style) |
| Colour | `stroke="currentColor"` — never a hardcoded hex |
| Live area | Keep artwork within the central ~20×20; ~2px padding to the edge |
| Optical alignment | Balance visual weight, not just bounding box; nudge for perceived centering |

**Canonical inline SVG shape:**

```html
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
     fill="none" stroke="currentColor" stroke-width="2"
     stroke-linecap="round" stroke-linejoin="round"
     aria-hidden="true" focusable="false">
  <!-- paths -->
</svg>
```

---

## 3. Colour

Icons take colour from **CSS `color`** via `currentColor`. Set colour with token-backed CSS, never inline hex.

- Default icon colour: `--color-role-text` (body ink). Muted/secondary: `--color-neutral-600` / `--color-neutral-500` (never below 500 for meaningful icons).
- Brand-accent icons: `--color-brand-600`. On dark surfaces use the remapped `.surface-dark` roles (`--color-neutral-0` / `--color-brand-300`), not hand-picked hex.
- **Meaningful icons must meet ≥3:1 contrast** against their background (WCAG 1.4.11) — see [`color-system.md`](./color-system.md). Decorative icons have no contrast requirement.
- **Never encode meaning in colour alone** — a red icon must also differ in shape/label. Pair status icons with text (see [`color-system.md`](./color-system.md) §7 checklist).

```css
.icon { width: 1.25rem; height: 1.25rem; color: var(--color-role-text); }
.icon--muted { color: var(--color-neutral-600); }
.icon--brand { color: var(--color-brand-600); }
```

---

## 4. Sizing

Icons scale by `width`/`height` (or `font-size` if `1em`-based). Keep them on the type/spacing scale.

| Token size | px | Use |
|---|---|---|
| `--space-4` | 16px | Inline with small/label text, dense tables |
| `1.25rem` | 20px | Default inline UI (buttons, list rows) |
| `--space-6` | 24px | Standalone UI, nav, section eyebrows |
| `--space-8` | 32px | Feature bullets, cards |
| `--space-10`+ | 40px+ | Marketing feature tiles (consider illustration instead) |

- **Optical stroke:** at 16px, a 2px stroke can look heavy — 1.5px reads cleaner; at 32px+, 2px is fine. Pick one stroke per surface and stay consistent.
- **Touch targets:** an icon-only button must have a **≥44px** hit area (WCAG comfortable target) with **≥8px** spacing, even if the glyph is 20–24px. Pad the button, not the icon. See `--target-minTouch` in tokens.
- Set explicit `width`/`height` on the `<svg>` to avoid layout shift.

---

## 5. Accessibility — decorative vs meaningful

The single most important icon rule. Decide **does this icon convey information the surrounding text doesn't?**

| Case | Markup | Notes |
|---|---|---|
| **Decorative** (adjacent visible text already says it) | `aria-hidden="true" focusable="false"` | Screen readers skip it. Most icons next to a label. |
| **Meaningful** (icon is the only label) | `role="img"` + `aria-label="…"` | e.g. an icon-only button. Label describes the **action/meaning**. |
| **Inside a labelled control** | icon `aria-hidden="true"`; label on the control | Put `aria-label` on the `<button>`, hide the icon. |
| **Standalone informational** | `role="img"` + `aria-label` (or `<title>`) | e.g. a status glyph with no text. |

```html
<!-- Decorative: text already says "Book a call" -->
<button>
  <svg aria-hidden="true" focusable="false"><!-- calendar --></svg>
  Book a call
</button>

<!-- Meaningful: icon-only button -->
<button aria-label="Close dialog">
  <svg aria-hidden="true" focusable="false"><!-- x --></svg>
</button>
```

- Always add `focusable="false"` to inline SVG (legacy IE/Edge would otherwise put SVGs in the tab order).
- Prefer labelling the **control** (`aria-label` on `<button>`) and hiding the icon — cleaner than `role="img"` on the SVG.
- If using `<title>` inside the SVG for a tooltip, still hide it from the a11y tree when the meaning is duplicated by visible text.

---

## 6. Rendering: inline SVG vs sprite

| Method | Use when | Trade-off |
|---|---|---|
| **Inline SVG** | Icons are small (<~5KB, ideally <1KB), few per page, need `currentColor`/per-instance styling | Simplest; not cached separately; bloats HTML if repeated a lot |
| **SVG sprite** (`<use href="#icon">`) | Same icon repeated many times, large icon library | One cached file; slightly more setup; still `currentColor`-able |
| **`<img src="icon.svg">`** | Icon is large/complex (illustration-grade, >~5KB) and reused | Cacheable; **loses `currentColor`** — can't recolor via CSS |
| **Icon font** | ❌ Do not use | Poor a11y, blurry rendering, FOUT, hard to style. Banned. |

**Guidance for {{BRAND_NAME}}:** inline SVG for the handful of icons in nav/hero (they're <1KB and want `currentColor`); an **SVG sprite** if a page uses many repeated icons. Externalize only genuinely large/complex illustrations as `<img>` for caching (see [`imagery.md`](./imagery.md) §5).

```html
<!-- Sprite usage -->
<svg class="icon" aria-hidden="true" focusable="false" width="24" height="24">
  <use href="/assets/icons/sprite.svg#calendar" />
</svg>
```

---

## 7. Emoji rule

**No emoji in {{BRAND_NAME}} product UI, marketing copy, headings, buttons, or brand assets.** Emoji render inconsistently across platforms, break the premium/calm-confidence tone, muddy accessibility (verbose/odd screen-reader output), and can't inherit brand colour or stroke.

| Context | Emoji? |
|---|---|
| Website UI, buttons, nav, headings | ❌ Never — use a Lucide icon |
| Marketing/body copy, blog | ❌ Never |
| Logo / brand assets | ❌ Never |
| Internal docs, commit messages, changelogs | ✅ Allowed (not user-facing) |
| Transactional SMS/email *to leads* | ⚠️ Avoid by default; only if a specific campaign is intentionally casual and approved |

Where you'd reach for an emoji (✅ ⚡ 📅 💬), use the matching Lucide icon (`check`, `zap`, `calendar-check`, `message-square`) so it inherits colour, stroke, and a11y handling.

---

## 8. Do / Don't

| Do | Don't |
|---|---|
| One icon set (Lucide) everywhere | Mix Lucide + Font Awesome + Material |
| 24px grid, 1.5–2px stroke, rounded caps | Mixed grids/strokes, sharp + round mixed |
| `stroke="currentColor"`, colour via CSS | Hardcode hex fills in the SVG |
| Draw missing icons on-grid at same stroke | Paste a foreign-style SVG to fill a gap |
| `aria-hidden` decorative / `aria-label` meaningful | Leave meaningful icon-only buttons unlabelled |
| ≥44px hit area on icon buttons | 24px tap targets with no padding |
| Run every icon through SVGO (§9) | Ship raw editor exports with metadata/junk |
| Pair status icons with text/shape | Convey status by colour alone |
| Icon fonts / emoji | Use either for UI |

---

## 9. SVG optimization checklist (SVGO)

Run **[SVGO](https://github.com/svg/svgo)** on every SVG in CI with a **committed `svgo.config.js`** — not ad-hoc. Icons must stay tiny (<1KB) and consistent.

```js
// svgo.config.js
module.exports = {
  multipass: true,
  floatPrecision: 2, // icons: 2 · illustrations: 3
  plugins: [
    {
      name: 'preset-default',
      params: {
        overrides: {
          removeViewBox: false,       // KEEP viewBox — required for scaling
          cleanupIds: false,          // keep sprite/<use> ids stable
          removeUnknownsAndDefaults: { keepRoleAttr: true }, // keep a11y roles
        },
      },
    },
    'removeDimensions',               // drop width/height, keep viewBox (set size in CSS)
    { name: 'sortAttrs' },
  ],
};
```

**Checklist per icon:**

- [ ] `viewBox="0 0 24 24"` preserved (`removeViewBox: false`).
- [ ] `stroke="currentColor"`, `fill="none"` — no hardcoded hex.
- [ ] `multipass: true`, `floatPrecision: 2` (icons) / `3` (illustrations).
- [ ] Metadata, editor cruft, comments, empty groups, and default attrs stripped.
- [ ] Accessibility attrs (`role`, `aria-*`) preserved (don't let SVGO delete them).
- [ ] IDs kept **only** if used by a sprite/`<use>` (else `cleanupIds` on).
- [ ] Result is **< 1KB** for a simple icon; inline if <~5KB, else externalize.
- [ ] Rounded caps/joins intact after optimization (`stroke-linecap`/`linejoin` present).
- [ ] SVGO runs in CI on commit, not manually.
- [ ] Renders identically before/after (visual diff a couple in the PR).

---

## 10. Pre-ship checklist (every icon)

- [ ] From Lucide (or custom-drawn on the 24px grid at matching stroke).
- [ ] 1.5–2px stroke, rounded caps/joins, `fill="none"`, `viewBox` present.
- [ ] `stroke="currentColor"`; colour set via token-backed CSS.
- [ ] Meaningful icons meet ≥3:1 contrast; status never colour-only.
- [ ] Sized on the scale; icon-only buttons have ≥44px hit area + ≥8px spacing.
- [ ] a11y decided: decorative `aria-hidden`+`focusable="false"`, or meaningful `role="img"`/`aria-label` (or label on the control).
- [ ] Rendered inline (small) or via sprite (repeated); no icon fonts, no emoji.
- [ ] Optimized through SVGO with the committed config (§9).

---

## Related

- [`brand-guidelines.md`](./brand-guidelines.md) — master brand overview & index.
- [`imagery.md`](./imagery.md) — illustration line-weight matches icon stroke; when to externalize SVGs.
- [`color-system.md`](./color-system.md) — icon colour roles, ≥3:1 rule for graphical objects, dark-surface remapping.
- [`logo-and-usage.md`](./logo-and-usage.md) — the logo symbol shares this 24px grid and stroke.
- [`typography.md`](./typography.md) — aligning icon size to the type scale.
- [`../accessibility/`](../accessibility/) — WCAG references for non-text contrast and labels.
- [`../../tokens/design-tokens.json`](../../tokens/design-tokens.json) — size, spacing, colour, and touch-target values referenced here.
- [`../../tokens/tokens.css`](../../tokens/tokens.css) — CSS custom properties consumed by code.
