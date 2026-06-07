# Chapter 8 — Is the Job Real: ATS Detection and Liveness
*A posting is not a job opening — it is a signal, and signals can lie.*

Here is a number that should bother you. Somewhere between 28 and 42 percent of job postings, depending on the study and the year, are ghosts — listings a company has no active intention of filling. One survey found 81 percent of recruiters admitting to posting jobs they weren't actually hiring for. That figure has held roughly steady across five years of measurement, which means it isn't an artifact of a particular labor market cycle. It is a structural feature of how hiring works, or rather, how it appears to work from the outside.

I want to sit with that before we get to the detection problem, because the number is stranger than it looks. A ghost job isn't a posting that went live and then the position was cancelled. It's a posting that was never, at the moment of posting, connected to an intention to hire someone. It can be a pipeline hedge — the company isn't hiring now but wants résumés queued when it does. It can be a signal to investors that the firm is growing. It can be bureaucratic inertia: a listing that went up two quarters ago and no one has gotten around to taking down. Whatever the cause, the effect for a candidate on a finite clock is the same. A day spent writing a cover letter, tailoring a résumé, researching the company, submitting an application — to a door that was never going to open.

<!-- → [CHART: Bar chart showing ghost-job prevalence estimates across multiple studies and years (2019–2024), y-axis 0–50%, with a shaded band at 28–42% and individual city/source data points labeled (e.g., LA 30.5%, Seattle 16.6%). Caption: "Ghost-job prevalence has held in the 28–42% range across five years — not a cycle artifact but a structural feature of the posting market."] -->

The question I want to work through with you is this: can you tell, before spending that day, whether the door is real? The answer is yes — not perfectly, but well enough to matter. To see how, you have to stop reading job postings as prose and start reading them as data.

## What you are actually looking at

When you pull up a careers page in a browser, you are looking at a rendered surface. What feeds that surface is a piece of software called an applicant-tracking system — Greenhouse, Lever, Ashby are the names you'll encounter most. These are not interchangeable wrappers around the same underlying structure. Each one organizes its data differently, exposes different fields through its feed, and structures timestamps and job identifiers in its own way. That matters because the signals that distinguish a real posting from a ghost live in those fields — not in the prose of the job description, which is marketing, but in the metadata, which is evidence.

The first thing I do when I hit a new company is run a single script:

```bash
python scripts/ats/detect-ats.py --company "Example Bio"
```

It returns a label — Greenhouse, Lever, Ashby, or unknown. That label is not interesting on its own. What it unlocks is the ability to read the feed correctly. A scraper built for Greenhouse reads Lever data as noise. Detection is the key; without it, everything downstream is garbled.

<!-- → [DIAGRAM: Three ATS platforms (Greenhouse, Lever, Ashby) each shown as a box with their characteristic URL/feed structure beneath, all pointing to a unified "postings record" schema with fields: job_id, title, posted_date, last_updated, description, status. Caption: "Each ATS structures its data differently; detection tells the scraper which schema to read."] -->

Once the ATS is identified, the pipeline pulls the company's postings directly from the provider's feed — no paid model calls, just structured data read from the source:

```bash
npm run ats:scan
```

This zero-token scan matters because it runs on every company in the pipeline. At scale, what gets expensive gets skipped. A check that costs nothing gets run every time, and recency of the scan stops being a variable you manage.

## The spam filter you already trust

Here is where the detection logic becomes interesting, and where I think an analogy does real explanatory work. Ghost job detection is structurally identical to spam filtering — not metaphorically, but mechanically.

Your email filter doesn't read a suspicious message and conclude it seems dishonest. It scores the message's behavioral fingerprints against patterns of mail that is actually wanted. Temporal anomalies: sent at 3 a.m. to ten thousand addresses in twelve seconds. Interaction voids: no replies, no clicks, bounce rates in unusual ratios. Textual homogeneity: the same message reused with minor surface variation, identifiable across millions of instances. The filter assembles these signals into a probability, not a verdict, and routes accordingly. It does this a billion times a day without reading a word of content.

Ghost postings have the same fingerprints. A posting that has been up eleven weeks with no update, at a company where other listings sit frozen at similar ages, looks like a bulk send with no engagement — the temporal anomaly. A portal that has never advanced a candidate, carries no closing date, and shows no sign of iterative recruiter activity looks like mail no one is responding to — the interaction void. A job description identical to three other listings at the same company, copy-pasted from a template and minimally varied by title, looks like a mass campaign with surface variation — textual homogeneity.

No single signal is decisive. A genuinely open role can sit untouched for weeks at a slow-moving organization. A ghost can be freshly posted specifically to look active. But together, the way no individual word makes an email spam but the pattern does, they yield a classification you can defend. That is the standard I care about: not certainty, but a call traceable to the specific signals that produced it.

