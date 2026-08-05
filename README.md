# Python Interview Prep

A drill kit for practising Python developer interviews. Every exercise is a
stubbed function with a full test suite already written — your job is to make
the tests pass, out loud, under time pressure.

## Setup

```bash
uv venv
uv pip install -e ".[dev]"
pre-commit install            # optional, but shows good practice in a repo
```

Then activate the environment — once per terminal window:

| Shell | Command |
|-------|---------|
| PowerShell | `.venv\Scripts\Activate.ps1` |
| cmd.exe | `.venv\Scripts\activate.bat` |
| bash / zsh | `source .venv/bin/activate` |

Your prompt gains a `(python-interview-prep)` prefix when it works. To skip
activation entirely, prefix commands with `.venv\Scripts\python.exe -m` instead.

## Keeping your solutions out of `main`

`main` is the pristine kit: every drill is a stub. Keep your answers on a branch
so the repo stays usable from scratch — by you next year, or by anyone who
clones it:

```bash
git checkout -b my-progress     # once
# ...solve drills, commit freely on this branch...
```

Don't push `my-progress` (or push it only to a private fork). To reset a single
drill and redo it from scratch:

```bash
git checkout main -- src/interview_prep/algorithms/arrays_strings.py
```

To wipe all your answers and start over completely:

```bash
git checkout main -- src/
```

## Finding your next drill

**This is the command to start every session with:**

```bash
python scripts/drills.py --todo
```

It lists every drill you haven't finished, with the exact `pytest` command to
run it, and `[x]`/`[ ]` for done/not done. Pick the top one and copy its command.

```
tests/test_arrays_strings.py
  [x] TestTwoSum                       (7 tests)
      pytest tests/test_arrays_strings.py::TestTwoSum -x
  [ ] TestMaxSubarraySum               (5 tests)
      pytest tests/test_arrays_strings.py::TestMaxSubarraySum -x
```

Narrow it to one topic by passing part of a filename:

```bash
python scripts/drills.py trees      # only tests/test_trees.py
python scripts/drills.py            # everything, done and not done
```

## The loop

```bash
python scripts/drills.py --todo                       # 1. what's next?
pytest tests/test_arrays_strings.py::TestTwoSum -x    # 2. run it — fails, points at the stub
                                                      # 3. implement it in src/
pytest tests/test_arrays_strings.py::TestTwoSum       # 4. all cases green?
```

Then, before you move on:

```bash
ruff check . && mypy && pytest tests/test_arrays_strings.py
```

Other useful runs:

```bash
pytest tests/test_arrays_strings.py    # a whole module
pytest --lf                            # only what failed last time
pytest                                 # everything
python scripts/progress.py             # per-module progress bars
```

## What's in here

| Area | Modules | What it drills |
|------|---------|----------------|
| Algorithms | `arrays_strings`, `linked_list`, `trees`, `graphs`, `dynamic_programming`, `sorting_searching` | The standard whiteboard round |
| Python language | `decorators`, `generators`, `context_managers`, `oop`, `concurrency` | The "are you actually a Python dev" round |
| Design | `lru_cache`, `rate_limiter`, `event_bus` | "Design this class in 30 minutes" |

Stubs live in [src/interview_prep/](src/interview_prep/), tests in [tests/](tests/).

## How to practise

1. **Time yourself.** 20 minutes per algorithm drill, 30 per design kata. Real
   interviews are timed; practising untimed builds the wrong reflex.
2. **Talk while you type.** State the approach and the complexity *before*
   writing code. Interviewers score communication as heavily as the solution.
3. **Read the docstring's target complexity.** A working O(n²) answer where
   O(n) exists usually reads as a fail.
4. **Write the brute force first, then optimise** — out loud. That progression
   is exactly what they want to see.
5. **Redo, don't just do.** Delete your solution a week later and redo it.
   Recall beats recognition.

### Suggested order

1. `arrays_strings` → `sorting_searching` → `linked_list` (warm-up, high frequency)
2. `trees` → `graphs` (mid-difficulty, very common)
3. `decorators` → `generators` → `context_managers` → `oop` (Python-specific depth)
4. `dynamic_programming` (hardest, most pattern-driven)
5. `design` katas (senior rounds)
6. `concurrency` (asked when the job mentions async, scraping, or pipelines)

## Verbal questions to prepare

The code drills won't cover these, but they come up in almost every screen:

- Why is `[]` a dangerous default argument value?
- `is` vs `==`; `__eq__` vs `__hash__` and the contract between them.
- What does the GIL actually prevent, and what does it not?
- Shallow vs deep copy; mutable default and mutable-argument gotchas.
- Generators vs lists: memory, laziness, and one-shot consumption.
- `@staticmethod` vs `@classmethod` vs plain method.
- How does MRO work, and what does `super()` really do?
- `__slots__`: what it buys you and what it costs.
- List/dict/set: average and worst-case complexity of the common operations.
- What does `asyncio` give you that threads don't?
- How do you profile a slow Python function? (`cProfile`, `timeit`, `line_profiler`)
- Virtual environments, `pyproject.toml`, and how you'd pin dependencies.

## Reference solutions

There deliberately aren't any. Looking one up teaches recognition; deriving it
teaches recall, and interviews test recall. If you get truly stuck, look up the
*technique* (e.g. "sliding window"), not the solution.
