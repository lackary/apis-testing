from dataclasses import dataclass, field
from typing import Optional, Union, List

@dataclass
class UnsplashBaseLinks:
    self: str
    html: str

@dataclass
class UnsplashAlternativeSlugs:
    en: Optional[str] = None
    es: Optional[str] = None
    ja: Optional[str] = None
    fr: Optional[str] = None
    it: Optional[str] = None
    ko: Optional[str] = None
    de: Optional[str] = None
    pt: Optional[str] = None

@dataclass
class UnsplashUserLinks(UnsplashBaseLinks):
    photos: str
    likes: str
    portfolio: str

@dataclass
class UnsplashUserProfileImage:
    small: str
    medium: str
    large: str

@dataclass
class UnsplashUrls:
    raw: str
    full: str
    regular: str
    small: str
    thumb: str
    small_s3: Optional[str] = None

@dataclass
class UnsplashSocial:
    instagram_username: Optional[str] = None
    portfolio_url: Optional[str] = None
    paypal_email: Optional[str] = None
    twitter_username: Optional[str] = None

@dataclass
class UnsplashPhotoLinks(UnsplashBaseLinks):
    download: str
    download_location: str

@dataclass
class UnsplashCollectionLinks(UnsplashBaseLinks):
    photos: str
    related: Optional[str] = None

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
    twitter_username: Optional[str] = None
    portfolio_url: Optional[str] = None
    bio: Optional[str] = None
    location: Optional[str] = None
    instagram_username: Optional[str] = None

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
    width: int
    height: int
    links: UnsplashPhotoLinks
    color: str
    alt_description: str
    likes: int
    liked_by_user: bool
    current_user_collections: list
    user: UnsplashUser
    description: Optional[str] = None
    promoted_at: Optional[str] = None
    sponsorship: Optional[str] = None

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

@dataclass
class UnsplashSearch:
    total: int
    total_pages: int
    results: List[Union[UnsplashPhoto, UnsplashCollection, UnsplashUser]]

@dataclass
class UnsplashTopic:
    id: str
    slug: str
    title: str
    published_at: str
    updated_at: str
    visibility: str
    featured: bool
    total_photos: int
    links: UnsplashCollectionLinks = None
    description: Optional[str] = None
    starts_at: Optional[str] = None
    ends_at: Optional[str] = None
    only_submissions_after: Optional[str] = None
    current_user_contributions: list = field(default_factory=list)
    total_current_user_submissions: Optional[int] = None
    media_types: Optional[List[str]] = field(default_factory=list)
    status: Optional[str] = None
    owners: Optional[List[UnsplashUser]] = field(default_factory=list)
    cover_photo: Optional[UnsplashPhoto] = None
    preview_photos: Optional[List[UnsplashPrevewPhoto]] = field(default_factory=list)