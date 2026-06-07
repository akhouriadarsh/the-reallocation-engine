# Chapter 6 — Where the Money Went: SEC Form D

<!-- voice-anchored: root style/VOICE.md. Anatomy: TIKTOC Part 10.
     Sourced from scripts/sec/README.md, data/80-days-to-stay day logs, CHAPTER-RESEARCH-MAP,
     "80 Days to Stay" essay. Draft. Never published. -->

There is a peculiar asymmetry in the way most people search for jobs. They look where the light is good — the big job boards, the recognizable logos, the company names they have heard of. The light is good there because those companies spent money to put it there. But the companies that most need to hire you right now, the ones sitting on fresh capital and a mandate to grow, often have no light on them at all. They are fourteen people in a converted warehouse in Cambridge. They just raised twelve million dollars. They have never crossed your radar. And the reason they haven't is not that they're obscure — it's that you've been using the wrong map.

The Securities and Exchange Commission maintains a public record of every private fundraise above a certain threshold. When a company closes a seed round, a Series A, a bridge round — when it takes in outside capital through what's called a private offering — it is legally required to file a form disclosing that fact. The form is called Form D. It has been sitting in a publicly accessible database for years, structured and searchable, containing the company name, its address, its industry, the amount raised, and when. In one snapshot of that record, there were over **568,000** companies that had reported raising money, and nearly **247,000** of them had raised at least five million dollars.[^formd]

Almost no job seeker has ever looked at it.

This is not because the data is hard to find. It is because the idea of looking there has not occurred to most people. The job board has trained a generation of candidates to think that companies find workers, not that workers find companies. Form D inverts this. Instead of waiting for a company to post a job, you identify the companies that just received the resources to hire — before the posting exists, before the recruiter has been briefed, often before the hiring manager has even written the job description. You show up earlier in the process, which is almost always an advantage.

The logic is simple enough to state in a sentence: **a company that just raised money is a company under pressure to spend it on people.** Early-stage companies don't raise capital to sit on it. They raise it to execute — and execution, in a young company, means hiring. Funding recency is therefore a leading indicator. A company that filed Form D for a twenty-million-dollar round eight weeks ago will be hiring in the next two quarters with near-certainty. The question is not whether they'll hire. The question is whether you'll know they exist.

This chapter is about making sure you know.

---

The pipeline for turning raw Form D filings into a usable shortlist lives in `scripts/sec/`, and the data it works with lives in `data/sec/form-d/` across three layers: `raw/` holds exactly what the SEC published, `extracted/` holds the parsed output, and `processed/` holds the cleaned and deduplicated result. The three-layer structure matters not for aesthetic reasons but for epistemic ones. If you look at a processed number and wonder where it came from, you can trace it back through extracted and into raw. That traceability is part of a larger contract running through this book: every company, every amount, every date in a real run comes from a filing, not from a guess. The pipeline is the source of truth. The audit log it writes is the receipt.

Running it is a sequence of seven commands:

```bash
cd scripts/sec

# 1. Download the Form D filing archives for the quarters you want
python download-form-d-quarters.py

# 2. Pull in the most recent quarters (keeps the archive current)
python refresh-recent-sec-quarters.py

# 3. Combine quarters into one dataset
python sec-combine-quarters.py

# 4. Filter to real offerings above your funding threshold
python sec-filter.py

# 5. Collapse to one record per company
python sec-unique.py

# 6. Infer each company's web domain
python sec-domain-inference.py

# 7. Flatten to the final processed table
python sec-flatten.py
```

Each step writes its output into the appropriate layer of `data/sec/form-d/` and leaves an audit file alongside it. The final product is a flat table: one row per funded company, with amount, date, industry, location, and — where the inference engine succeeded — a web domain. That last column matters more than it might seem. A company name without a website is a dead end. The domain inference step tries to give you a way in.

The inference works by guessing and verifying URLs from company names. It gets the right answer about sixty-two percent of the time.[^domain] Which means roughly thirty-eight percent of funded companies still need a human to locate the website before anything further can happen. This is not a bug in the pipeline — it is a feature of the problem. Some work cannot be automated, and the pipeline is honest about where it stops and you begin.

---

The hard part of working with Form D is not running the pipeline. It is resisting a mistake that is easy to make once the ranked table is in front of you: sorting by dollar amount and concluding that bigger is better.

It is not.

A two-hundred-million-dollar late-stage round is not a hiring opportunity in the same sense as a six-million-dollar seed. The company that raised two hundred million is probably large enough to have a formal recruiting apparatus — a parser-gated application system, a hundred applicants for every role, a process designed to process. The company that raised six million at fourteen people is a founder who will read your email. The signal in Form D is not the size of the raise. The signal is the combination of recency and company size. A small company that just got funded is a company where you can make a difference and where the people deciding to hire you will know your name.

