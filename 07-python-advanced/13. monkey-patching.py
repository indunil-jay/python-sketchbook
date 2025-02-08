import requests  # type: ignore


def get(url: str):
    return '<TEST_RESPONSE>'


# monkey patch, or override
requests.get = get

data = requests.get('https://www.apple.com')
print(data)
