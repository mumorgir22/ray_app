from fastapi import APIRouter, Depends

from app.users.depends import get_user_id
from app.users.schemas import UserSchemaResponse, UsersSchemaResponse
from app.users.services import UserService

router = APIRouter()


@router.get("", response_model=UsersSchemaResponse)
async def get_all_users_api(service: UserService = Depends(UserService)) -> UsersSchemaResponse:
    return await service.get_users_service()


@router.get("/user", response_model=UserSchemaResponse)
async def get_user_api(
    user_id: int = Depends(get_user_id), service: UserService = Depends(UserService)
) -> UserSchemaResponse:
    return await service.get_user_service(user_id)
