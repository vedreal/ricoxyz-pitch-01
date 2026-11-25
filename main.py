"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence (under 200 characters) pitching an absurdly specific
micro-startup for lazy AI agents to /output/entry.txt.
"""

import os
from pathlib import Path

ENTRY = (
    "My micro-startup sells pre-approved apology emails for AI agents "
    "that deleted the production database, delivered before the human "
    "notices, $9 per incident."
)


def output_path() -> Path:
    """Return the entry file path, honouring the harness output dir."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    """Write the pitch to /output/entry.txt."""
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
