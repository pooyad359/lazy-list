from collections import namedtuple
import random
from lazy_list import LazyList


def test_lazy_list():
    a = LazyList([1, 2, 3, 4])
    b = LazyList([1, 2, 3, 4])
    assert a == b


def test_lazy_list_to_list():
    l = [1, 2, 3]
    a: LazyList[int] = LazyList(l)
    assert a.to_list() == l


def test_lazy_list_evaluate():
    l = [1, 2, 3]
    a: LazyList[int] = LazyList(l)
    assert a.evaluate() == l


def test_lazy_list_map():
    a: LazyList[int] = LazyList([1, 2, 3])
    b = a.map(lambda x: x + 1)
    assert b.evaluate() == [2, 3, 4]


def test_lazy_list_filter():
    a: LazyList[int] = LazyList(range(5))
    b = a.filter(lambda x: x > 2)
    assert b.evaluate() == [3, 4]


def test_lazy_list_filter_none():
    a: LazyList[int] = LazyList(range(5))
    b = a.filter()
    assert b.evaluate().length == 4
    assert all(b)


def test_lazy_list_reduce():
    a: LazyList[int] = LazyList(range(5))
    b = a.reduce(lambda x, y: x + y)
    assert b == sum(a.evaluate())


def test_lazy_list_reduce_with_init():
    a: LazyList[int] = LazyList(range(5))
    b = a.reduce(lambda x, y: x + y, 5)
    assert b == sum(a) + 5


def test_lazy_list_at():
    a: LazyList[int] = LazyList(range(5))
    for i in range(5):
        assert a.at(i) == i


def test_lazy_list_sort():
    random.seed(12)
    a: LazyList[int] = LazyList(random.choices(range(20), k=20))
    b = a.sort()
    for i, j in b.sliding_window(2):
        assert i <= j


def test_lazy_list_contains():
    lst = range(10)
    a: LazyList[int] = LazyList(lst)
    for i in lst:
        assert i in a


def test_lazy_list_reverse():
    lst = list(range(10))
    a = LazyList(lst)
    b = a.reverse().to_list()
    for i in range(len(lst)):
        assert lst[~i] == b[i]


def test_lazy_list_append():
    a: LazyList[int] = LazyList(range(10))
    b = a.append(100)
    assert a == b.slice(stop=10)
    assert b.last == 100


def test_lazy_list_append_left():
    a: LazyList[int] = LazyList(range(10))
    b = a.append_left(100)
    assert a == b.slice(start=1)
    assert b.first == 100


def test_lazy_list_extend():
    a: LazyList[int] = LazyList(range(10))
    c = [22, 33, 44] * 5
    b = a.extend(c)
    assert b.to_list() == a.to_list() + c


def test_lazy_list_extend_left():
    a: LazyList[int] = LazyList(range(10))
    c = [22, 33, 44] * 5
    b = a.extend_left(c)
    assert b.to_list() == c + a.to_list()


def test_lazy_list_enumerate():
    a: LazyList[int] = LazyList(random.choices(range(10), k=10))
    b = a.enumerate()
    for i, (j, _) in enumerate(b):
        assert i == j


def test_lazy_list_insert():
    a: LazyList[int] = LazyList(range(10))
    b = a.insert(5, 111)
    c = b.to_list()
    assert b.at(5) == 111
    c.pop(5)
    assert c == a


def test_lazy_list_pop():
    a: LazyList[int] = LazyList([i * 11 for i in range(10)])
    b = a.pop(6)
    assert 66 not in b
    assert len(a.to_list()) == len(b.to_list()) + 1


def test_lazy_list_pop_left():
    a: LazyList[int] = LazyList([i * 11 for i in range(10)])
    b = a.pop_left()
    assert 0 not in b
    assert a.get_length_eagerly() == b.get_length_eagerly() + 1


def test_lazy_list_remove():
    a: LazyList[int] = LazyList([i * 11 for i in range(10)])
    b = a.remove(55)
    assert 55 not in b
    assert a.get_length_eagerly() == b.get_length_eagerly() + 1


def test_lazy_list_remove_all():
    a: LazyList[int] = LazyList([1, 2, 2, 3, 4, 5, 5, 5, 6])
    value = 5
    b = a.remove_all(value)
    assert value not in b
    assert a.get_length_eagerly() == b.get_length_eagerly() + a.count(value)


def test_lazy_list_all():
    a: LazyList[int] = LazyList([1, 2, 2, 3, 4])
    assert a.all(lambda x: x > 0)


def test_lazy_list_all_false():
    a: LazyList[int] = LazyList([1, 2, 2, 3, 4])
    assert not a.all(lambda x: x > 1)


