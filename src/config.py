from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = 'ThematicAPI'
    APP_VERSION: str = '1.0'
    APP_HOST: str = '0.0.0.0'
    APP_PORT: int = 8000
    OPENAPI_URL: str = '/openapi.json'
    DOCS_URL: str = '/docs'
    ELASTIC_HOST: str = 'elasticsearch'
    ELASTIC_PORT: int = 9200

    @property
    def elastic_uri(self) -> str:
        return f'http://{self.ELASTIC_HOST}:{self.ELASTIC_PORT}'


settings = Settings()
