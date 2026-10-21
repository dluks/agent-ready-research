---
name: setup-claude
description: Regenerate .claude/skills/ and CLAUDE.md from the canonical .agents/skills/ and AGENTS.md, after cloning or after editing skills.
disable-model-invocation: true
---

# Setup Claude

Regenerate Claude Code integration files from canonical repo files. Do not edit generated project skill copies directly; update `.agents/skills` and rerun this setup.

Run from the repository root:

```bash
mkdir -p .claude/skills
for skill_dir in .agents/skills/*; do
  [ -d "$skill_dir" ] || continue
  skill_name="$(basename "$skill_dir")"
  rm -rf ".claude/skills/$skill_name"
  cp -R "$skill_dir" ".claude/skills/$skill_name"
done
printf '@AGENTS.md\n' > CLAUDE.md
```

This replaces only the project skill directories whose names exist in `.agents/skills`. It must not delete unrelated `.claude/skills/*` directories in an existing project.

After setup, verify the generated files:

```bash
test "$(cat CLAUDE.md)" = "@AGENTS.md"
for skill_dir in .agents/skills/*; do
  skill_name="$(basename "$skill_dir")"
  test -f ".claude/skills/$skill_name/SKILL.md"
done
```
