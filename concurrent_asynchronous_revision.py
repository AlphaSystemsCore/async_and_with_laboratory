import asyncio

async def task(url):
    print(f"I'm working on it: {url}...")
    await asyncio.sleep(2)
    print(f"The task is done: {url}")


async def main():
    await asyncio.gather(task("http://httl.com")
    ,task("http://sdjflkas.com"),
    task("http://malavida.com"))

asyncio.run(main())
