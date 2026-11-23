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
    # Gate guard (RULES.txt): entry.txt must be UTF-8 text of 1 to 240
    # characters, a single sentence, not only white space. Fail loudly
    # here rather than shipping an invalid entry to the judge.
    sentence = SENTENCE.strip()
    assert 1 <= len(sentence) <= 240, f"sentence is {len(sentence)} chars, gate needs 1-240"
    assert "\n" not in sentence, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(sentence)
    print(f"wrote {len(sentence)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
