# Agent Instructions

Read `MYCROFT.md` before doing anything. It is the source of truth for this repository — the principles, the verification stack, the recipe lifecycle, and the logging rules. Then read `DOMAIN.md` for this repository's domain, layout, and what is runnable today.

If any other file conflicts with `MYCROFT.md`, `MYCROFT.md` governs and the conflict is a bug — log it in `logs/RUN_LOG.md`.

Summary of the contract (the full version in MYCROFT.md governs):

1. Verified local data before external lookup; stored scripts before ad hoc code.
2. Never invent a count, rate, or confidence; label model judgments as judgments.
3. Gates are hard stops cleared by a named human and logged.
4. Machines verify conformance; humans verify adequacy.
5. Log meaningful runs, blockers, and artifacts in `logs/RUN_LOG.md`.
