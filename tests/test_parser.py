import pytest

from protein_editor import parse_sysex


def test_parse_sysex_valid_message() -> None:
    msg = bytes([0xF0, 0x00, 0x20, 0x33, 0x10, 0x7F, 0x00, 0xF7])
    parsed = parse_sysex(msg)
    assert parsed["start"] == 0xF0
    assert parsed["end"] == 0xF7
    assert parsed["payload"] == bytes([0x10, 0x7F, 0x00])


def test_parse_sysex_empty_rejected() -> None:
    with pytest.raises(ValueError):
        parse_sysex(b"")


def test_parse_sysex_invalid_frame_rejected() -> None:
    with pytest.raises(ValueError):
        parse_sysex(bytes([0x00, 0x01, 0xF7]))
