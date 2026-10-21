---
name: handoff
description: Compact the current conversation into a handoff document for another agent session to pick up.
argument-hint: "What will the next session be used for?"
disable-model-invocation: true
---

Write a handoff document summarising the current conversation so a fresh agent can continue the work. Save it to the temporary directory of the researcher's OS (`$TMPDIR`, else `/tmp`; `%TEMP%` on Windows) and give the full path.

Include a "suggested skills" section in the document, naming which skills the next agent should call the Skill tool for.

Point to what the project already records instead of repeating it: `CONTEXT.md`, the lab notebook, plans, tasks, decision records, commits, and output paths. If the session produced results that belong in the lab notebook and are not there yet, say so in the handoff so the next agent records them.

Redact any sensitive information, such as credentials, API keys, unpublished sensitive data, or personal information about study participants.

If the researcher passed arguments, treat them as a description of what the next session will focus on and tailor the document accordingly.
