from dataclasses import dataclass

@dataclass
class UnsplashUser:
    id: str
    updated_at: str
    username: str
    name: str
    first_name: str
    last_name: str
    location: str

@dataclass
class UnsplashPhoto:
    id: str
    created_at: str
    updated_at: str
    width: int
    height: int
    likes: int
    color: str
    user: UnsplashUser