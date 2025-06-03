from src.data.remote.api_requests import *
from config import API_COLLECTIONS, API_PHOTOS, API_USERS

def test_get_photos():
    photos = get_photos(per_page=5)
    assert len(photos) == 5

def test_get_photo():
    photo = get_photo(id="4ICax0QMs8U")
    assert photo.id == "4ICax0QMs8U"

def test_get_collections():
    collections = get_collections(per_page=5)

    assert len(collections) == 5
def test_get_collection():
    collection = get_collection(id="26LduKzGz1Y")
    assert collection.id == "26LduKzGz1Y"
    assert collection.title is not None
    assert isinstance(collection.user, UnsplashUser)

def test_get_user():
    user = get_user(username="pawel_czerwinski")
    assert user.username == "pawel_czerwinski"
    assert user.name is not None
    assert user.bio is not None

def test_get_user_photos():
    user_photos = get_user_photos(username="pawel_czerwinski", per_page=5)
    assert len(user_photos) == 5
    for photo in user_photos:
        assert isinstance(photo, UnsplashPhoto)
        assert photo.id is not None
        assert isinstance(photo.user, UnsplashUser)

def test_get_user_collections():
    user_collections = get_user_collections(username="pawel_czerwinski", per_page=5)
    assert len(user_collections) == 5
    for collection in user_collections:
        assert isinstance(collection, UnsplashCollection)
        assert collection.id is not None
        assert isinstance(collection.user, UnsplashUser)
        assert isinstance(collection.cover_photo, UnsplashPhoto) if collection.cover_photo else True

def test_get_search_photos():
    search_results = get_search(category=API_PHOTOS, query="Taipei", per_page=5)
    assert len(search_results) == 5
    for photo in search_results:
        assert isinstance(photo, UnsplashPhoto)
        assert photo.id is not None
        assert isinstance(photo.user, UnsplashUser)

def test_get_search_collections():
    search_results = get_search(category=API_COLLECTIONS, query="Taipei", per_page=5)
    assert len(search_results) == 5
    for collection in search_results:
        assert isinstance(collection, UnsplashCollection)
        assert collection.id is not None
        assert isinstance(collection.user, UnsplashUser)
        assert isinstance(collection.cover_photo, UnsplashPhoto) if collection.cover_photo else True

def test_get_search_users():
    search_results = get_search(category=API_USERS, query="Taipei", per_page=5)
    assert len(search_results) == 5
    for user in search_results:
        assert isinstance(user, UnsplashUser)
        assert user.username is not None
        assert user.name is not None

def test_get_topics():
    topics = get_topics(per_page=5)
    assert len(topics) == 5
    for topic in topics:
        assert isinstance(topic, UnsplashTopic)
        assert topic.id is not None
        assert topic.slug is not None
        assert topic.title is not None
        assert topic.visibility in ["visible", "featured"]

def test_get_topic():
    topic = get_topic(id_or_slug="wallpapers")
    assert topic.id is not None
    assert topic.slug == "wallpapers"
    assert topic.title is not None
    assert topic.visibility in ["visible", "featured"]

def test_get_topic_photos():
    topic_photos = get_topic_photos(id_or_slug="wallpapers", per_page=5)
    assert len(topic_photos) == 5
    for photo in topic_photos:
        assert isinstance(photo, UnsplashPhoto)
        assert photo.id is not None
        assert isinstance(photo.user, UnsplashUser)
