import asyncio 

async def greet_asynchronous_funtion():
    # this is a coroutine function or asynchronous code
    print("Hello")


def greet_normal_function():
    # returns what is inside direct
    print("Hello")


asyncio.run(greet_asynchronous_funtion())
greet_normal_function()