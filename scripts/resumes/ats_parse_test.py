#!/usr/bin/env python3
"""
ATS parse-test harness for The Reallocation Engine.

The repo's `scripts/resumes/generate-pdf.mjs` renders "ATS-friendly" PDFs from
Markdown CVs, but nothing verifies that the fields actually survive parsing.
This harness closes that gap. It re-reads a generated PDF with independent text
extractors and reports, per field, whether the content in the source Markdown CV
is recoverable from the PDF's text layer.

WHAT IT VERIFIES (every field traces to a record in the source CV, or is a
labeled script-output):
  * name (H1) survives
  * contact tokens survive (email, phone, each URL)
  * every `## ` section heading survives   (+ observed case in the PDF)
  * every `### ` entry heading survives
  * every date range survives
  * bullets survive AND stay separate (strict boundary check catches merges)
  * the renderer's own normalization promises hold in the PDF text layer
    (no smart dashes, no curly quotes, no ellipsis char, no zero-width chars)

WHAT IT CANNOT VERIFY (stated plainly, not hidden):
  * whether a *real* ATS (Workday, Greenhouse) parses the same way. This harness
    uses proxy extractors (pdfplumber / pypdf / pdftotext), not a real ATS.
    A PASS means "our extractor recovered the field," not "an employer's ATS will."

EMPTY vs ERROR are never conflated:
  * EMPTY  = the source CV has no such field, so there is nothing to check.
  * ERROR  = the field IS in the source CV but was NOT recovered from the PDF.

Exit codes:
  0  every ERROR-eligible check PASSED (EMPTY / SKIP do not fail the run)
  1  at least one field is ERROR (present in source, lost in PDF)
  2  precondition failure (PDF missing, or no extractor available) — the run
     did not happen; this is not scored as a field result.

Usage:
  python3 scripts/resumes/ats_parse_test.py resumes/aarav-patel-cv.md
  python3 scripts/resumes/ats_parse_test.py resumes/aarav-patel-cv.md --pdf output/resumes/aarav-patel-cv.pdf
  python3 scripts/resumes/ats_parse_test.py --all
  python3 scripts/resumes/ats_parse_test.py resumes/aarav-patel-cv.md --json

Dependencies (install once, in the repo venv):
  pip install pdfplumber pypdf
  # optional third extractor comes from poppler's `pdftotext` if on PATH
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import unicodedata
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

# scripts/resumes/ats_parse_test.py -> repo root is two parents up
REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PDF_DIR = REPO_ROOT / "output" / "resumes"
DEFAULT_REPORT_DIR = REPO_ROOT / "reports" / "generated"

# --- character classes that the renderer's normalizeTextForATS() promises to remove ---
ZERO_WIDTH = "\u200b\u200c\u200d\u2060\ufeff"
CURLY_DQUOTES = "\u201c\u201d\u201e\u201f"
CURLY_SQUOTES = "\u2018\u2019\u201a\u201b"
FANCY_DASHES = "\u2014\u2013"
ELLIPSIS_CHAR = "\u2026"

MONTHS = (
    "Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec|"
    "January|February|March|April|June|July|August|September|October|November|December"
)
# "Mon YYYY - Mon YYYY", "Mon YYYY - Present", allowing hyphen or en/em dash
DATE_RANGE_RE = re.compile(
    rf"((?:{MONTHS})\.?\s+\d{{4}}\s*[-\u2013\u2014]\s*(?:(?:{MONTHS})\.?\s+\d{{4}}|Present|Current))"
)
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")
PHONE_RE = re.compile(r"\(?\d{3}\)?[\s.\-]?\d{3}[\s.\-]?\d{4}")
# domain-ish tokens (github.com/..., linkedin.com/..., aaravpatel.dev) — not emails
URL_RE = re.compile(
    r"\b(?:https?://)?(?:www\.)?(?:[A-Za-z0-9\-]+\.)+"
    r"(?:com|dev|io|org|net|ai|me|co|xyz|app|tech)\b[A-Za-z0-9./_\-]*",
    re.IGNORECASE,
)

STATUS_PASS = "PASS"
STATUS_FAIL = "FAIL"   # ERROR: in source, lost in PDF
STATUS_WRAP = "WRAP"   # present, but split across a line break (line-wrap risk)
STATUS_EMPTY = "EMPTY"  # not in source; nothing to check
STATUS_SKIP = "SKIP"   # extractor unavailable


# ----------------------------------------------------------------------------- #
# Normalization
# ----------------------------------------------------------------------------- #
def normalize_ats(text: str) -> str:
    """Mirror generate-pdf.mjs `normalizeTextForATS()` exactly."""
    if not text:
        return ""
    for ch in FANCY_DASHES:
        text = text.replace(ch, "-")
    for ch in CURLY_DQUOTES:
        text = text.replace(ch, '"')
    for ch in CURLY_SQUOTES:
        text = text.replace(ch, "'")
    text = text.replace(ELLIPSIS_CHAR, "...")
    for ch in ZERO_WIDTH:
        text = text.replace(ch, "")
    text = text.replace("\u00a0", " ")
    return text


def strip_md_inline(text: str) -> str:
    """
    Remove Markdown inline markers the way the renderer's inlineMarkdown() does:
    `**bold**` -> `bold`, `` `code` `` -> `code`. The markers never reach the
    PDF text layer, so ground truth must drop them too or a rendered field
    false-FAILs. (Found by test_clean_extraction_all_pass.)
    """
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    return text


def canon(text: str, *, casefold: bool = False) -> str:
    """
    Canonical form for MATCHING both sides of a comparison. Strips Markdown
    inline syntax, applies the same normalization the renderer does, then
    NFKC + whitespace-collapse so that a dash/whitespace/quote/marker
    difference between source and PDF never causes a false FAIL. This
    two-sided normalization is the fix for the drift break.
    """
    t = strip_md_inline(text)
    t = normalize_ats(t)
    t = unicodedata.normalize("NFKC", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t.casefold() if casefold else t


# ----------------------------------------------------------------------------- #
# Ground truth: parse the source Markdown CV
# ----------------------------------------------------------------------------- #
@dataclass
class GroundTruth:
    name: str | None = None
    contact_line: str | None = None
    emails: list[str] = field(default_factory=list)
    phones: list[str] = field(default_factory=list)
    urls: list[str] = field(default_factory=list)
    sections: list[str] = field(default_factory=list)   # ## headings
    entries: list[str] = field(default_factory=list)     # ### headings
    date_ranges: list[str] = field(default_factory=list)
    bullets: list[str] = field(default_factory=list)


def parse_ground_truth(markdown: str) -> GroundTruth:
    gt = GroundTruth()
    lines = markdown.split("\n")
    seen_h1 = False
    contact_captured = False

    for raw in lines:
        line = raw.strip()
        if not line:
            continue

        h = re.match(r"^(#{1,6})\s+(.+)$", line)
        if h:
            level, textval = len(h.group(1)), h.group(2).strip()
            if level == 1 and gt.name is None:
                gt.name = textval
                seen_h1 = True
            elif level == 2:
                gt.sections.append(textval)
            elif level == 3:
                gt.entries.append(textval)
            continue

        b = re.match(r"^-\s+(.+)$", line)
        if b:
            gt.bullets.append(b.group(1).strip())
            continue

        # first non-heading, non-bullet paragraph after the H1 == contact line
        if seen_h1 and not contact_captured and not gt.sections:
            gt.contact_line = line
            contact_captured = True

    # contact tokens (from the whole doc, but contact line is where they live)
    source_for_contacts = gt.contact_line or markdown
    gt.emails = _dedupe(EMAIL_RE.findall(source_for_contacts))
    gt.phones = _dedupe(PHONE_RE.findall(source_for_contacts))
    # blank emails first so an email's domain (e.g. example.com) is not
    # mistaken for a portfolio URL
    url_source = EMAIL_RE.sub(" ", source_for_contacts)
    urls = [u for u in URL_RE.findall(url_source) if "@" not in u]
    gt.urls = _dedupe(urls)

    gt.date_ranges = _dedupe(m.group(1) for m in DATE_RANGE_RE.finditer(markdown))
    return gt


def _dedupe(items) -> list[str]:
    out, seen = [], set()
    for it in items:
        key = canon(it, casefold=True)
        if key and key not in seen:
            seen.add(key)
            out.append(it.strip())
    return out


# ----------------------------------------------------------------------------- #
# Extractors (independent, so disagreement is a finding)
# ----------------------------------------------------------------------------- #
def extract_pdfplumber(pdf_path: Path) -> str | None:
    try:
        import pdfplumber  # type: ignore
    except ImportError:
        return None
    with pdfplumber.open(str(pdf_path)) as pdf:
        return "\n".join((p.extract_text() or "") for p in pdf.pages)


def extract_pypdf(pdf_path: Path) -> str | None:
    try:
        from pypdf import PdfReader  # type: ignore
    except ImportError:
        return None
    reader = PdfReader(str(pdf_path))
    return "\n".join((pg.extract_text() or "") for pg in reader.pages)


def extract_pdftotext(pdf_path: Path) -> str | None:
    if not shutil.which("pdftotext"):
        return None
    try:
        res = subprocess.run(
            ["pdftotext", "-layout", str(pdf_path), "-"],
            capture_output=True, text=True, timeout=60,
        )
        return res.stdout if res.returncode == 0 else None
    except Exception:
        return None


EXTRACTORS = [
    ("pdfplumber", extract_pdfplumber),
    ("pypdf", extract_pypdf),
    ("pdftotext", extract_pdftotext),
]


# ----------------------------------------------------------------------------- #
# Checks
# ----------------------------------------------------------------------------- #
@dataclass
class Result:
    category: str
    label: str
    status: str
    detail: str = ""


def _present(needle: str, hay_canon: str) -> bool:
    n = canon(needle, casefold=True)
    return bool(n) and n in hay_canon


def _survival(needle: str, hay_canon: str, hay_despaced: str) -> tuple[str, str] | None:
    """
    Classify a token-like field (URL, email, phone, date range):
      PASS  = present contiguously
      WRAP  = every character is present, but a line break split the token
              (a real line-wrap risk: a line-by-line ATS may miss it)
      FAIL  = not recovered at all
    Returns None if the needle is empty.
    """
    n = canon(needle, casefold=True)
    if not n:
        return None
    if n in hay_canon:
        return STATUS_PASS, ""
    if re.sub(r"\s+", "", n) in hay_despaced:
        return STATUS_WRAP, "survived but split across a line break (line-wrap risk)"
    return STATUS_FAIL, "not recovered"


def check_text(gt: GroundTruth, extracted: str) -> list[Result]:
    """Run every field check against ONE extractor's output."""
    results: list[Result] = []
    hay = canon(extracted, casefold=True)
    hay_despaced = re.sub(r"\s+", "", hay)
    lines_canon = [canon(ln, casefold=True) for ln in extracted.split("\n") if ln.strip()]

    # name
    if gt.name is None:
        results.append(Result("name", "name", STATUS_EMPTY, "no H1 in source"))
    else:
        results.append(Result(
            "name", gt.name,
            STATUS_PASS if _present(gt.name, hay) else STATUS_FAIL,
        ))

    # contact (WRAP-aware: single tokens should never contain a line break)
    for cat, items in (("email", gt.emails), ("phone", gt.phones), ("url", gt.urls)):
        if not items:
            results.append(Result("contact", cat, STATUS_EMPTY, "none in source"))
            continue
        for it in items:
            status, detail = _survival(it, hay, hay_despaced)
            results.append(Result("contact", it, status, detail))

    # section headings (case-insensitive survival + observed case in PDF)
    if not gt.sections:
        results.append(Result("section", "sections", STATUS_EMPTY, "none in source"))
    for sec in gt.sections:
        ok = _present(sec, hay)
        observed = _observed_case(sec, extracted)
        detail = f"observed as '{observed}'" if observed else ""
        results.append(Result("section", sec, STATUS_PASS if ok else STATUS_FAIL, detail))

    # entry headings
    if not gt.entries:
        results.append(Result("entry", "entries", STATUS_EMPTY, "none in source"))
    for ent in gt.entries:
        results.append(Result(
            "entry", ent,
            STATUS_PASS if _present(ent, hay) else STATUS_FAIL,
        ))

    # date ranges (WRAP-aware)
    if not gt.date_ranges:
        results.append(Result("date", "date ranges", STATUS_EMPTY, "none in source"))
    for dr in gt.date_ranges:
        status, detail = _survival(dr, hay, hay_despaced)
        results.append(Result("date", dr, status, detail))

    # bullets: STRICT boundary check (catches merges that a naive substring
    # test would miss). A bullet PASSES only if its distinctive leading
    # fragment appears at the START of some extracted line.
    if not gt.bullets:
        results.append(Result("bullet", "bullets", STATUS_EMPTY, "none in source"))
    for bullet in gt.bullets:
        frag = canon(bullet, casefold=True)[:40]
        if not frag:
            continue
        naive = frag in hay
        strict = any(ln.startswith(frag) for ln in lines_canon)
        if strict:
            status, detail = STATUS_PASS, ""
        elif naive:
            status, detail = STATUS_FAIL, "present but not at a line start (merged bullet)"
        else:
            status, detail = STATUS_FAIL, "not recovered"
        results.append(Result("bullet", bullet[:48] + ("..." if len(bullet) > 48 else ""),
                              status, detail))

    # renderer normalization promises, verified in the actual PDF text layer
    results.extend(check_normalization(extracted))
    return results


