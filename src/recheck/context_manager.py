from collections.abc import Iterator
from contextlib import contextmanager
from time import perf_counter, sleep


@contextmanager
def timer(a: str) -> Iterator[None]:
    start = perf_counter()
    try:
        yield
    finally:
        print(perf_counter() - start)


def some_fn():
    sleep(2)


with timer("ravi"):
    some_fn()
