# scripts/code_review_zipper.py

import os
import tarfile
from datetime import datetime
from pathlib import Path

# --- Configuration ---
include_paths = ["src/khora_adapter", "tests", "README.md", "mypi.ini", "pyproject.toml", ".coveragerc", "dir_structure.txt"]
exclude_patterns = ["__pycache__", ".git", ".env", "venv", "scripts"]
timestamp = datetime.now().strftime("%Y%m%d_%H%M")
output_file = f"code_review_package_{timestamp}.tar.gz"


def should_exclude(path: Path) -> bool:
    return any(part in exclude_patterns for part in path.parts)


def collect_files(base_paths):
    for path in base_paths:
        p = Path(path)
        if not p.exists():
            continue
        if p.is_file():
            if not should_exclude(p):
                yield p
        else:
            for file in p.rglob("*"):
                if file.is_file() and not should_exclude(file):
                    yield file


def main():
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent.resolve()
    artifacts_dir = project_root / "artifacts"
    artifacts_dir.mkdir(exist_ok=True)

    dest = artifacts_dir / output_file
    print(f"📦 Creating code review archive: {dest.name}")

    with tarfile.open(dest, "w:gz") as tar:
        for file in collect_files([project_root / p for p in include_paths]):
            try:
                arcname = file.relative_to(project_root)
                print(f"  + {arcname}")
                tar.add(file, arcname=str(arcname))
            except ValueError:
                print(f"  ⚠️ Skipped (outside project): {file}")
                continue

    print(f"✅ Archive created successfully: {dest}")


if __name__ == "__main__":
    main()
