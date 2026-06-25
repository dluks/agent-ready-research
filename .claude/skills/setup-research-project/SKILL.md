---
name: setup-research-project
description: Set up a new agent-ready research scaffold by interviewing the researcher, choosing a single-project or umbrella layout, and writing durable context files. Use when starting from this template, cloning it next to existing work, or turning a loose research idea into a structured project.
---

# Setup Research Project

Build the smallest useful structure, but ask as many questions as needed to make
the result real. Do not stop at a shallow five-question interview if the project
shape, data, outputs, or existing materials are still ambiguous.

## Process

1. Inspect the current repository layout and existing context files.
2. Determine the setup mode:
   - **Single project**: one research effort lives at the repository root.
   - **Umbrella project**: the root coordinates multiple related projects under
     `projects/`, while shared context and papers live at the root.
3. Ask one question at a time until the mode, materials, data, outputs, and next
   action are clear. If written context already answers a question, infer a
   conservative answer and mark it as an assumption.
4. If the researcher already has a folder or repository to bring in, invoke
   `migrate-research-project` before moving files:
   - Single project: propose migration into the root layout.
   - Umbrella project: propose migration into `projects/<project-name>/`.
5. Populate or update root context:
   - `README.md`
   - `AGENTS.md`
   - `CONTEXT.md`
   - `context/decisions/0001-project-shape.md`
6. Create the selected layout.
7. Finish with a summary of files created, assumptions, unanswered questions,
   and the next useful skill.

## Layout Branches

### Single Project

Use when one repository should hold the analysis, code, data inventory, outputs,
and writing for one coherent project.

Typical root layout:

- `data/README.md`
- `notebooks/`
- `src/`
- `outputs/`
- `papers/`
- `context/decisions/`
- `context/meetings/`
- `context/reading/`

### Umbrella Project

Use when several related projects should share context but keep their own code,
data inventory, notebooks, outputs, and possibly git history.

Typical root layout:

- `CONTEXT.md`
- `context/decisions/`
- `context/meetings/`
- `context/reading/`
- `papers/`
- `projects/<project-name>/`

Each `projects/<project-name>/` may then contain its own `README.md`,
`AGENTS.md`, `CONTEXT.md`, `data/README.md`, `notebooks/`, `src/`, and
`outputs/`. If the project already exists as a Git repository, preserve it and
attach it under `projects/` rather than flattening it.

## Interview Topics

- Research question, motivation, and current phase.
- Whether this is one project or an umbrella over several related projects.
- Expected outputs: paper, thesis chapter, dataset, model, map, report, poster,
  talk, package, or operational product.
- Existing materials: notes, proposals, papers, manuscripts, datasets,
  notebooks, scripts, talks, folders, or related repositories.
- For each existing material: keep external, copy into root, copy into
  `projects/<name>/`, or attach as a git submodule.
- Data ownership, size, storage location, and which files are canonical.
- Collaborators, roles, and decision-making norms.
- Tooling preferences: notebooks, scripts, command-line tools, package manager,
  cloud/HPC environment, issue tracker, Zotero, Overleaf, GitHub, RStudio.
- What the researcher wants the agent to be able to answer after setup.

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
