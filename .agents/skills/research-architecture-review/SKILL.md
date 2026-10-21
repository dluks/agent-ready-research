---
name: research-architecture-review
description: Review a research repository's structure for clarity, provenance, reproducibility, and LLM navigability. Use when a project feels messy, hard to onboard into, or difficult for agents to navigate.
---

# Research Architecture Review

Look for structure that hides the science from collaborators or agents.

## Process

1. Read `README.md`, `AGENTS.md`, `CONTEXT.md`, and `data/README.md`.
2. Decide where to look before you look (YAGNI). Structure pays off where work
   is still happening, so weight the active parts of the project:
   - If the researcher named an area (a paper, a dataset, a pipeline, a pain
     point), start there.
   - Otherwise, walk back a good stretch of history (`git log --oneline
     --name-only`) and note which directories, notebooks, and scripts keep
     changing. Let those pull your attention first. If changes are scattered
     with no clear hot spot, widen the net.

   Finished analyses and archived material rarely need restructuring; leave
   them alone unless they block current work.
3. Inventory the top-level directories and the main analysis paths.
4. Identify friction:
   - unclear research question
   - missing data provenance
   - canonical files mixed with scratch files
   - outputs detached from the analysis that produced them
   - decisions trapped in chat, email, or notebook prose
   - reusable code trapped in notebooks
   - linked projects flattened into one repository
5. Propose at most five improvements. For each, include:
   - files or directories involved
   - problem
   - recommended change
   - benefit for humans
   - benefit for LLM agents
   - risk or cost
6. Recommend the first change to make.

## Completion Criteria

The review is done when the researcher can choose one concrete structural
improvement without needing a full reorganization.
