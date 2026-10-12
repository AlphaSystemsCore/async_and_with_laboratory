import httpx
import asyncio


async def make_request():
    payload = {"message": "Hello"}
    url = "http://127.0.0.1:8002/receive-greeting"

    async with httpx.AsyncClient() as client:
        request = await client.post(url, json=payload)
        content = request.json()
    return content

if __name__ == "__main__":
    content = asyncio.run(make_request)
    print(content)