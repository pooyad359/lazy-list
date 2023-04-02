import random
from collections import deque, namedtuple

from lazy_list import EagerList, LazyList


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


def test_eager_list_copy():
    _list: EagerList[int] = EagerList(range(10))
    result = _list.copy()
    assert result == _list
    assert result is not _list


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


def test_eager_list_index_slice_method():
    _list: EagerList[int] = EagerList(range(5))
    assert _list.slice(0, 3) == list(range(3))


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
    assert all(_predicate(o) for o in result)


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


def test_eager_list_slice():
    _list = EagerList([1, 2, 3, 4, 5])
    assert _list[1:3] == [2, 3]
    assert _list[1:] == [2, 3, 4, 5]
    assert _list[::-1] == [5, 4, 3, 2, 1]


def test_eager_list_is_in():
    _list = EagerList(range(5))
    for i in range(5):
        assert i in _list
    assert 6 not in _list


def test_eager_list_combinations():
    _list = EagerList(range(4))
    result = _list.combinations(2)
    expected = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    assert result == expected


def test_eager_list_combination_with_replacement():
    _list = EagerList(range(4))
    result = _list.combinations_with_replacement(2)
    expected = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
    assert result == expected


def test_eager_list_permutations():
    _list = EagerList(range(4))
    result = _list.permutations(2)
    expected = [(0, 1), (0, 2), (0, 3), (1, 0), (1, 2), (1, 3), (2, 0), (2, 1), (2, 3), (3, 0), (3, 1), (3, 2)]
    assert result == expected


def test_eager_list_product():
    _list = EagerList(range(3))
    result = _list.product([3, 4, 5])
    expected = [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)]
    assert result == expected


def test_eager_list_n_unique():
    _list = EagerList([1, 2, 3, 4, 4, 3, 2, 1])
    assert _list.n_unique() == 4


def test_eager_list_is_distinct():
    _list = EagerList([1, 2, 3, 4, 4, 3, 2, 1])
    assert not _list.is_distinct()
    _list = EagerList([1, 2, 3, 4, 5, 6, 7, 8])
    assert _list.is_distinct()