Recency degrades. The hiring surge that follows a funding announcement is real and it is time-limited. In the quarters immediately after a raise, a company is actively trying to build the team the investors paid for. Eighteen months later, the urgency has passed — either they hired or they didn't, and the fresh-capital energy has moved on to execution. When you filter the table, the recency cutoff matters: within twelve months is a signal; beyond eighteen months is history.

The geography filter matters for obvious reasons. A biotech seed round in San Diego is not a useful lead for someone who needs to work in Boston. But there is a subtler geographic point worth making. Early-stage companies cluster. Cambridge, MA has a density of biotech labs that no job board adequately surfaces. Filtering Form D to a metro area and a relevant industry will often reveal a population of companies that simply does not appear in a normal job search — not because the jobs aren't there, but because the companies haven't yet bought the advertising that makes them visible.

---

Consider a concrete case, the kind of thing that actually happens when you run this pipeline. A data-science graduate is targeting Boston, open to biotech and AI. The pipeline runs over the most recent quarters. Filtering to Massachusetts, raised at least five million, filed within twelve months, sorted by recency, produces a list. Near the top: a few names the graduate recognizes. Three rows down: a Cambridge biotech with a twelve-million-dollar raise eight weeks ago that has no job board presence, no careers page in search results, and no recruiter outreach in anyone's inbox. It exists in this search because it filed a form with the SEC. It would not exist in any other search the graduate might run.

That company goes on the target list above several brand names. Not because it's more prestigious. Because it just got the money, and at its size, a single hire — one good data scientist — changes what they can do. The job board optimizes for visibility. The Form D search optimizes for timing. Timing is almost always worth more.

The limit of this approach is equally concrete and equally worth stating plainly. Form D tells you a company raised money. It does not tell you what they will hire for, whether a given role fits your background, whether they have ever sponsored a visa, or whether the posting you eventually find reflects a real and open position. Funded is a necessary signal. It is not a sufficient one. It narrows the population of companies worth investigating — it does not close the investigation. The next several chapters add the facts that Form D cannot supply: whether the company has the machinery to sponsor visas, whether the specific roles they post match your profile, whether the geography works, and whether the humans at the company are actually responsive.

Think of Form D as triangulation. You are not picking your next employer from this table. You are identifying which companies are worth the effort of deeper research. The companies that make the list are the ones where the effort has a real chance of paying off — where the money is recent, the size is right, and the industry is relevant. Everything else is noise.

---

There is one more thing the pipeline cannot do that is worth being explicit about. Sixty-two percent domain inference sounds like a high number until you think about what the thirty-eight percent represents. Each company in that remainder is a funded firm you cannot easily reach without further work. Some of them are the most interesting leads — small, obscure, operating without a marketing department. The fact that the pipeline couldn't find their website is not evidence that they're not worth pursuing. It is evidence that finding them requires a human judgment that no script can substitute for.

This is not an accident of implementation. It is a structural property of the search problem. The companies that are hardest to find automatically are often the ones where showing up — actually tracking down the website, finding the right person, writing the email — yields the most asymmetric return. Everyone else gave up at the domain lookup step. You didn't.

The pipeline's job is to get you to the right population and sort it by the strongest signal available, which is recency. Your job is to take that shortlist and close the gap between a row in a table and a real conversation with a real person. Form D is where you find the companies worth having that conversation with.

## LLM Exercises

1. **(Apply) Refresh and produce.** Run the pipeline for the current quarters and generate the processed company table. Confirm the row count against the run's audit — the count should come from the audit, not your memory.
2. **(Analyze) Ten invisible firms.** Pull ten funded companies in your target city and note, for each, whether you would ever have found them on a job board. Mark the ones that exist only because you read the filings.
3. **(Apply) Fix a missing domain.** Find one high-fit company where domain inference failed, locate its real website by hand, and note how long it took — that is the human cost the sixty-two-percent number hides.

## Key terms

- **Form D:** the SEC filing a company makes when it raises money in a private offering; public, structured, and rich with hiring signal.
- **Funding recency:** how recently a company raised; a leading indicator of near-term hiring and a twenty-percent factor in the sponsorship tier.
- **Entity resolution:** collapsing the many spellings of one company into a single record.
- **Domain inference:** automatically guessing and verifying a company's website so a funded firm can actually be reached.

## Run-log prompt

Record the quarters processed, the audited row count, your filter thresholds (geography, funding floor, recency), and the count of high-fit firms whose domains you had to find by hand.

[^formd]: Aggregate Form D counts (≈568,707 filers; ≈246,572 raising ≥$5M) from the "80 Days to Stay" build logs (`data/80-days-to-stay/`) and connecting essay. **[verify]** against a current pipeline run.

[^domain]: ~62% domain-inference success (≈38% requiring manual lookup) from the "80 Days to Stay" build logs and the "80 Days to Stay: Connecting Recent Funding" essay. **[verify]**
