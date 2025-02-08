# Task is a key concept in asyncio for running multiple coroutines concurrently.
# task is a wrapper or coroutine, scheduled the coroutines to run the event loop, as soon as possiable.


import asyncio


async def fetch_data(data: int) -> dict:
    print('fetching data...')
    await asyncio.sleep(3)
    return {'data': data}


async def main():
    task = asyncio.create_task(fetch_data(100))

    # data: dict = await task

    # print(data)

   # cancle a task remove from schedule pool

    # task.cancel()

    # task.cancelled()  return boolean value for task is cancled or not

    # task.result()   get immediatley value when task is completed.
    # await asyncio.sleep(2) without this it will throw an error

    await asyncio.sleep(2)
    try:
        await asyncio.wait_for(task, timeout=5)
        #   more than 5 seconds it will trow timeout error
        if task.done():
            data: dict = task.result()
            print(data)
        else:
            print('no data')
    except asyncio.CancelledError:
        print('task was cancelled.')


asyncio.run(main())
