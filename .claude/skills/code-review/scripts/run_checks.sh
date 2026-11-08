#!/usr/bin/env bash
# Automated pre-review checks for the advanced_python repo.
# Usage: run_checks.sh [paths...]   (no args = changed + untracked .py files)
set -u

repo_root="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$repo_root" || exit 1

if [ "$#" -gt 0 ]; then
  targets=("$@")
else
  targets=()
  while IFS= read -r f; do
    [ -n "$f" ] && [ -f "$f" ] && targets+=("$f")
  done < <({ git diff --name-only HEAD; git ls-files --others --exclude-standard; } | grep -E '\.py$' | sort -u)
fi

if [ "${#targets[@]}" -eq 0 ]; then
  echo "No Python files to check."
  exit 0
fi

echo "== Targets"
printf '  %s\n' "${targets[@]}"

echo
echo "== ruff check"
if command -v ruff >/dev/null 2>&1; then
  ruff check "${targets[@]}" || true
else
  echo "  ruff not found; skipped"
fi

echo
echo "== ruff format --check"
if command -v ruff >/dev/null 2>&1; then
  ruff format --check "${targets[@]}" || true
fi

echo
echo "== Byte-compile"
uv run --quiet python -m py_compile $(find "${targets[@]}" -name '*.py' -type f) && echo "  OK"

echo
echo "== Non-snake_case function/variable names"
# def camelCase(...) or camelCase = ... at any indentation
grep -rnE --include='*.py' '^\s*(async\s+)?def\s+[a-z]+[A-Z][A-Za-z0-9]*\s*\(|^\s*[a-z]+[A-Z][A-Za-z0-9]*\s*(:[^=]+)?=[^=]' "${targets[@]}" \
  || echo "  none found"
