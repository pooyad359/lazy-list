from __future__ import annotations
from collections import deque
from copy import copy
from functools import reduce
import itertools
from operator import itemgetter, attrgetter
from typing import (
    TypeVar,
    List,
    Callable,
    Any,
    overload,
    Tuple,
    Iterable,
    Sequence,
    Dict,
    Hashable,
    Set,
    Deque,
)
import random
from toolz import itertoolz
from lazy_list.eager_list import EagerList

X = TypeVar("X")
Y = TypeVar("Y")
Y1 = TypeVar("Y1")
Y2 = TypeVar("Y2")
Y3 = TypeVar("Y3")
Y4 = TypeVar("Y4")


class LazyList(Iterable[X]):
    def __init__(self, values: Iterable[X]):
        self.__values = iter(values)

    def __str__(self) -> str:
        return f"LazyList(...)"

    def __repr__(self) -> str:
        return f"LazyList(...)"

    def __iter__(self) -> Iterable[X]:
        return self.iterator

    def __eq__(self, other) -> bool:
        return self.zip(other).map(lambda x: x[0] == x[1]).all()

    def to_list(self) -> List[X]:
        return list(self.iterator)

    @property
    def iterator(self):
        iter1, iter2 = itertools.tee(self.__values)
        self.__values = iter1
        return iter2

    def evaluate(self) -> EagerList[X]:
        """Evaluate items and return as `EagerList`"""
        return EagerList(self)

    def map(self, function: Callable[[X], Y]) -> "LazyList[Y]":
        """Map function over elements of the list"""
        return LazyList(map(function, self))

    def filter(self, function: Callable[[X], Y] | None = None) -> "LazyList[X]":
        """Return an iterator yielding those items of iterable for which function(item)
        is true. If function is None, return the items that are true."""
        return LazyList(filter(function, self))

    def reduce(self, function: Callable[[X, X], X], initial: X | None = None) -> "LazyList[X]":
        """Apply a function of two arguments cumulatively to the items of a sequence,
        from left to right, so as to reduce the sequence to a single value."""
        if initial is None:
            return reduce(function, self)
        else:
            return reduce(function, self, initial)

    def sort(self, key: Callable[[X], Any] = None, reverse: bool = False) -> "LazyList[X]":
        """Return a new list containing all items from the iterable in ascending order.
        A custom key function can be supplied to customize the sort order, and the
        reverse flag can be set to request the result in descending order."""
        return LazyList((o for o in sorted(self, key=key, reverse=reverse)))

    def reverse(self) -> "LazyList[X]":
        """Reverse the list.
        It forces LazyList to evaluate, in order to reverse."""
        return LazyList(reversed(self.to_list()))

    def append(self, item) -> "LazyList[X]":
        """Append an item to the end of the list"""
        return LazyList(itertools.chain(self, [item]))

    def append_left(self, item) -> "LazyList[X]":
        """Append an item to the beginning of the list"""
        return LazyList(itertools.chain([item], self))

    def extend(self, *iterables: Iterable[X]) -> "LazyList[X]":
        """Extend by appending items for one or more iterables to the end of the list"""
        return LazyList(itertoolz.concatv(self, *iterables))

    def extend_left(self, *iterables: Iterable[X]) -> "LazyList[X]":
        """Extend by appending items for one or more iterables to the beginning of the list"""
        return LazyList(itertoolz.concatv(*iterables, self))

    def enumerate(self) -> "LazyList[Tuple[int, X]]":
        """Return a tuple of (index, item) for every item in the list"""
        return LazyList(enumerate(self))

    def clear(self) -> "LazyList[X]":
        """Return an empty list"""
        return LazyList([])

    def copy(self) -> "LazyList[X]":
        """Create a copy of the list"""
        return LazyList(self.iterator)

    def insert(self, index: int, item: X) -> "LazyList[X]":
        """Insert object before index"""
        left = self.slice(stop=index)
        right = self.slice(start=index)
        return left.extend([item], right)

    def get_length_eagerly(self) -> int:
        """Returns the length by eagerly evaluating `LazyList` into a `list`"""
        return len(self.to_list())

    def pop(self, index: int = 0) -> "LazyList[X]":
        """Remove item at index (default first)."""
        if index < 0:
            raise ValueError("`index` must be a positive value")
        return LazyList(o for i, o in self.enumerate() if i != index)

    def pop_left(self) -> "LazyList[X]":
        """Remove first item."""
        return self.pop(0)

    def index(self, value: X) -> int:
        for i, v in self.enumerate():
            if v == value:
                return i
        raise ValueError(f"{value} is not in list")

    def remove(self, value: X) -> "LazyList[X]":
        """Remove first occurrence of value."""
        index = self.index(value)
        return self.pop(index)

    def remove_all(self, value: X) -> "LazyList[X]":
        """Remove all occurrences of value."""
        return self.filter(lambda x: x != value)

    def count(self, value: X) -> int:
        return self.filter(lambda x: x == value).get_length_eagerly()

    def all(self, function: Callable[[X], bool] | None = None) -> bool:
        """Apply `function` to all items and returns True if they are all True.
        If `function` is `None`, use values directly."""
        if function is None:
            return all(self)
        return all(self.map(function))

    def any(self, function: Callable[[X], bool] | None = None) -> bool:
        """Apply `function` to all items and returns True if any return True.
        If `function` is `None`, use values directly."""
        if function is None:
            return any(self)
        return any(self.map(function))

    def fixed(self, value: Y) -> "LazyList[Y]":
        """Return a list of same size with a fixed value"""
        return LazyList(value for _ in self)

    def slice(self, start: int = None, stop: int = None, step: int = None) -> "LazyList[X]":
        """Use slice to subset the list."""
        if start is None and step is None:
            return LazyList(itertools.islice(self, stop))
        else:
            return LazyList(itertools.islice(self, start, stop, step))

    def contains(self, value: X) -> bool:
        """Check if value is in the list"""
        return value in self

    def join(self, delimiter: str) -> str:
        """Join the items together into a string separated by `delimiter`
        >>> a = LazyList([1, 2, 3])
        >>> a.join(",")
        "1,2,3"
        """
        return delimiter.join(self.map(str))

    def where(self, predicate: Callable[[X], bool]) -> LazyList[int]:
        """Return indices where predicate returns `True`"""
        return self.enumerate().filter(lambda o: predicate(o[1])).get_item(0)

    @overload
    def zip(self, other: Iterable[Y]) -> "LazyList[Tuple[X, Y]]":
        ...

    @overload
    def zip(self, other1: Iterable[Y1], other2: Iterable[Y2]) -> "LazyList[Tuple[X, Y1, Y2]]":
        ...

    @overload
    def zip(
        self,
        other1: Iterable[Y1],
        other2: Iterable[Y2],
        other3: Iterable[Y3],
    ) -> "LazyList[Tuple[X, Y1, Y2, Y3]]":
        ...

    @overload
    def zip(
        self,
        other1: Iterable[Y1],
        other2: Iterable[Y2],
        other3: Iterable[Y3],
        other4: Iterable[Y4],
    ) -> "LazyList[Tuple[X, Y1, Y2, Y3, Y4]]":
        ...

    @overload
    def zip(
        self,
        other1: Iterable[Any],
        other2: Iterable[Any],
        other3: Iterable[Any],
        other4: Iterable[Any],
        *others: Iterable[Any],
    ) -> "LazyList[Tuple[Any, ...]]":
        ...

    def zip(self, *others: Iterable[Y]) -> "LazyList[Tuple[X, *Y]]":
        return LazyList(zip(self, *others))

    @overload
    def zip_longest(self, other: Iterable[Y]) -> "LazyList[Tuple[X|None, Y|None]]":
        ...

    @overload
    def zip_longest(
        self,
        other1: Iterable[Y1],
        other2: Iterable[Y2],
    ) -> "LazyList[Tuple[X|None, Y1|None, Y2|None]]":
        ...

    @overload
    def zip_longest(
        self,
        other1: Iterable[Y1],
        other2: Iterable[Y2],
        other3: Iterable[Y3],
    ) -> "LazyList[Tuple[X|None, Y1|None, Y2|None, Y3|None]]":
        ...

    @overload
    def zip_longest(
        self,
        other1: Iterable[Y1],
        other2: Iterable[Y2],
        other3: Iterable[Y3],
        other4: Iterable[Y4],
    ) -> "LazyList[Tuple[X|None, Y1|None, Y2|None, Y3|None, Y4|None]]":
        ...

    @overload
    def zip_longest(
        self,
        other1: Iterable[Any],
        other2: Iterable[Any],
        other3: Iterable[Any],
        other4: Iterable[Any],
        *others: Iterable[Any],
    ) -> "LazyList[Tuple[Any, ...]]":
        ...

    def zip_longest(self, *others):
        return LazyList(itertools.zip_longest(self, *others))

    # @overload
    # def __getitem__(self, index: int) -> X:
    #     ...

    # @overload
    # def __getitem__(self, index: Iterable | slice) -> "LazyList[X]":
    #     ...

    # def __getitem__(self, index):
    #     if isinstance(index, slice):
    #         return LazyList(self.list[index])
    #     if isinstance(index, Iterable):
    #         return LazyList([v for i, v in enumerate(self) if i in index])
    #     else:
    #         return self.list[index]

    def at(self, index: int) -> X:
        """Returns item(s) at index.
        `LazyList.at(index)` is the same as `LazyList.nth(index)`"""
        return self.nth(index)

    def accumulate(self, function: Callable[[X, X], X]) -> "LazyList[X]":
        """Apply function over values cumulatively"""
        return LazyList(itertools.accumulate(self, function))

    def combinations(self, r: int) -> "LazyList[Tuple[X, ...]]":
        """Return successive r-length combinations of elements in the iterable.

        LazyList(range(4)).combinations(3) --> (0,1,2), (0,1,3), (0,2,3), (1,2,3)"""
        return LazyList(itertools.combinations(self, r))

    def combinations_with_replacement(self, r: int) -> "LazyList[Tuple[X, ...]]":
        """Return successive r-length combinations of elements in the iterable allowing
        individual elements to have successive repeats."""
        return LazyList(itertools.combinations_with_replacement(self, r))

    def permutations(self, r: int) -> "LazyList[Tuple[X, ...]]":
        """Return successive r-length permutations of elements in the iterable.

        LazyList(range(3)).permutations(2) --> (0,1), (0,2), (1,0), (1,2), (2,0), (2,1)"""
        return LazyList(itertools.permutations(self, r))

    def product(self, other: Iterable[Y]) -> "LazyList[Tuple[X, Y]]":
        """Cartesian product of input iterables. Equivalent to nested for-loops.
        >>> a = LazyList([1,2])
        >>> b = "AB"
        >>> a.product(b).evaluate()
        EagerList([(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')])
        """
        return LazyList(itertools.product(self, other))

    def compress(self, selector: Iterable[bool]) -> "LazyList[Tuple[X, ...]]":
        """Return data elements corresponding to true selector elements.
        >>> a = LazyList([1, 2, 3, 4])
        >>> b = [True, False, 1, 0]
        >>> a.compress(b).evaluate()
        EagerList([1, 3])
        """
        return LazyList(itertools.compress(self, selector))

    def dropwhile(self, predicate: Callable[[X], bool]) -> "LazyList[X]":
        """Drop items from the iterable while predicate(item) is true.

        Afterwards, return every element in the list"""
        return LazyList(itertools.dropwhile(predicate, self))

    def takewhile(self, predicate: Callable[[X], bool]) -> "LazyList[X]":
        """Return successive entries from an iterable as long as the predicate evaluates
        to true for each entry."""
        return LazyList(itertools.takewhile(predicate, self))

    def filterfalse(self, predicate: Callable[[X], bool] | None) -> "LazyList[X]":
        """Return those items of iterable for which function(item) is false.

        If function is None, return the items that are false.
        """
        return LazyList(itertools.filterfalse(predicate, self))

    def loop(self, n: int) -> "LazyList[X]":
        """Loops over the list `n` times"""
        return LazyList(itertoolz.concat(itertools.repeat(self, n)))

    def interleave(self, *iterables: Iterable[X]) -> "LazyList[X]":
        """Interleave a sequence of sequences.
        Example:
        >>> a = LazyList([1,2,3])
        >>> b = [4,5,6]
        >>> a.interleave(b)
        LazyList([1, 4, 2, 5, 3, 6])"""
        return LazyList(itertoolz.interleave([self, *iterables]))

    def unique(self) -> "LazyList[X]":
        """Return only unique elements of a sequence"""
        return LazyList(itertoolz.unique(self))

    def is_distinct(self) -> bool:
        """All values in sequence are distinct"""
        return self.evaluate().is_distinct()

    def take(self, n: int) -> "LazyList[X]":
        """The first n elements of a sequence"""
        return LazyList(itertoolz.take(n, self))

    def drop(self, n: int) -> "LazyList[X]":
        """The sequence following the first n elements"""
        return LazyList(itertoolz.drop(n, self))

    def take_nth(self, n: int) -> "LazyList[X]":
        """Every nth item in seq"""
        return LazyList(itertoolz.take_nth(n, self))

    def nth(self, n: int) -> X:
        """The nth element in a sequence. Similar to `LazyList.at(n)` and `LazyList[n]`
        except `n` can only be a single index."""
        return itertoolz.nth(n, self)

    def concat(self, iterables: Sequence[Iterable[X]]) -> "LazyList[X]":
        """Extend the list by appending items from other iterables.
        Similar to `LazyList.extend` except iterables are passed in as a sequence instead of arguments.
        """
        return LazyList(itertoolz.concat([self, *iterables]))

    def interpose(self, value: X) -> "LazyList[X]":
        """Introduce element between each pair of elements in seq

        Example:
        >>> a = LazyList([1,2,3])
        >>> a.interpose(0)
        LazyList([1, 0, 2, 0, 3])"""
        return LazyList(itertoolz.interpose(value, self))

    def frequencies(self) -> Dict[X, int]:
        """Count the frequency of occurrence for each unique item.

        Example:
        >>> a = LazyList("aaabbcc")
        >>> a.frequencies()
        {'a': 3, 'b': 2, 'c': 2}"""
        return itertoolz.frequencies(self)

    def group_by(self, key: Callable[[X], Y]) -> Dict[Y, LazyList[X]]:
        """Group a collection by a key function

        Example:
        >>> a = LazyList(range(6))
        >>> a.group_by(lambda x: x%2)
        {0: LazyList([0, 2, 4]), 1: LazyList([1, 3, 5])}"""
        return {k: EagerList(v) for k, v in itertoolz.groupby(key, self).items()}

    def reduce_by(self, key: Callable[[X], Y], reducer: Callable[[X, X], X]) -> Dict[Y, X]:
        """Perform a simultaneous groupby (using key) and reduction (using reducer)

        Example:
        >>> a = LazyList(range(6))
        >>> a.reduce_by(lambda x: x % 2, max)
        {0: 4, 1: 5}"""
        return itertoolz.reduceby(key, reducer, self)

    def sliding_window(self, n: int) -> "LazyList[Tuple[X, ...]]":
        """A sequence of overlapping subsequences

        Example:
        >>> a = LazyList(range(5))
        >>> a.sliding_window(2).evaluate()
        LazyList([(0, 1), (1, 2), (2, 3), (3, 4)])"""
        return LazyList(itertoolz.sliding_window(n, self))

    def partition(self, n: int, pad: str | X = "__no__pad__") -> "LazyList[Tuple[X, ...]]":
        """Partition sequence into tuples of length n.

        Example:
        >>> a = LazyList(range(5))
        >>> a.partition(2)
        LazyList([(0, 1), (2, 3)])  # Note `4` does not appear
        >>> a.partition(2, pad=None).evaluate()
        LazyList([(0, 1), (2, 3), (4, None)])"""
        return LazyList(itertoolz.partition(n, self, pad=pad))

    def partition_all(self, n: int) -> "LazyList[Tuple[X, ...]]":
        """Partition all elements of sequence into tuples of length at most n
        The final tuple may be shorter to accommodate extra elements.

        Example:
        >>> a = LazyList(range(5))
        >>> a.partition_all(2).evaluate()
        LazyList([(0, 1), (2, 3), (4,)])
        """
        return LazyList(itertoolz.partition_all(n, self))

    def tail(self, n: int) -> "LazyList[X]":
        """The last n elements of a sequence"""
        return LazyList(itertoolz.tail(n, self))

    def top_k(self, k: int, key: None | Callable[[X], Any] = None) -> "LazyList[X]":
        """Find the k largest elements of a sequence"""
        return LazyList(itertoolz.topk(k, self, key=key))

    def random_sample(
        self,
        k: int = 1,
        random_state: Any | None = None,
    ) -> "LazyList[X]":
        """Return a k sized LazyList of population elements chosen with replacement"""
        random.seed(random_state)
        population = list(self)
        return LazyList(random.choice(population) for _ in range(k))

    def get_item(self, item: Hashable) -> "LazyList[Any]":
        """Uses `itemgetter` to retrieve items
        item could be index of a sequence or key of dictionary. Equivalent to:
        `LazyList.map(lambda x: x[item])"""
        getter: Callable[[Hashable], Any] = itemgetter(item)
        return self.map(getter)

    def get_attr(self, attribute: str) -> "LazyList[Any]":
        """Uses `attrgetter` to retrieve attributes. Equivalent to:
        `LazyList.map(lambda x: x.attribute)"""
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
        for value in self.reverse():
            if predicate(value):
                return value

    def find_last_index(self, predicate: Callable[[X], bool]) -> int:
        """Return the index of last item where predicate returns `True`"""
        for index, value in self.enumerate().reverse():
            if predicate(value):
                return index

    @property
    def first(self) -> X:
        return itertoolz.first(self)

    @property
    def second(self) -> X:
        return itertoolz.second(self)

    @property
    def last(self) -> X:
        return itertoolz.last(self)

    def to_set(self) -> Set[X]:
        return set(self)

    def to_deque(self) -> Deque[X]:
        return deque(self)
