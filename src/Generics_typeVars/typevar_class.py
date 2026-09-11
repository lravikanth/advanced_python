from typing import Generic, TypeVar

T = TypeVar("T", bound=int | str)  # we can also specify bound


class Contrainer(Generic[T]):  # noqa: UP046
    def __init__(self, item: T) -> None:
        self.item = item

    def get_item(self) -> T:
        return self.item


int_con = Contrainer(20)
str_con = Contrainer("Ravi")
# this wont complain bcoz bool is a sub class of int
bool_con = Contrainer(True)
# this will complain by pylance.. but will execute
# float_con = Contrainer(3.14)
print(int_con.get_item())
print(str_con.get_item())
print(bool_con.get_item())
# print(float_con.get_item())
