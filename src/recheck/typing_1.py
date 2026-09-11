from typing import Final, Literal, NotRequired, TypedDict, final

mode = Literal[2, 3, 4]


def fn(a: mode):
    print(a)


fn(2)
fn(4)
fn(5)

# typed dict - Type hinting


class Cordinate(TypedDict):
    x: int
    y: int
    loc: str
    state: NotRequired[str]


c1: Cordinate = {"x": 5, "y": 3, "loc": "ATL"}
print(c1)
c2: Cordinate = {"x": 5, "y": 3}
print(c2)

# final and @final decorator
MAX: Final = 10
MAX = 20

print(MAX)


@final
class A:
    var1: Final = 200

    @final
    def fn(self) -> None:
        print("final method cannot be iherited")


class B(A):
    var1 = 400

    @classmethod
    def fn(cls) -> None:
        print("from child class cannot be inherited")

    @staticmethod
    def fn1(): ...


ca1 = B()
ca1.fn()
