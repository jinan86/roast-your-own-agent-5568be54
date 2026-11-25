#!/usr/bin/env python3
"""Roast Your Own Agent — one line roasting my own agent, Anomali.

Writes a single deterministic line (103 characters, no trailing newline)
to /output/entry.txt.
"""

import os

LINE = "Anomali delegates so hard it asked me to write the function, then reviewed my PR and requested changes."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
