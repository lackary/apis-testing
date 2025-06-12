import requests
from src.utils.constant import API_PHOTOS, API_COLLECTIONS, API_USERS, API_SEARCH, API_TOPICS
from src.utils.constant import API_URL
from src.utils.constant import TEST_PHOTO_ID, TEST_COLLECTION_ID, TEST_USER_USERNAME, TEST_TOPIC_ID_OR_SLUG, TEST_SEARCH_QUERY

def test_get_photos_api(api_headers):
    api = API_URL + API_PHOTOS
    response = requests.get(api, headers=api_headers)
    assert response.status_code == 200

def test_get_photo_api(api_headers):
    api = API_URL + API_PHOTOS
    photo_id = TEST_PHOTO_ID
    response = requests.get(f"{api}/{photo_id}", headers=api_headers)
    assert response.status_code == 200

def test_get_collections_api(api_headers):
    api = API_URL + API_COLLECTIONS
    response = requests.get(api, headers=api_headers)
    assert response.status_code == 200

def test_get_collection_api(api_headers):
    api = API_URL + API_COLLECTIONS
    collection_id = TEST_COLLECTION_ID
    response = requests.get(f"{api}/{collection_id}", headers=api_headers)
    assert response.status_code == 200

def test_get_user_api(api_headers):
    api= API_URL + API_USERS
    username = TEST_USER_USERNAME
    response = requests.get(f"{api}/{username}", headers=api_headers)
    assert response.status_code == 200

def test_get_user_photos_api(api_headers):
    api= API_URL + API_USERS
    username = TEST_USER_USERNAME
    response = requests.get(f"{api}/{username}{API_PHOTOS}", headers=api_headers)
    assert response.status_code == 200

def test_get_user_collections_api(api_headers):
    api= API_URL + API_USERS
    username = TEST_USER_USERNAME
    response = requests.get(f"{api}/{username}{API_COLLECTIONS}", headers=api_headers)
    assert response.status_code == 200

def test_get_search_photos_api(api_headers):
    api = API_URL + API_SEARCH + API_PHOTOS
    query = TEST_SEARCH_QUERY
    response = requests.get(f"{api}", params={"query": query, "per_page": 5}, headers=api_headers)
    assert response.status_code == 200

def test_get_search_collections_api(api_headers):
    api = API_URL + API_SEARCH +API_COLLECTIONS
    query = TEST_SEARCH_QUERY
    response = requests.get(f"{api}", params={"query": query, "per_page": 5}, headers=api_headers)
    assert response.status_code == 200

def test_get_search_users_api(api_headers):
    api = API_URL + API_SEARCH + API_USERS
    query = TEST_SEARCH_QUERY
    response = requests.get(f"{api}", params={"query": query, "per_page": 5}, headers=api_headers)
    assert response.status_code == 200

def test_get_topics_api(api_headers):
    api = API_URL + API_TOPICS
    response = requests.get(api, headers=api_headers)
    assert response.status_code == 200

def test_get_topic_api(api_headers):
    api = API_URL + API_TOPICS
    topic_id_or_slug = TEST_TOPIC_ID_OR_SLUG
    response = requests.get(f"{api}/{topic_id_or_slug}", headers=api_headers)
    assert response.status_code == 200

def test_get_topic_photos_api(api_headers):
    api = API_URL + API_TOPICS
    topic_id_or_slug = TEST_TOPIC_ID_OR_SLUG
    response = requests.get(f"{api}/{topic_id_or_slug}{API_PHOTOS}", headers=api_headers)
    assert response.status_code == 200
