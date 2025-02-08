import asyncio


async def main():
    print('stared...')
    res = await asyncio.sleep(1, result={'item': 123})
    print(res)


asyncio.run(main())
