from __future__ import annotations

import re
from operator import methodcaller
from typing import Any, Dict, Iterable, Tuple, TypeVar

from lazy_list.eager_list import EagerList

X = TypeVar("X")


class StrList(EagerList[str]):
    def __str__(self) -> str:
        return f"StrList{list(self)}"

    def __repr__(self) -> str:
        return f"StrList({list(self)})"

    def capitalize(self):
        return StrList(self.map(str.capitalize))

    def casefold(self):
        return StrList(self.map(str.casefold))

    def center(self, width: int, fill_char: str = " "):
        return StrList(self.map(lambda x: str.center(x, width, fill_char)))

    def str_count(
        self,
        substring: str,
        start: int | None = None,
        end: int | None = None,
    ) -> EagerList[int]:
        return self.map(lambda x: str.count(x, substring, start, end))

    def encode(self, encoding: str = "utf-8", errors: str = "strict"):
        return self.map(lambda x: str.encode(x, encoding=encoding, errors=errors))

    def endswith(
        self,
        suffix: str,
        start: int | None = None,
        end: int | None = None,
    ) -> EagerList[bool]:
        return self.map(lambda x: str.endswith(x, suffix, start, end))

    def expandtabs(self, tabsize: int = 8):
        return StrList(self.map(lambda x: str.expandtabs(x, tabsize)))

    def find(
        self,
        substring: str,
        start: int | None = None,
        end: int | None = None,
    ):
        return self.map(lambda x: str.find(x, substring, start, end))

    def format(self, *args, **kwargs):
        return StrList(self.map(lambda x: str.format(x, *args, **kwargs)))

    def format_map(
        self,
        args: Iterable[Tuple[Any, ...]] | None = None,
        kwargs: Iterable[Dict[str, Any]] | None = None,
    ):
        _args = args or self.fixed(tuple())
        _kwargs = kwargs or self.fixed({})
        return StrList(self.zip(_args, _kwargs).map(lambda x: str.format(x[0], *x[1], **x[2])))

    def str_index(
        self,
        substring: str,
        start: int | None = None,
        end: int | None = None,
    ):
        return self.map(lambda x: str.index(x, substring, start, end))

    def isalnum(self):
        return self.map(str.isalnum)

    def isalpha(self):
        return self.map(str.isalpha)

    def isascii(self):
        return self.map(str.isascii)

    def isdecimal(self):
        return self.map(str.isdecimal)

    def isdigit(self):
        return self.map(str.isdigit)

    def isidentifier(self):
        return self.map(str.isidentifier)

    def islower(self):
        return self.map(str.islower)

    def isnumeric(self):
        return self.map(str.isnumeric)

    def isprintable(self):
        return self.map(str.isprintable)

    def isspace(self):
        return self.map(str.isspace)

    def istitle(self):
        return self.map(str.istitle)

    def isupper(self):
        return self.map(str.isupper)

    def ljust(self, width: int, fillchar: str = " "):
        return StrList(self.map(lambda x: str.ljust(x, width, fillchar)))

    def lower(self):
        return StrList(self.map(str.lower))

    def lstrip(self, chars: str | None = None):
        return StrList(self.map(lambda x: str.lstrip(x, chars)))

    def str_partition(self, sep: str) -> EagerList[Tuple[str, str, str]]:
        return self.map(lambda x: str.partition(x, sep))

    def str_replace(self, old: str, new: str, count: int = -1):
        return StrList(self.map(lambda x: str.replace(x, old, new, count)))

    def rfind(
        self,
        substring: str,
        start: int | None = None,
        end: int | None = None,
    ):
        return self.map(lambda x: str.rfind(x, substring, start, end))

    def rindex(
        self,
        substring: str,
        start: int | None = None,
        end: int | None = None,
    ):
        return self.map(lambda x: str.rindex(x, substring, start, end))

    def rjust(self, width: int, fillchar: str = " "):
        return StrList(self.map(lambda x: str.rjust(x, width, fillchar)))

    def rpartition(self, sep: str):
        return self.map(lambda x: str.rpartition(x, sep))

    def rsplit(self, sep: str | None = None, maxsplit: int = -1):
        return self.map(lambda x: str.rsplit(x, sep, maxsplit))

    def rstrip(self, chars: str = " "):
        return StrList(self.map(lambda x: str.rstrip(x, chars)))

    def split(self, sep: str | None = None, maxsplit: int = -1):
        return self.map(lambda x: str.split(x, sep, maxsplit))

    def splitlines(self, keepends: bool = False):
        return self.map(lambda x: str.splitlines(x, keepends))

    def startswith(
        self,
        prefix: str | Tuple[str, ...],
        start: int | None = None,
        end: int | None = None,
    ):
        return self.map(lambda x: str.startswith(x, prefix, start, end))

    def strip(self, chars: str | None = None):
        return StrList(self.map(lambda x: str.strip(x, chars)))

    def swapcase(self):
        return StrList(self.map(str.swapcase))

    def title(self):
        return StrList(self.map(str.title))

    def translate(self, table):
        return StrList(self.map(lambda x: str.translate(x, table)))

    def upper(self):
        return StrList(self.map(str.upper))

    def zfill(self, width: int):
        return StrList(self.map(lambda x: str.zfill(x, width)))

    def is_number(self):
        def _is_number(x: str) -> bool:
            try:
                float(x)
                return True
            except ValueError:
                return False

        return self.map(_is_number)

    def filter_endswith(
        self,
        suffix: str,
        start: int | None = None,
        end: int | None = None,
        inverse: bool = False,
    ):
        function = methodcaller("endswith", suffix, start, end)
        return StrList(self.filterfalse(function) if inverse else self.filter(function))

    def filter_startswith(
        self,
        prefix: str,
        start: int | None = None,
        end: int | None = None,
        inverse: bool = False,
    ):
        function = methodcaller("startswith", prefix, start, end)
        return StrList(self.filterfalse(function) if inverse else self.filter(function))

    def filter_isalnum(self, inverse: bool = False):
        function = methodcaller("isalnum")
        return StrList(self.filterfalse(function) if inverse else self.filter(function))

    def filter_isalpha(self, inverse: bool = False):
        function = methodcaller("isalpha")
        return StrList(self.filterfalse(function) if inverse else self.filter(function))

    def filter_isascii(self, inverse: bool = False):
        function = methodcaller("isascii")
        return StrList(self.filterfalse(function) if inverse else self.filter(function))

    def filter_isdecimal(self, inverse: bool = False):
        function = methodcaller("isdecimal")
        return StrList(self.filterfalse(function) if inverse else self.filter(function))

    def filter_isdigit(self, inverse: bool = False):
        function = methodcaller("isdigit")
        return StrList(self.filterfalse(function) if inverse else self.filter(function))

    def filter_isidentifier(self, inverse: bool = False):
        function = methodcaller("isidentifier")
        return StrList(self.filterfalse(function) if inverse else self.filter(function))

    def filter_islower(self, inverse: bool = False):
        function = methodcaller("islower")
        return StrList(self.filterfalse(function) if inverse else self.filter(function))

    def filter_isnumeric(self, inverse: bool = False):
        function = methodcaller("isnumeric")
        return StrList(self.filterfalse(function) if inverse else self.filter(function))

    def filter_isprintable(self, inverse: bool = False):
        function = methodcaller("isprintable")
        return StrList(self.filterfalse(function) if inverse else self.filter(function))

    def filter_isspace(self, inverse: bool = False):
        function = methodcaller("isspace")
        return StrList(self.filterfalse(function) if inverse else self.filter(function))

    def filter_istitle(self, inverse: bool = False):
        function = methodcaller("istitle")
        return StrList(self.filterfalse(function) if inverse else self.filter(function))

    def filter_isupper(self, inverse: bool = False):
        function = methodcaller("isupper")
        return StrList(self.filterfalse(function) if inverse else self.filter(function))

    def filter_is_number(self, inverse: bool = False):
        def _is_number(x: str) -> bool:
            try:
                float(x)
                return True
            except ValueError:
                return False

        return StrList(self.filterfalse(_is_number) if inverse else self.filter(_is_number))

    def find_all(self, pattern: str, flags: re._FlagsType = 0):
        """Use regex to find all matches in every element."""
        return self.map(lambda x: re.findall(pattern, x, flags))

    def find_first_match(self, pattern: str, flags: re._FlagsType = 0):
        """Use regex to find the first match in every element.
        Return empty string if no match found.
        """

        def _find_first(pattern, string, flags):
            try:
                return next(re.finditer(pattern, string, flags)).group()
            except StopIteration:
                return ""

        return StrList(self.map(lambda x: _find_first(pattern, x, flags)))

    def is_fullmatch(self, pattern: str, flags: re._FlagsType = 0):
        """Apply the pattern to the entire element and returns True if is a match."""
        return self.map(lambda x: bool(re.fullmatch(pattern, x, flags)))

    def filter_fullmatch(self, pattern: str, flags: re._FlagsType = 0):
        """Apply the pattern to the entire element and return element if is a match."""
        return StrList(self.filter(lambda x: bool(re.fullmatch(pattern, x, flags))))

    def is_match(self, pattern: str, flags: re._FlagsType = 0):
        """Apply the pattern at the start of the element and returns True if is a match."""
        return self.map(lambda x: bool(re.match(pattern, x, flags)))

    def filter_match(self, pattern: str, flags: re._FlagsType = 0):
        """Apply the pattern at the start of the element and return element if is a match."""
        return StrList(self.filter(lambda x: bool(re.match(pattern, x, flags))))

    def find_match_groups(self, pattern: str, flags: re._FlagsType = 0):
        return self.map(lambda x: re.match(pattern, x, flags)).map(lambda x: x if x is None else x.groups())

    def sub(
        self,
        pattern,
        replacement: str,
        count: int = 0,
        flags: re._FlagsType = 0,
    ):
        """Apply `re.sub` to each element"""
        return StrList(self.map(lambda x: re.sub(pattern, replacement, x, count, flags)))

    def subn(
        self,
        pattern,
        replacement: str,
        count: int = 0,
        flags: re._FlagsType = 0,
    ):
        """Apply `re.subn` to each element"""
        return self.map(lambda x: re.subn(pattern, replacement, x, count, flags))
