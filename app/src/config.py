from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    MONGO_SCHEMA: str = Field(default='mongodb')
    MONGO_PORT: int = Field(default=27017)
    MONGO_HOST: str = Field(default='localhost')

    CZ_TOML_PATH: str = Field(default='/cz.toml')


settings = Settings()
