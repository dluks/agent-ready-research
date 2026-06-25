---
name: contextualize-existing-project
description: Make an existing research repository agent-ready by gathering context and adding missing context files without migrating it into a new scaffold. Use when the researcher is already inside a repo and wants AGENTS.md, CONTEXT.md, data inventory, decisions, and helpful directories generated in place.
---

# Contextualize Existing Project

Use this inside an existing repository that should keep its current location and
history. This is not a migration workflow. Do not move or reorganize files unless
the researcher explicitly approves a separate migration plan.

## Process

1. Inspect the repository:
   - `git status`
   - top-level directories
   - existing `README.md`, `AGENTS.md`, `CLAUDE.md`, `CONTEXT.md`
   - data, notebook, source, output, paper, and project-like directories
2. Interview the researcher until you understand:
   - research question and current phase
   - whether this repo is a single project or an umbrella
   - canonical data and outputs
   - important notebooks, scripts, papers, and external materials
   - collaborator roles and decision-making norms
   - what future agents should be able to answer
3. Add or update context in place:
   - `README.md`
   - `AGENTS.md`
   - `CLAUDE.md` as `@AGENTS.md` when Claude compatibility is desired
   - `CONTEXT.md`
   - `data/README.md` when data exists or is referenced
   - `context/decisions/0001-project-context.md`
4. Create optional directories only when useful:
   - Single project: `data/`, `notebooks/`, `src/`, `outputs/`, `papers/`,
     `context/meetings/`, `context/reading/`
   - Umbrella project: `projects/`, `papers/`, `context/decisions/`,
     `context/meetings/`, `context/reading/`
5. If the repo contains several related but separable projects, propose a
   `projects/` layout and a follow-up migration plan. Do not apply it by
   default.
6. Finish with a summary of context added, assumptions made, and the next useful
   skill to run.

## Completion Criteria

The repository is contextualized when a new collaborator or agent can answer:

- What is this project trying to do?
- What is the current state?
- Where are the important data, code, notebooks, outputs, and papers?
- Which files are canonical?
- What decisions have already been made?
- What should happen next?
