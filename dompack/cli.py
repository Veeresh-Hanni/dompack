import argparse
import os
import shutil
import subprocess
import sys
from importlib import metadata
from typing import List, Optional

from .bundles import EXTRAS

HELP = "dompk - domain-based Python tech stack installer"
ALIAS_BUNDLES = {
    "dev": "all",
    "pydev": "all",
    "setup": "all",
    "python": "all",
}
AUTO_VENV_PYTHON: Optional[str] = None


def run(cmd: List[str]) -> int:
    """Run a shell command and return exit code."""
    print(">>", " ".join(cmd))
    return subprocess.call(cmd)


def run_capture(cmd: List[str]) -> subprocess.CompletedProcess:
    """Run a command and capture output for controlled retry logic."""
    print(">>", " ".join(cmd))
    return subprocess.run(cmd, text=True, capture_output=True)


def _python_in_venv() -> bool:
    return sys.prefix != getattr(sys, "base_prefix", sys.prefix)


def _detect_linux_family() -> str:
    """Return linux family hint: debian, rpm, or unknown."""
    if not sys.platform.startswith("linux"):
        return "unknown"
    try:
        with open("/etc/os-release", "r", encoding="utf-8") as file_obj:
            data = file_obj.read().lower()
        if any(x in data for x in ["debian", "ubuntu", "kali", "mint"]):
            return "debian"
        if any(x in data for x in ["fedora", "rhel", "centos", "rocky", "alma", "suse"]):
            return "rpm"
    except Exception:
        pass
    return "unknown"


def _linux_help_for_venv() -> None:
    family = _detect_linux_family()
    print("\nInstall venv tooling and retry:")
    if family == "debian":
        print("  sudo apt update && sudo apt install -y python3-venv python3-pip")
    elif family == "rpm":
        print("  sudo dnf install -y python3 python3-pip python3-virtualenv")
    else:
        print("  Install python3-venv/python3-virtualenv and python3-pip via your distro.")


def _local_venv_python() -> str:
    def find_python(venv_dir: str) -> str:
        candidates = [
            os.path.join(venv_dir, "bin", "python"),
            os.path.join(venv_dir, "Scripts", "python.exe"),
            os.path.join(venv_dir, "Scripts", "python"),
        ]
        for candidate in candidates:
            if os.path.exists(candidate):
                return candidate
        return ""

    # Reuse any valid local venv first.
    for existing in [".venv", ".dompack-venv"]:
        if os.path.isdir(existing):
            python_bin = find_python(existing)
            if python_bin:
                return python_bin

    # Create a dedicated venv when existing .venv is cross-platform-incompatible.
    venv_dir = ".dompack-venv"
    print(f"Creating local virtual environment: {venv_dir}")
    code = run([sys.executable, "-m", "venv", venv_dir])
    if code != 0:
        _linux_help_for_venv()
        return ""

    python_bin = find_python(venv_dir)
    if not python_bin:
        print(f"ERROR: venv python not found in {venv_dir}")
        return ""
    return python_bin


def resolve_installer(installer: str) -> Optional[str]:
    """Resolve installer backend: uv, pip, or auto."""
    if installer == "pip":
        return "pip"
    if installer == "uv":
        return "uv" if shutil.which("uv") else None
    if installer == "auto":
        return "uv" if shutil.which("uv") else "pip"
    return None


