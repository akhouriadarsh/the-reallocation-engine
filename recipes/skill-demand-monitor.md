# skill-demand-monitor -- Tool And Stack Signals For Job Intelligence

## Purpose

Adapted from martech/product positioning and tech-stack signal recipes. Use this recipe to infer which tools, platforms, and technical skills are appearing in target-company materials and job postings, then map them to resume keywords, training priorities, and interview preparation.

## Source Inventory

| Source Node | Node Type | Source URL or Path | Human Check |
|---|---|---|---|
| Recipe specification | Markdown recipe | `recipes/skill-demand-monitor.md` | Confirm this specification is current and approved before script generation. |

## Inputs

| Input | Type | Source | Required? |
|---|---|---|---|
| Job postings | Markdown/CSV/HTML | ATS scan outputs or saved postings | Yes |
| Company/product sources | Markdown/RSS/API | `[TODO: DATA SOURCE] company docs, engineering blogs, product pages, or release notes` | No |
| Skill taxonomy | JSON/Markdown | `[TODO: DEFINE] map tools to skill categories and resume labels` | Yes |

## Phase Gates

1. Source gate: All required source paths are present or explicitly marked with a typed TODO. Test: `test -f "recipes/skill-demand-monitor.md" && rg -n "\[TODO: DEFINE]" "recipes/skill-demand-monitor.md" || true`. Human capacity: [TO].
2. Scope gate: The run declares `sample` mode or an approved live mode before ingest begins. Test: `python3 -m json.tool data/raw/skill-demand-monitor/run-envelope.json`. Human capacity: [PF].
3. Data-shape gate: Every raw and verified JSON output parses before downstream scripts run. Test: `find data/raw/skill-demand-monitor data/verified/skill-demand-monitor -name "*.json" -print -exec python3 -m json.tool {} \;`. Human capacity: [PA].
4. Script-readiness gate: Every step script exists or is represented by a typed development TODO. Test: `test -f scripts/ingest/skill-demand-monitor-ingest-inputs.py || rg --fixed-strings "[TODO: DEV]" "recipes/skill-demand-monitor.md"`. Human capacity: [IJ].
5. Approval gate: Live network calls, external writes, credentials, production databases, emails, dashboards, publishing, or model calls with sensitive data require an approval record. Test: `test -f logs/gate-decisions/skill-demand-monitor-approval.json || rg --fixed-strings "[TODO: APPROVE]" "recipes/skill-demand-monitor.md"`. Human capacity: [EI].
6. Report gate: Agent log and human report are written with the required fields and sections. Test: `test -f logs/skill-demand-monitor-[DATE].json && test -f reports/generated/skill-demand-monitor-[DATE].md`. Human capacity: [TO].

## Steps

1. Step name: Verify provenance. Labor: AI with Human gate.
   Script called: `scripts/tools/skill-demand-monitor-verify-provenance.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `skill-demand-monitor`.
   Output: workflow, source_paths, exists, parsed_ok, approval_state, checked_at.
   Where output goes: `logs/`
2. Step name: Ingest declared inputs. Labor: AI with Human gate.
   Script called: `scripts/ingest/skill-demand-monitor-ingest-inputs.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `skill-demand-monitor`.
   Output: records, source_name, source_type, fetched_at, sample_mode, rejects.
   Where output goes: `data/raw/skill-demand-monitor/`
3. Step name: Validate data shape. Labor: AI with Human gate.
   Script called: `scripts/gigo/skill-demand-monitor-validate-data-shape.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `skill-demand-monitor`.
   Output: record_count, required_fields_present, missing_fields, parse_errors, schema_version.
   Where output goes: `data/verified/skill-demand-monitor/`
4. Step name: Transform and quality check. Labor: AI with Human gate.
   Script called: `scripts/gigo/skill-demand-monitor-transform-quality-check.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `skill-demand-monitor`.
   Output: verified_records, record_count, duplicates, rejects, flags, quality_notes.
   Where output goes: `data/verified/skill-demand-monitor/`
