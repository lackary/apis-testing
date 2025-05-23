from dataclasses import dataclass, field
from typing import Optional

dataclass
class UnsplashAlternativeSlugs:
    en: Optional[str] = field(default=None)
    es: Optional[str] = field(default=None)
    ja: Optional[str] = field(default=None)
    fr: Optional[str] = field(default=None)
    it: Optional[str] = field(default=None)
    ko: Optional[str] = field(default=None)
    de: Optional[str] = field(default=None)
    pt: Optional[str] = field(default=None)

dataclass
class UnsplashUserLinks:
    self: str
    html: str
    photos: str
    likes: str
    portfolio: str

dataclass
class UnsplashUserProfileImage:
    small: str
    medium: str
    large: str

dataclass
class UnsplashUrls:
    raw: str
    full: str
    regular: str
    small: str
    thumb: str
    small_s3: str

dataclass
class UnsplashSocial:
    instagram_username: str
    portfolio_url: str
    twitter_username: str
    paypal_email: str

dataclass
class UnsplashPhotoLinks:
    self: str
    html: str
    download: str
    download_location: str
@dataclass
class UnsplashUser:
    id: str
    updated_at: str
    username: str
    name: str
    first_name: str
    last_name: str
    twitter_username: str
    portfolio_url: str
    bio: str
    location: str
    links: UnsplashUserLinks
    profile_image: UnsplashUserProfileImage
    instagram_username: str
    total_collections: int
    total_likes: int
    total_photos: int
    total_promoted_photos: int
    total_illustrations: int
    total_promoted_illustrations: int
    accepted_tos: bool
    for_hire: bool
    social: UnsplashSocial


@dataclass
class UnsplashPhoto:
    id: str
    slug: str
    created_at: str
    updated_at: str
    promoted_at: str
    width: int
    height: int
    urls: UnsplashUrls
    links: UnsplashPhotoLinks
    color: str
    blur_hash: str
    description: str
    alt_description: str
    likes: int
    liked_by_user: bool
    current_user_collections: list
    sponsorship: str
    asset_type: str
    user: UnsplashUser