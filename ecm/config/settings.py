from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    DB_URL: str

    JWT_KEY: str
    JWT_ALGORITHM: str


    ENVIRONMENT: str = 'dev'

    class Config:
        env_file = SettingsConfigDict(
            env_file='.env',
            env_file_encoding='utf-8'
        )
