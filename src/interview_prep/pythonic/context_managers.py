"""Context manager drills.

Write some with ``__enter__``/``__exit__`` and some with
``contextlib.contextmanager`` — interviewers ask you to contrast them, and to
explain what returning ``True`` from ``__exit__`` does.
"""

from collections.abc import Iterator
from pathlib import Path
from types import TracebackType
from typing import Any, Self


class Timer:
    """Measure the wall-clock duration of a ``with`` block.

    After the block, ``timer.elapsed`` holds the duration in seconds. It must be
    set even if the block raises, and the exception must still propagate.
    """

    elapsed: float

    def __enter__(self) -> Self:
        raise NotImplementedError

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> bool:
        raise NotImplementedError


class suppress_errors:
    """Swallow the listed exception types raised inside the block.

    Store the swallowed exception on ``self.exception`` (``None`` if the block
    completed cleanly). Exceptions not listed must propagate.
    """

    def __init__(self, *exceptions: type[BaseException]) -> None:
        raise NotImplementedError

    def __enter__(self) -> Self:
        raise NotImplementedError

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> bool:
        raise NotImplementedError


def atomic_write(path: Path) -> Iterator[Any]:
    """Write to a temp file, then atomically replace ``path`` on clean exit.

    On an exception the temp file is removed and ``path`` is left untouched.
    Decorate this with ``@contextlib.contextmanager`` and yield the open handle.
    """
    raise NotImplementedError


def temporary_attribute(obj: object, name: str, value: Any) -> Iterator[None]:
    """Set ``obj.name`` to ``value`` for the block, then restore the old value.

    Restore correctly whether or not the attribute existed before, and even if
    the block raises. Decorate with ``@contextlib.contextmanager``.
    """
    raise NotImplementedError


def working_directory(path: Path) -> Iterator[Path]:
    """``chdir`` into ``path`` for the block and always restore the old cwd."""
    raise NotImplementedError
