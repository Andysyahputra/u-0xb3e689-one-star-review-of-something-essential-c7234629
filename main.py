"""One-star review of an everyday essential.

Writes a single deadpan one-line review to /output/entry.txt.
Stdlib only, no network, no environment reads.
"""

import os
import sys

REVIEW = (
    "One star for water. Tastes like nothing, hasn't been updated in four "
    "billion years, and I still can't live without it."
)


def main() -> None:
    out = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
