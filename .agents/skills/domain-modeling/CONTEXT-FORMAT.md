# CONTEXT.md Format

## Structure

Use this shape when creating or extending `CONTEXT.md`:

```md
# <Project Or Context Name>

<One or two sentences describing what this research context is and why it exists.>

## Research Question

<The current research question, claim, or objective. Mark as provisional if it is still being sharpened.>

## Current State

<What is known, what phase the work is in, and what the next concrete step is.>

## Language

**Crowdsourced Biodiversity Data**:
Species occurrence records contributed by volunteers through public platforms and later filtered for this project. Use this for the source data type, not the cleaned analysis table or model input.
_Avoid_: Citizen science data, iNaturalist data, GBIF data

**Primary Outcome**:
The main response variable used to evaluate the research question.
_Avoid_: Target, label, dependent variable

**Figure 2 Map**:
The manuscript-ready map that communicates the spatial result for Figure 2. This is not the exploratory notebook render or an intermediate GIS layer.
_Avoid_: Final map, map output

## Assumptions And Open Questions

- <Assumption or unresolved terminology question.>
```

Existing `CONTEXT.md` files do not need to be rewritten to exactly match this template. Preserve useful local structure and add the missing language section clearly. The example terms above are illustrative; replace them with the project's actual vocabulary.

## Rules

- **Be opinionated.** When several words exist for the same concept, pick the preferred project term and list the others under `_Avoid_`.
- **Keep definitions tight.** One or two sentences is usually enough. Define what the concept is, not every action that can be performed with it.
- **Use research terms.** Include concepts specific to this project: study areas, populations, cohorts, variables, instruments, datasets, outputs, figures, manuscripts, and local acronyms.
- **Do not include generic tooling terms.** General programming, statistics, or workflow concepts only belong here when the project uses them in a local, non-obvious way.
- **Record unresolved terms honestly.** If a term is still ambiguous, write the competing meanings and the question that needs researcher input.
- **Group terms when useful.** Natural clusters such as Data, Methods, Outputs, Places, People, or Manuscript Terms are fine. A flat list is also fine for small projects.

## Single Vs Umbrella Repos

**Single project:** Use one root `CONTEXT.md`.

**Umbrella project:** Use root `CONTEXT.md` for shared language across the umbrella. Put project-specific language in `projects/<name>/CONTEXT.md` when a term only makes sense inside that project.

When unsure whether a term is shared or project-specific, ask before writing it.
