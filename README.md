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

## AI Transparency

This repository contains AI-assisted code contributions (primarily generated or edited with Codex).

Human code review has not been completed for all recent changes.
Validation so far is mainly automated and local testing plus AI cross-checks (for example Claude Sonnet), not formal manual QA.
Please treat the current state as actively evolving and verify behavior in your own setup.

## Contributing

Contributions are welcome.

Bug reports, reproducible test cases, and pull requests are appreciated.
If you spot issues in MIDI parsing, monitoring, or SysEx handling, please open an issue with logs and sample data.
Community improvements and review help are explicitly invited.

## Next Steps

1. Add real SysEx dump samples into `data/sysex_dumps`
2. Extend parser for model-specific headers and checksums
3. Start parameter map in `docs/parameter-map-template.csv`
