import asyncio
import time

async def fetch_data(id, delay):
    print("receiving data... id: ", id)
    await asyncio.sleep(delay)
    print("data received... id: ", id)
    return {"id": id, "data": "some data"}

async def main():
    results = await asyncio.gather(fetch_data(1, 2), fetch_data(2, 3), fetch_data(3, 1))

    for result in results:
        print(result)

t = time.time()
asyncio.run(main())
print(time.time() - t)