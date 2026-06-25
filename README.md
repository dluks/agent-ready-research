# agent-ready-research

A context-first starter kit for research projects that LLM agents can actually
understand.

The template is intentionally small. Its main job is to preserve context,
decisions, data provenance, and working conventions in predictable places. Add
more structure only when the project needs it.

## Start Here

1. Open this repository in your LLM coding tool.
2. Run the `setup-research-project` skill.
3. Answer the interview questions.
4. Let the skill populate the project context files.

If you already have a messy project folder, run `migrate-research-project`
first. It inventories the folder and proposes a non-destructive migration plan
before moving or copying anything.

## Core Layout

| Path | Purpose |
| ---- | ------- |
| `README.md` | Human-facing project overview and setup notes. |
| `AGENTS.md` | Agent-facing project rules, boundaries, and workflows. |
| `CONTEXT.md` | Research question, glossary, current state, assumptions. |
| `context/decisions/` | Dated decision records that explain why choices were made. |
| `data/README.md` | Data inventory, provenance, sensitivity, and storage notes. |
| `.codex/skills/` | Project-local workflows for Codex. |
| `.claude/skills/` | The same project-local workflows for Claude Code. |

## Optional Layout

Create these only when useful:

| Path | Use when |
| ---- | -------- |
| `context/meetings/` | Meeting notes or transcripts affect the project state. |
| `context/reading/` | Literature notes need to stay close to the project. |
| `notebooks/` | Exploratory analysis is part of the workflow. |
| `src/` | Reusable code is emerging from scripts or notebooks. |
| `outputs/` | Figures, tables, reports, or derived products are shared. |
| `papers/` | Manuscripts, abstracts, posters, or slide decks belong here. |
| `projects/` | Several related research projects should be grouped under one context-rich umbrella. Existing Git repositories can be attached here as submodules. |

## Principles

- Start with context, not tooling.
- Keep unpublished data and credentials out of git by default.
- Record decisions while they are still fresh.
- Prefer a small structure that researchers will actually maintain.
- Treat the repository as durable context for agents, collaborators, and future
  you.
- Keep `.codex/skills/` and `.claude/skills/` synchronized when editing shared
  skills.
