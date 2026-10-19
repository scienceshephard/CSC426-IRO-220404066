#!/usr/bin/env python3
"""Create a print-friendly combined listing of the IRO implementation files."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "CODE-LISTING.txt"
SOURCES = (
    "app/index.html",
    "app/styles.css",
    "app/app.js",
    "google-forms/CreateIROForm.gs",
)

parts = [
    "IRO — ISSUES REPORTING OUTLET\n",
    "Student: Opeyemi Raphael-Ogbe | Matric number: 220404066\n",
    "Combined source listing. Generated from the project files.\n",
]
for relative_path in SOURCES:
    path = ROOT / relative_path
    parts.extend(("\n" + "=" * 88 + "\n", f"FILE: {relative_path}\n", "=" * 88 + "\n"))
    parts.append(path.read_text(encoding="utf-8"))
    if not parts[-1].endswith("\n"):
        parts.append("\n")

OUTPUT.write_text("".join(parts), encoding="utf-8")
print(f"Wrote {OUTPUT.relative_to(ROOT)}")
