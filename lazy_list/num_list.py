from __future__ import annotations

import math
import operator
import statistics
from typing import Callable, List, Literal, Tuple, Union

from lazy_list.eager_list import EagerList
from lazy_list.wrappers import keep_type, safe_execution

Numeric = Union[int, float, bool]


class NumList(EagerList[Numeric]):
    """The `NumList` class is a subclass of `EagerList`, which provides additional methods that are useful for
    numerical operations. The `NumList` class supports all the methods of the `EagerList` class, plus additional
    numerical methods, such as `pow`, `inverse`, `ceil`, `floor`, `exp`, `log`, `sqrt`, and more."""

    @keep_type
    def safe_map(
        self,
        func: Callable[[Numeric], Numeric],
        exceptions: List[Exception] | None = None,
        default=math.nan,
    ):
        """Map `func` over the list. If function raises an exception, the default value is returned.
        By default `ValueError`, `TypeError`, and `ZeroDivisionError` are caught.
        """
        return self.map(safe_execution(func, exceptions=exceptions, default=default))

    @keep_type
    def pow(self, exponent: Numeric) -> NumList:
        """Raises each element in the list to the power of `exponent`."""
        return self.map(lambda x: math.pow(x, exponent))

    @keep_type
    def inverse(self) -> NumList:
        """Computes the reciprocal of each element in the list."""
        return self.map(lambda x: 1 / x)

    @keep_type
    def ceil(self) -> NumList:
        """Rounds each element up to the nearest integer."""
        return NumList(self.map(math.ceil))

    @keep_type
    def floor(self) -> NumList:
        """Rounds each element down to the nearest integer."""
        return self.map(math.floor)

    @keep_type
    def exp(self) -> NumList:
        """Computes the exponential of each element in the list."""
        return self.map(math.exp)

    @keep_type
    def exp_n(self, value: Numeric) -> NumList:
        """Raises `value` to the power of each element in the list."""
        return self.map(lambda x: value**x)

    @keep_type
    def abs(self) -> NumList:
        """Computes the absolute value of each element in the list."""
        return self.map(abs)

    def is_close(self, value, rel_tol: float = 1e-9, abs_tol: float = 0) -> EagerList[bool]:
        """Returns a boolean list that indicates whether each element in the list is close to the given `value`, within
        a relative tolerance of `rel_tol` or an absolute tolerance of `abs_tol`."""
        return self.map(lambda x: math.isclose(x, value, rel_tol=rel_tol, abs_tol=abs_tol))

    def is_finite(self) -> EagerList[bool]:
        """Returns a boolean list that indicates whether each element in the list is a finite number."""
        return self.map(math.isfinite)

    def is_inf(self) -> EagerList[bool]:
        """Returns a boolean list that indicates whether each element in the list is positive or negative infinity."""
        return self.map(math.isinf)

    def is_nan(self) -> EagerList[bool]:
        """Returns a boolean list that indicates whether each element in the list is NaN (not a number)."""
        return self.map(math.isnan)

    @keep_type
    def log(self, base=math.e) -> NumList:
        """
        log(x, [base=math.e]) Return the logarithm of x to the given base.
        If the base not specified, returns the natural logarithm (base e) of x.
        """
        return self.map(lambda x: math.log(x, base))

    @keep_type
    def log10(self) -> NumList:
        """Return the base 10 logarithm of x."""
        return self.map(math.log10)

    @keep_type
    def log1p(self) -> NumList:
        """
        Return the natural logarithm of 1+x (base e).
        The result is computed in a way which is accurate for x near zero.
        """
        return self.map(math.log1p)

    @keep_type
    def log2(self) -> NumList:
        """Return the base 2 logarithm of x."""
        return self.map(math.log2)

    def modf(self) -> EagerList[Tuple[float, float]]:
        """
        Return the fractional and integer parts of x.
        Both results carry the sign of x and are floats.
        """
        return self.map(lambda x: math.modf(x))

    @keep_type
    def mod(self, value: Numeric) -> NumList:
        """Same as % operation"""
        return self.map(lambda x: operator.mod(x, value))

    @keep_type
    def remainder(self, value: Numeric) -> NumList:
        """
        Difference between x and the closest integer multiple of y.
        Unlike mod (%) the value can be negative.

        Return x - n*y where n*y is the closest integer multiple of y. In the case
        where x is exactly halfway between two multiples of y, the nearest even value
        of n is used. The result is always exact."""
        return self.map(lambda x: math.remainder(x, value))

    @keep_type
    def sqrt(self) -> NumList:
        """Computes the square root of each element in the list."""
        return self.map(math.sqrt)

    @keep_type
    def root(self, degree: Numeric) -> NumList:
        """Computes the `degree`-th root of each element in the list."""
        return self.pow(1 / degree)

    @keep_type
    def trunc(self) -> NumList:
        """Truncates the Real x to the nearest Integral toward 0.

        Uses the __trunc__ magic method."""
        return self.map(math.trunc)

    @keep_type
    def add(self, value) -> NumList:
        """Add `value` to each element"""
        return self.map(lambda x: x + value)

    @keep_type
    def sub(self, value) -> NumList:
        """Subtract `value` from each element"""
        return self.map(lambda x: x - value)

    @keep_type
    def mul(self, value) -> NumList:
        """Multiply each element by `value`"""
        return self.map(lambda x: x * value)

    @keep_type
    def div(self, value) -> NumList:
        """Divide each element by `value`"""
        return self.map(lambda x: x / value)

    def max(self) -> Numeric:
        """Return maximum value"""
        return max(self)

    def min(self) -> Numeric:
        """Return minimum value"""
        return min(self)

    def mean(self) -> Numeric:
        """Return the sample arithmetic mean"""
        return statistics.mean(self)

    def harmonic_mean(self) -> Numeric:
        """Return the harmonic mean
        The harmonic mean, sometimes called the subcontrary mean, is the reciprocal of
        the arithmetic mean of the reciprocals of the data, and is often appropriate when
        averaging quantities which are rates or ratios, for example speeds.
        harmonic_mean([a, b, c]) == 3 / (1/a + 1/b + 1/c)
        """
        return statistics.harmonic_mean(self)

    def geometric_mean(self) -> Numeric:
        """Convert data to floats and compute the geometric mean"""
        return statistics.geometric_mean(self)

    def median(self) -> Numeric:
        """Return the median (middle value)."""
        return statistics.median(self)

    def sum(self) -> Numeric:
        """Return sum of all elements."""
        return sum(self)

    @keep_type
    def cum_sum(self) -> NumList:
        """return cumulative sum of elements"""
        return self.accumulate(operator.add)

    def std_dev(self) -> Numeric:
        """Return the square root of the sample variance."""
        return statistics.stdev(self)

    def variance(self) -> Numeric:
        """Return the sample variance of elements."""
        return statistics.variance(self)

    @keep_type
    def quantiles(
        self, n: int = 4, method: Literal["inclusive", "exclusive"] = "exclusive"
    ) -> NumList:
        """Divide *data* into *n* continuous intervals with equal probability.

        Returns a list of (n - 1) cut points separating the intervals."""
        return statistics.quantiles(self, n=n, method=method)

    @keep_type
    def window_reduce(
        self, window: int, function: Callable[[Tuple[Numeric, ...], Numeric]]
    ) -> NumList:
        """
        Apply a function over windows of size `n`.
        E.g., moving average with window size of 4:
        >>> lst = NumList(range(10))
        >>> lst.window_reduce(4, lambda *x: sum(x)/len(x))
        # NumList([1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5])
        """
        return self.sliding_window(window).map(lambda x: function(*x))

    @keep_type
    def diff(self):
        """
        Difference between consecutive elements.
        >>> lst = NumList([1, 2, 4, 8])
        >>> diff = lst.diff()
        # NumList([1, 2, 4])"""
        return self.window_reduce(2, lambda x, y: y - x)

    @keep_type
    def moving_average(self, window: int) -> NumList:
        """Moving average of the sequence"""
        return self.window_reduce(window, lambda *x: sum(x) / len(x))