def pip_install(
    *packages: str,
    upgrade: bool = False,
    installer: str = "auto",
    break_system_packages: bool = False,
) -> int:
    """Install package(s) using uv pip or pip."""
    global AUTO_VENV_PYTHON
    selected = resolve_installer(installer)
    if selected is None:
        print("ERROR: uv was requested but not found in PATH.")
        print("Install uv or run with --installer pip.")
        return 1

    if selected == "uv":
        cmd = ["uv", "pip", "install"]
        if break_system_packages:
            cmd.append("--system")
        if upgrade:
            cmd.append("--upgrade")
        cmd.extend(packages)
        return run(cmd)
    else:
        if (
            AUTO_VENV_PYTHON
            and sys.platform.startswith("linux")
            and not _python_in_venv()
            and not break_system_packages
        ):
            cmd = [AUTO_VENV_PYTHON, "-m", "pip", "install"]
        else:
            cmd = [sys.executable, "-m", "pip", "install"]

    if break_system_packages:
        cmd.append("--break-system-packages")
    if upgrade:
        cmd.append("--upgrade")
    cmd.extend(packages)

    proc = run_capture(cmd)
    if proc.stdout:
        print(proc.stdout, end="")
    if proc.stderr:
        print(proc.stderr, end="", file=sys.stderr)
    if proc.returncode == 0:
        return 0

    externally_managed = "externally-managed-environment" in (proc.stderr or "").lower()
    if (
        selected == "pip"
        and externally_managed
        and sys.platform.startswith("linux")
        and not _python_in_venv()
        and not break_system_packages
    ):
        print(
            "\nDetected externally managed Python on Linux. "
            "Retrying inside a local virtual environment."
        )
        AUTO_VENV_PYTHON = AUTO_VENV_PYTHON or _local_venv_python()
        if not AUTO_VENV_PYTHON:
            return proc.returncode
        retry_cmd = [AUTO_VENV_PYTHON, "-m", "pip", "install"]
        if upgrade:
            retry_cmd.append("--upgrade")
        retry_cmd.extend(packages)
        return run(retry_cmd)

    return proc.returncode


def list_bundles() -> int:
    print("Available dompack bundles:\n")
    all_names = sorted(set(EXTRAS.keys()) | set(ALIAS_BUNDLES.keys()))
    for name in all_names:
        if name in ALIAS_BUNDLES:
            print(f"  - {name} -> {ALIAS_BUNDLES[name]}")
        else:
            print(f"  - {name}")
    print("\nRun: dompack install <bundle>")
    return 0


def show_version() -> int:
    try:
        print(metadata.version("dompk"))
    except Exception:
        from . import __version__

        print(__version__)
    return 0


def resolve_bundle(name: str) -> Optional[str]:
    normalized = name.lower()
    if normalized in EXTRAS:
        return normalized
    return ALIAS_BUNDLES.get(normalized)


def install_packages(
    packages: List[str],
    installer: str,
    upgrade: bool = False,
    strict: bool = False,
    break_system_packages: bool = False,
) -> int:
    failed: List[str] = []
    for pkg in packages:
        code = pip_install(
            pkg,
            installer=installer,
            upgrade=upgrade,
            break_system_packages=break_system_packages,
        )
        if code != 0:
            failed.append(pkg)
            if strict:
                break

    if failed:
        print("\nSome packages failed:")
        for pkg in failed:
            print(f"  - {pkg}")
        if strict:
            return 1
        print("\nContinuing because strict mode is disabled.")
        return 0
    return 0


def install_bundle(
    name: str, installer: str, strict: bool, break_system_packages: bool
) -> int:
    bundle = resolve_bundle(name)
    if bundle is None:
        print(f"Unknown bundle: {name}")
        return 1

    print(f"Installing bundle '{name}' using '{bundle}' package set.")
    return install_packages(
        EXTRAS[bundle],
        installer=installer,
        strict=strict,
        break_system_packages=break_system_packages,
    )


def upgrade_bundle(
    name: str, installer: str, strict: bool, break_system_packages: bool
) -> int:
    bundle = resolve_bundle(name)
    if bundle is None:
        print(f"Unknown bundle: {name}")
        return 1

    print(f"Upgrading packages in bundle '{name}'...\n")
    code = install_packages(
        EXTRAS[bundle],
        installer=installer,
        upgrade=True,
        strict=strict,
        break_system_packages=break_system_packages,
    )
    print("\nUpgrade completed.")
    return code


def search(keyword: str) -> int:
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


