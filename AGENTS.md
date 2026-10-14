# aiolyric - Agent Guidelines

Python library for the Honeywell Lyric API.

## Quick Start

Tools (Python, uv) are pinned in `mise.toml`. Run tasks with `mise run <task>`.

- **Check everything**: `mise run check`
- **Lint**: `mise run lint` (Ruff, Ruff format check, Pylint)
- **Type check**: `mise run typecheck` (mypy)
- **Format**: `mise run format`
- **Test all**: `mise run test`
- **Test single**: `uv run --no-sync pytest tests/test_module.py::test_function`
- **Build**: `mise run build`

## Versioning and releases

The committed version in `pyproject.toml` is a `0.0.0` placeholder. Publishing a
GitHub release sets the version from the release tag and publishes to PyPI with
trusted publishing (`.github/workflows/release.yml`). Don't bump versions in
commits.

Python and aiohttp follow Home Assistant's versions through Renovate.

## Code Style

- **Python**: 3.14+, don't use `from __future__ import annotations`
- **Formatting**: Ruff formatter, 4-space indentation
- **Imports**: Ruff isort rules, absolute imports for parent modules
- **Types**: Use type hints, prefer `|` union syntax, dataclasses with slots
- **Naming**: snake_case for variables/functions, PascalCase for classes
- **Error handling**: Use specific exceptions, avoid bare except clauses
- **Docstrings**: Google-style, present tense
- **Testing**: Use pytest with syrupy for snapshots
