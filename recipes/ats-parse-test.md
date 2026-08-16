---
# NOTE: reconcile these frontmatter keys against an existing recipes/*.md before
# committing — doctor.mjs checks that every recipe carries lifecycle frontmatter,
# and the exact key names must match the repo's schema.
title: ATS Parse-Test Harness
status: RUNNABLE-SAMPLE
attestation: null
chapters: [13, 16]
---

# Recipe: ATS Parse-Test Harness

## 1. Executive summary
Re-parse a résumé PDF that `scripts/resumes/generate-pdf.mjs` produced, and
report — per field — whether the content in the source Markdown CV actually
survives into the PDF's text layer. The engine ships a résumé renderer but never
verifies its "ATS-friendly" claim; this recipe closes that gap with a real,
deterministic PASS/FAIL check. It verifies against proxy extractors, not a real
ATS, and says so.

## 2. Required reads (read before you run)
- `scripts/resumes/ats_parse_test.py` — the harness (docstring states scope + exit codes).
- `scripts/resumes/generate-pdf.mjs` — the renderer under test (its
  `normalizeTextForATS()` defines the promises this harness checks).
- `scripts/resumes/VERIFIED-INFERRED.md` — the verified-vs-inferred boundary.
- `recipes/ats-parse-test.card.md` — the human card and its failure modes.

## 3. Phase gates (each with a failure path)
- **G1 — source exists.** The `.md` CV must exist. Missing → exit 2, do not score.
- **G2 — PDF exists.** The generated PDF must exist. Missing → exit 2 with a
  "generate it first" message; do not fabricate a result.
- **G3 — an extractor is available.** At least one of pdfplumber / pypdf /
  pdftotext must import or be on PATH. None → exit 2; the run did not happen.
- **G4 — field survival.** Any field present in the source but lost in the PDF
  (ERROR) → exit 1. EMPTY (absent from source) and SKIP (extractor missing)
  never fail the run.

If a gate has no failure path it is decoration; each gate above names its own.

## 4. Primary stored tools
- `python3 scripts/resumes/ats_parse_test.py <cv.md> [--pdf <pdf>] [--all] [--json]`
- `python3 scripts/resumes/test_ats_parse_test.py` (offline unit + break tests)

## 5. Workflow (imperative, verbatim)
```
# one-time: install extractors into the repo venv
pip install pdfplumber pypdf

# 1. render the PDF under test
node scripts/resumes/generate-pdf.mjs resumes/aarav-patel-cv.md

# 2. run the harness (writes an audit under reports/generated/)
python3 scripts/resumes/ats_parse_test.py resumes/aarav-patel-cv.md

# 3. run the offline test suite (must print N/N passed, exit 0)
python3 scripts/resumes/test_ats_parse_test.py

# 4. break attempt — render the adversarial fixture, then re-parse it
node scripts/resumes/generate-pdf.mjs scripts/resumes/fixtures/adversarial-normalization-cv.md
python3 scripts/resumes/ats_parse_test.py scripts/resumes/fixtures/adversarial-normalization-cv.md \
  --pdf output/resumes/adversarial-normalization-cv.pdf
```

## 6. Output contract
- A per-field table: `status(PASS|FAIL|EMPTY|SKIP) · category · field · note`.
- A parse PASS-rate, explicitly labeled **script-output** (never a record).
- Extractor disagreements listed as findings.
- A Markdown audit at `reports/generated/ats-parse-test-<name>-<date>.md`.
- Field VALUES trace to the source CV (record); statuses and the rate are
  script-output; real-ATS behavior is NOT emitted (unverifiable here).

## 7. Verification checks
- `test_ats_parse_test.py` prints `N/N passed` and exits 0.
- The two break tests (dash-drift false-FAIL; merged-bullet false-PASS) pass.
- On a normal CV, exit code is 0 and no field is FAIL.
- On the adversarial fixture, the normalization checks report on smart
  punctuation / zero-width residue in the actual PDF text layer.

## 8. Logging rules
- Append one entry per run to `logs/RUN_LOG.md`: date, CV, primary extractor,
  PASS-rate, any FAIL fields, any extractor disagreements, and anything the
  run could not verify.
- Record break attempts and their outcomes, including bugs found in the harness
  itself.

## 9. Stop conditions
- Stop and exit 2 if the PDF or all extractors are missing — never emit a
  PASS-rate without a real extraction behind it.
- Stop and mark ERROR (not EMPTY) when a source field is lost in the PDF.
- Prefer "not verifiable against a real ATS" over implying the check proves
  employer-side parsing.
