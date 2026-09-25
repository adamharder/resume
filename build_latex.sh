#!/usr/bin/env bash
# Build the LaTeX resume into resume.pdf.
# Requires a TeX distribution with pdflatex (e.g. TeX Live, MacTeX, or Overleaf).
# Run twice so cross-references and layout settle.
set -euo pipefail

cd "$(dirname "$0")"

JOBNAME=resume

# -interaction=nonstopmode keeps the build going past minor errors;
# -halt-on-error stops hard on real failures.
pdflatex -jobname="$JOBNAME" -interaction=nonstopmode -halt-on-error resume.tex >/dev/null
pdflatex -jobname="$JOBNAME" -interaction=nonstopmode -halt-on-error resume.tex >/dev/null

# Clean up auxiliary build artifacts (keep the .pdf).
rm -f "${JOBNAME}.aux" "${JOBNAME}.log" "${JOBNAME}.out"

echo "Wrote $(pwd)/${JOBNAME}.pdf ($(stat -c%s "${JOBNAME}.pdf" 2>/dev/null || stat -f%z "${JOBNAME}.pdf") bytes)"
