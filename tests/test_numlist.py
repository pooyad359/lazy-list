import math

from pytest import approx

from lazy_list.num_list import NumList


def test_numlist_default_map():
    lst = NumList([-1, -2])
    out = lst.default_map(math.log)
    for o in out:
        assert math.isnan(o)


def test_numlist_pow():
    lst = NumList([1, 2, 3])
    out = lst.pow(3)
    assert out == [1, 8, 27]
    assert isinstance(out, NumList)


def test_numlist_inverse():
    lst = NumList([1, 2, 3])
    out = lst.inverse()
    for i, j in zip(lst, out):
        assert j == approx(1 / i)
    assert isinstance(out, NumList)


def test_numlist_ceil():
    lst = NumList([-1.1, 1, 2.1, 4.6, 8.9999])
    expected = [-1, 1, 3, 5, 9]
    out = lst.ceil()
    for i, j in zip(expected, out):
        assert i == approx(j)
    assert isinstance(out, NumList)


def test_numlist_floor():
    lst = NumList([-1.1, 1, 2.1, 4.6, 8.9999])
    expected = [-2, 1, 2, 4, 8]
    out = lst.floor()
    for i, j in zip(expected, out):
        assert i == approx(j)
    assert isinstance(out, NumList)


def test_numlist_exp():
    lst = NumList([0, 1, 2, 3, 4])
    expected = [math.exp(o) for o in lst]
    out = lst.exp()
    for i, j in zip(expected, out):
        assert i == approx(j)
    assert isinstance(out, NumList)


def test_numlist_exp_n():
    lst = NumList([0, 1, 2, 3, 4])
    expected = [1, 2, 4, 8, 16]
    out = lst.exp_n(2)
    for i, j in zip(expected, out):
        assert i == approx(j)
    assert isinstance(out, NumList)


def test_numlist_abs():
    lst = NumList([-1, 0, 4.1])
    expected = [1, 0, 4.1]
    out = lst.abs()
    for i, j in zip(expected, out):
        assert i == j
    assert isinstance(out, NumList)


def test_numlist_is_close():
    lst = NumList([1, 0, 4.1, 1.234, 7 / 6])
    expected = [True, False, False, False, True]
    assert lst.is_close(1, abs_tol=0.2) == expected


def test_numlist_is_finite():
    lst = NumList([1, 4.1, math.nan, -2.54, math.inf, -math.inf])
    expected = [True, True, False, True, False, False]
    assert lst.is_finite() == expected


def test_numlist_is_inf():
    lst = NumList([1, 4.1, math.nan, -2.54, math.inf, -math.inf])
    expected = [False, False, False, False, True, True]
    assert lst.is_inf() == expected


def test_numlist_is_nan():
    lst = NumList([1, 4.1, math.nan, -2.54, math.inf, -math.inf])
    expected = [False, False, True, False, False, False]
    assert lst.is_nan() == expected


def test_numlist_log_e():
    lst = NumList([1, 2, 3])
    expected = [0, math.log(2), math.log(3)]
    out = lst.log()
    for i, j in zip(out, expected):
        assert i == approx(j)
    assert isinstance(out, NumList)


def test_numlist_log_3():
    lst = NumList([1, 3, 8, 27])
    expected = [0, 1, math.log(8, 3), 3]
    out = lst.log(3)
    for i, j in zip(out, expected):
        assert i == approx(j)
    assert isinstance(out, NumList)


def test_numlist_log10():
    lst = NumList([1, 10, 25, 1000])
    expected = [0, 1, math.log10(25), 3]
    out = lst.log10()
    for i, j in zip(out, expected):
        assert i == approx(j)
    assert isinstance(out, NumList)


def test_numlist_log1p():
    lst = NumList([1, 3, 5, 1000, 0.001])
    expected = [math.log1p(o) for o in lst]
    out = lst.log1p()
    for i, j in zip(out, expected):
        assert i == approx(j)
    assert isinstance(out, NumList)


def test_numlist_log_2():
    lst = NumList([1, 2, 4, 256, 1 / 4, 5])
    expected = [0, 1, 2, 8, -2, math.log2(5)]
    out = lst.log2()
    for i, j in zip(out, expected):
        assert i == approx(j)
    assert isinstance(out, NumList)


def test_numlist_modf():
    lst = NumList([1.1, 2, -3.35, 4])
    expected = [(0.1, 1), (0, 2), (-0.35, -3), (0, 4)]
    out = lst.modf()
    for i, j in zip(out, expected):
        assert i[0] == approx(j[0])
        assert i[1] == j[1]


def test_numlist_mod():
    lst = NumList([1, 2, 4, 6.55, 8.8])
    expected = [1, 2, 1, 0.55, 2.8]
    out = lst.mod(3)
    for i, j in zip(out, expected):
        assert i == approx(j)
    assert isinstance(out, NumList)


def test_numlist_sqrt():
    lst = NumList([1, 2, 4, 5, 9])
    expected = [1, 2**0.5, 2, 5**0.5, 3]
    out = lst.sqrt()
    for i, j in zip(out, expected):
        assert i == approx(j)
    assert isinstance(out, NumList)


def test_numlist_root():
    lst = NumList([1, 2, 8, 5, 27])
    expected = [1, 2 ** (1 / 3), 2, 5 ** (1 / 3), 3]
    out = lst.root(3)
    for i, j in zip(out, expected):
        assert i == approx(j)
    assert isinstance(out, NumList)


def test_numlist_trunc():
    lst = NumList([-5, -2.7, -2.3, 0, 2.3, 2.7, 5])
    expected = [-5, -2, -2, 0, 2, 2, 5]
    out = lst.trunc()
    for i, j in zip(out, expected):
        assert i == j
    assert isinstance(out, NumList)


def test_numlist_remainder():
    lst = NumList([1, 2, 4, 6.55, 8.8])
    expected = [1, -1, 1, 0.55, -0.2]
    out = lst.remainder(3)
    for i, j in zip(out, expected):
        assert i == approx(j)
    assert isinstance(out, NumList)


def test_numlist_cumsum():
    lst = NumList([1, 2, 3, 4])
    expected = [1, 3, 6, 10]
    out = lst.cum_sum()
    for i, j in zip(out, expected):
        assert i == approx(j)
    assert isinstance(out, NumList)


def test_numlist_window_reduce():
    lst = NumList(range(10))
    expected = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]
    out = lst.window_reduce(4, lambda *x: sum(x) / len(x))
    for i, j in zip(out, expected):
        assert i == approx(j)
    assert isinstance(out, NumList)


def test_numlist_diff():
    lst = NumList([1, 2, 4, 8])
    out = lst.diff()
    assert out == [1, 2, 4]
    assert isinstance(out, NumList)
