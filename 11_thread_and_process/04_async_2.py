import asyncio

async def fetch_data(delay):
    print("receiving data...")
    await asyncio.sleep(delay)
    print("data received...")
    return {"data": "some data"}

async def main():
    print("start")
    task = fetch_data(2)
    print("end")
    
    result = await task
    print(f"received data: {result}")

asyncio.run(main())