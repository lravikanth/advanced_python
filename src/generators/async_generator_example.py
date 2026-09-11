import asyncio
from random import randint
from time import perf_counter

from req_http import http_get, http_get_sync

MAX = 898
URL = "https://pokeapi.co/api/v2/pokemon/"


def get_poke_sync() -> str:
    id = randint(1, MAX)
    url = URL + str(id)
    poke = http_get_sync(url)
    return str(poke["name"])


# print(get_poke_sync())


async def get_poke() -> str:
    id = randint(1, MAX)
    url = URL + str(id)
    poke = await http_get(url)
    return str(poke["name"])


# async with generator
async def next_poke(total: int):
    for _ in range(total):
        yield await get_poke()

async def next_poke_gather(total: int):
    for _ in range(total):
        yield await get_poke()


# async
async def main():
    t1 = perf_counter()
    async for name in next_poke(20):
        print(name[0])
    t2 = perf_counter()
    # print(l1)
    # running on
    print(f"Time elapsed for async genrator one after the other: {t2 - t1}")

    # We can use list comp also to call async generators
    t1 = perf_counter()
    result = [name async for i in next_poke(20)]
    print(*result)
    t2 = perf_counter()
    # print(l1)
    print(
        f"Time elapsed for async genrator with list comp one after the other: {t2 - t1}"
    )


asyncio.run(main())
