import sys
import requests
import json
from src.data.model.photo import Photo
from src.data.constants import *

print(f"sys.path: {sys.path}")

def get_photos():
    api = base_url + "/photos"
    query = "?per_page=5"
    unsplash_headers = {"Authorization": f"Client-ID {KEY}"}
    response = requests.get(api+query, headers=unsplash_headers)
    json_str = response.json()
    dataclass_fields = set(Photo.__annotations__.keys())
    photos = [Photo(**{k: v for k, v in item.items() if k in dataclass_fields}) for item in json_str]

    for photo in photos:
        print(f"photo: {photo}")

def get_photo(id: str):
    api = base_url + "/photos"
    print("")
    query = f"/{id}"
    unsplash_headers = {"Authorization": f"Client-ID {KEY}"}
    response = requests.get(api+query, headers=unsplash_headers)
    json_data = response.json()
    print(f"json_data type: {type(json_data)}")
    print(f"json_data: {json_data}")
    print(f"{json.dumps(json_data, indent=4)}")
    dataclass_fields = set(Photo.__annotations__.keys())
    photo = Photo(**{k: v for k, v in json_data.items() if k in dataclass_fields})
    return photo

def main(*args):
    test = "python3 test"
    print(f'{test}')
    # get_photos()
    # photo = get_photo(id="SCfDL1HxuEs")
    # print(f"photo: {photo}")
    json_str = '{"name": "John Doe", "age": 30, "city": "New York"}'
    person_data = json.loads(json_str)
    print(f"person_data type: {type(person_data)}")
    json_str_array = """
                    [
                    {"name": "John Doe", "age": 30, "city": "New York"},
                    {"name": "Jane Smith", "age": 25, "extra_key": "value"}
                    ]
                    """
    json_data = json.loads(json_str_array)
    print(f"json_data type: {type(json_data)}")


if __name__ == "__main__":
    main(sys.argv)