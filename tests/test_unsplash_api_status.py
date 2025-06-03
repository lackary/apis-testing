import requests

def test_get_photos_api(api_url, api_photos, api_headers):
    api = api_url + api_photos
    response = requests.get(api, headers=api_headers)
    assert response.status_code == 200

def test_get_photo_api(api_url, api_photos, api_headers):
    api = api_url + api_photos
    photo_id = "4ICax0QMs8U"
    response = requests.get(f"{api}/{photo_id}", headers=api_headers)
    assert response.status_code == 200

def test_get_collections_api(api_url, api_collections, api_headers):
    api = api_url + api_collections
    response = requests.get(api, headers=api_headers)
    assert response.status_code == 200

def test_get_collection_api(api_url, api_collections, api_headers):
    api = api_url + api_collections
    collection_id = "26LduKzGz1Y"
    response = requests.get(f"{api}/{collection_id}", headers=api_headers)
    assert response.status_code == 200

def test_get_user_api(api_url, api_users, api_headers):
    api = api_url + api_users + "/pawel_czerwinski"
    response = requests.get(api, headers=api_headers)
    assert response.status_code == 200

def test_get_user_photos_api(api_url, api_users, api_photos, api_headers):
    api = api_url + api_users + "/pawel_czerwinski" + api_photos
    response = requests.get(api, headers=api_headers)
    assert response.status_code == 200

def test_get_user_collections_api(api_url, api_users, api_collections, api_headers):
    api = api_url + api_users + "/pawel_czerwinski" + api_collections
    response = requests.get(api, headers=api_headers)
    assert response.status_code == 200

def test_get_search_photos_api(api_url, api_search, api_photos, api_headers):
    api = api_url + api_search + api_photos
    query = "Taipei"
    response = requests.get(f"{api}", params={"query": query, "per_page": 5}, headers=api_headers)
    assert response.status_code == 200

def test_get_search_collections_api(api_url, api_search, api_collections, api_headers):
    api = api_url + api_search + api_collections
    query = "Taipei"
    response = requests.get(f"{api}", params={"query": query, "per_page": 5}, headers=api_headers)
    assert response.status_code == 200

def test_get_search_users_api(api_url, api_search, api_users, api_headers):
    api = api_url + api_search + api_users
    query = "Taipei"
    response = requests.get(f"{api}", params={"query": query, "per_page": 5}, headers=api_headers)
    assert response.status_code == 200

def test_get_topics_api(api_url, api_topics, api_headers):
    api = api_url + api_topics
    response = requests.get(api, headers=api_headers)
    assert response.status_code == 200

def test_get_topic_api(api_url, api_topics, api_headers):
    api = api_url + api_topics
    topic_id = "wallpapers"
    response = requests.get(f"{api}/{topic_id}", headers=api_headers)
    assert response.status_code == 200

def test_get_topic_photos_api(api_url, api_topics, api_headers):
    api = api_url + api_topics
    topic_id = "wallpapers"
    response = requests.get(f"{api}/{topic_id}/photos", headers=api_headers)
    assert response.status_code == 200
