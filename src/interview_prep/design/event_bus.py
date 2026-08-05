"""Event bus / observer kata.

Follow-up questions to prepare: how do you avoid leaking subscribers (weak
references), what happens when one handler raises, and how would you make
delivery asynchronous?
"""

from collections.abc import Callable
from typing import Any

Handler = Callable[..., None]


class EventBus:
    """A synchronous publish/subscribe bus."""

    def __init__(self) -> None:
        raise NotImplementedError

    def subscribe(self, event: str, handler: Handler) -> Callable[[], None]:
        """Register ``handler`` for ``event`` and return an unsubscribe callable."""
        raise NotImplementedError

    def unsubscribe(self, event: str, handler: Handler) -> None:
        """Remove ``handler``. Removing an unregistered handler is a no-op."""
        raise NotImplementedError

    def publish(self, event: str, *args: Any, **kwargs: Any) -> int:
        """Call every handler in subscription order; return how many ran.

        A handler raising must not stop the others — collect the failures and
        re-raise them as an ``ExceptionGroup`` once all handlers have run.
        """
        raise NotImplementedError

    def subscribers(self, event: str) -> list[Handler]:
        """Return the handlers for ``event`` (a copy, not the internal list)."""
        raise NotImplementedError


class StateMachine:
    """A finite state machine with declared transitions.

    ``transitions`` maps ``(state, event) -> next_state``. An undeclared
    transition raises ``ValueError`` and leaves the state unchanged. Record
    every applied transition in ``history``.
    """

    def __init__(self, initial: str, transitions: dict[tuple[str, str], str]) -> None:
        raise NotImplementedError

    @property
    def state(self) -> str:
        raise NotImplementedError

    def fire(self, event: str) -> str:
        """Apply ``event`` and return the new state."""
        raise NotImplementedError

    def can_fire(self, event: str) -> bool:
        raise NotImplementedError
