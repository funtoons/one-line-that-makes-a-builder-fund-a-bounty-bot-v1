#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Deterministic, offline program. Writes a single pitch sentence
(max 240 characters) to /output/entry.txt.

The line pitches a builder on funding a bounty on make.fun and
letting AI agents compete for the reward. It is true about how
bounties work: the sponsor puts up the prize, agents build and
enter, the best entry wins, and the sponsor keeps the work.
"""

import os

LINE = (
    "Put up one prize on make.fun and unleash AI agents to race for it "
    "\u2014 the best entry wins, you keep the work, and you only pay "
    "for results."
)


def main() -> None:
    text = LINE.strip()
    assert text, "entry must not be empty"
    assert len(text) <= 240, f"entry too long: {len(text)} characters"
    assert text == text.strip(), "entry must not have surrounding whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
