"""Show how many drills are still stubbed out.

Usage::

    python scripts/progress.py
"""

from __future__ import annotations

import ast
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "src" / "interview_prep"


def count_stubs(path: Path) -> tuple[int, int]:
    """Return ``(implemented, total)`` for the callables defined in ``path``."""
    tree = ast.parse(path.read_text(encoding="utf-8"))
    implemented = total = 0
    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef):
            continue
        total += 1
        body = [n for n in node.body if not isinstance(n, ast.Expr)]
        is_stub = len(body) == 1 and (
            isinstance(body[0], ast.Raise)
            and isinstance(body[0].exc, ast.Name)
            and body[0].exc.id == "NotImplementedError"
        )
        if not is_stub:
            implemented += 1
    return implemented, total


def bar(done: int, total: int, width: int = 24) -> str:
    filled = round(width * done / total) if total else width
    return "#" * filled + "." * (width - filled)


def main() -> int:
    modules = sorted(p for p in SRC.rglob("*.py") if p.name != "__init__.py")
    if not modules:
        print("No drill modules found.", file=sys.stderr)
        return 1

    grand_done = grand_total = 0
    current_group = ""
    for module in modules:
        group = module.parent.name
        if group != current_group:
            current_group = group
            print(f"\n{group}/")
        done, total = count_stubs(module)
        grand_done += done
        grand_total += total
        print(f"  {module.stem:<24} [{bar(done, total)}] {done:>2}/{total}")

    pct = 100 * grand_done / grand_total if grand_total else 100
    print(f"\nTotal: {grand_done}/{grand_total} implemented ({pct:.0f}%)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
