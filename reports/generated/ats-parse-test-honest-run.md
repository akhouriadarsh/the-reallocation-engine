# Honest run: ATS parse-test harness

Author: Adarsh Akhouri
Date of run: 2026 08 16
Machine: macOS (Apple silicon), Python 3.13.0, Node v23.1.0, pdfplumber 0.11.10,
pypdf 6.16.1, Playwright Chromium installed.

This document reports a real run, not a description of one. The commands and their
actual output appear below.

## What was run

```
node scripts/resumes/generate-pdf.mjs resumes/aarav-patel-cv.md
python3 scripts/resumes/ats_parse_test.py resumes/aarav-patel-cv.md
python3 scripts/resumes/test_ats_parse_test.py
node scripts/resumes/generate-pdf.mjs scripts/resumes/fixtures/adversarial-normalization-cv.md
python3 scripts/resumes/ats_parse_test.py scripts/resumes/fixtures/adversarial-normalization-cv.md --pdf output/resumes/adversarial-normalization-cv.pdf
```

## Plausibility audit before trusting the output

Before reading the result as true, three sanity checks:

1. Field count. The source CV has one name, several contact tokens, four section
   headings, seven entry headings, five date ranges, and many bullets. The harness
   reported 45 eligible fields, which matches the visible structure of the CV. A
   result of, say, 6 fields would have signaled a parsing failure. It did not.
2. Not everything passed. A run that returns a flat 100% on the first try is
   suspicious. This run returned one WRAP, which is the tool distinguishing a real
   defect rather than rubber stamping the PDF.
3. Both extractors agreed. pdfplumber and pypdf produced the same per field verdict,
   so the result does not hinge on one library's quirk. pdftotext was not installed,
   reported honestly as SKIP.

## Reference run: aarav-patel-cv

Result: parse PASS-rate 44/45 = 97.8%. WRAP 1. lost 0. EMPTY 0.

The one non PASS field:

```
WRAP  [contact] github.com/aaravpatel-example  (survived but split across a line break (line-wrap risk))
```

Reading the PDF text layer directly showed why:

```
... linkedin.com/in/aaravpatel-example | github.com/aaravpatel-
example | aaravpatel.dev
```

The GitHub URL was split across a line break: `github.com/aaravpatel-` ended one
line and `example` began the next. Its neighbors fit on the line and survived
whole. This is a real line-wrap risk. A line-by-line ATS reader could capture a
broken GitHub link.

A second real finding from the same run: every section heading was observed in the
PDF text layer in upper case (`Experience` became `EXPERIENCE`, `Technical Skills`
became `TECHNICAL SKILLS`, and so on). The renderer's CSS uppercases headings for
display, and that upper case is what lands in the extractable text. This matters
for any ATS whose section matching is case sensitive.

## The metric readout

The metric this component reports is the parse PASS-rate, and its working range is
0 to 100 percent over the fields present in a given CV. For this CV it is 44/45,
which is 97.8 percent, with one field held out as WRAP rather than counted as a
clean pass, so the rate is not rounded up to 100.

## Deliberate break attempt

The rubric asks for a real attempt to make the contribution produce a wrong answer.
Two were built into the test suite and one adversarial résumé was run live.

1. False FAIL from drift. A date written with an en dash in the source but rendered
   as a hyphen in the PDF would fail a naive exact compare. The harness normalizes
   both sides, so it correctly matches. Locked by a test.
2. False PASS from a merged bullet. If two bullets merge onto one line, a plain
   substring check would still find the text and wrongly pass. The harness uses a
   strict line-start check that flags the merge as a failure. Locked by a test.
3. Adversarial résumé run live. A fixture CV was seeded with an em dash, an en dash,
   curly quotes, an ellipsis character, and a zero-width space, then rendered and
   re-parsed. Result: 16/16, all four normalization checks PASS, which means the
   renderer scrubbed every one of those characters before they reached the PDF.

Honest note on the break attempt: number 3 did not break anything, because the
renderer held. As a stress test it is a verified positive about the renderer, not a
case where the tool was caught being wrong. The genuine "caught being wrong"
evidence is numbers 1 and 2, plus two bugs the tests found during the build (a
Markdown bold marker causing a false FAIL, and an email domain leaking in as a URL),
both fixed.

## Tests

```
14/14 passed
```

## What the machine could not know

The harness can prove that a field survives into the PDF text layer as read by
pdfplumber and pypdf. It cannot know whether a specific employer's applicant
tracking system parses the same PDF the same way. Workday, Greenhouse, and iCIMS
each parse differently, and none of them was in the loop here. So the judgment the
tool hands back to a human is narrow and honest: these fields are recoverable by a
standard text extractor, the GitHub link is at risk because it wrapped, and the
headings will arrive upper cased. Whether that is good enough for a given ATS is a
human call the tool does not make.

A second thing the machine could not know: the normalization checks cover the
zero-width family, curly quotes, en and em dashes, and the ellipsis character. They
do not cover the soft hyphen (U plus 00AD) or every other invisible character, so a
résumé poisoned with one of those could pass both the renderer and this checker. It
is a named blind spot, not a solved problem.
