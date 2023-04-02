import random
from collections import namedtuple

from lazy_list import EagerList


def test_eager_list_str():
    _list: EagerList[int] = EagerList([1, 2, 3])
    assert str(_list) == "EagerList[1, 2, 3]"


def test_eager_list_repr():
    _list: EagerList[int] = EagerList([1, 2, 3])
    assert repr(_list) == "EagerList([1, 2, 3])"


def test_eager_list_map():
    _list: EagerList[int] = EagerList([1, 2, 3])
    result = _list.map(lambda x: x + 1)
    assert result == [2, 3, 4]


def test_eager_list_filter():
    _list: EagerList[int] = EagerList(range(5))
    result = _list.filter(lambda x: x > 2)
    assert result == [3, 4]


def test_eager_list_filter_none():
    _list: EagerList[int] = EagerList(range(5))
    result = _list.filter()
    assert result.length == 4


def test_eager_list_reduce():
    _list: EagerList[int] = EagerList(range(5))
    result = _list.reduce(lambda x, y: x + y)
    assert result == sum(_list)


def test_eager_list_reduce_with_init():
    _list: EagerList[int] = EagerList(range(5))
    result = _list.reduce(lambda x, y: x + y, 5)
    assert result == sum(_list) + 5


def test_eager_list_at():
    _list: EagerList[int] = EagerList(range(5))
    for i in range(5):
        assert _list.at(i) == i


def test_eager_list_sort():
    random.seed(12)
    _list: EagerList[int] = EagerList(random.choices(range(20), k=20))
    result = _list.sort()
    for i, j in zip(result[:-1], result[1:]):
        assert i <= j


def test_eager_list_append():
    _list: EagerList[int] = EagerList(range(10))
    result = _list.append(100)
    assert _list == result[:-1]
    assert result[-1] == 100


def test_eager_list_append_left():
    _list: EagerList[int] = EagerList(range(10))
    result = _list.append_left(100)
    assert _list == result[1:]
    assert result[0] == 100


def test_eager_list_clear():
    _list: EagerList[int] = EagerList(range(10))
    result = _list.clear()
    assert result.length == 0
    assert isinstance(result, EagerList)


def test_eager_list_extend():
    _list: EagerList[int] = EagerList(range(10))
    c = [22, 33, 44] * 5
    result = _list.extend(c)
    assert result.to_list() == _list.to_list() + c


def test_eager_list_extend_left():
    _list: EagerList[int] = EagerList(range(10))
    c = [22, 33, 44] * 5
    result = _list.extend_left(c)
    assert result.to_list() == c + _list.to_list()


def test_eager_list_insert():
    _list: EagerList[int] = EagerList(range(10))
    result = _list.insert(5, 111)
    assert result[5] == 111
    assert result.pop(5) == _list


def test_eager_list_pop():
    _list: EagerList[int] = EagerList([i * 11 for i in range(10)])
    result = _list.pop(6)
    assert 66 not in result
    assert _list.length == result.length + 1


def test_eager_list_pop_left():
    _list: EagerList[int] = EagerList([i * 11 for i in range(10)])
    result = _list.pop_left()
    assert 0 not in result
    assert _list.length == result.length + 1


def test_eager_list_remove():
    _list: EagerList[int] = EagerList([i * 11 for i in range(10)])
    result = _list.remove(55)
    assert 55 not in result
    assert _list.length == result.length + 1


def test_eager_list_remove_all():
    _list: EagerList[int] = EagerList([1, 2, 2, 3, 4, 5, 5, 5, 6])
    value = 5
    result = _list.remove_all(value)
    assert value not in result
    assert _list.length == result.length + _list.count(value)


def test_eager_list_all():
    _list: EagerList[int] = EagerList([1, 2, 2, 3, 4])
    assert _list.all(lambda x: x > 0)


def test_eager_list_all_false():
    _list: EagerList[int] = EagerList([1, 2, 2, 3, 4])
    assert not _list.all(lambda x: x > 1)


def test_eager_list_all_none():
    _list: EagerList[int] = EagerList([1, 2, 2, 3, 4])
    assert _list.all()


def test_eager_list_any():
    _list: EagerList[int] = EagerList([1, 2, 2, 3, 4])
    assert _list.any(lambda x: x > 3)


def test_eager_list_any_false():
    _list: EagerList[int] = EagerList([1, 2, 2, 3, 4])
    assert not _list.any(lambda x: x > 4)


def test_eager_list_any_none():
    _list: EagerList[int] = EagerList([0, 0, 1, 0])
    assert _list.any()


