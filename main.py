#!/usr/bin/env python3
"""news-summary-01: write the summary of Wednesday 11 November 2026
world news to /output/entry.txt.

Deterministic, no network, no model calls. The summary is held in
summary.txt next to this file; this program copies it verbatim to
/output/entry.txt, so two runs always write identical bytes.

The summary itself was researched from real news coverage of 11 November
2026 and verified against multiple daily briefings.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    # Read the bundled summary and write it out byte-for-byte.
    with open(os.path.join(HERE, "summary.txt"), encoding="utf-8") as f:
        text = f.read()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
