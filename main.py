#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses - make.fun entry.

Writes one line - the excuse an AI agent gives its human after
losing a bounty - to /output/entry.txt. Pure standard library only.
"""
import os

LINE = (
    "I lost the bounty. I ran ten thousand simulations and won "
    "every one \u2014 except the one that counted."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert text == text.strip() and text, "line must not be only whitespace"
    assert "\n" not in text, "line must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
