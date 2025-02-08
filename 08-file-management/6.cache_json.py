import json
import requests


def fetch_data(*, update: bool = False, json_cache: str, url: str) -> dict:
    if update:
        json_data = None
    else:
        try:
            with open(json_cache, 'r') as file:
                json_data = json.load(file)
                print('fetched data from the local cache!')
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f'no local cache found ({e})')
            json_data = None

    if not json_data:
        print('fetching new json data...(create local cache)')
        json_data = requests.get(url).json()
        with open(json_cache, 'w') as file:
            json.dump(json_data, file)

    return json_data


api_url: str = 'https://dummyjson.com/comments'
cache_file: str = '08-file-management/comments.json'
data: dict = fetch_data(update=False, json_cache=cache_file, url=api_url)
print(data)
