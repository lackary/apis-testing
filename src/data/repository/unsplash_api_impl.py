from httpx import AsyncClient
from src.domain.repository.unsplash_api_interface import UnsplashApi
from src.data.model.unsplash_data import UnsplashPhoto
from src.utils.decorators import handle_api_call_exceptions
from config import API_PHOTOS
from src.utils.json_helper import parse_json

class UnsplashApiImpl(UnsplashApi):

    def __init__(self, client: AsyncClient):
        self.client = client

    @handle_api_call_exceptions
    async def get_photos(self, page: int = 1, per_page: int = 10) -> list[UnsplashPhoto]:
        """Fetch a list of photos."""
        response = await self.client.get(API_PHOTOS, params={"page": page, "per_page": per_page})
        response.raise_for_status()
        json_data = response.json()
        photos = parse_json(json_data, UnsplashPhoto)
        return photos
