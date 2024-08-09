from dataclasses import dataclass

@dataclass
class Photo:
    id: str
    created_at: str
    updated_at: str
    width: int
    height: int