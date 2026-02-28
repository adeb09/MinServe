from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment or .env file."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    port: int = Field(default=8080, description="Server port")
    backend_url: str = Field(
        default="http://localhost:8001",
        description="Backend Server URL",
    )


# Singleton instance; import this to access settings
settings = Settings()
