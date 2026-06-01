"""Basic SysEx parsing helpers for Waldorf Protein reverse engineering."""

from __future__ import annotations


def parse_sysex(data: bytes) -> dict:
    """Parse a raw SysEx message into a minimal structured dictionary.

    This intentionally keeps assumptions minimal until the Protein format is mapped.
    """
    if not data:
        raise ValueError("Empty SysEx payload")
    if data[0] != 0xF0 or data[-1] != 0xF7:
        raise ValueError("Invalid SysEx framing: expected F0 ... F7")

    return {
        "start": data[0],
        "manufacturer_or_ext": data[1:4],
        "payload": data[4:-1],
        "end": data[-1],
        "length": len(data),
    }
