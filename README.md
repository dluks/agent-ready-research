# agent-ready-research

A context-first starter kit for research projects that LLM agents can actually
understand.

The template is intentionally small. Its main job is to preserve context,
decisions, data provenance, and working conventions in predictable places. Add
more structure only when the project needs it.

## Start Here

For a new project:

1. Clone this repository next to your existing work or into a fresh folder.
2. Open it in your LLM coding tool.
3. Run the `setup-research-project` skill.
4. Answer the interview questions.
5. Let the skill choose a single-project or umbrella layout and populate the
   project context files.

If you already have a messy project folder, run `migrate-research-project`
first. It inventories the folder and proposes a non-destructive migration plan
before moving or copying anything.

If you are already inside an existing repository and want to make it
agent-ready in place, run `contextualize-existing-project`.

## Core Layout

| Path | Purpose |
| ---- | ------- |
| `README.md` | Human-facing project overview and setup notes. |
| `AGENTS.md` | Agent-facing project rules, boundaries, and workflows. |
| `CONTEXT.md` | Research question, glossary, current state, assumptions. |
| `context/decisions/` | Dated decision records that explain why choices were made. |
| `.codex/skills/` | Project-local workflows for Codex. |
| `.claude/skills/` | The same project-local workflows for Claude Code. |

## Optional Layout

Create these only when useful:

| Path | Use when |
| ---- | -------- |
| `context/meetings/` | Meeting notes or transcripts affect the project state. |
| `context/reading/` | Literature notes need to stay close to the project. |
| `data/README.md` | A single-project repo needs root data inventory, provenance, sensitivity, and storage notes. Umbrella repos usually keep this inside each `projects/<name>/`. |
| `notebooks/` | Exploratory analysis is part of the workflow. |
| `src/` | Reusable code is emerging from scripts or notebooks. |
| `outputs/` | Figures, tables, reports, or derived products are shared. |
| `papers/` | Manuscripts, abstracts, posters, or slide decks belong here. |
| `projects/` | Several related research projects should be grouped under one context-rich umbrella. Existing Git repositories can be attached here as submodules. |

## Layout Modes

### Single Project

Use the root for the project itself:

| Path | Purpose |
| ---- | ------- |
| `data/` | Data inventory and lightweight pointers. |
| `notebooks/` | Exploratory analysis. |
| `src/` | Reusable code. |
| `outputs/` | Figures, tables, reports, maps, or derived products. |
| `papers/` | Manuscripts, talks, posters, and writing. |

### Umbrella Project

Use the root for shared context and put related projects under `projects/`:

| Path | Purpose |
| ---- | ------- |
| `context/` | Shared decisions, meeting notes, and reading notes. |
| `papers/` | Cross-project manuscripts and presentations. |
| `projects/<name>/` | Each related project, often with its own data, notebooks, source, outputs, and agent guide. |

## Principles

- Start with context, not tooling.
- Keep unpublished data and credentials out of git by default.
- Record decisions while they are still fresh.
- Prefer a small structure that researchers will actually maintain.
- Treat the repository as durable context for agents, collaborators, and future
  you.
- Keep `.codex/skills/` and `.claude/skills/` synchronized when editing shared
  skills.
