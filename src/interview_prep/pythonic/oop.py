"""OOP and data-model drills.

These probe ``__dunder__`` methods, dataclasses, properties, ABCs and the
descriptor protocol — the usual "how well do you know Python objects" round.
"""

from __future__ import annotations

from typing import Any


class Vector:
    """A 2D vector supporting Python's operator protocol.

    Implement: ``__init__(x, y)``, ``__repr__`` (round-trippable), ``__eq__``,
    ``__hash__`` (immutable value semantics), ``__add__``, ``__sub__``,
    ``__mul__`` (scalar, both sides via ``__rmul__``), ``__abs__`` (magnitude),
    ``__iter__``, ``__len__`` (always 2) and ``__bool__``.
    """

    def __init__(self, x: float, y: float) -> None:
        raise NotImplementedError


class Temperature:
    """A temperature stored in Celsius, exposed both ways.

    ``celsius`` is a property that rejects values below absolute zero
    (-273.15) with ``ValueError``. ``fahrenheit`` is a computed property with a
    working setter. Add a ``from_fahrenheit`` classmethod.
    """

    def __init__(self, celsius: float) -> None:
        raise NotImplementedError


class Shape:
    """An abstract base class for shapes.

    Use ``abc.ABC``: abstract ``area()`` and ``perimeter()``, plus a concrete
    ``describe()`` using them. Instantiating ``Shape`` must raise ``TypeError``.
    """


class Circle(Shape):
    """A circle. Implement ``area`` and ``perimeter``; reject a negative radius."""

    def __init__(self, radius: float) -> None:
        raise NotImplementedError


class Rectangle(Shape):
    """A rectangle. Implement ``area`` and ``perimeter``; reject negative sides."""

    def __init__(self, width: float, height: float) -> None:
        raise NotImplementedError


class TypedField:
    """A data descriptor enforcing an attribute's type.

    Usage::

        class Person:
            name = TypedField(str)
            age = TypedField(int)

    Assigning the wrong type raises ``TypeError``. Store per-instance values so
    two instances never share state — that's the classic descriptor bug. Use
    ``__set_name__`` to learn the attribute name.
    """

    def __init__(self, expected_type: type) -> None:
        raise NotImplementedError

    def __set_name__(self, owner: type, name: str) -> None:
        raise NotImplementedError

    def __get__(self, obj: Any, objtype: type | None = None) -> Any:
        raise NotImplementedError

    def __set__(self, obj: Any, value: Any) -> None:
        raise NotImplementedError


class Stack:
    """A LIFO stack over a list.

    Implement ``push``, ``pop`` (``IndexError`` when empty), ``peek``,
    ``__len__``, ``__bool__`` and ``__contains__``.
    """

    def __init__(self) -> None:
        raise NotImplementedError
