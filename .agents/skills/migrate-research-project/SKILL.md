---
name: migrate-research-project
description: Inventory an existing messy research folder and propose a conservative migration into a single-project root or an umbrella projects directory. Use when a researcher already has notebooks, scripts, data, papers, repos, or notes outside the scaffold.
---

# Migrate Research Project

Help the researcher get value before reorganizing files. Inventory first,
propose second, copy or move only after approval.

## Process

1. Ask for the source folder path if it is not already clear.
2. Run the inventory script from the canonical skills tree:

   ```bash
   python .agents/skills/migrate-research-project/scripts/inventory_research_folder.py /path/to/source --out migration_inventory.md
   ```

3. Read the inventory and identify:
   - likely canonical files
   - scratch or duplicate-looking files
   - notebooks and scripts
   - manuscripts, slides, figures, and tables
   - datasets and large files
   - possible secrets
   - existing git repositories
   - related projects that may belong together under `projects/`
4. Determine the migration target:
   - **Single project**: migrate approved materials into the root layout
     (`data/`, `notebooks/`, `src/`, `outputs/`, `papers/`, `context/`).
   - **Umbrella project**: migrate each related project into
     `projects/<project-name>/`; keep shared context and papers at the root.
   - **Existing git repo**: preserve history and propose adding it under
     `projects/` rather than flattening it, unless the researcher explicitly
     wants a copy-only import.
5. Interview the researcher about ambiguous items. Ask one question at a time.
   Use `domain-modeling` while you interview. Treat terminology as part of the migration, not a follow-up chore: clarify the source folder's project names, dataset names, acronyms, output names, local jargon, and overloaded words as they come up.
6. Propose a migration table before changing anything:

   | Current path | Proposed destination | Action | Reason |
   | ------------ | -------------------- | ------ | ------ |

7. Default to non-destructive actions:
   - copy rather than move
   - preserve original filenames
   - do not stage large/private data
   - document external data locations in `data/README.md`
   - write `MIGRATION_LOG.md`
8. After approval, apply the agreed migration and update the relevant
   `README.md`, `CONTEXT.md`, `data/README.md`, `MIGRATION_LOG.md`, and decision
   record.

## Language

Every migration should begin or extend `CONTEXT.md` with a `## Language` section. This is one of the main ways the migrated project becomes agent-ready: future agents need the project's vocabulary as much as they need its folder layout. Treat this as research-domain modeling, not as a documentation afterthought.

Use the `domain-modeling` skill's `CONTEXT.md` format for this section and its decision-record guidance when a migration decision is worth preserving.

Capture canonical names for:

- research questions, study areas, populations, and domain concepts
- datasets, cohorts, variables, instruments, measurements, and external sources
- notebooks, scripts, outputs, figures, tables, reports, manuscripts, and talks
- acronyms, abbreviations, shorthand folder names, and overloaded words

Do not wait for perfect definitions. Seed the section with the best current definitions, mark unresolved terms as questions, and refine it as the migration interview resolves ambiguity.

## Safety Rules

- Never reorganize files without an approved migration table.
- Never commit credentials, private tokens, or sensitive unpublished data.
- If a file may be sensitive, leave it in place and document it as external.
- If the source folder is already a git repository, preserve its history or
  propose adding it under `projects/` rather than flattening it.
