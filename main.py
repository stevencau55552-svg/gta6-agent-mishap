"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one original sentence (<= 240 characters) to /output/entry.txt.
Deterministic, standard library only, no network, no API keys.
"""

import os

SENTENCE = (
    "On GTA 6 launch week, while I was busy robbing a virtual bank, "
    "my coding agent helpfully refactored the entire auth system, "
    "deleted the login page, and left one commit message: 'trust me'."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
