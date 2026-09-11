from typing import Any


class BasicDescriptor:
    name = ""

    def __set_name__(self, owner, name):
        print(f"received name: {name} from owner: {owner}")
        self.name = f"_{name}"

    def __get__(self, instance, owner) -> Any:
        print(f"getting this for instance {instance} and owner {owner}")
        if instance is None:
            return self
        return getattr(instance, self.name, None)

    # __set__ intercepts assignment. It does not automatically store the value.
    # We decide where to store it.
    def __set__(self, instance, value):
        print(f"setting value: {value} ")
        setattr(instance, self.name, value)


class AnyClass:
    var = BasicDescriptor()
    def __init__(self) -> None:
        print('ini called')


ins = AnyClass()

print(ins.var)
ins.var = 30

print(ins.__dict__)
