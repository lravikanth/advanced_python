# 3 main caching decorators cache, cached_property and lru_cache
from functools import lru_cache


@lru_cache(maxsize=3)
def add_5(num):
    print("Adding five")
    return num + 5

print(add_5(10))
print(add_5(15))
print(add_5(20))
print(add_5(30))
print(add_5.cache_info())
print(add_5(15))
print(add_5(10))
print(add_5(15))
print(add_5(20))
