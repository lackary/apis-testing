import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "BASE_URL"
UNSPLASH_ACCESS_KEY = "UNSPLASH_ACCESS_KEY"
API_PHOTOS = "API_PHOTOS"

def test_base_url():
    """
    Test if the base URL is set in the environment variables.
    """
    assert os.getenv("BASE_URL") is not None, "BASE_URL environment variable not set"

def test_unsplash_access_key():
    """
    Test if the Unsplash access key is set in the environment variables.
    """
    assert os.getenv("UNSPLASH_ACCESS_KEY") is not None, "UNSPLASH_ACCESS_KEY environment variable not set"

def test_api_photos():
    """
    Test if the API photos endpoint is set in the environment variables.
    """
    assert os.getenv("API_PHOTOS") is not None, "API_PHOTOS environment variable not set"
