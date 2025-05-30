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
    instagram_username: Optional[str] = field(default=None)
    portfolio_url: Optional[str] = field(default=None)
    paypal_email: Optional[str] = field(default=None)
    twitter_username: Optional[str] = field(default=None)

dataclass
class UnsplashPhotoLinks:
    self: str
    html: str
    download: str
    download_location: str

@dataclass
class UnsplashCollectionLinks:
    self: str
    html: str
    photos: str
    related: str

@dataclass
class UnsplashUser:
    id: str
    updated_at: str
    username: str
    name: str
    first_name: str
    last_name: str
    links: UnsplashUserLinks
    profile_image: UnsplashUserProfileImage
    total_collections: int
    total_likes: int
    total_photos: int
    total_promoted_photos: int
    total_illustrations: int
    total_promoted_illustrations: int
    accepted_tos: bool
    for_hire: bool
    social: UnsplashSocial
    twitter_username: Optional[str] = field(default=None)
    portfolio_url: Optional[str] = field(default=None)
    bio: Optional[str] = field(default=None)
    location: Optional[str] = field(default=None)
    instagram_username: Optional[str] = field(default=None)

@dataclass
class UnsplashPrevewPhoto:
    id: str
    slug: str
    created_at: str
    updated_at: str
    blur_hash: str
    asset_type: str
    urls: UnsplashUrls

@dataclass
class UnsplashPhoto(UnsplashPrevewPhoto):
    # id: str
    # slug: str
    # created_at: str
    # updated_at: str
    width: int
    height: int
    # urls: UnsplashUrls
    links: UnsplashPhotoLinks
    color: str
    # blur_hash: str
    description: str
    alt_description: str
    likes: int
    liked_by_user: bool
    current_user_collections: list
    # asset_type: str
    user: UnsplashUser
    promoted_at: Optional[str] = field(default=None)
    sponsorship: Optional[str] = field(default=None)

@dataclass
class UnsplashCollection:
    id: str
    title: str
    description: str
    published_at: str
    last_collected_at: str
    updated_at: str
    featured: bool
    total_photos: int
    private: bool
    share_key: str
    links: UnsplashCollectionLinks
    user: UnsplashUser
    cover_photo: UnsplashPhoto
    preview_photos: Optional[list[UnsplashPrevewPhoto]] = field(default=list)