<!-- → [INFOGRAPHIC: Three-column layout labeled "Temporal Anomalies," "Interaction Voids," "Textual Homogeneity." Under each: two or three bullet examples from job-posting context (e.g., "unchanged for 8+ weeks," "no portal activity," "description reused across 3 listings"). Footer: "Ghost detection scores behavioral patterns — the same move your spam filter makes."] -->

## Five signals and one classification

The liveness check reads five things, in this order.

How old is the posting? Age alone is weak — the base rate of slow organizations is too high to make age decisive — but it is a prior that subsequent signals update. A nine-day posting enters the analysis differently than a seventy-seven-day posting.

When was it last updated? Posting date and update date are different fields. A three-month-old posting that was refreshed last week is behaving like an active search. A three-month-old posting frozen since the day it went up is not.

Are the company's other listings changing? This is the signal I find most diagnostic. If a company has twelve open roles and ten of them have been sitting untouched for the same number of weeks, that pattern tells you something about how the company uses its careers page — probably as a passive presence rather than an active hiring signal. If roles are appearing and disappearing, that's churn, and churn indicates an active search function.

Is the description specific? A listing that names a team lead, a project in progress, a specific dataset or codebase or migration underway, is a listing someone wrote for a real role. A listing that is word-for-word reproducible from a template — or from a prior listing at the same company — is a listing that was generated, not composed.

Does the context make an active search plausible? Funding tier, recent headcount trajectory, the occupation's demand signal from earlier in the pipeline — these are not liveness signals in themselves, but a fresh listing at a company that just closed a Series B reads differently than the same listing at a company in a freeze.

The classification runs after all five:

```bash
npm run ats:liveness
```

The output is one of three calls per posting: live, ghost, or investigate. The first two are self-explanatory. The third is the honest response to mixed signals — recent posting but templated description; stale posting at a company that just raised money. Investigate means: one cheap check resolves this faster than a blind application or a blind skip.

## One company, both doors

Let me make this concrete. A biotech with a strong sponsorship tier has two open data roles, both with the same title. `detect-ats.py` returns Greenhouse.

Posting A went up nine days ago. The description references a specific named project — a model being retrained on a new assay dataset — and names the team lead the role would report to. The company's other listings show recent count changes; two roles present last week are absent this week. Five signals, all pointing the same direction. `ats:liveness` calls it live.

Posting B has been up eleven weeks. The description is word-for-word identical to a data scientist posting the company ran eighteen months ago and to two other currently active listings under slightly different titles. No portal activity is detectable. The count for this listing has not changed across three scans. Five signals, all pointing the same direction. `ats:liveness` flags it stale — likely ghost.

The same employer. The same title. The same sponsorship tier. One of these is a door; one is a picture of a door. The decision is not about the company — the company is real. The decision is about the posting.

<!-- → [TABLE: Side-by-side comparison of Posting A vs. Posting B across five liveness signals: posting age, last-updated, description specificity, company hiring activity, portal movement. Color-coded green/red per signal. Final row: liveness classification. Caption: "Same employer, same title — the signals separate them. Liveness is a property of the listing, not the firm."] -->

## Where judgment re-enters

Here is the error the classification is most likely to induce. You get a live call and stop thinking. You treat "live" the way you would treat a verified fact — as having the same standing as a DOL filing count or a USCIS data point. It doesn't.

A liveness call is a probability, not a certification. The signals reduce the odds of wasting a day. They cannot read hiring manager intent.

A posting scored live can be a role that the company has been slow-walking through four rounds of internal headcount approval and will quietly kill if it doesn't close by quarter end. A posting scored ghost can be the one role where a slow-moving organization has a genuinely active search underway, conducted by a hiring manager who simply doesn't believe in updating careers pages. The signals catch the pattern. The exception lives in intent the pattern cannot see.

The decision rule is: *live* means apply if tier and fit hold. *Ghost* means skip. *Investigate* means one cheap check is faster than a blind application — a single direct message to a recruiter, or a look at the company's recent LinkedIn for engineering posts, takes ten minutes and gives you what the behavioral scores cannot: a human response. The liveness classification is a data claim, built from observable posting signals, logged, auditable. The reading of what that classification means for this particular company, this particular team, this particular moment is a judgment call, and it belongs to you.

## What the pipeline cannot see

I want to be clear-eyed about what this system actually measures and what it doesn't.

It measures what the posting does, not what the company intends. That gap is real.

A stale posting can be real. An organization buried in a product sprint may have a genuine open role that no one on the recruiting side has had time to update in two months. The metrics say ghost; the actual answer is "we'd love to talk, we just haven't looked at the careers page." That's a real door the filter misses. Filtering it out is the cost of the filter.

