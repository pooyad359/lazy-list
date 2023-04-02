import random
from collections import deque, namedtuple

import pytest

from lazy_list import EagerList, LazyList


def test_lazy_list_str():
    _list = LazyList([1, 2, 3, 4])
    assert str(_list) == "LazyList(...)"


def test_lazy_list_repr():
    _list = LazyList([1, 2, 3, 4])
    assert repr(_list) == "LazyList(...)"


def test_lazy_list_eq():
    _list = LazyList([1, 2, 3, 4])
    _list2 = LazyList([1, 2, 3, 4])
    assert _list == _list2


def test_lazy_list_neq():
    _list = LazyList([1, 2, 3, 4])
    _list2 = LazyList([1, 2, 3])
    assert _list != _list2


def test_lazy_list_to_list():
    _list: LazyList[int] = LazyList([1, 2, 3])
    assert _list.to_list() == [1, 2, 3]
    assert isinstance(_list.to_list(), list)


def test_lazy_list_evaluate():
    _list: LazyList[int] = LazyList([1, 2, 3])
    result = _list.evaluate()
    assert result == [1, 2, 3]
    assert isinstance(result, EagerList)


def test_lazy_list_map():
    _list: LazyList[int] = LazyList([1, 2, 3])
    result = _list.map(lambda x: x + 1)
    assert result.evaluate() == [2, 3, 4]


def test_lazy_list_filter():
    _list: LazyList[int] = LazyList(range(5))
    result = _list.filter(lambda x: x > 2)
    assert result.evaluate() == [3, 4]


def test_lazy_list_filter_none():
    _list: LazyList[int] = LazyList(range(5))
    result = _list.filter()
    assert result.evaluate().length == 4
    assert all(result)


def test_lazy_list_reduce():
    _list: LazyList[int] = LazyList(range(5))
    result = _list.reduce(lambda x, y: x + y)
    assert result == sum(_list.evaluate())


def test_lazy_list_reduce_with_init():
    _list: LazyList[int] = LazyList(range(5))
    result = _list.reduce(lambda x, y: x + y, 5)
    assert result == sum(_list) + 5


def test_lazy_list_at():
    _list: LazyList[int] = LazyList(range(5))
    for i in range(5):
        assert _list.at(i) == i


def test_lazy_list_sort():
    random.seed(12)
    _list: LazyList[int] = LazyList(random.choices(range(20), k=20))
    result = _list.sort()
    for i, j in result.sliding_window(2):
        assert i <= j


def test_lazy_list_contains():
    lst = range(10)
    _list: LazyList[int] = LazyList(lst)
    for i in lst:
        assert i in _list


def test_lazy_list_reverse():
    lst = list(range(10))
    _list = LazyList(lst)
    result = _list.reverse().to_list()
    for i in range(len(lst)):
        assert lst[~i] == result[i]


def test_lazy_list_append():
    _list: LazyList[int] = LazyList(range(10))
    result = _list.append(100)
    assert _list == result.slice(stop=10)
    assert result.last == 100


def test_lazy_list_append_left():
    _list: LazyList[int] = LazyList(range(10))
    result = _list.append_left(100)
    assert _list == result.slice(start=1)
    assert result.first == 100


def test_lazy_list_extend():
    _list: LazyList[int] = LazyList(range(10))
    c = [22, 33, 44] * 5
    result = _list.extend(c)
    assert result.to_list() == _list.to_list() + c


def test_lazy_list_extend_left():
    _list: LazyList[int] = LazyList(range(10))
    c = [22, 33, 44] * 5
    result = _list.extend_left(c)
    assert result.to_list() == c + _list.to_list()


def test_lazy_list_enumerate():
    _list: LazyList[int] = LazyList(random.choices(range(10), k=10))
    result = _list.enumerate()
    for i, (j, _) in enumerate(result):
        assert i == j


def test_lazy_list_insert():
    _list: LazyList[int] = LazyList(range(10))
    result = _list.insert(5, 111)
    c = result.to_list()
    assert result.at(5) == 111
    c.pop(5)
    assert c == _list


def test_lazy_list_pop():
    _list: LazyList[int] = LazyList([i * 11 for i in range(10)])
    result = _list.pop(6)
    assert 66 not in result
    assert len(_list.to_list()) == len(result.to_list()) + 1


