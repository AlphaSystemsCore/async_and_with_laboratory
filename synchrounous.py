import httpx
import time

def send_data():
    payload = {"message": "Hello"}
    url = "http://127.0.0.1:8002/receive-greeting"

    with httpx.Client() as client:
        request = client.post(url, json=payload)
        content = request.json()
    return content

time_in_async = 0.07565943199733738
start = time.perf_counter()
content = send_data()
print(content)
print(time.perf_counter() - start)
