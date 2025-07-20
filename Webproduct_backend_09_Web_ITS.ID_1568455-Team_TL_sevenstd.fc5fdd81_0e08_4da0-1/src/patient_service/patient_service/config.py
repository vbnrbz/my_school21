from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    KAFKA_BOOTSTRAP_SERVERS: str = "localhost:9092"
    KAFKA_TOPIC: str = "patient_metrics"
    API_PREFIX: str = "/api/v1"
    DEBUG: bool = False
    METRICS_INTERVAL: int = 5
    PATIENT_UUID: str = "default_patient_id"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

settings = Settings()