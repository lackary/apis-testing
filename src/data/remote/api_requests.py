import sys
import os
import requests
from src.data.model.unsplash_data import *
from src.utils.json_helper import *
from src.utils.constant import API_URL, API_PHOTOS, API_COLLECTIONS, API_USERS, API_SEARCH, API_TOPICS
from config import UNSPLASH_ACCESS_KEY

unsplash_headers = {
    "Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}",
    "Accept-Version": "v1",
    "Content-Type": "application/json"
}

SEARCH_MAP = {
    API_PHOTOS: API_PHOTOS,
    API_COLLECTIONS: API_COLLECTIONS,
    API_USERS: API_USERS
}

def safe_api_call(func):
    """
    Decorator to handle API call exceptions.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.exceptions.RequestException as e:
            print(f"API call failed: {e}", file=sys.stderr)
        except ValueError as e:
            print(f"JSON parsing error: {e}", file=sys.stderr)
        except TypeError as e:
            print(f"Type error: {e}", file=sys.stderr)
        except Exception as e:
            print(f"An unexpected error occurred: {e}", file=sys.stderr)
        finally:
            # Optionally, you can log the error or take other actions
            print("API call completed with errors.", file=sys.stderr)
        return None
    return wrapper

@safe_api_call
def get_photos(per_page = 10, headers = unsplash_headers):
    api = API_URL + API_PHOTOS
    query = f"?per_page={per_page}"
    response = requests.get(api+query, headers=headers)
    json_data = response.json()
    photos = parse_json(json_data, UnsplashPhoto)
    return photos

@safe_api_call
def get_photo(id: str, headers = unsplash_headers):
    api = API_URL + API_PHOTOS
    query = f"/{id}"
    response = requests.get(api+query, headers=headers)
    json_data = response.json()
    photo = parse_json(json_data, UnsplashPhoto)
    return photo

@safe_api_call
def get_collections(per_page = 10, headers = unsplash_headers):
    api = API_URL + API_COLLECTIONS
    query = f"?per_page={per_page}"
    response = requests.get(api+query, headers=headers)
    json_data = response.json()
    collections = parse_json(json_data, UnsplashCollection)
    return collections

@safe_api_call
def get_collection(id: str, headers = unsplash_headers):
    api = API_URL + API_COLLECTIONS
    query = f"/{id}"
    response = requests.get(api+query, headers=headers)
    json_data = response.json()
    collection = parse_json(json_data, UnsplashCollection)
    return collection

def get_user(username: str, headers = unsplash_headers):
    """
    Get user information by username.
    """
    api = API_URL + API_USERS
    query = f"/{username}"
    response = requests.get(api+query, headers=headers)
    json_data = response.json()
    user = parse_json(json_data, UnsplashUser)
    return user

def get_user_photos(username: str, per_page = 10, headers = unsplash_headers):
    """
    Get photos uploaded by a user.
    """
    api = API_URL + API_USERS
    query = f"/{username}{API_PHOTOS}?per_page={per_page}"
    response = requests.get(api+query, headers=headers)
    json_data = response.json()
    photos = parse_json(json_data, UnsplashPhoto)
    return photos

def get_user_collections(username: str, per_page = 10, headers = unsplash_headers):
    """
    Get collections created by a user.
    """
    api = API_URL + API_USERS
    query = f"/{username}{API_COLLECTIONS}?per_page={per_page}"
    response = requests.get(api+query, headers=headers)
    json_data = response.json()
    collections = parse_json(json_data, UnsplashCollection)
    return collections

@safe_api_call
def get_search(category: str, query: str, per_page = 10, headers = unsplash_headers):
    if category not in SEARCH_MAP:
        raise ValueError("Unknown category")
    api = API_URL + API_SEARCH + category
    query_params = f"?query={query}&per_page={per_page}"
    response = requests.get(api+query_params, headers=headers)
    json_data = response.json()
    search_data = parse_json(json_data, UnsplashSearch)
    return search_data.results

@safe_api_call
def get_topics(per_page = 10, headers = unsplash_headers):
    """
    Get topics from the Unsplash API.
    """
    api = API_URL + API_TOPICS
    query = f"?per_page={per_page}"
    response = requests.get(api+query, headers=headers)
    json_data = response.json()
    topics = parse_json(json_data, UnsplashTopic)
    return topics

@safe_api_call
def get_topic(id_or_slug: str, headers = unsplash_headers):
    """
    Get a specific topic by its ID.
    """
    api = API_URL + API_TOPICS
    query = f"/{id_or_slug}"
    response = requests.get(api+query, headers=headers)
    json_data = response.json()
    topic = parse_json(json_data, UnsplashTopic)
    return topic


@safe_api_call
def get_topic_photos(id_or_slug: str, per_page = 10, headers = unsplash_headers):
    """
    Get photos for a specific topic.
    """
    api = API_URL + API_TOPICS
    query = f"/{id_or_slug}{API_PHOTOS}?per_page={per_page}"
    response = requests.get(api+query, headers=headers)
    json_data = response.json()
    photos = parse_json(json_data, UnsplashPhoto)
    return photos