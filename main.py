import httpx


async def send_data():
    with httpx.Client() as client:
        request = client.post(url, payload)
        content = request.content()
    return content