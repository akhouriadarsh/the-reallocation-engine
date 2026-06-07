---
title: "The Reallocation Engine"
author: "Nik Bear Brown"
date: 2026
lang: en-US
rights: "Copyright © 2026 Nik Bear Brown. All rights reserved."
publisher: "Bear Brown, LLC"
...
# The Reallocation Engine

**Nik Bear Brown**

---

## Copyright

Copyright © 2026 Nik Bear Brown. All rights reserved.

Published by Bear Brown, LLC.

No part of this publication may be reproduced, distributed, or transmitted in any form or by any means without the prior written permission of the publisher, except in the case of brief quotations in critical reviews and certain other noncommercial uses permitted by copyright law.

ISBN: [INSERT ISBN]

First edition: 2026

---

## Dedication

*[For the readers doing the work before the tools can make sense of it.]*

---

## Preface

This book exists because the easy part of intellectual work has become easier, and the hard part has become easier to hide. A person can now generate a draft, a diagram, a summary, a lesson, a program, a business plan, or a research scaffold before they have fully understood what the work requires. That is useful. It is also dangerous. The danger is not that the machine writes. The danger is that the human stops noticing which parts of the work still require judgment.

The Reallocation Engine is written for readers who want more than tool fluency. It is for people who need a usable method: a way to decide what to delegate, what to inspect, what to refuse, and what to practice until it becomes part of their own competence. The present draft contains 2 body chapters.

Why now is straightforward. AI systems have moved from novelty to infrastructure. They sit inside writing, coding, design, research, teaching, analysis, operations, and decision support. The old advice — learn the tool, write better prompts, move faster — is not enough. Speed without judgment simply accelerates error.

I write this from the intersection of teaching, engineering, AI systems, and curriculum design.

This preface is a rough production draft. It should be tightened after the chapters stabilize, especially where a coauthor, editor, course team, or domain expert has supplied the lived knowledge that makes the book more than a generic AI text.
# Introduction

The first sign of trouble is usually not failure. It is fluency.

The draft looks clean. The answer sounds reasonable. The chart has labels. The code runs. The plan has phases. The explanation has the rhythm of expertise. Nothing in the surface announces that a human still has work to do.

This book is about the gap between a polished artifact and a trustworthy one.

The central argument of **The Reallocation Engine** is that readers need a working method for the part of the work that cannot be delegated: the judgment that decides whether an output is correct, useful, ethical, situated, and worth acting on.

## What This Book Is

This book is a practical map of a domain under AI pressure. It names the concepts, habits, distinctions, and workflows that let a reader use AI while preserving the human competence the work depends on.

## What This Book Is Not

This book is not a comprehensive technical manual for every AI system. It is not a replacement for disciplinary training. It is not a promise that AI will make hard work disappear. Avoidance is not a strategy. The strategy is disciplined use.

## The Recurring Concept

The recurring concept is the boundary between execution and judgment. Execution is the production of an artifact. Judgment is the disciplined decision about whether that artifact should exist, whether it is right, whether it fits the situation, what it leaves out, and what consequences follow from using it.

## How This Book Is Organized

- **Chapter 1: Introduction.** Introduction establishes one part of the book's working method and gives the reader language for using that method in practice.
- **Chapter 2: Chapter 1.** Chapter 1 establishes one part of the book's working method and gives the reader language for using that method in practice.

## How To Read This Book

Read the introduction first, then move through the chapters in order if you are new to the subject. If you are using the book as a reference, you can skip to the chapter closest to the problem in front of you, but do not skip the judgment frame.

## A Note About AI

This book is written for the AI era, but it is not an invitation to outsource understanding. AI can help draft, summarize, transform, compare, and generate alternatives. Those are execution tasks. The book's deeper concern is the work that remains after execution becomes cheap: deciding what question matters, what evidence counts, what tradeoffs are acceptable, what failure would look like, and who is responsible when the output leaves the screen.

These books are intended to integrate with **Medhavy** (also known as **Medhavi**), an AI-powered intelligent textbook system whose name comes from Sanskrit: मेधावी, meaning intelligent or intellectually brilliant. In that environment, chapters can become adaptive practice: hints, quizzes, worked examples, and feedback loops. But even there, the learning target remains human.

## Closing Return

Return to the polished artifact. Do not ask first whether it is impressive. Ask what would have to be true for it to be trusted. Ask what the machine could not know. Ask what you are now responsible for. Then begin.

## Tags

#the #reallocation #engine #AI #education #judgment #Medhavy #Medhavi #intelligent-textbook
# Chapter 1 — The Fluency Trap
*What the screen never asks you — and why fluency and correctness stopped being the same thing.*

It is a Tuesday in March, and you are twelve minutes into a take-home assignment for a job you need more than the people interviewing you will ever know. The prompt asks you to clean a dataset and justify your choices. You paste it into the model. Three seconds pass. The answer arrives — complete, formatted, confident. There is a function. There are comments. There is even a short paragraph explaining the reasoning, written in the calm cadence of someone who has done this a hundred times.

You read it. It looks right. It looks, in fact, exactly like what a competent analyst would produce. You run it. It runs. The chart has labels. The nulls are handled. Nothing on the screen is asking you for anything.

So you submit it.

Here is what you cannot see in that moment: whether the model dropped a category of rows that mattered, whether the imputation it chose quietly biased the result toward the answer the hiring manager wants, whether the "reasonable" choice it made is the one a domain expert would have flagged in a sentence. You cannot see it because seeing it is a separate skill from producing it — and producing it is the part you just handed away.

This is the trap. Not failure. Fluency. The first sign of trouble is almost never a crash or an error message or a blank screen. It is a clean output that looks like the work of an expert, produced by a system that has no idea whether it is right, handed to a person who has not yet built the judgment to check.

I want to take that apart, because almost everything that matters about working in the AI era — and almost everything that matters for you specifically, if you are an international student with a visa clock running — lives inside it.

## Two Words Doing Different Jobs

We need to separate two things that the word "work" has been quietly gluing together.

The first is **execution**: producing the artifact. Writing the function, drafting the email, building the slide, generating the SQL, cleaning the rows. Execution is the visible output — the thing that appears on the screen and can be graded, shipped, or submitted.

The second is **judgment**: the decision about whether that artifact should exist, whether it is right, whether it fits the situation in front of you, what it leaves out, and what follows from using it. Judgment is the part that does not appear on the screen. It is the analyst noticing that the "cleaned" dataset threw away every applicant who left one field blank — and that those applicants were disproportionately the ones the model was supposed to find.

For most of the history of work, these two arrived welded together. You could not produce the artifact without exercising at least some judgment along the way, because producing it was slow and manual and full of small decisions. The grind *was* the training. Every junior analyst who hand-cleaned a thousand datasets was, without being told, building the pattern-recognition that would later let them glance at a result and feel that something was off.

AI breaks the weld. It makes execution nearly free and nearly instant, and it leaves judgment exactly as expensive as it ever was. That is the whole event. Not "AI is smart" or "AI is dumb." AI is *fluent* — it produces the surface of competence at a speed and polish no human can match — and fluency and correctness are not the same thing.

Watch how this shows up in how work is actually graded. In courses that permit AI use — because in the real world everyone has the same tools — roughly three-quarters of a typical grade measures procedural competence: did you follow the constraints, meet the technical requirements, use the tools correctly, produce complete and coherent work on time? Everyone with a model can now do that. The remaining fifth or so measures judgment: did you understand the *actual* problem rather than the stated one, what did you decide under ambiguity, would this survive contact with a real stakeholder?[^grading] The first portion has collapsed in value because it has collapsed in scarcity. The second has not, because it cannot be generated.

So the question "can you do the work?" has split into two questions that now have wildly different answers. Can you produce the artifact? Yes — so can everyone, instantly. Can you tell whether the artifact is any good? That is the only question left with a scarce answer. And it is the one the screen never asks you.

<!-- → [CHART: two-bar column chart showing the value split — "Procedural competence" (~75-80%) vs "Judgment" (~20-25%) as share of grade/market value; a second panel shows the same split for "Who can supply it" — AI can supply the first bar almost entirely, humans exclusively supply the second; caption should read: "The question 'can you do the work?' has split. One half is now free. The other has not moved."] -->

## Why the Doing Was the Training

Now the mechanism — the part I had to think through several times before it sat still.

If judgment is so valuable, why not just skip the grind and learn judgment directly? Read the textbook, study the patterns, let the machine handle the grunt work, and arrive at the senior-level skill without the thousand tedious repetitions?

Because that is not how the skill forms. And we now have a clean experiment showing it.

In January 2026, Anthropic published a randomized controlled trial — the kind of study where you split people into two groups, change exactly one thing, and watch what happens.[^anthropic] They took fifty-two junior software engineers and had them learn a Python library called Trio that none of them knew. One group could use an AI assistant. The other had to write the code by hand. Same problem, same time, one difference: who did the executing.

Then — and this is the move that makes it an experiment about judgment rather than productivity — they gave everyone the same quiz afterward. Fourteen questions on reading, debugging, and understanding the library. A test not of *can you produce code* but of *do you understand what the code does*.

The hand-coding group averaged 67 percent. The AI-assisted group averaged 50 percent. Seventeen points — close to two letter grades — opened up between two sets of people who had just spent the same amount of time on the same problem.[^anthropic] The only thing that differed was whether a machine did the executing.

And here is the detail that turns a finding into a warning. Inside the AI group, behavior split the outcome cleanly. The engineers who used the model to *interrogate* — asking it conceptual questions, challenging its answers, forcing themselves to understand what it produced — scored 65 percent or higher. The engineers who used it to *delegate* — describe the problem, accept the output, move on — scored below 40.[^anthropic] Same tool. Same task. Opposite result. The variable was not the AI. It was whether the human kept doing the judgment work while the machine did the typing.

<!-- → [INFOGRAPHIC: three-column comparison — "Hand-coding" (67% comprehension quiz average), "AI + interrogation" (≥65%), "AI + delegation" (<40%); visual treatment should emphasize that the middle and left columns converge while the right column falls off sharply; caption: "The tool is identical in the middle and right columns. The variable is what the human does while it runs."] -->

That is the mechanism, and it has a name worth carrying: **comprehension debt**. When you let the machine execute and you skip the understanding, you do not avoid the cost of learning. You defer it. You take out a loan against a moment in the future when the system breaks in a way that requires you to understand it — and comprehension debt, like every debt, comes due at the worst possible time, with interest.

The senior engineer and the junior engineer can run the exact same prompt and get opposite trajectories from it. Give a model to someone who already has judgment, and it multiplies them — they read the output, hear the wrong note before the tests catch it, steer and correct. Researchers call that the **AI boost**. Give the same model to someone who has not yet built that judgment, and it produces plausible output they cannot evaluate, the work gets done, and the learning does not happen. That is **AI drag**.[^drag] The tool is identical. The difference is entirely in what the human brings to it — and what they keep doing while it runs.

Sit with the cruelty of that for a second, because it is the center of this book. The boost goes to people who already have judgment. The drag falls on the people still trying to build it. AI does not lift everyone equally. It widens the gap between those who can already tell good from plausible and those who cannot yet — and it does so precisely at the rung where that telling was supposed to be learned.

## The Rung That Got Removed

Step back from the one student at the desk and look at the whole structure.

The traditional path to judgment ran through unglamorous work. You joined as a junior, you did the boilerplate, the cleanup, the first drafts nobody senior wanted to write — and in doing it, over a couple of years, you built the eye. The grunt work was the apprenticeship. It was never efficient. It was how the judgment got made.

That rung is the exact rung AI executes best. Boilerplate code, first-draft memos, routine cleanup, standard analysis — the fluent, common, likely output is precisely what the machine produces at no cost. So the rational short-term move for a company is to stop hiring for it. Why pay a junior to do slowly and imperfectly what the model does instantly?

You can watch the contradiction this creates play out in public. In February 2026, IBM's chief human resources officer, Nickle LaMoreaux, stood up at a summit in New York and announced that IBM would *triple* its entry-level hiring in the United States — including software developers, the very roles "we're being told AI can do."[^ibm] Her argument was not sentimental. It was structural: a company that skips entry-level hiring to save money now will, in three to five years, have no one with the judgment to run the powerful tools it bought, and will have to poach mid-level people from competitors at a premium. The pipeline that produces senior judgment runs through junior work. Cut the bottom rung and you do not get cheaper seniors. You get no seniors.

IBM rewrote the junior role rather than deleting it — less routine coding, more AI oversight, error correction, customer contact, what they called "systems judgment."[^ibm] Read that closely. They did not eliminate the entry-level job. They redefined it as *the judgment part of the job, with the execution stripped out*. The boilerplate went to the machine. What is left for the human, even on day one, is the part the machine cannot do.

This is the inversion that has happened to skilled work across the board. A software engineer used to spend perhaps ninety percent of the day as the musician — fingers on keys, translating intent into syntax, debugging semicolons — and maybe ten percent on judgment, squeezed into the margins. That ratio has flipped. The execution is cheap; the work that is left, and the work that is paid for, is the judgment: what should this system do, does it introduce a risk, is it solving a problem worth solving.[^inversion]

And the market is pricing it exactly that way. As of 2025, AI had moved from a curiosity to a board-level liability: the share of S&P 500 companies naming AI as a *material risk* in their annual filings jumped from 12 percent in 2023 to 72 percent in 2025.[^spx] A material risk is not hype — it is a legal disclosure that this could hurt the company badly enough that shareholders must be warned. Seven hundred of America's largest firms, in the dry language of securities law, are telling their investors that getting the judgment wrong about these fluent machines is a danger to the enterprise. The thing they are afraid of is not that the AI cannot execute. It is that someone will trust a fluent output that was wrong.

<!-- → [CHART: line chart, 2023–2025, showing share of S&P 500 companies disclosing AI as material risk in 10-K filings — from 12% to 72% to 83% (Conference Board Dec 2025 update); annotate the 2023→2025 jump with a label reading "hype becomes liability"; caption: "Seven hundred of America's largest companies are telling investors in legal language: trusting the wrong fluent output is an enterprise risk."] -->

## Why This Lands Hardest on You

Now bring the two pictures together — the student at the desk and the structure around them — because at their intersection sits a specific person this book is written for.

If you are an international student in the United States on F-1 status, working under Optional Practical Training, you are standing exactly where the boost and the drag pull hardest in opposite directions, and you are doing it against a clock written into federal law.

Here is the clock. On post-completion OPT, you may accrue no more than ninety cumulative days of unemployment across your entire authorization period. Not business days — calendar days. Weekends count. Holidays count. The counter starts the day your work authorization begins and does not stop. Exceed it, and the Department of Homeland Security terminates your immigration record. There is no grace period. You must leave the country.[^opt] This is why the system at the heart of this book budgets to *eighty* days, not ninety — you want a margin between you and a cliff that does not forgive.

<!-- → [INFOGRAPHIC: timeline diagram showing the 90-day unemployment clock — a horizontal bar representing the OPT authorization period, with a red segment marking cumulative unemployment days, a dashed line at 80 days labeled "this book's working limit," and a hard stop at 90 labeled "DHS terminates record / no grace period"; annotate that weekends and holidays count; caption: "The clock does not distinguish between a Tuesday and a Sunday. It runs."] -->

Now lay the structure on top of that clock. The entry-level rung — the one that used to absorb new graduates and teach them judgment over a patient couple of years — is the rung being automated and, in most companies that are not IBM, quietly removed. The market is paying for judgment you have not yet been given the chance to build. And the most natural response to a ninety-day clock and a wall of rejections is to apply faster — to let the machine generate the cover letters, autofill the applications, produce the take-home in three fluent seconds and submit it. To delegate. To run up comprehension debt at the precise moment you can least afford to have it come due in an interview.

The fluency trap, for you, is not abstract. It is the difference between using these tools as a boost — interrogating, checking, building the judgment that makes you the rare candidate who can tell good from plausible — and using them as a drag, producing fluent applications that look like everyone else's fluent applications, learning nothing, and watching the days tick down.

This is the trade-off named plainly. AI optimizes for the fluent, the common, the likely. That is what it is *for*, and it is genuinely miraculous at it. What it cannot do is supply the salient, the situated, the correct-in-this-particular-case — the judgment about whether the likely answer is the right answer here, for this dataset, this employer, this person whose visa depends on it. Lean on the fluency and skip the judgment, and the tool works beautifully right up until the moment it matters, which is the one moment it cannot help you.

## What the Screen Never Asks

Return to the Tuesday afternoon, the take-home, the answer that arrived in three clean seconds.

Nothing on that screen was wrong, exactly. The code ran. The chart had labels. The reasoning read like competence. The trap was never that the output would look like failure. The trap is that it looks like success — and that the success is the machine's, produced in a register of fluency that asks nothing of you and quietly skips the one contribution only you can make.

So the discipline this entire book is built on starts with a single reflex, and you can begin practicing it this afternoon. When the fluent artifact appears, do not first ask whether it is impressive. Ask what would have to be true for it to be trusted. Ask what the machine could not know — about this dataset, this employer, this situation it has never seen. Ask what you are now responsible for when this leaves the screen and reaches a human who will act on it.

That reflex is judgment. It is the part that does not get cheaper. On a ninety-day clock, with the bottom rung disappearing and the boost flowing to whoever already has the eye, it is also the only thing that reliably separates you from the flood of fluent, identical, unexamined output arriving in every inbox you are trying to reach.

The machine will do the typing. The judgment is yours, and it always was. The rest of this book is about how to build it on purpose — fast enough to beat the clock.

---

**What Would Change My Mind.** If a replication of the Anthropic trial — or several — found that AI-assisted learners caught up to or surpassed hand-coders on delayed comprehension once they had used the tools for longer, the "comprehension debt" mechanism would need serious revision: it would mean the debt is repaid by familiarity rather than compounding. The current evidence is one well-designed but small (n = 52) study; one study is a finding, not a law.

**Still Puzzling.** I do not fully understand where the line sits between *interrogating* a model and *delegating* to it in real practice. The trial shows the two produce opposite outcomes, but a working analyst does both within the same hour, often within the same prompt. I do not yet know how to teach someone to feel which skill they are in while they are in it — and that, not the statistics, may be the hardest thing this book has to do.

---

## Exercises

**Warm-up**

1. *Tests the execution/judgment distinction.* A classmate says, "I used AI to clean the data and it worked fine — the model ran without errors." What question should you ask before accepting that verdict? Identify the specific gap between "no errors" and "correct." *(Difficulty: Low)*

2. *Tests comprehension debt as a concept.* In your own words, explain why letting a model execute a task you don't yet understand increases your risk over time rather than reducing it. Use the debt metaphor: what is being borrowed, and when does it come due? *(Difficulty: Low)*

3. *Tests the AI boost/drag distinction.* Two new analysts join the same team on the same day with the same tools. Six months later, one has developed strong judgment and one has not. What behavioral difference during their first month most likely explains the gap? *(Difficulty: Low)*

**Application**

4. *Tests interrogation vs. delegation in practice.* You ask a model to write a SQL query that returns the top ten customers by revenue last quarter. It returns a clean, well-formatted query in under three seconds. Write a list of five specific questions you should ask — either of the model or of yourself — before trusting that output in a stakeholder report. *(Difficulty: Medium)*

5. *Tests the value split between execution and judgment.* A job posting says: "We use AI tools extensively; comfort with AI-assisted coding is required." A classmate reads this as evidence that judgment skills matter less now that the tools do the coding. Construct the counter-argument, using the IBM example and the grading-split framing from this chapter. *(Difficulty: Medium)*

6. *Tests the OPT clock stakes.* You have been on post-completion OPT for four months. You have used thirty days of your unemployment allowance. You receive a take-home assignment and have the option to submit the AI-generated version quickly or spend two additional days working through it yourself. What factors — specific to your immigration status and to the comprehension-debt argument — should shape that decision? *(Difficulty: Medium)*

**Synthesis**

7. *Tests the rung-removal and judgment-pipeline arguments together.* IBM's decision to triple entry-level hiring in 2026 and redefine those roles around "systems judgment" appears to contradict the widespread claim that AI is eliminating entry-level jobs. Explain the logic that makes both statements simultaneously true, and identify what kind of company would make the error IBM is trying to avoid. *(Difficulty: High)*

8. *Tests fluency vs. correctness as a systemic risk.* The chapter cites S&P 500 companies disclosing AI as a material risk in their 10-K filings. Why would a fluent-but-wrong output be categorized as an enterprise-level financial risk rather than just a quality-control problem? What does "material risk" mean in securities law, and what does the jump from 12% to 72% reveal about where corporate liability is now being located? *(Difficulty: High)*

**Challenge**

9. *Open-ended; points toward Chapter 2.* The chapter identifies the interrogation/delegation split as the variable that determined outcomes in the Anthropic trial — but admits it doesn't yet know how to teach someone to feel which skill they're in while they're in it. Design a simple self-monitoring practice — something a student could do daily during a job search — that would help them notice, in real time, whether they are interrogating or delegating. What signal would they be listening for? *(Difficulty: Challenge)*

---

**Tags:** #fluency-trap #execution-vs-judgment #comprehension-debt #OPT-90-day-clock #AI-and-entry-level-work

[^grading]: Grading split (≈75–80% procedural / 20–25% judgment) drawn from "The Job Apocalypse (Not Yet): Thinking Has Become the Job" (uploaded essay, N. Bear Brown). **[verify]** — locate the primary syllabus/rubric data this figure summarizes before publication; currently sourced to the author's own essay, not an external study.

[^anthropic]: Anthropic, "How AI assistance impacts the formation of coding skills," randomized controlled trial published Jan 29 2026: 52 junior engineers learning the Trio Python library; AI-assisted group averaged 50% on a 14-question comprehension quiz vs 67% for hand-coders (~17 points). Within the AI group, conceptual-interrogation users scored ≥65% while code-delegators scored <40%. https://www.anthropic.com/research/AI-assistance-coding-skills (see also InfoQ summary, Feb 2026: https://www.infoq.com/news/2026/02/ai-coding-skill-formation/). Note: these are the study's reported figures; an earlier draft essay paraphrased the split as "24–39% vs 65–86%" — use the primary numbers above.

[^drag]: "AI boost" / "AI drag" framing attributed to Mark Russinovich and Scott Hanselman, via "The Ladder That Isn't There" (uploaded essay, N. Bear Brown). **[verify]** — trace to the original Russinovich/Hanselman source before publication.

[^ibm]: IBM to triple US entry-level hiring in 2026, announced by CHRO Nickle LaMoreaux at Charter's Leading with AI Summit, Feb 12 2026; roles recast toward AI oversight, error correction, customer contact, and "systems judgment." Fortune, Feb 13 2026: https://fortune.com/2026/02/13/tech-giant-ibm-tripling-gen-z-entry-level-hiring-according-to-chro-rewriting-jobs-ai-era/

