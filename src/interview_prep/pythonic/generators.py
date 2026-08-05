"""Generator and iterator drills.

The theme: laziness. None of these may materialise the whole input.
"""

from collections.abc import Callable, Iterable, Iterator
from typing import TypeVar

T = TypeVar("T")


def take(iterable: Iterable[T], n: int) -> Iterator[T]:
    """Yield at most the first ``n`` items. Must not consume more than needed."""
    raise NotImplementedError


def chunked(iterable: Iterable[T], size: int) -> Iterator[list[T]]:
    """Yield consecutive chunks of ``size`` items; the last may be shorter.

    Raise ``ValueError`` if ``size < 1``.
    """
    raise NotImplementedError


def flatten(nested: Iterable[object]) -> Iterator[object]:
    """Recursively flatten arbitrarily nested iterables.

    Strings and bytes count as scalars, not iterables — that trap is the point.
    """
    raise NotImplementedError


def unique(iterable: Iterable[T]) -> Iterator[T]:
    """Yield items in order, skipping any value seen before.

    Assume items are hashable.
    """
    raise NotImplementedError


def sliding_window(iterable: Iterable[T], size: int) -> Iterator[tuple[T, ...]]:
    """Yield overlapping windows of ``size`` consecutive items.

    Yield nothing if the input is shorter than ``size``. Hint: ``collections.deque``.
    """
    raise NotImplementedError


def infinite_counter(start: int = 0, step: int = 1) -> Iterator[int]:
    """Yield ``start``, ``start + step``, ... forever."""
    raise NotImplementedError


def read_large_file(path: str, chunk_lines: int = 1000) -> Iterator[list[str]]:
    """Yield the file's lines in batches without loading it all into memory.

    Lines have their trailing newline stripped.
    """
    raise NotImplementedError


def pipeline(source: Iterable[T], *stages: Callable[[Iterator[T]], Iterator[T]]) -> Iterator[T]:
    """Compose generator stages left to right into one lazy pipeline."""
    raise NotImplementedError
