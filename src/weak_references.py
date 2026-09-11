# Python uses ref counting for GC or obj deletion
# when there are no more references left. The obj del funcation is called.
# then when GC triggers.. memory gets cleared

import sys
import time
import weakref


class A:
    def __del__(self):
        print("obj A is getting deleted")


obj = A()
obj2 = obj

print(" Ref count obj: ", sys.getrefcount(obj))

obj = 1
# obj2 = 1

print(" Ref count obj: ", sys.getrefcount(obj2))
print(" Ref count obj: ", sys.getrefcount(obj))


obj_new = A()
obj_weak = weakref.ref(obj_new)
print(" Ref count obj_new: ", sys.getrefcount(obj_new))  # 2
# 2 bcoz calling getRef make a ref so the count is 2

# once strong ref is removed. del is called.
obj_new = 1
time.sleep(10)
