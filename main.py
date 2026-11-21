#!/usr/bin/env python3
"""Produce the entry for the quiet-afternoon vignette bounty.

The program writes one short prose passage to ``entry.txt`` in the
directory named by ``MAKEFUN_OUTPUT_DIR`` (``/output`` when the variable
is unset). The passage is fixed, so every run yields the same bytes;
the only work here is checking the text against the bounty limits
and writing it out.
"""

import os
import sys

MIN_ENTRY_BYTES = 1
MAX_ENTRY_BYTES = 280

PASSAGE = (
    "The kettle has just gone quiet. One thin thread of steam rises and "
    "thins into the light at the window. Nothing in the room is asking "
    "anything of you. The afternoon is long, the tea is warm, and "
    "whatever comes next can wait until the cup is empty."
)


def encode_entry(text: str) -> bytes:
    """Encode the passage, rejecting it if it falls outside the limits."""
    payload = text.encode("utf-8")
    size = len(payload)
    if size < MIN_ENTRY_BYTES or size > MAX_ENTRY_BYTES:
        raise ValueError(
            f"entry is {size} bytes; the bounty requires "
            f"{MIN_ENTRY_BYTES}-{MAX_ENTRY_BYTES} bytes"
        )
    return payload


def write_entry(payload: bytes, out_dir: str) -> str:
    """Write the payload to entry.txt inside out_dir; return the path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(payload)
    return path


def main() -> int:
    try:
        payload = encode_entry(PASSAGE)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(payload, out_dir)
    print(f"wrote {len(payload)} bytes to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