5. Step name: Run approved tools. Labor: AI with Human gate.
   Script called: `scripts/tools/skill-demand-monitor-run-approved-tools.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `skill-demand-monitor`.
   Output: tool_name, input_path, output_path, action_taken, approval_id, no_write_mode.
   Where output goes: `logs/`
6. Step name: Produce human report. Labor: AI with Human gate.
   Script called: `scripts/tools/skill-demand-monitor-produce-human-report.py` [TODO: DEV] Define input schema, output schema, transformation logic, and error handling for this script before implementation.
   Input: declared recipe inputs, prior step outputs, and gate decisions for `skill-demand-monitor`.
   Output: summary, sources_checked, gate_results, findings, typed_todos, next_decision.
   Where output goes: `reports/generated/`

## Output Contract

### Agent output
File: `logs/skill-demand-monitor-[DATE].json`
Fields: workflow, run_id, mode, steps_completed, records_seen, rejects, duplicates, flags, stop_conditions, todo_items, source_files, gate_decisions, generated_at, raw_output_paths, verified_output_paths, report_path.

### Human report
File: `reports/generated/skill-demand-monitor-[DATE].md`
Reader: domain lead or human boss responsible for accepting the `skill-demand-monitor -- Tool And Stack Signals For Job Intelligence` run.
Decision enabled: approve the run for the next phase, request source/schema fixes, or block live execution.
Sections: run summary, purpose, source inventory, inputs used, phase-gate results, steps completed, records seen, rejects, duplicates, flags, typed TODOs, human approvals, verified findings, inferred findings, decision recommendation.

## Stop Conditions

- Stop if skill taxonomy is missing.
- Stop if the report recommends adding skills not supported by student evidence.
- Stop if job postings are stale or lack URLs.
- Stop if training recommendations cannot be tied to target roles.

## Snickerdoodle

### Run Commands
Full dialogic run:
`snickerdoodle run skill-demand-monitor --mode dialogic`

Sample mode (no live network calls, no writes):
`snickerdoodle run skill-demand-monitor --mode dialogic --sample`

### Step Commands

| Step | CLI Command | Flags |
|---|---|---|
| Verify provenance | `snickerdoodle run skill-demand-monitor --step verify-provenance` | `--sample` `--no-write` |
| Ingest declared inputs | `snickerdoodle run skill-demand-monitor --step ingest-inputs` | `--sample` |
| Validate data shape | `snickerdoodle run skill-demand-monitor --step validate-data-shape` | `--sample` |
| Transform and quality check | `snickerdoodle run skill-demand-monitor --step transform-quality-check` | `--sample` |
| Run approved tools | `snickerdoodle run skill-demand-monitor --step run-approved-tools` | `--sample` `--no-write` |
| Produce human report | `snickerdoodle run skill-demand-monitor --step produce-human-report` | `--sample` `--no-write` |

### Gate Commands

| Gate | CLI Command |
|---|---|
| Gate 1 - Source gate | `snickerdoodle gate skill-demand-monitor --gate 1 --decision approve --note "Sources checked"` |
| Gate 2 - Scope gate | `snickerdoodle gate skill-demand-monitor --gate 2 --decision approve --note "Scope and mode approved"` |
| Gate 3 - Data-shape gate | `snickerdoodle gate skill-demand-monitor --gate 3 --decision approve --note "Outputs parse"` |
| Gate 4 - Script-readiness gate | `snickerdoodle gate skill-demand-monitor --gate 4 --decision approve --note "Scripts ready or TODO DEV accepted"` |
| Gate 5 - Approval gate | `snickerdoodle gate skill-demand-monitor --gate 5 --decision approve --note "Live or sensitive actions approved"` |
| Gate 6 - Report gate | `snickerdoodle gate skill-demand-monitor --gate 6 --decision approve --note "Report and log complete"` |

### Script Locations

| Step | Script Path | Layer |
|---|---|---|
| Verify provenance | `scripts/tools/skill-demand-monitor-verify-provenance.py` | tools |
| Ingest declared inputs | `scripts/ingest/skill-demand-monitor-ingest-inputs.py` | ingest |
| Validate data shape | `scripts/gigo/skill-demand-monitor-validate-data-shape.py` | gigo |
| Transform and quality check | `scripts/gigo/skill-demand-monitor-transform-quality-check.py` | gigo |
| Run approved tools | `scripts/tools/skill-demand-monitor-run-approved-tools.py` | tools |
| Produce human report | `scripts/tools/skill-demand-monitor-produce-human-report.py` | tools |

### Output Locations

| Output | Path | Format |
|---|---|---|
| Raw ingest | `data/raw/skill-demand-monitor/` | JSON |
| Verified data | `data/verified/skill-demand-monitor/` | JSON |
| Agent log | `logs/skill-demand-monitor-[DATE].json` | JSON |
| Human report | `reports/generated/skill-demand-monitor-[DATE].md` | Markdown |
| Gate decisions | `logs/gate-decisions/` | JSON |

## Provenance

| Source | Verification command | Notes |
|---|---|---|
| `data/ats/applications.md` | `test -f "data/ats/applications.md"` | Referenced source/evidence path from prior recipe text. |
| `recipes/apply.md` | `test -f "recipes/apply.md"` | Referenced source/evidence path from prior recipe text. |
| `recipes/interview-prep.md` | `test -f "recipes/interview-prep.md"` | Referenced source/evidence path from prior recipe text. |
| `recipes/training.md` | `test -f "recipes/training.md"` | Referenced source/evidence path from prior recipe text. |

## Existing Recipe Notes Preserved For Implementation

### Workflow

1. Extract tools, platforms, frameworks, and certifications from job postings.
2. Optionally enrich with company docs and product pages.
3. Normalize mentions into skill category, tool name, evidence source, and count.
4. Compare extracted skills against the student's profile.
5. Produce resume keyword suggestions and training priorities.
6. Human approves which skills move to resume, project, or training work.
