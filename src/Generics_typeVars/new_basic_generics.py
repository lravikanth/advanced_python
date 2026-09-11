#generics after 3.12

#non genric type alias
type IntOrStr = int | str

#Generic type alias

type ListOrSet[T] = list[T] | set[T]

def gen_fn[V](input: list[V]) -> V:
    return input[0]


print(gen_fn([2, 3, 4]))
print(gen_fn(['a','b','c']))
