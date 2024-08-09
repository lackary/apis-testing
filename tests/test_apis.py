import requests
from dataclasses import dataclass

from ..src.data.model.photo import Photo
from ..src.data.remote import *

base_url = "https://api.unsplash.com"



def test_get_photos_api():
    api = base_url + "/photos"
    unsplash_headers = {"Authorization": f"Client-ID {KEY}"}
    response = requests.get(api, headers=unsplash_headers)
    # json_str = response.json()
    # print(f"json_str type: {type(json_str)}") # list
    # # for item in json_str:
    # #     print(f"item {type(item)}") #dict
    # #     print(f"id: {item['id']}")
    # dataclass_fields = set(Photo.__annotations__.keys())
    # photos = [Photo(**{k: v for k, v in item.items() if k in dataclass_fields}) for item in json_str]
    # # # newline
    # # print(f"{json.dumps(json_str, indent=4)}")
    # for photo in photos:
    #     print(f"photo: {photo}")

    assert response.status_code == 200
