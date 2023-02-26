from __future__ import annotations
from typing import List, TypeVar, overload, Tuple
from lazy_list.eager_list import EagerList

X = TypeVar("X")


class StrList(EagerList[str]):

    def __str__(self) -> str:
        return f"StrList{list(self)}"

    def __repr__(self) -> str:
        return f"StrList({list(self)})"

    def capitaliz(self):
        return self.map(str.capitalize)

    def casefold(self):
        return self.map(str.casefold)

    def center(self, width: int):
        return self.map(lambda x: str.center(x, width))

    def str_count(
        self,
        substring: str,
        start: int | None = None,
        end: int | None = None,
    ):
        return self.map(lambda x: str.count(x, substring, start, end))

    def encode(self, encoding: str = "utf-8", errors: str = "strict"):
        return self.map(
            lambda x: str.encode(x, encoding=encoding, errors=errors))

    def endswith(
        self,
        suffix: str,
        start: int | None = None,
        end: int | None = None,
    ) -> EagerList[bool]:
        return self.map(lambda x: str.endswith(x, suffix, start, end))

    def exapndtabs(self, tabsize: int = 8):
        return self.map(lambda x: str.expandtabs(x, tabsize))

    def find(
        self,
        substring: str,
        start: int | None = None,
        end: int | None = None,
    ):
        return self.map(lambda x: str.find(x, substring, start, end))

    def format(self, *args, **kwargs):
        return self.map(lambda x: str.format(x, *args, **kwargs))

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

    def join(self, sep: str = " "):
        return sep.join(self)

    def ljust(self, width: int, fillchar: str = ""):
        return self.map(lambda x: str.ljust(x, width, fillchar))

    def lower(self):
        return self.map(str.lower)

    def lstrip(self, chars: str | None = None):
        return self.map(lambda x: str.lstrip(x, chars))

    def str_partition(self, sep: str) -> EagerList[Tuple[str, str, str]]:
        return self.map(lambda x: str.partition(x, sep))

    def replace(self, old: str, new: str, count: int = -1):
        return self.map(lambda x: str.replace(x, old, new, count))

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

    def rjust(self, width: int, fillchar: str = ' '):
        return self.map(lambda x: str.rjust(x, width, fillchar))

    def rpartition(self, sep: str):
        return self.map(lambda x: str.rpartition(x, sep))

    def rsplit(self, sep: str | None = None, maxsplit: int = -1):
        return self.map(lambda x: str.rsplit(x, sep, maxsplit))

    def rstrip(self, chars: str):
        return self.map(lambda x: str.rstrip(x, chars))

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
        return self.map(lambda x: str.strip(x, chars))

    def swapcase(self):
        return self.map(str.swapcase)

    def title(self):
        return self.map(str.title)

    def translate(self, table):
        return self.map(lambda x: str.translate(x, table))

    def upper(self):
        return self.map(str.upper)

    def zfill(self, width: int):
        return self.map(lambda x: str.zfill(x, width))
