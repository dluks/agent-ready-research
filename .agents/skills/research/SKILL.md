---
name: research
description: Investigate a question against high-trust primary sources (papers, dataset documentation, official tool docs, source code) and save the findings as a cited Markdown note in the project. Use when the researcher wants a method, dataset, tool, or claim looked up, or wants reading legwork handed to a background agent.
---

Spin up a **background agent** to do the research, so you keep working while it reads.

Its job:

1. Investigate the question against **primary sources**: the paper that introduced the method, the dataset's own documentation or data paper, the official docs or source code of a tool. Follow every claim back to the source that owns it, and prefer those over a blog post or review that summarizes them.
2. Write the findings to a single Markdown file, citing each claim's source (DOI or URL, plus page, section, or version where it matters). Mark anything the sources leave unsettled as an open question.
3. Save it in `context/reading/` unless the project already keeps such notes elsewhere, and say where it went. If a finding settles a term or a decision, tell the researcher so it can go into `CONTEXT.md` or `context/decisions/`.