def test_eager_list_fill():
    _list: EagerList[int] = EagerList(range(20))
    start, stop = 5, 10
    value = 99
    result = _list.fill(value, start, stop)
    for i in range(start, stop):
        assert result[i] == value


def test_eager_list_fixed():
    _list: EagerList[int] = EagerList(range(20))
    value = 99
    result = _list.fixed(value)
    for i in result:
        assert i == value


def test_eager_list_join():
    _list: EagerList[int] = EagerList([1, 2, 3])
    assert _list.join(",") == "1,2,3"


def test_eager_list_index_last():
    _list: EagerList[int] = EagerList([1, 2, 3, 2, 1])
    assert _list.index_last(2) == 3


def test_eager_list_where():
    _list: EagerList[int] = EagerList([1, 2, 3, 2, 1])
    assert _list.where(lambda x: x != 2) == [0, 2, 4]


def test_eager_list_index_slice():
    _list: EagerList[int] = EagerList(range(5))
    assert _list[:3] == list(range(3))


def test_eager_list_index_iterable():
    _list: EagerList[int] = EagerList(range(5))
    assert _list[[1, 3]] == [1, 3]


def test_eager_list_zip():
    _list = EagerList(range(5))
    result = reversed(range(5))
    for z, _a, _b in zip(_list.zip(result), _list, result):
        assert z == (_a, _b)


def test_eager_list_accumulate():
    _list = EagerList([1, 2, 3, 4])
    assert _list.accumulate(lambda x, y: x * y) == [1, 2, 6, 24]


def test_eager_list_zip_longest():
    _list = EagerList(range(10))
    result = range(5)
    assert len(_list.zip_longest(result)) == len(_list)


def test_eager_list_compress():
    _list = EagerList([1, 2, 3, 4])
    result = [True, False, 1, 0]
    assert _list.compress(result) == [1, 3]


def test_eager_list_dropwhile():
    def _predicate(x):
        return x < 5

    _list = EagerList(range(10))
    result = _list.dropwhile(_predicate)
    assert all([not _predicate(o) for o in result])


def test_eager_list_takewhile():
    def _predicate(x):
        return x < 5

    _list = EagerList(range(10))
    result = _list.takewhile(_predicate)
    assert all([_predicate(o) for o in result])


def test_eager_list_loop():
    _list = EagerList([1, 2, 3])
    result = _list.loop(3)
    assert result.length == _list.length * 3


def test_eager_list_interleave():
    list1 = EagerList(range(5))
    list2 = list(range(6, 10))
    list3 = list(range(10, 20))
    result = list1.interleave(list2, list3)
    assert result.length == len(list1 + list2 + list3)
    assert result[:3] == [list1[0], list2[0], list3[0]]


def test_eager_list_unique():
    _list = EagerList([1, 2, 3, 4, 4, 3, 2, 1])
    result = _list.unique()
    assert result.length == 4
    for i in _list:
        assert i in result


def test_eager_list_groupby():
    _list = EagerList(range(6))
    result = _list.group_by(lambda x: x % 2)
    assert result[0] == [0, 2, 4]
    assert result[1] == [1, 3, 5]


def test_eager_list_get_item_dict():
    _list = EagerList([{"_list": 1}, {"_list": 2}])
    assert _list.get_item("_list") == [1, 2]


def test_eager_list_get_item_sequence():
    _list = EagerList([(0, 1, 2), (3, 4, 5), (6, 7, 8)])
    assert _list.get_item(1) == [1, 4, 7]


def test_eager_list_get_attr():
    Point = namedtuple("Point", ["x", "y"])
    _list = EagerList([Point(1, 2), Point(3, 4), Point(5, 6)])
    assert _list.get_attr("x") == [1, 3, 5]


def test_eager_list_rotate_positive():
    _list = EagerList([1, 2, 3, 4, 5])
    result = _list.rotate(2)
    assert result == [4, 5, 1, 2, 3]


def test_eager_list_rotate_negative():
    _list = EagerList([1, 2, 3, 4, 5])
    result = _list.rotate(-2)
    assert result == [3, 4, 5, 1, 2]


def test_eager_list_rotate_both():
    _list = EagerList([1, 2, 3, 4, 5])
    steps = 3
    assert _list == _list.rotate(steps).rotate(-steps)


def test_eager_list_rotate_large():
    _list = EagerList([1, 2, 3, 4, 5])
    steps = 30
    assert _list == _list.rotate(steps).rotate(-steps)
