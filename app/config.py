from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    MODEL_NAME: str = "llama3:8b"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()