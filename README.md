# Waldorf Protein Editor

Repository scaffold for a community-driven patch editor and SysEx analysis toolkit for the Waldorf Protein.

## Goals

- Parse and validate Waldorf Protein SysEx dumps
- Build parameter mapping from controlled dump comparisons
- Provide foundations for a future patch editor

## Quick Start

```bash
python -m venv .venv
. .venv/Scripts/activate
pip install -e .[dev]
pytest
```

## Repository Layout

- `src/protein_editor`: Core parser and model code
- `tests`: Unit tests
- `docs`: Reverse engineering notes and mapping docs
- `data/sysex_dumps`: Local SysEx examples (not committed by default)
- `scripts`: Helper scripts

## Next Steps

1. Add real SysEx dump samples into `data/sysex_dumps`
2. Extend parser for model-specific headers and checksums
3. Start parameter map in `docs/parameter-map-template.csv`
