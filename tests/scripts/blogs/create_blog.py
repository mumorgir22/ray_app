import requests

from tests.scripts.users.login import login
from tests.scripts.users.login import payload as login_payload
from tests.scripts.users.login import url as login_url


def create_blog(api_url: str, payload: dict, headers: dict) -> dict:
    response = requests.post(api_url, json=payload, headers=headers).json()
    return response if isinstance(response, dict) else {}


if __name__ == "__main__":
    url = "http://127.0.0.1:8000/blogs/"
    token = login(login_url, login_payload)
    headers = {"authorization": "Bearer " + token["access_token"]}
    payload = {"name": "blog_name", "description": "blog_description", "image": "blog_image"}
    output_data = create_blog(url, payload, headers)
    print(output_data)
