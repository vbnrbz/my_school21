from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    BASE_DIR: Path = Path(__file__).parent.parent  # monitor_service/app -> monitor_service/
    DATA_SERVICE_DIR: Path = BASE_DIR.parent / "data_service"  # ../data_service
    DATABASE_URL: str = f"sqlite+aiosqlite:///{DATA_SERVICE_DIR / 'patients.db'}"
    HOST: str = "0.0.0.0"
    PORT: int = 8001

    class Config:
        env_file = ".env"

settings = Settings()
