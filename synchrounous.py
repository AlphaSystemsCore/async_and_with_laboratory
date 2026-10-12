import httpx


def send_data():
    payload = {"message": "Hello"}
    url = "http://127.0.0.1:8002/receive-greeting"

    with httpx.Client() as client:
        request = client.post(url, json=payload)
        content = request.json()
    return content

content = send_data()
print(content)