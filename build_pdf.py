#!/usr/bin/env python3
"""Render resume.md -> resume.pdf using markdown + WeasyPrint."""
import sys
from pathlib import Path
import markdown
from weasyprint import HTML

BASE = Path(__file__).resolve().parent
SRC = BASE / "resume.md"
OUT = BASE / "resume.pdf"

CSS = """
@page {
    size: Letter;
    margin: 0.5in 0.6in 0.5in 0.6in;
}
html { font-size: 10.3pt; }
body {
    font-family: "Helvetica Neue", Arial, "Liberation Sans", sans-serif;
    color: #111;
    line-height: 1.3;
}
h1 {
    font-size: 19pt;
    margin: 0 0 1pt 0;
    border-bottom: 2px solid #111;
    padding-bottom: 2pt;
}
h1 + ul {            /* contact links directly under the name */
    list-style: none;
    margin: 3pt 0 0 0;
    padding: 0;
    font-size: 9pt;
}
h1 + ul li { margin: 0; }
h2 {
    font-size: 12pt;
    margin: 7pt 0 3pt 0;
    padding-bottom: 1.5pt;
    border-bottom: 1px solid #999;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
h3 {
    font-size: 11pt;
    margin: 6pt 0 1pt 0;
}
h4 {
    font-size: 10pt;
    margin: 6pt 0 1pt 0;
    color: #333;
}
p { margin: 3pt 0; }
ul { margin: 1pt 0 2pt 0; padding-left: 15pt; }
li { margin: 0.5pt 0; }
strong { color: #000; }
a { color: #1a4a7a; text-decoration: none; }
/* Keep section headers with their following content */
h2, h3, h4 { page-break-after: avoid; }
"""

def main():
    md_text = SRC.read_text(encoding="utf-8")
    body_html = markdown.markdown(
        md_text,
        extensions=["extra", "sane_lists"],
    )
    html_doc = f"<!DOCTYPE html><html><head><meta charset='utf-8'></head><body>{body_html}</body></html>"
    HTML(string=html_doc, base_url=str(BASE)).write_pdf(str(OUT), stylesheets=[__import__("weasyprint").CSS(string=CSS)])
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")

if __name__ == "__main__":
    sys.exit(main())
