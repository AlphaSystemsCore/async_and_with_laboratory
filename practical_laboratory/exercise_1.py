# Prove that an async function returns a coroutine
async def calculate():
    return  100


results = calculate()
print(results)
