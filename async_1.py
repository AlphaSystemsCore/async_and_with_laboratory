import asyncio

async def asynchronous_function():
    return 10

async def main():
    result = await asynchronous_function()
    print(result)

print(type(main))
asyncio.run(main())