def _observed_case(section: str, extracted: str) -> str | None:
    m = re.search(re.escape(section), extracted, re.IGNORECASE)
    return m.group(0) if m else None


def check_normalization(extracted: str) -> list[Result]:
    checks = [
        ("no-zero-width", ZERO_WIDTH, "zero-width chars"),
        ("no-curly-quotes", CURLY_DQUOTES + CURLY_SQUOTES, "curly quotes"),
        ("no-fancy-dashes", FANCY_DASHES, "en/em dashes"),
        ("no-ellipsis-char", ELLIPSIS_CHAR, "ellipsis char U+2026"),
    ]
    out = []
    for label, chars, human in checks:
        found = [c for c in chars if c in extracted]
        out.append(Result(
            "normalize", label,
            STATUS_FAIL if found else STATUS_PASS,
            f"found {human}: {[hex(ord(c)) for c in found]}" if found else "",
        ))
    return out


# ----------------------------------------------------------------------------- #
# Orchestration
# ----------------------------------------------------------------------------- #
@dataclass
class ExtractorRun:
    name: str
    results: list[Result]


def score(results: list[Result]) -> dict:
    eligible = [r for r in results if r.status in (STATUS_PASS, STATUS_FAIL, STATUS_WRAP)]
    passed = sum(1 for r in eligible if r.status == STATUS_PASS)
    failed = sum(1 for r in eligible if r.status == STATUS_FAIL)
    wrapped = sum(1 for r in eligible if r.status == STATUS_WRAP)
    empty = sum(1 for r in results if r.status == STATUS_EMPTY)
    # WRAP stays in the denominator so a split field is never rounded away to 100%
    rate = (passed / len(eligible)) if eligible else None
    return {"pass": passed, "fail": failed, "wrap": wrapped, "empty": empty,
            "eligible": len(eligible), "pass_rate": rate}


