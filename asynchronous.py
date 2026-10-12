import httpx
import asyncio
import time


async def make_request():
    payload = {"message": "Hello"}
    url = "http://127.0.0.1:8002/receive-greeting"

    async with httpx.AsyncClient() as client:
        # client.post returns a response
        response = await client.post(url, json=payload)
        content = response.json()
    return content

if __name__ == "__main__":
    # use asyncio.run(awaitable) to run the coroutine
    start = time.perf_counter()
    content = asyncio.run(make_request())
    print(content)
    print(time.perf_counter() - start)