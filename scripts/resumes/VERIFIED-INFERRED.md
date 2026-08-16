# Verified vs Inferred boundary: ATS parse-test harness

This table applies the book's "give to the machine / keep for the human" split to
every value this contribution emits. Each field is labeled by where it comes
from: `record` (from the source Markdown CV), `script-output` (produced by the
harness at run time), `your-input` (a person supplied it), `model-inference`
(a language model guessed it), or `missing` (not available).

The single most important line: this harness makes **no** model inferences. The
`model-inference` column is empty. Every value is either a record from the CV or
a deterministic script output.

| Value the harness emits | Label | Where it comes from |
|---|---|---|
| Field VALUES (name, email, phone, URLs, section titles, entry titles, date ranges, bullet text) | record | parsed from the source Markdown CV |
| PASS / FAIL / WRAP / EMPTY per field | script-output | computed by comparing the CV field against the PDF text layer |
| parse PASS-rate (for example 44/45 = 97.8%) | script-output | count of clean PASS over eligible fields |
| WRAP count and the "split across a line" note | script-output | detected when characters survive but a line break split the token |
| "observed as EXPERIENCE" heading case | script-output | read from the actual PDF text layer |
| extractor disagreements | script-output | comparison of pdfplumber vs pypdf vs pdftotext |
| which extractors ran vs were unavailable | script-output | import / PATH check at run time |
| the source CV path and the PDF path | your-input | passed on the command line (or defaulted) |
| whether a real ATS (Workday, Greenhouse, iCIMS) would parse identically | missing | not verifiable here; see the limitation below |

## The one thing this cannot verify

A PASS means an independent proxy extractor recovered the field from the PDF text
layer. It does **not** mean an employer's real applicant tracking system will
recover it. Real ATS parsers differ from each other and from these extractors, so
the harness reports proxy behavior, never employer behavior. This boundary is the
professional signal: the tool states plainly what it does and does not know.

## Numbers that trace to a record

For the reference run on `resumes/aarav-patel-cv.md`:

- 45 fields were checked. Each field VALUE traces to a line in the source CV.
- 44 returned clean PASS; 1 returned WRAP (`github.com/aaravpatel-example`, split
  across a line break in the PDF). 0 were lost. The 97.8% is the count 44/45,
  not an estimate.
- Every `## ` heading was observed uppercased in the PDF text layer
  (`Experience` rendered and extracted as `EXPERIENCE`), read from the PDF, not
  assumed.
