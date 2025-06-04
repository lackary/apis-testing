from dependency_injector import containers, providers
from src.data.remote.unsplash_api_client import UnsplashApiClient
from src.data.repository.unsplash_api_impl import UnsplashApiImpl

class AppContainer(containers.DeclarativeContainer):
    """
    Application container for dependency injection.
    This container is used to configure and provide dependencies for the application.
    """
    # You can also define configuration providers if needed
    config = providers.Configuration()

    # UnsplashApiClient provider
    unsplash_api_client = providers.Singleton(
        UnsplashApiClient,
        base_url=config.api_url,
        access_key=config.unsplash_access_key
    )

    unsplash_api = providers.Singleton(
        UnsplashApiImpl,
        client=providers.Callable(lambda client: client.get_client(), unsplash_api_client)
    )
    # Add more providers as needed
    # e.g., database connection, repositories, etc.