# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A personal learning sandbox for advanced Python features (Python 3.14, managed with `uv`). There is no test suite, no CI, and no build step. Most files are standalone demo scripts, not a cohesive application.

## Commands

```bash
uv sync                                   # install all workspace members into .venv
uv run python src/<topic>/<file>.py       # run a standalone demo script
uv run python -m protocols.main           # packages with absolute imports: run from src/ (cd src first)
uv run python expense_tracker/main.py     # expense_tracker app, from repo root
ruff check . && ruff format .             # lint/format (ruff is installed globally, not a project dep)
```

## Layout

- `src/<topic>/` — one folder per concept (decorators, descriptors, generators, metaclasses, generics/TypeVars, context managers, iterators, protocols, etc.). Scripts are independent; there is no shared library code. `src/recheck/` holds revision rewrites of the same topics.
- `src/protocols/` and `src/abc_protocols/` are near-duplicate IoT-device examples (`Device` base, `devices`, `service.IoTService`, `diagonistics`). They import themselves by absolute package name (`from protocols import ...`), so they must be run with `src/` as the working directory / on `sys.path`.
- `expense_tracker/` — a small app and a **uv workspace member** of the root project. Its modules (`main.py` → `initiate.py` → `expense.py`) use flat, non-package imports (`import initiate`); this works when run as a script (`python expense_tracker/main.py`) because the script's directory lands on `sys.path`, but not via `-m` from the repo root.
- `expense_tracker/packages/tax_calulation/` — a second workspace member (src-layout, `uv_build` backend) that `expense_tracker` depends on via `[tool.uv.sources] tax-calulation = { workspace = true }`. Note the package name is spelled `tax_calulation` (sic) everywhere; keep that spelling when importing.

The workspace is declared in the root `pyproject.toml` under `[tool.uv.workspace]`; add new local packages there and reference them from dependents with `{ workspace = true }`.
