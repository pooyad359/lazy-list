from __future__ import annotations

import itertools
import random
import statistics
from collections import deque
from functools import reduce
from operator import attrgetter, itemgetter, methodcaller
from typing import Any, Callable, Deque, Dict, Hashable, Iterable, List, Sequence, Set, Tuple, TypeVar, overload

from toolz import itertoolz

X = TypeVar("X")
Y = TypeVar("Y")
Y1 = TypeVar("Y1")
Y2 = TypeVar("Y2")
Y3 = TypeVar("Y3")
Y4 = TypeVar("Y4")


class EagerList(List[X]):
    def __str__(self) -> str:
        return f"EagerList{list(self)}"

    def __repr__(self) -> str:
        return f"EagerList({list(self)})"

    def map(self, function: Callable[[X], Y]) -> "EagerList[Y]":
        """Map function over elements of the list"""
        return EagerList(map(function, self))

    def filter(self, function: Callable[[X], Y] | None = None) -> "EagerList[X]":
        """Return an iterator yielding those items of iterable for which function(item)
        is true. If function is None, return the items that are true."""
        return EagerList(filter(function, self))

    def reduce(self, function: Callable[[X, X], X], initial: X | None = None) -> "EagerList[X]":
        """Apply a function of two arguments cumulatively to the items of a sequence,
        from left to right, so as to reduce the sequence to a single value."""
        if initial is None:
            return reduce(function, self)
        else:
            return reduce(function, self, initial)

    def sort(self, key: Callable[[X], Any] = None, reverse: bool = False) -> "EagerList[X]":
        """Return a new list containing all items from the iterable in ascending order.
        A custom key function can be supplied to customize the sort order, and the
        reverse flag can be set to request the result in descending order."""
        return EagerList(sorted(self, key=key, reverse=reverse))

    def reverse(self) -> "EagerList[X]":
        """Reverse the list"""
        return EagerList(reversed(self))

    def append(self, item) -> "EagerList[X]":
        """Append an item to the end of the list"""
        return EagerList(self + [item])

    def append_left(self, item) -> "EagerList[X]":
        """Append an item to the beginning of the list"""
        return EagerList([item] + self)

    def enumerate(self) -> "EagerList[Tuple[int, X]]":
        """Return a tuple of (index, item) for every item in the list"""
        return EagerList(enumerate(self))

    def clear(self) -> "EagerList[X]":
        """Return an empty list"""
        return EagerList([])

    def copy(self) -> "EagerList[X]":
        """Create a copy of the list"""
        return EagerList(self.to_list().copy())

    def extend(self, *iterables: Iterable[X]) -> "EagerList[X]":
        """Extend by appending items for one or more iterables to the end of the list"""
        return EagerList(itertoolz.concatv(self, *iterables))

    def extend_left(self, *iterables: Iterable[X]) -> "EagerList[X]":
        """Extend by appending items for one or more iterables to the beginning of the list"""
        return EagerList(itertoolz.concatv(*iterables, self))

    def insert(self, index: int, item: X) -> "EagerList[X]":
        """Insert object before index"""
        _list = self.to_list()
        _list.insert(index, item)
        return EagerList(_list)

    def pop(self, index: int = -1) -> "EagerList[X]":
        """Remove item at index (default last)."""
        _list = self.to_list()
        _list.pop(index)
        return EagerList(_list)

    def pop_left(self) -> "EagerList[X]":
        """Remove first item."""
        return self.pop(0)

    def remove(self, value: X) -> "EagerList[X]":
        """Remove first occurrence of value."""
        _list = self.to_list()
        _list.remove(value)
        return EagerList(_list)

    def remove_all(self, value: X) -> "EagerList[X]":
        """Remove all occurrences of value."""
        return self.filter(lambda x: x != value)

    def all(self, function: Callable[[X], bool] | None = None) -> bool:
        """Apply `function` to all items and returns True if they are all True.
        If `function` is `None`, use values directly."""
        return all(self) if function is None else all(self.map(function))

    def any(self, function: Callable[[X], bool] | None = None) -> bool:
        """Apply `function` to all items and returns True if any return True.
        If `function` is `None`, use values directly."""
        return any(self) if function is None else any(self.map(function))

    def fill(self, value: X, start: int, end: int | None = None) -> "EagerList[X]":
        """Create a new list with items from `start` to `end` filled with `value`."""
        _slice = slice(start, end)
        new_list = self.to_list()
        indices = range(*_slice.indices(self.length))
        length = len(indices)
        new_values = [value] * length
        new_list[_slice] = new_values
        return EagerList(new_list)

    def fixed(self, value: Y) -> "EagerList[Y]":
        """Return a list of same size with a fixed value"""
        return EagerList([value] * self.length)

    def slice(self, start: int = None, stop: int = None, step: int = None) -> "EagerList[X]":
        """Use slice to subset the list.
        See: `slice`"""
        _slice = slice(start, stop, step)
        return EagerList(self.to_list()[_slice])

    def contains(self, value: X) -> bool:
        """Check if value is in the list"""
        return value in self

    def join(self, delimiter: str) -> str:
        """Join the items together into a string separated by `delimiter`
        >>> a = EagerList([1, 2, 3])
        >>> a.join(",")
        "1,2,3"
        """
        return delimiter.join(self.map(str))

    def index_last(self, value: X) -> int:
        """Return the last index of value"""
        index = self.reverse().index(value)
        return self.length - 1 - index

    def where(self, predicate: Callable[[X], bool]) -> EagerList[int]:
        """Return indices where predicate returns `True`"""
        return self.enumerate().filter(lambda o: predicate(o[1])).get_item(0)

    @overload
    def zip(self, other: Iterable[Y]) -> "EagerList[Tuple[X, Y]]":
        pass

    @overload
    def zip(self, other1: Iterable[Y1], other2: Iterable[Y2]) -> "EagerList[Tuple[X, Y1, Y2]]":
        pass

    @overload
    def zip(
        self,
        other1: Iterable[Y1],
        other2: Iterable[Y2],
        other3: Iterable[Y3],
    ) -> "EagerList[Tuple[X, Y1, Y2, Y3]]":
        pass

    @overload
    def zip(
        self,
        other1: Iterable[Y1],
        other2: Iterable[Y2],
        other3: Iterable[Y3],
        other4: Iterable[Y4],
    ) -> "EagerList[Tuple[X, Y1, Y2, Y3, Y4]]":
        pass

    @overload
    def zip(
        self,
        other1: Iterable[Any],
        other2: Iterable[Any],
        other3: Iterable[Any],
        other4: Iterable[Any],
        *others: Iterable[Any],
    ) -> "EagerList[Tuple[Any, pass]]":
        pass

    def zip(self, *others):
        return EagerList(zip(self, *others))

    @overload
    def zip_longest(self, other: Iterable[Y]) -> "EagerList[Tuple[X|None, Y|None]]":
        pass

    @overload
    def zip_longest(
        self,
        other1: Iterable[Y1],
        other2: Iterable[Y2],
    ) -> "EagerList[Tuple[X|None, Y1|None, Y2|None]]":
        pass

    @overload
    def zip_longest(
        self,
        other1: Iterable[Y1],
        other2: Iterable[Y2],
        other3: Iterable[Y3],
    ) -> "EagerList[Tuple[X|None, Y1|None, Y2|None, Y3|None]]":
        pass

    @overload
    def zip_longest(
        self,
        other1: Iterable[Y1],
        other2: Iterable[Y2],
        other3: Iterable[Y3],
        other4: Iterable[Y4],
    ) -> "EagerList[Tuple[X|None, Y1|None, Y2|None, Y3|None, Y4|None]]":
        pass

    @overload
    def zip_longest(
        self,
        other1: Iterable[Any],
        other2: Iterable[Any],
        other3: Iterable[Any],
        other4: Iterable[Any],
        *others: Iterable[Any],
    ) -> "EagerList[Tuple[Any, pass]]":
        pass

    def zip_longest(self, *others):
        return EagerList(itertools.zip_longest(self, *others))

    @overload
    def __getitem__(self, index: int) -> X:
        pass

    @overload
    def __getitem__(self, index: Iterable | slice) -> "EagerList[X]":
        pass

    def __getitem__(self, index):
        if isinstance(index, slice):
            return EagerList(self.to_list()[index])
        if isinstance(index, Iterable):
            return EagerList([v for i, v in enumerate(self) if i in index])
        else:
            return self.to_list()[index]

    @overload
    def at(self, index: int) -> X:
        pass

    @overload
    def at(self, index: Iterable | slice) -> "EagerList[X]":
        pass

    def at(self, index):
        """Returns item(s) at index.
        `EagerList.at(index)` is the same as `EagerList[index]`"""
        return self[index]

    def accumulate(self, function: Callable[[X, X], X]) -> "EagerList[X]":
        """Apply function over values cumulatively"""
        return EagerList(itertools.accumulate(self, function))

    def combinations(self, r: int) -> "EagerList[Tuple[X, pass]]":
        """Return successive r-length combinations of elements in the iterable.

        EagerList(range(4)).combinations(3) --> (0,1,2), (0,1,3), (0,2,3), (1,2,3)"""
        return EagerList(itertools.combinations(self, r))

    def combinations_with_replacement(self, r: int) -> "EagerList[Tuple[X, pass]]":
        """Return successive r-length combinations of elements in the iterable allowing
        individual elements to have successive repeats."""
        return EagerList(itertools.combinations_with_replacement(self, r))

    def permutations(self, r: int) -> "EagerList[Tuple[X, pass]]":
        """Return successive r-length permutations of elements in the iterable.

        EagerList(range(3)).permutations(2) --> (0,1), (0,2), (1,0), (1,2), (2,0), (2,1)"""
        return EagerList(itertools.permutations(self, r))

    def product(self, other: Iterable[Y]) -> "EagerList[Tuple[X, Y]]":
        """Cartesian product of input iterables. Equivalent to nested for-loops.
        >>> a = EagerList([1,2])
        >>> b = "AB"
        >>> a.product(b)
        EagerList([(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')])
        """
        return EagerList(itertools.product(self, other))

    def compress(self, selector: Iterable[bool]) -> "EagerList[Tuple[X, pass]]":
        """Return data elements corresponding to true selector elements.
        >>> a = EagerList([1, 2, 3, 4])
        >>> b = [True, False, 1, 0]
        >>> a.compress(b)
        EagerList([1, 3])
        """
        return EagerList(itertools.compress(self, selector))

    def dropwhile(self, predicate: Callable[[X], bool]) -> "EagerList[X]":
        """Drop items from the iterable while predicate(item) is true.

        Afterwards, return every element in the list"""
        return EagerList(itertools.dropwhile(predicate, self))

    def takewhile(self, predicate: Callable[[X], bool]) -> "EagerList[X]":
        """Return successive entries from an iterable as long as the predicate evaluates
        to true for each entry."""
        return EagerList(itertools.takewhile(predicate, self))

    def filterfalse(self, predicate: Callable[[X], bool] | None) -> "EagerList[X]":
        """Return those items of iterable for which function(item) is false.

        If function is None, return the items that are false.
        """
        return EagerList(itertools.filterfalse(predicate, self))

    def loop(self, n: int) -> "EagerList[X]":
        """Loops over the list `n` times"""
        return EagerList(self * n)

    def interleave(self, *iterables: Iterable[X]) -> "EagerList[X]":
        """Interleave a sequence of sequences.
        Example:
        >>> a = EagerList([1,2,3])
        >>> b = [4,5,6]
        >>> a.interleave(b)
        EagerList([1, 4, 2, 5, 3, 6])"""
        return EagerList(itertoolz.interleave([self, *iterables]))

    def unique(self) -> "EagerList[X]":
        """Return only unique elements of a sequence"""
        return EagerList(itertoolz.unique(self))

    def n_unique(self) -> int:
        """Return number of unique elements"""
        return len(set(self))

    def is_distinct(self) -> bool:
        """All values in sequence are distinct"""
        return itertoolz.isdistinct(self)

    def take(self, n: int) -> "EagerList[X]":
        """The first n elements of a sequence"""
        return EagerList(itertoolz.take(n, self))

    def drop(self, n: int) -> "EagerList[X]":
        """The sequence following the first n elements"""
        return EagerList(itertoolz.drop(n, self))

    def take_nth(self, n: int) -> "EagerList[X]":
        """Every nth item in seq"""
        return EagerList(itertoolz.take_nth(n, self))

    def nth(self, n: int) -> "X":
        """The nth element in a sequence. Similar to `EagerList.at(n)` and `EagerList[n]`
        except `n` can only be a single index."""
        return itertoolz.nth(n, self)

    @overload
    def get(self, index: int) -> X:
        pass

    @overload
    def get(self, index: Sequence[int]) -> "EagerList[X]":
        pass

    def get(self, index):
        """
        If index is a single integer, return the element at that index.
        If index is a sequence of integers, return a list of elements at those indices.
        """
        if isinstance(index, int):
            return itertoolz.get(index, self)
        return EagerList(itertoolz.get(index, self))

    def concat(self, iterables: Sequence[Iterable[X]]) -> "EagerList[X]":
        """Extend the list by appending items from other iterables.
        Similar to `EagerList.extend` except iterables are passed in as a sequence instead of arguments.
        """
        return EagerList(itertoolz.concat([self, *iterables]))

    def interpose(self, value: X) -> "EagerList[X]":
        """Introduce element between each pair of elements in seq

        Example:
        >>> a = EagerList([1,2,3])
        >>> a.interpose(0)
        EagerList([1, 0, 2, 0, 3])"""
        return EagerList(itertoolz.interpose(value, self))

    def frequencies(self) -> Dict[X, int]:
        """Count the frequency of occurrence for each unique item.

        Example:
        >>> a = EagerList("aaabbcc")
        >>> a.frequencies()
        {'a': 3, 'b': 2, 'c': 2}"""
        return itertoolz.frequencies(self)

    def frequency_tuples(self) -> "EagerList[Tuple[X, int]]":
        """Count the frequency of occurrence for each unique item and return as tuple of items
            and their number of occurrences

        Example:
        >>> a = EagerList("aaabbcc")
        >>> a.frequency_tuples()
        EagerList([('a', 3), ('b', 2), ('c', 2)])
        """
        return EagerList(itertoolz.frequencies(self).items())

    def mode(self) -> X:
        """Return the most common data point from discrete or nominal data.
        If there are multiple modes with same frequency, return the first one encountered"""
        return statistics.mode(self)

    def multi_mode(self) -> "EagerList[X]":
        """Return a list of the most frequently occurring values.

        Will return more than one result if there are multiple modes or an empty list if *data* is empty
        """
        return EagerList(statistics.multimode(self))

    def group_by(self, key: Callable[[X], Y]) -> Dict[Y, EagerList[X]]:
        """Group a collection by a key function

        Example:
        >>> a = EagerList(range(6))
        >>> a.group_by(lambda x: x%2)
        {0: EagerList([0, 2, 4]), 1: EagerList([1, 3, 5])}"""
        return {k: EagerList(v) for k, v in itertoolz.groupby(key, self).items()}

    def reduce_by(self, key: Callable[[X], Y], reducer: Callable[[X, X], X]) -> Dict[Y, X]:
        """Perform a simultaneous groupby (using key) and reduction (using reducer)

        Example:
        >>> a = EagerList(range(6))
        >>> a.reduce_by(lambda x: x % 2, max)
        {0: 4, 1: 5}"""
        return itertoolz.reduceby(key, reducer, self)

    def sliding_window(self, n: int) -> "EagerList[Tuple[X, pass]]":
        """A sequence of overlapping subsequences

        Example:
        >>> a = EagerList(range(5))
        >>> a.sliding_window(2)
        EagerList([(0, 1), (1, 2), (2, 3), (3, 4)])"""
        return EagerList(itertoolz.sliding_window(n, self))

    def partition(self, n: int, pad: str | X = "__no__pad__") -> "EagerList[Tuple[X, pass]]":
        """Partition sequence into tuples of length n.

        Example:
        >>> a = EagerList(range(5))
        >>> a.partition(2)
        EagerList([(0, 1), (2, 3)])  # Note `4` does not appear
        >>> a.partition(2, pad=None)
        EagerList([(0, 1), (2, 3), (4, None)])"""
        return EagerList(itertoolz.partition(n, self, pad=pad))

    def partition_all(self, n: int) -> "EagerList[Tuple[X, pass]]":
        """Partition all elements of sequence into tuples of length at most n
        The final tuple may be shorter to accommodate extra elements.

        Example:
        >>> a = EagerList(range(5))
        >>> a.partition_all(2)
        EagerList([(0, 1), (2, 3), (4,)])
        """
        return EagerList(itertoolz.partition_all(n, self))

    def tail(self, n: int) -> "EagerList[X]":
        """The last n elements of a sequence"""
        return EagerList(itertoolz.tail(n, self))

    def top_k(self, k: int, key: None | Callable[[X], Any] = None) -> "EagerList[X]":
        """Find the k largest elements of a sequence"""
        return EagerList(itertoolz.topk(k, self, key=key))

    def random_sample(
        self,
        k: int = 1,
        weights: Sequence[int | float] | None = None,
        random_state: Any | None = None,
    ) -> "EagerList[X]":
        """Return a k sized EagerList of population elements chosen with replacement"""
        random.seed(random_state)
        return EagerList(random.choices(self, weights, k=k))

    def get_item(self, item: Hashable) -> "EagerList[Any]":
        """Uses `itemgetter` to retrieve items
        item could be index of a sequence or key of dictionary. Equivalent to:
        `EagerList.map(lambda x: x[item])"""
        getter: Callable[[Hashable], Any] = itemgetter(item)
        return self.map(getter)

    def get_attr(self, attribute: str) -> "EagerList[Any]":
        """Uses `attrgetter` to retrieve attributes. Equivalent to:
        `EagerList.map(lambda x: x.attribute)"""
        getter: Callable[[str], Any] = attrgetter(attribute)
        return self.map(getter)

    def find_first(self, predicate: Callable[[X], bool]) -> X:
        """Return the first item where predicate returns `True`"""
        for value in self:
            if predicate(value):
                return value

    def find_first_index(self, predicate: Callable[[X], bool]) -> int:
        """Return the index of first item where predicate returns `True`"""
        value = self.find_first(predicate)
        return self.index(value)

    def find_last(self, predicate: Callable[[X], bool]):
        """Return the last item where predicate returns `True`"""
        for value in reversed(self):
            if predicate(value):
                return value

    def find_last_index(self, predicate: Callable[[X], bool]):
        """Return the index of last item where predicate returns `True`"""
        value = self.find_last(predicate)
        return self.index_last(value)

    def rotate(self, n: int) -> "EagerList[Any]":
        steps = n % self.length
        return EagerList(self[-steps:] + self[:-steps])

    def to_list(self) -> List[X]:
        return list(self)

    def call_method(self, method: str, *args, **kwargs):
        function = methodcaller(method, *args, **kwargs)
        return self.map(function)

    @property
    def length(self) -> int:
        return len(self)

    @property
    def first(self) -> X:
        return self[0]

    @property
    def second(self) -> X:
        return self[1]

    @property
    def last(self) -> X:
        return self[-1]

    def to_set(self) -> Set[X]:
        return set(self)

    def to_deque(self) -> Deque[X]:
        return deque(self)

    @property
    def lazy(self):
        from lazy_list.lazy_list import LazyList

        return LazyList(iter(self))
