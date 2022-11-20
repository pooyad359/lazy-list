from collections import namedtuple
import random
from lazy_list import EagerList


def test_eager_list_map():
    a: EagerList[int] = EagerList([1, 2, 3])
    b = a.map(lambda x: x + 1)
    assert b == [2, 3, 4]


def test_eager_list_filter():
    a: EagerList[int] = EagerList(range(5))
    b = a.filter(lambda x: x > 2)
    assert b == [3, 4]


def test_eager_list_filter_none():
    a: EagerList[int] = EagerList(range(5))
    b = a.filter()
    assert b.length == 4


def test_eager_list_reduce():
    a: EagerList[int] = EagerList(range(5))
    b = a.reduce(lambda x, y: x + y)
    assert b == sum(a)


def test_eager_list_reduce_with_init():
    a: EagerList[int] = EagerList(range(5))
    b = a.reduce(lambda x, y: x + y, 5)
    assert b == sum(a) + 5


def test_eager_list_at():
    a: EagerList[int] = EagerList(range(5))
    for i in range(5):
        assert a.at(i) == i


def test_eager_list_sort():
    random.seed(12)
    a: EagerList[int] = EagerList(random.choices(range(20), k=20))
    b = a.sort()
    for i, j in zip(b[:-1], b[1:]):
        assert i <= j


def test_eager_list_append():
    a: EagerList[int] = EagerList(range(10))
    b = a.append(100)
    assert a == b[:-1]
    assert b[-1] == 100


def test_eager_list_append_left():
    a: EagerList[int] = EagerList(range(10))
    b = a.append_left(100)
    assert a == b[1:]
    assert b[0] == 100


def test_eager_list_extend():
    a: EagerList[int] = EagerList(range(10))
    c = [22, 33, 44] * 5
    b = a.extend(c)
    assert b.to_list() == a.to_list() + c


def test_eager_list_extend_left():
    a: EagerList[int] = EagerList(range(10))
    c = [22, 33, 44] * 5
    b = a.extend_left(c)
    assert b.to_list() == c + a.to_list()


def test_eager_list_insert():
    a: EagerList[int] = EagerList(range(10))
    b = a.insert(5, 111)
    assert b[5] == 111
    assert b.pop(5) == a


def test_eager_list_pop():
    a: EagerList[int] = EagerList([i * 11 for i in range(10)])
    b = a.pop(6)
    assert 66 not in b
    assert a.length == b.length + 1


def test_eager_list_pop_left():
    a: EagerList[int] = EagerList([i * 11 for i in range(10)])
    b = a.pop_left()
    assert 0 not in b
    assert a.length == b.length + 1


def test_eager_list_remove():
    a: EagerList[int] = EagerList([i * 11 for i in range(10)])
    b = a.remove(55)
    assert 55 not in b
    assert a.length == b.length + 1


def test_eager_list_remove_all():
    a: EagerList[int] = EagerList([1, 2, 2, 3, 4, 5, 5, 5, 6])
    value = 5
    b = a.remove_all(value)
    assert value not in b
    assert a.length == b.length + a.count(value)


def test_eager_list_all():
    a: EagerList[int] = EagerList([1, 2, 2, 3, 4])
    assert a.all(lambda x: x > 0)


def test_eager_list_all_false():
    a: EagerList[int] = EagerList([1, 2, 2, 3, 4])
    assert not a.all(lambda x: x > 1)


def test_eager_list_all_none():
    a: EagerList[int] = EagerList([1, 2, 2, 3, 4])
    assert a.all()


def test_eager_list_any():
    a: EagerList[int] = EagerList([1, 2, 2, 3, 4])
    assert a.any(lambda x: x > 3)


def test_eager_list_any_false():
    a: EagerList[int] = EagerList([1, 2, 2, 3, 4])
    assert not a.any(lambda x: x > 4)


def test_eager_list_any_none():
    a: EagerList[int] = EagerList([0, 0, 1, 0])
    assert a.any()


def test_eager_list_fill():
    a: EagerList[int] = EagerList(range(20))
    start, stop = 5, 10
    value = 99
    b = a.fill(value, start, stop)
    for i in range(start, stop):
        assert b[i] == value