def doctor() -> int:
    print("\nRunning dompack environment diagnostics...\n")
    print(f"Python executable: {sys.executable}")
    print(f"Python version: {sys.version}\n")

    try:
        pip_v = subprocess.check_output(
            [sys.executable, "-m", "pip", "--version"], text=True
        )
        print("Pip:", pip_v.strip())
    except Exception:
        print("ERROR: pip not found!")

    print("\nChecking installed packages...\n")
    installed = {
        dist.metadata["Name"].lower().replace("_", "-")
        for dist in metadata.distributions()
        if dist.metadata.get("Name")
    }

    for name, pkgs in EXTRAS.items():
        missing = []
        for pkg in pkgs:
            base = pkg.split("[")[0].lower().replace("_", "-")
            if base not in installed:
                missing.append(pkg)

        if missing:
            print(f"[{name}] Missing:")
            for m in missing:
                print(f"  - {m}")
            print()
        else:
            print(f"[{name}] OK all packages installed.\n")

    print("Doctor complete.")
    return 0


def update_self(installer: str, break_system_packages: bool) -> int:
    print("Updating dompk to latest version...")
    return pip_install(
        "dompk",
        upgrade=True,
        installer=installer,
        break_system_packages=break_system_packages,
    )


def generate_requirements(bundle: str) -> int:
    resolved = resolve_bundle(bundle)
    if resolved is None:
        print(f"Unknown bundle: {bundle}")
        return 1

    filename = f"requirements-{bundle}.txt"
    with open(filename, "w", encoding="utf-8") as file_obj:
        for pkg in EXTRAS[resolved]:
            file_obj.write(pkg + "\n")

    print(f"Generated {filename}")
    return 0


def create_bundle(name: str, pkgs: List[str]) -> int:
    name = name.lower()
    EXTRAS[name] = pkgs

    print(f"Created custom bundle '{name}':")
    for pkg in pkgs:
        print(f"  - {pkg}")
    print("\nYou must manually save this bundle into bundles.py")
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="dompk", description=HELP)
    parser.add_argument(
        "--installer",
        choices=["auto", "pip", "uv"],
        default="auto",
        help="Package installer backend (default: auto, prefers uv when available)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Stop bundle install/upgrade on first package error",
    )
    parser.add_argument(
        "--break-system-packages",
        action="store_true",
        help="Pass --break-system-packages to pip on Linux system Python",
    )
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("list", help="List all bundles")
    sub.add_parser("doctor", help="Check environment")
    sub.add_parser("update-self", help="Update dompk")

    p_install = sub.add_parser("install", help="Install bundle: dompk install <name>")
    p_install.add_argument("bundle")

    p_upgrade = sub.add_parser("upgrade", help="Upgrade bundle")
    p_upgrade.add_argument("bundle")

    p_search = sub.add_parser("search", help="Search packages inside bundles")
    p_search.add_argument("keyword")

    p_gen = sub.add_parser("req", help="Generate requirements.txt for a bundle")
    p_gen.add_argument("bundle")

    p_new = sub.add_parser("create-bundle", help="Create new custom bundle")
    p_new.add_argument("name")
    p_new.add_argument("packages", nargs="+")

    parser.add_argument("--version", action="store_true")
    args = parser.parse_args(argv)

    if args.version:
        return show_version()
    if args.cmd == "list":
        return list_bundles()
    if args.cmd == "install":
        return install_bundle(
            args.bundle, args.installer, args.strict, args.break_system_packages
        )
    if args.cmd == "upgrade":
        return upgrade_bundle(
            args.bundle, args.installer, args.strict, args.break_system_packages
        )
    if args.cmd == "search":
        return search(args.keyword)
    if args.cmd == "doctor":
        return doctor()
    if args.cmd == "update-self" or args.cmd == "update":
        return update_self(args.installer, args.break_system_packages)
    if args.cmd == "req":
        return generate_requirements(args.bundle)
    if args.cmd == "create-bundle":
        return create_bundle(args.name, args.packages)

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
