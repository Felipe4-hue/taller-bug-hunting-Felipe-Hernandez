from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Taller Mecánico - Bug Hunting"
    DATABASE_URL: str = "sqlite+aiosqlite:///./taller_bugs.db"
    API_KEY_SECRETA: str = "SENA2026"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()