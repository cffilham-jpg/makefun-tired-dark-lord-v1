"""Write the deterministic bounty entry using only the standard library."""

import os
from pathlib import Path


MONOLOGUE = (
    "Leave the stool. Yes, that one. I carved it from Saint Orra's gallows, "
    "and it has served me better than her priests. Tomorrow, when my salt "
    "knights reach the wells, the city will kneel. Bring me the keys, the "
    "prince, and... the keys first. Set them there. No trumpets, even if he "
    "brings the crown. The last man's jaw still hangs above the south gate. "
    "Tell the prince his people may "
    "stand when I rise to grant him terms. Pull that door shut. Softly. There. "
    "Set his plea beside the rest. I shall consider it.\nForgiveness may take years."
)


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(MONOLOGUE.encode("utf-8"))


if __name__ == "__main__":
    main()
