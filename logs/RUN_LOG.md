# RUN_LOG for the ATS parse-test harness

This file records runs for the ats-parse-test contribution. Format per
SNICKERDOODLE logging: date, recipe, inputs, outputs, result, open issues.
No secrets, no personal contact details, no private application notes.

## 2026-08-16 : ats-parse-test v0.1.0 : sample run and break attempt

- Recipe: ats-parse-test v0.1.0
- Inputs: resumes/aarav-patel-cv.md (repo sample CV), and the break fixture
  scripts/resumes/fixtures/adversarial-normalization-cv.md
- Environment: macOS (Apple silicon), Python 3.13.0, Node v23.1.0,
  pdfplumber 0.11.10, pypdf 6.16.1, Playwright Chromium installed. pdftotext
  not installed (reported as SKIP).

### What was run
- `node scripts/resumes/generate-pdf.mjs resumes/aarav-patel-cv.md`
- `python3 scripts/resumes/ats_parse_test.py resumes/aarav-patel-cv.md`
- `python3 scripts/resumes/test_ats_parse_test.py`
- `node scripts/resumes/generate-pdf.mjs scripts/resumes/fixtures/adversarial-normalization-cv.md`
- `python3 scripts/resumes/ats_parse_test.py scripts/resumes/fixtures/adversarial-normalization-cv.md --pdf output/resumes/adversarial-normalization-cv.pdf`
- `npm run verify`
- `npm run doctor`

### Results
- Sample CV: parse PASS-rate 44/45 = 97.8%. WRAP 1, lost 0, EMPTY 0. The WRAP was
  github.com/aaravpatel-example, split across a line break in the PDF text layer.
  All four section headings observed upper-cased (Experience -> EXPERIENCE, etc.).
- Adversarial CV: 16/16, all four normalization checks PASS (the renderer scrubbed
  the seeded em/en dash, curly quotes, ellipsis, and zero-width space).
- Tests: 14/14 passed.
- verify: all conform; manifest check passed (4 pre-existing warnings).
- doctor: recipes 44/44 carry lifecycle frontmatter. Only privacy flag is the
  pre-existing search/resume.json (not introduced by this contribution).

### What failed and was fixed
- Markdown bold marker (**Languages:**) caused a false FAIL; fixed by stripping
  inline Markdown before matching. Caught by test_clean_extraction_all_pass.
- An email domain leaked into the URL list; fixed by blanking emails before URL
  extraction. Caught while validating ground truth on the real CV.
- The github URL was first reported as a bare FAIL; added a distinct WRAP status
  so a field whose characters survive but split across a line break is reported
  honestly rather than as a flat FAIL or a false PASS.

### Open issues / what should be tested next
- No validation against a real ATS (Workday, Greenhouse, iCIMS). Proxy extractors
  only.
- Normalization checks do not cover the U+00AD soft hyphen or every invisible
  character; a future check could add it.
- pdftotext (third extractor) was not installed, so the multi-parser comparison
  ran with two extractors. Install poppler to exercise the third.
- Small sample (a handful of repo CVs); the PASS-rate is a spot check, not a
  population estimate.

## 2026-08-16 : ats-parse-test v0.1.1 : re-attestation after adding tests

- Recipe: ats-parse-test v0.1.1 (bumped from v0.1.0)
- Change: added three tests to test_ats_parse_test.py to close claim-vs-test gaps
  the card advertised but the suite did not cover:
  entry-heading survival, date-range survival, and extractor disagreement detection.
- Ran: python3 scripts/resumes/test_ats_parse_test.py
- Result: 17/17 passed (was 14/14).
- Per SNICKERDOODLE, the script change voided the v0.1.0 attestation; re-attested at
  v0.1.1. Only the test file changed; harness logic and recipe workflow unchanged.
- Open issues: unchanged from the v0.1.0 entry (no real-ATS validation; soft hyphen
  not checked; pdftotext not installed; small sample).
