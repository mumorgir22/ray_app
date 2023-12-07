import requests


def get_users(api_url: str) -> dict:
    response = requests.get(api_url).json()
    return response if isinstance(response, dict) else {}


if __name__ == "__main__":
    url = "http://127.0.0.1:8000/users/"
    output_data = get_users(url)
    print(output_data)
