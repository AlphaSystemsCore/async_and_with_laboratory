import asyncio

async def fetch_data():
    print("Starting request...")

    await asyncio.sleep(2)

    print("Request finished...")

    return {"message":"Hello"}

async def main():
    result = await fetch_data()
    print(result)

asyncio.run(main())