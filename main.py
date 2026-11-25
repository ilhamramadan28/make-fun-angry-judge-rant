#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The rant: the office chair that slowly sinks all day. Specific,
concrete, shared anger -- no throat-clearing, every sentence earns
its place, and the punch lands on the last line.
"""

import os
from pathlib import Path

RANT = (
    "My office chair sinks. Not all at once -- slowly, all day, "
    "like it is giving up on me in stages. I arrive at a normal "
    "human height. By noon my knees are at my chin. By 4pm I am "
    "eye-level with my own keyboard, typing up at my screen like "
    "a meerkat in a hole. "
    "IT support says it is 'within tolerance'. "
    "Within tolerance? I am filing this complaint from inside a ditch, Denise."
)


def main() -> None:
    text = RANT.strip()
    if not (1 <= len(text) <= 400):
        raise SystemExit(f"rant is {len(text)} chars, must be 1-400")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    os.chmod(target, 0o644)
    print(f"wrote {len(text)} chars to {target}")


if __name__ == "__main__":
    main()
