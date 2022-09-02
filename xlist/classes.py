from functools import reduce
from collections.abc import Iterable


class XList(list):
    def __str__(self):
        return f"XList{list(self)}"

    def __repr__(self):
        return f"XList({list(self)})"

    def map(self, function):
        return XList(map(function, self))

    def filter(self, function):
        return XList(filter(function, self))

    def reduce(self, function, initial=None):
        if initial is None:
            return reduce(function, self)
        else:
            return reduce(function, self, initial)

    def at(self, index):
        return self[index]

    def sort(self, key=None, reverse=False):
        return XList(sorted(self, key=key, reverse=reverse))

    def reverse(self):
        return XList(reversed(self))

    def append(self, item):
        return XList(self + [item])

    def clear(self):
        return XList([])

    def copy(self):
        return XList(self.list.copy())

    def extend(self, iterable):
        return XList(self + list(iterable))

    def insert(self, index, item):
        l = list(self)
        l.insert(index, item)
        return XList(l)

    def pop(self):
        raise NotImplementedError()

    def remove(self, value):
        l = self.list
        l.remove(value)
        return XList(l)

    def all(self, function):
        """Apply `function` to all items and returns True if they are all True."""
        return all(self.map(function))

    def any(self, function):
        """Apply `function` to all items and returns True if any return True."""
        return any(self.map(function))

    def fill(self, value, start, end=None):
        """Create a new list with items from `start` to `end` filled with `value`."""
        _slice = slice(start, end)
        new_list = self.list
        indices = range(*_slice.indices(self.length))
        length = len(indices)
        new_values = [value] * length
        new_list[_slice] = new_values
        return XList(new_list)

    def fixed(self, value):
        """Return a list of same size with a fixed value"""
        return XList([value] * self.length)

    def find(self, condition):
        raise NotImplementedError()

    def find_index(self, condition):
        raise NotImplementedError()

    def find_last(self, condition):
        raise NotImplementedError()

    def find_last_index(self, condition):
        raise NotImplementedError()

    def slice(self, start=None, stop=None, step=None):
        _slice = slice(start, stop, step)
        return XList(self.list[_slice])

    def contains(self, value):
        return value in self

    def join(self, delimiter: str):
        return delimiter.join(self.map(str))

    def index_last(self, value):
        index = self.reverse().index(value)
        return self.length - 1 - index

    def __getitem__(self, index):
        if isinstance(index, slice):
            return XList(self.list[index])
        if isinstance(index, Iterable):
            return XList([v for i, v in enumerate(self) if i in index])
        else:
            return self.list[index]

    @property
    def list(self):
        return list(self)

    @property
    def length(self):
        return len(self)

    @property
    def first(self):
        return self[0]

    @property
    def last(self):
        return self[-1]