def test_lazy_list_pop_left():
    _list: LazyList[int] = LazyList([i * 11 for i in range(10)])
    result = _list.pop_left()
    assert 0 not in result
    assert _list.get_length_eagerly() == result.get_length_eagerly() + 1


def test_lazy_list_remove():
    _list: LazyList[int] = LazyList([i * 11 for i in range(10)])
    result = _list.remove(55)
    assert 55 not in result
    assert _list.get_length_eagerly() == result.get_length_eagerly() + 1


def test_lazy_list_remove_all():
    _list: LazyList[int] = LazyList([1, 2, 2, 3, 4, 5, 5, 5, 6])
    value = 5
    result = _list.remove_all(value)
    assert value not in result
    assert _list.get_length_eagerly() == result.get_length_eagerly() + _list.count(value)


def test_lazy_list_all():
    _list: LazyList[int] = LazyList([1, 2, 2, 3, 4])
    assert _list.all(lambda x: x > 0)


def test_lazy_list_all_false():
    _list: LazyList[int] = LazyList([1, 2, 2, 3, 4])
    assert not _list.all(lambda x: x > 1)


def test_lazy_list_all_none():
    _list: LazyList[int] = LazyList([1, 2, 2, 3, 4])
    assert _list.all()


def test_lazy_list_any():
    _list: LazyList[int] = LazyList([1, 2, 2, 3, 4])
    assert _list.any(lambda x: x > 3)


def test_lazy_list_any_false():
    _list: LazyList[int] = LazyList([1, 2, 2, 3, 4])
    assert not _list.any(lambda x: x > 4)


def test_lazy_list_any_none():
    _list: LazyList[int] = LazyList([0, 0, 1, 0])
    assert _list.any()


def test_lazy_list_fixed():
    _list: LazyList[int] = LazyList(range(20))
    value = 99
    result = _list.fixed(value)
    assert result.get_length_eagerly() == _list.get_length_eagerly()
    for i in result:
        assert i == value


def test_lazy_list_is_in():
    _list: LazyList[int] = LazyList(range(10))
    for i in range(10):
        assert i in _list
    for i in range(10, 20):
        assert i not in _list


def test_lazy_list_join():
    _list: LazyList[int] = LazyList([1, 2, 3])
    assert _list.join(",") == "1,2,3"


def test_lazy_list_where():
    _list: LazyList[int] = LazyList([1, 2, 3, 2, 1])
    assert _list.where(lambda x: x != 2) == [0, 2, 4]


def test_lazy_list_zip():
    _list = LazyList(range(5))
    result = LazyList(range(5)).reverse()
    for z, _a, _b in zip(_list.zip(result), _list, result):
        assert z == (_a, _b)


def test_lazy_list_zip_longest():
    _list = LazyList(range(10))
    result = range(5)
    assert _list.zip_longest(result).get_length_eagerly() == _list.get_length_eagerly()


def test_lazy_list_accumulate():
    _list = LazyList([1, 2, 3, 4])
    assert _list.accumulate(lambda x, y: x * y) == [1, 2, 6, 24]


def test_lazy_list_combination():
    _list = LazyList([1, 2, 3, 4])
    result = _list.combinations(2)
    assert result.get_length_eagerly() == 6


def test_lazy_list_combinations_with_replacement():
    _list = LazyList([1, 2, 3, 4])
    result = _list.combinations_with_replacement(2)
    assert result.get_length_eagerly() == 10


def test_lazy_list_permutations():
    _list = LazyList([1, 2, 3, 4])
    result = _list.permutations(2)
    assert result.get_length_eagerly() == 12


def test_lazy_list_compress():
    _list = LazyList([1, 2, 3, 4])
    result = [True, False, 1, 0]
    assert _list.compress(result) == [1, 3]


def test_lazy_list_dropwhile():
    def _predicate(x):
        return x < 5

    _list = LazyList(range(10))
    result = _list.dropwhile(_predicate)
    assert all(not _predicate(o) for o in result)


def test_lazy_list_takewhile():
    def _predicate(x):
        return x < 5

    _list = LazyList(range(10))
    result = _list.takewhile(_predicate)
    assert all(_predicate(o) for o in result)


def test_lazy_list_filter_false():
    _list = LazyList(range(10))
    assert _list.filterfalse(lambda x: bool(x % 2)) == _list.filter(lambda x: not (x % 2))


