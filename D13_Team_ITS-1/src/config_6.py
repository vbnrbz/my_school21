from pydantic_settings import BaseSettings, SettingsConfigDict

class Configuration(BaseSettings):
    login: str
    base_folder: str

    class Config:
        env_file: str = 'src/.env'
        extra: str = 'allow'

class SMTPSettings(BaseSettings):
    server: str
    port: int
    email: str
    email_password: str

    model_config = SettingsConfigDict(env_prefix='SMTP_', env_file='src/.env', extra='allow')
