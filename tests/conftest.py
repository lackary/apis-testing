import pytest
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    """
    Fixture to provide the base URL for the API.
    """
    base_url = os.getenv("BASE_URL")
    print(f"base_url: {base_url}")
    assert base_url is not None, "BASE_URL environment variable not set"
    return base_url

@pytest.fixture(scope="session")
def api_photos():
    """
    Fixture to provide the API endpoint for photos.
    """
    api_photos = os.getenv("API_PHOTOS")
    print(f"api_photos: {api_photos}")
    assert api_photos is not None, "API_PHOTOS environment variable not set"
    return api_photos

@pytest.fixture
def api_headers():
    """
    Fixture to provide the headers for the API requests.
    """
    access_key = os.getenv("UNSPLASH_ACCESS_KEY")
    print(f"access_key: {access_key}")
    assert access_key is not None, "UNSPLASH_ACCESS_KEY environment variable not set"
    return {
        "Authorization": f"Client-ID {access_key}"
    }
