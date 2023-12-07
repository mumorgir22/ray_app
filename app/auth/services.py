from fastapi import Depends, HTTPException, status

from app.auth.dao import AuthServiceDAO
from app.auth.schemas import (
    CreateUserSchema,
    JWTResponse,
    LoginUserSchema,
    RefreshTokenSchema,
)
from core.auth_utils.auth import auth_utils


class AuthService:
    def __init__(self, auth_dao: AuthServiceDAO = Depends(AuthServiceDAO)) -> None:
        self._auth_dao = auth_dao

    async def create_user_services(self, payload: CreateUserSchema) -> JWTResponse:
        if await self._auth_dao.check_users_exist(email=payload.email, phone=payload.phone):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Account already exist")
        else:
            hashed_password = auth_utils.encode_password(password=payload.password)
            user_id = await self._auth_dao.add_new_user(
                username=payload.username,
                hashed_password=hashed_password,
                email=payload.email,
                phone=payload.phone,
                city=payload.city,
            )
            tokens = auth_utils.create_jwt_tokens(user_id=user_id)
            return JWTResponse(access_token=tokens.access_token, refresh_token=tokens.refresh_token)

    async def login_user_services(self, payload: LoginUserSchema) -> JWTResponse:
        user = await self._auth_dao.login_user(email=payload.email, phone=payload.phone)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Account dont exist or Incorrect Email",
            )
        if not auth_utils.verify_password(password=payload.password, encoded_password=user.hashed_password):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Incorrect Password")
        tokens = auth_utils.create_jwt_tokens(user_id=user.id)
        return JWTResponse(access_token=tokens.access_token, refresh_token=tokens.refresh_token)

    @staticmethod
    def refresh_access_token_services(payload: RefreshTokenSchema) -> JWTResponse:
        tokens = auth_utils.create_jwt_tokens(user_id=auth_utils.decode_refresh_token(token=payload.refresh_token))
        return JWTResponse(access_token=tokens.access_token, refresh_token=tokens.refresh_token)
