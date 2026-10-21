---
name: research-plan
description: Turn the current research discussion into a written analysis plan, synthesizing what has already been discussed. Use when the researcher has an idea, meeting notes, proposal text, a grilling session, or an exploratory result and needs an executable plan.
---

# Research Plan

This skill takes the current conversation and what you know about the project and produces an analysis plan. Synthesize what you already know; the interview belongs in `research-grill`, which the researcher can run first if the idea is still fuzzy.

## Process

1. Read `CONTEXT.md`, the nearest relevant `data/README.md`, and the decisions in `context/decisions/` that touch this work. Use the project's `## Language` terms throughout the plan, and respect existing decisions.
2. Identify the research objective and the output the plan is meant to produce.
3. Sketch how the result will be checked: the validation, baseline, or sanity check that would convince a skeptical collaborator. Prefer checks the project already uses. Confirm with the researcher that these checks match their expectations; this is the one question this skill asks.
4. Write the plan using the template below. Save it where the project already keeps plans; if there is no convention, use `context/plans/YYYY-MM-DD-<short-title>.md`.
5. Tell the researcher where the plan is, and that `to-tasks` can break it into tasks.

## Template

```md
# Analysis Plan: <title>

Date: YYYY-MM-DD

## Research Objective

The question this work answers, from the researcher's perspective.

## Expected Output

Paper section, figure, table, dataset, model, map, report, or decision.

## Questions The Plan Must Answer

A numbered list of the concrete things a reader should be able to learn from
the result. Be extensive: cover every part of the objective, including edge
cases such as missing data, subsets, and sensitivity checks.

1. ...

## Inputs

Datasets, notes, manuscripts, code, prior results, and access constraints.

## Method

The analytical approach and why it fits the question.

## Analysis Decisions

Decisions already made: unit of analysis, spatial and temporal scope, cohort
or sample definition, model family, preprocessing choices, thresholds.
Describe them in prose. Leave out file paths and code, which go stale quickly.

## Validation

How we will know the result is credible (from step 3).

## Risks And Caveats

Data gaps, assumptions, confounders, sensitivity, reproducibility risks.

## Out Of Scope

## Further Notes
```
