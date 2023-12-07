from pydantic import BaseModel


class WeatherSchema(BaseModel):
    temperature: str
    wind_speed: str


class UserSchema(BaseModel):
    id: int
    username: str
    hashed_password: str
    email: str | None
    phone: str | None
    city: str | None


class UsersSchemaResponse(BaseModel):
    items: list[UserSchema]


class UserSchemaResponse(BaseModel):
    username: str
    email: str | None
    phone: str | None
    city: str | None
    weather: WeatherSchema | None