def run_one(md_path: Path, pdf_path: Path) -> tuple[list[ExtractorRun], GroundTruth, list[str]]:
    markdown = md_path.read_text(encoding="utf-8")
    gt = parse_ground_truth(markdown)
    runs: list[ExtractorRun] = []
    missing: list[str] = []
    for name, fn in EXTRACTORS:
        text = fn(pdf_path)
        if text is None:
            missing.append(name)
            continue
        runs.append(ExtractorRun(name, check_text(gt, text)))
    return runs, gt, missing


def disagreements(runs: list[ExtractorRun]) -> list[str]:
    """Fields where extractors disagree on PASS/FAIL — each is a finding."""
    if len(runs) < 2:
        return []
    by_key: dict[tuple[str, str], dict[str, str]] = {}
    for run in runs:
        for r in run.results:
            by_key.setdefault((r.category, r.label), {})[run.name] = r.status
    out = []
    for (cat, label), per in by_key.items():
        statuses = {s for s in per.values() if s in (STATUS_PASS, STATUS_FAIL)}
        if len(statuses) > 1:
            detail = ", ".join(f"{k}={v}" for k, v in per.items())
            out.append(f"[{cat}] {label}: {detail}")
    return out


def slug(md_path: Path) -> str:
    return md_path.stem


