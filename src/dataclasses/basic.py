from dataclasses import dataclass, field

# dataclass generated 3 __ methods __init , __repr and __eq


@dataclass
class Point:
    x: int
    y: int
    l: list[int] = field(default_factory=list)


p1 = Point(3, 2, [2, 3])
p2 = Point(5, 7, [4, 5])
p3 = Point(3, 2, [7, 8])

print(p1, p2, p3)
print(p1 == p3)

# issue with default mutable class variables. They get shares across instances


class P1:
    l: list[int] = []

    def __init__(self, x: int, y: int, l: int) -> None:
        self.x = x
        self.y = y
        self.l.append(l)

    def add(self, k: int) -> None:
        self.l.append(k)


p1 = P1(2, 3, 7)
p2 = P1(4, 5, 8)

p1.add(19)
p2.add(25)

print(p1.l)
print(p2.l)


# list get appended with func calls.
def func(x: int, l: list[int] = []):
    l.append(x)
    print(l)


func(10)
func(12)


def func1(x: int) -> None:
    l: list[int] = []
    l.append(x)
    print(l)


func1(10)
func1(12)
