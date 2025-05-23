
import sys
import os
import requests
from ..model.unsplash_data import UnsplashPhoto
from ..constants import *
from .json_helper import *
from dotenv import load_dotenv

load_dotenv()
base_url = os.getenv("BASE_URL")
if base_url is None:
    print("BASE_URL environment variable not set")
    sys.exit(1)
access_key = os.getenv("UNSPLASH_ACCESS_KEY")
if access_key is None:
    print("UNSPLASH_ACCESS_KEY environment variable not set")
    sys.exit(1)
unsplash_headers = {"Authorization": f"Client-ID {access_key}"}

def get_photos(per_page = 10, headers = unsplash_headers):
    api = base_url + "/photos"
    query = f"?per_page={per_page}"
    response = requests.get(api+query, headers=headers)
    json_data = response.json()
    photos = parse_json(json_data, UnsplashPhoto)
    # dataclass_fields = set(Photo.__annotations__.keys())
    # photos = [Photo(**{k: v for k, v in item.items() if k in dataclass_fields}) for item in json_data]
    return photos

def get_photo(id: str, headers = unsplash_headers):
    api = base_url + "/photos"
    query = f"/{id}"
    response = requests.get(api+query, headers=unsplash_headers)
    json_data = response.json()

    photo = parse_json(json_data, UnsplashPhoto)
    # dataclass_fields = set(Photo.__annotations__.keys())
    # photo = Photo(**{k: v for k, v in json_data.items() if k in dataclass_fields})
    return photo