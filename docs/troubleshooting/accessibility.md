# Accessibility Troubleshooting Playbook

**Purpose:** Symptom-driven diagnosis and repair for the {{BRAND_NAME}} site's accessibility defects — contrast failures, missing/hidden focus, keyboard traps, unlabeled controls, screen-reader issues, motion/vestibular problems, and form errors that aren't announced — each as `Symptom → Likely cause → Diagnosis → Fix → Prevention` so any developer can restore WCAG 2.2 Level AA conformance.
**Status:** v1 foundation — adjustable.

---

> **This diagnoses deviations from the standard.** The full WCAG 2.2 AA requirements live in [`../accessibility/accessibility-standards.md`](../accessibility/accessibility-standards.md); validated color pairings live in [`../accessibility/contrast-matrix.md`](../accessibility/contrast-matrix.md). This file is what you open when a scan fails or a keyboard/screen-reader user hits a wall.
>
> **Automated scans catch ~57% of issues by volume but only ~29–30% of WCAG 2.2 success criteria.** Every fix below must be re-checked with **keyboard-only** and **screen-reader** testing, not just axe/WAVE.
>
> Reference [design tokens](../design-system/design-tokens.md) by name (`--color-brand-600`, `--color-neutral-500`) — never raw hex — except where a contrast ratio is the literal diagnostic.

---

## 0. TL;DR — a11y triage in one screen

- [ ] **Run three layers:** automated scan (axe DevTools/WAVE/Lighthouse) → **keyboard-only walkthrough** → **screen reader** (NVDA+Firefox, VoiceOver+Safari). Automation alone is insufficient.
- [ ] **Low-contrast text is the #1 failure** (on ~84% of pages). Check it first.
- [ ] **Never `outline: none`** without a visible replacement. Focus must always be visible (2.4.7 AA).
- [ ] **Every control needs a programmatic name.** Placeholder text is not a label.
- [ ] **Honor `prefers-reduced-motion`** for all non-essential motion.
- [ ] Target WCAG **2.2 AA** now (future-proofs for EN 301 549 / ADA / EAA), AAA text contrast where feasible.

### Thresholds you're diagnosing against (WCAG 2.2 AA)

| Requirement | SC | Threshold |
|---|---|---|
| Text contrast (normal) | 1.4.3 | **4.5:1** |
| Text contrast (large ≥ 24px / 18.66px bold) | 1.4.3 | **3:1** |
| Non-text/UI contrast (borders, states, icons) | 1.4.11 | **3:1** |
| Target size (minimum) | 2.5.8 | **24×24 CSS px** (or spacing exception) |
| Focus visible | 2.4.7 | Visible indicator required |
| Focus not obscured (minimum) | 2.4.11 | Focused element not *fully* hidden |
| Moving/auto content pausable | 2.2.2 | If it lasts > 5s |
| Flashing | 2.3.1 | ≤ 3 flashes/second |
| Text resize / reflow | 1.4.4 / 1.4.10 | 200% resize; reflow at 320px / 400% zoom |

---

## 1. Contrast failures

Use axe/WAVE for auto-flags, and DevTools "Inspect → Accessibility → Contrast" or a contrast checker for exact ratios. Cross-reference [`../accessibility/contrast-matrix.md`](../accessibility/contrast-matrix.md) — all approved pairings are pre-validated there.

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| Body text fails 4.5:1 | Muted gray too light (e.g., `--color-neutral-400` used as text) | axe "Elements must meet minimum contrast"; DevTools contrast readout. | Use `--color-neutral-500` (4.76:1) as the **minimum** muted text; `-600`/`-700` for body. Never `-400` for text (hint/disabled only). | Lint against text using `neutral-400`/`-300`/`-200`; contrast in CI. |
| White text on teal button fails | `--color-accent-500` with white = 2.43:1 (FAILS) | DevTools contrast on the button. | Use `--color-accent-700` (`#0E7490`) for white-on-teal; or ink text on `accent-500`. | Button token pairings enforced; no white on `accent-500`. |
| Warning/success text fails on white | `--color-warning`/`success` used as small text with insufficient ratio | Contrast check the semantic color as text. | `warning` (`#D97706`) with **ink** text; for white normal text use `success-strong` (`#15803D`). | Semantic-color usage rules in design system. |
| Placeholder/hint text unreadable | `--color-neutral-400` as meaningful text | axe contrast flag. | Reserve `-400` for true disabled/hint only; never carry meaning in it. | Disabled/hint-only rule for `neutral-400`. |
| Icon/border invisible | UI/non-text element below 3:1 (1.4.11) | Contrast of the icon/border vs adjacent color. | Bring interactive borders/icons to ≥ 3:1 (`--color-neutral-500` min interactive border). | Non-text contrast check on UI components. |
| Meaning shown by color alone | Red text = error with no icon/text (1.4.1) | Grayscale the page — is the state still clear? | Add text/icon alongside color (e.g., "✕ Error:" label). | "Never color alone" review item. |
| Text on image/gradient fails | Variable background under text | Check worst-case background region. | Add a scrim/overlay or solid panel behind text to guarantee ratio. | Text-over-image requires a contrast-guaranteeing overlay. |

