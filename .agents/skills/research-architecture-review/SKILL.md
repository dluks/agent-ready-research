---
name: research-architecture-review
description: Review a research repository's structure for clarity, provenance, reproducibility, and LLM navigability. Use when a project feels messy, hard to onboard into, or difficult for agents to navigate.
---

# Research Architecture Review

Look for structure that hides the science from collaborators or agents.

## Process

1. Read `README.md`, `AGENTS.md`, `CONTEXT.md`, and `data/README.md`.
2. Inventory the top-level directories and the main analysis paths.
3. Identify friction:
   - unclear research question
   - missing data provenance
   - canonical files mixed with scratch files
   - outputs detached from the analysis that produced them
   - decisions trapped in chat, email, or notebook prose
   - reusable code trapped in notebooks
   - linked projects flattened into one repository
4. Propose at most five improvements. For each, include:
   - files or directories involved
   - problem
   - recommended change
   - benefit for humans
   - benefit for LLM agents
   - risk or cost
5. Recommend the first change to make.

## Completion Criteria

The review is done when the researcher can choose one concrete structural
improvement without needing a full reorganization.
