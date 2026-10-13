import asyncio
import httpx

async def main(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

        print(response.status_code)
        print(response.json())

async def caller():
    await asyncio.gather(
        main("https://httpbin.org/get"),
        main("https://httpbin.org/get"),
        main("https://httpbin.org/get")
    )

asyncio.run(caller())
