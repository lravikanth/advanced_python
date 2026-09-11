from typing import Any


class GenerateFunction:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("before calling", args, kwds)
        val = self.func(*args, **kwds)
        print("after exec")
        return val


@GenerateFunction
def my_func(a: int, b: str, k="k"):
    print("my func", a, b, k)
    return True


print(my_func(6, "a", k="Lukkani"))
