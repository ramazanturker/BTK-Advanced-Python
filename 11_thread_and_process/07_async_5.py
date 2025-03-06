import asyncio
import time

async def fetch_data(id, delay):
    print("receiving data... id: ", id)
    await asyncio.sleep(delay)
    print("data received... id: ", id)
    return {"id": id, "data": "some data"}

async def main():
    tasks = []

    for id, delay in enumerate([2, 1, 3], start=1):
        tasks.append(asyncio.create_task(fetch_data(id, delay)))

    await asyncio.gather(*tasks)

t = time.time()
asyncio.run(main())
print(time.time() - t)