#!/usr/bin/env python3
"""Strip any `.devN` suffix from the package version in setup.py."""

from __future__ import annotations

import re
from pathlib import Path


def main() -> None:
    """Strip any `.devN` suffix from the package version in setup.py."""
    project_root = Path(__file__).resolve().parents[1]
    setup_path = project_root / "setup.py"
    contents = setup_path.read_text(encoding="utf-8")

    match = re.search(r'version="([^"]+)"', contents)
    if not match:
        raise SystemExit("version field not found in setup.py")

    version = match.group(1)
    new_version = re.sub(r"\.dev\d*$", "", version)

    if new_version == version:
        print("No dev suffix to strip")
        return

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
