"""Decorator drills.

Every one of these must preserve ``__name__``/``__doc__`` (``functools.wraps``)
and work on functions taking arbitrary ``*args``/``**kwargs``.
"""

from collections.abc import Callable
from typing import Any, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def timer(func: F) -> F:
    """Log the wall-clock duration of each call to ``func``.

    Write the duration in seconds to ``func.__wrapped_durations__`` (a list you
    attach to the wrapper) so it is testable without capturing stdout.
    """
    raise NotImplementedError


def memoize(func: F) -> F:
    """Cache results keyed by the call arguments.

    Handle keyword arguments correctly, expose ``wrapper.cache_clear()`` and
    ``wrapper.cache_info()`` returning ``(hits, misses)``.
    Then: explain when you would just use ``functools.lru_cache`` instead.
    """
    raise NotImplementedError


def retry(times: int = 3, exceptions: tuple[type[BaseException], ...] = (Exception,)) -> Callable[[F], F]:
    """Return a decorator retrying the call up to ``times`` total attempts.

    Only the listed ``exceptions`` trigger a retry; the last failure is
    re-raised. Raise ``ValueError`` if ``times < 1``.
    """
    raise NotImplementedError


def count_calls(func: F) -> F:
    """Track how many times ``func`` was called in ``wrapper.calls``."""
    raise NotImplementedError


def validate_types(func: F) -> F:
    """Check arguments against the function's annotations at call time.

    Raise ``TypeError`` with a helpful message on a mismatch. Unannotated
    parameters are not checked. Hint: ``inspect.signature`` +
    ``sig.bind(*args, **kwargs)``.
    """
    raise NotImplementedError


def singleton(cls: type) -> type:
    """Make a class return the same instance on every instantiation.

    Then: explain why this pattern is often a smell in Python and what you'd
    use instead (module-level object, dependency injection).
    """
    raise NotImplementedError
