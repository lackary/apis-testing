import requests
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient

app = FastAPI()

client = TestClient(app)

def test_fake_404():
    response = client.get("/not-found")
    assert response.status_code == 404

def test_api_not_found(api_url, api_headers):
    api = api_url + "/not-found"
    response = requests.get(api, headers=api_headers)
    assert response.status_code == 404

def test_api_unauthorized(api_url, api_photos, api_headers):
    # Simulate unauthorized access by not providing the access key
    response = requests.get(api_url + api_photos)
    assert response.status_code == 401

def test_get_photos_api(api_url, api_photos, api_headers):
    api = api_url + api_photos
    response = requests.get(api, headers=api_headers)
    assert response.status_code == 200

def test_get_photo(api_url, api_photos, api_headers):
    api = api_url + api_photos
    photo_id = "4ICax0QMs8U"
    response = requests.get(f"{api}/{photo_id}", headers=api_headers)
    assert response.status_code == 200

def test_get_collections_api(api_url, api_collections, api_headers):
    api = api_url + api_collections
    response = requests.get(api, headers=api_headers)
    assert response.status_code == 200
