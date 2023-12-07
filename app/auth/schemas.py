from pydantic import BaseModel, EmailStr, validator

from core.utils.validators import validate_phone_number


class UserSchemaBase(BaseModel):
    password: str
    email: EmailStr | None
    phone: str | None

    @validator("phone")
    def verify_phone(cls, value: str) -> str:
        return validate_phone_number(value)


class CreateUserSchema(UserSchemaBase):
    username: str
    city: str | None


class LoginUserSchema(UserSchemaBase):
    pass


class JWTResponse(BaseModel):
    access_token: str
    refresh_token: str


class RefreshTokenSchema(BaseModel):
    refresh_token: str


class UsersSomeSchema(BaseModel):
    id: int
    username: str
    email: str