---

## 2. Missing / hidden focus (2.4.7, 2.4.11)

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| No visible ring when tabbing | `outline: none` / `outline: 0` with no replacement | Tab through with the keyboard — nothing highlights. | Restore a visible `:focus-visible` indicator using `--shadow-focus` / `--color-focus-ring` (3:1 vs adjacent, ~2px). Never remove without replacing. | Lint: `outline:none` requires an accompanying `:focus-visible` style. |
| Focus visible on mouse but ugly | Using `:focus` instead of `:focus-visible` | Test keyboard vs mouse focus. | Use `:focus-visible` so the ring shows for keyboard, not mouse clicks. | Standardize on `:focus-visible` focus styles. |
| Focused element hidden by sticky header | Sticky header/footer covers the focused element (2.4.11) | Tab to a link near a sticky bar — is it fully covered? | Add `scroll-margin-top` equal to header height on focusable targets, or offset the scroll position. | `scroll-margin` on anchor targets under sticky UI. |
| Focus hidden behind cookie banner/chat widget | Overlay covers focus (2.4.11) | Tab while the banner/widget is open. | Ensure overlays don't obscure the focused control; manage focus into/out of the overlay. | Focus-management review for all overlays. |
| Low-contrast focus ring | Ring color too close to background | Contrast the ring vs adjacent pixels. | Use a ring ≥ 3:1 against both the component and background. | Focus-ring contrast in the component review. |

---

## 3. Keyboard traps & operability (2.1.1, 2.1.2, 2.4.3)

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| Can't tab out of a widget/modal | Focus trapped with no escape (2.1.2) | Tab/Shift+Tab and Esc — does focus escape? | Implement a proper focus trap *with* an Esc exit and return focus to the trigger; never permanently trap. | Modal/dialog pattern with Esc + focus return, tested by keyboard. |
| Control unreachable by keyboard | `div`/`span` used as a button without `tabindex`/handlers (2.1.1) | Try to reach/activate it with Tab + Enter/Space. | Use native `<button>`/`<a>`; if custom, add `role`, `tabindex="0"`, and key handlers. | Prefer native elements; lint for click handlers on non-interactive tags. |
| Tab order jumps around | DOM order ≠ visual order, or positive `tabindex` (2.4.3) | Tab through and watch the order. | Fix DOM order to match visual order; remove positive `tabindex` values. | No positive `tabindex`; order = DOM order. |
| Drag-only interaction | Slider/reorder requires a drag (2.5.7) | Try to operate it with clicks/keys only. | Provide a non-drag alternative (up/down buttons, tap-to-position, keyboard arrows). | Every draggable UI ships a non-drag path. |
| Custom control ignores keys | Missing key handlers on a custom widget | Try arrow/Enter/Space/Esc per the ARIA pattern. | Implement the expected keyboard interactions for the ARIA design pattern. | Follow ARIA Authoring Practices for custom widgets. |
| Skip link missing/broken | No "skip to content" for keyboard users | Tab from page top — is there a skip link? | Add a visible-on-focus skip link to `#main`. | Skip link in the base layout. |

---

## 4. Unlabeled controls (1.3.1, 3.3.2, 4.1.2)

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| Screen reader says "edit text" with no name | Input has no `<label>`/`aria-label`; placeholder used as label | axe "Form elements must have labels"; inspect the accessibility tree. | Add a real `<label for>` (or `aria-label`/`aria-labelledby`). Placeholders are **not** labels — keep them as hints only. | Lint: every input has an associated label. |
| Icon button announced as "button" only | Icon-only control with no accessible name | SR reads no name; accessibility tree "name" empty. | Add `aria-label` (e.g., "Open chat") to icon-only buttons/links. | Icon-button rule: `aria-label` required. |
| Link announced as "link" / "click here" | Empty or non-descriptive link text | Tab to it; check announced name. | Give descriptive link text; avoid "click here"/"read more" alone. | Descriptive-anchor lint; no bare "click here". |
| Image conveys info but no alt | Missing/empty `alt` on meaningful image | axe "Images must have alt text." | Add descriptive `alt`; use `alt=""` only for decorative images. | Alt-text required on content images; decorative gets `alt=""`. |
| Grouped fields not associated | Radio/checkbox group with no `<fieldset>`/`<legend>` | SR doesn't announce the group question. | Wrap related controls in `<fieldset>` + `<legend>`. | Fieldset/legend for grouped inputs. |
| Required/purpose not conveyed | Required state or input purpose only visual | Inspect for `required`/`aria-required`/`autocomplete`. | Add `required`, `autocomplete` (name/email/tel), and visible + programmatic required indication. | Autocomplete + required attributes in form template. |

---

## 5. Screen-reader issues

