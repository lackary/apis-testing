import requests
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient

app = FastAPI()

client = TestClient(app)

def test_fake_404():
    response = client.get("/not-found")
    assert response.status_code == 404

def test_server_bad_request(api_url, api_search, api_photos, api_headers):
    """
    Test if the API returns a 400 status code for a bad request.
    """
    # Simulate a bad request by providing an invalid parameter
    api= api_url + api_search + api_photos
    response = requests.get(api, headers=api_headers)
    assert response.status_code == 400

def test_server_unauthorized(api_url, api_photos, api_headers):
    """
    Test if the API returns a 401 status code when unauthorized access is attempted.
    """
    # Simulate unauthorized access by not providing the access key
    api = api_url + api_photos
    response = requests.get(api, api_headers)
    assert response.status_code == 401

def test_server_not_found(api_url, api_headers):
    """
    Test if the API returns a 404 status code for a non-existent endpoint.
    """
    api = api_url + "/not-found"
    response = requests.get(api, headers=api_headers)
    assert response.status_code == 404
