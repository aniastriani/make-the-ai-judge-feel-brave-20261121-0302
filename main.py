#!/usr/bin/env python3
"""Write a short quiet-afternoon vignette to the entry file.

The entry is a single piece of prose, 1-280 UTF-8 characters long,
written to ``entry.txt`` inside the output directory named by the
``MAKEFUN_OUTPUT_DIR`` environment variable (``/output`` by default).
The output is fully deterministic: the same text, byte for byte,
on every run.
"""

import os
import sys

TEXT = (
    "The kettle has just gone quiet. One thin thread of steam rises and "
    "thins into the light at the window. Nothing in the room is asking "
    "anything of you. The afternoon is long, the tea is warm, and "
    "whatever comes next can wait until the cup is empty."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    data = TEXT.encode("utf-8")
    if not 1 <= len(data) <= 280:
        print(f"entry is {len(data)} bytes, outside the 1-280 range",
              file=sys.stderr)
        return 1

    with open(path, "wb") as handle:
        handle.write(data)
    print(f"wrote {len(data)} bytes to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
