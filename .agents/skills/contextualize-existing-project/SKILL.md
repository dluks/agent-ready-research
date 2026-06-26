---
name: contextualize-existing-project
description: Make an existing research repository agent-ready by gathering context, pruning noisy agent docs, and adding missing context files without migrating it into a new scaffold. Use when the researcher is already inside a repo and wants AGENTS.md, CONTEXT.md, data inventory, decisions, and helpful directories generated in place.
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
2. If `CLAUDE.md` has project instructions, treat it as source material, not as
   the final guide:
   - distill durable rules into `AGENTS.md`
   - replace `CLAUDE.md` with `@AGENTS.md`
   - prefer deleting stale, generic, tool-specific, or aspirational advice
3. Interview the researcher until you understand:
   - research question and current phase
   - whether this repo is a single project or an umbrella
   - the core domain terms, acronyms, dataset names, output names, and overloaded words that future agents must use consistently
   - canonical data and outputs
   - important notebooks, scripts, papers, and external materials
   - collaborator roles and decision-making norms
   - what future agents should be able to answer
   - for existing `CLAUDE.md` / `AGENTS.md` content: what must stay, move, or go
4. Add or update context in place:
   - `README.md`
   - slim, canonical `AGENTS.md`
   - `CLAUDE.md` as `@AGENTS.md`
   - `CONTEXT.md`, including an initial `## Language` section
   - `data/README.md` when data exists or is referenced
   - `context/decisions/0001-project-context.md`
5. Create optional directories only when useful:
   - Single project: `data/`, `notebooks/`, `src/`, `outputs/`, `papers/`,
     `context/meetings/`, `context/reading/`
   - Umbrella project: `projects/`, `papers/`, `context/decisions/`,
     `context/meetings/`, `context/reading/`
6. If the repo contains several related but separable projects, propose a
   `projects/` layout and a follow-up migration plan. Do not apply it by
   default.
7. Finish with a summary of context added, assumptions made, and the next useful
   skill to run.

## Agent Guide Pruning

Default to a shorter `AGENTS.md`. Keep only instructions that are specific,
current, and repeatedly useful for this repository. Move background context to
`CONTEXT.md`, data details to `data/README.md`, and past decisions to
`context/decisions/`. Do not preserve content just because it was already in
`CLAUDE.md` or `AGENTS.md`.

## Language

Starting the language section is a core part of contextualizing an existing research project, not an optional polish step. In `CONTEXT.md`, create or extend a `## Language` section with the canonical terms future agents and collaborators should use. This is the research-project analogue of domain-modeling while you work.

Use the `domain-modeling` skill while interviewing: challenge fuzzy or conflicting terms, test them against concrete research scenarios, and update `CONTEXT.md` as terms resolve instead of saving terminology for the end.

Include terms for:

- domain concepts and populations
- datasets, cohorts, variables, instruments, and measurements
- important notebooks, scripts, outputs, papers, reports, and figures
- local acronyms, abbreviations, and overloaded words
- distinctions that prevent common misunderstandings

Keep definitions concise and research-facing. If a term is ambiguous, record the candidate meanings and the question that needs researcher input instead of pretending it is resolved.

## Completion Criteria

The repository is contextualized when a new collaborator or agent can answer:

- What is this project trying to do?
- What is the current state?
- What do the project's key terms mean, and which terms should be avoided or clarified?
- Where are the important data, code, notebooks, outputs, and papers?
- Which files are canonical?
- What decisions have already been made?
- What should happen next?
