---
name: setup-claude
description: Link .claude/skills/ to the canonical .agents/skills/ and write CLAUDE.md as @AGENTS.md, after adding, renaming, or removing a skill.
disable-model-invocation: true
---

# Setup Claude

Claude Code reads project skills from `.claude/skills/`; Codex reads `.agents/skills/` directly. This repo keeps one copy of each skill in `.agents/skills/` and gives Claude Code a symlink per skill (`.claude/skills/<name> -> ../../.agents/skills/<name>`). The links are committed, so a fresh clone works without running this skill. Run it after adding, renaming, or removing a skill.

Edit skills only in `.agents/skills/`.

Run from the repository root:

```bash
mkdir -p .claude/skills
# Remove links whose target skill no longer exists (renamed or deleted skills).
for link in .claude/skills/*; do
  [ -L "$link" ] && [ ! -e "$link" ] && rm "$link"
done
# Link every canonical skill. An old copied directory with the same name is replaced.
for skill_dir in .agents/skills/*/; do
  skill_name="$(basename "$skill_dir")"
  target=".claude/skills/$skill_name"
  [ -L "$target" ] || rm -rf "$target"
  ln -sfn "../../.agents/skills/$skill_name" "$target"
done
printf '@AGENTS.md\n' > CLAUDE.md
```

This touches only entries named after a skill in `.agents/skills/` and dangling links. Other skills in `.claude/skills/` stay as they are.

Verify:

```bash
test "$(cat CLAUDE.md)" = "@AGENTS.md"
for skill_dir in .agents/skills/*/; do
  test -f ".claude/skills/$(basename "$skill_dir")/SKILL.md"
done
```

## Windows

Git checks symlinks out as plain text files on Windows unless Developer Mode is on and `git config core.symlinks true` is set before cloning. If the verify step fails there, use copies instead, and rerun this skill after every skill edit:

```bash
for skill_dir in .agents/skills/*/; do
  skill_name="$(basename "$skill_dir")"
  rm -rf ".claude/skills/$skill_name"
  cp -R "$skill_dir" ".claude/skills/$skill_name"
done
```
