import collections.abc
import random
import time

import rich.progress
from rich.console import Console

c = Console()


def exp_op() -> float:
    time.sleep(0.2)
    return random.random()


def get_results(times: int) -> list[float]:
    result: list[float] = []
    for i in range(times):
        result.append(exp_op())
    return result


# generator


def gen_results(times: int) -> collections.abc.Iterator[float]:
    for i in range(times):
        yield exp_op()


for num in rich.progress.track(gen_results(25), console=c):
    c.print(f"{num:.2f}")
