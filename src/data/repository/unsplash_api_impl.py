from httpx import AsyncClient
from src.domain.repository.unsplash_api_interface import UnsplashApi
from src.data.model.unsplash_data import UnsplashPhoto, UnsplashCollection, UnsplashUser, UnsplashTopic, UnsplashSearch
from src.utils.decorators import handle_api_call_exceptions
from config import API_PHOTOS, API_COLLECTIONS, API_USERS, API_SEARCH, API_TOPICS
from src.utils.json_helper import parse_json
import logging

logger = logging.getLogger(__name__)

class UnsplashApiImpl(UnsplashApi):
    SEARCH_MAP = {
        API_PHOTOS: API_PHOTOS,
        API_COLLECTIONS: API_COLLECTIONS,
        API_USERS: API_USERS
    }

    def __init__(self, client: AsyncClient):
        self._client = client

    @handle_api_call_exceptions
    async def get_photos(self, page: int = 1, per_page: int = 10) -> list[UnsplashPhoto]:
        """Fetch a list of photos."""
        response = await self._client.get(API_PHOTOS, params={"page": page, "per_page": per_page})
        response.raise_for_status()
        json_data = response.json()
        photos = parse_json(json_data, UnsplashPhoto)
        return photos

    @handle_api_call_exceptions
    async def get_photo(self, photo_id: str) -> UnsplashPhoto:
        """Fetch a single photo by its ID."""
        response = await self._client.get(f"{API_PHOTOS}/{photo_id}")
        response.raise_for_status()
        json_data = response.json()
        photo = parse_json(json_data, UnsplashPhoto)
        return photo

    @handle_api_call_exceptions
    async def get_collections(self, page = 1, per_page = 10):
        """Fetch a list of collections."""
        response = await self._client.get(API_COLLECTIONS, params={"page": page, "per_page": per_page})
        response.raise_for_status()
        json_data = response.json()
        collections = parse_json(json_data, UnsplashCollection)
        return collections

    @handle_api_call_exceptions
    async def get_collection(self, collection_id: str) -> UnsplashCollection:
        """Fetch a single collection by its ID."""
        response = await self._client.get(f"{API_COLLECTIONS}/{collection_id}")
        response.raise_for_status()
        json_data = response.json()
        collection = parse_json(json_data, UnsplashCollection)
        return collection

    @handle_api_call_exceptions
    async def get_collection_photos(self, collection_id: str, page: int = 1, per_page: int = 10) -> list[UnsplashPhoto]:
        """Fetch photos from a specific collection."""
        response = await self._client.get(f"{API_COLLECTIONS}/{collection_id}{API_PHOTOS}", params={"page": page, "per_page": per_page})
        response.raise_for_status()
        json_data = response.json()
        photos = parse_json(json_data, UnsplashPhoto)
        return photos

    @handle_api_call_exceptions
    async def get_user(self, username: str) -> UnsplashUser:
        """Fetch user information by username."""
        response = await self._client.get(f"{API_USERS}/{username}")
        response.raise_for_status()
        json_data = response.json()
        user = parse_json(json_data, UnsplashUser)
        return user

    @handle_api_call_exceptions
    async def get_user_photos(self, username: str, page: int = 1, per_page: int = 10) -> list[UnsplashPhoto]:
        """Fetch photos uploaded by a user."""
        response = await self._client.get(f"{API_USERS}/{username}{API_PHOTOS}", params={"page": page, "per_page": per_page})
        response.raise_for_status()
        json_data = response.json()
        photos = parse_json(json_data, UnsplashPhoto)
        return photos

    @handle_api_call_exceptions
    async def get_user_collections(self, username: str, page: int = 1, per_page: int = 10) -> list[UnsplashCollection]:
        """Fetch collections created by a user."""
        response = await self._client.get(f"{API_USERS}/{username}{API_COLLECTIONS}", params={"page": page, "per_page": per_page})
        response.raise_for_status()
        json_data = response.json()
        collections = parse_json(json_data, UnsplashCollection)
        return collections

    @handle_api_call_exceptions
    async def get_topics(self, page: int = 1, per_page: int = 10) -> list[UnsplashTopic]:
        """Fetch a list of topics."""
        response = await self._client.get(API_TOPICS, params={"page": page, "per_page": per_page})
        response.raise_for_status()
        json_data = response.json()
        topics = parse_json(json_data, UnsplashTopic)
        return topics

    @handle_api_call_exceptions
    async def get_topic(self, topic_id_or_slug: str) -> UnsplashTopic:
        """Fetch a single topic by its ID."""
        response = await self._client.get(f"{API_TOPICS}/{topic_id_or_slug}")
        response.raise_for_status()
        json_data = response.json()
        topic = parse_json(json_data, UnsplashTopic)
        return topic

    @handle_api_call_exceptions
    async def get_topic_photos(self, topic_id_or_slug: str, page: int = 1, per_page: int = 10) -> list[UnsplashPhoto]:
        """Fetch photos related to a specific topic."""
        response = await self._client.get(f"{API_TOPICS}/{topic_id_or_slug}{API_PHOTOS}", params={"page": page, "per_page": per_page})
        response.raise_for_status()
        json_data = response.json()
        photos = parse_json(json_data, UnsplashPhoto)
        return photos

    @handle_api_call_exceptions
    async def get_search(self, category: str, query: str, page: int = 1, per_page: int = 10) -> UnsplashSearch:
        """Search for photos based on a query."""
        if category not in self.SEARCH_MAP:
            raise ValueError("Unknown category")
        response = await self._client.get(f"{API_SEARCH}/{category}", params={"query": query, "page": page, "per_page": per_page})
        response.raise_for_status()
        json_data = response.json()
        search_data = parse_json(json_data, UnsplashSearch)
        return search_data