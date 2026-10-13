# Prove that an async function returns a coroutine
async def calculate():
    print(100)

import asyncio
results = asyncio.run(calculate())


# 1. Why did'nt result contain 100?
# this is because its a coroutine and contains an asynchronous computable and waitable task

# 2. What did calculate return ?
# a coroutine object

# 3. How would you obtain the value of 100 correctly?
# By running the corroutine object in the event loop or in asyncio.run()

# 3.Why might asyncio.run() be appropriate in a standalone script but not inside an already-running FastAPI event loop?
# this is because the corroutine will be handle automatically by the event loop

