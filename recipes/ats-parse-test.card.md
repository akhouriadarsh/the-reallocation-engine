---
status: RUNNABLE-SAMPLE
todos_open: 0
last_gate: null
attestation: null
recipe_version: 0.1.0
---

# Card: ATS Parse-Test Harness (human)

## Purpose
Give the résumé renderer a test it never had: prove that the fields in a source
Markdown CV actually survive into the generated PDF's text layer, the way an ATS
would read it. Turns the renderer's unverified "ATS-friendly" claim into a
per-field PASS/FAIL with a real number.

## What it CAN verify
- The name, contact tokens, section headings, entry headings, date ranges, and
  bullets from the source CV are recoverable from the PDF text layer.
- Bullets stay separate (a merged bullet is caught, not counted as survived).
- The renderer's own normalization promises hold in the PDF (no smart dashes,
  curly quotes, ellipsis char, or U+200B-family zero-width chars).
- Whether independent extractors (pdfplumber / pypdf / pdftotext) agree.

## What it CANNOT verify
- **Whether a real ATS (Workday, Greenhouse, iCIMS) parses the same way.** This
  is the load-bearing limitation. A PASS means "our proxy extractor recovered
  the field," not "an employer's ATS will." Different ATS parsers differ.
- Whether the résumé's *content* is true, or good — only whether it survived.
- Invisible characters outside the checked set (e.g. U+00AD soft hyphen) — see
  failure mode 4.

## Dependencies
- `pdfplumber` and `pypdf` (`pip install pdfplumber pypdf`); optional
  `pdftotext` from poppler if on PATH.
- A PDF produced by `scripts/resumes/generate-pdf.mjs` (needs Node + Playwright
  Chromium).

## Annotated commands
- `python3 scripts/resumes/ats_parse_test.py resumes/aarav-patel-cv.md`
  → parse-test one CV against its default PDF (`output/resumes/<name>.pdf`).
- `... --all` → every `resumes/*-cv.md`.
- `... --json` → machine-readable output for CI.
- `python3 scripts/resumes/test_ats_parse_test.py` → offline unit + break tests.

## What it produces
- Console per-field table + a PASS-rate labeled *script-output*.
- A Markdown audit at `reports/generated/ats-parse-test-<name>-<date>.md`.
- Exit 0 (all survived) / 1 (a field lost) / 2 (precondition failed).

## Failure modes (named)
1. **Drift (match policy vs renderer).** The harness normalizes both sides
   (dashes, curly quotes, Markdown `**bold**`/`` `code` ``) to avoid false
   FAILs. If the renderer changes its normalization, or a CV uses inline syntax
   the harness doesn't strip, a field that survived will false-FAIL. *Two real
   instances were found and fixed during the build (Markdown-bold markers; an
   email domain leaking as a URL) — logged in RUN_LOG.*
2. **Contract-violation.** The harness must never print a PASS-rate that isn't
   backed by a real extraction. If an extractor returned no text but the code
   proceeded, the rate would misrepresent status. Guarded by the SKIP path and
   exit 2 — but this is the mode to watch, and any change here must preserve it.
3. **False PASS via substring.** Headings and dates use substring presence, so a
   reordered or merged field can still contain the substring and wrongly PASS.
   Mitigated for bullets by a strict line-start check; NOT fully mitigated for
   headings/dates. A section that moved to the wrong place can still PASS.
4. **Invisible-character blind spot.** The normalization checks cover the
   U+200B family, curly quotes, en/em dashes, and the ellipsis char. They do
   NOT cover U+00AD soft hyphen or other invisibles, which pass through both the
   renderer and this checker undetected.
5. **Small-n.** The repo ships only a handful of CVs. A PASS-rate over ~4-5
   résumés is a spot check, not a population estimate; do not report it as one.
6. **Environment drift.** Playwright/Chromium version and font substitution can
   change the extracted text, so results may not reproduce byte-for-byte on a
   different machine.
