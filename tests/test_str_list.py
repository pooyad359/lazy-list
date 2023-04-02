import pytest

from lazy_list import EagerList, StrList


def test_str_list_str():
    _list = StrList(["a", "b", "c"])
    assert str(_list) == "StrList['a', 'b', 'c']"


def test_str_list_repr():
    _list = StrList(["a", "b", "c"])
    assert repr(_list) == "StrList(['a', 'b', 'c'])"


def test_str_list_capitalize():
    _list = StrList(["a", "b", "c"])
    result = _list.capitalize()
    expected = ["A", "B", "C"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_casefold():
    _list = StrList(["a", "B", "cC"])
    result = _list.casefold()
    expected = ["a", "b", "cc"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_center():
    _list = StrList(["a", "b", "c"])
    result = _list.center(3)
    expected = [" a ", " b ", " c "]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_center_fill_char():
    _list = StrList(["a", "b", "c"])
    result = _list.center(3, "*")
    expected = ["*a*", "*b*", "*c*"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_str_count_basic():
    _list = StrList(["abc", "bbca", "cbb", "aaa"])
    result = _list.str_count("b")
    expected = [1, 2, 2, 0]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_str_count_range():
    _list = StrList(["abc", "bbca", "cbb", "aaaab"])
    result = _list.str_count("b", 1, 3)
    expected = [1, 1, 2, 0]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_encode():
    _list = StrList(["a", "b", "c"])
    result = _list.encode()
    expected = [b"a", b"b", b"c"]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_endswith():
    _list = StrList(["abc", "bbca", "cbb", "aaaab"])
    result = _list.endswith("b")
    expected = [False, False, True, True]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_endswith_range():
    _list = StrList(["abc", "bbca", "cbb", "aaaab"])
    result = _list.endswith("b", 0, 2)
    expected = [True, True, True, False]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_expandtabs():
    _list = StrList(["a\tb", "b\tc", "c\td"])
    result = _list.expandtabs()
    expected = ["a       b", "b       c", "c       d"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_find():
    _list = StrList(["abc", "bbca", "cbb", "aaaab"])
    result = _list.find("b")
    expected = [1, 0, 1, 4]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_find_range():
    _list = StrList(["abc", "bbca", "cbb", "aaaab"])
    result = _list.find("b", 1, 3)
    expected = [1, 1, 1, -1]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_find_not_found():
    _list = StrList(["abc", "bbca", "cbb", "aaaab"])
    result = _list.find("d")
    expected = [-1, -1, -1, -1]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_format_arg():
    _list = StrList(["a{}", "b{}", "c{}"])
    result = _list.format(1)
    excepted = ["a1", "b1", "c1"]
    assert result == excepted
    assert isinstance(result, StrList)


def test_str_list_format_kwargs():
    _list = StrList(["a{a}{b}", "b{b}{c}", "c{c}{a}"])
    result = _list.format(a=1, b=2, c=3)
    excepted = ["a12", "b23", "c31"]
    assert result == excepted
    assert isinstance(result, StrList)


def test_str_list_format_map_basic_args():
    _list = StrList(["a{}", "b{}", "c{}"])
    result = _list.format_map(args=[(1,), (2,), (3,)])
    excepted = ["a1", "b2", "c3"]
    assert result == excepted
    assert isinstance(result, StrList)


def test_str_list_format_map_basic_kwargs():
    _list = StrList(["a{a}", "b{a}", "c{a}"])
    result = _list.format_map(kwargs=[dict(a=1), dict(a=2), dict(a=3)])
    excepted = ["a1", "b2", "c3"]
    assert result == excepted
    assert isinstance(result, StrList)


def test_str_list_format_map_basic_args_kwargs():
    _list = StrList(["a{}{a}", "b{}{a}", "c{}{a}"])
    result = _list.format_map(
        args=[(1,), (2,), (3,)],
        kwargs=[dict(a=4), dict(a=5), dict(a=6)],
    )
    excepted = ["a14", "b25", "c36"]
    assert result == excepted
    assert isinstance(result, StrList)


def test_str_list_str_index_basic():
    _list = StrList(["abc", "bbca", "cbb", "aaaab"])
    result = _list.str_index("b")
    expected = [1, 0, 1, 4]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_str_index_range():
    _list = StrList(["abcb", "babca", "cbb", "aaaab"])
    result = _list.str_index("b", 2)
    expected = [3, 2, 2, 4]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_str_index_not_found():
    _list = StrList(["abc", "bbca", "cbb", "aaaab"])
    with pytest.raises(ValueError):
        _list.str_index("d")


def test_str_list_isalnum():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1"])
    result = _list.isalnum()
    expected = [True, True, True, False, True, False]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_isalpha():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1"])
    result = _list.isalpha()
    expected = [True, False, False, False, False, False]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_isascii():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1", "你好"])
    result = _list.isascii()
    expected = [True, True, True, True, True, True, False]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_isdecimal():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1"])
    result = _list.isdecimal()
    expected = [False, True, True, False, False, False]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_isdigit():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1"])
    result = _list.isdigit()
    expected = [False, True, True, False, False, False]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_isidentifier():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1"])
    result = _list.isidentifier()
    expected = [True, False, False, False, True, True]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_islower():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1", "Aa", "A"])
    result = _list.islower()
    expected = [True, False, False, False, True, True, False, False]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_isnumeric():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1"])
    result = _list.isnumeric()
    expected = [False, True, True, False, False, False]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_isprintable():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1", chr(1)])
    result = _list.isprintable()
    expected = [True, True, True, True, True, True, False]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_isspace():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1", " "])
    result = _list.isspace()
    expected = [False, False, False, False, False, False, True]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_istitle():
    _list = StrList(["a", "1a", "A a", "1.2", "b1", "b_1", "Aa", "A"])
    result = _list.istitle()
    expected = [False, False, False, False, False, False, True, True]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_isupper():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1", "Aa", "A"])
    result = _list.isupper()
    expected = [False, False, False, False, False, False, False, True]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_ljust():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1"])
    result = _list.ljust(5)
    expected = ["a    ", "1    ", "12   ", "1.2  ", "b1   ", "b_1  "]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_lower():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1", "Aa", "A"])
    result = _list.lower()
    expected = ["a", "1", "12", "1.2", "b1", "b_1", "aa", "a"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_lstrip():
    _list = StrList(["a  ", " 1", " 12 ", "1.2", "b1", "b_1", "Aa", "  A"])
    result = _list.lstrip()
    expected = ["a  ", "1", "12 ", "1.2", "b1", "b_1", "Aa", "A"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_lstrip_char():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1", "Aa", "A"])
    result = _list.lstrip("1")
    expected = ["a", "", "2", ".2", "b1", "b_1", "Aa", "A"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_str_partition():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1", "Aa", "A"])
    result = _list.str_partition("1")
    expected = [
        ("a", "", ""),
        ("", "1", ""),
        ("", "1", "2"),
        ("", "1", ".2"),
        ("b", "1", ""),
        ("b_", "1", ""),
        ("Aa", "", ""),
        ("A", "", ""),
    ]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_str_replace():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1", "Aa", "A"])
    result = _list.str_replace("1", "2")
    expected = ["a", "2", "22", "2.2", "b2", "b_2", "Aa", "A"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_rfind():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1", "Aa", "1A1"])
    result = _list.rfind("1")
    expected = [-1, 0, 0, 0, 1, 2, -1, 2]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_rindex():
    _list = StrList(["1", "12", "1.2", "b1", "b_1", "1A1"])
    result = _list.rindex("1")
    expected = [0, 0, 0, 1, 2, 2]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_rjust():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1"])
    result = _list.rjust(5)
    expected = ["    a", "    1", "   12", "  1.2", "   b1", "  b_1"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_rpartition():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1", "Aa", "1A1"])
    result = _list.rpartition("1")
    expected = [
        ("", "", "a"),
        ("", "1", ""),
        ("", "1", "2"),
        ("", "1", ".2"),
        ("b", "1", ""),
        ("b_", "1", ""),
        ("", "", "Aa"),
        ("1A", "1", ""),
    ]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_rsplit():
    _list = StrList(["a", "1", "1212", "1.2", "b1", "b_1", "A1a", "1A1"])
    result = _list.rsplit("1")
    expected = [["a"], ["", ""], ["", "2", "2"], ["", ".2"], ["b", ""], ["b_", ""], ["A", "a"], ["", "A", ""]]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_split():
    _list = StrList(["a", "1", "1212", "1.2", "b1", "b_1", "A1a", "1A1"])
    result = _list.split("1")
    expected = [["a"], ["", ""], ["", "2", "2"], ["", ".2"], ["b", ""], ["b_", ""], ["A", "a"], ["", "A", ""]]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_str_splitlines():
    _list = StrList(["a\nb", "1\n2", "1212", "1.2", "b1", "b_1", "A1a", "1A1"])
    result = _list.splitlines()
    expected = [["a", "b"], ["1", "2"], ["1212"], ["1.2"], ["b1"], ["b_1"], ["A1a"], ["1A1"]]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_startswith():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1", "Aa", "1A1"])
    result = _list.startswith("1")
    expected = [False, True, True, True, False, False, False, True]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_strip():
    _list = StrList(["a  ", "1", "12 ", "1.2", "b1", "b_1", "Aa", "A"])
    result = _list.strip()
    expected = ["a", "1", "12", "1.2", "b1", "b_1", "Aa", "A"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_swapcase():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1", "Aa", "A"])
    result = _list.swapcase()
    expected = ["A", "1", "12", "1.2", "B1", "B_1", "aA", "a"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_title():
    _list = StrList(["a", "aa a", "12", "1.2", "b1", "b_1", "Aa", "A"])
    result = _list.title()
    expected = ["A", "Aa A", "12", "1.2", "B1", "B_1", "Aa", "A"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_translate():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1", "Aa", "A"])
    result = _list.translate(str.maketrans("1", "2"))
    expected = ["a", "2", "22", "2.2", "b2", "b_2", "Aa", "A"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_upper():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1", "Aa", "A"])
    result = _list.upper()
    expected = ["A", "1", "12", "1.2", "B1", "B_1", "AA", "A"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_zfill():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1", "Aa", "A"])
    result = _list.zfill(5)
    expected = ["0000a", "00001", "00012", "001.2", "000b1", "00b_1", "000Aa", "0000A"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_is_number():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1"])
    result = _list.is_number()
    expected = [False, True, True, True, False, False]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_filter_endswith():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1"])
    result = _list.filter_endswith("1")
    expected = ["1", "b1", "b_1"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_filter_startswith():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1", "Aa", "1A1"])
    result = _list.startswith("1")
    expected = [False, True, True, True, False, False, False, True]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_filter_isalnum():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1"])
    result = _list.filter_isalnum()
    expected = ["a", "1", "12", "b1"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_filter_isalpha():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1", "aA"])
    result = _list.filter_isalpha()
    expected = ["a", "aA"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_filter_isascii():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1", "aA", "€"])
    result = _list.filter_isascii()
    expected = ["a", "1", "12", "1.2", "b1", "b_1", "aA"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_filter_isdecimal():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1", "aA", "€"])
    result = _list.filter_isdecimal()
    expected = ["1", "12"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_filter_isdigit():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1", "aA", "€"])
    result = _list.filter_isdigit()
    expected = ["1", "12"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_filter_isdigit_inverse():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1", "aA", "€"])
    result = _list.filter_isdigit(inverse=True)
    expected = ["a", "1.2", "b1", "b_1", "aA", "€"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_filter_isidentifier():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1", "aA", "€"])
    result = _list.filter_isidentifier()
    expected = ["a", "b1", "b_1", "aA"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_filter_islower():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1", "aA", "€"])
    result = _list.filter_islower()
    expected = ["a", "b1", "b_1"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_filter_isnumeric():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1", "aA", "€"])
    result = _list.filter_isnumeric()
    expected = ["1", "12"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_filter_isprintable():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1", "aA", chr(1)])
    result = _list.filter_isprintable()
    expected = ["a", "1", "12", "1.2", "b1", "b_1", "aA"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_filter_isspace():
    _list = StrList(["a", "1", "12", "1.2", "b1", "b_1", "aA", " "])
    result = _list.filter_isspace()
    expected = [" "]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_filter_istitle():
    _list = StrList(["a", "Abc A", "12", "1.2", "b1", "b_1", "aA", "A"])
    result = _list.filter_istitle()
    expected = ["Abc A", "A"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_filter_isupper():
    _list = StrList(["a", "Abc A", "12", "1.2", "b1", "b_1", "BA", "A"])
    result = _list.filter_isupper()
    expected = ["BA", "A"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_filter_is_number():
    _list = StrList(["a", "1", "12", "-1.2", "b1", "b_1", "01"])
    result = _list.filter_is_number()
    expected = ["1", "12", "-1.2", "01"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_find_all():
    _list = StrList(["a", "1", "12", "-1.2", "b1", "b_1", "01"])
    result = _list.find_all(r"(\d+)")
    expected = [[], ["1"], ["12"], ["1", "2"], ["1"], ["1"], ["01"]]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_find_first_match():
    _list = StrList(["a", "1", "12", "-1.2", "b1", "b_1", "01"])
    result = _list.find_first_match(r"(\d+)")
    expected = ["", "1", "12", "1", "1", "1", "01"]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_is_fullmatch():
    _list = StrList(["a", "1", "12", "-1.2", "b1", "b_1", "01"])
    result = _list.is_fullmatch(r"(\d+)")
    expected = [False, True, True, False, False, False, True]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_filter_is_fullmatch():
    _list = StrList(["a", "1", "12", "-1.2", "b1", "b_1", "01"])
    result = _list.filter_fullmatch(r"(\d+)")
    expected = ["1", "12", "01"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_is_match():
    _list = StrList(["a", "1", "12", "-1.2", "b1", "b_1", "01"])
    result = _list.is_match(r"(\d+)")
    expected = [False, True, True, False, False, False, True]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_filter_is_match():
    _list = StrList(["a", "1", "12", "-1.2", "b1", "b_1", "01"])
    result = _list.filter_match(r"(\d+)")
    expected = ["1", "12", "01"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_find_match_groups():
    _list = StrList(["a", "1", "12", "-1.2", "b1", "b_1", "01"])
    result = _list.find_match_groups(r"([a-z])(\d*)")
    expected = [("a", ""), None, None, None, ("b", "1"), ("b", ""), None]
    assert result == expected
    assert isinstance(result, EagerList)


def test_str_list_sub():
    _list = StrList(["a", "1", "12", "-1.2", "b1", "b_1", "01"])
    result = _list.sub(r"(\d+)", "X")
    expected = ["a", "X", "X", "-X.X", "bX", "b_X", "X"]
    assert result == expected
    assert isinstance(result, StrList)


def test_str_list_subn():
    _list = StrList(["a", "1", "12", "-1.2", "b1", "b_1", "01"])
    result = _list.subn(r"(\d+)", "X")
    expected = [("a", 0), ("X", 1), ("X", 1), ("-X.X", 2), ("bX", 1), ("b_X", 1), ("X", 1)]
    assert result == expected
    assert isinstance(result, EagerList)
