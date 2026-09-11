class Stack[T]:
    def __init__(self, value: T) -> None:
        self.items: list[T] = [value]

    def push(self, v: T) -> None:
        self.items.append(v)

    def pop(self) -> T:
        return self.items.pop()


i = Stack(10)
i.push(100)
print(i.pop())
print(i.pop())

s = Stack("Ravi")
s.push("Saanvi")
print(s.pop())
print(s.pop())


def get_even[T](v: list[T]) -> list[T]:
    return [k for i, k in enumerate(v) if i % 2 == 0]


s = ["a", "b", "c", "d"]
i = [1, 2, 3, 4, 5, 6]

k = get_even(s)
j = get_even(i)

print(k, j)
