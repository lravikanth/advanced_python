class DemoDescriptor:
    def __get__(self, instance, owner):
        print(f"__get__ called with instance {instance} and owner {owner.__name__}")
        return 45

    def __set__(self, instance, value):
        print(f"__set__ called with instance {instance} and value {value}")


class Thing:
    x = DemoDescriptor()


t = Thing()
print(t.x)


###property decorator


class Empoyee:
    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last
        # self.email = first + "." + last + "@gmail.com"

    def full_name(self):
        return self.first + " " + self.last

    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, a):
        return a


emp = Empoyee("Ravi", "Lukkani")

print(emp.first)
print(emp.email)
emp.email = "a@a.com"
print(emp.email)
print(emp.full_name())
