# Type hinting was introduces in 3.5 and above
# typing module was introduced.
# a lot of types were introduced

# glorified comments syntax..
from ast import TypeAlias
from dataclasses import dataclass
from typing import Any, Callable, Literal, NamedTuple, Optional, Union


def add(a: int, b: int) -> int:
    return a + b


# optional parameter. Is old.. modern python is int | None - Union types
def log(s: str, filename: str | None) -> None: ...


@dataclass
class C1:
    name: str
    height: Optional[int]


log("log entry", filename=None)

# added in 3.6 Variable annotation
# named typle was introduced


class NT(NamedTuple):
    x: int
    y: int


# list and dict dont need imports from typing since 3.9
def sq_all(l1: list[int]) -> dict[int, int]:
    return {i: (i**2) for i in l1}


print(sq_all([3, 4, 5]))


# Any data type is part of typing module
def fn(c: Any, b: int) -> Any: ...


# Unions -- This is also old syntax. modern syntax is: int | str
def multipy(item: Union[int, str], x: int) -> Union[str, int]: ...


# TypeAlias-- Newer syntax 3.12+
# type alias are written in Class syntax
type AnyList = list[int | str]


def get_id_or_name_list() -> AnyList: ...


# callables Syntax Callable[[<input params>], return_type]

some_func = Callable[[int], int]


def display(x: int) -> int:
    print("This fn is called. ", x)
    return x


def calling_fn(call_this: some_func, a: int) -> int:
    return call_this(a)


calling_fn(display, 10)

# Literals enforcing actual values that can be accepted by the funcation


def literal_ex(a: Literal["a", "b"], b: Literal[3, 4, 5]) -> None: ...


# also we can define a list and pass it
type AllowedLetters = Literal["a", "b"]
type AllowedNumbers = Literal[3, 4, 5]


def literal_ex2(
    a: AllowedLetters,
    b: AllowedNumbers,
    c: list[AllowedLetters],
) -> None: ...
