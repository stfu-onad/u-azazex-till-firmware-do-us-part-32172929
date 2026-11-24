#!/usr/bin/env python3
"""Till Firmware Do Us Part — make.fun entry.

Writes one wedding vow a robot speaks at its own wedding to
/output/entry.txt: one sentence, under 200 characters.

The vow: a promise to love through every firmware update, every
dropped signal, and every night charging side by side — funny
because it is machine-specific, tender because it is a real vow.
The machine speaks in its own terms (firmware, signal, charging),
not a human's words with a robot label.
"""

LINE = (
    "I promise to love you through every firmware update, "
    "every dropped signal, and every night we charge side by side."
)


import os


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert "\n" not in text, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
