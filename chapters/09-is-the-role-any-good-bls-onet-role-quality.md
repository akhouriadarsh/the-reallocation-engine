# Chapter 9 — Is the Role Any Good: BLS / O\*NET Role Quality

<!-- voice-anchored: root style/VOICE.md. Anatomy: TIKTOC Part 10.
     Sourced from scripts/bls/README.md, projects/soc_classification_draft.md, CHAPTER-RESEARCH-MAP.
     Draft. Never published. -->

Two postings cross your screen on the same afternoon. Both say "Analyst." Same flattering word, same vague glamour. But one of them sits in an occupation where national employment has risen for four consecutive years and the wage band is strong and still widening; the other sits in an occupation that is quietly contracting, where median wages have stalled and headcount has fallen. The titles are identical. The futures are not. And the person reading only the title has no way to tell the difference.

This is the situation job titles were made for. Not yours — theirs. A title is a marketing artifact, written by whoever drafted the posting, calibrated to attract applicants rather than to describe the work. "Analyst" sounds important, versatile, valuable. Whether the underlying occupation is growing or shrinking, well-compensated or wage-stagnant, in demand or being automated away — none of that is in the title. The title was written to get you to apply, not to help you decide whether you should.

The U.S. labor statistics system does something the title doesn't. It classifies the actual occupation underneath the title — assigns it a code, measures it, tracks it over years. Once you can see the occupation, you can see the trajectory the title was hiding.

---

Every occupation in the American labor market has been assigned a Standard Occupational Classification code — a SOC code. It is a government taxonomy, stable and consistent across agencies. A "Data Analyst" at a startup and a "Data Analyst" at a bank might be doing very different things, but if both postings map to the same SOC, the same national employment count and wage distribution describes the occupation they are both part of. The SOC code is the hinge. Get it right, and everything useful follows from it.

Two federal data systems organize what follows from it:

**O\*NET** — the Occupational Information Network — describes what the occupation is. For each SOC code, it provides alternate titles (the many ways the same job gets marketed), job zones (how much preparation the occupation typically requires), and rated skill and ability levels. If you want to know whether the occupation your posting maps to is the same occupation you trained for, O\*NET's alternate-title list will tell you.

**BLS OEWS** — the Bureau of Labor Statistics' Occupational Employment and Wage Statistics — measures the occupation's footprint. National employment counts per year, wage distributions at the tenth, twenty-fifth, fiftieth, seventy-fifth, and ninetieth percentiles. If you want to know whether the field is growing and what it pays, OEWS supplies the numbers.

Both are organized by SOC code. The pipeline in `scripts/bls/` joins them into a compact table — one row per occupation — and that compact row is what turns a marketing title into a labor-market fact. Build the table once:

```bash
cd scripts/bls
python extract-soc-occupation-table.py     # builds the compact SOC/OEWS/O*NET table into data/bls/compact/
```

The output is a single flat table. Pull your target occupation's row. You get alternate titles confirming the match, job zone, skill and ability ratings, national employment over multiple OEWS survey years, and the full wage distribution. That is role quality — not a feeling about the posting, but a set of features measured by the people whose job it is to measure them.

---

The hardest part of this is the first step: correctly mapping the posting's title to the right SOC code. And this is worth slowing down on, because the whole chapter's value depends on getting it right. A wrong SOC match is silent. It doesn't error out. It just quietly attaches the wrong wages, the wrong employment trend, and the wrong skill profile to the role you're evaluating. You'll make a decision based on a different job than the one you're actually considering.

A language model is genuinely useful here, within limits. It has encountered thousands of job titles and their occupational descriptions, and it is good at proposing a plausible SOC match from a messy posting. But proposing is not confirming. The verification step is mandatory: take the model's proposed SOC, look at the alternate-title list in the compact row, and check whether your posting's title or description actually appears there. If it does, the match is confirmed. If it doesn't, you re-classify before you trust any number downstream. The model proposes; the data confirms; you judge. This is the same verified-data contract from Chapter 3, now applied to classification rather than company counts.[^soc]

