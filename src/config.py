from pydantic_settings import BaseSettings, SettingsConfigDict

#connect our PostgreSQL
class Settings(BaseSettings):
    DATABASE_URL:str

    model_config=SettingsConfigDict(
        env_file =".env",
        extra="ignore"
    )


# object of our class
Config = Settings()