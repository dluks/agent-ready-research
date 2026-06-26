#!/usr/bin/env python3
"""Inventory a research folder without modifying it."""

from __future__ import annotations

import argparse
import os
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


LARGE_BYTES = 50 * 1024 * 1024
SECRET_HINTS = ("secret", "token", "password", "passwd", "credential", ".env", "api_key")
DATA_EXTS = {
    ".csv",
    ".tsv",
    ".xlsx",
    ".xls",
    ".parquet",
    ".feather",
    ".nc",
    ".nc4",
    ".h5",
    ".hdf5",
    ".zarr",
    ".tif",
    ".tiff",
    ".gpkg",
    ".geojson",
    ".shp",
}
NOTE_EXTS = {".md", ".txt", ".docx", ".tex", ".bib", ".pdf"}
CODE_EXTS = {".py", ".r", ".R", ".jl", ".sh", ".sql"}
FIGURE_EXTS = {".png", ".jpg", ".jpeg", ".svg", ".pdf"}
SKIP_DIRS = {".git", "__pycache__", ".venv", "node_modules", ".ipynb_checkpoints"}


@dataclass
class Entry:
    path: Path
    size: int
    kind: str
    flags: list[str]


def classify(path: Path, size: int) -> tuple[str, list[str]]:
    name = path.name.lower()
    suffix = path.suffix.lower()
    flags: list[str] = []

    if any(hint in name for hint in SECRET_HINTS):
        flags.append("possible secret")
    if size >= LARGE_BYTES:
        flags.append("large")

    if path.name == ".git":
        return "git metadata", flags
    if suffix == ".ipynb":
        return "notebook", flags
    if suffix in CODE_EXTS:
        return "code", flags
    if suffix in DATA_EXTS or name.endswith(".zarr"):
        return "data", flags
    if suffix in NOTE_EXTS:
        return "notes or writing", flags
    if suffix in FIGURE_EXTS:
        return "figure or document", flags
    return "other", flags


def walk(root: Path) -> list[Entry]:
    entries: list[Entry] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        current = Path(dirpath)
        if ".git" in dirnames:
            rel = current.relative_to(root)
            entries.append(Entry(rel / ".git", 0, "nested git repository", []))
        for filename in filenames:
            full = current / filename
            try:
                size = full.stat().st_size
            except OSError:
                continue
            rel = full.relative_to(root)
            kind, flags = classify(rel, size)
            entries.append(Entry(rel, size, kind, flags))
    return entries


def human_size(size: int) -> str:
    units = ("B", "KB", "MB", "GB", "TB")
    value = float(size)
    for unit in units:
        if value < 1024 or unit == units[-1]:
            return f"{value:.1f} {unit}" if unit != "B" else f"{int(value)} B"
        value /= 1024
    return f"{size} B"


def render_markdown(root: Path, entries: list[Entry]) -> str:
    by_kind = Counter(entry.kind for entry in entries)
    by_ext = Counter(entry.path.suffix.lower() or "[none]" for entry in entries)
    flagged = [entry for entry in entries if entry.flags]
    examples: dict[str, list[Entry]] = defaultdict(list)
    for entry in entries:
        if len(examples[entry.kind]) < 12:
            examples[entry.kind].append(entry)

    lines = [
        "# Migration Inventory",
        "",
        f"Source folder: `{root}`",
        f"Files scanned: {sum(1 for e in entries if e.kind != 'nested git repository')}",
        "",
        "## File Kinds",
        "",
        "| Kind | Count |",
        "| ---- | ----- |",
    ]
    for kind, count in by_kind.most_common():
        lines.append(f"| {kind} | {count} |")

    lines.extend(["", "## Common Extensions", "", "| Extension | Count |", "| --------- | ----- |"])
    for ext, count in by_ext.most_common(20):
        lines.append(f"| `{ext}` | {count} |")

    lines.extend(["", "## Flagged Files", "", "| Path | Size | Flags |", "| ---- | ---- | ----- |"])
    if flagged:
        for entry in flagged[:100]:
            lines.append(
                f"| `{entry.path}` | {human_size(entry.size)} | {', '.join(entry.flags)} |"
            )
    else:
        lines.append("| None found |  |  |")

    lines.extend(["", "## Examples By Kind"])
    for kind in sorted(examples):
        lines.extend(["", f"### {kind}", ""])
        for entry in examples[kind]:
            lines.append(f"- `{entry.path}` ({human_size(entry.size)})")

    lines.extend(
        [
            "",
            "## Next Questions",
            "",
            "- Which notebooks, scripts, or documents are canonical?",
            "- Which files are scratch, obsolete, or duplicated?",
            "- Which data should stay outside git?",
            "- Is this a single project or an umbrella with entries under `projects/`?",
            "- Are any nested git repositories separate projects for `projects/`?",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--out", type=Path, default=Path("migration_inventory.md"))
    args = parser.parse_args()

    source = args.source.expanduser().resolve()
    if not source.exists() or not source.is_dir():
        raise SystemExit(f"Source folder does not exist or is not a directory: {source}")

    entries = walk(source)
    args.out.write_text(render_markdown(source, entries), encoding="utf-8")
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
