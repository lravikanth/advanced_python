---
name: code-review
description: Review Python changes in the advanced_python repo for correctness, snake_case naming, typing, and idiomatic use of advanced Python features (decorators, descriptors, generators, protocols, metaclasses, generics). Use when the user asks to review code, a diff, a file, or a folder in this project.
---

# Code review (advanced_python)

Review Python code in this repo and report concrete, verified findings. This is a learning repo of standalone demo scripts plus a small uv workspace (`expense_tracker` → `tax_calulation`), so judge code by whether it is correct and demonstrates the concept clearly. Don't judge it as production code.

## 1. Pick the target

- If the user named a file, folder, or commit range, review that.
- Otherwise, review uncommitted changes: `git diff HEAD` plus untracked `.py` files from `git status --short`.
- If there is nothing to review, say so and stop.

## 2. Run the automated checks

```bash
bash .claude/skills/code-review/scripts/run_checks.sh [paths...]
```

With no paths, it checks changed/untracked `.py` files. It runs `ruff check`, `ruff format --check`, and a byte-compile, and reports snake_case violations. Treat its output as leads to confirm, not final findings.

## 3. Read and review

Read each target file in full, not just the diff hunks. Review it against [references/checklist.md](references/checklist.md). For each candidate issue:

- Confirm it by reading the surrounding code. Run the script with `uv run python <file>` when behavior is in doubt (run modules under `src/protocols` or `src/abc_protocols` from `src/` with `-m`).
- Drop anything you cannot tie to a concrete failure or a clear convention violation.

## 4. Report

List findings most severe first, grouped as **Bugs**, **Conventions**, and **Suggestions**. For each, give:

- `path:line` as a clickable link
- what's wrong, in one sentence
- the concrete scenario or input that shows it
- a minimal fix

End with one line saying what you checked and anything you couldn't verify. Don't edit files unless the user asks for fixes.
