#!/usr/bin/env python3
"""Build a simple print bundle from the project Markdown and source listing."""

from html import escape
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def inline(text: str) -> str:
    text = escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    return text


def render_markdown(source: str) -> str:
    lines = source.splitlines()
    output: list[str] = []
    paragraph: list[str] = []
    list_kind: str | None = None
    code: list[str] | None = None
    table: list[str] | None = None

    def flush_paragraph() -> None:
        if paragraph:
            output.append("<p>" + inline(" ".join(part.strip() for part in paragraph)) + "</p>")
            paragraph.clear()

    def close_list() -> None:
        nonlocal list_kind
        if list_kind:
            output.append(f"</{list_kind}>")
            list_kind = None

    def flush_table() -> None:
        nonlocal table
        if not table:
            return
        rows = [[cell.strip() for cell in row.strip().strip("|").split("|")] for row in table]
        if len(rows) > 1 and all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in rows[1]):
            head, body = rows[0], rows[2:]
            output.append("<table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>")
            for row in body:
                output.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>")
            output.append("</tbody></table>")
        table = None

    for line in lines:
        if line.strip().startswith("```"):
            flush_paragraph(); close_list(); flush_table()
            if code is None:
                code = []
            else:
                output.append("<pre><code>" + escape("\n".join(code)) + "</code></pre>")
                code = None
            continue
        if code is not None:
            code.append(line)
            continue

        if line.strip().startswith("|"):
            flush_paragraph(); close_list()
            if table is None:
                table = []
            table.append(line)
            continue
        flush_table()

        heading = re.match(r"^(#{1,6})\s+(.*)$", line)
        if heading:
            flush_paragraph(); close_list()
            level = min(len(heading.group(1)), 4)
            output.append(f"<h{level}>{inline(heading.group(2))}</h{level}>")
            continue
        if re.match(r"^\s*---+\s*$", line):
            flush_paragraph(); close_list(); output.append("<hr>"); continue
        if line.startswith("> "):
            flush_paragraph(); close_list()
            output.append("<blockquote>" + inline(line[2:]) + "</blockquote>")
            continue
        bullet = re.match(r"^\s*[-*]\s+(.*)$", line)
        numbered = re.match(r"^\s*\d+\.\s+(.*)$", line)
        if bullet or numbered:
            flush_paragraph()
            wanted = "ul" if bullet else "ol"
            if list_kind != wanted:
                close_list(); output.append(f"<{wanted}>"); list_kind = wanted
            output.append("<li>" + inline((bullet or numbered).group(1)) + "</li>")
            continue
        if not line.strip():
            flush_paragraph(); close_list(); continue
        close_list()
        paragraph.append(line)

    flush_paragraph(); close_list(); flush_table()
    if code is not None:
        output.append("<pre><code>" + escape("\n".join(code)) + "</code></pre>")
    return "\n".join(output)


documents = (
    ("SRS.md", "Software Requirements Specification"),
    ("USE-CASES.md", "Use Cases"),
    ("ISHIKAWA-ANALYSIS.md", "Ishikawa Analysis"),
    ("OBJECT-LISTING.md", "Object Listing"),
)
parts = ["""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>IRO Coursework Submission Pack</title><style>
@page{size:A4;margin:16mm} @page wide{size:A4 landscape;margin:14mm}
*{box-sizing:border-box}body{font:10pt/1.45 Arial,Helvetica,sans-serif;color:#17231f;max-width:100%;margin:0}
h1{font-size:18pt;line-height:1.15;color:#153b35;margin:0 0 14pt}h2{font-size:14pt;color:#153b35;margin:16pt 0 8pt;break-after:avoid}
h3{font-size:11pt;color:#153b35;margin:12pt 0 5pt;break-after:avoid}h4{font-size:10pt;color:#153b35;margin:10pt 0 5pt}
p,li,td,th,blockquote{font-size:10pt}p{margin:5pt 0 8pt}ul,ol{padding-left:20pt;margin:5pt 0 10pt}li{margin:2pt 0}
table{border-collapse:collapse;width:100%;margin:8pt 0 12pt;break-inside:auto}tr{break-inside:avoid}td,th{border:1px solid #cbd5cc;padding:5pt;text-align:left;vertical-align:top}th{background:#edf4e7}
blockquote{margin:8pt 0;padding:7pt 11pt;border-left:3px solid #9bb78b;background:#f5f8f2}code,pre{font-family:"Courier New",monospace}pre{white-space:pre-wrap;overflow-wrap:anywhere;border:1px solid #d8dfd8;padding:8pt;line-height:1.3;break-inside:auto}code{font-size:9pt}pre code{font-size:10pt}a{color:#315a3b;text-decoration:none}hr{border:0;border-top:1px solid #ccd5cc;margin:13pt 0}
.page-break{break-before:page}.diagram-page{page:wide;break-before:page;text-align:center}.diagram-page img{width:100%;height:auto;max-height:175mm;object-fit:contain}.diagram-page h2{text-align:left}
.cover{padding-top:25mm;min-height:230mm}.cover .meta{border-top:2px solid #153b35;padding-top:12pt;margin-top:24pt}.small-note{font-size:9pt;color:#5f6f65}
@media screen{body{max-width:860px;margin:30px auto;padding:25px 38px;background:white;box-shadow:0 5px 35px #0002}.diagram-page{margin-top:35px}.page-break{margin-top:40px}}
</style></head><body>
<section class="cover"><p class="small-note">CSC426 WEEKLY DEV – WEEKEND 3</p><h1>IRO — Issues Reporting Outlet</h1><p>Software requirements, use cases, problem analysis, object listing, and implementation code.</p><div class="meta"><p><strong>Student:</strong> Opeyemi Raphael-Ogbe</p><p><strong>Matric number:</strong> 220404066</p><p><strong>Project:</strong> Issues reporting for AAUA students and nearby communities</p><p><strong>Version:</strong> 1.0 · 19 October 2026</p></div><p class="small-note">The prototype is local-only. Sample records and the accompanying CSV are fictional and are identified as simulated.</p></section>
"""]

for filename, heading in documents:
    source = (DOCS / filename).read_text(encoding="utf-8")
    parts.append(f'<section class="page-break"><p class="small-note">{escape(heading.upper())}</p>{render_markdown(source)}</section>')
    if filename == "USE-CASES.md":
        parts.append('<section class="diagram-page"><h2>Use-case diagram — reporting and case management</h2><img src="../diagrams/UseCase-Reporting.svg" alt="IRO reporting and case management use-case diagram"></section>')
        parts.append('<section class="diagram-page"><h2>Use-case diagram — administration</h2><img src="../diagrams/UseCase-Administration.svg" alt="IRO administration use-case diagram"></section>')
    if filename == "ISHIKAWA-ANALYSIS.md":
        parts.append('<section class="diagram-page"><h2>Ishikawa fishbone diagram</h2><img src="../diagrams/Ishikawa.svg" alt="IRO Ishikawa fishbone problem analysis"></section>')

listing = (DOCS / "CODE-LISTING.txt").read_text(encoding="utf-8")
parts.append('<section class="page-break"><p class="small-note">CODE LISTING</p><h1>Project source code</h1><pre><code>' + escape(listing) + '</code></pre></section>')
parts.append("</body></html>")
output = DOCS / "SUBMISSION-PACK.html"
output.write_text("\n".join(parts), encoding="utf-8")
print(f"Wrote {output.relative_to(ROOT)}")
