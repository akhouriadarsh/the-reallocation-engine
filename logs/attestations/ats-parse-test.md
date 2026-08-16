## Attestation
- Recipe: ats-parse-test v0.1.1
- By: Adarsh Akhouri · 2026-08-16

> Re-attestation at v0.1.1: v0.1.0 was attested on 2026-08-16. Three tests were then added to close claim-vs-test gaps (entry-heading survival, date-range survival, and extractor disagreement detection). Per SNICKERDOODLE, a script change voids the prior attestation; this re-attests at v0.1.1. Only the test file changed; the harness logic and recipe workflow are unchanged.

### Tested
| Ran | Saw | Expected |
|---|---|---|
| `node scripts/resumes/generate-pdf.mjs resumes/aarav-patel-cv.md` | `-> output/resumes/aarav-patel-cv.pdf (2 pages)` | a PDF is produced from the sample CV |
| `python3 scripts/resumes/ats_parse_test.py resumes/aarav-patel-cv.md` | 44/45 clean PASS, 1 WRAP (github.com/aaravpatel-example split across a line), 0 lost; every `##` heading observed upper-cased in the PDF text layer | most fields survive; any non-survival is reported per field, not hidden |
| `python3 scripts/resumes/ats_parse_test.py --all` (batch over all four repo CVs) | aarav 44/45, maya 46/46, priya 47/47, rohan 53/54; 0 lost anywhere; github URL WRAP in 2 of 4; maya's Skills heading observed lower-cased | a batch, not a single file; findings should generalize or be reported per resume |
| `python3 scripts/resumes/test_ats_parse_test.py` | `17/17 passed` | the offline unit and break tests pass |
| Added test: entry-heading survival via check_text (present and dropped cases) | PASS when present, FAIL when dropped | entry-heading survival is claimed on the card, so it is tested |
| Added test: date-range survival via check_text (present and dropped cases) | PASS when present, FAIL when dropped | date-range survival is claimed on the card, so it is tested |
| Added test: extractor disagreement detection (one parser keeps a URL, one drops it) | the disagreement is reported; agreeing parsers report none | the card claims the tool reports extractor agreement, so it is tested |
| `python3 scripts/resumes/ats_parse_test.py scripts/resumes/fixtures/adversarial-normalization-cv.md --pdf output/resumes/adversarial-normalization-cv.pdf` (deliberate break: em/en dash, curly quotes, ellipsis, zero-width space seeded) | 16/16, all four normalization checks PASS | either the renderer scrubs the seeded characters (PASS) or the harness flags residue (FAIL); it flagged none because the renderer scrubbed them |
| Deliberate break in the test suite: a date written with an en dash in source, a hyphen in the PDF | harness matches correctly (would false-FAIL under a naive exact compare) | the harness must not false-FAIL on renderer normalization drift |
| Deliberate break in the test suite: two bullets merged onto one extracted line | harness reports FAIL via the strict line-start check (a naive substring test would false-PASS) | a merged bullet must be caught, not counted as survived |
| `npm run verify` | `all conform`; `manifest check passed (4 warnings)` | conformance passes; the 4 warnings are pre-existing repo warnings |
| `npm run doctor` | recipes 44/44 carry lifecycle frontmatter; the only privacy flag is the pre-existing `search/resume.json` | doctor clean for this contribution |

### Did not test
- Any real applicant tracking system (Workday, Greenhouse, iCIMS). The harness uses proxy extractors (pdfplumber, pypdf) only, so a PASS means a standard extractor recovered the field, not that an employer's ATS will.
- The soft hyphen (U+00AD) and other invisible characters outside the checked set. The normalization checks cover the zero-width family, curly quotes, en and em dashes, and the ellipsis character only. A résumé poisoned with a soft hyphen could pass both the renderer and this checker. Named blind spot, not solved.
- pdftotext as a third extractor was not installed on this machine, so the multi-parser comparison ran with two extractors, not three (reported honestly as SKIP).
- Whether the line-wrap that produced the WRAP result reproduces on a different machine; Playwright/Chromium version and font substitution can change where a line breaks.

### Broke during testing, fixed
- A Markdown bold marker (`**Languages:**`) caused a false FAIL because the renderer strips `**` when it converts to `<strong>`. Fixed by stripping Markdown inline syntax on both sides before matching (`strip_md_inline` in `scripts/resumes/ats_parse_test.py`). Caught by `test_clean_extraction_all_pass` during the build.
- An email domain (`example.com`) leaked into the extracted URL list because the email's domain matched the URL pattern. Fixed by blanking emails before scanning for URLs. Caught while validating ground truth on the real CV.
