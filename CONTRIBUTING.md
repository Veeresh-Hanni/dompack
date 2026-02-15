# Contributing

Thanks for contributing to Dompack.

## Prerequisites

- Python 3.8+
- Git

## Setup

```bash
git clone https://github.com/<your-username>/dompack.git
cd dompack
python -m venv .venv
```

Activate:

- Linux/macOS: `source .venv/bin/activate`
- Windows PowerShell: `.\.venv\Scripts\Activate.ps1`

Install editable:

```bash
pip install -e .
```

## Build

```bash
python -m build
python -m twine check dist/*
```

## Run CLI Locally

```bash
python -m dompack.cli list
python -m dompack.cli install web
```

## Code Guidelines

- Keep `dompack/bundles.py` and `pyproject.toml` extras in sync.
- Prefer Python 3.8-compatible syntax.
- Keep CLI output clear and actionable.
- Update docs and changelog with behavior changes.

## Release Flow

1. Bump version in:
   - `pyproject.toml`
   - `dompack/__init__.py`
2. Build:
   - `python -m build`
3. Validate:
   - `python -m twine check dist/*`
4. Publish:
   - `python -m twine upload dist/*`

## Commit Prefixes

- `feat:` new feature
- `fix:` bug fix
- `docs:` documentation
- `refactor:` code cleanup
- `test:` tests
- `chore:` maintenance
