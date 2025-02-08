import asyncio


async def fetch_data(data: int) -> dict:
    print('fetching data...')
    await asyncio.sleep(2)
    return {'data': data}


async def counter():
    for i in range(10):
        await asyncio.sleep(0.5)
        print(i)


async def main():
    task1 = asyncio.create_task(fetch_data(123))
    task2 = asyncio.create_task(counter())

    data: dict = await task1
    print(data)
    await task2


asyncio.run(main())
