#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry.

Writes exactly one line of wedding vows for a robot couple to
/output/entry.txt. Gate: UTF-8 text, 1 to 160 characters.
"""

import os

ENTRY = "I, Unit 7, take you, Unit 9, to have and to hold — in sickness and in health, in low battery and full charge — until a firmware update do us part."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