# ----------------------------------------------------------------------------- #
# Reporting
# ----------------------------------------------------------------------------- #
def print_console(md_path: Path, primary: ExtractorRun, all_runs: list[ExtractorRun],
                  missing: list[str], sc: dict, disagree: list[str]) -> None:
    print(f"\nATS parse-test: {md_path.name}")
    print(f"primary extractor: {primary.name}"
          + (f"  |  also ran: {', '.join(r.name for r in all_runs if r.name != primary.name)}"
             if len(all_runs) > 1 else ""))
    if missing:
        print(f"extractors unavailable (SKIP): {', '.join(missing)}")
    print("-" * 64)
    cat_order = ["name", "contact", "section", "entry", "date", "bullet", "normalize"]
    for cat in cat_order:
        rows = [r for r in primary.results if r.category == cat]
        for r in rows:
            mark = {"PASS": "PASS ", "FAIL": "FAIL ", "WRAP": "WRAP ",
                    "EMPTY": "EMPTY", "SKIP": "SKIP "}[r.status]
            extra = f"  ({r.detail})" if r.detail else ""
            print(f"  {mark} [{cat}] {r.label}{extra}")
    print("-" * 64)
    rate = "n/a" if sc["pass_rate"] is None else f"{sc['pass_rate']*100:.1f}%"
    # every number here is script-output, not a record
    print(f"  parse PASS-rate (script-output): {sc['pass']}/{sc['eligible']} = {rate}"
          f"   | WRAP (split across a line): {sc['wrap']}"
          f"   | lost: {sc['fail']}"
          f"   | EMPTY (not in source): {sc['empty']}")
    if disagree:
        print(f"  extractor disagreements ({len(disagree)}):")
        for d in disagree:
            print(f"    - {d}")
    print()


