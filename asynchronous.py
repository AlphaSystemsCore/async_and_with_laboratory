import httpx

async def make_request():
    payload = {"message": "Hello"}
    url = "http://127.0.0.1:8002/receive-greeting"
    
    async with httpx.AsyncClient() as client:
        request = await client.post(url, payload)
        content = request.json()
        return content


print(await make_request())