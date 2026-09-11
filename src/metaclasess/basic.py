# class is also an obj created by type class
def return_cls():
    class c1:
        x = 5

    return c1


a = return_cls()
b = a()
print(a.x)
print(type(a))
print(type(b))

# in () we can add parent clases
# to add methods. Def func and attach func to attrs


def f1(self):
    self.z = 200


c2 = type("c2", (), {"y": 20, "method1": f1})
ins_c2 = c2()
print(ins_c2.y)  # type: ignore
ins_c2.method1()  # type: ignore
print(ins_c2.z)  # type: ignore