def test_eager_list_take():
    _list = EagerList(range(10))
    assert _list.take(5) == [0, 1, 2, 3, 4]
    assert _list.take(10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert _list.take(15) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_eager_list_drop():
    _list = EagerList(range(10))
    assert _list.drop(0) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert _list.drop(5) == [5, 6, 7, 8, 9]
    assert _list.drop(10) == []
    assert _list.drop(15) == []


def test_eager_list_take_nth():
    _list = EagerList(range(10))
    assert _list.take_nth(2) == [0, 2, 4, 6, 8]
    assert _list.take_nth(3) == [0, 3, 6, 9]
    assert _list.take_nth(10) == [0]
    assert _list.take_nth(15) == [0]


def test_eager_list_nth():
    _list = EagerList(range(10))
    for i in range(10):
        assert _list.nth(i) == i


def test_eager_list_get():
    _list = EagerList(range(10))
    assert _list.get(0) == 0
    assert _list.get([1, 4, 7]) == [1, 4, 7]


def test_eager_list_concat():
    _list = EagerList(range(5))
    assert _list.concat(([5, 6, 7], [8, 9])) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_eager_list_interpose():
    _list = EagerList(range(5))
    assert _list.interpose(5) == [0, 5, 1, 5, 2, 5, 3, 5, 4]


def test_eager_list_frequencies():
    _list = EagerList([1, 2, 3, 4, 2, 2, 1])
    assert _list.frequencies() == {1: 2, 2: 3, 3: 1, 4: 1}


def test_eager_list_frequency_tuples():
    _list = EagerList([1, 2, 3, 4, 2, 2, 1])
    assert _list.frequency_tuples() == [(1, 2), (2, 3), (3, 1), (4, 1)]


def test_eager_list_mode():
    _list = EagerList([1, 2, 3, 4, 2, 2, 1])
    assert _list.mode() == 2


def test_eager_list_mode_str():
    _list = EagerList(["a", "b", "c", "d", "b", "b", "a"])
    assert _list.mode() == "b"


def test_eager_list_multimode():
    _list = EagerList([1, 2, 3, 4, 0, 2, 1])
    result = _list.multi_mode()
    expected = [1, 2]
    assert result == expected
    assert isinstance(result, EagerList)


def test_eager_list_reduce_by():
    _list = EagerList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    result = _list.reduce_by(lambda x: x % 2 == 0, lambda x, y: x + y)
    expected = {True: 30, False: 25}
    assert result == expected


def test_eager_list_partition_default():
    _list = EagerList([1, 2, 3, 4, 5, 6, 7])
    result = _list.partition(3)
    expected = [(1, 2, 3), (4, 5, 6)]
    assert result == expected
    assert isinstance(result, EagerList)


def test_eager_list_partition_pad():
    _list = EagerList([1, 2, 3, 4, 5, 6, 7])
    result = _list.partition(3, -1)
    expected = [(1, 2, 3), (4, 5, 6), (7, -1, -1)]
    assert result == expected
    assert isinstance(result, EagerList)


def test_eager_list_partition_all():
    _list = EagerList([1, 2, 3, 4, 5, 6, 7])
    result = _list.partition_all(3)
    expected = [(1, 2, 3), (4, 5, 6), (7,)]
    assert result == expected
    assert isinstance(result, EagerList)


def test_eager_list_tail():
    _list = EagerList([1, 2, 3, 4, 5, 6, 7])
    result = _list.tail(3)
    expected = [5, 6, 7]
    assert result == expected
    assert isinstance(result, EagerList)


def test_eager_list_top_k():
    _list = EagerList([8, 2, 3, 4, 5, 6, 7])
    result = _list.top_k(3)
    expected = [8, 7, 6]
    assert result == expected
    assert isinstance(result, EagerList)


def test_eager_list_random_sample():
    _list = EagerList([1, 2, 3, 4, 5, 6, 7])
    result = _list.random_sample(3)
    for i in result:
        assert i in _list
    assert len(result) == 3
    assert isinstance(result, EagerList)


def test_eager_list_random_sample_seed():
    _list = EagerList([1, 2, 3, 4, 5, 6, 7])
    result1 = _list.random_sample(3, random_state=1)
    result2 = _list.random_sample(3, random_state=1)
    result3 = _list.random_sample(3, random_state=2)
    assert result1 == result2
    assert result1 != result3


def test_eager_list_find_first():
    _list = EagerList([1, 2, 3, 4, 5, 6, 7])
    result = _list.find_first(lambda x: x % 3 == 0)
    expected = 3
    assert result == expected


def test_eager_list_find_first_index():
    _list = EagerList([1, 2, 3, 4, 5, 6, 7])
    result = _list.find_first_index(lambda x: x % 3 == 0)
    expected = 2
    assert result == expected


def test_eager_list_find_last():
    _list = EagerList([1, 2, 3, 4, 5, 6, 7])
    result = _list.find_last(lambda x: x % 3 == 0)
    expected = 6
    assert result == expected


def test_eager_list_find_last_index():
    _list = EagerList([1, 2, 3, 4, 5, 6, 7])
    result = _list.find_last_index(lambda x: x % 3 == 0)
    expected = 5
    assert result == expected


def test_eager_list_call_method():
    _list = EagerList(["a", "b", "c"])
    results = _list.call_method("upper")
    expected = ["A", "B", "C"]
    assert results == expected


def test_eager_list_first():
    _list = EagerList([1, 2, 3, 4, 5, 6, 7])
    assert _list.first == 1


def test_eager_list_second():
    _list = EagerList([1, 2, 3, 4, 5, 6, 7])
    assert _list.second == 2


def test_eager_list_last():
    _list = EagerList([1, 2, 3, 4, 5, 6, 7])
    assert _list.last == 7


def test_eager_list_to_set():
    _list = EagerList([1, 2, 3, 4, 5, 6, 7])
    result = _list.to_set()
    expected = {1, 2, 3, 4, 5, 6, 7}
    assert result == expected


def test_eager_list_to_deque():
    _list = EagerList([1, 2, 3, 4, 5, 6, 7])
    result = _list.to_deque()
    expected = deque([1, 2, 3, 4, 5, 6, 7])
    assert result == expected


def test_eager_list_to_lazt_list():
    _list = EagerList([1, 2, 3, 4, 5, 6, 7])
    result = _list.lazy
    expected = LazyList([1, 2, 3, 4, 5, 6, 7])
    assert result == expected
    for i, j in zip(result, expected):
        assert i == j
    assert isinstance(result, LazyList)


def test_eager_list_contains():
    elements = [1, 2, 3, 4, 5, 6, 7]
    _list = EagerList(elements)
    for element in elements:
        assert element in _list
    assert not _list.contains(8)