def test_lazy_list_loop():
    _list = LazyList([1, 2, 3])
    result = _list.loop(3)
    assert result.get_length_eagerly() == _list.get_length_eagerly() * 3


def test_lazy_list_interleave():
    list1 = LazyList(range(5))
    list2 = list(range(6, 10))
    list3 = list(range(10, 20))
    result = list1.interleave(list2, list3)
    assert result.get_length_eagerly() == list1.get_length_eagerly() + len(list2 + list3)
    assert result.slice(stop=3) == [list1.first, list2[0], list3[0]]


def test_lazy_list_unique():
    _list = LazyList([1, 2, 3, 4, 4, 3, 2, 1])
    result = _list.unique()
    assert result.get_length_eagerly() == 4
    for i in _list:
        assert i in result


def test_lazy_list_take_nth():
    _list = LazyList(range(6))
    assert _list.take_nth(2) == [0, 2, 4]


def test_lazy_list_groupby():
    _list = LazyList(range(6))
    result = _list.group_by(lambda x: x % 2)
    assert result[0] == [0, 2, 4]
    assert result[1] == [1, 3, 5]


def test_lazy_list_get_item_dict():
    _list = LazyList([{"_list": 1}, {"_list": 2}])
    assert _list.get_item("_list") == [1, 2]


def test_lazy_list_get_item_sequence():
    _list = LazyList([(0, 1, 2), (3, 4, 5), (6, 7, 8)])
    assert _list.get_item(1) == [1, 4, 7]


def test_lazy_list_get_attr():
    Point = namedtuple("Point", ["x", "y"])
    _list = LazyList([Point(1, 2), Point(3, 4), Point(5, 6)])
    result = _list.get_attr("x")
    assert result == [1, 3, 5]
    assert isinstance(result, LazyList)


def test_lazy_list_clear():
    _list = LazyList(range(10))
    result = _list.clear()
    assert result.get_length_eagerly() == 0
    assert isinstance(result, LazyList)


def test_lazy_list_copy():
    _list = LazyList(range(10))
    result = _list.copy()
    assert result.evaluate() == _list.evaluate()
    assert result is not _list
    assert isinstance(result, LazyList)


def test_lazy_list_pop_invalid():
    _list = LazyList([1, 2, 3, 4, 5])
    with pytest.raises(IndexError):
        _list.pop(-1)


def test_lazy_list_index_error():
    _list = LazyList([1, 2, 3, 4, 5])
    with pytest.raises(ValueError):
        _list.index(6)


def test_lazy_list_contains_method():
    _list = LazyList([1, 2, 3, 4, 5])
    assert _list.contains(3)
    assert not _list.contains(6)


def test_lazy_list_sort_with_key():
    _list = LazyList([1, 2, 3, 4, 5])
    result = _list.sort(key=lambda x: 1 / x)
    assert result == [5, 4, 3, 2, 1]
    assert isinstance(result, LazyList)


def test_lazy_list_product():
    _list = LazyList([1, 2, 3])
    result = _list.product([4, 5])
    assert result.get_length_eagerly() == 6
    assert result == [(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)]
    assert isinstance(result, LazyList)


def test_lazy_list_is_distict():
    _list = LazyList([1, 2, 3, 4, 5])
    assert _list.is_distinct()
    result = _list.append(1)
    assert not result.is_distinct()


def test_lazy_list_take():
    _list = LazyList(range(10))
    assert _list.take(0) == []
    assert _list.take(3) == [0, 1, 2]
    assert _list.take(20) == list(range(10))
    assert isinstance(_list.take(5), LazyList)


def test_lazy_list_drop():
    _list = LazyList(range(10))
    assert _list.drop(0) == list(range(10))
    assert _list.drop(3) == [3, 4, 5, 6, 7, 8, 9]
    assert _list.drop(20) == []
    assert isinstance(_list.drop(5), LazyList)


def test_lazy_list_concat():
    _list = LazyList(range(5))
    result = _list.concat([LazyList([5, 6, 7]), [8, 9, 10]])
    assert result.get_length_eagerly() == 11
    assert result == list(range(11))
    assert isinstance(result, LazyList)


def test_lazy_list_interpose():
    _list = LazyList(range(5))
    result = _list.interpose(0)
    assert result.get_length_eagerly() == 9
    assert result == [0, 0, 1, 0, 2, 0, 3, 0, 4]
    assert isinstance(result, LazyList)


