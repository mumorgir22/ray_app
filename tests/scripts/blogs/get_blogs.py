import requests

from tests.scripts.users.login import login, payload, url


def get_blogs(api_url: str, headers: dict) -> list:
    response = requests.get(api_url, headers=headers).json()
    return response if isinstance(response, list) else []


if __name__ == "__main__":
    url_get = "http://127.0.0.1:8000/blogs/"
    token = login(url, payload)
    headers = {"authorization": "Bearer " + token["access_token"]}
    blogs = get_blogs(url_get, headers)
    print(blogs)
