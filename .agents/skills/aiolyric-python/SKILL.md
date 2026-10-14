---
name: aiolyric-python
description: Work on aiolyric, the Python library for the Honeywell Lyric (Resideo) API. Use when changing its models, client, update methods, tests or packaging, or when running its lint, type check, test or build tasks.
---

# aiolyric Python

The `aiolyric` package is the library Home Assistant's `lyric` integration uses to read and control Honeywell Lyric thermostats through Resideo's API.

## Tasks

All tasks live in `mise.toml` and run from the repository root. mise provides Python and uv, and the tasks keep the venv at `.venv`.

- **Lint, type check and test**: `mise run check`
- **Lint**: `mise run lint` (Ruff, Ruff format check and Pylint)
- **Type check**: `mise run typecheck`
- **Format**: `mise run format`
- **Test all**: `mise run test`
- **Test single**: `mise run test tests/test_module.py::test_function`
- **Build**: `mise run build`

CI runs `mise run -c lint ::: typecheck ::: test ::: build` from `.github/workflows/check.yml`.

## Code Style

- **Python**: the `requires-python` version in `pyproject.toml`, which follows Home Assistant. Don't use `from __future__ import annotations`.
- **Formatting**: 4-space indentation, Ruff formatter, 88 char line length
- **Imports**: sorted by Ruff, absolute imports for parent modules
- **Types**: Use type hints, prefer `|` union syntax, dataclasses with slots
- **Naming**: snake_case for variables/functions, PascalCase for classes
- **Error handling**: Use specific exceptions, avoid bare except clauses
- **Docstrings**: Google-style, present tense

## API responses

- Check field names and casing against Resideo's docs at <https://developer.honeywellhome.com/lyric/apis>. Live responses sometimes differ from the docs (for example `Enabled` and `Day`), so read the documented key first and fall back to the observed one rather than replacing it.
- Ask contributors for a redacted live response when a field isn't in the public docs.

## Tests

- pytest with syrupy for snapshots. `asyncio_mode` is `auto`.
- `tests/conftest.py` mocks every API URL with aioresponses, and `tests/__init__.py` holds the fixture responses. Add a mock there for any new endpoint.
- For update methods, assert on the JSON actually sent (see `last_sent_json` in `tests/test_init.py`), not only that the call succeeds.
