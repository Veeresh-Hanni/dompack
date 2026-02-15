# Dompack

Domain-based Python tech stack installer.

Install one package and quickly set up bundles for web, ML, AI, databases, security, and more.

## Install

```bash
pip install dompk
```

Commands after install:

```bash
dompack --version
dompk --version
```

`dompack` and `dompk` both run the same CLI.

## Quick Usage

List bundles:

```bash
dompack list
dompk list
```

Install a bundle:

```bash
dompack install <bundle>
dompk install <bundle>
```

Full developer setup:

```bash
dompack install pydev
```

Equivalent with alias:

```bash
dompk install pydev
```

## Installer Backends

Auto (default, prefers `uv` if available):

```bash
dompack install web
dompk install web
```

Force `uv pip`:

```bash
dompack --installer uv install web
dompk --installer uv install web
```

Force `pip`:

```bash
dompack --installer pip install web
dompk --installer pip install web
```

## Linux (Debian/RPM) PEP 668

If system Python is externally managed, Dompack automatically retries installs in a local virtual environment (`.venv` if valid, otherwise `.dompack-venv`).

Advanced override (system Python):

```bash
dompack --break-system-packages install web
dompk --break-system-packages install web
```

## Bundle Aliases

- Core aliases: `common`, `core`, `base`
- Full setup aliases: `all`, `pydev`, `dev`, `setup`, `python`
- Python tooling aliases: `bootstrap`, `boot`, `pytools`

Examples:

```bash
dompack install fa
dompack install dj
dompack install ml
dompack install security
dompack install bootstrap
```

## Other Commands

```bash
dompack upgrade <bundle>
dompack search <keyword>
dompack doctor
dompack update-self
dompack req <bundle>
dompack create-bundle <name> <pkg1> <pkg2> ...
```

## Notes

- Package name on PyPI: `dompk`
- Console commands: `dompack`, `dompk`
- Current release: `0.0.2`

## License

MIT
