from typing import Protocol, runtime_checkable


@runtime_checkable
class Writable(Protocol):
    def write(self, aj: str) -> None: ...


def any_method(c: Writable, a: str):
    c.write(a)


class Buffer:
    def __init__(self) -> None:
        pass

    def write(self, aj: str) -> None:
        print(aj)


any_method(Buffer(), "Ravi Lukkani")

# instance check
in1 = Buffer()
print(isinstance(in1, Writable))
