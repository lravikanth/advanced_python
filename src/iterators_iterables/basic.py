# iterables - Its some thing looped over
# it will have __iter__ method
# No next method
# loop thru multiple times
# ierator: Has a state where it know where it is in iteration and knows to get next item
# can only loop thru once. Once it hit stopInteration exception.

# Generators are also iterators where next and iter method are impl automatically
from dataclasses import dataclass
from typing import Iterable

list1 = [2, 3, 4]
for i in list1:
    print(i)
for i in list1:
    print("2ed time: ", i)

print(dir(list1))

# run __iter on iterable to get an iterator

it = list1.__iter__()
# instead of calling dunder method we can call iter method to get iterator
# we should them by passing to iter method
it1 = iter(list1)
# now next mehtod can be found
print(next(it1))
print(next(it1))
print(next(it1))
# print(next(it1))  # stop iteration exception

for i in it1:
    print(i)

for i in list1:
    print(i)


@dataclass(frozen=True)
class Item:
    i: int


def fn(a: Iterable[Item]) -> int:
    total = 0
    for r in a:
        total = r.i + total
    return total


a = {Item(1), Item(2)}

print(fn(a))
