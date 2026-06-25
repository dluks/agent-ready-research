---
name: to-work-packages
description: Break a research or analysis plan into independently executable work packages. Use when a plan needs to become tasks for a researcher, collaborator, student, or agent.
---

# To Work Packages

Break plans into thin, verifiable slices. Each package should produce evidence:
a figure, table, report, test, notebook section, data card, or decision.

## Process

1. Read the source plan and project context.
2. Identify dependencies between tasks.
3. Draft work packages in dependency order.
4. Ask the researcher whether the granularity is right before creating files or
   tracker issues.

## Package Template

```md
## <title>

### Goal

What this package proves or produces.

### Inputs

Data, code, notes, papers, or decisions required.

### Work

The smallest complete path through the analysis.

### Acceptance Criteria

- [ ] A concrete, inspectable output exists.
- [ ] Assumptions and caveats are documented.
- [ ] The result can be reproduced or manually checked.

### Blocked By

None, or the package title/identifier.
```
