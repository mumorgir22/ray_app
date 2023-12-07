import requests

from tests.scripts.users.login import login
from tests.scripts.users.login import payload as login_payload
from tests.scripts.users.login import url as login_url


def delete_blog(api_url: str, headers: dict) -> dict | str:
    res = requests.delete(api_url, headers=headers)
    return "Blog deleted successfully" if res.status_code == 204 else res.json()


if __name__ == "__main__":
    blog_id = 72
    url = f"http://127.0.0.1:8000/blogs/{blog_id}"
    token = login(login_url, login_payload)
    headers = {"authorization": "Bearer " + token["access_token"]}
    response = delete_blog(url, headers)
    print(response)
