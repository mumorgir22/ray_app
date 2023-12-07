from fastapi import APIRouter, Depends, status

from app.blogs.schemas import BlogCreateSchema, BlogSchemaResponse, BlogUpdateSchema
from app.blogs.services import BlogsService
from app.users.depends import get_user_id

router = APIRouter()
blog_service = BlogsService()


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_blogs_api(
    blog_create: BlogCreateSchema,
    user_id: int = Depends(get_user_id),
    service: BlogsService = Depends(BlogsService),
) -> BlogCreateSchema:
    await service.create_blog_services(blog_create=blog_create, user_id=user_id)
    return blog_create


@router.get("", status_code=status.HTTP_200_OK, response_model=list[BlogSchemaResponse])
async def get_blogs_api(
    user_id: int = Depends(get_user_id),
    service: BlogsService = Depends(BlogsService),
) -> list[BlogSchemaResponse]:
    return await service.get_blogs_service(user_id=user_id)


@router.patch("/{blog_id}", status_code=status.HTTP_200_OK)
async def update_blogs_api(
    blog_id: int,
    blog_update: BlogUpdateSchema,
    user_id: int = Depends(get_user_id),
    service: BlogsService = Depends(BlogsService),
) -> BlogUpdateSchema:
    await service.check_true_users_services(blog_id, user_id)
    await service.update_blog_services(blog_id, blog_update, user_id)
    return blog_update


@router.delete("/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog_api(
    blog_id: int,
    user_id: int = Depends(get_user_id),
    service: BlogsService = Depends(BlogsService),
) -> None:
    await service.check_true_users_services(blog_id, user_id)
    await service.delete_blog_services(blog_id, user_id)
