# Agent Guide

This file is the source of truth for agents working in this research project.
Keep it short, concrete, and current.

## What This Project Is

Fill this in with the `setup-research-project` skill.

- Research question:
- Primary outputs:
- Main collaborators:
- Current project phase:

## How To Work Here

- Read `CONTEXT.md` before making project-shaping recommendations.
- Read the nearest relevant `data/README.md` before touching data, analysis
  inputs, or generated outputs.
- Record durable decisions in `context/decisions/`.
- Do not commit credentials, private tokens, unpublished sensitive data, or
  large raw files unless the project explicitly says they are safe to track.
- Ask before reorganizing existing files. Prefer a migration plan first.

## Directory Rules

- `context/` is for project memory: decisions, meetings, reading notes, and
  background that does not belong to a single script or notebook.
- `data/` is for data inventory and lightweight pointers. Large datasets may
  live elsewhere; document their location and access requirements in
  `data/README.md`.
- `notebooks/` is for exploratory work.
- `src/` is for reusable code that should survive beyond one notebook.
- `outputs/` is for generated figures, tables, reports, and analysis products.
- `papers/` is for manuscripts, posters, talks, and related writing.
- `projects/` is optional. Use it when several related research projects should
  sit under one context-rich umbrella. Existing Git repositories can be attached
  here as submodules, while the root keeps shared context, decisions, and papers.
- For a single project, `data/`, `notebooks/`, `src/`, `outputs/`, and
  `papers/` usually live at the root. For an umbrella project, those directories
  usually live inside each `projects/<name>/` repo or folder.

## Skills

The project ships starter skills in `.agents/skills/`. Treat this as the only editable source of truth for project-local skills.

User-invoked (the researcher types the name; agents tell the researcher to run them):

- `setup-research-project`: interview the researcher and populate the initial
  context files, branching between single-project and umbrella layouts.
- `migrate-research-project`: inventory an existing folder and propose a
  conservative migration path into the root or `projects/<name>/`.
- `research-grill`: run `research-grilling` with `research-domain-modeling` so the interview also updates language and durable decisions.
- `handoff`: compact the current session into a handoff document for the next agent session.
- `setup-claude`: refresh the `.claude/skills/` symlinks to `.agents/skills/` and write `CLAUDE.md` as `@AGENTS.md` after adding, renaming, or removing a skill.

Model-invoked (agents may also call these with the Skill tool when they fit):

- `contextualize-existing-project`: make an existing repository agent-ready in
  place without migrating it into this scaffold.
- `research-domain-modeling`: sharpen the project's language and record durable research decisions as terms and tradeoffs become clear.
- `research-grilling`: interview the researcher in rounds of numbered questions, each with a recommended answer, to stress-test a plan, method, claim, dataset, interpretation, or output.
- `research-plan`: turn a discussion into a written analysis plan.
- `to-tasks`: break a plan into small tasks, each listing the tasks that block it.
- `lab-notebook`: record experiments, runs, and results so work can be resumed and checked later. The notebook lives in `context/lab-notebook.md` once created.
- `pi-update`: turn lab notebook entries and results into an evidence-backed progress update for a PI, collaborators, or a lab meeting.
- `research`: look up a question in primary sources and save a cited note in `context/reading/`.
- `research-architecture-review`: review the project structure for agent and
  collaborator navigability.
