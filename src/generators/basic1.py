# generator functions are the one that have yield stmt in them
# only calling next will call the generator function

from typing import Any


def get_values() -> Any:
    yield "Ravi"
    yield "kanth"
    yield 22
    yield True
    return 22


def caller() -> None:
    gen = get_values()
    # this prints generator obj funcation
    print(gen)
    # this gets first value
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    # we will get stopIteration exception. If no yield found
    # the exception will also have return value if returned as attr
    #print(next(gen))


caller()

#we use for loop in generator. Interally for loops calls next
#until stop iteration exception is found and handled

for i in get_values():
    print(i)
