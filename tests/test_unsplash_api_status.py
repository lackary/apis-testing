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
