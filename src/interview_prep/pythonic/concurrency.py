"""Concurrency drills.

The interview question behind all of these: *when do you reach for threads,
processes, or asyncio, and why?* Short version to be able to defend — threads
for I/O-bound work, processes for CPU-bound work (the GIL), asyncio for many
concurrent I/O waits with low per-task overhead.
"""

import asyncio
from collections.abc import Callable, Coroutine, Iterable, Sequence
from typing import Any, TypeVar

T = TypeVar("T")
R = TypeVar("R")


def parallel_map(func: Callable[[T], R], items: Sequence[T], workers: int = 4) -> list[R]:
    """Apply ``func`` to each item using a thread pool, preserving input order.

    Use ``concurrent.futures.ThreadPoolExecutor``. Exceptions from a worker must
    propagate to the caller.
    """
    raise NotImplementedError


def cpu_parallel_map(func: Callable[[T], R], items: Sequence[T], workers: int = 4) -> list[R]:
    """Same, but with a process pool for CPU-bound work.

    Note the constraint this adds: ``func`` and the items must be picklable.
    """
    raise NotImplementedError


class ThreadSafeCounter:
    """A counter safe to increment from many threads.

    Implement ``increment(n=1)``, ``decrement(n=1)`` and a ``value`` property,
    guarding shared state with ``threading.Lock``. Then: explain why
    ``self._count += 1`` is not atomic even with the GIL.
    """

    def __init__(self, start: int = 0) -> None:
        raise NotImplementedError


async def gather_with_limit(
    coros: Iterable[Coroutine[Any, Any, T]], limit: int
) -> list[T]:
    """Run the coroutines with at most ``limit`` in flight, preserving order.

    Hint: ``asyncio.Semaphore`` wrapping each coroutine, then ``asyncio.gather``.
    """
    raise NotImplementedError


async def with_timeout(coro: Coroutine[Any, Any, T], seconds: float, default: T) -> T:
    """Await ``coro``, returning ``default`` if it takes longer than ``seconds``.

    The pending task must be cancelled, not leaked.
    """
    raise NotImplementedError


async def producer_consumer(items: Sequence[int], consumers: int = 3) -> list[int]:
    """Push ``items`` through an ``asyncio.Queue`` to N consumers.

    Return everything the consumers processed (order need not match). Shut the
    workers down cleanly — no hanging tasks, no ``join()`` deadlock.
    """
    raise NotImplementedError


def run_async(coro: Coroutine[Any, Any, T]) -> T:
    """Run a coroutine to completion from sync code (helper, implemented)."""
    return asyncio.run(coro)
