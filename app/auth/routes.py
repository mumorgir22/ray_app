from fastapi import APIRouter, Depends, status

from app.auth.schemas import (
    CreateUserSchema,
    JWTResponse,
    LoginUserSchema,
    RefreshTokenSchema,
)
from app.auth.services import AuthService

router = APIRouter()


@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=JWTResponse)
async def signup_user(payload: CreateUserSchema, service: AuthService = Depends(AuthService)) -> JWTResponse:
    return await service.create_user_services(payload=payload)


@router.post("/login", status_code=status.HTTP_200_OK, response_model=JWTResponse)
async def login_user(payload: LoginUserSchema, service: AuthService = Depends(AuthService)) -> JWTResponse:
    return await service.login_user_services(payload=payload)


@router.post("/refresh", status_code=status.HTTP_201_CREATED, response_model=JWTResponse)
def refresh_access_token(payload: RefreshTokenSchema, service: AuthService = Depends(AuthService)) -> JWTResponse:
    return service.refresh_access_token_services(payload=payload)
