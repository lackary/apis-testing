
import sys
import os
import requests
from src.data.model.unsplash_data import *
from src.data.remote.json_helper import *
from config import API_URL, UNSPLASH_ACCESS_KEY, API_PHOTOS, API_COLLECTIONS, API_SEARCH

unsplash_headers = {
    "Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}",
    "Accept-Version": "v1",
    "Content-Type": "application/json"
}

SEARCH_MAP = {
    API_PHOTOS: API_PHOTOS,
    API_COLLECTIONS: API_COLLECTIONS,
}

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

def get_collections(per_page = 10, headers = unsplash_headers):
    api = API_URL + API_COLLECTIONS
    query = f"?per_page={per_page}"
    response = requests.get(api+query, headers=headers)
    json_data = response.json()
    collections = parse_json(json_data, UnsplashCollection)
    return collections

def get_collection(id: str, headers = unsplash_headers):
    api = API_URL + API_COLLECTIONS
    query = f"/{id}"
    response = requests.get(api+query, headers=headers)
    json_data = response.json()
    collection = parse_json(json_data, UnsplashCollection)
    return collection

def get_search(category: str, query: str, per_page = 10, headers = unsplash_headers):
    if category not in SEARCH_MAP:
        raise ValueError("Unknown category")
    api = API_URL + API_SEARCH + category
    query_params = f"?query={query}&per_page={per_page}"
    response = requests.get(api+query_params, headers=headers)
    json_data = response.json()
    search_data = parse_json(json_data, UnsplashSearch)
    return search_data.results
