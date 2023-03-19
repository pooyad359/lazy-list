from __future__ import annotations

from typing import Any, Callable, Iterable, TypeVar

T = TypeVar("T")

DEFAULT_EXCEPTIONS = (ValueError, TypeError, ZeroDivisionError)


def keep_type(func: Callable[[T, Any], Iterable[T]]) -> T:
    """A decorator that ensures that the returned value of a method call is of the same type
    as the object that the method was called on."""

    def wrapper(self: T, *args, **kwargs):
        return type(self)(func(self, *args, **kwargs))

    return wrapper


def safe_execution(func, exceptions=None, default=None):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except DEFAULT_EXCEPTIONS:
            return default

    return wrapper
