---
name: to-tasks
description: Break a research or analysis plan into small tasks, each listing the tasks that block it, so independent tasks can run in parallel. Use when a plan needs to become tasks for a researcher, collaborator, student, or agent.
---

# To Tasks

Break a plan, or the current conversation, into **tasks**: thin slices that each produce inspectable evidence, and each declaring the tasks that **block** it.

## Process

### 1. Gather context

Work from whatever is already in the conversation. If the researcher points to a plan (for example a file in `context/plans/`) or a tracker issue, read all of it. Read `CONTEXT.md` and relevant decisions, and use the project's `## Language` terms in task titles and descriptions.

### 2. Draft thin slices

Each task cuts a narrow but complete path from inputs to a checked result. A completed task produces evidence someone can look at: a figure, table, map, report section, notebook section, data card, test, or decision. A task that only prepares data with nothing to inspect is usually too thin; fold it into the first task that uses the data.

Size each task so one person or one fresh agent session can finish it. Put any cleanup that makes later tasks easier (shared loading code, a cleaned canonical dataset) first.

Give each task its **blocking edges**: the other tasks that must finish before it can start. A task with no blockers can start immediately, so independent tasks can run in parallel.

### 3. Check the breakdown with the researcher

Present the proposed tasks as a numbered list. For each task, show:

- **Title**: short descriptive name
- **Blocked by**: which other tasks (if any) must finish first
- **What it produces**: the evidence this task leaves behind

Ask the researcher:

- Does the granularity feel right (too coarse, too fine)?
- Are the blocking edges right: does each task only depend on tasks that genuinely gate it?
- Should any tasks be merged or split further?

Iterate until the researcher approves the breakdown.

### 4. Write the tasks

Use the place the project already tracks work:

- **Issue tracker (GitHub, GitLab, ...)**: create one issue per task in dependency order (blockers first) so each task can reference real issue numbers. Use the tracker's native "blocked by" link where it has one; otherwise list the blockers in the issue body.
- **Local files**: write one file per task under `context/tasks/<plan-slug>/<NN>-<slug>.md`, numbered from `01` in dependency order (blockers first), using the template below.

Work the **frontier**: any task whose blockers are all done. For a purely linear chain that means top to bottom.

## Task Template

```md
# <NN>: <Task title>

**What it produces:** the evidence this task leaves behind, from the researcher's perspective.

**Blocked by:** the numbers and titles of the tasks that gate this one, or "None (can start immediately)".

**Inputs:** data, code, notes, papers, or decisions required.

- [ ] A concrete, inspectable output exists.
- [ ] Assumptions and caveats are documented.
- [ ] The result can be reproduced or manually checked.
```

Leave out specific file paths and code snippets in task descriptions unless they are the point of the task; they go stale fast.
