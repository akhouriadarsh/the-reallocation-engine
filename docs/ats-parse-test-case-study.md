# Does an "ATS friendly" resume actually survive parsing? A verifier that checks.

Adarsh Akhouri · [PR #48 on the-reallocation-engine](https://github.com/nikbearbrown/the-reallocation-engine/pull/48)

## The problem

Job seekers are told to use an "ATS friendly" resume, and tools happily generate
one. The catch: almost nobody checks whether the generated PDF is actually
readable by the software that parses it. The claim "ATS friendly" is made at the
moment the file is written and never tested against reality. For an international
candidate whose entire pipeline runs through applicant tracking systems, a link
or a section title that silently fails to parse is a real cost, and an invisible
one.

The Reallocation Engine, an evidence first job search system, had exactly this
gap. Its resume generator (`scripts/resumes/generate-pdf.mjs`) renders a Markdown
CV into a PDF it describes as ATS friendly, but no test in the repository ever
confirmed that the fields survive extraction. The renderer graded its own homework.

## What I built

A parse test harness (`scripts/resumes/ats_parse_test.py`) that closes the loop.
It takes the source Markdown CV and the generated PDF, re-reads the PDF with
independent text extractors (pdfplumber and pypdf, with pdftotext as an optional
third), and reports, field by field, whether the content survived.

Architecture in three moves:

1. Parse the source CV into ground truth: name, contact tokens, section headings,
   entry headings, date ranges, and bullets. Ground truth comes from the CV
   itself, so the tool cannot check for a field the resume does not have.
2. Extract the PDF text with two or three independent parsers. Disagreement
   between parsers is surfaced as a finding rather than hidden.
3. Classify each field: PASS (recovered cleanly), WRAP (all characters present
   but split across a line break, a real line wrap risk), FAIL (present in the
   source, lost in the PDF), or EMPTY (not in the source, nothing to check).
   EMPTY and FAIL are never conflated.

## The measurable improvement

Run across the four resumes the repository ships, the harness returns concrete
numbers per resume: 44 of 45 (97.8 percent), 46 of 46, 47 of 47, and 53 of 54.
No field was lost in any resume. The one held-out class is WRAP, a field whose
characters all survived but were split across a line break.

More useful than the headline number are the two specific defects it surfaced,
each of which was invisible before:

- The GitHub link wrapped across a line break in the PDF
  (`github.com/aaravpatel-` on one line, `example` on the next), so a line by line
  ATS could capture a broken link. The batch showed this is a pattern, not a fluke:
  the link split in two of the four resumes and survived whole in the other two, so
  whether it survives is a layout accident.
- Section headings are stored upper cased in the PDF text layer (`Experience`
  becomes `EXPERIENCE`) because the renderer's CSS uppercases them, which matters
  for case sensitive ATS matching. The batch also caught that this is not even
  consistent: one resume's `Skills` heading came out lower cased while every other
  heading was upper, so the renderer's heading case cannot be relied on either way.

## Verified versus inferred

The professional signal here is knowing exactly what the tool does and does not
prove. Field values are records from the CV. PASS, WRAP, FAIL, and the rate are
script outputs. The tool makes no model inferences. And the one thing it cannot
verify is stated plainly: it checks against proxy extractors, not against a real
applicant tracking system, so a PASS means a standard text extractor recovered
the field, not that Workday or Greenhouse will. Naming that boundary is the point,
not a footnote.

## Failure modes I went looking for

I treated my own tool as guilty until proven innocent. Two bugs surfaced while
testing it and were fixed:

- Markdown bold markers in a bullet (`**Languages:**`) caused a false FAIL,
  because the renderer strips those markers on the way to the PDF. Fixed by
  stripping inline Markdown from both sides before comparing.
- An email domain leaked into the list of portfolio URLs. Fixed by removing
  emails before scanning for URLs.

Two more breaks are locked as tests: a date written with an en dash in the source
but a hyphen in the PDF must not false FAIL, and two bullets merged onto one line
must be caught rather than counted as survived. I later added tests for entry
heading survival, date range survival, and extractor disagreement, so every
capability the tool advertises has a test behind it. Full suite: 17 of 17 passing.

Known blind spot, disclosed rather than hidden: the checks cover the zero width
character family, curly quotes, en and em dashes, and the ellipsis character, but
not the soft hyphen (U+00AD) or every other invisible character. A resume poisoned
with one of those could pass both the renderer and this checker.

## A demo you can open

The pull request is [#48](https://github.com/nikbearbrown/the-reallocation-engine/pull/48).
It is a single commit, eight files, cherry picked onto the upstream main so the
diff shows only this contribution. The harness runs in three commands:

```
node scripts/resumes/generate-pdf.mjs resumes/aarav-patel-cv.md
python3 scripts/resumes/ats_parse_test.py resumes/aarav-patel-cv.md
python3 scripts/resumes/test_ats_parse_test.py
```

## Why it matters

The most valuable thing a verification tool can say is not "everything is fine."
It is "here is the one place it is not, and here is what I cannot know." This
harness turns an unchecked marketing claim into a per field result with an honest
boundary, and on its first real run it found a broken link that no one had seen.
