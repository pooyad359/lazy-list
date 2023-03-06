from lazy_list import StrList


def test_filter_isdigit():
    l = StrList(['a', '1', '12', '1.2', 'b1', 'b_1'])
    assert l.filter_isdigit() == ['1', '12']


def test_filter_isdigit_inverse():
    l = StrList(['a', '1', '12', '1.2', 'b1', 'b_1'])
    assert l.filter_isdigit(inverse=True) == ['a', '1.2', 'b1', 'b_1']