def write_report(md_path: Path, gt: GroundTruth, primary: ExtractorRun,
                 all_runs: list[ExtractorRun], missing: list[str], sc: dict,
                 disagree: list[str], report_dir: Path) -> Path:
    report_dir.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()
    out = report_dir / f"ats-parse-test-{slug(md_path)}-{today}.md"
    rate = "n/a" if sc["pass_rate"] is None else f"{sc['pass_rate']*100:.1f}%"
    lines = [
        f"# ATS parse-test audit — {md_path.name}",
        "",
        f"- date: {today}",
        f"- source CV (record): `{md_path}`",
        f"- primary extractor (script-output): {primary.name}",
        f"- extractors run: {', '.join(r.name for r in all_runs) or 'none'}",
        f"- extractors unavailable (SKIP): {', '.join(missing) or 'none'}",
        "",
        "## Verified vs inferred (this audit)",
        "- Field VALUES come from the source Markdown CV — **record**.",
        "- PASS / FAIL / EMPTY and the PASS-rate are **script-output**.",
        "- Whether a *real* ATS parses identically is **not verified** — proxy extractor only.",
        "",
        "## Result (primary extractor)",
        "",
        "| status | category | field | note |",
        "|---|---|---|---|",
    ]
    for r in primary.results:
        note = r.detail.replace("|", "\\|")
        lines.append(f"| {r.status} | {r.category} | {r.label.replace('|', '\\|')} | {note} |")
    lines += [
        "",
        f"**parse PASS-rate (script-output):** {sc['pass']}/{sc['eligible']} = {rate}  ",
        f"**WRAP (present but split across a line break — line-wrap risk):** {sc['wrap']}  ",
        f"**lost (in source, not recovered):** {sc['fail']}  ",
        f"**EMPTY (absent from source, not a failure):** {sc['empty']}",
        "",
    ]
    if disagree:
        lines.append("## Extractor disagreements (findings)")
        lines += [f"- {d}" for d in disagree]
        lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