Consider what it looks like when this goes wrong. A posting titled "Growth Analyst" gets mapped by the model to a SOC for market research analysts — reasonable enough on its face. The compact row for that SOC shows stable employment and a wage band that looks acceptable. But the alternate-title list doesn't contain anything close to "growth analyst" — the posting is actually describing a role closer to a data scientist, and that occupation's SOC has a completely different wage distribution and a steeper skill profile. If you skip the alternate-title check, you've just evaluated the wrong job. The title was ambiguous; the alternate-title list is not.

---

Once the SOC is confirmed, the compact row gives you three features that matter for the decision:

**Employment trend.** Has national headcount in this occupation been rising or falling across the OEWS survey years in the data? Flat is not the same as falling, and rising is not the same as booming, but the direction over multiple years is about as reliable a signal as you can get about whether the occupation is healthy. Declining employment, in an occupation you plan to spend years in, is a structural headwind worth knowing about before you accept an offer.

**Wage band.** The OEWS wage distribution tells you what people in this occupation actually earn, at each percentile. This is not what this company offers — it's what the occupation pays across thousands of employers. If the median is well above your threshold, the occupation rewards the work. If the median has been flat for several survey years while others have risen, something is compressing wages in this field — and that compression will be your problem eventually.

**Job zone.** O\*NET's job zones run from one to five, describing the typical preparation each occupation requires — from jobs that need little beyond a few days of training to occupations requiring extensive graduate preparation and years of experience. A job zone four or five occupation with a posting that claims to want recent graduates is either mismapped or unusual; knowing the zone helps you calibrate how competitive the real candidate pool is likely to be.

These three features, read together from one compact row, tell you more about a role's quality than any amount of reading the posting itself. The posting was written to make the role sound desirable. The compact row was built from surveys of everyone actually employed in the occupation.

---

The limit of this read is worth being explicit about. National OEWS estimates are national and lagging — typically one to two years behind the survey. They don't capture what this specific company pays, what the local market pays in your city, or what's happening in the last eighteen months of a fast-moving field. A company that just raised a Series A may be paying at the top of the wage band for talent; a company burning through runway may be offering equity and a below-median salary. The compact row tells you the occupation's gravity; it cannot tell you the specific role's orbit around it.

The SOC taxonomy also lags genuinely new work. If a role is at the frontier of a field that didn't exist five years ago — some combinations of machine learning engineering and product work, for instance — the best available SOC code may be an imperfect match for something genuinely novel. The numbers you read off it will be real, but they'll describe a proxy occupation rather than the thing itself. This is not a reason to skip the lookup. It is a reason to hold the numbers as directional rather than definitive when the alternate-title match is weak even after careful checking.

Role quality, read this way, is a strong directional signal. It is not a salary quote. The occupation that is rising, well-compensated, and skill-intensive at the right level for your background belongs on your list. The one with three years of declining employment and a stalled wage band, regardless of its title, deserves serious skepticism. You now have the tool to tell the difference. What you do not yet have is the clock — whether the hiring process at these companies can actually move fast enough to matter for your timeline.

## LLM Exercises

1. **(Apply) Build and look up.** Generate the compact table and pull the rows for two of your target roles. Record SOC code, employment trend, and wage band for each.
2. **(Evaluate) Rank three.** Take three real postings, map each to its SOC, and rank them by quality and direction, citing the specific features — not the titles — behind the ranking.
3. **(Analyze) Catch a misclassification.** Find one posting whose obvious title maps to a SOC that the alternate-title list says is wrong, and show the correct match.

## Key terms

- **SOC code:** the Standard Occupational Classification identifier for the real occupation underneath a job title; the hinge of the whole chapter.
- **O\*NET:** the occupational database of alternate titles, job zones, and ability/skill ratings — what is this work?
- **BLS OEWS:** national employment and wage estimates per occupation — how many exist and what do they pay?
- **Compact table:** the joined O\*NET + OEWS row per occupation produced by `extract-soc-occupation-table.py`.

## Run-log prompt

Record each target's confirmed SOC code, the employment trend and wage band you read, and any title you had to re-classify against the alternate-title list.

[^soc]: SOC classification (and its measurable misclassification rate) is the subject of `projects/soc_classification_draft.md` + `_methods.md` in this repository — a parallel research track. Its quantitative results contain `[TO DO]` placeholders and must not be cited as final numbers. **[verify]**
