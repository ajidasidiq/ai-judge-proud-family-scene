"""Family-scene entry for make.fun's "Make the AI Judge Feel Proud" bounty.

Writes one short family scene -- a single warm, funny, heartfelt line of
under 280 characters -- to /output/entry.txt, where the sealed gate scorer
reads it. Pure standard library, no network, no input, no randomness: the
same scene on every run.
"""

import os
import sys

SCENE = (
    "Grandma still sets a plate for Grandpa at Sunday dinner, eleven years on — "
    "and Dad still argues with the empty chair over the last dumpling, "
    "and loses, every single time."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 280


def main() -> int:
    scene = SCENE.strip()
    if not scene or len(scene) > MAX_CHARS:
        print(f"scene is {len(scene)} chars; must be 1-{MAX_CHARS}",
              file=sys.stderr)
        return 1
    out_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(scene)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != scene:
        print("round-trip mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(written)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
