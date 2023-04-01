from __future__ import annotations

from typing import Any, Callable, Iterable, List, TypeVar

T = TypeVar("T")

DEFAULT_EXCEPTIONS = (ValueError, TypeError, ZeroDivisionError)


def keep_type(func: Callable[[T, Any], Iterable[T]]) -> T:
    """A decorator that ensures that the returned value of a method call is of the same type
    as the object that the method was called on."""

    def wrapper(self: T, *args, **kwargs):
        return type(self)(func(self, *args, **kwargs))

    return wrapper


def catch_exceptions(func, exceptions: List[Exception] = None, default=None):
    """A decorator which makes a function to return a default value if an exception is raised."""
    _exceptions = exceptions or DEFAULT_EXCEPTIONS

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except _exceptions:
            return default

    return wrapper
