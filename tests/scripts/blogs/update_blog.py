import requests

from tests.scripts.users.login import login
from tests.scripts.users.login import payload as login_payload
from tests.scripts.users.login import url as login_url

payload = {"name": "some_update", "description": None, "image": "other image"}


def update_blog(api_url: str, payload: dict, headers: dict) -> str:
    res = requests.patch(api_url, json=payload, headers=headers).json()
    return res


if __name__ == "__main__":
    blog_id = 72
    url = f"http://127.0.0.1:8000/blogs/{blog_id}"
    token = login(login_url, login_payload)
    headers = {"authorization": "Bearer " + token["access_token"]}
    response = update_blog(url, payload, headers)
    print(response)
