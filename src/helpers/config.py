import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

def get_secret(name, default=None):
  
    secret_path = f"/run/secrets/{name}"
    
    if os.path.exists(secret_path):
        with open(secret_path, "r") as f:
            return f.read().strip()
    
    return os.getenv(name.upper(), default)

class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK: int
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_ROOT_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str


    model_config = SettingsConfigDict(
        secrets_dir="/run/secrets",
        env_file="../.env"
        )

@lru_cache # we use this for The Singleton Approach because without this python for each call well create new instance so this is bad practice
def getSetting():
    return Settings()