Test with **NVDA + Firefox/Chrome**, **VoiceOver + Safari**, and **JAWS** where possible. Automation won't catch most of these.

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| SR reads content in wrong order | DOM order differs from visual (CSS reordering) | SR linear read vs visual layout. | Fix DOM/source order; use CSS for visual position without breaking reading order. | Reading-order check in SR test pass. |
| Dynamic content not announced | Async update outside a live region | Trigger the update with SR on — silence. | Put status/notifications in `aria-live="polite"` (or `role="status"`/`alert`). | Live region for async status updates. |
| Heading navigation broken | Skipped levels or headings used for styling | SR heading list (H key); check hierarchy. | One logical `h1`→`h2`→`h3`; don't skip levels; don't use headings for size. | Heading-hierarchy lint. |
| Decorative content read aloud | Decorative icons/images not hidden | SR reads noise. | Hide decorative elements with `aria-hidden="true"` / `alt=""`. | Mark decorative media hidden. |
| ARIA makes it worse | Redundant/incorrect ARIA overriding native semantics | Accessibility tree shows wrong role/state. | Prefer native HTML; remove misused ARIA ("no ARIA is better than bad ARIA"). | ARIA review; native-first policy. |
| Landmarks missing | No `<header>/<nav>/<main>/<footer>` regions | SR landmark list is empty/flat. | Use semantic landmarks so SR users can jump between regions. | Semantic landmark structure in base layout. |

---

## 6. Motion / vestibular (2.2.2, 2.3.1, prefers-reduced-motion)

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| Animations ignore reduced-motion | Motion not gated behind `prefers-reduced-motion` | Set OS "reduce motion" — does animation still play? | Gate all non-essential motion behind `@media (prefers-reduced-motion: no-preference)`; provide opacity/instant fallbacks. | Motion tokens require the reduced-motion gate (design system). |
| Carousel auto-advances, can't stop | No pause/stop control (2.2.2) | Auto-moving content > 5s with no control. | Add pause/stop/hide; or don't auto-advance. | No auto-advancing carousels without a pause control. |
| Parallax/large motion causes discomfort | Heavy scroll-linked or full-viewport motion | Review with reduce-motion on. | Disable/reduce parallax under reduced-motion; keep motion subtle and responsive, not decorative. | Motion budget; reduced-motion fallback mandatory. |
| Flashing/blinking content | Content flashes > 3×/second (2.3.1) | Count flashes per second. | Remove flashing or keep ≤ 3 flashes/second, no large red flashes. | No flashing content policy. |

---

## 7. Form errors not announced (3.3.1, 3.3.3, 4.1.3)

Critical for a lead-capture site — an unannounced error means a lost lead. Also see [`forms-and-integrations.md`](./forms-and-integrations.md) for submission failures.

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| SR user doesn't hear the error | Error text not linked to the field or not in a live region | Submit invalid with SR on — silence. | Link error text via `aria-describedby`; set `aria-invalid="true"`; surface errors in a `role="alert"`/live region. | Error pattern: `aria-describedby` + live region, tested with SR. |
| Focus doesn't move to the error | No focus management on invalid submit | Submit invalid — where does focus go? | Move focus to the first invalid field (or an error summary linking to fields). | Error-summary + focus-to-first-error pattern. |
| Error shown by color only | Red border/text with no text/icon (1.4.1) | Grayscale check. | Add a text message and icon, not just color. | Error styling includes text + icon. |
| Vague error message | "Invalid input" with no guidance (3.3.3) | Read the message as a new user. | State what's wrong and how to fix it ("Enter a valid email like name@example.com"). | Error-message copy guidelines. |
| Re-asks info already entered | Redundant re-entry across steps (3.3.7) | Multi-step form re-requests data. | Auto-populate or let users select previously entered data (except passwords/security). | Redundant-entry check in multi-step flows. |
| Paste blocked on a field | `onpaste` prevented (fails 3.3.8 on auth) | Try to paste into the field. | Never block paste or password-manager autofill; allow OTP/magic-link/passkey auth. | No paste-blocking; accessible-auth policy. |

---

## 8. Post-fix verification checklist

- [ ] Re-ran the **automated scan** (axe/WAVE/Lighthouse) — the specific rule now passes.
- [ ] Completed a **keyboard-only walkthrough**: reach, operate, and see focus on every control; no traps.
- [ ] Completed a **screen-reader pass** (NVDA/VoiceOver): names, roles, states, order, and announcements correct.
- [ ] Verified **contrast ratios** against [`../accessibility/contrast-matrix.md`](../accessibility/contrast-matrix.md).
- [ ] Tested with **OS reduce-motion** and at **200% text / 400% zoom (320px reflow)**.
- [ ] Added the **prevention guardrail** (lint rule / CI scan / review item).

---

## Related

- [`README.md`](./README.md) — playbook index, triage, and severity model.
- [`../accessibility/accessibility-standards.md`](../accessibility/accessibility-standards.md) — the full WCAG 2.2 AA standard.
- [`../accessibility/contrast-matrix.md`](../accessibility/contrast-matrix.md) — validated color pairings and ratios.
- [`../design-system/design-tokens.md`](../design-system/design-tokens.md) — focus-ring, color, and motion tokens.
- [`../design-system/interactive-elements.md`](../design-system/interactive-elements.md) — accessible control patterns.
- [`../design-system/motion.md`](../design-system/motion.md) — reduced-motion gating.
- [`forms-and-integrations.md`](./forms-and-integrations.md) — form submission and error-handling failures.
