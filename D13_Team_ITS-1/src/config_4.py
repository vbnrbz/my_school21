from pydantic_settings import BaseSettings


class Configuration(BaseSettings):
    login: str
    base_folder: str

    class Config:
        env_file: str = 'src/.env'
        extra: str = 'allow'
