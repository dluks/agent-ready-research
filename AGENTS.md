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

- `setup-research-project`: interview the researcher and populate the initial
  context files, branching between single-project and umbrella layouts.
- `migrate-research-project`: inventory an existing folder and propose a
  conservative migration path into the root or `projects/<name>/`.
- `contextualize-existing-project`: make an existing repository agent-ready in
  place without migrating it into this scaffold.
- `domain-modeling`: sharpen the project's language and record durable research decisions as terms and tradeoffs become clear.
- `grilling`: interview the researcher one question at a time to stress-test a plan, method, claim, dataset, interpretation, or output.
- `research-grill`: run `grilling` with `domain-modeling` so the interview also updates language and durable decisions.
- `setup-claude`: regenerate `.claude/skills/` from `.agents/skills/` and write `CLAUDE.md` as `@AGENTS.md` when Claude Code needs local setup.
- `research-plan`: turn a discussion into an analysis plan.
- `to-work-packages`: break a plan into independently executable research tasks.
- `research-architecture-review`: review the project structure for agent and
  collaborator navigability.
