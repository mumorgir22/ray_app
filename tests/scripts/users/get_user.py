import requests

from tests.scripts.users.login import login, payload, url


def get_user(api_url: str, headers: dict) -> dict:
    response = requests.get(api_url, headers=headers).json()
    return response if isinstance(response, dict) else {}


if __name__ == "__main__":
    url_get = "http://127.0.0.1:8000/users/user/"
    token = login(url, payload)
    headers = {"authorization": "Bearer " + token["access_token"]}
    user_data = get_user(url_get, headers)
    print(user_data)
