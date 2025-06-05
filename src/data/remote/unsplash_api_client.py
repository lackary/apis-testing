from httpx import AsyncClient

class UnsplashApiClient:
    """
    Client for interacting with the Unsplash API.
    This class is responsible for making HTTP requests to the Unsplash API endpoints.
    """

    def __init__(self, base_url: str, access_key: str):
        self.base_url = base_url
        self.access_key = access_key
        self._client = AsyncClient(
            base_url=self.base_url,
            headers={
                "Authorization": f"Client-ID {self.access_key}"
                }
            )

    def get_client(self) -> AsyncClient:
        """Returns the configured HTTP client."""
        return self._client

    async def close(self):
        """Close the HTTP client connection."""
        await self._client.aclose()