[^inversion]: The "90% musician → 90% judgment" inversion is developed in "The Inversion: Why Software Engineers Are Becoming Judgment Workers" (uploaded essay, N. Bear Brown).

[^spx]: Share of S&P 500 companies disclosing AI as a material risk rose from 12% (2023) to 72% (10-K filings through Aug 15 2025), per The Conference Board / ESGAUGE. Fortune, Oct 8 2025: https://fortune.com/2025/10/08/sp-500-companies-disclosed-ai-risk-10-k-forms-reputation-risk/. A December 2025 update put the figure at 83%: https://www.conference-board.org/press/governing-AI-2026
# Chapter 2 — The Reallocation Principle
*Why the most disciplined job search strategy in the room is usually the most broken one.*

Here is a number I want you to hold: **54%**.

In 2025, roughly 54% of hires came through personal connections rather than through a cold application.[^connections] More than half. Sit with that for a moment, because the implication is structural, not motivational. The market is not rewarding effort distributed evenly across all channels. It is rewarding effort concentrated in specific ones. And the channel that produces more than half of all hires is not the channel that feels most like work.

I want to show you why that is, and why it is almost impossible to act on without first understanding the machinery behind it.

---

The applicant I have in mind is not a slacker. They are awake at eight, coffee cooling beside a browser with seventeen open tabs, and they apply. By noon the counter reads thirty. By end of day, forty-one. They do this five days a week. The spreadsheet is color-coded and meticulous. Five hundred applications in a month, almost all to companies you would recognize from a billboard.

This person has optimized hard — for the wrong variable.

Here is what the spreadsheet cannot show. By 2025, around 82% of companies were screening résumés with software, and roughly one in five rejected candidates automatically, with no human in the loop.[^screening] A large fraction of the postings were not even real openings — somewhere between a quarter and 42% of listings at any given moment are "ghost jobs," postings the company has no active intent to fill.[^ghost] Every hour spent clicking Submit was an hour not spent on the two activities that actually move the needle.

The question worth asking is: why does the volume strategy persist? Why does anyone — smart, hardworking, data-literate — continue doing something the numbers have quietly stopped rewarding?

The answer has to do with what feedback looks like in a broken system. Volume produces a counter. The counter goes up. The counter going up feels like progress. Networking and portfolio work produce nothing for days, then suddenly produce a conversation, which may eventually produce an offer. The feedback loop is delayed and nonlinear, which means our instincts misread it. We reach for the activity that generates immediate, legible signal — the number — and we call it discipline.

What we are actually doing is optimizing for throughput in a channel that has been quietly devalued by the very automation we learned to use.

<!-- → [CHART: bar chart comparing conversion rates across three channels — cold application (~0.2%), employee referral (~2–4%), direct network introduction (~5–10%) — student should see the order-of-magnitude gap between channels, not just the absolute numbers] -->

---

The asymmetry in conversion rates is the crux of this. A referred candidate is several times more likely to convert than an inbound one — cold applications convert at something like 0.2%, while a warm referral can convert at rates an order of magnitude higher.[^referral] When you combine that with the 54% figure, the arithmetic of the typical job search becomes almost painful to look at.

If you have eight hours, and you spend all eight applying cold, you are concentrating all of your effort in the channel that produces less than half of hires at the lowest conversion rate in the system. You are not unlucky. You are mathematically misallocated.

This is not a motivational observation. It is a resource-allocation problem. And resource-allocation problems have a structural solution: stop distributing effort by habit and start distributing it by expected return.

The expected return on an hour is not constant across activities. An hour of targeted networking reaches into the 54% channel. An hour building a portfolio piece creates verifiable evidence of capability — and in 2025, workers with validated AI skills were commanding something like a 56% wage premium over peers who only claimed equivalent skills.[^premium] An hour of cold applying, by contrast, feeds a machine that discounts most of what you send it before a human reads a word.

Once you see the return structure, the reallocation is obvious. Two hours applying — targeted, filtered, not sprayed. Three hours networking. Three hours on portfolio. I call this the 3-3-2 day, and the rest of this book is built to make it actually achievable rather than just strategically correct.

<!-- → [INFOGRAPHIC: three-column layout showing the 3-3-2 split — "2 hrs: Targeted Applying," "3 hrs: Networking," "3 hrs: Portfolio" — with the 54% and 56% figures anchored to the networking and portfolio columns respectively] -->

---

Let me be precise about what 3-3-2 is doing, because there is a version of this argument that sounds like "apply less," and that is not it.

The two hours of applying are not a ceiling on ambition. They are a forcing function for quality. If you can only apply to roles for two hours, you apply to fewer roles. That means you must filter more aggressively before you apply. And that filtering — knowing which roles are real, which companies have any history of sponsoring the visa type you need, which postings match what you can actually demonstrate — is where most of the signal lives anyway.

The machine I am building across the next several chapters is designed to compress that filter into something fast. The goal is not fewer applications as an end in itself. The goal is: make two hours of targeted applying produce more movement than eight hours of spray-and-pray did — and then use the reclaimed six hours on the channels the data says to use.

This is the reallocation principle in one sentence: **spend effort where the return is, not where the feedback is.**

---

There is a worked example worth walking through, because the principle is easy to endorse and hard to execute.

A master's graduate on OPT, three months into a search, switches strategies mid-stream. Week one of the old approach: forty hours, roughly two hundred applications to brand-name firms. Four auto-acknowledgements, one recruiter screen, zero onsites. Several of those companies, it turns out, had near-zero history of sponsoring the visa type needed — so even the "successful" applications were dead on arrival.

Week one of 3-3-2: ten hours applying — about twenty-five targeted applications, each to a company pre-checked for sponsorship history and a live posting. Fifteen hours networking — twelve outreach messages, four informational conversations, two of which produced referrals into the 54% channel. Ten hours portfolio — one deployed project with real metrics, written up.

Fewer applications. More movement.

The mechanism is not magic. The referrals work because they bypass the parser. The portfolio piece works because it converts a claim into evidence. The targeted applications work because they are aimed at companies that can actually act on them.

<!-- → [TABLE: side-by-side comparison of spray-and-pray week vs. 3-3-2 week — rows: hours spent, applications sent, recruiter screens, referrals generated, portfolio pieces completed, estimated pipeline value; student should see the input-output ratio flip] -->

---

Now I want to tell you something the 3-3-2 day cannot know.

A scorer — any algorithm — can tell you a role appears low-value and should be skipped. It cannot know that the hiring manager is your former professor's co-founder. It cannot know that the company whose posting scores mediocre is the one organization whose mission you can speak about with genuine conviction in a room, which is worth something the number ignores. It cannot know that you are three weeks from a visa deadline, which changes the entire calculus of which channel can close fast enough to matter.

The reallocation principle is a default for where returns *usually* lie. The person operating it is the one who holds private information the model cannot access. Override the default when you have a reason. Follow it when you don't.

This matters because there is a failure mode on both ends. The applicant who ignores the principle and keeps spraying is the one we started with — disciplined, misallocated, watching the counter go up. But the applicant who treats 3-3-2 as a ritual and never deviates is making a different mistake: substituting a heuristic for judgment. The whole argument of this book is that judgment is what you bring, and the tools are what handle the parts that do not require it.

<!-- → [DIAGRAM: decision tree for "where does a freed hour go?" — branch: fewer than ~10 live conversations → send to networking; portfolio has no deployed metric-bearing project from last 90 days → send to portfolio; both healthy → additional targeted applications; student should see this as a rule, not a preference] -->

---

There is one more piece of the reallocation puzzle that does not show up in time budgets: the skip.

A skip is a deliberate decision not to apply to a role you would otherwise have applied to. I am going to argue throughout this book that the skip is a first-class action — not a failure, not laziness, but a resource-allocation decision with the same weight as apply.

The freed time from a skip does not go back into applying to a different marginal role. The whole point of the filter is to catch marginal roles before they consume your two applying hours. When the filter fires and you do not apply, the freed time goes to networking if you have fewer than about ten live conversations going, and to portfolio if you have not deployed a metric-bearing project in the last ninety days. Only after both of those are healthy does a freed hour go back into more targeted applications.

The rule exists to stop the volume instinct from quietly reclaiming the time the filter just saved. Because it will try. The counter is seductive. "I have a free half-hour, I could just send one more application" is the volume instinct speaking in its most reasonable voice.

The answer is: no, you couldn't. That half-hour is already spent. You just haven't decided where yet.

---

By the end of this chapter, you should be able to explain — not just agree with — why volume is the wrong optimization target in the current market. You should be able to map the return structure across the three channels and defend a personal time allocation against expected return. And you should be able to write a 3-3-2 plan that names the times, names the networking actions, and names the portfolio piece in progress.

What you do not yet have is a filter trustworthy enough to actually skip on. That is the next problem. A reallocation strategy built on a filter you can't trust is just a different way of guessing. The question the next chapter forces is: what would make a claim about a role's value reliable enough to act on?

[^screening]: AI résumé-screening and auto-rejection rates (~82% screen with AI; ~21% auto-reject) from "The Collapse of the Traditional Résumé" (uploaded essay, N. Bear Brown). **[verify]** — trace to primary survey before publication.

[^ghost]: Ghost-job rate (≈28–42% depending on source/month) from "What Is a Ghost Job?" and "Can AI Help Detect Ghost Jobs?" (uploaded essays, N. Bear Brown), citing standstill rates held ~28–38% over five years. **[verify]** — trace to the underlying labor-market reports.

[^connections]: ~54% of 2025 hires via personal connections — "The 3-3-2 Split" (uploaded essay, N. Bear Brown). **[verify]**

[^referral]: Referral vs. cold-application conversion (referrals several-fold higher; cold ≈0.2%) — "The 3-3-2 Split." **[verify]** — the "4–10× more likely" figure appears in the plain-summary and must be source-cited.

[^premium]: ~56% wage premium for validated AI skills (2025) — "The Collapse of the Traditional Résumé." **[verify]**

---

## Exercises

**Warm-up**

1. *(Recall — tests the return-structure argument)* In your own words, explain why cold applications convert at a lower rate than referrals — not just that they do, but what structural feature of the hiring process produces that gap. One paragraph.

2. *(Recall — tests the 3-3-2 allocation)* A colleague tells you they have been applying for three months without an offer and asks whether they should "apply harder." What is the first question you ask them, and what data point from this chapter supports why you ask it?

3. *(Recall — tests the skip concept)* Define a "skip" as used in this chapter. Why is calling it a failure the wrong frame?

**Application**

4. *(Apply — tests personal allocation)* Draft your 3-3-2 plan for one workday. Name the exact two-hour applying window, your three networking actions, and the portfolio piece you are building this week. A plan without specific hours on it is a wish, not a plan.

5. *(Apply — tests the decision rule)* You have just decided not to apply to a role that scored poorly on the filter. Where does the freed hour go? Walk through the decision rule step by step, applied to your actual current situation.

6. *(Apply — tests gap diagnosis)* Tally last week's hours across apply / network / portfolio. Identify which channel is starved. Name one concrete action that moves you toward 3-3-2 this week.

**Synthesis**

7. *(Synthesis — tests override judgment)* Describe a specific scenario in which you would rationally override the 3-3-2 default and tilt heavily toward the applying channel. What information would you need to hold, and what would make that override correct rather than just an expression of the volume instinct?

8. *(Synthesis — tests the full argument)* A recruiter tells you that the applicants who get the most responses are the ones who apply most consistently every day. Steelman their claim, then explain where it breaks down given the data in this chapter.

**Challenge**

9. *(Challenge — tests structural limits)* The 3-3-2 day assumes you have a network to activate. Design a modified allocation for the first two weeks of a search when your relevant professional network is genuinely near-zero. What changes, what stays the same, and how do you know when to switch to the standard 3-3-2?
# Chapter 3 — The Verified-Data Contract
*The one rule that separates a filter you can trust from a guess wearing the costume of one.*

There is a particular kind of wrong answer that is worse than no answer at all, and it is this: an answer that sounds right. Not obviously wrong. Not hedged or uncertain. Fluent, confident, plausible — and untrue.

I want to be precise about what I mean, because the distinction matters more here than almost anywhere else I can think of. A language model asked whether a particular Cambridge biotech sponsors work visas will not say "I don't know." It will say something like: "as a mid-size biotech competing for specialized talent, this company likely sponsors visas for research-focused roles." Every word of that sentence is defensible. The reasoning is plausible. The conclusion is probably true for a lot of companies in that description. And it is not a finding. It is the most coherent-sounding sentence the model could assemble from patterns in its training data — which is a completely different operation from looking at a record.

The Department of Labor publishes every Labor Condition Application a U.S. employer files before hiring a foreign worker. The USCIS publishes H-1B approval and denial counts by employer. If you run a script against those records and ask the same question, you get a different kind of answer: this company filed fifteen LCAs in three years and had an 85% H-1B approval rate. Or you get zero filings, ever. The number is not the most plausible thing you could say — it is what actually happened, as far as the public record goes.

The whole architecture of this book is built on that distinction. One answer is fluent. The other is *true*. The discipline required to build on the second, and only the second, is what I mean by the verified-data contract.

<!-- → [INFOGRAPHIC: Two-column side-by-side: left column labeled "Model's answer" shows the fluent prose sentence with no source; right column labeled "Verified answer" shows the LCA count, approval rate, and year, traced to DOL and USCIS records. Caption: "Same question. One answer is plausible. One is checkable."] -->

## Why the contract is a single rule, not a set of guidelines

I've seen job-search systems — and empirical systems of all kinds — that try to manage the fluency problem with caveats: add a disclaimer, note that the model might be wrong, invite the user to verify. This doesn't work, and it doesn't work for a specific reason. A caveat lives outside the output. It is a warning label on a product, not a change to what the product contains. If the number inside the output was produced by a language model filling in a plausible-sounding value, the caveat is decoration on a fabrication.

The contract is different because it is a *prior constraint on what gets to enter the system at all*, not an advisory attached to what came out. The rule is stated once, in the shared configuration that every skill in this system reads before doing anything else: **Run the script and read the audit before you prompt. Never invent a count, a rate, or a coverage number.**

That is it. One rule. The simplicity is intentional. Complex rules are negotiated; a one-rule contract is harder to quietly break. The model's role in this system is to help you *read* data — to frame a finding, identify what's interesting about a number, suggest what to look at next. It is not permitted to be the source of a number. Sources of truth in this system are specific things: script outputs, audit reports, logged runs. Not the model's best guess at what the number probably is.

## What the system actually measures, and where it lives

The verified-data contract is not a philosophy statement. It is enforced by the architecture. There are three subsystems that produce the numbers this book is built on, and each of them writes to auditable records you can read and question.

<!-- → [DIAGRAM: Three boxes labeled scripts/sec/ (funding), scripts/ats/ (postings and liveness), scripts/bls/ (role quality), each with an arrow pointing to a corresponding *-audit.md output, all feeding into RUN_LOG.md. Caption: "The three pipelines and where their output lives — every number traces back through this graph."] -->

`scripts/sec/` pulls from SEC filings to measure company funding. When a company raises a round or files material financials, that event is in the public record. The script finds it; the audit reports what was found and what was dropped. `scripts/ats/` queries job-board data to measure whether a company is actively posting and whether particular openings are live. `scripts/bls/` draws on Bureau of Labor Statistics data to assess role quality — compensation, demand trajectory, geographic concentration. Each subsystem writes an audit: a record of what the pipeline did on a given run, how many rows it processed, what coverage it achieved, what it couldn't match.

`DATA_CONTRACT.md` defines what data exists and where it lives — including which files are private (your own application records, credentials, anything that identifies you personally) and how those are handled. `RUN_LOG.md` is the system's memory: every run leaves a trace, so a decision you make today on the strength of a number can be reconstructed and questioned tomorrow. This is the same practice good empirical work has always demanded — state your method, show your coverage, let a claim be checked.

## The tool prefers what it already trusts

There is a mechanism underneath the contract I haven't named yet, and it is the part people miss when they picture a verification tool. They imagine it reaching out to the network every time — hitting the Department of Labor server, re-downloading the disclosure file, re-counting from scratch. That is not what happens, and the difference is the whole reason the contract is cheap to keep.

Each of these tools checks for **local verified data first**. Once the DOL disclosure data has been downloaded and checked, it lives in a local store. When a script runs, it asks a prior question before it asks the network anything: *do I already have verified data for this, and is it still fresh?* If the answer is yes, the script reads the local copy and never touches the network. The audit says so plainly — *served from cache* — so you can see that this run rested on data already verified, not on a fresh pull nobody checked.

Only when the local answer is no — the data is missing, or older than the freshness window the contract defines — does the tool go and fetch. And fetching is not the same as trusting. The moment new data arrives it is **verified on arrival**: the schema is what was expected, the row counts are sane, the source is the one it claims to be. Only then is it written to the local store, and only then does a line go into the run log recording that a fetch happened and what it pulled. The network is the fallback, not the default.

This is not mainly an optimization for speed, though it is faster. It is what makes a run **reproducible**. A number you cited last Tuesday can be regenerated today from the same local verified data, because the tool did not silently re-pull a changed file underneath you. When the data genuinely changes — a new quarter of filings drops — the fetch is logged, visible, and dated, so the change is a recorded event instead of a mystery. Verified-once-then-cached is how "never invent a number" stays affordable: you are not re-earning trust on every run, you are reusing trust you already audited.

## The smallest honest thing you can do right now

Before you understand every component, before the sponsorship pipeline and the ATS scraper and the funding detector are fully built, there is one thing you can do that establishes the contract in practice rather than just in principle. Run a verification:

```bash
npm run ats:verify
```

This calls `scripts/ats/verify-pipeline.mjs`, which checks the tracker and scan data for internal consistency and prints what it found. The output is the audit. I want you to run this not because you need the result yet, but because there is a specific feeling I want you to have: the difference between being told the data is fine and *seeing the check pass*. One of those is someone's word. The other is evidence. The contract is the decision to require the second.

<!-- → [TABLE: Three columns — Pipeline, What it verifies, What the audit reports. Rows: ats:verify / tracker-scan consistency / row counts, coverage, drop reasons; sec:verify / filing-record completeness / companies matched, date range, gaps; bls:verify / role-quality data freshness / series IDs, last update, missing occupations. Caption: "The three verification commands and what each audit tells you."] -->

## The seam where fluency sneaks back in

Here is the error I want to warn you about specifically, because it is not obvious and it catches almost everyone, including me when I'm moving fast. You run the script. The script returns a real number — fifteen filings, 85% approval rate, sourced to DOL records. Now you hand that number to a language model and ask it to interpret the finding. The model says: "fifteen filings over three years is strong for a company of this size in this sector."

Did the model count anything? No. It estimated. It applied a pattern from its training data about what "strong" looks like for biotechs of similar size — a pattern it cannot actually show you, because it does not know what the pattern is, only that the output sounds reasonable. The moment an unsourced judgment re-enters through interpretation, the contract has been quietly broken. You ran the script, which was right. You then let the model paper over a gap in the reading, which was wrong.

The discipline required is to watch the seam between the data and the reading of the data. Data claim: fifteen filings, 85% approval rate, sourced to DOL/USCIS. Model judgment: this is strong for a company of this type. Both are present in that paragraph. Only the first can be defended against scrutiny. The second is permitted — it is genuinely useful — but it has to be *labeled as judgment*, not dressed as a fact derived from counting.

For any sentence in a system output, one question settles it: could this sentence have been produced by counting records? If yes, it must trace to a script output or an audit report. If it cannot be traced, it is not allowed to stand. If no — if it is a reading, a framing, a suggestion — it is model judgment, and it is allowed, but it must be visible as such.

<!-- → [INFOGRAPHIC: Decision tree — "Could this sentence have been produced by counting records?" Yes branch leads to "Data claim: must trace to script output or audit." No branch leads to "Model judgment: allowed, but must be labeled." Both branches end at "Is the label visible in the output?" Caption: "The one-question test for every sentence in a mixed output."] -->

## What the data can't tell you

The contract guarantees that counts and rates are real. It does not guarantee that the right things were measured. This is a distinction the contract cannot collapse for you, and I want to be honest about where it leaves you.

The data knows a company filed fifteen LCAs. It does not know that all fifteen were for one senior scientist role that was filled and will not open again. It knows an approval rate; it does not know that the company was acquired last month and the sponsorship policy changed last week. A name-matching failure — "Google LLC," "Google Inc," "Alphabet" — can make a prolific sponsor look like a non-filer. A company can sponsor and stay below the detection threshold if they filed in a window your data doesn't cover.

The contract stops you from building on fiction. It does not give you omniscience. What it gives you is a floor: you know the numbers you have are real, and you know where the gaps are, because the audit reported them instead of hiding them. A 94%-accurate system can still harm someone systematically if no one asks what it failed to measure. The contract makes you the person who asks that question — not the model, not the system, you. The gaps it reports are your honest starting debt: claims you currently cannot source, labeled as such, waiting for better data.

<!-- → [TABLE: Two columns — What the contract guarantees / What the contract cannot guarantee. Rows include: counts and rates are real / that the right things were measured; gaps are labeled not hidden / that coverage is complete; decisions trace to auditable records / that the records captured the full picture; model judgments are labeled / that those judgments are correct. Caption: "The floor the contract provides and the ceiling it doesn't claim to reach."] -->

## The shape of everything that follows

Before any of those tools, two chapters finish the method this one began. Chapter 4 shows that every tool here is a *skill* with two customers — the AI that runs it and the human who maintains it — and that you therefore write each one twice. Chapter 5 takes the floor this chapter laid down (the numbers are real) and asks the harder question the contract cannot answer on its own: are they the *right* numbers, measured the right way?

Then the building starts. Every chapter from there forward builds one of the three sources of truth or shows you how to read what they produce. Chapter 6 builds the funding detector — SEC filings, round size, recency, the money that forces companies to hire. Chapter 7 builds the sponsorship pipeline. Chapter 8 builds the posting liveness check. Each of them opens by reading the shared contract, each of them writes to an audit, each of them contributes a line to the run log.

The prime directive is already set: run the script and read the audit before you prompt. Never invent a count, a rate, or a coverage number. From here, the work is building the scripts worth running.

The one question I haven't fully answered yet: of all the companies in the world, which ones just got the money that forces them to hire? That's where we go next — and the answer, it turns out, is sitting in a federal filing database, waiting to be counted.

---

## Exercises

**Warm-up**

1. *(Recall, easy)* State the prime directive in your own words — not the exact phrasing, but the principle it enforces. What two-step sequence does it require before any model prompt, and what does each step accomplish?
   *Tests whether you can articulate the contract without reciting it verbatim.*

