import asyncio

async def task(url):
    print(f"I'm working on it: {url}...")
    await asyncio.sleep(2)
    print(f"The task is done: {url}")