def test_eager_list_fixed():
    a: EagerList[int] = EagerList(range(20))
    value = 99
    b = a.fixed(value)
    for i in b:
        assert i == value


def test_eager_list_join():
    a: EagerList[int] = EagerList([1, 2, 3])
    assert a.join(",") == "1,2,3"


def test_eager_list_index_last():
    a: EagerList[int] = EagerList([1, 2, 3, 2, 1])
    assert a.index_last(2) == 3


def test_eager_list_where():
    a: EagerList[int] = EagerList([1, 2, 3, 2, 1])
    assert a.where(lambda x: x != 2) == [0, 2, 4]


def test_eager_list_index_slice():
    a: EagerList[int] = EagerList(range(5))
    assert a[:3] == list(range(3))


def test_eager_list_index_iterable():
    a: EagerList[int] = EagerList(range(5))
    assert a[[1, 3]] == [1, 3]


def test_eager_list_zip():
    a = EagerList(range(5))
    b = reversed(range(5))
    for z, _a, _b in zip(a.zip(b), a, b):
        assert z == (_a, _b)


def test_eager_list_accumulate():
    a = EagerList([1, 2, 3, 4])
    assert a.accumulate(lambda x, y: x * y) == [1, 2, 6, 24]


def test_eager_list_zip_longest():
    a = EagerList(range(10))
    b = range(5)
    assert len(a.zip_longest(b)) == len(a)


def test_eager_list_compress():
    a = EagerList([1, 2, 3, 4])
    b = [True, False, 1, 0]
    assert a.compress(b) == [1, 3]


def test_eager_list_dropwhile():
    def _predicate(x):
        return x < 5

    a = EagerList(range(10))
    b = a.dropwhile(_predicate)
    assert all([not _predicate(o) for o in b])


def test_eager_list_takewhile():
    def _predicate(x):
        return x < 5

    a = EagerList(range(10))
    b = a.takewhile(_predicate)
    assert all([_predicate(o) for o in b])


def test_eager_list_loop():
    a = EagerList([1, 2, 3])
    b = a.loop(3)
    assert b.length == a.length * 3


def test_eager_list_interleave():
    a = EagerList(range(5))
    b = list(range(6, 10))
    c = list(range(10, 20))
    result = a.interleave(b, c)
    assert result.length == len(a + b + c)
    assert result[:3] == [a[0], b[0], c[0]]


def test_eager_list_unique():
    a = EagerList([1, 2, 3, 4, 4, 3, 2, 1])
    b = a.unique()
    assert b.length == 4
    for i in a:
        assert i in b


def test_eager_list_groupby():
    a = EagerList(range(6))
    b = a.group_by(lambda x: x % 2)
    assert b[0] == [0, 2, 4]
    assert b[1] == [1, 3, 5]


def test_eager_list_get_item_dict():
    a = EagerList([{"a": 1}, {"a": 2}])
    assert a.get_item("a") == [1, 2]


def test_eager_list_get_item_sequence():
    a = EagerList([(0, 1, 2), (3, 4, 5), (6, 7, 8)])
    assert a.get_item(1) == [1, 4, 7]


def test_eager_list_get_attr():
    Point = namedtuple("Point", ["x", "y"])
    a = EagerList([Point(1, 2), Point(3, 4), Point(5, 6)])
    assert a.get_attr("x") == [1, 3, 5]


def test_eager_list_rotate_positive():
    a = EagerList([1, 2, 3, 4, 5])
    b = a.rotate(2)
    assert b == [4, 5, 1, 2, 3]


def test_eager_list_rotate_negative():
    a = EagerList([1, 2, 3, 4, 5])
    b = a.rotate(-2)
    assert b == [3, 4, 5, 1, 2]


def test_eager_list_rotate_both():
    a = EagerList([1, 2, 3, 4, 5])
    steps = 3
    assert a == a.rotate(steps).rotate(-steps)


def test_eager_list_rotate_large():
    a = EagerList([1, 2, 3, 4, 5])
    steps = 30
    assert a == a.rotate(steps).rotate(-steps)