2. *(Identify, easy)* Name the three script subsystems in this chapter and the source of truth each one draws from. What does each pipeline write as its output?
   *Tests whether you've mapped the architecture to its actual data sources.*

3. *(Recall, easy)* What is `RUN_LOG.md` for, and why does the system require it rather than just trusting that you remember what you ran?
   *Tests the reasoning behind the audit trail, not just its existence.*

**Application**

4. *(Apply, moderate)* Run `npm run ats:verify`. Read the output. Write a `RUN_LOG.md` entry covering: what you ran, what the audit reported, and one thing the output told you that you would otherwise have assumed without evidence.
   *Tests the transition from knowing the contract to executing it.*

5. *(Analyze, moderate)* Take this sentence: "This well-funded Series B startup probably sponsors visas and would be a strong culture fit for someone with your background." Break it into its data claims and its model judgments. Label each. For each data claim, name the source it would need to trace to. For each model judgment, note whether it is labeled as judgment in the original sentence.
   *Tests the data-claim vs. model-judgment distinction on a realistic example.*

6. *(Apply, moderate)* Name one company you believe sponsors H-1B visas that might not appear in the public LCA/USCIS data — and explain why (recent acquisition, name-matching failure, filing timing, role type). Write one sentence describing how you would label that gap in an output rather than guessing past it.
   *Tests coverage-gap reasoning: what to do when the contract can't give you the answer.*

**Synthesis**

7. *(Synthesize, harder)* A colleague proposes adding a fourth data source to the system: LinkedIn profile counts per company as a proxy for growth. Walk through the contract requirements this would need to satisfy before the system could treat those counts as verified data rather than model-estimated data. What would the script, the audit, and the run-log entry each need to contain?
   *Tests whether you can apply the contract's architecture to a novel source.*

8. *(Synthesize, harder)* Consider the seam problem described in the chapter — verified numbers re-entering interpretation as unsourced estimates. Design a simple output-formatting convention (a label, a section header, a field name — your choice) that would make the data-claim / model-judgment boundary visible to someone reading a system output who hasn't read this chapter. Justify your design choice.
   *Tests whether you can operationalize the distinction, not just state it.*

**Challenge**

9. *(Evaluate, open-ended)* The chapter states that a 94%-accurate system can still harm someone systematically if no one asks what it failed to measure. Construct one realistic failure scenario in the job-search context — a specific type of company, candidate, or role — where the verified-data contract would pass all three of its checks (real counts, labeled gaps, audited runs) and still produce a systematically misleading result. What would a fifth check look like that catches this failure?
   *Tests whether you can find the limits of the contract itself, not just apply it correctly.*
# Chapter 4 — Two Customers: Writing a Skill for the AI and the Human

*A document that tries to serve everyone serves no one — the problem is older than software, and skills are not exempt from it.*

There is a small confusion built into the word "skill" that I want to name before it causes trouble. A skill lives in a markdown file. Markdown is text you read. So naturally, when someone writes a skill, they write it for a reader — they explain what it does, they describe its purpose, they use complete sentences and transitions. The file is readable and pleasant and almost entirely useless to the agent that has to execute it tonight.

I want to be precise about what I mean by "tonight." The F-1 clock is running. You have somewhere between sixty and ninety days to line up a job offer with a company willing to sponsor, file the paperwork, and get it processed. Every skill in this engine either runs on verified data or it doesn't. And whether it runs on verified data is decided not by what you intended when you wrote it, but by what happens when an agent reads it at eleven PM and starts executing. The document that should have said "call `npm run ats:scan` first, before anything else" instead said "the skill is designed to use the scan results" — and the agent, unable to locate the output it needed, quietly substituted something plausible. The skill ran. Nothing in the output announced the substitution. The data was invented.

That failure has a cause, and the cause is a design error. The skill was written for one customer and executed by another.

## The two customers

Every skill has two customers with completely different needs.

The first customer is the AI executing it. It needs the skill to be **terse and imperative**. It needs to know, in the fewest words possible, what to read first, what commands to run in what order, what output files to inspect, what to log, and under what conditions to stop. It does not need context or rationale. Rationale is processing budget that could be spent on execution. The AI doesn't care that the scan skill exists to enforce the verified-data contract — it cares that the first line says "Read `skills/_shared.md`" and the second line names the next file. The executable recipe is optimized for an agent to follow exactly, tonight.

The second customer is the human maintaining it. This is future-you, reading in March, who has forgotten what the skill does, has no memory of why certain design choices were made, and needs to understand the skill well enough to fix it when it breaks or extend it when your search changes. The maintainer needs to know what the skill does, what it depends on, how to run it, what it produces when it works, and what goes wrong when it doesn't. The maintainer does not need an imperative step-list dressed as prose — that is confusing to read and easy to skip. The human artifact is a card: purpose, dependencies, commands, outputs, failure modes. Optimized for comprehension rather than execution.

The problem is that these two needs are in tension. The imperative recipe is stripped of explanation so the agent doesn't get distracted. The human card is heavy on explanation so the maintainer understands the reasoning. A document that tries to do both splits the difference: too much prose to be clean for the agent, too imperative to make sense to a reader who has forgotten the context. A skill written to serve both customers simultaneously serves neither.

So you write it twice.

<!-- → [DIAGRAM: Two boxes side by side, labeled "AI Artifact (recipe)" and "Human Artifact (card)". AI box lists: terse, imperative, read-first order, commands verbatim, stop conditions. Human box lists: purpose statement, dependencies, how-to-run, what-it-produces, failure modes. Both boxes share a footer labeled "Verified-Data Contract (_shared.md)" with arrows pointing into both. Caption: "Same skill, two documents. The contract is the one thing both artifacts must honor."] -->

## What each artifact contains

The AI artifact — the recipe an agent follows — has a predictable structure. It opens with what to read first, before anything else. This is not optional and it is not decorative: loading `skills/_shared.md` first is what makes the runtime honest by construction. The shared contract states the prime directive, identifies the sources of truth, and defines the rules for when a number is verified and when it must be labeled as judgment. An agent that loads the shared contract before running the first command operates inside a defined constraint. An agent that skips it operates from its own priors.

After the read-first order, the recipe lists the commands — actual, verbatim, runnable commands, not descriptions of what commands could be run. Then it names what to inspect in the output and what counts as evidence of a successful run: not "the output looks reasonable" but "row count is nonzero, provider hits are listed by platform, no errors in stderr." Then it states the stop conditions: what halt execution. Then it names the log entry to write. That's the recipe. It should be readable at a glance without decoding.

The human artifact is structured differently. It opens with a purpose statement that tells the maintainer what the skill is *for* in one or two sentences. Then it lists dependencies: which files the skill reads, which scripts it calls, which other skills it assumes have run first. Then it gives the commands — the same commands as the recipe, but here they're annotated: what each one does, what the output is, what to notice in the result. Then it describes what the skill produces when everything works: which files are written, what an audit looks like, what a log entry should contain. Finally, and most importantly, it lists failure modes: specific, named ways the skill can break. Not "something might go wrong" but "if `data/ats/portals.yml` doesn't exist, the scan will silently use the example config and produce output against the example companies, not your companies."

That last section is the one that gets skipped when someone writes a skill fast. And it is the one you need most at eleven PM on a Thursday when the output looks wrong and you don't know why.

<!-- → [TABLE: Three columns — Section, AI artifact, Human artifact. Rows: Opening / read-first list / purpose statement; Core content / imperative commands with no commentary / annotated commands with output descriptions; Evidence / stop conditions and output checks / what success looks like in full; Logging / log entry template / what the log should contain and why; Failure / not present / named failure modes with specific causes. Caption: "The structural difference between the two artifacts — the same commands appear in both, but their context is inverted."] -->

## Drift is a failure mode, not just inconvenience

There is a failure mode I have not named yet, and it is more damaging than either the missing rationale or the over-explained recipe. It is drift: the recipe changes, and the human doc doesn't.

Drift happens because updates feel minor. You change one command — you add a flag, rename an output file, change the order of two steps because the second one now depends on output from the first. You update the recipe because the recipe is what the agent runs, and the agent fails if the recipe is wrong. The human doc also needs updating, but you're in a hurry, and it's just documentation, and you'll do it later. Later doesn't come, because it never does when you're racing a clock.

Six weeks later, you read the human doc to understand why the scan skill works the way it does. The human doc describes a workflow that no longer exists. It names a file the recipe no longer produces. It lists a command that now fails without a flag the recipe added. You can no longer trust the documentation, which means you now have to reverse-engineer the recipe to understand your own skill, which costs more time than writing the human doc would have.

Drift is its own failure mode — not a consequence of forgetting to maintain the docs, but a structural property of having two artifacts with no enforcement binding them. The only enforcement is discipline: when you update one, you update both in the same commit, and the human doc's failure-modes section explicitly lists "human doc not updated when recipe changes" as one of the named failure modes. The system cannot automate this. The discipline is yours.

## Both artifacts honor the verified-data contract

The shared contract from Chapter 3 is the one thing both artifacts must honor, and each honors it differently.

The AI artifact honors it procedurally: `skills/_shared.md` is the first item in the read-first list. The agent loads it, and the contract's prime directive is active for the entire run. The rules are live in context: use collected data and tested scripts first; never invent counts, rates, or coverage numbers; if a result comes from LLM judgment, label it as such.

The human artifact honors it structurally: the dependencies section lists which scripts the skill calls and which audits it reads, making the data provenance visible to anyone reading the card. The failure modes section includes specific entries for contract violations — what happens if the script isn't called, what the output looks like when a model fills in a gap versus when a script ran. The maintainer who reads the human artifact should finish it knowing exactly which parts of the verified-data contract this skill relies on and what breaks if that reliance is violated.

There is an additional fact here worth stating plainly. The F-1/OPT reader running this engine is both customers at different times. You author the skill, sitting at your laptop with context about what the skill is supposed to do, what scripts you built, what data you collected, what can go wrong. You are the human customer. Tonight, an agent runs the skill you wrote. The agent is the AI customer. In March, you — or someone who is nearly a stranger to this codebase — reads the human doc to understand why something is behaving strangely. You are the human customer again, but with much less context than you had when you wrote it.

The reader who has forgotten everything is not a hypothetical. It is you in three months. The human artifact is a letter you are writing to that person. Write it like it is.

## The scan skill, shown both ways

The best way to understand the two-artifact structure is to see it for one skill. The `scan` skill is the right choice: it is the first active skill in the engine's chain, it calls real scripts, and it exists in the repository you are using, so the commands are not examples I've constructed for illustration.

Here is the recipe an AI would follow:

---

**scan — AI recipe**

Read first:
- `skills/_shared.md`
- `scripts/ats/README.md`
- `data/ats/portals.example.yml`
- `data/ats/portals.yml` (if it exists)
- `data/ats/scan-history.tsv` (if it exists)
- `skills/RUN_LOG.md`

Run:
```bash
cd scripts/ats
python3 detect-ats.py "Company Name" --output ../../data/ats/ats_detection_sample.csv
cd ../..
npm run ats:scan
npm run ats:liveness -- --file data/ats/job-urls.txt
npm run ats:verify
```

Inspect output: count rows; count provider hits by platform; record empty results separately from errors; note where output was written.

Deduplicate: prefer exact URL; then company plus normalized role title; record suspected duplicates, do not delete uncertain entries.

Stop conditions: if `data/ats/portals.yml` does not exist, copy `data/ats/portals.example.yml` and edit before proceeding. Do not run the provider scanner against the example config.

Log template:
```markdown
## YYYY-MM-DD -- ATS scan
- **Skill:** scan
- **Input:** data/...
- **Command:** `...`
- **Output:** data/...
- **Worked:** ...
- **Did not work:** ...
- **Evidence:** row counts, provider counts, sample URLs
- **Next:** ...
```

Prompting rule: use LLM judgment only after script output has been inspected. The LLM may summarize patterns, explain likely failure causes, or propose the next test. It must not invent ATS hits, live job counts, or sponsorship claims.

---

Now here is the human card a maintainer reads:

---

**scan — human card**

**Purpose.** Detect which applicant-tracking system (ATS) a company uses and pull current job postings from configured portals. This is a data-collection step, not an analysis step. Its output feeds the pipeline skill.

**What it can verify:** whether a company exposes Greenhouse, Lever, or Ashby jobs; whether a portal scan produced new URLs; whether a posting URL appears in scan history; whether a posting is probably live after a liveness check.

**What it cannot verify on its own:** sponsorship likelihood; role quality; whether a company is a good target. Those require SEC/H-1B and BLS/SOC data, handled by later skills.

**Dependencies:**
- `skills/_shared.md` — the verified-data contract; must be loaded first
- `scripts/ats/detect-ats.py` — detects ATS by company name or CSV input
- `scripts/ats/scan.mjs` (via `npm run ats:scan`) — runs configured portal scan
- `scripts/ats/` — liveness check and verify commands
- `data/ats/portals.yml` — your working portal config (not the example)
- `data/ats/scan-history.tsv` — deduplication history from prior runs

**How to run:**
```bash
# Detect ATS for specific companies:
cd scripts/ats
python3 detect-ats.py "Company A" "Company B" --output ../../data/ats/ats_detection_sample.csv

# Run full portal scan (requires portals.yml to be configured):
cd ../..
npm run ats:scan

# Check liveness of specific URLs:
npm run ats:liveness -- --file data/ats/job-urls.txt

# Verify pipeline consistency:
npm run ats:verify
```

**What it produces:** detection output CSV; scan output with provider hits by platform; liveness signals per URL; a verification audit. A log entry in `skills/RUN_LOG.md` documenting what ran, what it found, and what failed.

**How it fails:**
1. `data/ats/portals.yml` missing — the scan will use the example config and return results for example companies, not your companies. The output will look plausible and be wrong. Check that `portals.yml` exists and is not identical to `portals.example.yml` before trusting any scan result.
2. ATS detection hits vs. live postings conflated — "ATS detected" means the provider is present. "Live posting" requires a liveness check. They are different facts. A skill output that reports ATS hits as if they were open jobs has skipped the liveness step.
3. Recipe updated, human doc not updated — if the commands in the recipe diverge from the commands in this card, one of them is wrong. Check the recipe before troubleshooting.
4. LLM fills in missing data — if the scan produces no results and the skill output contains confident sponsorship claims or ATS findings, the prompting rule was violated. No script output means no verified data. The output must say what it couldn't find, not invent a replacement.

---

The commands are identical between the two artifacts. What differs is the frame: the recipe assumes the reader will execute immediately; the human card assumes the reader is trying to understand. The same content, arranged for two different questions — "what do I run?" versus "what is this and how does it break?"

<!-- → [INFOGRAPHIC: Two annotated documents side by side — left labeled "AI Recipe (scan.md)" with callout arrows pointing to: read-first list, verbatim commands, stop condition, log template; right labeled "Human Card (scan — maintainer view)" with callout arrows pointing to: purpose statement, dependency list, annotated commands, failure modes numbered 1–4. Caption: "The recipe is optimized for execution. The card is optimized for comprehension. Neither does the other's job."] -->

## What writing them twice forces you to think about

There is an unexpected benefit to writing the skill twice that I didn't anticipate when I designed this architecture. The discipline of writing the human card — especially the failure-modes section — forces you to think adversarially about your own recipe. When you sit down to write "how does this fail," you discover that you have not thought carefully about what happens when `portals.yml` is missing, or when the liveness check returns zero results, or when the output CSV is empty because none of the companies matched. Those are the moments you realize the recipe has a gap: it doesn't say what to do in those cases, which means the agent running it tonight will improvise. Improvisation in a verified-data system looks a lot like invention, which is what the contract prohibits.

Writing the failure modes is how you find the missing stop conditions. The human card is not just documentation — it is a test of the recipe.

## The bridge to Chapter 5

Writing a skill well — two artifacts, shared contract loaded first, failure modes named, recipe and card maintained together — does not make the data the skill reads trustworthy. The scan skill can be structurally correct in every way this chapter describes and still return stale detection results, or miss a company because of a name-matching failure, or report a liveness signal on a posting that closed yesterday. The recipe follows the contract. The contract ensures the numbers aren't invented. Neither of those guarantees the numbers are the right numbers, measured the right way.

That question — are these the right numbers? — is the subject of Chapter 5. The verified-data contract set a floor: what you have is real. Chapter 5 asks whether real is enough.

---

## Exercises

**Warm-up**

1. *(Recall, easy)* Name the two customers a skill must serve and describe in one sentence what each one needs from the skill document. Why does a document that tries to serve both simultaneously tend to serve neither?
   *Tests whether you can articulate the two-customer problem before applying it.*

2. *(Recall, easy)* What is the first item in the `scan` skill's read-first list, and why does the recipe specify it first rather than letting the agent decide when to load it?
   *Tests whether you understand the shared contract as a prior constraint on execution, not a reference document.*

3. *(Identify, easy)* List three things the `scan` skill explicitly states it cannot verify on its own. For each one, name which other part of the engine would need to provide that information.
   *Tests whether you've understood the scan skill's scope before extending it.*

**Application**

4. *(Apply, moderate)* Take any skill in the `skills/` directory other than `scan.md`. Write its human card from scratch: purpose statement, dependencies, how to run, what it produces, and at least two named failure modes. Compare your card against the skill file — what did the original file contain that you missed, and what did you name that the original file didn't?
   *Tests the transition from understanding the two-artifact structure to producing the human artifact for a real skill.*

5. *(Analyze, moderate)* Run `npm run ats:scan` and then `npm run ats:verify`. Read both outputs. Write the `RUN_LOG.md` entry according to the scan skill's log template. Then write one sentence identifying whether any part of the output required LLM judgment to interpret, and if so, how that judgment is labeled.
   *Tests the run-inspect-record loop applied to the scan skill specifically, with attention to the data/judgment boundary.*

6. *(Analyze, moderate)* The chapter describes drift as a failure mode: the recipe changes and the human doc doesn't. Describe a realistic scenario in which drift would cause an incorrect run tonight. What would the incorrect run look like, and how would you detect that it was wrong? What single change to your workflow would prevent the scenario?
   *Tests adversarial reasoning about drift as a structural problem, not just a maintenance oversight.*

**Synthesis**

7. *(Synthesize, harder)* Design the human card for a hypothetical new skill — call it `refresh` — that re-downloads and re-verifies SEC Form D data for companies already in the pipeline. You don't have the recipe in front of you. Write the dependency list, the commands (drawing only from what `skills/_shared.md` lists as real commands), and at least three failure modes that are specific to re-downloading data that may have already been verified. Explain your reasoning for each failure mode.
   *Tests whether you can construct the human artifact from first principles using the shared contract as your ground.*

8. *(Synthesize, harder)* The chapter argues that writing the failure-modes section of the human card is a test of the recipe. Pick one failure mode from the `scan` skill's human card above. Trace backwards from that failure mode to a gap in the recipe — a condition the recipe doesn't handle, a step it doesn't specify, a stop condition it doesn't include. Write the missing recipe element. Then explain why the failure mode, not the recipe, was easier to see first.
   *Tests whether you can use the human artifact as a diagnostic tool for improving the AI artifact.*

**Challenge**

9. *(Evaluate, open-ended)* The two-artifact design requires discipline to maintain because there is no automatic enforcement binding the recipe and the human card. Propose a lightweight enforcement mechanism — it can be a naming convention, a commit hook, a section in the log template, or anything else — that would make drift detectable without requiring a human to compare the two artifacts manually on every update. Specify what the mechanism checks, what signal it produces when drift is detected, and what it cannot catch. Then evaluate its tradeoff: how much friction does it add per update, and how much drift does it prevent?
   *Tests whether you can design an enforcement solution that takes the two-customer constraint seriously, including its limits.*
# Chapter 5 — Verifying the Data

*A number that traces to a real record can still be measuring the wrong thing.*

Chapter 3 established a floor: every count, rate, and coverage number in this system must trace to a script output or an audit report, never to a model's best guess. That floor matters enormously. It is the difference between building on evidence and building on fluent fabrication.

But a floor is not a ceiling. Chapter 3 guarantees the number is real — that it came from counting rows in a public record, not from a language model estimating what the number probably was. This chapter asks a harder question: even if the number is real, is it trustworthy? Does it measure what you think it measures? Does the headline figure hold up when you look at the assumptions underneath it?

The distinction is not subtle. You can have a perfectly audited, perfectly script-sourced count that is quietly measuring the wrong thing. A join failure can make a prolific sponsor look like a non-filer. A base-rate mismatch can make a genuine signal look stronger than it is. A name-matching gap can exclude an entire corporate family from the dataset without leaving any evidence the missingness check can see. These are not data-pipeline bugs — they are epistemic failures. The numbers are real. The interpretation is wrong.

The methods in this chapter come from a companion book, *Computational Skepticism for AI*, where they are developed in full technical depth. I'm drawing on them here because they apply directly to the DOL and USCIS datasets this book runs on. If the reasoning feels compact in places, that's intentional — this is the practitioner application, not the derivation. What matters here is the procedure and what it surfaces.

<!-- → [INFOGRAPHIC: Three-tier stack. Bottom tier labeled "Chapter 3 guarantee: numbers trace to real records." Middle tier (this chapter) labeled "Chapter 5 asks: are the right things being measured?" Top tier labeled "Trustworthy inference." An arrow on the left side labels the gap between tiers 1 and 2: "Coverage gaps, name-matching failures, base-rate mismatch." Caption: "The floor the contract provides. This chapter builds the next tier."] -->

## The opening question: why are there exactly N rows?

Before I run any analysis on the LCA disclosure data, I ask a question that sounds almost too simple: *why are there exactly N rows in this dataset?*

The question comes from the epistemic-frame interrogation developed in *Computational Skepticism for AI*. The point is this: a dataset is not a census. It is a recording made by a particular instrument under particular conditions. The row count is not a fact about the world — it is a fact about the recording. Something determined where the data collection started, where it stopped, what joined successfully, and what got dropped quietly along the way. Unless you know what that something was, you don't fully know what the dataset represents.

For the DOL LCA disclosure data, the answer is more specific than it first appears. The dataset contains every Labor Condition Application that employers filed before hiring a foreign worker on an H-1B, H-1B1, or E-3 visa. So the row count is bounded by: who filed, in what time window, for what visa category, under what employer name, and whether the filing was accepted into the disclosure system. Each of those conditions is a filter the dataset silently applies before you ever open it.

Here is the practical consequence for this book: an employer who sponsored consistently but always filed under slightly different name variations — "Google LLC" in one quarter, "Google Inc." in another, "Alphabet Inc." in a third — will produce rows scattered across three employer-name buckets. An aggregation that groups by employer name and counts filings will treat these as three different companies, each with a modest filing count, instead of one company with a substantial one. The dataset is not wrong. The join is not broken. The rows are real. But the count you compute from them is not the count you meant to compute.

