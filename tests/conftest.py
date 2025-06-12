import pytest
import pytest_asyncio
import os
from dotenv import load_dotenv
from src.di.app_container import AppContainer
from src.utils.constant import API_URL

load_dotenv()

pytest_plugins = ["pytest_asyncio"]
@pytest.fixture(scope="session")
def api_url():
    """
    Fixture to provide the base URL for the API.
    """
    api_url = os.getenv("API_URL")
    assert api_url is not None, "API_URL environment variable not set"
    return api_url

@pytest.fixture
def api_headers():
    """
    Fixture to provide the headers for the API requests.
    """
    access_key = os.getenv("UNSPLASH_ACCESS_KEY")
    assert access_key is not None, "UNSPLASH_ACCESS_KEY environment variable not set"
    return {
        "Authorization": f"Client-ID {access_key}"
    }

@pytest_asyncio.fixture(scope="function")
async def unsplash_api():
    """
    Fixture to provide an instance of the Unsplash API client.
    """
    api_url = API_URL
    unsplash_access_key = os.getenv("UNSPLASH_ACCESS_KEY")
    container = AppContainer()
    container.config.api_url.from_value(api_url)
    container.config.unsplash_access_key.from_value(unsplash_access_key)

    unsplash_api = container.unsplash_api()
    assert unsplash_api is not None, "Unsplash API client not initialized"
    yield unsplash_api
    # close client after all tests
    try:
        await unsplash_api._client.aclose()
    except RuntimeError as e:
        if "Event loop is closed" not in str(e):
            raise  # Ensure the client is closed after tests
