import os
from pathlib import Path
from dotenv import load_dotenv

# Step 1: 取得 APP_ENV
app_env = os.getenv("APP_ENV", "dev")  # 預設 dev

# Step 2: 載入對應 .env 檔
env_path = Path(f"env/.env.{app_env}")
load_dotenv(dotenv_path=env_path)

# Step 3: 提供設定
APP_ENV = os.getenv("APP_ENV")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
API_URL = os.getenv("API_URL")
UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")
API_PHOTOS = os.getenv("API_PHOTOS")
API_COLLECTIONS = os.getenv("API_COLLECTIONS")
API_USERS = os.getenv("API_USERS")
API_SEARCH = os.getenv("API_SEARCH")
API_HEADERS = {
    "Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}",
    "Accept-Version": "v1",
    "Content-Type": "application/json"
}