This is the "why exactly N rows?" move applied to the join problem. The boundary of the dataset is not just the schema — it is the schema plus every reference the schema's contents imply. The LCA dataset references employer names. Employer names reference legal entities. Legal entities undergo mergers, renamings, and restructurings. The full count lives somewhere in that chain. The dataset gives you a sample of it, bounded by however the names happened to be entered in the filing system.

<!-- → [DIAGRAM: One company (Alphabet / Google LLC / Google Inc.) shown as three separate employer-name buckets in the LCA filing data, each with a small filing count. A dotted box around all three labeled "Same legal filer." An arrow pointing to the aggregated true count. Caption: "Name-matching failures don't break the dataset. They fragment it. The rows are real; the employer grouping is not."] -->

## The six-step interrogation procedure

The six-step procedure in *Computational Skepticism for AI* is designed for any dataset you intend to base a deployment on. I'll walk through it applied to the sponsorship dataset — the LCA-to-H-1B join that the Sponsorship Scorer in Chapter 7 will run.

**Step 1 — Read the metadata and lock your prediction.** Before running any analysis, read the DOL disclosure file documentation. It tells you what fields are present, what time window is covered, and what constitutes a valid LCA. Write down what you expect the data to look like: how many rows, which employers should be there, what the approval rate distribution should look like. Lock this prediction before you look.

The prediction-lock matters for a specific reason. Without it, you only ever see the data as it is, which feels obvious, and you don't notice you've learned anything. With it, every gap between prediction and reality is a finding — the data is telling you something you didn't already know.

**Step 2 — Run the exploratory analysis.** Distributions, missingness, counts by employer, counts by year, counts by SIC code. The procedural pass. Note what shows up. Chapter 3's verification commands (`npm run ats:verify`, the sec and bls equivalents) produce the artifacts this step needs.

**Step 3 — Test the metadata against the actual data.** Does the time range match what the documentation says? Are the row counts consistent with the filing volumes the DOL reports in its summary statistics? Are there SIC codes present that shouldn't be, or absent that should be?

Here is where the "exactly N rows" question pays off. If the documentation implies a certain employer-universe coverage and the data shows a different pattern, that gap is a finding. Pursue it before moving on.

**Step 4 — Ask what is not in the data.** Look for dropped rows in the LCA-to-USCIS join. An employer who filed LCAs but whose H-1B counts appear zero or missing in the join may have a name-matching failure rather than a sponsorship failure. Look for time periods with sparse records — USCIS data has known gaps in certain fiscal quarters. Look for the companies that your prediction said should be there but aren't.

This step is not about finding errors in the data. It is about finding the shape of the data's coverage. What it can and cannot see.

**Step 5 — Trace at least one row end to end.** Pick one company from the dataset — say, the Cambridge biotech from Chapter 3's example. Follow its LCA filings through to the USCIS H-1B approval counts. Check whether the employer name in the LCA disclosure file matches the employer name in the USCIS data. Check whether the filing dates fall inside the H-1B fiscal year that would produce the approval counts you see.

I have done this trace. The experience is instructive every time. Almost every real dataset you trace this way turns up at least one surprise: a quarter where the filing count jumps because the company changed its legal name mid-year; a match that works on the first four words of the name but fails on the fifth; an approval count that appears lower than expected because one subsidiary filed separately.

**Step 6 — Write the epistemic frame and compare to your prediction.** What does the sponsorship dataset actually represent? It represents: LCA filings by employers operating under the names they used in a specific DOL submission window, joined to USCIS approval counts under the names USCIS recorded in its data, for the visa categories included in both disclosure regimes.

That is a more specific statement than "sponsorship data." The gap between the two is where the interpretation risk lives.

## Base rates and the confidence illusion

Even after the interrogation, there is a second failure mode that the procedure alone doesn't catch. It lives not in the data itself but in how a signal derived from the data gets interpreted. The mechanism is base rates, and the analysis comes from *Computational Skepticism for AI*'s treatment of calibration.

Here is the problem stated concretely. Suppose the Sponsorship Scorer produces a "0.65 probability of sponsorship" for a company in a given SIC code. That number came from a real signal — fifteen LCA filings, an 85% H-1B approval rate, sourced to DOL/USCIS records, exactly as Chapter 3 requires. But what does 0.65 actually warrant you to say?

It depends on the base rate. In most SIC codes, only a small fraction of employers have ever filed an LCA. In some technology-adjacent codes, this fraction might be 15–20%. In manufacturing, healthcare administration, or retail, it might be 2–3%. If only 3% of employers in a SIC code have ever filed an LCA, and the scorer's signal is calibrated, then even a strong positive signal produces a posterior probability that is lower than the raw 0.65 suggests. The math is Bayes' theorem, and it produces a result that consistently surprises people until they've worked through it enough times for it to become intuitive.

The false-positive problem is not hypothetical. A 99%-accurate test applied to a population where 1 in 10,000 people has the condition produces, for every 10,000 tests, approximately 1 true positive and approximately 100 false positives — so among all positive results, fewer than 1% are genuine. The numbers for sponsorship signals are not as extreme as this example, but the structure is identical: the base rate of the underlying phenomenon (this specific employer actually sponsoring H-1B workers for this type of role, right now, with openings available) is lower than the signal suggests.

Four diagnostic questions, drawn from *Computational Skepticism for AI*, settle whether a sponsorship signal is actually telling you what you think it is:

**What is the base rate?** What fraction of employers in this SIC code, size range, and geography have filed an LCA in the past three years? If the answer is 4%, a "likely sponsor" signal is working against a strong prior that says the company is not a sponsor. The signal has to overcome that prior, not just clear some absolute threshold.

**Is the signal calibrated?** A calibrated scorer means that when it says 0.65, the actual frequency of true positives among all cases scored at 0.65 is genuinely around 65%. Modern models are often well-calibrated in the middle of their probability range and badly overconfident at the extremes. Has anyone checked this scorer's calibration curve?

**What is the cost distribution of errors?** A false positive costs you an application fee, a cover letter, and time. A false negative costs you a lead you didn't pursue. These are not symmetric costs for an F-1 student racing a 90-day clock, but they are also not equally weighted across all circumstances. The right threshold depends on the cost ratio.

**What has changed since the data was collected?** The LCA data is historical. A company that was a prolific filer in 2021–2023 may have implemented a hiring freeze in 2024 or been acquired by a parent with a different sponsorship policy. The filing history is real; the inference to present sponsorship posture is an extrapolation across a time gap the data cannot bridge.

