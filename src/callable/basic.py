from collections.abc import Callable
from typing import Any

# callable syntax. Callable[[input parameters],return type]


def run_addition(fn: Callable[[int, int], int], a: int, b: int) -> int:
    c: int = fn(a, b)
    return c


def add(a: int, b: int) -> int:
    return a + b


print(run_addition(add, 5, 6))


def run(func: Callable[[int], None], a: int) -> None:
    func(a)


def print_int(a: int) -> None:
    print(f"printting {a}")


run(print_int, 5)

var = Callable[[Any], str]


def var_cast(data_type: var, a: int) -> str:
    print(f"got data type: {var} and value: {a}")
    r = data_type(a)
    print(type(r))
    return r


result = var_cast(str, 5)
print(result + "Ravi")


# callable factory pattern
min = Callable[[int], bool]


def validate_number(a: int) -> min:
    def min_check(value: int) -> bool:
        return value < a

    return min_check


check_voting = validate_number(21)
check_adult = validate_number(50)


class Person:
    def __init__(self, age: int) -> None:
        self.age = age

    def voting(self) -> bool:
        return check_voting(self.age)

    def adult(self) -> bool:
        return check_adult(self.age)


p = Person(30)

print(p.voting())
print(p.adult())
