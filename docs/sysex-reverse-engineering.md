# SysEx Reverse Engineering Notes

## Suggested workflow

1. Capture an INIT patch dump.
2. Change exactly one parameter on the device.
3. Capture a second dump.
4. Diff payload bytes and log changed offsets.
5. Repeat for each parameter class.

## Record template

- Dump A file:
- Dump B file:
- Changed parameter:
- Byte offset(s):
- Value mapping hypothesis:
- Confirmed range:
