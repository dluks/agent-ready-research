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

Use `domain-modeling` whenever terminology, canonical datasets, project-specific acronyms, outputs, or durable decisions need to be clarified while you work.

Skills live in `.agents/skills/`. If a Claude Code checkout needs project-local instructions, run `setup-claude` to regenerate `.claude/skills/` and `CLAUDE.md` from the canonical repo files.

## Core Layout

| Path | Purpose |
| ---- | ------- |
| `README.md` | Human-facing project overview and setup notes. |
| `AGENTS.md` | Agent-facing project rules, boundaries, and workflows. |
| `CONTEXT.md` | Research question, language/glossary, current state, assumptions. |
| `context/decisions/` | Dated decision records that explain why choices were made. |
| `.agents/skills/` | Canonical project-local workflows for agents. |

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

## Adding Existing Projects As Submodules

If an umbrella repo should link to existing Git repositories, add them under
`projects/` as submodules. A submodule keeps the project in its own repository,
while the umbrella repo records which version of that project belongs with the
shared context.

```bash
git submodule add git@github.com:your-org/project-name.git projects/project-name
git commit -m "Add project-name submodule"
```

When someone clones the umbrella repo, they should clone with submodules:

```bash
git clone --recurse-submodules git@github.com:your-org/umbrella-repo.git
```

If they already cloned it without submodules, populate them afterward:

```bash
git submodule update --init --recursive
```

When a submodule moves to a newer commit, commit that pointer from the umbrella
repo so everyone else gets the same project version.

## Principles

- Start with context, not tooling.
- Carry over domain-modeling discipline into research work: start the language section early, using research concepts, data, methods, and outputs instead of application entities.
- Keep unpublished data and credentials out of git by default.
- Record decisions while they are still fresh.
- Prefer a small structure that researchers will actually maintain.
- Treat the repository as durable context for agents, collaborators, and future
  you.
- Keep `.agents/skills/` as the only editable skills source. Regenerate tool-specific copies from it when needed.
