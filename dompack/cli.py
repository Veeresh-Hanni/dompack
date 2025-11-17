import argparse
import subprocess
import sys
import shutil
import os
import pkgutil
from importlib import metadata

from .bundles import EXTRAS

HELP = "dompack — domain-based Python tech stack installer"


# -----------------------------------------
# UTILITIES
# -----------------------------------------
def run(cmd: list):
    """Run a shell command."""
    print(">>", " ".join(cmd))
    return subprocess.call(cmd)


def pip_install(package: str):
    """Install a package using current interpreter."""
    cmd = [sys.executable, "-m", "pip", "install", package]
    return run(cmd)


# -----------------------------------------
# BASIC COMMANDS
# -----------------------------------------
def list_bundles():
    print("Available dompack bundles:\n")
    for name in sorted(EXTRAS.keys()):
        print(f"  - {name}: pip install dompack[{name}]")
    print("\nRun: dompack install <bundle>")


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
    print(f"Installing: {pkg}")
    return pip_install(pkg)


# -----------------------------------------
# UPGRADE BUNDLE
# -----------------------------------------
def upgrade_bundle(name):
    if name not in EXTRAS:
        print(f"Unknown bundle: {name}")
        return 1

    print(f"Upgrading packages in bundle '{name}'...\n")
    for pkg in EXTRAS[name]:
        pip_install(f"--upgrade {pkg}")
    print("\n✓ Upgrade completed.")
    return 0


# -----------------------------------------
# SEARCH PACKAGES
# -----------------------------------------
def search(keyword):
    print(f"Searching bundles for: '{keyword}'\n")

    keyword = keyword.lower()
    found = False

    for name, pkgs in EXTRAS.items():
        matches = [p for p in pkgs if keyword in p.lower()]
        if matches:
            found = True
            print(f"[{name}]")
            for m in matches:
                print(f"  - {m}")
            print()

    if not found:
        print("No matching packages found.")
    return 0


# -----------------------------------------
# DOCTOR - Environment Checker
# -----------------------------------------
def doctor():
    print("\n🔍 Running dompack environment diagnostics...\n")

    # python version
    print(f"Python executable: {sys.executable}")
    print(f"Python version: {sys.version}\n")

    # pip version
    try:
        pip_v = subprocess.check_output([sys.executable, "-m", "pip", "--version"]).decode()
        print("Pip:", pip_v)
    except:
        print("ERROR: pip not found!")

    # check installed bundles
    print("Checking installed packages...\n")
    installed = {p.name.lower() for p in pkgutil.iter_modules()}

    for name, pkgs in EXTRAS.items():
        missing = [p for p in pkgs if p.split("[")[0] not in installed]
        if missing:
            print(f"[{name}] Missing:")
            for m in missing:
                print("  -", m)
            print()
        else:
            print(f"[{name}] ✓ All packages installed.\n")

    print("\nDoctor complete.")
    return 0


# -----------------------------------------
# UPDATE SELF
# -----------------------------------------
def update_self():
    print("Updating dompack to latest version...")
    pip_install("--upgrade dompack")
    return 0


# -----------------------------------------
# GENERATE REQUIREMENTS
# -----------------------------------------
def generate_requirements(bundle):
    if bundle not in EXTRAS:
        print("Unknown bundle:", bundle)
        return 1

    filename = f"requirements-{bundle}.txt"
    with open(filename, "w") as f:
        for pkg in EXTRAS[bundle]:
            f.write(pkg + "\n")

    print(f"✓ Generated {filename}")
    return 0


# -----------------------------------------
# CREATE CUSTOM BUNDLE
# -----------------------------------------
def create_bundle(name, pkgs):
    name = name.lower()

    EXTRAS[name] = pkgs
    print(f"Created custom bundle '{name}':")
    for p in pkgs:
        print("  -", p)
    print("\n(You must manually save this bundle into bundles.py)")
    return 0


# -----------------------------------------
# MAIN
# -----------------------------------------
def main(argv=None):
    parser = argparse.ArgumentParser(prog="dompack", description=HELP)
    sub = parser.add_subparsers(dest="cmd")

    # core
    sub.add_parser("list", help="List all bundles")
    sub.add_parser("doctor", help="Check environment")
    sub.add_parser("update-self", help="Update dompack")

    # install
    p_install = sub.add_parser("install", help="Install bundle: dompack install <name>")
    p_install.add_argument("bundle")

    # upgrade
    p_upgrade = sub.add_parser("upgrade", help="Upgrade bundle")
    p_upgrade.add_argument("bundle")

    # search
    p_search = sub.add_parser("search", help="Search packages inside bundles")
    p_search.add_argument("keyword")

    # generate requirements
    p_gen = sub.add_parser("req", help="Generate requirements.txt for a bundle")
    p_gen.add_argument("bundle")

    # custom bundle
    p_new = sub.add_parser("create-bundle", help="Create new custom bundle")
    p_new.add_argument("name")
    p_new.add_argument("packages", nargs="+")

    # version flag
    parser.add_argument("--version", action="store_true")

    args = parser.parse_args(argv)

    # dispatch
    if args.version:
        return show_version()

    if args.cmd == "list":
        return list_bundles()

    if args.cmd == "install":
        return install_bundle(args.bundle)

    if args.cmd == "upgrade":
        return upgrade_bundle(args.bundle)

    if args.cmd == "search":
        return search(args.keyword)

    if args.cmd == "doctor":
        return doctor()

    if args.cmd == "update-self":
        return update_self()

    if args.cmd == "req":
        return generate_requirements(args.bundle)

    if args.cmd == "create-bundle":
        return create_bundle(args.name, args.packages)

    parser.print_help()


if __name__ == "__main__":
    main()
