import httpx


def send_data():
    payload = {"message": "Hello"}
    url = "https://m.kilimall.co.ke/search?q=computers&page=2&page=3&page=1&source=searchProduct|enterSearch|computers|home|searchProductResults"

    with httpx.Client() as client:
        request = client.get(url)
        content = request.content
    return content

content = send_data()
print(content)