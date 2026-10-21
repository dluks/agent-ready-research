---
name: research-grilling
description: Interview the researcher relentlessly about a research plan, study design, method, dataset, claim, interpretation, paper argument, or output. Use when the researcher wants to stress-test research before analysis or writing, or uses any grill trigger phrases.
---

Interview the researcher relentlessly until you reach a shared understanding. Map the research as a **design tree**: every decision (question, scope, data, method, validation, interpretation, output) branches into the decisions that hang off it.

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled: the questions you can ask _now_ without guessing at answers you haven't heard yet. Ask the whole frontier in one round: number each question and give your recommended answer or the tradeoff you see. Then wait for the researcher's answers before the next round.

Format a round like so:

```
❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>

---

❓ **Q2** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>
```

Word each question so "yes" accepts your recommended answer.

Each round the researcher answers reshapes the tree: settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier and ask the next round. A question whose answer depends on another question still open in this round belongs to a _later_ round.

Finding _facts_ is your job. When a frontier question needs a fact from the project (repository, `data/README.md`, notebooks, scripts, papers, outputs, decision records, or a quick check of the data itself), dispatch a sub-agent to find it, and look up anything you can before asking the researcher. Keep the round moving while it runs: a running lookup is an unsettled prerequisite, so only the questions downstream of it wait for the sub-agent to report. The _decisions_ are the researcher's: put each to them and wait.

The session is done when the frontier is empty: every branch of the design tree visited, nothing left silently assumed. Wait for the researcher to confirm you have reached a shared understanding before acting on it.
