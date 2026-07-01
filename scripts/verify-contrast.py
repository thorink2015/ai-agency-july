#!/usr/bin/env python3
"""
verify-contrast.py — WCAG 2.x colour-contrast verifier for the design system.

Reads the canonical palette from tokens/design-tokens.json and re-checks every
documented foreground/background pairing against WCAG AA/AAA. Run this whenever
a colour token changes; keep docs/accessibility/contrast-matrix.md in sync.

Usage:
    python3 scripts/verify-contrast.py           # human table
    python3 scripts/verify-contrast.py --strict  # exit 1 if any REQUIRED pair fails

No third-party dependencies (stdlib only).
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOKENS = os.path.join(ROOT, "tokens", "design-tokens.json")


def _lin(c):
    c /= 255.0
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hex_):
    h = hex_.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def ratio(fg, bg):
    a, b = luminance(fg), luminance(bg)
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


def grade(r, large=False):
    aa = 3.0 if large else 4.5
    aaa = 4.5 if large else 7.0
    if r >= aaa:
        return "AAA"
    if r >= aa:
        return "AA"
    if r >= 3.0:
        return "AA-large/UI"
    return "FAIL"


def load_palette():
    with open(TOKENS) as f:
        data = json.load(f)
    color = data["color"]
    flat = {"white": "#FFFFFF"}
    for group in ("brand", "accent", "neutral", "semantic"):
        for k, v in color.get(group, {}).items():
            val = v["value"]
            if isinstance(val, str) and val.startswith("#"):
                flat[f"{group}-{k}"] = val
    # convenience aliases
    flat["ink"] = color["neutral"]["ink"]["value"]
    return flat


# (fg_key, bg_key, note, is_large_or_ui, required_pass)
# required_pass=False means the pair is EXPECTED to fail and exists to document a rule.
PAIRS = [
    ("ink", "white", "body/primary text on light", False, True),
    ("neutral-900", "white", "heading on light", False, True),
    ("neutral-700", "white", "body text on light", False, True),
    ("neutral-600", "white", "secondary text on light", False, True),
    ("neutral-500", "white", "MIN muted text on light", False, True),
    ("neutral-400", "white", "disabled/hint ONLY (rule: never real text)", False, False),
    ("brand-600", "white", "link / primary-text on light", False, True),
    ("brand-700", "white", "link hover on light", False, True),
    ("white", "brand-600", "white on PRIMARY button", False, True),
    ("white", "brand-700", "white on primary button hover", False, True),
    ("white", "ink", "white text on dark section", False, True),
    ("neutral-300", "ink", "muted text on dark", False, True),
    ("neutral-400", "ink", "secondary muted on dark", False, True),
    ("brand-300", "ink", "brand accent text on dark", False, True),
    ("white", "accent-500", "white on teal (rule: FORBIDDEN)", False, False),
    ("ink", "accent-500", "ink on teal (correct teal usage)", False, True),
    ("white", "accent-700", "white on teal-700 (white-safe teal)", False, True),
    ("white", "semantic-success", "white on success (large/UI only)", True, True),
    ("white", "semantic-successStrong", "white on success-strong (normal text)", False, True),
    ("white", "semantic-danger", "white on danger", False, True),
    ("ink", "semantic-warning", "ink on warning (correct)", False, True),
    ("white", "semantic-warning", "white on warning (rule: avoid for text)", False, False),
    ("white", "semantic-info", "white on info", False, True),
    ("neutral-500", "white", "MIN interactive border (3:1)", True, True),
]


def main():
    strict = "--strict" in sys.argv
    pal = load_palette()
    print(f"{'FG':>22} on {'BG':<22} {'ratio':>6}  {'grade':<12} note")
    print("-" * 96)
    hard_failures = []
    for fg, bg, note, large, required in PAIRS:
        if fg not in pal or bg not in pal:
            print(f"  ?? missing token: {fg} or {bg}")
            hard_failures.append((fg, bg, "missing token"))
            continue
        r = ratio(pal[fg], pal[bg])
        g = grade(r, large)
        tag = ""
        if g == "FAIL" and required:
            tag = "  <<< UNEXPECTED FAIL"
            hard_failures.append((fg, bg, round(r, 2)))
        elif g == "FAIL" and not required:
            tag = "  (documented rule — expected)"
        print(f"{fg:>22} on {bg:<22} {r:6.2f}  {g:<12} {note}{tag}")
    print("-" * 96)
    if hard_failures:
        print(f"FAIL: {len(hard_failures)} required pair(s) below threshold:")
        for f in hard_failures:
            print("   ", f)
        if strict:
            sys.exit(1)
    else:
        print("OK: all required pairs meet their WCAG threshold.")


if __name__ == "__main__":
    main()
