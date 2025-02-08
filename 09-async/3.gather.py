import asyncio


async def fetch_data(data: int) -> dict:

    print('fetching data...')
    await asyncio.sleep(3)
    if (data == 0):
        raise Exception('No data...')
    return {'data': data}


async def main():
    # all the things need to be resolve to be corrects
    tasks = asyncio.gather(fetch_data(1), fetch_data(10),
                           fetch_data(100), fetch_data(0), return_exceptions=True)
    results = await tasks
    print(results)


asyncio.run(main())
