from src.data.remote.api_requests import *

def test_get_photos():
    photos = get_photos(per_page=5)
    assert len(photos) == 5

def test_get_photo():
    photo = get_photo(id="4ICax0QMs8U")
    assert photo.id == "4ICax0QMs8U"