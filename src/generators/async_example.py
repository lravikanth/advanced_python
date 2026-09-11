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

#async
async def main():
    t1 = perf_counter()
    l1: list[str] = []
    for _ in range(20):
        result = await get_poke()
        l1.append(result[0])
    t2 = perf_counter()
    #print(l1)
    print(f"Time elapsed for async await imediately: {t2 - t1}")

    t1 = perf_counter()
    l1: list[str] = []
    # * unpack list to indivual items. In this case individual calls.
    l1 = await asyncio.gather(*[get_poke() for _ in range(20)])
    t2 = perf_counter()
    #print(l1)
    print(f"Time elapsed for async await with gather: {t2 - t1}")


asyncio.run(main())


