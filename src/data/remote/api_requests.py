
import sys
import os
import requests
from src.data.model.unsplash_data import *
from src.data.remote.json_helper import *
from config import API_URL, UNSPLASH_ACCESS_KEY, API_PHOTOS

unsplash_headers = {"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"}

def get_photos(per_page = 10, headers = unsplash_headers):
    api = API_URL + API_PHOTOS
    query = f"?per_page={per_page}"
    response = requests.get(api+query, headers=headers)
    json_data = response.json()
    photos = parse_json(json_data, UnsplashPhoto)
    return photos

def get_photo(id: str, headers = unsplash_headers):
    api = API_URL + API_PHOTOS
    query = f"/{id}"
    response = requests.get(api+query, headers=headers)
    json_data = response.json()
    photo = parse_json(json_data, UnsplashPhoto)
    return photo