# Contributing

This repository currently includes AI-assisted code contributions (primarily generated or edited with Codex).
Please verify behavior in your own setup, especially for MIDI parsing, monitoring, and SysEx handling.

## Branching

- Use feature branches from `main`
- Keep commits focused and descriptive

## Pull Requests

- Include a concise summary and test notes
- Link related issues
- Keep diffs small when possible
- Include reproducible steps or sample data when fixing parser, monitoring, or SysEx issues

## Development

```bash
pip install -e .[dev]
pytest
```

## Reporting Issues

- Bug reports and reproducible test cases are appreciated
- If possible, include logs and sample SysEx or MIDI data
- Community improvements and review help are explicitly invited
