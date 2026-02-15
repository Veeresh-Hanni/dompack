# Changelog

All notable changes to this project are documented here.

## 1.1.2 - 2026-02-15

- Added `dompk` console alias.
- Added installer backend selection: `--installer auto|pip|uv`.
- Added strict mode: `--strict`.
- Added Linux system Python flag: `--break-system-packages`.
- Added automatic Linux PEP 668 fallback to local venv when pip is externally managed.
- Fixed cross-OS venv handling (`.venv` Windows vs Linux layout mismatch).
- Added bundle aliases: `pydev`, `dev`, `setup`, `python` -> `all`.
- Added Python tooling bundle aliases: `bootstrap`, `boot`, `pytools`.
- Improved package compatibility markers in optional dependencies for heavy native packages.
- Synced docs and metadata with current CLI behavior.

## 1.1.1 - 2025-11-18

- Advanced CLI commands added:
  - `upgrade`
  - `search`
  - `doctor`
  - `update-self`
  - `req`
  - `create-bundle`
- Expanded optional dependency bundles.

## 0.1.0 - 2025-11-17

- Initial release with domain-based bundle installation.
- Basic CLI:
  - `dompack list`
  - `dompack install <bundle>`