def test_lazy_list_all_none():
    a: LazyList[int] = LazyList([1, 2, 2, 3, 4])
    assert a.all()


def test_lazy_list_any():
    a: LazyList[int] = LazyList([1, 2, 2, 3, 4])
    assert a.any(lambda x: x > 3)


def test_lazy_list_any_false():
    a: LazyList[int] = LazyList([1, 2, 2, 3, 4])
    assert not a.any(lambda x: x > 4)


def test_lazy_list_any_none():
    a: LazyList[int] = LazyList([0, 0, 1, 0])
    assert a.any()


def test_lazy_list_fixed():
    a: LazyList[int] = LazyList(range(20))
    value = 99
    b = a.fixed(value)
    assert b.get_length_eagerly() == a.get_length_eagerly()
    for i in b:
        assert i == value


def test_lazy_list_contains():
    a: LazyList[int] = LazyList(range(10))
    for i in range(10):
        assert i in a
    for i in range(10, 20):
        assert i not in a


def test_lazy_list_join():
    a: LazyList[int] = LazyList([1, 2, 3])
    assert a.join(",") == "1,2,3"


def test_lazy_list_where():
    a: LazyList[int] = LazyList([1, 2, 3, 2, 1])
    assert a.where(lambda x: x != 2) == [0, 2, 4]


def test_lazy_list_zip():
    a = LazyList(range(5))
    b = LazyList(range(5)).reverse()
    for z, _a, _b in zip(a.zip(b), a, b):
        assert z == (_a, _b)


def test_lazy_list_zip_longest():
    a = LazyList(range(10))
    b = range(5)
    assert a.zip_longest(b).get_length_eagerly() == a.get_length_eagerly()


def test_lazy_list_accumulate():
    a = LazyList([1, 2, 3, 4])
    assert a.accumulate(lambda x, y: x * y) == [1, 2, 6, 24]


def test_lazy_list_combination():
    a = LazyList([1, 2, 3, 4])
    b = a.combinations(2)
    assert b.get_length_eagerly() == 6


def test_lazy_list_combinations_with_replacement():
    a = LazyList([1, 2, 3, 4])
    b = a.combinations_with_replacement(2)
    assert b.get_length_eagerly() == 10


def test_lazy_list_combinations_with_replacement():
    a = LazyList([1, 2, 3, 4])
    b = a.permutations(2)
    assert b.get_length_eagerly() == 12


def test_lazy_list_compress():
    a = LazyList([1, 2, 3, 4])
    b = [True, False, 1, 0]
    assert a.compress(b) == [1, 3]


def test_lazy_list_dropwhile():
    def _predicate(x):
        return x < 5

    a = LazyList(range(10))
    b = a.dropwhile(_predicate)
    assert all([not _predicate(o) for o in b])


def test_lazy_list_takewhile():
    def _predicate(x):
        return x < 5

    a = LazyList(range(10))
    b = a.takewhile(_predicate)
    assert all([_predicate(o) for o in b])


def test_lazy_list_filter_false():
    a = LazyList(range(10))
    assert a.filterfalse(lambda x: x % 2) == a.filter(lambda x: not (x % 2))


def test_lazy_list_loop():
    a = LazyList([1, 2, 3])
    b = a.loop(3)
    assert b.get_length_eagerly() == a.get_length_eagerly() * 3


def test_lazy_list_interleave():
    a = LazyList(range(5))
    b = list(range(6, 10))
    c = list(range(10, 20))
    result = a.interleave(b, c)
    assert result.get_length_eagerly() == a.get_length_eagerly() + len(b + c)
    assert result.slice(stop=3) == [a.first, b[0], c[0]]


def test_lazy_list_unique():
    a = LazyList([1, 2, 3, 4, 4, 3, 2, 1])
    b = a.unique()
    assert b.get_length_eagerly() == 4
    for i in a:
        assert i in b


def test_lazy_list_take_nth():
    a = LazyList(range(6))
    assert a.take_nth(2) == [0, 2, 4]


def test_lazy_list_groupby():
    a = LazyList(range(6))
    b = a.group_by(lambda x: x % 2)
    assert b[0] == [0, 2, 4]
    assert b[1] == [1, 3, 5]


def test_lazy_list_get_item_dict():
    a = LazyList([{"a": 1}, {"a": 2}])
    assert a.get_item("a") == [1, 2]


def test_lazy_list_get_item_sequence():
    a = LazyList([(0, 1, 2), (3, 4, 5), (6, 7, 8)])
    assert a.get_item(1) == [1, 4, 7]


def test_lazy_list_get_attr():
    Point = namedtuple("Point", ["x", "y"])
    a = LazyList([Point(1, 2), Point(3, 4), Point(5, 6)])
    assert a.get_attr("x") == [1, 3, 5]
