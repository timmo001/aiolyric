#!/usr/bin/env python3
"""Ensure the package version in setup.py has a `.dev0` suffix.

If the version already includes a `.dev` suffix, no change is made.
"""

from __future__ import annotations

from pathlib import Path
import re


def main() -> None:
    """Ensure the package version in setup.py has a `.dev0` suffix."""
    project_root = Path(__file__).resolve().parents[1]
    setup_path = project_root / "setup.py"
    contents = setup_path.read_text(encoding="utf-8")

    match = re.search(r'version="([^"]+)"', contents)
    if not match:
        raise SystemExit("version field not found in setup.py")

    version = match.group(1)
    if "dev" in version:
        print("Version already has dev suffix, no change")
        return

    new_version = f"{version}.dev0"
    new_contents = contents.replace(
        f'version="{version}"', f'version="{new_version}"', 1
    )

    setup_path.write_text(new_contents, encoding="utf-8")

    # Keep aiolyric/_version.py in sync if present
    module_version_path = project_root / "aiolyric" / "_version.py"
    if module_version_path.exists():
        module_version_path.write_text(
            (
                '"""Provides aiolyric version information."""\n\n'
                "# Maintained by scripts in ./script/ and the version in setup.py\n\n"
                f'__version__ = "{new_version}"\n'
                '__all__ = ["__version__"]\n'
            ),
            encoding="utf-8",
        )
    print(f"Updated version to {new_version}")


if __name__ == "__main__":
    main()
