from pydantic_settings import BaseSettings  # type: ignore

class Settings(BaseSettings):
  database_url: str = 'postgresql://postgres:admin@localhost/postgres'

  class Config:
    env_file = ".myapp"
    env_prefix = "myapp"

settings = Settings()
