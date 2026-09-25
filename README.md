resume
======

Adam Harder's online resume

## Build the PDF

There are two source-of-truth documents; both produce `resume.pdf`. Use one or
the other (not both) -- they will overwrite the same output file.

### LaTeX -> `resume.pdf` (pdflatex)
Requires a TeX distribution (TeX Live, MacTeX) or Overleaf.

```bash
./build_latex.sh
# or, manually:
# pdflatex -jobname=resume resume.tex && pdflatex -jobname=resume resume.tex
```

### Markdown -> `resume.pdf` (WeasyPrint)
Requires Python with `weasyprint` and `markdown` installed.

```bash
python3 build_pdf.py
```

