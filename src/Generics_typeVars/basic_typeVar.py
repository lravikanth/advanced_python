#all this is pre 3.12 version of python

from typing import TypeAlias, TypeVar

T = TypeVar("T")


def func(input: list[T]) -> T:  # noqa: UP047
    return input[0]


out = func([True, False])
print(out)


# Python has concept of alias for types

intOrStr = int | str


def fun1(input: intOrStr) -> intOrStr:
    if isinstance(input, int):
        return input + 2
    return input + "Ravi"


print(fun1(5))
print(fun1("Lukkani "))

# for generic type aliases
ListOrSet: TypeAlias = list[T] | set[T]  # noqa: UP040
