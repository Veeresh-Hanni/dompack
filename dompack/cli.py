import argparse
import subprocess
import sys
from importlib import metadata
from .bundles import EXTRAS

HELP = "dompack — domain-based Python tech stack installer (CLI)"


def list_bundles():
    print("Available dompack bundles:\n")
    keys = sorted(EXTRAS.keys())
    for name in keys:
        print(f"  - {name}: pip install dompack[{name}]")
    print("\nTip: use short aliases like 'fa' for fastapi, 'fl' for flask, 'db' for databases.")


def show_version():
    try:
        print(metadata.version("dompack"))
    except Exception:
        from . import __version__
        print(__version__)


def install_bundle(name):
    if name not in EXTRAS:
        print(f"Unknown bundle: {name}")
        return 1

    pkg = f"dompack[{name}]"
    print(f"Running: pip install {pkg}")

    # Use the current Python interpreter's pip
    cmd = [sys.executable, "-m", "pip", "install", pkg]
    return subprocess.call(cmd)


def main(argv=None):
    parser = argparse.ArgumentParser(prog="dompack", description=HELP)
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("list", help="List available bundles")

    p_install = sub.add_parser("install", help="Install a bundle: dompack install <name>")
    p_install.add_argument("bundle", help="Bundle name (eg: fa, fl, db, ml, all)")

    parser.add_argument("--version", action="store_true", help="Show version")

    args = parser.parse_args(argv)

    if args.version:
        show_version()
        return

    if args.cmd == "list":
        list_bundles()
        return

    if args.cmd == "install":
        return_code = install_bundle(args.bundle)
        if return_code != 0:
            print("pip returned non-zero exit code", return_code)
        return

    parser.print_help()


if __name__ == "__main__":
    main()
