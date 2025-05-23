import os
import requests
from dotenv import load_dotenv

load_dotenv()
base_url = os.getenv("BASE_URL")

def test_get_photos_api(api_headers):
    api = base_url + "/photos"
    response = requests.get(api, headers=api_headers)
    assert response.status_code == 200

def test_get_photo(api_headers):
    api = base_url + "/photos"
    photo_id = "4ICax0QMs8U"
    response = requests.get(f"{api}/{photo_id}", headers=api_headers)
    assert response.status_code == 200
