---
name: setup-research-project
description: Set up a research project scaffold by interviewing the researcher and writing durable context files. Use when starting a new research repo, adapting this template, or turning a loose idea into an agent-ready project.
---

# Setup Research Project

Build the smallest useful project structure. Do not introduce workflow tooling
unless the researcher asks for it.

## Process

1. Inspect the current repository layout.
2. Interview the researcher. Ask one question at a time when running
   interactively; if running from written context, infer conservative defaults
   and mark assumptions.
3. Populate or update:
   - `README.md`
   - `AGENTS.md`
   - `CONTEXT.md`
   - `data/README.md`
   - `context/decisions/0001-project-shape.md`
4. Create optional directories only when the answers require them:
   - `notebooks/`
   - `src/`
   - `outputs/`
   - `papers/`
   - `context/meetings/`
   - `context/reading/`
   - `projects/`
5. Finish with a short summary of what was created, what assumptions were made,
   and the next useful skill to run.

## Interview Topics

- Research question and motivation.
- Expected outputs: paper, thesis chapter, dataset, model, map, report, poster,
  talk, package, or operational product.
- Existing materials: notes, proposals, papers, manuscripts, datasets,
  notebooks, scripts, talks, or related repositories.
- Project grouping: whether this should be one standalone project or an
  umbrella with related repositories under `projects/`.
- Data sensitivity, ownership, size, and storage location.
- Collaborators, roles, and decision-making norms.
- Current project phase: idea, exploratory analysis, pipeline build, writing,
  revision, publication, maintenance.
- Tooling preferences: notebooks, scripts, command-line tools, package manager,
  cloud/HPC environment, issue tracker.

## Decision Record Template

Use `context/decisions/YYYY-MM-DD-short-title.md`.

```md
# Decision: <title>

Date: YYYY-MM-DD

## Context

What situation forced this decision?

## Decision

What did we decide?

## Consequences

What gets easier, harder, or explicitly out of scope?
```
