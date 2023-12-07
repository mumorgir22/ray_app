import requests


def signup(api_url: str, payload: dict) -> dict:
    response = requests.post(api_url, json=payload).json()
    return response if isinstance(response, dict) else {}


if __name__ == "__main__":
    url = "http://127.0.0.1:8000/auth/signup/"
    payload = {"username": "test_user", "email": "test01@mail.com", "password": "pass", "city": "SPB"}
    output_data = signup(url, payload)
    print(output_data)
