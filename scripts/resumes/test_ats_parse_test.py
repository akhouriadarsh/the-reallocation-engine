#!/usr/bin/env python3
"""
Offline test suite for ats_parse_test.py — no PDF, no network required.

Run:
  python3 scripts/resumes/test_ats_parse_test.py
Prints "N/N passed" and exits 0 on success, 1 on any failure.

Includes the two DELIBERATE BREAK ATTEMPTS the capstone asks for — cases
engineered to make the harness produce a WRONG answer, and the checks that
catch each:
  BREAK 1 (false FAIL / drift): source uses an en-dash, the PDF a hyphen.
          A naive raw compare FAILs a field that actually survived.
          canon() normalizes both sides -> correct PASS.
  BREAK 2 (false PASS / merged bullet): a substring test says a bullet
          survived when it actually merged into the previous line.
          The strict line-start check catches the merge -> correct FAIL.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ats_parse_test as H  # noqa: E402

SAMPLE_CV = """# Aarav Patel
Boston, MA | (617) 555-0148 | aarav.patel@example.com | linkedin.com/in/aaravpatel-example | github.com/aaravpatel-example | aaravpatel.dev
## Experience
### Dassault Systemes | Software Engineer
Waltham, MA | Jan 2026 - May 2026
- Engineered a feature flag platform in TypeScript with MSSQL and Redis.
- Designed a multi-agent AI workflow over Elasticsearch crash logs.
## Technical Skills
- **Languages:** Go, JavaScript, TypeScript, Java, Python, SQL
## Projects
### CVE-GPT
- Engineered an event-driven CVE ingestion pipeline on Kubernetes.
## Education
### Northeastern University
Boston, MA | M.S. in Software Engineering Systems | Sep 2023 - Dec 2025 | GPA: 3.83/4.0
"""

_failures: list[str] = []


def check(cond: bool, msg: str) -> None:
    if not cond:
        _failures.append(msg)


# --- normalization ---------------------------------------------------------- #
def test_normalize_strips_zero_width():
    dirty = "Soft\u200bware\ufeff Engineer"
    check(H.normalize_ats(dirty) == "Software Engineer", "zero-width not stripped")


def test_normalize_converts_smart_punctuation():
    check(H.normalize_ats("2020\u20132021") == "2020-2021", "en-dash not normalized")
    check(H.normalize_ats("\u201chi\u201d") == '"hi"', "curly double-quotes not normalized")
    check(H.normalize_ats("O\u2019Brien") == "O'Brien", "curly apostrophe not normalized")
    check(H.normalize_ats("a\u2026b") == "a...b", "ellipsis char not normalized")
    check(H.normalize_ats("a\u00a0b") == "a b", "nbsp not normalized")


def test_canon_collapses_and_normalizes():
    check(H.canon("Jan 2020  \u2013 May 2021") == H.canon("Jan 2020 - May 2021"),
          "canon should equate en-dash and hyphen after whitespace collapse")


# --- ground truth ----------------------------------------------------------- #
def test_ground_truth_parses_real_cv():
    gt = H.parse_ground_truth(SAMPLE_CV)
    check(gt.name == "Aarav Patel", f"name wrong: {gt.name!r}")
    check(gt.sections == ["Experience", "Technical Skills", "Projects", "Education"],
          f"sections wrong: {gt.sections}")
    check("Dassault Systemes | Software Engineer" in gt.entries, "missing experience entry")
    check("CVE-GPT" in gt.entries, "missing project entry")
    check("Northeastern University" in gt.entries, "missing education entry")
    check(any("Jan 2026" in d for d in gt.date_ranges), f"date ranges missing: {gt.date_ranges}")
    check(any("Sep 2023" in d for d in gt.date_ranges), "education date range missing")
    check("aarav.patel@example.com" in gt.emails, f"email missing: {gt.emails}")
    check(any("617" in p for p in gt.phones), f"phone missing: {gt.phones}")
    check(any("github.com" in u for u in gt.urls), f"urls missing: {gt.urls}")
    check(not any("@" in u for u in gt.urls), "email leaked into urls")
    check("example.com" not in gt.urls, "email domain leaked into urls")


# --- happy path: clean extraction passes ------------------------------------ #
def test_clean_extraction_all_pass():
    gt = H.parse_ground_truth(SAMPLE_CV)
    # simulate a faithful extractor: the source text, sections upper-cased (CSS),
    # with every line preserved as its own line.
    extracted = SAMPLE_CV.replace("## ", "## ").upper()  # aggressive: everything upper
    # rebuild a realistic extraction: keep case for body, upper only headings
    lines = []
    for ln in SAMPLE_CV.split("\n"):
        s = ln.strip()
        if s.startswith("## "):
            lines.append(s[3:].upper())
        elif s.startswith("### "):
            lines.append(s[4:])
        elif s.startswith("# "):
            lines.append(s[2:])
        elif s.startswith("- "):
            lines.append(s[2:].replace("**", ""))
        else:
            lines.append(s)
    extracted = "\n".join(lines)
    results = H.check_text(gt, extracted)
    fails = [r for r in results if r.status == H.STATUS_FAIL]
    check(not fails, f"clean extraction should pass; failed: {[(r.category, r.label) for r in fails]}")


def test_observed_heading_case_reported():
    gt = H.parse_ground_truth("# X\ncontact\n## Experience\n- a\n")
    results = H.check_text(gt, "X\ncontact\nEXPERIENCE\na")
    sec = [r for r in results if r.category == "section" and r.label == "Experience"][0]
    check(sec.status == H.STATUS_PASS, "uppercased heading should still PASS")
    check("EXPERIENCE" in sec.detail, f"observed case not reported: {sec.detail!r}")


# --- EMPTY vs ERROR --------------------------------------------------------- #
def test_empty_is_not_failure():
    gt = H.parse_ground_truth("# X\ncontact\n## Experience\n")  # no bullets, no projects
    results = H.check_text(gt, "X\ncontact\nEXPERIENCE")
    bullet = [r for r in results if r.category == "bullet"][0]
    check(bullet.status == H.STATUS_EMPTY, "no bullets in source should be EMPTY, not FAIL")


def test_lost_field_is_error():
    gt = H.parse_ground_truth("# X\ncontact\n## Experience\n- did this thing\n")
    results = H.check_text(gt, "X\ncontact\nEXPERIENCE")  # bullet dropped
    bullet = [r for r in results if r.category == "bullet"][0]
    check(bullet.status == H.STATUS_FAIL, "bullet present in source but lost should be FAIL")


# --- BREAK 1: false FAIL from dash drift ------------------------------------ #
def test_break_dash_drift_false_fail_is_fixed():
    # source has en-dash; PDF (post-normalization) has hyphen
    source_date = "Jan 2020 \u2013 May 2021"
    pdf_text = "Jan 2020 - May 2021"
    # naive raw compare (the bug): would be False
    naive = source_date in pdf_text
    check(naive is False, "raw compare should mismatch (this is the bug we fix)")
    # the harness uses canon on both sides (the fix): matches
    hay = H.canon(pdf_text, casefold=True)
    check(H._present(source_date, hay), "canon both sides should MATCH across dash drift")


# --- BREAK 2: false PASS from a merged bullet ------------------------------- #
def test_break_merged_bullet_false_pass_is_caught():
    gt = H.parse_ground_truth(
        "# X\ncontact\n## Experience\n- Led the migration effort\n- Cut costs sharply\n"
    )
    # extractor merged bullet 2 onto bullet 1's line (a real ATS failure)
    merged = "X\ncontact\nEXPERIENCE\nLed the migration effort Cut costs sharply"
    results = H.check_text(gt, merged)
    b2 = [r for r in results if r.category == "bullet" and r.label.startswith("Cut costs")][0]
    # naive substring WOULD say present; strict boundary marks it FAIL
    hay = H.canon(merged, casefold=True)
    check(H.canon("Cut costs sharply", casefold=True) in hay, "substring is present (naive would PASS)")
    check(b2.status == H.STATUS_FAIL, "merged bullet must be caught as FAIL by strict check")
    check("merged" in b2.detail, f"merge should be labeled: {b2.detail!r}")


# --- normalization promises verified on extracted text ---------------------- #
def test_normalization_checks_flag_residue():
    good = H.check_normalization("clean hyphen - straight 'quotes' done.")
    check(all(r.status == H.STATUS_PASS for r in good), "clean text should pass normalization checks")
    bad = H.check_normalization("bad \u2014 dash and \u201ccurly\u201d and zero\u200bwidth")
    labels_failed = {r.label for r in bad if r.status == H.STATUS_FAIL}
    check("no-fancy-dashes" in labels_failed, "should flag em-dash")
    check("no-curly-quotes" in labels_failed, "should flag curly quotes")
    check("no-zero-width" in labels_failed, "should flag zero-width")


# --- WRAP: a URL split across a line break ---------------------------------- #
def test_wrap_split_url_is_wrap_not_fail():
    gt = H.parse_ground_truth(
        "# X\ncontact | github.com/aaravpatel-example\n## Experience\n- a\n"
    )
    # extractor wrapped the URL mid-token across two lines (the real Aarav finding)
    extracted = "X\ncontact | github.com/aaravpatel-\nexample\nEXPERIENCE\na"
    results = H.check_text(gt, extracted)
    url = [r for r in results if r.category == "contact"
           and "github.com" in r.label][0]
    check(url.status == H.STATUS_WRAP, f"split URL should be WRAP, got {url.status}")
    check("line" in url.detail, f"WRAP should mention the line break: {url.detail!r}")


def test_wrap_intact_url_is_pass():
    gt = H.parse_ground_truth("# X\ncontact | github.com/aaravpatel-example\n## E\n- a\n")
    extracted = "X\ncontact | github.com/aaravpatel-example\nE\na"
    results = H.check_text(gt, extracted)
    url = [r for r in results if r.category == "contact" and "github.com" in r.label][0]
    check(url.status == H.STATUS_PASS, f"intact URL should PASS, got {url.status}")


def test_wrap_missing_url_is_fail():
    gt = H.parse_ground_truth("# X\ncontact | github.com/aaravpatel-example\n## E\n- a\n")
    extracted = "X\ncontact\nE\na"  # URL entirely gone
    results = H.check_text(gt, extracted)
    url = [r for r in results if r.category == "contact" and "github.com" in r.label][0]
    check(url.status == H.STATUS_FAIL, f"missing URL should FAIL, got {url.status}")


# --- entry heading survival (claimed on the card, now tested) ---------------- #
def test_entry_heading_survival_pass_and_fail():
    gt = H.parse_ground_truth(
        "# X\ncontact\n## Experience\n### Acme Corp | Engineer\n- did a thing\n"
    )
    kept = H.check_text(gt, "X\ncontact\nEXPERIENCE\nAcme Corp | Engineer\ndid a thing")
    ent = [r for r in kept if r.category == "entry"][0]
    check(ent.status == H.STATUS_PASS, f"present entry heading should PASS, got {ent.status}")
    lost = H.check_text(gt, "X\ncontact\nEXPERIENCE\ndid a thing")  # entry line dropped
    ent2 = [r for r in lost if r.category == "entry"][0]
    check(ent2.status == H.STATUS_FAIL, f"lost entry heading should FAIL, got {ent2.status}")


# --- date range survival (claimed on the card, now tested) ------------------- #
def test_date_range_survival_pass_and_fail():
    gt = H.parse_ground_truth(
        "# X\ncontact\n## Experience\n### Acme | Eng\nBoston | Jan 2020 - May 2021\n- x\n"
    )
    kept = H.check_text(gt, "X\ncontact\nEXPERIENCE\nAcme | Eng\nBoston | Jan 2020 - May 2021\nx")
    d = [r for r in kept if r.category == "date"][0]
    check(d.status == H.STATUS_PASS, f"present date range should PASS, got {d.status}")
    lost = H.check_text(gt, "X\ncontact\nEXPERIENCE\nAcme | Eng\nBoston\nx")  # date dropped
    d2 = [r for r in lost if r.category == "date"][0]
    check(d2.status == H.STATUS_FAIL, f"lost date range should FAIL, got {d2.status}")


# --- extractor disagreement detection (claimed on the card, now tested) ------ #
def test_extractor_disagreement_is_reported():
    gt = H.parse_ground_truth("# X\ncontact | github.com/x-example\n## E\n- a\n")
    # extractor A keeps the URL intact; extractor B drops it -> they disagree
    run_a = H.ExtractorRun("pdfplumber",
                           H.check_text(gt, "X\ncontact | github.com/x-example\nE\na"))
    run_b = H.ExtractorRun("pypdf",
                           H.check_text(gt, "X\ncontact\nE\na"))
    dis = H.disagreements([run_a, run_b])
    check(any("github.com" in d for d in dis),
          f"disagreement on the URL should be reported, got {dis}")
    # and when both agree, no disagreement is reported for that field
    run_c = H.ExtractorRun("pypdf",
                           H.check_text(gt, "X\ncontact | github.com/x-example\nE\na"))
    dis2 = H.disagreements([run_a, run_c])
    check(not any("github.com" in d for d in dis2),
          f"agreeing extractors should report no URL disagreement, got {dis2}")


def main() -> int:
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    for t in tests:
        try:
            t()
        except Exception as exc:  # a raised error counts as a failure, named
            _failures.append(f"{t.__name__} raised {type(exc).__name__}: {exc}")
    total = len(tests)
    passed = total - len(_failures)
    print(f"{passed}/{total} passed")
    for f in _failures:
        print(f"  FAIL: {f}")
    return 0 if not _failures else 1


if __name__ == "__main__":
    sys.exit(main())
