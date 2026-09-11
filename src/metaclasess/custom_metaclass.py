from typing import Any


class Meta(type):
    # this is called even before __init__
    def __new__(self, name: str, bases, attrs):# -> Any:
        print(attrs)
        a ={}
        #lets change all attr names to caps. attr is a dict
        for name,val in attrs.items():
            if name.startswith("__"):
                a[name] = val
            else:
                a[name.upper()] = val
        #we need to pass new dict
        return type(name, bases, a)


class Person(metaclass=Meta):
    name = "Ravi"
    age = 48

    def walk(self):
        print(f"{self.NAME} is walking") # type: ignore


a = Person()
print(a.NAME, a.AGE) # type: ignore
a.WALK() # type: ignore
