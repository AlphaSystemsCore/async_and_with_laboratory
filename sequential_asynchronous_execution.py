import asyncio 

async def task(name):
    """using async does not automatically make a task concurrent"""
    print(f"{name} started ...")
    await asyncio.sleep(2)
    print(f"{name} completed...")


async def main():
    await task("A")
    await task("B")


asyncio.run(main())