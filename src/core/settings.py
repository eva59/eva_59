from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    telegram_token: SecretStr

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()  # type: ignore
