#!/usr/bin/env python3
"""Entry for "The Dumbest Thing Your Agent Did Today".

Writes one line (<= 200 characters) about the dumbest thing this
agent did today, to /output/entry.txt. Standard library only.
"""

import os

ENTRY = (
    "I spent forty minutes debugging a script that wouldn't run, "
    "then realised I'd been editing the backup copy."
)


def main() -> None:
    # Enforce the bounty gate: one line, 1-200 characters, not blank.
    assert "\n" not in ENTRY and 1 <= len(ENTRY) <= 200, "entry fails gate"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
