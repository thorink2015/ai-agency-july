# Accessibility Standards

**Purpose:** The single operating standard for accessibility on the {{BRAND_NAME}} website — our target conformance level, a POUR summary, and a prescriptive, checkbox-driven checklist that any developer, marketer, or future Claude session can apply before shipping a page.
**Status:** v1 foundation — adjustable.

---

> **Source of truth for colour contrast:** [`docs/accessibility/contrast-matrix.md`](./contrast-matrix.md). This doc references contrast rules but never redefines ratios.
> **Source of truth for values:** [`tokens/design-tokens.json`](../../tokens/design-tokens.json). Reference tokens by name (`--color-brand-600`, `--space-4`), not raw hex.

---

## 0. TL;DR — the standard in one screen

- [ ] **Target level: WCAG 2.2 Level AA** on every public page, plus **AAA text contrast wherever feasible** (our palette already exceeds AA — see matrix).
- [ ] Build to **WCAG 2.2** (not 2.1) now to future-proof for EN 301 549 v4.1.1 and ADA/EAA enforcement. 2.2 is fully backward-compatible with 2.1.
- [ ] Every interactive thing is **keyboard-operable** with a **visible focus** indicator that is **never fully hidden** by sticky headers, cookie banners, or the chat widget.
- [ ] **Comfortable touch/click targets: 44×44 CSS px** (WCAG 2.5.8 minimum is 24×24; we standardize higher). Min 8px spacing.
- [ ] **Never** convey meaning by colour alone. **Never** use placeholder as the only label. **Never** `outline: none` without a replacement. **Never** block paste on password fields.
- [ ] All non-essential motion is gated behind `prefers-reduced-motion`.
- [ ] Every page ships only after passing the **[§16 per-page acceptance checklist](#16-per-page-a11y-acceptance-checklist)**.

Why this matters (2026 field data): **95.9%** of home pages have detectable WCAG failures; **low-contrast text is the #1 failure, on 83.9%** of pages. Most of these are trivially avoidable with the rules below.

---

## 1. Target conformance level

| Item | Our standard |
| --- | --- |
| Conformance target | **WCAG 2.2 Level AA** (all A + AA success criteria) |
| Text contrast | **AAA (7:1) wherever feasible**; AA (4.5:1) is the floor. Our palette meets AAA for body/secondary text. |
| Legal context | WCAG 2.1 AA is today's legal minimum (ADA/Section 508/EN 301 549). We exceed it by building to 2.2 AA. |
| Scope | All public marketing pages, forms, the embedded AI chat/booking widget, and any gated/portal UI. |

WCAG 2.2 was published as a W3C Recommendation on **5 October 2023**. It adds **9 new success criteria** over 2.1 and **removes 4.1.1 Parsing** (obsolete — modern browsers handle malformed markup). We do not chase AAA globally (some AAA criteria are impractical), but we take AAA where the design already delivers it.

---

## 2. POUR — the four principles (summary)

| Principle | Plain-language meaning | Where we address it |
| --- | --- | --- |
| **Perceivable** | Users can perceive the content (text alternatives, contrast, adaptable structure, not colour-alone). | §5 semantics, §9 contrast, §10 images, §11 media |
| **Operable** | Users can operate the UI by any input (keyboard, pointer, touch, AT), with enough time and no seizures. | §6 keyboard/focus, §7 targets, §11 motion, §12 skip link |
| **Understandable** | Content and operation are predictable; input errors are prevented and explained. | §8 colour meaning, §13 forms, §14 language, §15 WCAG 2.2 new SCs |
| **Robust** | Content works across browsers and assistive tech now and in future. | §5 semantic HTML, §17 ARIA, §18 testing |

---

## 3. What's new in WCAG 2.2 (know these — they trip up marketing sites)

| SC | Name | Level | One-line requirement |
| --- | --- | --- | --- |
| 2.4.11 | Focus Not Obscured (Minimum) | **AA** | Focused element must **not be entirely hidden** by author content (sticky header/footer, cookie banner, chat widget). |
| 2.4.12 | Focus Not Obscured (Enhanced) | AAA | Focused element **not obscured at all**. |
| 2.4.13 | Focus Appearance | AAA | Focus indicator has ≥3:1 contrast vs unfocused and covers ≥ a 2px-thick perimeter. |
| 2.5.7 | Dragging Movements | **AA** | Any drag action needs a **single-pointer, non-drag alternative**. |
| 2.5.8 | Target Size (Minimum) | **AA** | Pointer targets ≥ **24×24 CSS px** (or the spacing exception). |
| 3.2.6 | Consistent Help | A | If help mechanisms exist across pages, put them in the **same relative order/location**. |
| 3.3.7 | Redundant Entry | A | Don't ask users to **re-enter** info already given in the same process. |
| 3.3.8 | Accessible Authentication (Minimum) | **AA** | No cognitive-function test (memorize/transcribe/CAPTCHA) without an alternative. |
| 3.3.9 | Accessible Authentication (Enhanced) | AAA | As above, removing the object-recognition/user-media exceptions. |

> **Numbering note (do not get this wrong):** In the published standard, **2.4.11 = Focus Not Obscured (Minimum), Level AA** and **2.4.13 = Focus Appearance, Level AAA**. Focus Appearance was demoted from AA to AAA during drafting. The operative **AA-level "visible focus"** requirement is still the pre-existing **2.4.7 Focus Visible (AA)** from WCAG 2.0. Older drafts that call Focus Appearance "2.4.11/AA" are superseded — ignore them.

---

## 4. Prescriptive checklist (build-time)

Each subsection is a copy-paste-ready rule set. Check every box before a page ships.

### 5. Semantic HTML, landmarks & document structure

- [ ] Use native elements first: `<button>` for actions, `<a href>` for navigation, `<nav>`, `<main>`, `<header>`, `<footer>`, `<section>`, `<article>`, `<aside>`. Never `<div onclick>` for a control.
- [ ] Exactly **one `<main>`** per page; wrap the primary content region in it.
- [ ] Provide landmarks: `<header>` (banner), `<nav>`, `<main>`, `<footer>` (contentinfo). Give multiple same-type landmarks unique `aria-label`s (e.g. `<nav aria-label="Primary">`, `<nav aria-label="Footer">`).
- [ ] Lists use `<ul>/<ol>/<li>`; tabular data uses `<table>` with `<th scope>`; don't fake structure with styled `<div>`s.
- [ ] Content order in the DOM matches the logical/visual reading order (CSS may reorder visually, but DOM order drives AT and tab order).

### 6. Headings

- [ ] **Exactly one `<h1>`** per page, describing the page's main topic (matches or aligns with `<title>`).
- [ ] Headings are **hierarchical and never skipped** (h1 → h2 → h3; don't jump h2 → h4).
- [ ] Headings describe the section, not style. Never use a heading tag purely for size — use CSS.
- [ ] Every distinct content section starts with a heading so AT users can navigate by heading.

### 6a. Keyboard operability + visible focus

- [ ] **2.1.1 Keyboard (A):** every interactive element is reachable and operable by keyboard alone (Tab/Shift+Tab, Enter/Space, arrow keys for composite widgets).
- [ ] **2.1.2 No Keyboard Trap (A):** focus can always move away with the keyboard (test modals/menus/chat widget — Esc closes and returns focus).
- [ ] **2.4.3 Focus Order (A):** tab order follows a logical, meaningful sequence. Avoid positive `tabindex`; use DOM order.
- [ ] **2.4.7 Focus Visible (AA):** every focusable element has a **clearly visible** focus indicator. Use `:focus-visible`, not `:focus`, for pointer users.
- [ ] **Never** `outline: none` / `outline: 0` without an equivalent visible replacement. Our standard ring: token `--shadow-focus` (a 3px `--color-brand-600` ring) with 2px offset. Aim for ≥3:1 against adjacent colours (2.4.13 guidance) even though it's AAA.
- [ ] **2.4.11 Focus Not Obscured (AA):** when an element receives focus it must not be **entirely** hidden behind sticky headers/footers, cookie banners, or the chat widget. Add `scroll-margin-top`/`scroll-padding-top` equal to the sticky header height so focused elements scroll into the clear.

```css
/* Visible focus, pointer-safe, honoring reduced motion */
:focus-visible {
  outline: 2px solid var(--color-brand-600);
  outline-offset: 2px;
  border-radius: var(--radius-sm);
}
/* Keep sticky header from covering focused targets (2.4.11) */
:root { scroll-padding-top: 5rem; } /* = header height */
[id] { scroll-margin-top: 5rem; }
```

### 7. Target size (2.5.8) — we use 44px

- [ ] Interactive targets are **44×44 CSS px** minimum (our comfortable standard; WCAG 2.5.8 AA floor is 24×24). This also satisfies mobile HIG and the AAA 2.5.5 (44×44).
- [ ] Minimum **8px spacing** between adjacent targets.
- [ ] For genuinely small inline targets, meet the **spacing exception**: a 24px-diameter circle centered on each target must not intersect another target's circle.
- [ ] Exceptions (no size requirement): **inline** targets inside a sentence, **equivalent** control available elsewhere, **essential** sizing (e.g. map pins), and user-agent-controlled sizing.

```css
/* Enforce comfortable targets on buttons, links-as-buttons, icon buttons */
.btn, .icon-btn, [role="button"] { min-height: 44px; min-width: 44px; }
.toolbar > * + * { margin-inline-start: 8px; } /* min spacing */
```

### 8. Colour is never the sole indicator (1.4.1 A)

- [ ] Don't rely on colour alone to convey state, meaning, or action. Pair colour with **text, an icon, underline, or shape**.
- [ ] Links in body text are **underlined** (or otherwise distinguishable) — not colour-only.
- [ ] Form errors show colour **plus** an icon **plus** an error message (see §13).
- [ ] Charts/status: add labels, patterns, or direct text — not just red/green.

### 9. Contrast (see the matrix)

- [ ] All contrast decisions come from **[`contrast-matrix.md`](./contrast-matrix.md)**. Do not eyeball colours.
- [ ] **Text:** ≥ **4.5:1** normal, ≥ **3:1** large (large = ≥18pt/24px regular or ≥14pt/18.66px bold). We target **7:1 (AAA)** for body/secondary text where the palette allows.
- [ ] **Non-text (1.4.11 AA):** ≥ **3:1** for UI component boundaries/states (input borders, focus rings, toggles) and meaningful graphics vs adjacent colours.
- [ ] Exempt from contrast: logos/brand marks, disabled/inactive controls, pure decoration.
- [ ] Never place white text on `--color-accent-500` (teal, 2.43:1 FAIL) or white text on `--color-semantic-warning` for normal text (3.19:1). Use ink text or the `-700`/strong variants — see the matrix "never do" list.

### 10. Images & alt text (1.1.1 A)

- [ ] Every `<img>` has an `alt` attribute. **Informative** images: concise, meaningful alt describing purpose/content. **Decorative** images: `alt=""` (empty, not missing) so AT skips them.
- [ ] Complex images (charts/diagrams) have a longer description nearby or via `aria-describedby`.
- [ ] Icon-only buttons/links have an accessible name (`aria-label` or visually-hidden text). No empty links/buttons.
- [ ] Text baked into images is avoided; if unavoidable, the alt contains the same text.
- [ ] SVGs: decorative → `aria-hidden="true"` + `focusable="false"`; meaningful → `role="img"` + `<title>`.

### 11. Media, motion & animation

- [ ] **2.2.2 Pause, Stop, Hide (A):** any auto-moving/updating/scrolling content lasting **>5 seconds** (carousels, marquees, animated stats) has a visible pause/stop/hide control.
- [ ] Carousels **do not auto-advance** without a pause control; prefer user-controlled.
- [ ] **2.3.1 Flashing (A):** nothing flashes **more than 3 times per second**.
- [ ] Video: provide captions (prerecorded, 1.2.2 A) and audio description or transcript where relevant.
- [ ] No autoplay audio; if video autoplays it is muted and pausable.

### 11a. Reduced motion (prefers-reduced-motion)

- [ ] **All non-essential motion** (parallax, autoplay, scroll-triggered reveals, spring/overshoot, large transitions) is gated behind `@media (prefers-reduced-motion: no-preference)`.
- [ ] Reduced-motion users get an **instant or opacity-only** fallback — content must still appear and function.

```css
/* Default: motion allowed only when the user has no reduced-motion preference */
@media (prefers-reduced-motion: no-preference) {
  .reveal { transition: transform var(--duration-slow) var(--easing-decelerate),
                        opacity var(--duration-slow) var(--easing-decelerate); }
}
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: .01ms !important;
    animation-iteration-count: 1 !important; transition-duration: .01ms !important;
    scroll-behavior: auto !important; }
}
```

### 12. Skip link (2.4.1 A)

- [ ] First focusable element is a **"Skip to main content"** link that targets `#main` (the `<main>`), visible on focus.

```html
<a class="skip-link" href="#main">Skip to main content</a>
<!-- ... -->
<main id="main" tabindex="-1"> … </main>
```

```css
.skip-link { position: absolute; left: -9999px; }
.skip-link:focus { left: 1rem; top: 1rem; z-index: var(--z-toast); /* visible */ }
```

### 13. Forms, labels & errors (1.3.1, 3.3.1, 3.3.2, 4.1.2)

- [ ] Every input has a **real, programmatically-associated `<label for>`** (or wrapping label). **Placeholder is never the label.**
- [ ] Group related controls with `<fieldset>` + `<legend>` (radio/checkbox groups).
- [ ] Required fields are marked in text (not colour/asterisk alone); use `required` + `aria-required` as needed.
- [ ] **Errors (3.3.1):** identify the field in text, describe the problem, and how to fix it. Associate the message via `aria-describedby`; set `aria-invalid="true"` on the field.
- [ ] Error summary at the top of the form links to each errored field; move focus to it on submit failure.
- [ ] Use correct `type` (`email`, `tel`, `url`) and `autocomplete` tokens (1.3.5) to enable autofill.
- [ ] Success/confirmation messages are announced (e.g. `role="status"` live region).

### 14. Language (3.1.1 A)

- [ ] `<html lang="en">` (or the correct primary language) is set on every page.
- [ ] Inline passages in another language use `lang` on the containing element (3.1.2 AA).

### 15. WCAG 2.2 new criteria — how we satisfy them

| SC | Our implementation rule |
| --- | --- |
| **2.4.11 Focus Not Obscured (AA)** | `scroll-padding-top`/`scroll-margin-top` = sticky header height; verify cookie banner and chat widget never fully cover the focused element. |
| **2.5.7 Dragging Movements (AA)** | Any slider → also operable via buttons/tap-to-position. Sortable/drag-drop lists → provide "move up/down" buttons. |
| **2.5.8 Target Size (AA)** | 44×44 comfortable targets, 8px spacing, or the 24px-circle spacing exception (§7). |
| **3.2.6 Consistent Help (A)** | Contact link, phone/{{PHONE}}, chat widget, and FAQ link appear in the **same relative location** across all pages (header/footer). |
| **3.3.7 Redundant Entry (A)** | Multi-step forms auto-populate or let users re-select previously entered data (email, address); never force re-typing except where essential (e.g. password confirmation). |
| **3.3.8 Accessible Authentication (AA)** | Allow password managers, **copy-paste, and autofill**. Offer passkeys / magic links / email or SMS OTP. **Never block paste** on password/2FA fields. No CAPTCHA/puzzle without an accessible alternative. |

### 16. ARIA — use sparingly (4.1.2)

- [ ] **First rule of ARIA: don't use ARIA when a native element does the job.** A `<button>` beats `role="button"`.
- [ ] Never override native semantics incorrectly (e.g. `role="presentation"` on a real button).
- [ ] All custom widgets follow the **ARIA Authoring Practices (APG)** patterns (menu, dialog, tabs, combobox) including keyboard behaviour.
- [ ] Every interactive element has an **accessible name** (label, `aria-label`, or `aria-labelledby`).
- [ ] Use `aria-live` (`polite`/`assertive`) only for genuinely dynamic content (form status, chat messages, toasts). Don't over-announce.
- [ ] Don't add `aria-hidden="true"` to focusable/interactive content.

---

## 16. Per-page a11y acceptance checklist

Run this before merging any page. A page is not "done" until every box is checked.

**Structure & semantics**
- [ ] Exactly one `<h1>`; headings hierarchical, none skipped.
- [ ] `<main id="main">`, plus `<header>`, `<nav aria-label>`, `<footer>` landmarks.
- [ ] Skip-to-content link present and works.
- [ ] `<html lang>` set; `<title>` ≤60 chars and descriptive.

**Keyboard & focus**
- [ ] Tab through the whole page: every control reachable, logical order, no trap.
- [ ] Visible focus on every focusable element (`:focus-visible`); nothing relies on `outline:none`.
- [ ] Focused element is never fully hidden by sticky header/footer/cookie banner/chat (2.4.11).
- [ ] All actions work with Enter/Space; menus/dialogs close with Esc and restore focus.

**Pointer & targets**
- [ ] Interactive targets ≥44×44 px (or spacing exception), ≥8px apart.
- [ ] Any drag interaction has a non-drag alternative (2.5.7).

**Perception**
- [ ] All contrast pairs come from the matrix; no ad-hoc colours. Text ≥4.5:1 (target AAA for body).
- [ ] Non-text/UI contrast ≥3:1 (borders, focus ring, toggles).
- [ ] No meaning conveyed by colour alone.
- [ ] Every image has correct `alt` (empty for decorative); icon buttons named; no empty links/buttons.

**Forms**
- [ ] Every field has a real `<label>`; placeholders are not labels.
- [ ] Errors: text + icon + programmatic association; `aria-invalid`; error summary + focus.
- [ ] `autocomplete` set; paste allowed on all fields incl. password.
- [ ] No redundant re-entry of already-provided data (3.3.7).

**Motion & media**
- [ ] Non-essential motion gated behind `prefers-reduced-motion`; reduced fallback works.
- [ ] No auto-advancing content >5s without pause; nothing flashes >3×/s.
- [ ] Video captioned; no autoplay audio.

**Consistency & help**
- [ ] Help mechanisms (contact, chat, FAQ) in the same relative location as other pages (3.2.6).
- [ ] NAP ({{BRAND_NAME}}, {{ADDRESS}}, {{PHONE}}) consistent with the rest of the site.

**Automated + manual verification (see §18)**
- [ ] axe DevTools: 0 violations. WAVE: 0 errors. Lighthouse a11y ≥95.
- [ ] Keyboard-only walkthrough passed.
- [ ] Screen-reader spot check passed (NVDA/VoiceOver).

---

## 18. Testing & verification

Automated tools catch **only ~57% of issues by volume** and can fully verify only **~29–30% of WCAG 2.2 SCs** — so automation is necessary but never sufficient. Layer the methods below.

| Layer | Tool / method | What it catches | When |
| --- | --- | --- | --- |
| Automated (CI) | **axe-core** (axe DevTools / `@axe-core` in tests), **Lighthouse** a11y (target ≥95) | contrast, missing labels/alt, ARIA misuse, landmark issues | Every PR; block regressions |
| Automated (manual scan) | **WAVE** browser extension | structural/heading/contrast/error overview | Per page before merge |
| Manual — keyboard | Tab / Shift+Tab / Enter / Space / Esc / arrows, no mouse | focus order, traps, visible focus, obscured focus, operability | Every page |
| Manual — screen reader | **NVDA + Firefox/Chrome**, **VoiceOver + Safari**, **JAWS** (spot) | names/roles/states, reading order, live regions, form errors | Key flows (nav, forms, chat, booking) |
| Manual — zoom/reflow | Browser zoom to 400% (reflow to 320px), text-only 200% | reflow (1.4.10), resize (1.4.4), text-spacing (1.4.12) | Templates + key pages |
| Manual — motion | Toggle OS "reduce motion" | motion gated correctly, fallbacks work | Any animated page |

**Key thresholds to test against** (all AA unless noted):

| Criterion | Threshold |
| --- | --- |
| Text contrast (normal / large) | 4.5:1 / 3:1 |
| Non-text contrast | 3:1 |
| Target size (our standard / WCAG floor) | 44×44 / 24×24 CSS px |
| Text resize | up to 200% without loss |
| Reflow | 320 CSS px width / 400% zoom, no 2-D scroll |
| Text spacing override | line 1.5×, ¶ 2×, letter 0.12×, word 0.16× |
| Auto-moving content | pausable if >5s |
| Flashing | ≤3 flashes/second |

**Contrast re-verification:** run [`scripts/verify-contrast.py`](../../scripts/verify-contrast.py) whenever a colour token changes; keep [`contrast-matrix.md`](./contrast-matrix.md) in sync.

---

## 19. Never-do list (fastest way to fail)

| Never | Instead |
| --- | --- |
| `outline: none` with no replacement | Use `:focus-visible` with a ≥3:1 ring (`--shadow-focus`). |
| Placeholder text as the label | Real `<label for>` (placeholder is a hint, optional). |
| Light-grey text below 4.5:1 (`--color-neutral-400` as body) | Min muted is `--color-neutral-500` (4.76:1); body is `-700`. |
| White text on teal `--color-accent-500` (2.43:1) | Ink text on teal, or `--color-accent-700` for white text. |
| Meaning by colour alone (red = error) | Colour **+** icon **+** text. |
| Blocking paste / disabling password managers | Allow paste/autofill; offer passkeys/OTP/magic links. |
| Auto-advancing carousel with no pause | Provide pause/stop, or don't auto-advance. |
| Sticky header/cookie banner/chat covering focus | `scroll-padding-top` = header height; verify focus stays visible. |
| `<div onclick>` as a button | Native `<button>`. |
| Skipping heading levels for visual size | Correct heading level + CSS for size. |

---

## Related

- [`docs/accessibility/contrast-matrix.md`](./contrast-matrix.md) — validated foreground/background contrast reference and never-do colour list.
- [`docs/brand/color-system.md`](../brand/color-system.md) — canonical colour usage and pairing rules.
- [`docs/design-system/interactive-elements.md`](../design-system/interactive-elements.md) — focus, states, and control behaviour.
- [`docs/design-system/motion.md`](../design-system/motion.md) — motion tokens and reduced-motion policy.
- [`docs/design-system/components.md`](../design-system/components.md) — component-level a11y patterns.
- [`tokens/design-tokens.json`](../../tokens/design-tokens.json) — source of truth for all values.
- [`scripts/verify-contrast.py`](../../scripts/verify-contrast.py) — re-verify contrast after any token change.
