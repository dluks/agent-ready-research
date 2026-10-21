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
3. Run `/setup-research-project`.
4. Answer the interview questions.
5. Let the skill choose a single-project or umbrella layout and populate the
   project context files.

If you already have a messy project folder, run `/migrate-research-project`
first. It inventories the folder and proposes a non-destructive migration plan
before moving or copying anything.

If you are already inside an existing repository and want to make it
agent-ready in place, run `contextualize-existing-project`.

## Skills

Skills come in two kinds. **User-invoked** skills run only when you type their
name; agents never start them on their own. **Model-invoked** skills can also be
picked up by the agent when the situation fits.

| Skill | Kind | What it does |
| ----- | ---- | ------------ |
| `setup-research-project` | user | Interview you and scaffold a new project. |
| `migrate-research-project` | user | Inventory a messy folder and plan a safe migration. |
| `research-grill` | user | Stress-test an idea and record terms and decisions as they settle. |
| `handoff` | user | Write a handoff document for the next agent session. |
| `setup-claude` | user | Refresh the `.claude/skills/` links after adding, renaming, or removing a skill. |
| `contextualize-existing-project` | model | Make an existing repository agent-ready in place. |
| `research-grilling` | model | Interview in rounds of numbered questions, each with a recommended answer. |
| `research-domain-modeling` | model | Sharpen the project's language in `CONTEXT.md` and record decisions. |
| `research-plan` | model | Turn a discussion into a written analysis plan. |
| `to-tasks` | model | Break a plan into small tasks, each listing the tasks that block it. |
| `lab-notebook` | model | Record experiments, runs, and results so work can be resumed and checked. |
| `pi-update` | model | Turn the lab notebook into a progress update for a PI or lab meeting. |
| `research` | model | Look up a question in primary sources and save a cited note. |
| `research-architecture-review` | model | Review the project structure for collaborators and agents. |

A typical loop: `/research-grill` to stress-test an idea, `research-plan` to
write it down, `to-tasks` to break the plan into tasks, and `lab-notebook` to
record what each task turned up. `pi-update` turns the notebook into
an update for your PI, collaborators, or lab meeting.

### Where skills live

Each skill has one copy, in `.agents/skills/<name>/`. A skill folder holds a
`SKILL.md` and optional supporting files (`references/`, `scripts/`, and
tool-specific metadata under `agents/`). For tools that look for skills
somewhere else, the repo links back to this folder: `.claude/skills/` holds one
symlink per skill, and `CLAUDE.md` points to `AGENTS.md`.

Edit skills only in `.agents/skills/`. After adding, renaming, or removing a
skill, run `/setup-claude` to refresh those links. It also covers Windows
checkouts without symlink support.

## Core Layout

| Path | Purpose |
| ---- | ------- |
| `README.md` | Human-facing project overview and setup notes. |
| `AGENTS.md` | Agent-facing project rules, boundaries, and workflows. |
| `CONTEXT.md` | Research question, language/glossary, current state, assumptions. |
| `context/decisions/` | Dated decision records that explain why choices were made. |
| `.agents/skills/` | Canonical project-local workflows for agents. |
| `.claude/skills/` | Symlinks into `.agents/skills/` for tools that read skills from there. |
| `CLAUDE.md` | Contains `@AGENTS.md`, so tools that read it get the same agent guide. |

## Optional Layout

Create these only when useful:

| Path | Use when |
| ---- | -------- |
| `context/meetings/` | Meeting notes or transcripts affect the project state. |
| `context/reading/` | Literature notes need to stay close to the project. The `research` skill saves its notes here. |
| `context/lab-notebook.md` | Experiments and analysis runs need a running record. Created by the `lab-notebook` skill. |
| `context/plans/` | Analysis plans written by `research-plan`. |
| `context/tasks/` | Task files written by `to-tasks` when the project has no issue tracker. |
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
- Carry over domain modeling discipline into research work: start the language section early, using research concepts, data, methods, and outputs instead of application entities.
- Keep unpublished data and credentials out of git by default.
- Record decisions while they are still fresh.
- Prefer a small structure that researchers will actually maintain.
- Treat the repository as durable context for agents, collaborators, and future
  you.
- Keep `.agents/skills/` as the only editable skills source. Other tools reach it through links.
