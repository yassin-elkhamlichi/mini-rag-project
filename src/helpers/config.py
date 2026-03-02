from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK: int

    model_config = SettingsConfigDict(env_file="../.env")

@lru_cache # we use this for The Singleton Approach because without this python for each call well create new instance so this is bad practice
def getSetting():
    return Settings()