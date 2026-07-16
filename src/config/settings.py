from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "PriorAuthIQ"
    version: str = "0.1.0"

    model_config = {
        "env_file": ".env"
    }


settings = Settings()