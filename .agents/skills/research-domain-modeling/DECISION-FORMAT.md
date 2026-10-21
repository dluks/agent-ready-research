# Decision Record Format

Decision records live in `context/decisions/` and use sequential numbering: `0001-project-shape.md`, `0002-canonical-dataset.md`, and so on.

For umbrella repos, shared decisions live at the root. Project-specific decisions may live in `projects/<name>/context/decisions/` when that project has its own context.

Create the directory lazily, only when the first decision is worth recording.

## Template

```md
# Decision: <short title>

Date: YYYY-MM-DD

## Context

<What situation forced the decision?>

## Decision

<What did we decide?>

## Consequences

<What gets easier, harder, or explicitly out of scope?>
```

Keep the record short. The value is preserving the reason for the decision, not filling out sections with generic prose.

## When To Offer A Decision Record

All three must be true:

1. **Hard to reverse**: changing direction later would be costly.
2. **Surprising without context**: a future reader would wonder why this choice was made.
3. **A real trade-off**: there were plausible alternatives and one was chosen for specific reasons.

## Research Examples

- Choosing the canonical dataset when several exports or snapshots exist.
- Deciding the unit of analysis, cohort definition, spatial extent, or temporal scope.
- Choosing a method or model family after considering plausible alternatives.
- Deciding which manuscript, figure, table, or report is canonical.
- Keeping sensitive or large data external and documenting the access path.
- Attaching an existing repo as a submodule instead of flattening it into the scaffold.
