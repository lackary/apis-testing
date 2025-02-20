
import sys
import requests
from ..model.unsplash_data import UnsplashPhoto
from ..constants import *
from .json_helper import *

unsplash_headers = {"Authorization": f"Client-ID {KEY}"}

def get_photos(per_page = 10):
    api = base_url + "/photos"
    query = f"?per_page={per_page}"
    response = requests.get(api+query, headers=unsplash_headers)
    json_data = response.json()
    photos = parse_json(json_data, UnsplashPhoto)
    # dataclass_fields = set(Photo.__annotations__.keys())
    # photos = [Photo(**{k: v for k, v in item.items() if k in dataclass_fields}) for item in json_data]
    return photos

def get_photo(id: str):
    api = base_url + "/photos"
    query = f"/{id}"
    response = requests.get(api+query, headers=unsplash_headers)
    json_data = response.json()

    photo = parse_json(json_data, UnsplashPhoto)
    # dataclass_fields = set(Photo.__annotations__.keys())
    # photo = Photo(**{k: v for k, v in json_data.items() if k in dataclass_fields})
    return photo