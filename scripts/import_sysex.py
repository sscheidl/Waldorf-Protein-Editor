from pathlib import Path

from protein_editor import parse_sysex


def main() -> None:
    dumps_dir = Path("data/sysex_dumps")
    files = sorted(dumps_dir.glob("*.syx"))
    if not files:
        print("No .syx files found in data/sysex_dumps")
        return

    for file in files:
        blob = file.read_bytes()
        parsed = parse_sysex(blob)
        print(f"{file.name}: len={parsed['length']} payload={len(parsed['payload'])}")


if __name__ == "__main__":
    main()
