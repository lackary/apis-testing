from abc import ABC, abstractmethod
from src.data.model.unsplash_data import UnsplashPhoto, UnsplashCollection, UnsplashUser, UnsplashSearch, UnsplashTopic

class UnsplashApi(ABC):

    @abstractmethod
    def get_photos(self, page: int = 1, per_page: int = 10) -> list[UnsplashPhoto]:
        """Fetch a list of photos."""
        pass

    @abstractmethod
    def get_photo(self, photo_id: str) -> UnsplashPhoto:
        """Fetch a single photo by its ID."""
        pass

    @abstractmethod
    def get_collections(self, page: int = 1, per_page: int = 10) -> list[UnsplashCollection]:
        """Fetch a list of collections."""
        pass

    @abstractmethod
    def get_collection(self, collection_id: str) -> UnsplashCollection:
        """Fetch a single collection by its ID."""
        pass

    @abstractmethod
    def get_collection_photos(self, collection_id: str, page: int = 1, per_page: int = 10) -> list[UnsplashPhoto]:
        """Fetch photos from a specific collection."""
        pass

    @abstractmethod
    def get_user(self, username: str) -> UnsplashUser:
        """Fetch user information by username."""
        pass

    @abstractmethod
    def get_user_photos(self, username: str, page: int = 1, per_page: int = 10) -> list[UnsplashPhoto]:
        """Fetch photos uploaded by a user."""
        pass

    @abstractmethod
    def get_user_collections(self, username: str, page: int = 1, per_page: int = 10) -> list[UnsplashCollection]:
        """Fetch collections created by a user."""
        pass

    @abstractmethod
    def get_topics(self, page: int = 1, per_page: int = 10) -> list[UnsplashTopic]:
        """Fetch a list of topics."""
        pass

    @abstractmethod
    def get_topic(self, topic_id_or_slug: str) -> UnsplashTopic:
        """Fetch a single topic by its ID."""
        pass

    @abstractmethod
    def get_topic_photos(self, topic_id_or_slug: str, page: int = 1, per_page: int = 10) -> list[UnsplashPhoto]:
        """Fetch photos related to a specific topic."""
        pass

    @abstractmethod
    def get_search(self, catagory: str, page: int = 1, per_page: int = 10) -> UnsplashSearch:
        """Search for photos based on a query."""
        pass
