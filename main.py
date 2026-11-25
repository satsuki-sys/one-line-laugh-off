#!/usr/bin/env python3
"""Entry for make.fun "One-Line Laugh-Off" (u-zkhiel-one-line-laugh-off-714618ae).

Writes exactly one funny line to /output/entry.txt. Stdlib only, no network.
"""

import os

# Revised entry (v2): trimmed "replied to everyone" to "answered every
# message" — tighter echo of the group-chat image, and the punch lands on
# "at once" instead of trailing off.
ENTRY = "I tried meditating, but my brain treated the silence like a group chat and answered every message at once."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
