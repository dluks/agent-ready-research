---
name: lab-notebook
description: "Record work in a lab notebook so it is both a literal activity log and an efficient re-entry aid. Use when the agent is running experiments, debugging workflows, triaging jobs, or updating project state that must be recoverable later."
---

# Lab Notebook

## Optimize For Re-entry And Auditability

- A notebook should answer both:
  - what exactly happened?
  - what do we currently believe?
- Prefer one low-friction chronological record plus a sparse current-summary layer.
- Reuse the project's existing notebook pattern instead of inventing a new structure.

## Choose The Notebook Shape

- If the project already has a notebook, keep its location and shape. Check `AGENTS.md` for a pointer first.
- If not, create one lazily, the first time there is an entry worth recording:
  - **Single project**: one file, `context/lab-notebook.md`, with a short summary at the top and the chronology below it (the one-file pattern).
  - **Umbrella project**: a sparse summary at the root in `context/lab-notebook.md`, plus a detailed chronology inside the project you are working in, `projects/<name>/context/lab-notebook.md` (the two-layer pattern). If that project already keeps its own docs somewhere else (for example `docs/`), put the detailed layer there.
- After creating a notebook, add a one-line pointer to `AGENTS.md` that says where it lives and to use this skill for entries.
- Keep one detailed layer per line of work. A second equally detailed notebook splits the record.
- Default rule:
  - detailed layer: append literal work record, never rewrite earlier entries
  - summary layer: update only when the decision or current understanding changes

## When To Write An Entry

- after a meaningful experiment, analysis run, or pipeline run, whether it worked or not;
- when something fails or is ruled out, because negative results save the most time later;
- when an inference changes what you would do next;
- before ending a work session, so the next session can resume from the notebook alone.

The notebook records what was tried, what came of it, and what we now believe. Git records what changed in files, `context/decisions/` records settled choices, and `context/meetings/` records what was said. Link to those instead of copying them.

## Use This Entry Contract

For each meaningful experiment, debugging step, or job intervention, capture:

1. Question or goal.
2. Action taken.
3. Evidence:
   - commands, scripts, configs, paths, job IDs, artifacts, metrics.
4. Result:
   - what actually happened.
5. Conclusion:
   - the inference you are drawing, if any.
6. Inference confidence:
   - `low`, `medium`, or `high` when the entry is making a real inference.
7. Decision impact:
   - what changed in current understanding, or what the next step is.

## Update The Summary Sparingly

- Update the summary layer only when one of these changes:
  - current best explanation
  - current best branch or baseline
  - settled negative results
  - next discriminative check
  - success criterion or decision rule
- Do not rewrite the summary after every routine action.
- The summary should be short enough that a fresh agent can re-enter from it.
- If multiple live explanations matter, keep a tiny hypothesis registry in the summary layer:
  - hypothesis
  - strongest support
  - strongest weakening evidence
  - next falsifier

## Make Entries Useful

- Include exact evidence paths and identifiers.
- Include representative visual artifact paths when a plot, overlay, slice, curve, or diff view materially affected the decision.
- Record negative results explicitly when they rule out a family of ideas.
- If the entry draws an inference, state it explicitly instead of leaving it implicit in the next step.
- Keep inference confidence coarse: `low`, `medium`, or `high`.
- Do not add confidence to entries that are only reporting raw observations or routine actions.
- Preserve chronology so later readers can reconstruct what happened.
- End each entry with "so what?" in concrete form.
- If nothing changed in understanding, say that explicitly.

## Avoid Notebook Drift

- Do not let the summary become stale relative to the chronology.
- Do not dump raw metrics or images without interpretation.
- Do not record an interpretation without enough evidence to re-check it later.
- Do not duplicate the full chronological detail into the summary.

## References

- Read `references/templates.md` for one-file and two-layer notebook templates.
