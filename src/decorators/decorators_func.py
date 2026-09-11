from collections.abc import Callable
from math import sqrt
from time import perf_counter
from typing import Any


def gen_func(my_func) -> Callable[..., Any]:
    def wrapper(*args, **kwargs):
        print("Before exec", args, kwargs)
        val = my_func(*args, **kwargs)
        print("after exec")
        return val

    return wrapper


@gen_func
def my_func(a: int, b: str, k="k"):
    print("my func", a, b, k)
    return True


my_func(5, "a", k="ravi")

a = 8

for element in range(2, int(sqrt(a)) + 1):
    if a % element == 0:
        print("not prime")
print("prime")

print(int(sqrt(a)))

############### Actual Example ###


def is_prime(number: int) -> bool:
    if number < 2:
        return True

    for element in range(2, int(sqrt(number)) + 1):
        if number % element == 0:
            return False
    return True


def beckmark(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args, **kwargs) -> Any:
        start_time = perf_counter()
        value = func(*args, *kwargs)
        end_time = perf_counter()
        print(
            f"Time taken: {end_time - start_time} and function name: {func.__name__} "
        )
        return value

    return wrapper


@beckmark
def count_prime_number(limit: int) -> int:
    count = 0
    for i in range(limit):
        if is_prime(i):
            count += 1

    return count


a = count_prime_number(1000)
print(a)
