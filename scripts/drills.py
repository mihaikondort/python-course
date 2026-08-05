"""List every drill, its status, and the exact command to run it.

Usage::

    python scripts/drills.py                 # all drills
    python scripts/drills.py arrays          # only files matching "arrays"
    python scripts/drills.py --todo          # only drills you haven't done
"""

from __future__ import annotations

import ast
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TESTS = ROOT / "tests"


def case_count(func: ast.FunctionDef) -> int:
    """Return how many cases a test function expands to, honouring @parametrize."""
    for decorator in func.decorator_list:
        if not isinstance(decorator, ast.Call):
            continue
        name = ast.unparse(decorator.func)
        if "parametrize" not in name:
            continue
        # parametrize(argnames, argvalues) — the second positional arg is the cases.
        if len(decorator.args) >= 2 and isinstance(decorator.args[1], ast.List | ast.Tuple):
            return len(decorator.args[1].elts)
    return 1


def drill_classes(path: Path) -> list[tuple[str, int]]:
    """Return ``(class_name, test_count)`` for each ``Test*`` class in ``path``."""
    tree = ast.parse(path.read_text(encoding="utf-8"))
    drills = []
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name.startswith("Test"):
            count = sum(
                case_count(child)
                for child in node.body
                if isinstance(child, ast.FunctionDef) and child.name.startswith("test")
            )
            drills.append((node.name, count))
    return drills


def passing_node_ids() -> set[str]:
    """Run the suite quietly and return the node ids that currently pass."""
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "--tb=no", "-q", "--no-header", "-p", "no:cacheprovider"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    return {
        line.split(" ")[1].split("::")[0] + "::" + line.split("::")[1]
        for line in result.stdout.splitlines()
        if line.startswith(("FAILED ", "ERROR "))
        and "::" in line
        and len(line.split("::")) > 1
    }


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    todo_only = "--todo" in sys.argv
    pattern = args[0] if args else ""

    files = sorted(p for p in TESTS.glob("test_*.py") if pattern in p.name)
    if not files:
        print(f"No test files matching {pattern!r}", file=sys.stderr)
        return 1

    print("Checking which drills already pass...\n", file=sys.stderr)
    broken = passing_node_ids()

    total = done = 0
    for path in files:
        rel = f"tests/{path.name}"
        rows = []
        for name, count in drill_classes(path):
            total += 1
            is_done = f"{rel}::{name}" not in broken
            done += is_done
            if todo_only and is_done:
                continue
            mark = "[x]" if is_done else "[ ]"
            rows.append(f"  {mark} {name:<32} ({count} tests)")
            rows.append(f"      pytest {rel}::{name} -x")
        if rows:
            print(f"\n{rel}")
            print("\n".join(rows))

    print(f"\n{done}/{total} drills complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
