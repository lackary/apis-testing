import pytest
from unittest.mock import AsyncMock, MagicMock
from src.data.repository.unsplash_api_impl import UnsplashApiImpl

@pytest.fixture
def mock_client():
    client = MagicMock()
    client.get = AsyncMock()
    return client

@pytest.fixture
def fake_photo():
    return {"id": "1", "user": {"id": "u1"}}

@pytest.fixture
def fake_collection():
    return {"id": "c1"}

@pytest.fixture
def fake_user():
    return {"id": "u1"}

@pytest.fixture
def fake_topic():
    return {"id": "t1"}

@pytest.fixture
def fake_search():
    return {"results": [{"id": "1"}]}

@pytest.fixture(autouse=True)
def patch_parse_json(monkeypatch):
    # Always return the input data for parse_json
    monkeypatch.setattr("src.data.repository.unsplash_api_impl.parse_json", lambda data, cls: data)

@pytest.mark.asyncio
async def test_get_photos_success(mock_client, fake_photo):
    mock_response = MagicMock()
    mock_response.raise_for_status = MagicMock()
    mock_response.json.return_value = [fake_photo]
    mock_client.get.return_value = mock_response

    api = UnsplashApiImpl(mock_client)
    result = await api.get_photos()
    assert isinstance(result, list)
    assert result[0]["id"] == "1"

@pytest.mark.asyncio
async def test_get_photo_success(mock_client, fake_photo):
    mock_response = MagicMock()
    mock_response.raise_for_status = MagicMock()
    mock_response.json.return_value = fake_photo
    mock_client.get.return_value = mock_response

    api = UnsplashApiImpl(mock_client)
    result = await api.get_photo("1")
    assert result["id"] == "1"

@pytest.mark.asyncio
async def test_get_collections_success(mock_client, fake_collection):
    mock_response = MagicMock()
    mock_response.raise_for_status = MagicMock()
    mock_response.json.return_value = [fake_collection]
    mock_client.get.return_value = mock_response

    api = UnsplashApiImpl(mock_client)
    result = await api.get_collections()
    assert isinstance(result, list)
    assert result[0]["id"] == "c1"

@pytest.mark.asyncio
async def test_get_collection_success(mock_client, fake_collection):
    mock_response = MagicMock()
    mock_response.raise_for_status = MagicMock()
    mock_response.json.return_value = fake_collection
    mock_client.get.return_value = mock_response

    api = UnsplashApiImpl(mock_client)
    result = await api.get_collection("c1")
    assert result["id"] == "c1"

@pytest.mark.asyncio
async def test_get_collection_photos_success(mock_client, fake_photo):
    mock_response = MagicMock()
    mock_response.raise_for_status = MagicMock()
    mock_response.json.return_value = [fake_photo]
    mock_client.get.return_value = mock_response

    api = UnsplashApiImpl(mock_client)
    result = await api.get_collection_photos("c1")
    assert isinstance(result, list)
    assert result[0]["id"] == "1"

@pytest.mark.asyncio
async def test_get_user_success(mock_client, fake_user):
    mock_response = MagicMock()
    mock_response.raise_for_status = MagicMock()
    mock_response.json.return_value = fake_user
    mock_client.get.return_value = mock_response

    api = UnsplashApiImpl(mock_client)
    result = await api.get_user("u1")
    assert result["id"] == "u1"

@pytest.mark.asyncio
async def test_get_user_photos_success(mock_client, fake_photo):
    mock_response = MagicMock()
    mock_response.raise_for_status = MagicMock()
    mock_response.json.return_value = [fake_photo]
    mock_client.get.return_value = mock_response

    api = UnsplashApiImpl(mock_client)
    result = await api.get_user_photos("u1")
    assert isinstance(result, list)
    assert result[0]["id"] == "1"

@pytest.mark.asyncio
async def test_get_user_collections_success(mock_client, fake_collection):
    mock_response = MagicMock()
    mock_response.raise_for_status = MagicMock()
    mock_response.json.return_value = [fake_collection]
    mock_client.get.return_value = mock_response

    api = UnsplashApiImpl(mock_client)
    result = await api.get_user_collections("u1")
    assert isinstance(result, list)
    assert result[0]["id"] == "c1"

@pytest.mark.asyncio
async def test_get_topics_success(mock_client, fake_topic):
    mock_response = MagicMock()
    mock_response.raise_for_status = MagicMock()
    mock_response.json.return_value = [fake_topic]
    mock_client.get.return_value = mock_response

    api = UnsplashApiImpl(mock_client)
    result = await api.get_topics()
    assert isinstance(result, list)
    assert result[0]["id"] == "t1"

@pytest.mark.asyncio
async def test_get_topic_success(mock_client, fake_topic):
    mock_response = MagicMock()
    mock_response.raise_for_status = MagicMock()
    mock_response.json.return_value = fake_topic
    mock_client.get.return_value = mock_response

    api = UnsplashApiImpl(mock_client)
    result = await api.get_topic("t1")
    assert result["id"] == "t1"

@pytest.mark.asyncio
async def test_get_topic_photos_success(mock_client, fake_photo):
    mock_response = MagicMock()
    mock_response.raise_for_status = MagicMock()
    mock_response.json.return_value = [fake_photo]
    mock_client.get.return_value = mock_response

    api = UnsplashApiImpl(mock_client)
    result = await api.get_topic_photos("t1")
    assert isinstance(result, list)
    assert result[0]["id"] == "1"

@pytest.mark.asyncio
async def test_get_search_success(mock_client, fake_search):
    mock_response = MagicMock()
    mock_response.raise_for_status = MagicMock()
    mock_response.json.return_value = fake_search
    mock_client.get.return_value = mock_response

    api = UnsplashApiImpl(mock_client)
    result = await api.get_search("/photos", "cat")
    assert "results" in result
    assert result["results"][0]["id"] == "1"

@pytest.mark.asyncio
async def test_get_search_invalid_category(mock_client):
    api = UnsplashApiImpl(mock_client)
    result = await api.get_search("invalid", "cat")
    assert result is None