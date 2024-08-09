import sys
import requests
from dataclasses import dataclass
print(f"sys.path: {sys.path}")
from src.data.model.photo import Photo

base_url = "https://api.unsplash.com"


def get_photos():
    api = base_url + "/photos"
    query = "?per_page=5"
    unsplash_headers = {"Authorization": f"Client-ID {KEY}"}
    response = requests.get(api+query, headers=unsplash_headers)
    json_str = response.json()
    print(f"json_str type: {type(json_str)}") # list
    # for item in json_str:
    #     print(f"item {type(item)}") #dict
    #     print(f"id: {item['id']}")
    dataclass_fields = set(Photo.__annotations__.keys())
    photos = [Photo(**{k: v for k, v in item.items() if k in dataclass_fields}) for item in json_str]
    # # newline
    # print(f"{json.dumps(json_str, indent=4)}")
    for photo in photos:
        print(f"photo: {photo}")

def main(*args):
    test = "python3 test"
    print(f'{test}')
    get_photos()

if __name__ == "__main__":
    main(sys.argv)