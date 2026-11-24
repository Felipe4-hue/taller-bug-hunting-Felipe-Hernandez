from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Taller"
    DATABASE_URL: str = "sqlite+aiosqlite:///./talle.db"
    API_KEY_SECRETA: str = "api-key"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()