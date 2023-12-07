from pydantic import BaseModel


class PostgresSettings(BaseModel):
    user: str
    password: str
    host: str
    port: int
    db_name: str
    echo: bool
    autoflush: bool

    def sqlalchemy_database_url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"


class RedisSettings(BaseModel):
    host: str
    port: int

    def redis_url(self) -> str:
        return f"redis://{self.host}:{self.port}"


class WeatherApiSettings(BaseModel):
    api_key: str


class Settings(BaseModel):
    postgres: PostgresSettings
    redis: RedisSettings
    weather_api: WeatherApiSettings
