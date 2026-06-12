# Tutorial 01 — Your First Scan

**What you'll do:** configure the ATS scanner, predict what it will find, run it without writing anything, read the output line by line, judge whether it's right, and record what happened.
**Time:** about 30 minutes.
**You need:** Node 18+, this repository cloned, and a terminal at the repo root.

This tutorial trains the loop everything else in this system uses: **run → inspect → record**. You will also make your first prediction and your first log entry. Neither is optional — they are the exercise.

---

## The concepts, in sixty seconds

An **ATS** (Applicant Tracking System) is the software a company uses to host its job postings — Greenhouse, Lever, and Ashby are the three this scanner speaks to. Each has a public JSON API behind its job board, which means a scanner can ask "what jobs does Databricks have posted right now?" without a browser, without scraping HTML, and without an AI model. Zero tokens; pure HTTP.

A **provider** is the plugin that knows how to talk to one ATS (`scripts/ats/providers/greenhouse.mjs`, `lever.mjs`, `ashby.mjs`).

**`--dry-run`** means: do everything except write files. The scan runs, the filters run, the report prints — but `data/ats/pipeline.md` and `data/ats/scan-history.tsv` are not touched. You can run it as many times as you want with no consequences.

## Step 0 — Setup

```bash
npm install
```

This installs `js-yaml` and `glob` (which the scanner needs) plus `playwright` and `sharp` (which it doesn't — they're for liveness checking and image work later). If `npm install` is slow, `npm install js-yaml glob --no-save` is enough for this tutorial.

## Step 1 — Read the config before you run anything

Open `data/ats/portals.example.yml` in an editor. Don't run anything yet. This file is the scanner's entire instruction set, and you should be able to predict the scan's behavior from it. Three sections:

**`title_filter`** — postings must match at least one `positive` keyword ("Software", "Engineer", "AI", "Machine Learning", "Data", "Product") and no `negative` keyword ("Intern", "Volunteer"). A posting titled "Machine Learning Intern" matches a positive *and* a negative — it gets filtered out.

**`location_filter`** — postings located in "United States", "USA", or "Remote" pass; everything else is removed. If this section were deleted, all locations would pass.

**`tracked_companies`** — the list of companies to scan. Look closely:

```yaml
  - name: Databricks
    enabled: true
    provider: greenhouse
    careers_url: https://job-boards.greenhouse.io/databricks
```

Only Databricks is `enabled: true`. The Lever and Ashby entries are `enabled: false` placeholders. So this config scans exactly **one** company, via the Greenhouse provider.

## Step 2 — Predict

Before running, write down (really — in a scratch file or notebook):

1. How many companies will be scanned?
2. Roughly how many jobs do you expect a company like Databricks to have posted? 10? 100? 1,000?
3. Of those, what fraction will survive the title and location filters?

This isn't busywork. The entire point of this system is that you, not the tool, are the judge of whether output makes sense — and you can't judge output against an expectation you never formed. (MYCROFT.md P1: machines verify conformance; humans verify adequacy.)

## Step 3 — Make the config real

The scanner reads `data/ats/portals.yml` by default — which doesn't exist yet. Copy the example:

```bash
cp data/ats/portals.example.yml data/ats/portals.yml
```

**Privacy note:** `portals.yml` is *your* target list — it reveals your job-search activity. It belongs to you, not to git. Check `git status` before any commit; per `DOMAIN.md`, everything under `data/ats/` is private by default.

(Alternative, without copying: `REALLOCATION_ENGINE_PORTALS=data/ats/portals.example.yml npm run ats:scan -- --dry-run`.)

## Step 4 — Run it

```bash
npm run ats:scan -- --dry-run
```

Reading that command left to right: `npm run ats:scan` invokes the script registered in `package.json` (which runs `node scripts/ats/scan.mjs`); the bare `--` means "everything after this belongs to the script, not to npm"; `--dry-run` is the no-writes flag. Forgetting the `--` is the classic mistake — npm silently swallows the flag and the scan **will write files**.

## Step 5 — Read the output, line by line

You'll see a report like this (numbers will differ — that's the point):

```
Scanning 1 companies via providers (0 local parser; 0 skipped — no provider matched)
(dry run — no files will be written)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Portal Scan — 2026-06-12
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Companies scanned:     1
Total jobs found:      247
Filtered by title:     163 removed
Filtered by location:  41 removed
Duplicates:            0 skipped
New offers added:      43
```

What each line is telling you:

