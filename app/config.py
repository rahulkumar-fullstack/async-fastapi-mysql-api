from pydantic_settings import BaseSettings
from pydantic import ConfigDict

# Environment settings using pydantic
class Settings(BaseSettings):
    db_url: str  # Database connection URL

    model_config = ConfigDict(env_file=".env")

# Load settings
settings = Settings()

#print(settings.db_url)
