# instance varialbe is looked in the instance __dict__.
# if super is called. Then looks at parent instance __dict
# then looks at current class variable.
# then looks at parent class variable


class Parent:
    a = "Parent class Var"

    def __init__(self) -> None:
        self.v = "Patent A"


class Child(Parent):
    x = "Child class Var"

    def __init__(self):
        super().__init__()
        self.c = "Child Variable"


obj = Child()
print(obj.c)
print("inst varialbe: ", obj.a)
print(obj.a)


obj_par = Parent()
# print(obj_par.a)


#### SLOTS ####
# all the variable needs to be declared during defining class
# no __dict__ exists for class
# Mutability of variables is not effected. We can still update existing variables
# so.. not new variable can be added
# very memory efficient -- HUGE
# and slightly improved access speed


class Parent_S:
    a = "Parent class Var"

    def __init__(self) -> None:
        self.x = "Patent A"


class Child_S(Parent):
    __slots__ = ("a", "b")
    x = "Child Var"

    def __init__(self):
        super().__init__()
        self.a = "Ravi"
        # self.c = "Child Variable"


obj = Child_S()
print("Slots: ", obj.a)
# obj.c = "Lukkani" -- Cannot not add new varialbes to slots.
print("Slots: ", obj.a)
print("Slots: ", obj.x)
