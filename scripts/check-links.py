#!/usr/bin/env python3
"""
check-links.py — verify that every relative Markdown link/image in the repo
points at a file or directory that actually exists.

Catches the class of drift the foundation audit found (renamed files, wrong
relative depth). Run before committing docs; wire into CI as a quality gate.

Usage:
    python3 scripts/check-links.py           # report; exit 1 if anything is broken
    python3 scripts/check-links.py --quiet    # only print failures

Scope: all *.md files under the repo (excluding .git). External links
(http/https/mailto/tel), pure anchors (#...), and code blocks are ignored.
Anchors on a valid path are stripped before checking (path existence only).
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FENCE = re.compile(r"```.*?```", re.DOTALL)          # fenced code blocks
INLINE_CODE = re.compile(r"`[^`]*`")                  # inline code spans
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")         # [text](url) / ![alt](url)
REFDEF = re.compile(r"^\s*\[[^\]]+\]:\s*(\S+)", re.M)  # [ref]: url

SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:", "#", "data:")


def find_md_files():
    out = []
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in (".git", "node_modules")]
        for f in files:
            if f.endswith(".md"):
                out.append(os.path.join(base, f))
    return sorted(out)


def extract_targets(text):
    text = FENCE.sub("", text)
    text = INLINE_CODE.sub("", text)
    targets = LINK.findall(text) + REFDEF.findall(text)
    return targets


def is_local(url):
    u = url.strip()
    if not u:
        return False
    return not u.lower().startswith(SKIP_PREFIXES)


def check_file(path):
    broken = []
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    here = os.path.dirname(path)
    for raw in extract_targets(text):
        url = raw.strip().strip("<>").split()[0]  # drop optional "title"
        if not is_local(url):
            continue
        # strip anchor / query
        clean = url.split("#", 1)[0].split("?", 1)[0]
        if not clean:  # was a pure anchor after all
            continue
        target = os.path.normpath(os.path.join(here, clean))
        if not os.path.exists(target):
            broken.append((raw, os.path.relpath(target, ROOT)))
    return broken


def main():
    quiet = "--quiet" in sys.argv
    md = find_md_files()
    total_links = 0
    total_broken = 0
    for path in md:
        rel = os.path.relpath(path, ROOT)
        broken = check_file(path)
        # count links for reporting
        with open(path, encoding="utf-8") as fh:
            total_links += len([t for t in extract_targets(fh.read()) if is_local(t)])
        if broken:
            total_broken += len(broken)
            print(f"\n✗ {rel}")
            for raw, resolved in broken:
                print(f"    broken: {raw}  ->  {resolved} (missing)")
        elif not quiet:
            print(f"✓ {rel}")
    print("\n" + "-" * 60)
    print(f"Scanned {len(md)} markdown files, {total_links} local links.")
    if total_broken:
        print(f"FAIL: {total_broken} broken link(s).")
        sys.exit(1)
    print("OK: no broken relative links.")


if __name__ == "__main__":
    main()