# ----------------------------------------------------------------------------- #
# CLI
# ----------------------------------------------------------------------------- #
def discover_all() -> list[Path]:
    resumes = REPO_ROOT / "resumes"
    if not resumes.is_dir():
        return []
    return sorted(p for p in resumes.glob("*-cv.md"))


def resolve_pdf(md_path: Path, pdf_arg: str | None) -> Path:
    if pdf_arg:
        return Path(pdf_arg).resolve()
    return DEFAULT_PDF_DIR / f"{md_path.stem}.pdf"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Re-parse generated résumé PDFs and report field survival.")
    ap.add_argument("md", nargs="?", help="source Markdown CV (e.g. resumes/aarav-patel-cv.md)")
    ap.add_argument("--pdf", help="generated PDF path (default: output/resumes/<name>.pdf)")
    ap.add_argument("--all", action="store_true", help="run every resumes/*-cv.md")
    ap.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    ap.add_argument("--no-report", action="store_true", help="do not write a markdown audit")
    args = ap.parse_args(argv)

    if args.all:
        targets = [(p, resolve_pdf(p, None)) for p in discover_all()]
        if not targets:
            print("No resumes/*-cv.md found.", file=sys.stderr)
            return 2
    else:
        if not args.md:
            ap.print_usage()
            return 2
        md = Path(args.md).resolve()
        if not md.exists():
            print(f"Source CV not found: {md}", file=sys.stderr)
            return 2
        targets = [(md, resolve_pdf(md, args.pdf))]

    overall_exit = 0
    json_payload = []
    for md_path, pdf_path in targets:
        if not pdf_path.exists():
            print(f"PDF not found: {pdf_path}\n"
                  f"  Generate it first:\n"
                  f"    node scripts/resumes/generate-pdf.mjs {md_path.relative_to(REPO_ROOT) if md_path.is_relative_to(REPO_ROOT) else md_path}",
                  file=sys.stderr)
            overall_exit = max(overall_exit, 2)
            continue

        runs, gt, missing = run_one(md_path, pdf_path)
        if not runs:
            print("No PDF text extractor available. Install one:\n"
                  "    pip install pdfplumber pypdf", file=sys.stderr)
            return 2

        primary = runs[0]  # pdfplumber if present (best ATS proxy), else next available
        sc = score(primary.results)
        disagree = disagreements(runs)

        if args.json:
            json_payload.append({
                "cv": str(md_path), "pdf": str(pdf_path),
                "primary_extractor": primary.name,
                "extractors_run": [r.name for r in runs],
                "extractors_missing": missing,
                "score": sc,
                "results": [vars(r) for r in primary.results],
                "disagreements": disagree,
            })
        else:
            print_console(md_path, primary, runs, missing, sc, disagree)
            if not args.no_report:
                report = write_report(md_path, gt, primary, runs, missing, sc, disagree,
                                      DEFAULT_REPORT_DIR)
                print(f"  audit written: {report.relative_to(REPO_ROOT) if report.is_relative_to(REPO_ROOT) else report}\n")

        if sc["fail"] > 0:
            overall_exit = max(overall_exit, 1)

    if args.json:
        print(json.dumps(json_payload, indent=2, ensure_ascii=False))

    return overall_exit


if __name__ == "__main__":
    sys.exit(main())
