import os
from dotenv import load_dotenv

load_dotenv()

UNSPLASH_ACCESS_KEY = "UNSPLASH_ACCESS_KEY"

def test_unsplash_access_key():
    """
    Test if the Unsplash access key is set in the environment variables.
    """
    assert os.getenv("UNSPLASH_ACCESS_KEY") is not None, "UNSPLASH_ACCESS_KEY environment variable not set"