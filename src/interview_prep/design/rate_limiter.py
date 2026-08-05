"""Rate limiter kata.

Be ready to compare the algorithms: fixed window is trivial but allows a 2x
burst at the boundary; sliding window log is exact but O(requests) memory;
token bucket allows controlled bursts and is what most APIs actually use.
"""

from typing import Any


class TokenBucket:
    """A token bucket allowing bursts up to ``capacity``.

    Tokens refill continuously at ``refill_rate`` per second (compute them
    lazily on each call — do not run a background thread). Inject
    ``time_func`` so tests can drive a fake clock.
    """

    def __init__(self, capacity: int, refill_rate: float, time_func: Any = None) -> None:
        raise NotImplementedError

    def allow(self, tokens: int = 1) -> bool:
        """Consume ``tokens`` and return ``True``, or return ``False`` if short."""
        raise NotImplementedError

    @property
    def available(self) -> float:
        """Current token count, refilled up to now. Never exceeds ``capacity``."""
        raise NotImplementedError


class SlidingWindowLimiter:
    """Allow at most ``limit`` requests per ``window`` seconds, per key.

    Keep a timestamp log per key and evict entries older than the window.
    """

    def __init__(self, limit: int, window: float, time_func: Any = None) -> None:
        raise NotImplementedError

    def allow(self, key: str) -> bool:
        """Record and allow the request, or return ``False`` if over the limit."""
        raise NotImplementedError

    def remaining(self, key: str) -> int:
        """Requests still allowed in the current window for ``key``."""
        raise NotImplementedError
