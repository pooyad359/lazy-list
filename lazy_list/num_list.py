from __future__ import annotations
import math
import statistics
import operator
from typing import Union
from lazy_list.eager_list import EagerList

Numeric = Union[int, float, bool]


class NumEagerList(EagerList[Numeric]):
    def pow(self, exponent) -> NumEagerList[Numeric]:
        return self.map(lambda x: math.pow(x, exponent))

    def ceil(self) -> NumEagerList[Numeric]:
        ...

    def floor(self) -> NumEagerList[Numeric]:
        ...

    def exp(self) -> NumEagerList[Numeric]:
        ...

    def abs(self) -> NumEagerList[Numeric]:
        ...

    def is_close(self, value) -> NumEagerList[Numeric]:
        ...

    def is_finite(self) -> NumEagerList[Numeric]:
        ...

    def is_inf(self) -> NumEagerList[Numeric]:
        ...

    def is_nan(self) -> NumEagerList[Numeric]:
        ...

    def log(self) -> NumEagerList[Numeric]:
        ...

    def log10(self) -> NumEagerList[Numeric]:
        ...

    def log1p(self) -> NumEagerList[Numeric]:
        ...

    def log2(self) -> NumEagerList[Numeric]:
        ...

    def modf(self, value) -> NumEagerList[Numeric]:
        ...

    def mod(self, value) -> NumEagerList[Numeric]:
        ...

    def remainder(self, value) -> NumEagerList[Numeric]:
        ...

    def sqrt(self) -> NumEagerList[Numeric]:
        ...

    def root(self, degree) -> NumEagerList[Numeric]:
        ...

    def trunc(self) -> NumEagerList[Numeric]:
        ...

    def add(self, value) -> NumEagerList[Numeric]:
        ...

    def sub(self, value) -> NumEagerList[Numeric]:
        ...

    def mul(self, value) -> NumEagerList[Numeric]:
        ...

    def div(self, value) -> NumEagerList[Numeric]:
        ...

    def div_safe(self, value) -> NumEagerList[Numeric]:
        ...

    def max(self) -> NumEagerList[Numeric]:
        ...

    def min(self) -> NumEagerList[Numeric]:
        ...

    def mean(self) -> NumEagerList[Numeric]:
        ...

    def harmonic_mean(self) -> NumEagerList[Numeric]:
        ...

    def geometric_mean(self) -> NumEagerList[Numeric]:
        ...

    def median(self) -> NumEagerList[Numeric]:
        ...

    def n_unique(self) -> NumEagerList[Numeric]:
        ...

    def sum(self) -> NumEagerList[Numeric]:
        ...

    def cum_sum(self) -> NumEagerList[Numeric]:
        ...

    def std_dev(self) -> NumEagerList[Numeric]:
        ...

    def variance(self) -> NumEagerList[Numeric]:
        ...
