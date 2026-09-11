import time


def timer(repeat=1):
    def decorator(fn):  # this is actual decorator
        def inner_wrapper(*args, **kwargs):
            for i in range(repeat):
                return_value = fn(*args, **kwargs)
            return return_value

        return inner_wrapper

    return decorator


@timer(repeat=5)
def my_func(max: int):
    total = 0
    time.sleep(1)
    for i in range(max):
        total = total + i * i
    print(total)
    return total


print(my_func(4))
