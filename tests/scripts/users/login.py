import requests

url = "http://127.0.0.1:8000/auth/login/"
payload = {"email": "test@mail.com", "password": "pass"}


def login(api_url: str, payload: dict) -> dict:
    response = requests.post(api_url, json=payload).json()
    return response if isinstance(response, dict) else {}


if __name__ == "__main__":
    output_data = login(url, payload)
    print(output_data)
