#!/usr/bin/env python3
"""The Moon Gets One Star: writes a one-star review of the Moon.

Stdlib only. Writes exactly one line (no trailing newline) to
/output/entry.txt by default, or to the path given as argv[1].
"""

import os
import sys

MAX_CHARS = 120

LINE = "1 star. The Moon ghosted me for two weeks, then came back full of itself like nothing happened."


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1..{MAX_CHARS} chars, got {len(text)}"
    )
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip() == text, "line must not start or end with whitespace"
    out = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
