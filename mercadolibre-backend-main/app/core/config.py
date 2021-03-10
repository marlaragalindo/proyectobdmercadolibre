from pydantic import AnyUrl, BaseSettings


class Settings(BaseSettings):
    app_name: str = "My App"
    database_url: AnyUrl

    class Config:
        env_file = ".env"


settings = Settings()
