from pydantic import BaseSettings

# Environment settings using pydantic
class Settings(BaseSettings):
    db_url: str  # Database connection URL

    class Config:
        env_file = ".env"

# Load settings
settings = Settings()
