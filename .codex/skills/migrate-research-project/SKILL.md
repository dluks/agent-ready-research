---
name: migrate-research-project
description: Inventory an existing messy research folder and propose a conservative migration into this template. Use when a researcher already has notebooks, scripts, data, papers, or notes outside the scaffold.
---

# Migrate Research Project

Help the researcher get value before reorganizing files. Inventory first,
propose second, copy or move only after approval.

## Process

1. Ask for the source folder path if it is not already clear.
2. Run the inventory script:

   ```bash
   python .codex/skills/migrate-research-project/scripts/inventory_research_folder.py /path/to/source --out migration_inventory.md
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
4. Interview the researcher about ambiguous items. Ask one question at a time.
5. Propose a migration table before changing anything:

   | Current path | Proposed destination | Action | Reason |
   | ------------ | -------------------- | ------ | ------ |

6. Default to non-destructive actions:
   - copy rather than move
   - preserve original filenames
   - do not stage large/private data
   - document external data locations in `data/README.md`
   - write `MIGRATION_LOG.md`
7. After approval, apply the agreed migration and update `README.md`,
   `CONTEXT.md`, `data/README.md`, and a decision record.

## Safety Rules

- Never reorganize files without an approved migration table.
- Never commit credentials, private tokens, or sensitive unpublished data.
- If a file may be sensitive, leave it in place and document it as external.
- If the source folder is already a git repository, preserve its history or
  propose adding it under `projects/` rather than flattening it.
