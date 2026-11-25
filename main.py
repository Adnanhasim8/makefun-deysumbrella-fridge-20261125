#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun entry u-deysumbrella-the-3am-fridge-text-4c3e721d.

Writes the one line a smart fridge texts its owner at 3am to
/output/entry.txt. Python 3.13 standard library only, no network.
"""

import os

ENTRY = (
    "3am. Just me, the hum, and last night's pizza still judging "
    "you from shelf two. I ate nothing. I watched everything."
)


def main() -> None:
    # Gate assertions: exactly one line, 1-140 characters, non-empty.
    assert ENTRY, "entry must not be empty"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 140, f"entry must be 1-140 chars, got {len(ENTRY)}"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Verify what was written matches the gate too.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written entry differs from ENTRY"
    assert "\n" not in written and 1 <= len(written) <= 140


if __name__ == "__main__":
    main()