| Line | Meaning | What to check |
|---|---|---|
| `Scanning 1 companies` | how many `enabled: true` entries matched a provider | should equal your count from Step 2, Q1 |
| `Total jobs found` | raw postings returned by the ATS API, before any filtering | compare to your Step 2, Q2 guess |
| `Filtered by title` | removed for matching no positive keyword, or a negative one | large number = your filters are doing work |
| `Filtered by location` | removed by the location filter | |
| `Duplicates` | already present in `pipeline.md` or seen earlier this scan | 0 on a first run; nonzero on a re-run without dry-run |
| `New offers added` | what would be written to `pipeline.md` (but wasn't — dry run) | this is your actual yield |

**If you instead see** `Errors (1): ✗ Databricks: fetch failed` — the scan machinery worked but the HTTP request didn't. Causes in likelihood order: no network, a firewall/proxy blocking `job-boards.greenhouse.io`, or the company moved its board. The error being *surfaced* rather than swallowed is correct behavior. Distinguish what was verified (config parsing, provider matching, the pipeline logic) from what wasn't (the live fetch) — that distinction goes in your log entry.

## Step 6 — Judge

The numbers are conformant (the script ran, the arithmetic adds up). Are they *adequate*? Two checks no script can do for you:

1. Open `https://job-boards.greenhouse.io/databricks` in a browser. Eyeball the posting count. Is `Total jobs found` in the same ballpark? If the page shows ~250 and the scan found 247, good. If the page shows 600 and the scan found 247, something is wrong — and "the tool said 247" is not an answer.
2. Look at the yield: `New offers added / Total jobs found`. If 95% of postings survived your filters, your filters are decorative. If 2% survived, they may be too aggressive. What's the *right* yield? That depends on what you're searching for — which is exactly why it's your call and not the scanner's.

## Step 7 — Record

Append an entry to `logs/RUN_LOG.md`:

```markdown
## YYYY-MM-DD — Tutorial 01: first scan (dry run)

- **Recipe:** scan (tutorial)
- **Inputs:** `data/ats/portals.yml` (1 company enabled: Databricks), `npm run ats:scan -- --dry-run`
- **Outputs:** none written (dry run); report read
- **Result:** [your numbers]. Predicted [your Step 2 numbers]; actual differed by [what and why you think].
- **Open issues:** [anything that surprised you, failed, or wasn't checked]
```

The prediction-vs-actual line is the valuable part. Write it honestly — a wildly wrong prediction with a good explanation is a better entry than a lucky guess.

---

## Exercises

Every exercise ends with a RUN_LOG entry. The log entry *is* the deliverable — for each one, record what you ran, what you saw, what you expected, and what you didn't check.

**1. Filter surgery (warm-up).** Remove `"Intern"` from the negative filter. Predict the change in `Filtered by title` before re-running. Run, compare, restore the filter. One sentence: why did the number move by that amount and not another?

**2. Add a company.** Pick a real company you'd actually target. Find its ATS by visiting its careers page and looking at the URL the job listings live on: `job-boards.greenhouse.io/<slug>` → greenhouse, `jobs.lever.co/<slug>` → lever, `jobs.ashbyhq.com/<slug>` → ashby. Add a `tracked_companies` entry with `enabled: true`, predict the new totals, run. If your company uses none of the three (Workday, iCIMS, SuccessFactors…), document that finding instead — "this scanner cannot see X because no provider exists" is a real result, and a [TODO: DEV] in the making.

**3. Single-company scan.** `npm run ats:scan -- --dry-run --company Databricks`. When would you reach for this flag instead of a full scan?

**4. Break it on purpose.** Set `provider: greenhose` (typo intended) on a company and run. Read the actual message. Is this failure a halt or a report? Should it be? Now you've met the conformance/adequacy boundary from MYCROFT.md in the wild — say which side this error sits on and whether the script agrees with you.

**5. The discrepancy hunt.** Compare the scan's `Total jobs found` for one company against its public board in a browser. They will rarely match exactly. Find one specific posting that explains part of the gap (a department the API exposes but the page hides, a location variant your filter eats, a posting added since your scan). Name it.

**6. Attest.** Write an attestation-format record (MYCROFT.md format: Ran/Saw/Expected table, mandatory *Did not test* section) covering exercises 1–5. At least one row must be exercise 4 — a deliberate break. This is a rehearsal: the format you just used on a tutorial is the same one that graduates a real recipe to VERIFIED.

---

## What can go wrong

| Symptom | Likely cause | Fix |
|---|---|---|
| `Cannot find module 'js-yaml'` | skipped Step 0 | `npm install` |
| scan ignores `--dry-run` and writes files | missing `--` separator | `npm run ats:scan -- --dry-run` |
| `0 companies` scanned | nothing `enabled: true`, or provider name typo | check `enabled:` and `provider:` |
| `fetch failed` | network/proxy, or board moved | try the careers_url in a browser; see Step 5 |
| scan can't find config | no `data/ats/portals.yml` | Step 3, or set `REALLOCATION_ENGINE_PORTALS` |

**Next:** Tutorial 02 (planned) takes the URLs a real (non-dry) scan writes to `data/ats/pipeline.md` and checks whether the postings are actually alive.
