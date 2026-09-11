import asyncio
from collections.abc import AsyncIterator

# async for is waiting for i in the list
# Ex: async for chunk in stream:
# generators remembers positions index
# insteads of pushing waits for customer to request data
# less memory consumption


def read_logs():
    lines = ["line 1", "line2", "line3"]
    for line in lines:
        print("sending line ", line)
        yield line


gen = read_logs()
for line in gen:
    print("recieved line ", line)

val = next(gen)


async def wait_return() -> AsyncIterator[int]:
    for i in range(10):
        await asyncio.sleep(1)
        yield i


async def async_for():
    total = 0
    async for i in wait_return():
        total = total + i
    return total


async def main():
    a = await async_for()
    print(a)


asyncio.run(main())