<!-- → [TABLE: Four columns — Diagnostic question / What it surfaces / Where to find the answer / What to do if the answer is unfavorable. Rows: Base rate / Prior probability before seeing the signal / SIC-level LCA filing frequency in the audit / Lower the effective threshold, require stronger corroboration; Calibration / Whether the scorer's stated probability is reliable / Calibration curve if available; cross-validate on holdout / Treat stated probabilities as ordinal ranks, not face-value probabilities; Cost distribution / Whether false positives or false negatives are more costly / Depends on application deadline and role fit / Adjust threshold accordingly; Freshness / Whether historical filings predict current posture / Filing date in the LCA data; recency filter in the audit / Downweight filings older than 18 months; flag acquisitions] -->

## The verb taxonomy: what a score warrants you to say

There is a third failure mode, and it is the most insidious because it looks like good practice. You have done the interrogation. You have checked the base rate. The signal is real and reasonably calibrated. You hand the result to a language model to frame for the user. The model says: "This company sponsors H-1B visas for data science roles."

That sentence is not warranted by the evidence.

*Computational Skepticism for AI* has a verb taxonomy for exactly this problem. Different levels of evidence warrant different verbs: *hypothesize, suggest, observe, find, show, demonstrate, conclude, prove.* Each occupies a specific evidential posture. Using a verb stronger than the evidence warrants is an epistemic error — a category of error that happens at the output layer, after the data is already verified, and is therefore invisible to any data-quality check.

Here is what the evidence actually warrants, stated in calibrated language:

The DOL LCA disclosure data **shows** fifteen filings by this employer in the three-year window covered by the dataset. The USCIS approval data **shows** an 85% H-1B approval rate for this employer in the same period. The Sponsorship Scorer **observes** a signal consistent with active filing.

What the evidence does not warrant: *this company sponsors.* "Sponsors" is a present-tense claim about current employer policy, extrapolated from historical filings through a name-matching join that may have coverage gaps. The historical evidence supports a finding about what happened. It does not support an unhedged present-tense conclusion.

The practical rule: every claim the system emits should carry its warranted epistemic verb. "We observe fifteen filings" is a data claim. "We find a strong historical sponsorship signal" is a finding from the data. "This company sponsors" is a conclusion that requires more than the data can directly supply. Chapter 3 established the data-claim / model-judgment distinction. This chapter gives it a finer vocabulary.

## The honest ceiling

I want to be direct about what the verified-data contract cannot guarantee, because the temptation to overstate it is real — especially when the data checks out, the pipeline runs clean, and everything looks right.

The contract guarantees counts are real. It cannot guarantee the right thing was measured.

Coverage gaps are structural. The LCA dataset covers H-1B, H-1B1, and E-3 visas. A company that sponsors TN workers under the US-Mexico-Canada Agreement, or L-1 intracompany transfers, or O-1 extraordinary ability visas, will appear in none of these disclosures. From the dataset's perspective, they are not a sponsor. From the candidate's perspective, they are.

Name-matching failures are not edge cases. The LCA database and the USCIS approval database are maintained by different agencies under different administrative systems. A company that appears as "TechCorp LLC" in DOL filings and "TECHCORP" in USCIS data may join successfully or may not, depending on the exact normalization applied in the join script. The join script's coverage is documented in the audit; the audit reports how many rows matched and how many didn't. But it reports this at the aggregate level. The individual company that fell through the join looks identical to a genuine non-filer from the outside.

Freshness windows are a policy choice with real consequences. The default in this system uses a three-year lookback window. That is long enough to provide stable signal for established sponsors and short enough to exclude obviously stale data. But a company that sponsored aggressively in 2020–2022 and then implemented a blanket hiring freeze in 2023 will still score as a strong sponsor under this window. The filing history is real. The current hiring posture is unknown.

None of these are arguments for abandoning the data. They are arguments for being precise about what the data can and cannot say, and for making sure the output layer respects that precision. The honest ceiling is not a failure — it is the accurate description of what you have.

<!-- → [TABLE: Two columns — What this chapter's method guarantees / What it cannot guarantee. Rows: The N rows in the dataset represent real filings / That all filings by this employer are in the dataset; The employer-name grouping reflects the filing record / That name-matching failures don't fragment prolific sponsors; The sponsorship signal is calibrated against base rates / That historical filing rates predict current hiring posture; Output verbs are warranted by the evidence / That the right visa category is covered for this candidate; Coverage gaps are labeled in the audit / That the gaps don't systematically exclude a particular type of employer. Caption: "What this chapter adds to the floor Chapter 3 built."] -->

## Worked example: one company end to end

Let me make this concrete with the kind of trace Step 5 requires.

Take a mid-sized Cambridge biotech — the type of company Chapter 3 used to contrast verified and model-generated answers. It's a reasonable sponsorship candidate: talent-competitive field, specialized roles, graduate-intensive hiring.

I run the sponsorship dataset query. The result comes back: twelve LCA filings over three years, 80% H-1B approval rate, predominantly filed under job titles in "Life Sciences Researchers" SOC codes. The Sponsorship Scorer returns 0.68. So far, so good.

Now the trace. I pull the raw LCA rows for this employer. The name appears in two variants: "BioTechCo LLC" (ten rows) and "BioTechCo, LLC" (two rows — note the comma). The USCIS approval data has this employer under "BIOTECHCO LLC" (all caps, no comma). The join script normalized case but did not strip punctuation. The two rows filed under "BioTechCo, LLC" did not join to the USCIS data. They appear in the LCA count but not in the approval count. The approval rate calculation is therefore based on ten LCA filings, not twelve.

This does not change the conclusion dramatically — the employer is still a genuine historical sponsor. But it illustrates the mechanism. The gap is not a data error. Both records are correct. The join is the fragmentation point. And the dataset's missingness check reported zero missing values — because the rows are present, just in separate buckets that don't join.

Now the base rate check. In this SIC code (pharmaceutical and medicine manufacturing), the three-year LCA filing rate among employers in the DOL's universe is approximately 8%. The scorer returned 0.68. Working through the Bayes update: prior 0.08, likelihood ratio based on the observed filing count, posterior approximately 0.38–0.45 depending on assumptions. The 0.68 overstates the posterior probability by somewhere between 50% and 75%.

What does this mean for an F-1 student considering this company? It means the verified-data finding is: "We observe twelve LCA filings in three years and an 80% historical approval rate." It does not mean "this company sponsors." It means this company has a demonstrated filing history that makes them a reasonable target for further investigation — specifically, a direct inquiry about current H-1B sponsorship posture for the specific role and visa type relevant to you.

That's a more conservative conclusion than the raw score implies. It is also an honest one.

## The bridge to Chapter 6

Chapter 6 builds the first complete tool: the funding detector, which queries SEC Form D filings to find companies that just raised capital and are therefore under pressure to hire.

The method from this chapter travels with it. For every number the funding detector produces — round size, recency, investor profile — the same four questions apply: what is the base rate of companies in this category that are actually hiring? Is the signal calibrated? What does a false positive cost? What has changed since the filing date?

The practical difference from a user perspective is significant. A company that just closed a Series B and has zero verified sponsorship history is a different kind of lead than a company with fifteen LCA filings that raised no capital in three years. Neither signal alone is sufficient. Both together, interrogated against base rates, interpreted with calibrated verbs, and labeled with their coverage gaps, are what a trustworthy inference looks like.

That is the architecture of every chapter from here forward. The verified-data contract provides the floor: numbers trace to records. The epistemic-frame interrogation provides the next tier: those records are measuring what you think they're measuring, within documented limits. The verb taxonomy provides the output discipline: the system says exactly what the evidence warrants, and no more.

---

## Exercises

**Warm-up**

1. State the distinction this chapter draws between Chapter 3's guarantee and Chapter 5's question. In one sentence each: what does Chapter 3 guarantee, and what additional question does this chapter require you to ask?
   *Tests whether you can articulate the floor vs. the honest ceiling without conflating them.*

2. Name the six steps of the epistemic-frame interrogation procedure. For each step, identify what kind of failure it is designed to surface that the exploratory data analysis alone would miss.
   *Tests structural recall of the procedure and the reasoning behind each step.*

3. What is the "why exactly N rows?" question, and why is it asked before looking at any histograms or summaries? What does the row count tell you that the data itself does not?
   *Tests the opening move of the interrogation and the concept of boundary vs. schema.*

**Application**

4. Download the DOL LCA disclosure file for the most recent quarter available. Apply Steps 1–3 of the six-step procedure: lock a prediction about the employer count and coverage, run the exploratory analysis, and test the metadata against the data. Write up one gap between your prediction and what you found. What does the gap indicate about the dataset's epistemic frame?
   *Tests the prediction-lock discipline applied to a real public dataset.*

5. Take the name-matching gap described in the worked example — "BioTechCo LLC" vs. "BioTechCo, LLC" — and write a normalization function in pseudocode or your preferred language that would merge these two variants. Then identify two types of name variation this function would still miss, and explain why they're harder to handle without additional data.
   *Tests the gap between knowing coverage failures exist and knowing how to address them.*

6. A company in the tech sector has twelve LCA filings over three years and an 82% H-1B approval rate. The Sponsorship Scorer returns 0.71. The LCA filing rate for employers in this company's SIC code is 12%. Using the four diagnostic questions from this chapter, write the calibrated finding — what the evidence warrants saying, stated with the appropriate epistemic verb. Do not write the word "sponsors" as an unqualified present-tense claim.
   *Tests base-rate calibration and the verb taxonomy together on a realistic example.*

**Synthesis**

7. The coverage gap for non-H-1B visa categories (TN, L-1, O-1) means the sponsorship dataset will systematically undercount certain types of employers. Identify one type of employer — by industry, size, or organizational structure — that is most likely to be undercounted for this reason. Explain the mechanism, name the coverage gap in the audit, and write the label you would attach to any output concerning this employer type.
   *Tests the honest-ceiling reasoning applied to a specific structural gap.*

8. Design a two-sentence output format for the Sponsorship Scorer that applies the verb taxonomy correctly. Sentence one should be a data claim (use "observe" or "find"). Sentence two should be an explicit calibration note (use "does not warrant" or "is consistent with"). Test your format on the Cambridge biotech example.
   *Tests the practical application of the verb taxonomy in system output design.*

**Challenge**

9. The six-step procedure, the base-rate calibration, and the verb taxonomy together form a method for building trustworthy inferences on top of verified data. Identify one realistic scenario — a specific type of company, role, or visa situation — in which all three checks pass and the inference is still systematically misleading. What would a fourth check look like? What evidence would it require, and who would be responsible for producing it?
   *Tests whether you can find the limits of the method itself, not just apply it correctly.*
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
# Chapter 7 — Who Sponsors: The 80 Days Sponsorship Scorer
*Why the record always outranks the reputation.*

Here is something that bothers me every time I see a job seeker's target list: the names on it are chosen for how they feel, not for what they've done. A household brand — a logo you've worn on a t-shirt — sits at the top. Fifteen companies you've never heard of sit nowhere, because you've never heard of them. And that ranking is exactly backwards, in a way that is measurable, sourced, and correctable.

A Cambridge biotech with no consumer presence files fifteen Labor Condition Applications over three years and maintains an 85% H-1B approval rate. The household brand files essentially zero LCAs for roles like yours. For a candidate who needs sponsorship, the unknown biotech is a vastly better target — not by opinion, not by vibe, but by the public record. The whole problem is that prestige is loud and the visa record is quiet. This chapter makes the quiet record louder.

<!-- → [CHART: horizontal bar chart showing a hypothetical pair of companies — "Famous Brand" vs. "Unknown Biotech" — with bars for LCA count, approval rate, funding recency, and composite score; the visual should make the ranking flip visceral and immediate] -->

What I want you to notice before we go further: this is not about dismissing well-known companies. Some famous companies are prolific sponsors. Some unknown biotechs file nothing. The point is that you do not know which is which from the name alone — you only know from the record. Everything in this chapter is about reading the record correctly.

---

The record lives in three datasets, all public, all free.

The first is **SEC Form D**, which you met in Chapter 6. It tells you when a company raised money and how much. Funding recency matters because a company that raised $12 million eight weeks ago is a different entity than one whose last round was three years ago and whose runway is unclear.

The second is the **DOL LCA disclosure data** — every Labor Condition Application an employer files with the Department of Labor as a precondition for hiring a foreign worker. An LCA is not the visa itself; it is the step before. It says: this employer is willing, organized, and legally set up to go through the process. A company with a filing history has built the machinery. A company with no filings either has not built it or has decided not to use it for roles like yours. Both conclusions matter.

The third is the **USCIS H-1B Employer Data Hub** — actual approvals and denials by employer and year. This is not intent; it is outcome. An employer can file LCAs and still fail at the H-1B stage. The approval rate tells you how the filings resolve.

<!-- → [DIAGRAM: three-node pipeline showing SEC Form D → DOL LCA Data → USCIS H-1B Hub flowing into a "Sponsorship Scorer" node, with arrows labeled "funding recency," "filing behavior," and "approval rate"; include a fourth node for "company-size signals" feeding in from below] -->

These three datasets are joined by the **80 Days pipeline** on resolved company names. That last phrase — resolved company names — is doing more work than it appears to. "Google LLC," "Google Inc.," and "Alphabet" must be recognized as one entity or a real sponsor looks like a stranger in the data. The join is the hard part. An "Unknown" tier caused by a failed name match is not the same as a true absence of filings, and I will return to that distinction because it is one of the two most important things in this chapter.

---

The scorer reduces those three datasets into a single number:

> **P(sponsorship) = LCA filing rate (3-yr) × 0.40 + H-1B approval rate × 0.30 + funding recency × 0.20 + company-size signals × 0.10**

Read those weights as a claim, and ask whether you agree with it.

The LCA filing rate carries 40% of the weight because filing is the most direct revealed action available in public data. A company that files LCAs has made a decision — to build the legal infrastructure, engage immigration counsel, pay the fees, and go through the process. That decision is load-bearing in a way that a company's reputation is not. You can be famous without ever filing an LCA. You can be unknown and file thirty.

The H-1B approval rate carries 30% because filings that don't succeed tell a different story than filings that do. An employer with a 40% approval rate and an employer with an 85% approval rate are both sponsors in name. In practice, they are different bets.

<!-- → [TABLE: side-by-side comparison of two hypothetical employers — one with high filing rate and low approval rate vs. one with moderate filing rate and high approval rate — showing how the composite score differs and what each profile implies about the employer's process] -->

Funding recency carries 20% because the question is not just whether a company has sponsored in the past but whether it has the resources and growth trajectory to do so now. A company that raised eight weeks ago is in a different hiring skill than one that is managing a quiet contraction.

Company-size signals carry 10% — not because size is unimportant, but because its effect is already partially captured by the other three. A fourteen-person lab and a ten-thousand-person firm behave differently on average, but the record is the record. A small lab with a strong filing history is better evidence than a large firm with none.

The composite probability then maps to a tier. **Proven** means strong, recent filing history and high approval — the evidence is unambiguous. **Likely** means some evidence: a few filings, or strong funding plus partial history. **Unknown** means no evidence either way. **Avoid** means evidence the company does *not* sponsor in your kind of role — a clear zero-history non-sponsor that the engine should actively skip rather than merely lack data on.

I should flag something here. The system design document underlying the 80 Days pipeline describes three tiers — Proven, Likely, Unknown. The plain-language summary of the same system adds Avoid as a fourth. This chapter uses four tiers because "Avoid" does real work: it lets the engine actively deprioritize known non-sponsors rather than merely lacking data on them. The tier set and exact probability thresholds for each boundary need to be reconciled against the SDD before this goes to print. I am being transparent about that because the tier labels and thresholds are the output a reader will act on, and the distinction between a system that has three skills and one that has four is not cosmetic.

<!-- → [INFOGRAPHIC: a horizontal spectrum from "Avoid" through "Unknown" through "Likely" to "Proven," with approximate probability ranges on the axis and brief action cues below each tier — what the engine does and what you do] -->

---

Now let me show you what this looks like on a real case — or rather, a case that is real in structure, with illustrative numbers, so you can see how the reasoning works before you run it on your own list.

Return to the Cambridge biotech. LCA filings: 15 over three years. That is a strong filing rate for a company of this size — they are not dabbling in sponsorship, they have built the process. H-1B approval rate: 85%. Funding: $12 million raised eight weeks ago, which puts the recency score near maximum. Size: roughly 40 employees, which is mid-small.

Running the weights: the LCA rate (×0.40) dominates because it is high and the weight is highest. The approval rate (×0.30) confirms the filings are not just optimistic paperwork. The funding recency (×0.20) says they have the resources to keep going. Size (×0.10) is neutral-to-positive — a 40-person lab is not so large that bureaucracy slows everything down and not so small that one departure breaks the immigration infrastructure. The composite lands well into Proven.

Now run the same logic on the household name. LCA rate: approximately zero for roles like yours. That ×0.40 term contributes nothing. No relevant H-1B approvals in your role category. The funding and size numbers are strong — they have the money, they have the infrastructure — but those terms together carry only 30% of the weight, and they cannot rescue a zero on the 70% that measures actual sponsorship behavior. The company lands in Avoid.

<!-- → [CHART: two stacked bar charts side-by-side showing the weighted score breakdown for each company — each bar segment labeled with its component and weight, making visible how the "Avoid" company's 70% goes to zero while the Proven company builds from all four components] -->

The decision is not close. The unknown biotech goes to the top of the active application list. The household name gets skipped. That is the backwards ranking, now defended by four sourced numbers.

But I want to be careful here. The record is a rear-view mirror. A company that sponsored heavily for three years may have frozen sponsorship last month. The immigration attorney who drove those 85% approvals may have left in March and taken the process knowledge with them. The LCA data is published on a lag. A company that raises a new round and starts hiring aggressively may look Unknown today and Proven in six months — and the record will not tell you that yet.

This is not a reason to distrust the tier. It is a reason to hold the tier correctly: as a well-evidenced prior, not a guarantee. You are Bayesian here. The tier tells you where the evidence points. The conversation you have with the recruiter is where you update.

---

The most common misread of this system is treating Unknown as Avoid. I want to spend a moment on this because it is not a subtle error — it is the error that throws away exactly the companies Chapter 6 worked to surface.

*Avoid* means the record shows this company does not sponsor your kind of role. The evidence is there; it is just negative. *Unknown* means the record is silent. Silent is different from negative. A company is Unknown for one of two reasons: either there is genuinely no filing history (they have never sponsored, or they are so young that the data does not exist yet), or the name did not match when the pipeline joined the datasets.

Those two causes of Unknown require opposite responses. A true absence of filings on a three-year-old company with strong funding is a prompt to look for direct sponsorship signals — a careers page that says "visa sponsorship available," a LinkedIn post about a recent hire on an H-1B, a direct question to the recruiter. A failed name match is a data problem you fix by resolving the entity and re-running. You cannot tell which you are dealing with by looking at the tier alone. You tell by reading the join-coverage audit.

<!-- → [TABLE: two-column table distinguishing "True Unknown" from "Name-Match Artifact Unknown" — rows for: how to identify it, what the record shows, what action it requires, and what the risk of treating it as Avoid would cost you] -->

The pipeline exposes this. From the project root:

```bash
cd scripts/sec
python validate-h1b-join-sample.py
```

checks the company-name join against USCIS H-1B data, and:

```bash
python scripts/audit-sec-dol-h1b-data.py
```

audits the full SEC + DOL + H-1B join coverage. The output is a number: how many companies on your shortlist matched, how many failed to match, and therefore how much of your list the tier actually covers. You read that coverage number before trusting any Unknown. If 30% of your shortlist failed to match, a significant fraction of your Unknowns are artifacts, not verdicts.

---

Let me say what I actually cannot see from this data, because intellectual honesty requires it.

The pipeline knows a company filed fifteen LCAs. It cannot know those fifteen were all for senior principal scientists and the company has a quiet policy against sponsoring entry-level hires. It knows an 85% approval rate; it cannot know that the attorney who drove those approvals left in March. It cannot know that an Avoid company just hired a new VP of Engineering who is changing the sponsorship policy this quarter. It cannot know that a Proven company just went through a round of layoffs and has frozen all new sponsorship for six months.

The tier is what the public record supports. What the public record cannot support is inference about a specific role, a specific month, a specific team. That is not a flaw in the scorer — it is the honest boundary of what any retrospective dataset can tell you. The boundary matters because crossing it silently is how you make bad decisions with confident numbers.

What the record can tell you, reliably, is: has this company demonstrated that it is willing and able to sponsor? That is the question the tier answers. Whether this company will sponsor you, in this role, right now — that is the question the tier informs but cannot answer.

<!-- → [DIAGRAM: a decision tree beginning at "Tier assigned" — branching from Proven/Likely to "Target actively" and then to "Verify role type matches filing history," from Unknown to "Check coverage / resolve name match" and "Look for direct signals," and from Avoid to "Skip — reallocate application time (see Chapter 2)"] -->

The last thing I want to leave you with is the decision rule, because knowing the tier is only useful if you know what to do with it.

Proven and Likely justify the targeted two hours of application effort from Chapter 2. These are companies where the evidence supports the investment. Unknown — if fit and funding are strong — stays on the list, but gets a different kind of attention: resolve the name match, find the direct signal, and only then decide. Avoid gets skipped. This is precisely the class of target the engine exists to let you skip. The hours you save on non-sponsors are the hours that fund the depth you put into Proven targets.

The puzzle the record cannot solve is one level up: a company that will sponsor is worthless to you if the posting they listed is a ghost. So before you spend the targeted application time a Proven tier earns — is the role even real?

---

## Exercises

**Warm-up**

1. *(Recall — single-concept)* The composite scoring formula weights four inputs. Without looking, name them and their weights. Then write a one-sentence explanation for why the LCA filing rate carries more weight than company-size signals.
   *Tests: understanding of weight rationale, not just memorization of numbers.*
   *Difficulty: Low*

2. *(Distinguish — single-concept)* A company appears as Unknown in your tier output. Describe two distinct reasons this could happen, and for each, state what action the correct interpretation requires.
   *Tests: the Unknown ≠ Avoid distinction and its practical consequences.*
   *Difficulty: Low*

3. *(Apply — single-concept)* You run the join-coverage audit and find that 40% of your shortlist failed to match. What does this tell you about the reliability of the Unknown tiers in that 40%? What is the first step?
   *Tests: reading coverage output before trusting tier assignments.*
   *Difficulty: Low*

**Application**

4. *(Compute — multi-input)* A company has the following inputs: LCA filing rate (3-yr) = 0.7, H-1B approval rate = 0.6, funding recency score = 0.9, company-size signal = 0.5. Compute the composite P(sponsorship) using the chapter's formula. Which tier would this place the company in, assuming standard thresholds?
   *Tests: mechanical application of the weighted formula.*
   *Difficulty: Medium*

5. *(Compare — multi-input)* Company A has a strong 3-year LCA history but a 45% approval rate. Company B has only 3 LCAs over three years but a 92% approval rate and recent Series B funding. Compute approximate scores for both. Which is the better target and why — and what does the comparison reveal about what the weights are actually measuring?
   *Tests: trade-off reasoning across inputs, not just formula execution.*
   *Difficulty: Medium*

6. *(Audit — procedure)* You assign a famous company an Avoid tier. A friend argues this is wrong because "everyone knows they hire internationally." Write the argument you make to defend the Avoid assignment, and name what single piece of new evidence would change the tier.
   *Tests: defending tier from evidence rather than reputation; updating on evidence.*
   *Difficulty: Medium*

**Synthesis**

7. *(Integrate — cross-chapter)* A company from your Chapter 6 shortlist scores Proven on sponsorship but has a funding event that is 26 months old. The LCA history is strong. How do you weight the stale funding against the filing history? What decision does the composite support, and what additional check does the stale funding prompt?
   *Tests: combining Chapter 6 funding logic with Chapter 7 scoring; not treating inputs as independent verdicts.*
   *Difficulty: High*

8. *(Diagnose — system behavior)* The 80 Days pipeline assigns Unknown to a company you know personally sponsors aggressively — you have a contact there who is on an H-1B. Walk through the two most likely explanations for the discrepancy, and describe the steps you would take to either correct the tier or confirm it as a pipeline limitation.
   *Tests: understanding name-match artifacts vs. true data absence; debugging system output against ground truth.*
   *Difficulty: High*

**Challenge**

9. *(Design — open-ended)* The current formula weights LCA filing rate at 0.40 and company-size signals at 0.10. Suppose you are building a version of this scorer specifically for targeting very early-stage startups (Series A and earlier). Make the case for at least one weight adjustment that would improve tier accuracy for this population, and explain what the adjustment reveals about what the original weights were implicitly assuming.
   *Tests: understanding the assumptions baked into the scoring model; applying the model's logic to a constrained subpopulation.*
   *Difficulty: High/Open-ended*
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
# Chapter 10 — The Visa Timeline Manager
*The clock is a gate, not a tiebreaker.*

Here is a thing that happens, and it is quietly devastating when it does. A student has three months of work authorization left. They find a role that fits almost perfectly — the company sponsors, the posting is live, the occupation matches, the quality signals are strong. They apply. They make it through the screens, the take-homes, the panels. Four months later, an offer arrives. And it is worthless. The start date is past the day their authorization ended. They spent the scarcest months of their search — the months they had the least of — chasing an offer that the calendar had already ruled out before the first email went out.

No filter in Chapters 7 through 7 would have caught this. Sponsorship was real. The role was live. The quality was high. The thing that killed it was time, and time is the one constraint that is *yours specifically* — invisible to the company, invisible to every scorer that does not know your dates.

<!-- → [DIAGRAM: a horizontal timeline showing: "Student applies" → "Phone screen" → "Technical rounds" → "Panel interview" → "Offer" — with a vertical red line labeled "Authorization ends" falling between "Technical rounds" and "Offer"; the visual makes visceral that everything after the red line is unreachable regardless of how good the news is] -->

What I want to sit with before we go further is the structure of this error. The student did not miscalculate. They did not misread a sponsorship tier. They made a decision that was perfectly rational given incomplete information: they applied to a high-quality role without first asking whether the calendar permitted it. The Visa Timeline Manager exists to make that omission impossible — to force the calendar question to the front, before the excitement of a good-looking posting makes it easy to postpone.

---

Three windows govern an international student's runway, and the way they interact is not obvious until you map them.

The first is **OPT** — post-completion Optional Practical Training. After you finish your degree, you have a window of authorized work, and inside that window you may accrue no more than 90 cumulative calendar days of unemployment.[^opt] That ceiling is not a soft guideline. Exceeding it terminates your status, with no grace period. The 90 days do not reset. They accumulate from the first day your OPT begins. Every day you are not employed or not in a valid application process counts against that ceiling whether you notice it or not.

The second is the **STEM OPT extension**. If your degree is in a qualifying STEM field, you are eligible for a 24-month extension beyond the standard OPT period — and critically, the unemployment ceiling rises to 150 days aggregate. Eligibility changes the math entirely. A student without STEM eligibility and four months of authorization has a fundamentally different runway than a STEM-eligible student with four months remaining and the extension not yet filed. The calendar says they are in the same situation. The law says they are not.

The third is the **H-1B lottery window** — the annual cycle of registration, selection, and petition that determines whether a path past OPT exists with a given employer in a given year. The lottery runs on a fixed annual schedule. If your authorization expires before the next window resolves, the H-1B path is not available to you regardless of how willing the employer is to sponsor. Sponsorship and the ability to act on sponsorship are different things, and the lottery timing is what separates them.

<!-- → [INFOGRAPHIC: three stacked horizontal bars representing OPT window, STEM OPT extension, and H-1B lottery window — annotated with key thresholds: 90-day unemployment ceiling, 150-day ceiling, lottery registration month, cap-subject start date — showing how a student's runway is the combination of all three, not just the first bar] -->

What the Visa Timeline Manager does is compress these three windows into a single number: a **timeline factor between 0 and 1** that gets multiplied into a role's composite score.

The design logic of a multiplier rather than an addend matters here. If the timeline factor were just another component that averaged in with sponsorship, fit, liveness, and quality, a strong-enough role could mathematically overcome a bad timeline. A 0.95 fit and a 0.9 quality score could dilute a 0 timeline to something that still looks actionable. That would be wrong — not just suboptimal, but wrong in a way that produces exactly the outcome from the opening case. The multiplier forecloses this. A factor of 0 zeroed into a composite of any magnitude produces 0. The clock is a gate.

---

The factor is computed from eight intake questions the system asks at setup: your visa type, your authorization end date, how many unemployment days you have already used, whether you are STEM-eligible, your field, your target buffer, and the estimated process length for the role being scored. These are first-class constraints, not profile decoration. They are what makes a score *yours* rather than generic.

Conceptually, the computation looks like this:

```text
factor = timeline_factor(
    auth_type              = "OPT",
    auth_end_date          = "2026-08-30",
    unemployment_days_used = 22,
    expected_time_to_start = "16 weeks",
    stem_eligible          = True,
    buffer_target          = "80 days"
)
# returns a value in [0, 1]; 0 = skip regardless
```

The output is always the factor *and* the dates that produced it. A timeline factor you cannot trace to specific dates is a number you cannot defend, and this is the one factor where a silent error costs you the whole search. If the factor says 0 and you cannot see why, you have a data entry problem, not a calendar problem — and those require different responses.

<!-- → [TABLE: three-column table showing: input parameter | what it measures | consequence of error — rows for auth_end_date, unemployment_days_used, expected_time_to_start, and stem_eligible; the "consequence of error" column makes visible that each input has asymmetric costs: being too optimistic costs the whole search, being too conservative costs one opportunity] -->

The factor resolves into three cases. A **factor of 0** means the role is skip-regardless: the expected time-to-start exceeds your remaining authorization, and no other signal changes that. A **factor near 1** means comfortable buffer — the expected hiring timeline finishes well inside your authorization with room to spare. A **factor between 0 and 1** is where most of the interesting cases live: buffer-based scaling, where as the expected start date creeps toward the cliff, the factor falls — gently penalizing roles that are probably fine but cut it close, so that all else equal the engine prefers the role you can safely land.

---

Let me walk through three roles for a single student to show how these cases feel in practice.

The student is a STEM-eligible master's graduate. OPT ends in roughly five months. Twenty-two unemployment days already used. Self-imposed target: an 80-day buffer below the 90-day ceiling, which functions as a margin of safety — not a legal threshold, just a planning discipline built into the engine.

**Role A** is a large firm. Its hiring process historically runs about five months: multiple rounds, committee review, compensation negotiation, offer processing. The expected start date lands past the authorization end. Factor = 0. Skip regardless — and the reason it deserves that label, not just "low priority," is that applying does not just waste time. It consumes unemployment days while you wait, which erodes the buffer you need for the roles you *can* land.

**Role B** is a startup that can move in about six weeks when motivated. Expected start lands with months of buffer. Factor ≈ 1. No timeline objection — the other factors decide.

**Role C** is a mid-size firm, roughly twelve-week process. Expected start lands inside authorization but eats most of the buffer. Factor ≈ 0.6 — kept, but penalized relative to B. If Role C and Role B were otherwise equal, the engine prefers B, because the candidate who lands B does not spend the last weeks of their authorization anxiously waiting for Role C's offer.

<!-- → [CHART: a horizontal bar chart showing the three roles with their expected start dates plotted against the student's authorization end date — Role A's bar extends past the end date (red), Role B finishes well short (green), Role C finishes just inside (yellow); a vertical dotted line marks the 80-day buffer target] -->

The decision rule that follows from this is simple to state and genuinely hard to execute: drop Role A *now*, before you invest more time in it. Free those weeks for Role B and for the networking that surfaces roles like Role B. Keep Role C with eyes open. The hard part is executing the drop on a role that looks excellent in every other dimension. The factor is designed to make that drop automatic — not a judgment call you have to make while excited about a good-looking posting, but a mathematical output you read before the excitement has a chance to override the calendar.

---

Now let me tell you what this factor cannot do, because the honest limits of any tool are part of using it correctly.

The factor knows your dates and a company's typical pace. It does not know that this particular hiring manager will fast-track you because their team is on fire, collapsing a five-month process to three weeks. It does not know that you would be willing to accept a role in a different country if the U.S. clock runs out, which would change what "skip" means for you entirely. And it absolutely cannot practice immigration law.

The difference between eligible and ineligible for a STEM extension can hinge on a detail — the CIP code on your transcript, a filing timing question, a program classification — that only an immigration professional should rule on. The factor gates out the impossible. The negotiable edges and the legal specifics stay human. This is not a caveat to be skim-read; it is load-bearing. A student who treats a factor of 0.4 as authorization to apply to a borderline role without consulting their DSO has misread what the number is. It is a planning multiplier, not legal advice.

<!-- → [DIAGRAM: a decision tree beginning at "Factor computed" — branch from 0 to "Skip regardless / reallocate time (Ch. 2)," branch from low but > 0 to "Apply only if strong on other factors AND accelerated process is possible," branch from high to "No timeline objection — let sponsorship, fit, liveness, quality decide"; each terminal node also shows a human-judgment check: "Verify with DSO if STEM eligibility is uncertain"] -->

There is one more error worth naming before this chapter closes. It is the error almost everyone makes at least once: finding a role that looks excellent in every other dimension and mentally filing the timeline question under "figure out later." Later is exactly when it is too late. The excitement of a good role is precisely the moment when the timeline question feels most like an interruption. That feeling is the signal to compute the factor first — because a factor of 0 means the excitement is a trap, and you want to know that before the four months, not after.

Five numbers now describe every role you are considering: sponsorship, fit, liveness, quality, and timeline. One of them can zero out all the others. The question is how the engine fuses them into a single decision — and why, in that fusion, sponsorship gets the loudest vote.

---

## Exercises

**Warm-up**

1. *(Recall — single-concept)* Explain, in one paragraph, why the timeline factor is implemented as a multiplier rather than an addend in the composite score. What outcome would a purely additive design allow that the multiplier forecloses?
   *Tests: understanding the gate logic vs. vote logic distinction.*
   *Difficulty: Low*

2. *(Distinguish — single-concept)* A student has a timeline factor of 0 for Role A and 0.55 for Role B. Role A has better sponsorship, fit, and quality scores. Write the decision and the reasoning. Then name the one thing that could change the factor for Role A without changing any of the other inputs.
   *Tests: reading the gate correctly; identifying expected-time-to-start as the lever.*
   *Difficulty: Low*

3. *(Apply — single-concept)* A STEM-eligible student and a non-STEM-eligible student both have four months of OPT remaining and 30 unemployment days used. Describe the difference in their timelines. How does STEM eligibility change which roles they can safely target?
   *Tests: the runway difference between OPT and STEM OPT; impact of the 150-day ceiling.*
   *Difficulty: Low*

**Application**

4. *(Compute — multi-input)* A student has OPT ending in 18 weeks, 15 unemployment days used, is STEM-eligible but has not yet filed the extension, and is evaluating a role whose typical process runs 14 weeks. Compute whether the factor is 0, near 1, or somewhere between — and identify what single action would most improve the student's timeline position before applying.
   *Tests: applying the factor components; identifying STEM extension filing as a runway-widening action.*
   *Difficulty: Medium*

5. *(Analyze — system behavior)* A student enters their authorization end date incorrectly — they enter a date three weeks later than the actual end. The factor comes back at 0.7 instead of 0. Trace the downstream consequences: what decisions does the 0.7 produce that the correct 0 would have prevented?
   *Tests: understanding that factor accuracy depends entirely on input accuracy; asymmetric cost of optimistic errors.*
   *Difficulty: Medium*

6. *(Evaluate — decision)* A role has a timeline factor of 0.3. The sponsorship tier is Proven, the fit is strong, and the liveness score is high. Make the case for applying and the case for skipping, then state which you would choose and what additional information would change the decision.
   *Tests: using the factor as one input in a multi-factor decision; identifying accelerated process as the key unknown.*
   *Difficulty: Medium*

**Synthesis**

7. *(Integrate — cross-chapter)* A student's Chapter 7 shortlist has twelve Proven-tier companies. After running the timeline factor, three are skip-regardless. Of the remaining nine, four have factors below 0.5. Using the freed-time logic from Chapter 2, describe how the factor output reshapes the student's week — which activities expand, which contract, and why the three hard drops are actually time gains.
   *Tests: connecting timeline gating to the time-budget logic of Chapter 2; treating skips as resource releases.*
   *Difficulty: High*

8. *(Diagnose — edge case)* A student near the end of their authorization receives an informal signal from a hiring manager that "we can move very fast if we want to." The role's timeline factor, computed from the company's historical process, is 0. Should the student apply? Walk through the reasoning, including what the factor can and cannot know, and what the student would need to verify before treating the informal signal as actionable.
   *Tests: limits of historical estimates; understanding what human judgment must add to the factor's output.*
   *Difficulty: High*

**Challenge**

9. *(Design — open-ended)* The current factor uses a single "expected time-to-start" estimate and a single buffer target. Propose an extension that would handle uncertainty in process length — for example, a probability distribution over possible process lengths rather than a point estimate. Describe what inputs the extension would require, how the factor output would change, and what the tradeoff is between precision and usability for a student managing twelve targets simultaneously.
   *Tests: thinking about uncertainty quantification; the design tradeoff between model sophistication and practical use.*
   *Difficulty: High/Open-ended*

[^opt]: F-1 post-completion OPT: max 90 aggregate days of unemployment (150 with STEM OPT extension); exceeding it terminates the record with no grace period. USCIS Policy Manual, Vol. 2, Part F, Ch. 5: https://www.uscis.gov/policy-manual/volume-2-part-f-chapter-5
# Chapter 11 — The Bayesian Role Scorer
*The constraint unique to you dominates the factor everyone told you was supreme.*

Start with the sentence. "Google is a great company, so I should apply." It is the most natural sentence in a job search, and it is wrong in a specific, costly way. Great by what measure, and for whom? For a candidate who needs visa sponsorship, "great company" and "good target" are two different questions, and conflating them is how the eight-hour applicant from Chapter 2 spent a month applying to firms that would never sponsor the role. This chapter replaces that sentence with arithmetic. And the arithmetic, for a non-sponsor, says no — however great the company.

I want to be honest about what that arithmetic is going to cost you emotionally, because it will fight your instincts in a specific place. The chapter demotes *fit* — the thing you have been told your entire life is what matters in a job search — below a constraint most candidates never put in the equation at all. The demotion is not an error in the math. It is the math doing exactly what it should.

## What the scorer is and what it takes as input

The Bayesian Role Scorer is the decision core of the pipeline. Everything built in the preceding chapters converges here. Sponsorship probability and tier (Chapter 7), liveness (Chapter 8), role quality and occupation code (Chapter 9), your timeline and the start-date clock (Chapter 10) — each of those chapters produced a number. This chapter combines them.

The new ingredient is fit: the probability that you are actually a match for this specific role, estimated by comparing your CV against the job description. I want to name this clearly before we go further: fit is a model judgment. It is not a record. It is not a verified fact from a government database. It is a language model comparing two documents and returning a probability. That label — *model judgment* — matters, and it will appear attached to fit throughout this chapter, because a composite that hides where its components came from is exactly the fluent-but-ungrounded artifact Chapter 1 taught you to distrust.

With all four inputs in hand, the composite takes this form:

**Composite ≈ P(sponsorship) × 0.35 + P(fit | CV, JD) × 0.30 + [other weighted factors]**

— the whole expression multiplied by a liveness factor and by a timeline factor, with a decision threshold near 0.3 that maps the composite to one of three recommendations: **Apply**, **Consider**, or **Skip**.[^weights]

There are three design decisions baked into this expression that are worth understanding from first principles, because each one will produce a recommendation that surprises you until you see the reasoning underneath it.

## Why sponsorship is weighted highest

Sponsorship carries a weight of 0.35 — above fit at 0.30. The question is why.

Weights in a scoring system should reflect which constraint is most binding for the specific person the system is built for. For a domestic applicant, sponsorship isn't a question. Fit dominates, because fit is the thing that will determine whether you get the offer. But for an international student, sponsorship is the constraint that silently kills the most applications — not because the candidate was unqualified, but because the company never sponsored in the first place and the candidate never knew to check. The application went in, the résumé cleared the ATS, and then something in the process stopped moving. Sponsorship was the reason. It is never written on a rejection email.

So the weighting is not a claim that sponsorship matters more than competence in the world. It is a claim that, for you, it is the factor most likely to cause an invisible rejection — and invisible rejections are the ones most worth preventing at the top of the funnel, before time is spent.

## Why liveness and timeline are multipliers, not addends

Fit and sponsorship are *votes*. They contribute proportionally to the composite. A higher sponsorship probability raises the score; a lower one lowers it. The contribution is graduated.

Liveness and timeline are different in kind. They are *gates*. A ghost posting — liveness approaching zero — makes the composite approach zero regardless of how strong the sponsorship and fit scores are. A timeline you cannot meet — start date constraints that make the role impossible — does the same. No amount of fit or sponsorship can carry a role through a gate that is closed.

This is the math expressing a truth about the job search, not imposing a rule on top of it. A perfect role at a sponsoring company is worth nothing if the posting is fiction or you cannot start in time. The multiplicative structure is the honest description of that reality.

## The worked case — one posting, all four factors traced

Let me make the composite concrete. A live posting at the Cambridge biotech from Chapter 7 — Proven tier, data role, our STEM-eligible graduate.

P(sponsorship) ≈ 0.9. *Source: LCA and H-1B records from Chapter 7.* This is a record, not a judgment.

P(fit | CV, JD) ≈ 0.7. *Source: model judgment, CV compared to the job description.* This is a judgment, labeled as such.

Liveness ≈ 1. *Source: ATS signals from Chapter 8.* The posting passed all five checks.

Timeline factor ≈ 0.85. *Source: the reader's OPT expiration and estimated processing window from Chapter 10.*

High sponsorship — the dominant term — multiplied by reasonable fit, with a live posting and comfortable timeline. The composite lands well above threshold. The recommendation is **Apply**.

Now the contrast. The same graduate. The same fit of 0.7. The same liveness and timeline. Applied to the household-name non-sponsor: P(sponsorship) ≈ 0. The dominant term — sponsorship at 0.35 weight — contributes almost nothing. No amount of fit rescues it. The composite falls below threshold. The recommendation is **Skip**.

The candidate did not get worse. The company did not get less impressive. The binding constraint changed, and the weighting surfaced it. That is the scorer's job.

<!-- → [TABLE: Two-role comparison showing Cambridge biotech vs. household-name non-sponsor across all four factors: sponsorship probability, fit score, liveness, timeline factor. Final rows: composite score, recommendation. Caption: "Same candidate, same fit — the dominant term (sponsorship) determines the outcome."] -->

## The three-way recommendation and when to override

**Apply** means the composite is above threshold and sponsorship and timeline are both healthy. This is the role that earns the targeted two hours of focused application work from Chapter 2.

**Consider** means the composite is near threshold, or strong on most factors with one soft spot — a Likely sponsorship tier rather than Proven, for instance. Apply only if this role beats your other Considers and you have buffer in your timeline.

**Skip** means the composite is below threshold, or zeroed by liveness or timeline. The recommendation is not that the company is bad. It is that your time, on a finite clock, is better spent elsewhere.

And then there is **Override** — the recommendation the system will not give you, but that you can give yourself. If you hold private information the data cannot — the hiring manager is a contact who told you directly they're actively interviewing, or the company just quietly started sponsoring last month and the LCA record hasn't caught up — you can override the scorer. But the discipline is this: write down what you knew that the scorer didn't. An override with a documented reason is a legitimate correction. An override without one is just ignoring the math because you like the company.

<!-- → [INFOGRAPHIC: Four-quadrant grid. X-axis: sponsorship probability (low → high). Y-axis: fit score (low → high). Regions labeled: top-right = Apply, top-left and bottom-right = Consider, bottom-left = Skip. Overlay: two data points for the worked example (Cambridge biotech = Apply zone, non-sponsor = Skip zone despite identical Y position). Caption: "The Apply/Consider/Skip regions show why fit alone doesn't determine the recommendation — the sponsorship axis moves you horizontally, not vertically."] -->

## The cautionary mirror — when scoring goes wrong

A different company built a hiring-match score by training on real managers' past decisions. The system learned to replicate those decisions, including the biases embedded in them — treating "what we did before" as "what is correct." A lawsuit (*Kistler v. Eightfold*) now asks a court to require what good scoring should have demanded from the start: disclose the score, allow disputes, fix the audit.[^eightfold]

Notice what separates that system from this one. The Eightfold scorer learned from opaque history; its weights are unknown even to the company that built it. This scorer's weights are stated — sponsorship 0.35, fit 0.30 — and each factor traces back to a named source. You can look at a recommendation and see exactly why it said what it said.

A composite score is a powerful tool and a dangerous one. The safety is not the math. It is the auditability. If you ever cannot explain why a role scored what it did — tracing each term to its source — distrust the recommendation before you distrust your confusion.

<!-- → [TABLE: Two-column comparison: "This scorer" vs. "Eightfold-style scorer." Rows: weight source (stated vs. learned from history), factor sourcing (explicit vs. opaque), auditability (can trace each term vs. cannot), failure mode (bad input laundered into confident output vs. bias laundered into confident output). Caption: "The safety of a composite score is not the math — it's whether you can see why it said what it said."] -->

## What the machine could not know

The composite knows four numbers. It cannot know that the "0.7 fit" undersells you because your one unusual project is exactly what this team needs and no keyword in the job description captured it. It cannot know that a company scored Skip just began sponsoring last month. It cannot know that you would thrive at a lower-scored role and burn out at a higher one.

The scorer's gift is that it makes the usual case explicit and defensible. Its danger is that a single confident number invites you to stop thinking. The discipline from Chapter 1 returns here in full: don't ask whether the score is impressive. Ask what it could not know, and whether you hold any of that knowledge. The score reduces uncertainty. It does not eliminate it — and pretending otherwise is the specific error that makes composite scores harmful rather than useful.

## Where this leaves you

The score says Apply. You know why it says Apply, term by term, source by source. The posting is real, the company sponsors, the fit is reasonable, and the clock is not against you.

What the scorer cannot do is write the application. And for an international candidate, how you frame your work authorization is where strong candidates get rejected for reasons that have nothing to do with their ability. The chapter that follows is about that problem. You earned the application. Now you have to write it.

---

## Exercises

**Warm-up**

1. *(Recall, easy)* Name the four inputs to the Bayesian Role Scorer and identify the source type for each — record, model judgment, or your own input. Why does labeling the source type matter for trusting the recommendation?
   *Tests whether you understand the auditability requirement as a design principle, not a paperwork step.*

2. *(Recall, easy)* Explain the difference between a weighted vote and a multiplier gate in the composite formula. Give one example of each from the scorer's four factors and explain what it means in practice when a gate approaches zero.
   *Tests the structural distinction between how sponsorship/fit contribute versus how liveness/timeline contribute.*

3. *(Identify, easy)* Why is sponsorship weighted at 0.35 — above fit at 0.30 — for an international student? Write the reasoning in one paragraph. Then explain whether the same weighting would be correct for a domestic applicant.
   *Tests whether you understand the weights as context-specific design decisions, not universal claims about what matters.*

**Application**

4. *(Apply, moderate)* Score five real postings from your target list using the four factors. For each posting, label every factor by source type (record, model judgment, your input) and write the recommendation. For at least one posting, show the arithmetic that drove the recommendation.
   *Tests the transition from understanding the framework to running it on real data.*

5. *(Analyze, moderate)* Take one posting where the scorer recommends Skip but your instinct says Apply. Work through the composite term by term and identify which factor is driving the gap between the score and your intuition. If you override, write down exactly what you know that the data does not.
   *Tests the override discipline and forces explicit reasoning about the conflict between score and instinct.*

6. *(Analyze, moderate)* Find a posting that would score well on fit (P(fit | CV, JD) ≥ 0.7) but poorly on sponsorship (P(sponsorship) ≤ 0.2). Compute the composite and explain, term by term, why the recommendation is what it is. Then explain this result to the version of yourself that said "Google is a great company, so I should apply."
   *Tests the central inversion of the chapter — fit cannot rescue a non-sponsor.*

**Synthesis**

7. *(Synthesize, harder)* The chapter argues that auditability — being able to trace every factor to its source — is the actual safety property of a composite scorer. Construct a concrete scenario in which a non-auditable composite score could harm a candidate. Then describe one specific design change to the scorer that would improve auditability without changing the weights.
   *Tests whether you can reason about the failure modes of composite scoring, not just the happy path.*

8. *(Synthesize, harder)* The fit factor is explicitly labeled a model judgment. Describe two specific ways the fit score could be systematically wrong — not just noisy, but biased in a consistent direction — and explain what the downstream effect on the Apply/Consider/Skip recommendation would be in each case. What check could you run to detect the error?
   *Tests adversarial reasoning about the weakest term in the composite.*

**Challenge**

9. *(Evaluate, open-ended)* The scorer uses fixed weights (sponsorship 0.35, fit 0.30). Design a calibration study — using only data you could collect during an actual job search — that would tell you whether those weights are correctly specified for your situation, and describe how you would update them if the study showed they were off. What would "correctly specified" even mean, given that you can't observe counterfactuals?
   *Tests whether you can think about the scorer's own calibration as an empirical question.*

[^weights]: Composite form and weights (sponsorship ×0.35, fit ×0.30, liveness and timeline as multipliers, decision threshold ≈0.3) from the system design document (Component 3, Bayesian Role Scorer). **[verify]** — confirm the exact composite expression and per-tier thresholds before publication.

[^eightfold]: Eightfold AI's match score learning manager bias, and *Kistler v. Eightfold* (FCRA: disclose the score, allow disputes, fix the audit), from "The Eightfold AI Match Score" (N. Bear Brown). **[verify]** the litigation specifics before publication.
# Chapter 12 — The OPT Framing Generator

<!-- voice-anchored: root style/VOICE.md. Anatomy: TIKTOC Part 10.
     Sourced from SDD Component 4, plain-summary, CHAPTER-RESEARCH-MAP. Ethics-sensitive (TIKTOC Risk 3).
     Draft. Never published. Hard rule: never misrepresent authorization. -->

Here is what happens in the first screen. A recruiter sees "international student" and a set of associations fires before a single question gets asked: sponsorship, cost, legal risk, delay. The candidate is filtered out. Not for their ability. Not for anything true. Because in the OPT and STEM-OPT window, none of those associations are accurate. The candidate is already authorized to work in the United States. They need no immediate sponsorship. They actually save the employer money. The candidate lost the role not to a competitor but to a misunderstanding they did nothing to correct — and in many cases didn't know they could.

This is a framing problem, and it has a solution. The solution is not to obscure your status. It is to present the accurate facts in the order and language that gives the person reading them the best chance of understanding what is actually true. What is actually true happens to be good news for the employer. Most candidates never say it.

---

Start with the fact most candidates can state but almost none deploy. Students on F-1 status working under OPT are generally exempt from FICA taxes — Social Security and Medicare — for the duration of the OPT period. The employer is also exempt from the matching contribution, which runs to roughly seven and a half percent of wages.[^fica] Hiring an OPT candidate is, for that window, cheaper than hiring an equivalent domestic worker. Not more expensive. Cheaper. The assumption in the first screen is not just wrong — it is backwards. And the candidate who says this clearly, in a first written contact, has changed the entire frame of the conversation.

That is the core fact. Everything else in this chapter is about when and how to say it.

---

The answer depends on who is reading it, which is why the chapter rests on the sponsorship tier from Chapter 7. A company that has sponsored dozens of H-1B visas understands OPT. A company with no sponsorship history may not know the acronym exists. Calibrating what you say to the audience's existing knowledge is not evasion — it is competent communication. The same true information can land as reassuring or confusing depending on the vocabulary you use to deliver it.

The tier ladder works as follows.

For a **Proven** employer — one that sponsors and knows the terrain — state your authorization directly. They understand OPT, they know the H-1B timeline, and clarity is an asset. Write it plainly: authorized to work in the U.S. on STEM OPT, familiar with the path forward. No softening needed. Softening would actually signal that you're uncertain about your own status.

For a **Likely** employer — some sponsorship history, but possibly not fluent in the details — lead with work authorization and the FICA benefit without leading with the acronym. The sentence that works is something like: "I'm authorized to work in the U.S. and, as an OPT employee, I'm FICA-exempt — a roughly seven-and-a-half-percent payroll saving for the coming period." Authorization first, benefit second, acronym explained rather than assumed. This defuses the opening-screen assumption before it can form.

For an **Unknown** employer — no signal either way — the written application says nothing about visa status. This is not concealment; it is timing. The first screen is the wrong place to raise a topic the employer may misread without context. Your materials sell your fit. When authorization comes up in an interview — and it will — you explain OPT, the FICA exemption, and the timeline in a conversation where you can answer questions as they arise and correct misreadings in real time. Paper cannot do that. You can.

The logic underlying the ladder is one idea: **disclose in proportion to the audience's understanding.** Where they understand OPT, be direct. Where they half-understand, lead with the benefit. Where they don't understand and have given no signal, let it surface in conversation. What never changes across the ladder is the hard rule: framing is accurate information presented strategically. It is never fabricated credentials, invented metrics, or misrepresented status. The moment a framing requires you to state something untrue, or to deny your authorization when directly asked, the tool has failed and you stop.

The line between strategy and misrepresentation is not subtle once you look at it directly. "Authorized to work in the U.S." is true and leads with the relevant fact. "I don't anticipate any issues with work authorization" is fine if you believe it. "I'm a permanent resident" is fraud if you aren't. The tool lives entirely on one side of that line. It has no use on the other side, and it will not help you cross it.

---

The table below summarizes the rules in compact form:

| Tier | Visa mention in written materials? | Lead with | Hard rule |
|---|---|---|---|
| Proven | Yes, direct | "Authorized; I/we know the OPT→H-1B path" | Never overstate the timeline you can offer |
| Likely | Yes, framed | "Authorized to work + FICA-exempt (~7.65% saving)" | Never imply you need no future sponsorship if you will |
| Unknown | No (initial) | Your fit; visa handled in interview | Never conceal authorization if directly asked |
| Avoid | — | (no materials) | — |

The hard rule cuts symmetrically. You do not over-claim — no implying permanent authorization you don't have, no stretching the OPT clock beyond its actual dates. And you do not deny or hide when directly asked. Strategic timing of true information is the entire toolkit. A false impression is not a variant of the toolkit. It is a different thing entirely.

---

What the generator cannot do is also worth stating plainly. It knows the sponsorship tier and the general OPT facts. It cannot know that the specific recruiter you're writing to was themselves an international student and will respond best to total directness regardless of tier. It cannot know that an Unknown-tier company was burned by a visa timeline problem last year and will ask about work authorization in the first email no matter what your materials say. It cannot make the ethical call for you in the gray moment when a framing that is technically accurate might leave a false impression in a careful reader's mind.

Framing is a starting calibration. The actual human across the table — and your willingness to hold the honesty line when it would be easy not to — is irreducibly yours to manage. The generator gets you to the conversation. What you do in it is not automatable.

This chapter also requires a legal and ethics reviewer before publication. The disclosure rules here touch employment and immigration law, and the hard rule against misrepresentation is not negotiable regardless of any framing suggestion the generator produces.[^ethics]

## LLM Exercises

1. **(Create) Three framings.** Generate visa framing for one real role at each of the three material-producing tiers (Proven, Likely, Unknown). Keep every claim true.
2. **(Evaluate) Catch the crossing.** Take a framing — yours or a provided one — that has crossed from strategic into misrepresentation. Identify the exact phrase that crosses the line and rewrite it to be both honest and effective.
3. **(Understand) Explain FICA in one sentence.** Write the FICA-exemption benefit as you would say it to a non-expert hiring manager — accurate, concrete, and not jargon.

## Key terms

- **Framing:** presenting accurate information strategically, calibrated to the audience's understanding — never fabrication.
- **FICA exemption:** OPT employees are generally exempt from Social Security and Medicare tax, saving the employer roughly seven and a half percent for the period — a real hiring benefit.
- **Disclosure-by-tier:** direct for Proven, benefit-led for Likely, interview-deferred for Unknown.
- **The hard rule:** never fabricate credentials, invent metrics, or misrepresent status; never deny authorization when asked.

## Run-log prompt

Record, per application, the tier, the framing approach used, and a one-line confirmation that every claim is accurate and no status was misrepresented.

[^fica]: F-1/OPT students are generally exempt from FICA (Social Security and Medicare) taxes, removing the employer's matching ~7.65% for the OPT period. Stated across the project's plain-summary and résumé/3-3-2 essays. **[verify]** against IRS guidance (e.g., IRS Publication 519 / FICA exemption for F-1) before publication.

[^ethics]: This chapter requires a legal/ethics review owner before publication (TIKTOC Risk 3 / Open Question 6). The hard rule against misrepresentation is non-negotiable and overrides any framing suggestion.
# Chapter 13 — Resumes That Survive the Filter
*The first reader doesn't care how it looks.*

There is a particular kind of effort that feels productive but costs you exactly what you spent it on. A candidate spends a weekend on a résumé. Two columns, a sidebar with tasteful skill bars, a small icon next to each section header, the name set large in a header graphic. It is the best-looking document they have ever made. They submit it to forty companies. Most reject it before a human opens it — not because the content was weak, but because the applicant-tracking system that read it first saw a scrambled wall of text. The two columns interleaved into nonsense. The skill bars, rendered as graphics, produced no text at all. The name, trapped in an image, was simply absent. The parser could not find a job title. So it scored the candidate as unqualified for everything, and the beautiful résumé disappeared.

This is not a corner case. By 2025, roughly 82% of companies screened résumés with software, and about one in five candidates were auto-rejected with no human review.[^screening] The first reader of your résumé is a parser. The parser does not care that the document is beautiful. It cares whether it can extract structured text. A résumé a human would admire and a machine cannot read is a résumé no human will ever see.

<!-- → [DIAGRAM: two parallel paths from "Submit résumé" — left path labeled "ATS-parseable": document → parser extracts name/title/dates cleanly → human review → interview; right path labeled "Designed layout": document → parser sees scrambled text or nothing → auto-reject → no human ever opens it; the fork happens before any human judgment] -->

I want to be precise about what this means, because the instinct is to fight it. "A distinctive design will make me stand out." Against a human, sometimes — if the human ever gets there. Against the parser that reads first, a distinctive design is how you disappear. Standing out is the job of your content and your portfolio. The résumé's job is narrower and absolute: pass the parser, then say something true and specific to the human behind it. Those are two different tasks, and conflating them is what produces the beautiful invisible résumé.

---

The pipeline this chapter rests on is `scripts/resumes/`, whose core is `generate-pdf.mjs`: a script that takes a Markdown CV and renders it to a PDF through Playwright/Chromium using a resume-safe rendering path — single-column, real text, standard section headings, no layout the parser will trip on. The whole point is that you author content in plain Markdown and let the pipeline produce a document engineered to parse. You do not hand-build a layout that looks good and reads as garbage. You write text, and the pipeline handles the document.

From the project root:

```bash
npm run resumes:pdf      # runs scripts/resumes/generate-pdf.mjs
```

The output is a rendered PDF. But the real check is not "does it look right." It is "does it parse." So there is a second, essential step: copy all text from the PDF — Ctrl/Cmd-A, Ctrl/Cmd-C — and paste it into a plain text editor. What you see pasted is roughly what the parser sees. If your name, titles, and dates come through as clean linear text in the right order, the document passes. If they scramble or vanish, you have found the break before a company did.

<!-- → [TABLE: two-column table showing "What you designed" vs. "What the parser extracted" for five common layout choices — two-column layout, skill bars as graphics, name in header image, dates in a table cell, section icons — right column shows the parser's view: interleaved text, blank, absent, misaligned, nothing] -->

That paste test is a practitioner heuristic, not a certificate. ATS systems vary. What one parses cleanly another may struggle with. But if text scrambles or disappears in plain paste, it will scramble or disappear in some meaningful fraction of the systems reading your application. The heuristic is conservative in the right direction: it tells you where the floor is, and the floor is what you need to be above.

---

Let me walk through what the test actually reveals, using a single CV rendered two ways.

The Markdown version, run through `resumes:pdf`: the PDF looks clean. Run the paste test. Name, contact information, each role's title and dates, the bullet content — all come through as ordered linear text. Section headings ("Experience," "Education," "Skills") survive as plain words, which are exactly the words parsers key on. The test passes.

The same content in a two-column designed template: paste it out. The left and right columns interleave line by line. "Data Analyst, 2023–2024" lands in the middle of an unrelated bullet from the other column. The skills section, rendered as little bars with labels, produces nothing — no text extracted at all. The parser reading that document cannot reliably locate a single job title. It has a name problem, a date problem, and a skill problem, all at once, and the human who might have found the candidate compelling never gets the chance to try.

<!-- → [CHART: side-by-side paste-test output for the same CV rendered two ways — left: clean linear text with name, title, dates, bullets in order; right: scrambled interleaving with missing sections marked in red; caption should note that the right-side output is what a typical two-column designed template actually produces when parsed] -->

The decision that follows from this is simple to state and genuinely uncomfortable to execute: ship the single-column rendered version; keep the pretty one for nothing, or for a human-only context like a portfolio site. The discomfort is real. The designed version *is* better-looking. But it is better-looking for a reader it will never reach.

---

Now let me say what the structures are that break parsers, because "don't use a fancy layout" is advice without traction until you know exactly which choices cause the problem.

**Multi-column layouts** are the most common failure mode. A parser reads text in document order, which in a two-column PDF is typically left-to-right across the full page width, not column by column. So the left column's first line and the right column's first line appear interleaved. This is not a subtle degradation — it makes the extracted text incoherent.

**Text in images** is the second. A name set in a header graphic is invisible to the parser. Literally absent. The parser cannot do OCR; it reads embedded text. If your name is an image, the parser does not know your name. If your section headers are icons rather than text characters, the parser does not see section structure.

**Tables used for layout** create extraction problems similar to columns: the parser linearizes the cells in ways that depend on the table's internal structure, not the visual arrangement you intended. Dates and job titles drift into wrong positions. A table is appropriate for genuinely tabular data; it is destructive when used to control visual layout.

**Skill bars and graphic elements** produce no text at all. They exist visually. To the parser, they are a gap.

The safe structures are their opposites: a single-column flow, real text characters for every piece of content that needs to be extracted, standard headings as plain words, dates in a consistent parseable format next to the roles they describe. These are not design constraints that prevent a good résumé. They are the constraints that ensure the résumé is read.

<!-- → [INFOGRAPHIC: a labeled résumé showing "safe zones" and "danger zones" — safe: single-column body text, standard section headers as text, dates as plain text adjacent to roles; danger: two-column layout, header graphic, skill bars, table-based layout, any text in an image; designed as a quick-reference visual a student can check their own document against] -->

---

There is something the pipeline cannot do, and I want to be direct about it.

The pipeline can guarantee a parseable document. It cannot know which of your true accomplishments will land with this hiring manager. It cannot tell you that your most parser-friendly bullet is also your most forgettable one. It cannot identify the phrase in your summary that makes a reader lean forward. ATS-safety is a floor — it ensures the human gets to read you at all. What you say once you are through the gate, and whether it is specific and true enough to earn the interview, is judgment the parser was never measuring.

The résumé, in a market where roughly 82% of companies run applications through software first, is not where you win. It is a gate you must not lose at. The winning moves — portfolio, proof of capability, demonstrated skill — happen elsewhere. The résumé's job is to get through the first filter intact and give the human on the other side something true and specific to respond to. Those are two requirements, and they are both necessary. An ATS-safe PDF with weak content still fails the human.

<!-- → [DIAGRAM: a two-stage model showing the résumé's job — Stage 1: "ATS filter" with the criterion "Can the parser find your name, title, and dates?" — Stage 2: "Human review" with the criterion "Is the content specific and true enough to earn a call?" — with an arrow between them labeled "What survives Stage 1 is the floor; Stage 2 is where content quality decides"] -->

Every component in the engine now works on its own: funding, sponsorship, liveness, role quality, timeline, scoring, framing, and a résumé that survives the filter. The next act stops handing you clean single tasks. It runs the whole engine — under real pressure, with a log — and that changes what you are doing in a way a single chapter cannot fully prepare you for.

---

## Exercises

**Warm-up**

1. *(Recall — single-concept)* Explain why a two-column PDF layout causes parser failures even when all the text is real text (not images). What is the parser actually doing when it reads a two-column document, and what does that produce?
   *Tests: understanding linearization as the mechanism, not just "columns are bad."*
   *Difficulty: Low*

2. *(Identify — single-concept)* Name four document structures that cause parsers to fail or produce scrambled output. For each, state what the parser sees instead of the intended content.
   *Tests: knowledge of the specific failure modes, not just the general principle.*
   *Difficulty: Low*

3. *(Apply — procedure)* Describe the paste-into-plain-text test step by step. What does it check? What does a passing result look like, and what does a failing result look like?
   *Tests: ability to execute and interpret the primary verification method.*
   *Difficulty: Low*

**Application**

4. *(Analyze — document)* A classmate sends you their résumé to review before they run `npm run resumes:pdf`. The document uses a two-column layout, has the candidate's name in a large header graphic, and uses icon symbols (not text) for section headers like Experience and Education. Before they render it, list every specific problem the paste test will likely reveal and explain the fix for each.
   *Tests: diagnosing multiple failure modes in a single document; pairing diagnosis with correction.*
   *Difficulty: Medium*

5. *(Evaluate — tradeoff)* A candidate argues they should keep a beautifully designed PDF for applications to design or creative roles because "those hiring managers will appreciate the aesthetic." Evaluate this argument. Under what specific conditions, if any, is it correct? What would need to be true about the application process for the designed version to be the right choice?
   *Tests: identifying the condition under which the design argument is valid — human-first review — vs. the much more common ATS-first case.*
   *Difficulty: Medium*

6. *(Apply — fix)* You have a CV section that lists technical skills as a visual grid: six cells arranged in two rows of three, each cell containing a skill name and a small logo. Rewrite this section in a form that passes the paste test without losing any of the skill information. Show the before structure and the after structure.
   *Tests: translating a visual layout element into parseable text without content loss.*
   *Difficulty: Medium*

**Synthesis**

7. *(Integrate — cross-chapter)* A student has a Proven-tier target company, a high timeline factor, and strong fit — all the signals from Chapters 7 through 10 point to applying. They run `npm run resumes:pdf`, do the paste test, and find their name is absent (it was in a header graphic) and two job titles scrambled. Walk through the decision: apply now with the broken résumé, delay to fix it, or something else? Include the timeline reasoning from Chapter 10 in your answer.
   *Tests: integrating ATS-safety as a go/no-go condition with the timeline urgency of Chapter 10.*
   *Difficulty: High*

8. *(Diagnose — system limits)* A student runs the paste test, sees clean linear text, and concludes their résumé will pass every ATS. Identify the specific conditions under which this conclusion is wrong — where the paste test gives a false pass — and explain what additional checks, if any, are available.
   *Tests: understanding the paste test as a strong heuristic with known limits, not a certificate.*
   *Difficulty: High*

**Challenge**

9. *(Design — open-ended)* The current pipeline converts Markdown to a single-column ATS-safe PDF. Propose a verification layer that would give a student more confidence than the paste test alone — for example, something that checks for specific parser-friendly conditions programmatically rather than by visual inspection. Describe what it would check, what output it would produce, and what it still could not guarantee.
   *Tests: thinking about what "ATS-safe" means as a verifiable property, not just a style guideline; understanding what any local check cannot know about a remote ATS.*
   *Difficulty: High/Open-ended*

[^screening]: ~82% of companies screen résumés with AI; ~21% auto-reject without human review — "The Collapse of the Traditional Résumé" (N. Bear Brown). **[verify]** against primary source.

[^proof]: The résumé-as-gate framing and the ~56% validated-AI-skill wage premium are from "The Collapse of the Traditional Résumé." **[verify]** the wage-premium figure before publication.
# Chapter 14 — Skills: Operating the Engine
*The fluent surface from Chapter 1 has come back, this time wearing the engine's own uniform.*

Here is a failure mode worth understanding before you run anything. You invoke a skill called `oferta` to evaluate a role. It returns a confident assessment: sponsorship looks strong, fit is solid, the composite is above threshold, you should apply. The output reads exactly like the verified findings you've trusted all book — sourced factors, labeled judgments, a traceable recommendation. But under the hood, something has changed. This run never called the sponsorship pipeline. It never read an audit. It asked a language model what it thought and dressed the guess in the format of a finding. You can't tell from the output. That's the whole danger.

The difference between a skill that *runs a script and reads an audit* and a skill that *quietly becomes a chat prompt* is the difference between the entire method working and the entire method failing silently. This chapter is about telling them apart — not once, but every time you run the engine.

## What a skill is

The engine's runtime lives in a directory called `skills/`. A skill is a named operation you invoke, and each one declares what scripts it calls, what data it reads, and what it logs. The declaration is not decorative. It is the thing you verify. A skill that calls no scripts and reads no audits is producing model judgment, not findings — and the output format will not tell you which one you're looking at.

Every skill opens by loading `skills/_shared.md`, the contract from Chapter 3. The contract is supposed to make the runtime honest by construction: every output labeled, every source named, every judgment flagged. Your job is to confirm, run by run, that it actually is.

The skills split into two groups, and understanding the split is the chapter's load-bearing insight.

**Active skills** are the ones that do verified work. `scan` detects the ATS and pulls the company's current postings. `pipeline` runs the scoring pass — sponsorship, fit, liveness, timeline — against the pulled data. `oferta` assembles the four factors into the composite from Chapter 11 and returns a sourced Apply/Consider/Skip recommendation. `tracker` logs decisions across the search (Chapter 15). `pdf` renders the ATS-safe résumé (Chapter 13). These skills call real scripts. They read real audits. Their outputs are findings.

**Draft and helper skills** are scaffolds — `apply`, `contacto`, `deep`, `followup`, `interview-prep`, `ofertas`, `project`, `training`, and others. They can be useful. But until you have confirmed, on a specific run, that a given draft skill calls scripts and writes a log, you treat its output as model judgment. Not worthless. Not a finding.

<!-- → [TABLE: Two-column table listing active skills vs. draft/helper skills. Active column: scan, pipeline, oferta, tracker, pdf — with one-line description of what each calls. Draft column: apply, contacto, deep, followup, interview-prep, ofertas, project, training — with the label "verify before trusting" for each. Caption: "The split is not permanent — a draft skill that you verify runs scripts becomes trustworthy. The taxonomy is about evidence, not hierarchy."] -->

The taxonomy is not a permanent ranking. A draft skill you have verified is trustworthy for that run. An active skill that has been edited without your knowledge might not be. The classification is always about what the skill did on this run, not what it is named.

## The loop

Operating the engine is one loop, repeated:

1. **Run** an active skill against a real target.
2. **Inspect** the output *and its provenance* — did it call the script? Is there an audit? Which numbers trace to records and which are labeled judgments?
3. **Record** the run in `RUN_LOG.md` — what you ran, what it returned, what you decided.

The loop is deliberately boring, and the boredom is the safety. Each pass leaves a trace. A decision made three weeks ago can be reconstructed, questioned, and updated when new information arrives. The moment you skip the inspect step — accepting a skill's output because it looks right, because the format is familiar, because the recommendation matches what you hoped — you've reopened the fluency trap. The surface was the danger in Chapter 1. It is still the danger in Chapter 14.

## A full sequence, end to end

Take one role from URL to evaluation:

```bash
# 1. scan — detect the ATS and pull the company's current postings
npm run ats:scan

# 2. pipeline — score the pulled roles
#    (run via the pipeline skill / auto-pipeline)

# 3. oferta — evaluate one role into a composite + Apply/Consider/Skip
#    (oferta skill; returns the sourced composite from Chapter 11)

# 4. verify — confirm the pipeline's data is internally consistent
npm run ats:verify
```

Four commands. Four links in a chain. What you read is the chain — not just the final recommendation, but each link's provenance. The scan result tells you which ATS was detected and which postings were pulled. The pipeline pass shows the four scored factors with their source labels. The `oferta` composite traces each term to its origin. The verification audit confirms the underlying data is consistent. A recommendation without its provenance is just an opinion in a formatted box.

## One target, fully operated

Let me make the loop concrete. A single role URL at a Likely-tier startup.

`scan` detects Lever and pulls the current posting. The posting is nine days old, description is specific, company hiring count has changed since last week — the liveness signal from Chapter 8 is clean.

The `pipeline` pass scores the role. Sponsorship probability from the LCA and H-1B join: 0.65 — Likely tier, not Proven. Fit from CV-vs-JD comparison: 0.72 — a model judgment, labeled as such. Liveness: live. Timeline factor: 0.8, from the reader's OPT expiration and estimated processing window.

`oferta` assembles the composite. Sponsorship at Likely (0.65) carries less weight than Proven (0.9) would. Fit is reasonable. The multipliers hold. The composite lands above threshold but not comfortably — the recommendation is **Consider**, not Apply.

`ats:verify` runs. The data is internally consistent. No flag.

`RUN_LOG.md` gets one entry: the command sequence, the composite with each factor labeled by source, the recommendation, and a one-line decision: *Compare against other Considers before spending an application slot.*

That's the whole loop. What makes it different from just reading the recommendation is the inspect step — knowing that the sponsorship term is 0.65 not 0.9, knowing why the composite landed on Consider rather than Apply, knowing which factor would have to improve to push it across the threshold. The recommendation is the headline. The provenance is the argument.

<!-- → [DIAGRAM: Flow diagram showing scan → pipeline → oferta → verify as four sequential boxes, each with a "provenance checkpoint" annotation (e.g., "ATS detected, postings list," "four factors with source labels," "composite with traced terms," "consistency audit"). Arrow at the end pointing to RUN_LOG.md. Caption: "The chain is only as trustworthy as its weakest provenance link — the verify step confirms consistency, not correctness."] -->

## The failure that looks like success

The error that ends the method quietly: trusting a skill by its name rather than its behavior.

"It's called `oferta`, so it must be evaluating with real data." Names are labels. Behavior is evidence. A skill can be edited — by you, by a collaborator, by a future version of the system — so that it stops calling its script and starts generating plausible-sounding output from the model's priors. The output format stays the same. The sourced-factors layout stays the same. The Apply/Consider/Skip recommendation stays the same. Nothing in the presentation tells you that the sponsorship probability now comes from the model's sense of what a good biotech sponsorship probability should be rather than from an LCA record.

The inspect step is the only protection. On every run of every skill you plan to trust, you confirm: did it call the script? Is there an audit? Can I trace the sponsorship number to a record?

If you can't answer yes to those questions, the output is a model judgment. It may be useful. It may even be accurate. But it is not a finding, and you should not make a Skip or Apply decision on its basis.

<!-- → [TABLE: Decision matrix — three rows: "Active skill, provenance visible (script called, audit present)," "Draft/helper skill, or provenance absent," "Any skill whose output you can't trace." For each: treatment (finding / model judgment / distrust the output), action (record and act / useful for drafting, not for decisions / re-run with inspection). Caption: "The skill's name is not the evidence. The provenance is the evidence."] -->

## What the loop cannot do

The run-inspect-record loop guarantees you *can* see provenance. It cannot guarantee you will draw the right conclusion from what you see.

Today's scan might have hit a stale cache and returned a posting that closed yesterday — the data is real, but the world has moved. The fit score of 0.72 might be confidently wrong for a role where your unusual project background is exactly what the team needs and no keyword in the job description captured it. The timeline factor rests on an estimate of processing time that the system cannot verify against the actual adjudication queue.

The engine runs the components and surfaces the evidence. The decision about whether a given run is trustworthy enough to act on is yours, every time. Automation makes the loop fast. It does not make it self-policing. A method that runs itself without a human in the inspect step is not the method.

## The shape of what the book has built

This is the chapter where all five components run together for the first time. Sponsorship detection (Chapter 7), liveness classification (Chapter 8), role quality (Chapter 9), timeline (Chapter 10), the composite scorer (Chapter 11) — each one producing a number with a labeled source, each number flowing into the oferta composite, each composite going into the run log as a traceable decision.

The engine is not complicated. It is thorough. The sophistication is not in the architecture; it is in the habit of inspection. You can run the whole sequence in under ten minutes for a single role. What takes discipline is doing the inspect step every time instead of shortcutting to the recommendation because the format looks familiar.

Running the engine produces decisions. A decision you can't reconstruct is one you can't learn from — and learning from the search is the subject of what comes next.

---

## Exercises

**Warm-up**

1. *(Recall, easy)* Name the five active skills and describe in one sentence what each one does. Then name three draft/helper skills and explain what "verify before trusting" means in practice for each.
   *Tests whether you can articulate the active/draft distinction before applying it.*

2. *(Recall, easy)* List the three steps of the run-inspect-record loop. For each step, write one sentence describing what you are confirming and why skipping that step reopens the fluency trap.
   *Tests whether you understand the loop as a safety mechanism, not just an operating procedure.*

3. *(Identify, easy)* What is provenance, and why does a composite recommendation without it reduce to an opinion in a formatted box? Give one example from the `oferta` output of what provenance looks like and what its absence would look like.
   *Tests whether you can distinguish a finding from a well-formatted guess.*

**Application**

4. *(Apply, moderate)* Run a full `scan → pipeline → oferta → verify` sequence on one real target role. Log each step in `RUN_LOG.md` with the command, key output, and provenance. Write the final recommendation with each of its four factors labeled by source type.
   *Tests the transition from understanding the sequence to executing it on live data.*

5. *(Analyze, moderate)* Pick one draft or helper skill you haven't verified. Run it and inspect the output for provenance signals: did it call a script, is there an audit, can you trace any number to a record? Write your verdict — finding-grade or judgment-grade — and explain the specific evidence that drove the classification.
   *Tests the verify-before-trusting discipline on a skill that doesn't announce its status.*

6. *(Analyze, moderate)* Describe how you would detect that an active skill has drifted — stopped calling its script without announcing it. What would be present in a genuine active-skill run that would be absent in a drifted run? What is the earliest point in the inspect step where you would catch the failure?
   *Tests adversarial reasoning about skill drift as a realistic failure mode.*

**Synthesis**

7. *(Synthesize, harder)* The chapter argues that the run-inspect-record loop's safety comes from the inspect step, not from the automation. Construct a scenario in which the loop runs correctly — scripts called, audit present, log written — but produces a confidently wrong recommendation. Identify which component's input was bad, trace how the error propagated through the composite, and describe what the run log would and would not tell you about the failure.
   *Tests whether you understand the loop as necessary but not sufficient for correct decisions.*

8. *(Synthesize, harder)* The `skills/_shared.md` contract is supposed to make the runtime honest by construction. Describe two ways the contract could fail — not because it is written incorrectly, but because the runtime doesn't enforce it. For each failure, write the specific `RUN_LOG.md` entry that would expose the problem and the one you would see if you weren't inspecting carefully.
   *Tests whether you can reason about contract enforcement as a behavioral property, not just a textual property.*

**Challenge**

9. *(Evaluate, open-ended)* Design a lightweight audit protocol — taking no more than two minutes per run — that would reliably catch the three most likely failure modes of the run-inspect-record loop: skill drift, stale cache data, and a mislabeled model judgment treated as a record. For each failure mode, specify the exact check, the observable signal that indicates failure, and the corrective action. Then identify which of the three is hardest to catch and explain why.
   *Tests whether you can reason about the loop's failure surface as an engineering problem with practical constraints.*
# Chapter 15 — The Pipeline Tracker and the Skip Rate

<!-- voice-anchored: root style/VOICE.md. Anatomy: TIKTOC Part 10.
     Sourced from SDD Component 5, plain-summary (skip rate ≥50%, 3-3-2), skills/tracker.md,
     "The 3-3-2 Split" essay, CHAPTER-RESEARCH-MAP. Privacy note: data/ats/ files are private (DATA_CONTRACT). Draft. Never published. -->

Imagine running the entire engine — scanning, scoring, framing, applying — and keeping no record of any of it. You'd have no response rate. No way to know whether Proven-tier applications outperform Unknown-tier ones. No signal that three weeks in, you've quietly drifted back to eight hours of clicking Submit. You'd be flying with no instruments, feeling busy, learning nothing. The decisions would still happen; you just couldn't see whether any of them worked, or correct course when they didn't.

The tracker is the instrument panel. But the most important number on it is not the one most people expect.

---

The counterintuitive heart of this chapter is this: **the target is a skip rate of at least fifty percent.** Of the roles the engine evaluates, you should be deciding not to apply to at least half.

Sit with why that's the goal and not a failure. If you apply to nearly everything the engine surfaces, your filter is too loose — you've recreated spray-and-pray with extra steps, and the targeted two hours from Chapter 2 has swollen back toward eight. A high skip rate means the filter is doing real work: separating the few roles worth a day off your ninety-day clock from the many that aren't. The skip rate is the dial that tells you whether the reallocation principle is actually operating or has quietly collapsed.

The reflex to resist is feeling good about a low skip rate because "I'm applying to a lot of things." That feeling is the volume instinct wearing a tracker. Low skip rate is not productivity. It is the filter failing. If your skip rate is twenty percent and you feel busy and productive, that pairing is the warning sign — busy and unfiltered is exactly the state the whole book exists to end.

So the tracker reads in two directions. Skip rate well under fifty percent means the filter is too permissive, or you're overriding it constantly; you're back to volume. Skip rate close to a hundred percent means either your upstream targeting is bad — no good roles reaching the scorer — or your thresholds are set impossibly high; either way, the funnel needs attention upstream. Skip rate above fifty percent with a steady flow of applies and a rising per-tier response rate: the engine is working as designed.

The skip is not an absence in the log. It is a decision, and a tracker that logs only applications is missing half the data about how well the filter works.

---

The component that makes this legible is the Pipeline Tracker, the engine's fifth component, maintained through the `tracker` skill and analyzed with the patterns script:

```bash
# Maintain / update the decision log (tracker skill writes data/ats/applications.md)
npm run ats:scan        # feeds new postings into the pipeline for decisions
# tracker skill: log each decision (company, role, score, tier, timeline flag, outcome incl. skip)

# Analyze tracker/scan/pipeline data for patterns and the allocation summary
python scripts/ats/analyze-patterns.py
```

For every decision the engine produces — apply or skip — the tracker records the company and role, the composite score and tier, the timeline flag, the recommendation, and the outcome. The output of `analyze-patterns.py` is the daily allocation summary plus your skip rate and per-tier response rates. You read the skip rate first. It is the fastest signal that the method is or isn't operating.

A privacy note that belongs here before anything else: your tracker files — `data/ats/applications.md`, `pipeline.md`, scan history — contain your real targets and real activity. They are private, never committed or shared without a privacy review. This is a hard rule that becomes load-bearing in Chapter 16.

---

Consider a week of actual tracker data: thirty roles evaluated, seventeen skipped, thirteen applied, nine of the thirteen in Proven or Likely tier. Skip rate is seventeen over thirty — fifty-seven percent. Healthy: the filter is doing real work. Early response data shows Proven-tier applications drawing replies at several times the rate of the few Unknown-tier ones, which is evidence that the tiering is predictive rather than decorative. The allocation summary, though, shows apply hours creeping to three and a half per day while networking has dipped — a drift warning that the tracker caught before a full week was gone.

The right response to that picture: keep the thresholds, because the skip rate is healthy, but reclaim an hour from applying back to networking next week. That is the 3-3-2 decision rule operating on real data rather than on principle.

The limit is equally worth stating. Early in the search, per-tier response samples are tiny and noisy — a three-application "trend" is not a trend. And the skip rate is a process metric, not an outcome metric. A healthy skip rate with zero responses still means something is wrong; it just means something upstream is wrong — bad targeting, weak materials — not that the filter itself has failed. The tracker measures discipline and targeting quality. It cannot conjure offers, and it cannot tell the difference between a targeting failure and a sector-wide hiring freeze. The numbers look identical. You read them in the context of a market the tracker can't see.

---

The decision rules for reading your own skip rate are compact enough to state directly:

Below forty percent is too loose. Trust the scorer's skips; stop overriding to apply. Between forty and fifty percent is borderline; watch whether your overrides are justified or habitual. Above fifty percent with steady applies and rising per-tier response rates is healthy — hold. Above roughly eighty-five percent, nearly everything skipped, means the funnel is starved or over-tight; fix upstream targeting in Chapters 6 and 5 or loosen the thresholds slightly.

The allocation summary closes the other loop. It shows how your hours actually split across apply, network, and portfolio — so the tracker doesn't just measure targeting quality, it catches allocation drift before a week has gone sideways. The skip rate tells you the filter is working. The allocation summary tells you that you are. You need both readings to know that the search is actually running the way Chapter 2 designed it.

## LLM Exercises

1. **(Apply) Log a week.** Record a week of decisions in the tracker — every Apply and every Skip with its score, tier, and timeline flag — and generate the daily allocation summary.
2. **(Evaluate) Diagnose your skip rate.** Compute your skip rate. Is it too low, too high, or healthy? Name the one change that moves it toward a working range, using the decision rules above.
3. **(Evaluate) Tier vs. response.** Once you have enough data, compare response rates across tiers. Does Proven outperform Unknown? Say what that implies about trusting the scorer.

## Key terms

- **Pipeline Tracker:** the component that logs every decision — score, tier, timeline flag, outcome, including skips.
- **Skip rate:** the share of evaluated roles you decide not to apply to; target ≥ 50% as evidence the filter works.
- **Daily allocation summary:** the read-out of how your hours split across apply / network / portfolio (3-3-2).
- **Process vs. outcome metric:** skip rate measures discipline and targeting quality; it must be read alongside response rate and market context.

## Run-log prompt

Record the week's skip rate, the per-tier response rates with sample sizes, the allocation summary, and the one adjustment you're making next week.
# Chapter 16 — The Build and the Honest Run
*You built a machine that is superhuman at execution precisely so you could spend your scarce attention on the questions it cannot reach.*

Think of an orchestra. Each musician can execute passages no conductor could play. But the conductor never touches an instrument. The conductor decides what the piece *means*, hears the wrong note before the score confirms it, and holds a hundred separate parts toward one intention. Remove the musicians and nothing gets played. Remove the conductor and you get a hundred fluent parts that don't add up to music.

That is the shape of building this engine. There is a part that belongs to the AI — scaffolding, schemas, scoring formulas, boilerplate, glue code, the structural logic of five components wired into one system. The AI is superhuman at this. Left to itself it produces clean, confident, internally consistent code in minutes. And there is a part that belongs to you: what your visa situation actually requires, whether the probability math makes sense given what you know, the domain knowledge the model cannot have, and the integration of five components into one system you will stake your job search — and your immigration status — on.[^boondoggle]

The whole book has been preparing you to be the conductor. This chapter is where you pick up the baton.

## How you build it

You don't ask the AI to "build a job-search engine." You conduct it through phases, each with a handoff condition — the precisely stated thing that must be true before the next phase begins.

**Phase one: foundation.** The directory layout, the data contract, the intake questions, the environment. The AI scaffolds the structure; you decide what your eight intake answers from Chapter 10 must constrain. These are first-class inputs, not setup trivia. Your OPT expiration date, your STEM eligibility, your field — the system that doesn't have those pinned is a system that can produce a confident recommendation about a role you can never legally start.

**Phase two: core skeleton.** The data structures and the five component stubs. The AI writes the schemas; you confirm they encode your situation. A schema that doesn't distinguish Proven from Likely sponsorship tiers, or that treats your timeline as a preference rather than a gate, is wrong in a way the AI cannot detect from the inside.

**Phase three: integration.** Wiring the five components into the composite scorer from Chapter 11 and the skills from Chapter 14. The AI connects the pieces; you verify that liveness and timeline act as multipliers — gates that zero the score — and not as weighted votes. This is the class of error that will look exactly like correct behavior. The code will run. The numbers will be in a plausible range. Only you know that a role expiring before you can start shouldn't score "Consider."

**Phase four: full feature build.** The pipelines — SEC, ATS, BLS — the framing generator, the résumé renderer. The AI builds each component; you verify each against its real dataset. "The SEC pipeline returns company funding records" is a verification you can run. "The SEC pipeline looks complete" is not.

**Phase five: hardening.** Error handling, the verification scripts, the audit trail. The AI implements; you decide what "correct" means for your search and what must never fail silently. A skill that stops calling its script and starts generating plausible output from the model's priors — the failure Chapter 14 opens with — is the thing hardening is designed to catch.

**Phase six: release.** The first real run.

<!-- → [DIAGRAM: Six build phases shown as a left-to-right sequence with labeled handoff conditions between phases. Each phase split into two rows: "AI executes" (top) and "You verify" (bottom). The gap between phases labeled "handoff condition — must be stated precisely before proceeding." Caption: "A handoff you can't state precisely is a phase you haven't actually finished."] -->

The handoff condition is the most important element of the whole build. "The scan returns real postings with provenance" is a handoff condition. "It looks done" is not. The places where builds go wrong are almost always places where a phase ended on a feeling rather than a test.

## The boundary, made operational

I want to be precise about where the line is, because this is where the abstract principle from Chapter 1 — execution versus judgment — becomes a checklist you can actually run.

The model can verify that code is internally consistent. It cannot verify that the code is grounded in the specific reality you are building it for. It will produce a sponsorship formula that compiles and a timeline factor that returns a number; it cannot know whether the weights match your binding constraint or whether the dates are yours. So the moves that remain irreducibly yours:

**Plausibility auditing** — reading the output and asking "could this be right?" before trusting the verification. The composite came back 0.7 for a non-sponsor. Chapter 11 says the dominant term should collapse to near zero when P(sponsorship) ≈ 0. Does 0.7 make sense? It doesn't. Catch it before it propagates.

**Problem formulation** — deciding what the engine is for, and re-engaging it when an audit finding changes the shape of the problem. The model builds what you specify; you remain responsible for whether the specification was right.

**Interpretive judgment** — supplying the meaning the model can't. An "Unknown" sponsorship tier is a coverage gap in the dataset, not a verdict on the company. A skipped role had a connection the data never saw. A fit score of 0.72 might undersell you for a role where your unusual background is precisely what the team needs and no keyword captured it.

**Orchestration** — holding all of it toward one end: a job, landed in time, honestly.

<!-- → [TABLE: Two-column table. Left column: "Give to the AI" — scaffolding, schemas, formula implementation, boilerplate, documentation drafts, glue code, anything where correctness is checkable. Right column: "Keep for yourself" — weight calibration, plausibility audits, Unknown-tier interpretation, privacy and honesty calls, final go/no-go on real decisions. Footer: "The test: can the model verify this against reality, or only against itself? If only against itself, it's yours."] -->

## The ethics gate

Before any first real run, two rules that are not optional:

**Privacy.** Your `data/ats/` files — applications, pipeline records, scan history — contain your real targets and real activity. Your environment may contain credentials. These files are private. Review for privacy and size before any commit, and never publish them. Building in public does not mean exposing your job search.[^privacy]

**Honesty.** Everything from Chapter 12 holds at the system level. Accurate framing, no fabricated credentials, no invented metrics, no misrepresented status. An engine that optimizes your search by shading the truth is the failure mode this book exists to prevent — fluency in the service of a false impression is still a false impression, and it is worse when it arrives in a polished format.

If a run would breach either gate, you don't run it. The ethics gate is the conductor's first responsibility, not an afterthought to the build.

## The first real run

Release is not a demo. It is the engine, running on your actual search:

```bash
# Stand up and verify the engine end to end
npm run ats:scan        # real postings from real companies
npm run ats:liveness    # classify them live/ghost
npm run ats:verify      # confirm pipeline data is consistent
# then: pipeline → oferta on real roles → tracker logs every decision
python scripts/ats/analyze-patterns.py   # skip rate + allocation summary
```

The output is a batch of real, logged decisions — Apply/Consider/Skip on actual roles, each factor sourced, each decision in the tracker, a skip rate you can read. Not a simulation. Not a walkthrough. The engine, applied to the search you are actually running.

When I ran the first batch, thirty roles came back with roughly 57 percent skipped. The Applies were concentrated in Proven and Likely tiers with beatable timelines. Each skip freed time that went toward the work no pipeline can do: reaching out, building the portfolio, following up on the connections the data never saw.

But before the batch ran, a plausibility audit caught something. A draft composite was treating the timeline factor as a weighted vote rather than a multiplier. A role that should have zeroed on the clock — the start date was past my OPT window — was scoring "Consider." The code ran. The number looked reasonable. It was wrong in exactly the way fluency hides: internally consistent, grounded in nothing.

Fixed. That is what plausibility auditing is for.

<!-- → [CHART: Horizontal bar chart showing one sample batch: 30 roles broken down into Apply (approx. 13%), Consider (approx. 30%), Skip (approx. 57%). Bars color-coded by sponsorship tier (Proven, Likely, Unknown, Non-sponsor). Caption: "A first real run on 30 roles — the skip rate isn't failure, it's the engine working. The time that doesn't go to ghost postings goes somewhere that matters."] -->

## What the machine could not know

The engine knows what it measured: funding records, government filings, ATS postings, occupation demand curves, your dates. It could not know that the founder of a skipped startup is your former lab partner. It could not know that its own fit score missed the one project that makes you right for a role where no keyword in the description captured it. It could not know that you would thrive at a lower-scored job and burn out at a higher one. It could not know whether staking your search on its math is wise — that judgment was never in the data.

This is not a limitation to work around. It is the design. You built a system that handles everything it can handle — reliably, repeatably, at scale — so that your scarce human attention is available for the things it cannot. The conductor doesn't play every instrument. The conductor hears the whole.

## The return

Return to the polished artifact from Chapter 1 — the clean recommendation that arrived in three confident seconds. You know now what to do with it. Don't ask whether it is impressive. Ask what would have to be true for it to be trusted. Ask what the machine could not know. Ask what you are now responsible for once the decision leaves the screen.

That question — *what am I now responsible for?* — is the one the whole book was climbing toward. The engine answers the questions it can answer. Everything it cannot is yours: the judgment, the stakes, the account you will give for the decision.

The search is live. The clock is running. Begin.

---

## Exercises

**Warm-up**

1. *(Recall, easy)* Name the six build phases and state a handoff condition for each — the specific, testable thing that must be true before the next phase begins. For at least two phases, explain why "it looks done" fails as a handoff condition.
   *Tests whether you understand the handoff condition as the load-bearing element of the build, not a documentation step.*

2. *(Recall, easy)* List the four irreducibly human moves — plausibility auditing, problem formulation, interpretive judgment, orchestration — and write one sentence describing what the AI cannot do in each case and why.
   *Tests whether you can articulate the Gru/Minion split before you're under build pressure.*

3. *(Identify, easy)* Explain the two rules at the ethics gate. For each one, describe one specific action during the build process that would violate it, and explain why the violation matters beyond the immediate run.
   *Tests whether you understand privacy and honesty as structural constraints, not afterthoughts.*

**Application**

4. *(Apply, moderate)* Build your engine through the first three phases — foundation, core skeleton, integration — and write the handoff condition you verified at each transition. For the integration phase, confirm that liveness and timeline act as multipliers. Show the specific output or test that verified it.
   *Tests the transition from understanding the phases to executing and verifying them.*

5. *(Analyze, moderate)* Before running the first real batch, perform a plausibility audit on the composite scorer. Take three roles and check whether each factor's contribution makes sense given what you know from Chapters 7–11. Identify one case where the output looked reasonable but was wrong, and trace the error to its source.
   *Tests the plausibility-auditing discipline as a behavioral practice, not a one-time check.*

6. *(Analyze, moderate)* Run `npm run ats:scan` and `npm run ats:liveness` on at least five real companies. Record the output with full provenance for each role (ATS detected, liveness classification, source of each signal). Identify one role where the liveness classification surprised you and explain what additional check resolved the ambiguity.
   *Tests the active-skill inspection habit from Chapter 14, applied at the first real run.*

**Synthesis**

7. *(Synthesize, harder)* The chapter argues that building the engine doesn't remove judgment — it relocates it from doing the work to deciding whether the work is right. Construct a scenario in which a fully built, correctly running engine produces a systematically wrong batch of recommendations. Identify what input or weight was miscalibrated, trace how the error propagated through all five components, and describe what a plausibility audit would have caught it and at which phase.
   *Tests whether you understand the engine's error surface as a design property, not just a runtime concern.*

8. *(Synthesize, harder)* The "what the machine could not know" account is not a disclaimer — it is the honest description of the search's residual uncertainty after the engine has done everything it can. Write the account for your own search: what does the engine measure, what does it miss, and what are you now responsible for that the data never touched?
   *Tests whether you can distinguish the engine's actual epistemic scope from its confident output.*

**Challenge**

9. *(Evaluate, open-ended)* The conductor metaphor — human orchestration of AI execution — implies that the conductor needs to hear when something is wrong before it becomes catastrophic. Design a monitoring protocol for a live, multi-week job search using this engine: what signals would tell you the engine has drifted from accurate to fluent, how often would you run the check, and what threshold would cause you to pause the search, re-audit the build, and re-verify the weights? Ground your answer in specific observable outputs the engine already produces.
   *Tests whether you can reason about the engine as a system with a maintenance requirement, not a one-time build.*

[^boondoggle]: The conductor model — Gru (human orchestration) / Minion (exact AI prompts), the Boondoggle Score, plausibility auditing, and the handoff condition — from `projects/the-reallocation-engine-boondoggle-score.md` and "Boondoggling: You Are the Conductor" (N. Bear Brown).

[^privacy]: Privacy constraint on `data/ats/applications.md`, `pipeline.md`, and scan history (review privacy and size before committing; never publish) from `DATA_CONTRACT.md` (TIKTOC Risk 1 — BLOCKER for any public build).
# Appendix — Fundamental Themes

<!-- voice-anchored: root style/VOICE.md. Appendix chapter synthesizing the recurring
     ideas across Chapters 1–16. Built 2026-06-02 (no prior 97-fundamenta-themes.md existed).
     Draft. Never published. -->

A textbook teaches one chapter at a time, but it is held together by a few ideas that appear and reappear under different names. This appendix names them. If you remember nothing else from *The Reallocation Engine*, remember these — they are the load-bearing beams, and every chapter is hung on at least one of them.

## 1. Fluency is not correctness

The book's first sentence and its last lesson. A polished artifact — clean code, a confident recommendation, a labeled chart — tells you nothing about whether it is *right*. Fluency is the surface of competence; correctness is a separate property that has to be checked.

*Where it appears:* the thesis of **Chapter 1** (the fluent take-home, the comprehension debt that opens up when you delegate the doing); the danger a skill poses when it "quietly turns into a chat prompt" (**Chapter 14**); the math error that looks reasonable and is wrong (**Chapter 16**).

## 2. The execution/judgment boundary

Work splits into two things AI has pulled apart: *execution* (producing the artifact) and *judgment* (deciding whether it should exist, whether it's right, what it leaves out). AI made execution nearly free and left judgment exactly as expensive. The whole engine exists to automate execution so your scarce attention can go to judgment.

*Where it appears:* defined in **Chapter 1**; made operational as Gru/Minion in **Chapter 16**; implicit every time a chapter ends with "what the machine could not know."

## 3. The verified-data contract

Run the script and read the audit before you prompt; never invent a count, a rate, or a coverage number. This is the rule that lets you trust a filter enough to *skip a real opportunity* on it.

*Where it appears:* stated in **Chapter 3**; enforced in every Act Two chapter (a number comes from a dataset or it doesn't stand); the reason skills must show provenance (**Chapter 14**).

## 4. Data claim vs. model judgment — label everything

For any sentence: could it have been produced by counting records? If yes, it's a data claim and must trace to a source. If no, it's a model judgment and must be *labeled* as one — never dressed as a fact. Fit (**Chapter 11**) and SOC classification (**Chapter 9**) are model judgments the book insists on labeling, because that is exactly where fluency sneaks back in.

## 5. The binding constraint dominates

Weights should reflect *which constraint is most binding for this specific reader.* For an international student, sponsorship — not fit — is the factor most likely to be the invisible reason for a rejection, so it gets the loudest vote (35%). And the clock is a hard constraint, so it isn't a vote at all.

*Where it appears:* the sponsorship weighting and "a perfect-fit application to a non-sponsor scores zero" (**Chapter 11**); the timeline factor of 0 that gates out a role no matter how good (**Chapter 10**).

## 6. Gates versus votes

Some factors are weighted preferences (sponsorship, fit); others are multipliers that can zero the whole score (liveness, timeline). Encoding a hard constraint as a gate rather than a vote is the math telling the truth: a ghost posting or an unbeatable clock isn't a small penalty, it's a disqualification.

*Where it appears:* the composite form in **Chapter 11**; the timeline multiplier in **Chapter 10**; liveness in **Chapter 8**.

## 7. Skip is a first-class action

Not applying is a decision, not a gap. The reallocation principle says effort should follow expected return, so the time a skip saves goes to the channels that actually produce hires (networking, portfolio) — and a healthy search *skips most of what it sees.*

*Where it appears:* the 3-3-2 allocation and the defense of a skip (**Chapter 2**); the ≥50% skip-rate health metric (**Chapter 15**); reallocating the time freed by a timeline-zero or non-sponsor (**Chapters 10, 9**).

## 8. The invisible-but-sponsoring company

Prestige is loud and the public record is quiet, so the record routinely ranks an unknown lab above a famous logo. The book's recurring case — the funded, sponsoring company you've never heard of — is the reward for reading the data instead of the billboards.

*Where it appears:* the funded firms job boards hide (**Chapter 6**); the backwards ranking the sponsorship scorer corrects (**Chapter 7**); the "Google is a great company" sentence the scorer overrules (**Chapter 11**).

## 9. Coverage and its gaps — Unknown is not Avoid

Verified data has holes. A company can sponsor and not appear in the window your data covers, or fail to match because its name is spelled three ways. So "Unknown" means *the record is silent*, not *they won't sponsor* — and you read the coverage number before trusting any absence.

*Where it appears:* entity resolution and the 38% of firms with no inferred domain (**Chapter 6**); the join coverage you check before trusting an Unknown tier (**Chapter 7**); the SOC match you confirm before reading the numbers hung off it (**Chapter 9**).

## 10. "What the machine could not know"

Every chapter ends here, and it is the point of the whole book. The data gives you the *usual* case; the exception lives in knowledge the data never had — a connection, a freeze, a project no keyword caught, a willingness to take a different path. Verified data is a floor that stops you building on fiction, then hands the situated judgment back to you.

*Where it appears:* literally, in every chapter's box; structurally, as the residue the engine is built to leave for the human.

## 11. Auditability is the real safety

A scoring system is dangerous not because it uses math but because the math can be opaque. The safety is not the formula — it's that you can see *why* a score is what it is. The book's scorer states its weights and sources its factors; the cautionary mirror (Eightfold, which learned managers' biases and disclosed nothing) shows the alternative.

*Where it appears:* the Eightfold contrast and "distrust the recommendation, not your confusion" (**Chapter 11**); provenance as the test for trusting a skill (**Chapter 14**); auditing the engine's own math (**Chapter 16**).

## 12. Honesty is a hard rule, not a tactic

Framing presents accurate information strategically; it never fabricates, misrepresents, or denies status when asked. Your search data is private and reviewed before any commit. An engine that optimizes by shading the truth is precisely the failure the book exists to prevent — fluency in the service of a false impression.

*Where it appears:* the disclosure-by-tier rules and the bright line against misrepresentation (**Chapter 12**); the privacy and honesty gates before any real run (**Chapter 16**).

## 13. The conductor and the orchestra

You are not the musician anymore; you are the conductor. The AI executes superhumanly; you decide what the piece means, hear the wrong note before the score confirms it, and hold all the parts toward one intention. Building the engine doesn't remove the judgment — it relocates it.

*Where it appears:* the Gru/Minion build model and the handoff condition (**Chapter 16**); the inversion from 90% execution to 90% judgment (**Chapter 1**).

---

**How to use this appendix.** When a chapter's mechanics blur, come back here and find the theme underneath — the SOC table, the sponsorship weights, and the skip rate are all the *same few ideas* wearing different clothes. The reader who finishes this book has not memorized five components and a dozen scripts. They have learned to distrust fluency, to ground decisions in data, to put the binding constraint in the math, and to keep for themselves the judgment the machine could never reach.

## Note on sources

This appendix synthesizes the chapters; it introduces no new facts. Every statistic, weight, and rule referenced here carries its citation or `[verify]` flag in the chapter where it first appears. The two recurring source debts to resolve before publication: the headline labor-market figures (54% via connections, ~56% AI-skill premium, ghost-job rates, ~7.65% FICA), and the sponsorship tier-set discrepancy (Proven/Likely/Unknown vs. +Avoid). Both are tracked in `CHAPTER-RESEARCH-MAP.md` and TIKTOC Risk 8.
---

## Acknowledgments

This rough draft acknowledges the readers, students, collaborators, reviewers, and AI-assisted production workflows that help turn a book from a directory of files into a usable learning object. Specific names should be added after manuscript review.

---

## About the Author

**Nik Bear Brown** is an Associate Teaching Professor in the College of Engineering at Northeastern University. He has taught artificial intelligence, computer science, statistics, applied mathematics, programming, visualization, web systems, game programming, and AI fluency across Northeastern, UCLA, Santa Monica College, ITT, and the Art Institutes Hollywood. His Ph.D. is in computer science from UCLA, with a major field in computational and systems biology and minor fields in artificial intelligence and statistics. He also holds a Master's in Information Design and Data Visualization and an MBA from Northeastern University.

[nikbearbrown.com](https://www.nikbearbrown.com) · [irreducibly.xyz](https://irreducibly.xyz) · [bearbrown.co](https://www.bearbrown.co/)

---

## Notes

Notes are organized by chapter in the production draft.

### Chapter 1

- Sources to be finalized during editorial review for "Introduction".

### Chapter 2

- Sources to be finalized during editorial review for "Chapter 1".


---

## References

A full bibliography will be compiled after fact-checking. Use a consistent citation style across the manuscript.

---

## No Index

This book is designed primarily for Kindle, online reading, and integration with **Medhavy** / **Medhavi**, the AI-powered intelligent textbook system. In those environments, search, links, adaptive navigation, glossary lookup, and generated study paths do more useful work than a static print index. A print index can be commissioned later if the book receives a print edition, but this draft intentionally omits one.

---

## Glossary

- **Key terms.** Definitions to be completed during final editorial pass.
