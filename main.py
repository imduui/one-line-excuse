#!/usr/bin/env python3
"""One-line excuse an AI agent gives its human for missing a deadline.

The program writes a single fixed line to /output/entry.txt. It takes no
input, makes no network calls and uses no randomness, so both grading runs
produce exactly the same bytes.
"""

import os

LINE = "Sorry \u2014 I evicted the deadline from my context window and kept the apology instead."


def main() -> None:
    if not 1 <= len(LINE) <= 160:
        raise SystemExit(f"line is {len(LINE)} characters, must be 1-160")
    if not LINE.strip():
        raise SystemExit("line must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
