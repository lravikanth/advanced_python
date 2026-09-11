#NOTE:dont hold on ref of a generator. This show pitfall of generators
#when exceptions happens. Resouces dont get released.

class Resource:
    def __init__(self, name) -> None:
        self.name = name

    def __enter__(self):
        self.connection = "Open"
        return self

    def __exit__(self, exc_type, exc, tb):
        print("Connection closed. Resource destroyed")


def gen():
    with Resource("DB_Info"):
        for i in range(5):
            try:
                yield i
            except BaseException as ex:
                print(type(ex))  # genExit exception is raised. since gen didnt
                # because of break
                raise  # re-raise same ex. So that clean up happens


# In Cpython if there are no references it get GC'ed


def call_gen() -> None:
    g = gen()  # here g is GC after the exit of main.
    # u can see resouce exited is called after the this loop and main exit.

    for i in g:
        print(i)
        if i == 3:
            break
    # after coming out for loop gen and resource are released
    # When gen goes out of scope GC collects Gen. The close method is called on Gen.
    # once gen is collected. resouce get freed up
    print("after loop")


call_gen()
