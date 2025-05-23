import pytest
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def api_headers():
    access_key = os.getenv("UNSPLASH_ACCESS_KEY")
    print(f"access_key: {access_key}")
    assert access_key is not None, "UNSPLASH_ACCESS_KEY environment variable not set"
    return {
        "Authorization": f"Client-ID {access_key}"
    }