A fresh posting can be fake. A recruiter running a sourcing campaign posts a crisp, specific, recently dated listing precisely because candidates screen for recency. The posting is designed to beat the detector. The signals say live; the actual answer is résumé harvest. That's a ghost the filter misses from the other direction.

Neither failure breaks the filter. A check that eliminates 35 percent of ghost applications and occasionally miscategorizes an outlier in both directions is worth running. But knowing where it fails matters — not because you can fix it in the current architecture, but because when the signals are mixed and the role genuinely matters, the right response is a human check, not confidence in the score.

<!-- → [TABLE: Two columns — "What liveness detection catches" / "What liveness detection misses." Rows: stale-but-real (slow orgs), fresh-but-fake (harvesting postings), ATS-invisible postings (direct/referral roles), postings frozen mid-search (position on hold). Caption: "The filter reduces waste; it doesn't read intent. The residual cases are where a human check earns its keep."] -->

## The rung you just added

At the end of this chapter, three facts exist about a role: the company can sponsor, the posting is live, and the signals behind both claims are logged and traceable. The pipeline has been built as a ladder of verified claims — each chapter adding one rung, each rung resting on data rather than plausibility.

The question the pipeline still cannot answer is whether the job is worth having. A real, sponsoring role at a company with an active posting is still a role in an occupation that might be contracting, at a salary band below market, in a geography you can't realistically reach. Sponsorship and liveness are necessary conditions. They are not sufficient ones.

That's where the next chapter begins. The role exists, and you can apply to it. Is it any good?

---

## Exercises

**Warm-up**

1. *(Recall, easy)* Name the three ATS platforms this chapter focuses on and explain why detecting the ATS is a prerequisite to reading the postings as data rather than prose. What does knowing the ATS unlock?
   *Tests whether you understand the detection step as necessary infrastructure, not just labeling.*

2. *(Recall, easy)* List the five liveness signals the pipeline checks. For each one, write one sentence describing what a "ghost" value looks like and one sentence describing what a "live" value looks like.
   *Tests whether you can articulate the signal space before applying it.*

3. *(Identify, easy)* What does "zero-token scan" mean, and why does it matter that the scan step costs no paid-model calls?
   *Tests the cost-structure reasoning behind the architecture choice.*

**Application**

4. *(Apply, moderate)* Run `detect-ats.py` on one of your target companies. Record: which ATS was detected, how you verified the result, and one thing the ATS label tells you about how to read that company's postings.
   *Tests the transition from knowing the command to interpreting its output.*

5. *(Analyze, moderate)* Take three postings from the same company — choose a company with multiple open roles. Classify each posting as live, ghost, or investigate. Write the specific signal values (posting age, update history, description specificity, portal activity, funding context) that drove each classification. Identify which classification you are least confident in and explain why.
   *Tests whether you can apply the multi-signal framework and acknowledge uncertainty.*

6. *(Analyze, moderate)* Find one posting that you would classify as "investigate" rather than committing to live or ghost. Describe the specific mixed signals that produced the ambiguity. Write the single cheapest check you could run to resolve it, and explain what response would push you toward live vs. ghost.
   *Tests the three-way decision rule and the reasoning behind the investigate category.*

**Synthesis**

7. *(Synthesize, harder)* A role passes the sponsorship check from Chapter 7 (Proven tier) and the liveness check from this chapter (classified live). A colleague argues that the two checks together are sufficient to justify a full application. Construct the strongest counter-argument: what third or fourth fact about the role would you want before committing a day of application effort, and what signal in the current pipeline — if any — approximates it?
   *Tests whether you understand the pipeline's layers as necessary-but-not-sufficient, not as a complete filter.*

8. *(Synthesize, harder)* The "ghost job as spam" analogy structures the liveness detection in this system. Spam filters have a well-known failure mode: sufficiently motivated senders learn the signals and game them. Describe one realistic way a recruiter running a ghost-posting campaign could specifically defeat the five liveness signals in this chapter — and then describe one additional signal not currently in the pipeline that would be harder to fake.
   *Tests adversarial reasoning about the detection model's limits.*

**Challenge**

9. *(Evaluate, open-ended)* The chapter states that the filter costs real opportunities: a stale-but-real posting at a slow organization gets classified ghost and filtered out. Design a research method — using only publicly available data and the tools already described — that would let you estimate the *false negative rate* of the liveness classifier for a specific industry or company size. What would you measure, over what time window, and what would the resulting estimate actually tell you about when to trust the filter and when to override it?
   *Tests whether you can reason about classifier quality as an empirical question, not just a design assumption.*
