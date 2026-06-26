---
name: domain-modeling
description: Build and sharpen a research project's language and durable decisions. Use when the researcher wants to pin down terminology, clarify a concept, resolve an overloaded acronym, name canonical data or outputs, or when another skill needs to maintain the project domain model.
---

# Domain Modeling

Actively build and sharpen the research project's domain model as you work. This is the active discipline of challenging terms, testing concrete research scenarios, and writing resolved vocabulary and decisions down as soon as they crystallize.

Merely reading `CONTEXT.md` for vocabulary is not this skill. Use this skill when you are changing or clarifying the project's language.

## File Structure

Most research repos have one root context:

```text
/
|-- CONTEXT.md
|-- context/
|   `-- decisions/
|       |-- 0001-project-shape.md
|       `-- 0002-canonical-dataset.md
`-- data/
```

Umbrella repos may have shared root context plus project-specific contexts:

```text
/
|-- CONTEXT.md                         # shared umbrella language
|-- context/
|   `-- decisions/                     # umbrella decisions
`-- projects/
    |-- project-a/
    |   |-- CONTEXT.md                 # project-specific language
    |   `-- context/decisions/
    `-- project-b/
        |-- CONTEXT.md
        `-- context/decisions/
```

Create files lazily, but do not avoid creating them when a real term or decision has been resolved. If no `CONTEXT.md` exists, create one when the first term is resolved. If no `context/decisions/` directory exists, create it when the first decision needs to be recorded.

## During The Session

### Challenge Against The Language

When the researcher uses a term that conflicts with `CONTEXT.md`, call it out immediately. Example: "`CONTEXT.md` defines `field campaign` as the 2024 survey, but here you seem to mean all survey years. Which meaning should be canonical?"

### Sharpen Fuzzy Language

When the researcher uses vague, overloaded, or local shorthand, propose a precise canonical term. Example: "You are saying `model output`; do you mean the raw prediction raster, the summarized table, or the manuscript figure?"

### Discuss Concrete Research Scenarios

Stress-test terminology with specific scenarios: alternate cohorts, edge-case sites, missing data, changed spatial or temporal scope, revised inclusion criteria, and outputs that share similar names. Use these scenarios to force precision about boundaries between concepts.

### Cross-Reference With Project Artifacts

When the researcher states how something works, check whether the repo agrees: `README.md`, `data/README.md`, notebooks, scripts, paper drafts, output names, and existing decisions. If artifacts contradict the stated language, surface the conflict and ask which source should become canonical.

### Update CONTEXT.md Inline

When a term is resolved, update the relevant `CONTEXT.md` immediately. Do not batch these updates. Use the format in [CONTEXT-FORMAT.md](./CONTEXT-FORMAT.md).

`CONTEXT.md` should stay research-facing. It can include project overview, current state, assumptions, and language, but it should not become a scratch pad or an implementation plan.

### Offer Decision Records Sparingly

Only offer to create a decision record when all three are true:

1. **Hard to reverse**: changing direction later would be costly.
2. **Surprising without context**: a future reader would wonder why this choice was made.
3. **A real trade-off**: there were plausible alternatives and one was chosen for specific reasons.

If any of the three is missing, skip the decision record. Use the format in [DECISION-FORMAT.md](./DECISION-FORMAT.md).
