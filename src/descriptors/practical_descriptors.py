from collections.abc import Callable
from typing import Any

validator = Callable[[str, Any], None]


def non_empty(field: str, value: Any) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} must be a non empty")


def min_value(n: int) -> validator:
    def _v(field: str, value: Any) -> None:
        if value < n:
            raise ValueError(f"{field} must be greater then {n}")

    return _v


class ValidatedField[T]:
    def __init__(
        self, cast: Callable[[Any], T], validators: tuple[validator, ...] = ()
    ) -> None:
        self.cast = cast
        self.validators = validators
        self.name = ""
        self.storage_name = ""

    def __set_name__(self, owner, name) -> None:
        self.name = name
        self.storage_name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.storage_name, None)

    def __set__(self, instance, value):

        casted = self.cast(value)
        for v in self.validators:
            v(self.name, casted)
        setattr(instance, self.storage_name, casted)


class Customer:
    name: ValidatedField[str] = ValidatedField(cast=str, validators=(non_empty,))
    age: ValidatedField[int] = ValidatedField(cast=int, validators=(min_value(18),))

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


c = Customer("RAvi", 48)
c1 = Customer("RAvi", 8)
print(c.__dict__)
print(c.name, c.age)
