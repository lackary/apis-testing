from abc import ABC, abstractmethod
from src.data.model.unsplash_data import UnsplashPhoto, UnsplashCollection, UnsplashUser, UnsplashSearch, UnsplashTopic

class UnsplashApi(ABC):

    @abstractmethod
    def get_photos(self, page: int = 1, per_page: int = 10) -> list[UnsplashPhoto]:
        """Fetch a list of photos."""
        pass
