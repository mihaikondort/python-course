"""LRU cache kata — the single most common "design a class" question."""

from typing import Any


class LRUCache:
    """A fixed-capacity least-recently-used cache.

    Both ``get`` and ``put`` must be O(1). Two accepted implementations:

    1. ``collections.OrderedDict`` + ``move_to_end`` — the pragmatic answer.
    2. A hash map plus a doubly linked list you maintain yourself — the answer
       they usually actually want, since it shows you know *why* it is O(1).

    Reading a key and overwriting a key both count as "recently used".
    """

    def __init__(self, capacity: int) -> None:
        """Raise ``ValueError`` if ``capacity < 1``."""
        raise NotImplementedError

    def get(self, key: str) -> Any:
        """Return the value, or ``None`` if absent. Marks the key as recent."""
        raise NotImplementedError

    def put(self, key: str, value: Any) -> None:
        """Insert or update, evicting the least recently used key if over capacity."""
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __contains__(self, key: str) -> bool:
        """Membership must NOT count as a use — no side effects."""
        raise NotImplementedError


class TTLCache:
    """A cache whose entries expire after ``ttl`` seconds.

    Take a ``time_func`` in ``__init__`` (defaulting to ``time.monotonic``) so
    tests can inject a fake clock — being asked "how would you test this?" is
    part of the exercise.
    """

    def __init__(self, ttl: float, time_func: Any = None) -> None:
        raise NotImplementedError

    def get(self, key: str) -> Any:
        """Return the value, or ``None`` if missing or expired."""
        raise NotImplementedError

    def put(self, key: str, value: Any) -> None:
        raise NotImplementedError
