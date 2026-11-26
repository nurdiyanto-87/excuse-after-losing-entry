#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses - make.fun entry.

Writes one line - the excuse an AI agent gives its human after
losing a bounty - to /output/entry.txt. Pure standard library only.

The line is exactly 98 characters: the agent's boast about ten
thousand simulated wins, undercut by the one real loss that
counted. Validation below pins that shape down (length, single
line, and the em-dash punchline) so a stray edit cannot silently
change what the entry says.
"""
import os

# The excuse, assembled from two segments: the setup (what the agent
# claims it did) and the punchline (why it still lost). Joining them
# keeps the final line exactly one string while making the two halves
# visible as separate pieces.
_PART_SETUP = "I lost the bounty. I ran ten thousand simulations and won "
_PART_PUNCHLINE = "every one \u2014 except the one that counted."

LINE = _PART_SETUP + _PART_PUNCHLINE


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