def test_lazy_list_frequencies():
    _list = LazyList([1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 1])
    result = _list.frequencies()
    assert result == {1: 4, 2: 3, 3: 2, 4: 1, 5: 1}


def test_lazy_list_reduce_by():
    _list = LazyList([1, 2, 3, 4, 5, 1])
    result = _list.reduce_by(lambda x: x % 2, lambda x, y: x + y)
    assert result == {0: 6, 1: 10}


def test_lazy_list_partition():
    _list = LazyList(range(7))
    result = _list.partition(3)
    assert result.evaluate() == [(0, 1, 2), (3, 4, 5)]


def test_lazy_list_partition_with_pad():
    _list = LazyList(range(7))
    result = _list.partition(3, pad=-1)
    assert result.evaluate() == [(0, 1, 2), (3, 4, 5), (6, -1, -1)]


def test_lazy_list_partition_all():
    _list = LazyList(range(7))
    result = _list.partition_all(3)
    assert result.evaluate() == [(0, 1, 2), (3, 4, 5), (6,)]


def test_lazy_list_tail():
    _list = LazyList(range(10))
    result = _list.tail(3)
    assert result == [7, 8, 9]
    assert isinstance(result, LazyList)


def test_lazy_list_top_k():
    _list = LazyList([5, 2, 6, 3, 7, 4, 8, 1, 9])
    result = _list.top_k(3)
    assert result == [9, 8, 7]
    assert isinstance(result, LazyList)


def test_lazy_list_top_k_with_key():
    _list = LazyList([5, 2, -6, -3, -7, 4, -8, 1, 9])
    result = _list.top_k(3, key=abs)
    assert result.evaluate() == [9, -8, -7]
    assert isinstance(result, LazyList)


def test_lazy_list_random_sample():
    _list = LazyList(range(10))
    result = _list.random_sample(3)
    for i in result:
        assert _list.contains(i)
    assert isinstance(result, LazyList)


def test_lazy_list_random_sample_seed():
    _list = LazyList(range(10))
    sample1 = _list.random_sample(3, random_state=1).evaluate()
    sample2 = _list.random_sample(3, random_state=1).evaluate()
    sample3 = _list.random_sample(3, random_state=2).evaluate()
    assert sample1 == sample2
    assert sample1 != sample3


def test_lazy_list_find_first():
    _list = LazyList([1, 2, 4, 8, 16])
    result = _list.find_first(lambda x: x > 10)
    assert result == 16


def test_lazy_list_find_first_no_result():
    _list = LazyList([1, 2, 4, 8, 16])
    with pytest.raises(ValueError):
        _list.find_first(lambda x: x > 20)


def test_lazy_list_find_first_index():
    _list = LazyList([1, 2, 4, 8, 16, 32, 64])
    result = _list.find_first_index(lambda x: x > 10)
    assert result == 4


def test_lazy_list_find_first_index_no_result():
    _list = LazyList([1, 2, 4, 8, 16])
    with pytest.raises(ValueError):
        _list.find_first_index(lambda x: x > 20)


def test_lazy_list_find_last():
    _list = LazyList([1, 2, 4, 8, 16])
    result = _list.find_last(lambda x: x < 10)
    assert result == 8


def test_lazy_list_find_last_no_result():
    _list = LazyList([1, 2, 4, 8, 16])
    with pytest.raises(ValueError):
        _list.find_last(lambda x: x > 20)


def test_lazy_list_find_last_index():
    _list = LazyList([1, 2, 4, 8, 16, 32, 64])
    result = _list.find_last_index(lambda x: x < 10)
    assert result == 3


def test_lazy_list_find_last_index_no_result():
    _list = LazyList([1, 2, 4, 8, 16])
    with pytest.raises(ValueError):
        _list.find_last_index(lambda x: x > 20)


def test_lazy_list_call_method():
    _list = LazyList(["a", "b", "c", "d", "e"])
    result = _list.call_method("upper")
    assert result == ["A", "B", "C", "D", "E"]


def test_lazy_list_second():
    _list = LazyList([1, 2, 3, 4, 5])
    assert _list.second == 2


def test_lazy_list_to_set():
    _list = LazyList([1, 2, 3, 4, 5])
    assert _list.to_set() == {1, 2, 3, 4, 5}


def test_lazy_list_to_deque():
    _list = LazyList([1, 2, 3, 4, 5])
    assert _list.to_deque() == deque([1, 2, 3, 4, 5])
