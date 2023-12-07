from fastapi import Depends, HTTPException, status

from app.blogs.dao import BlogServiceDAO
from app.blogs.schemas import BlogCreateSchema, BlogSchemaResponse, BlogUpdateSchema


class BlogsService:
    def __init__(self, blog_dao: BlogServiceDAO = Depends(BlogServiceDAO)) -> None:
        self._blog_dao = blog_dao

    async def get_blogs_service(self, user_id: int) -> list[BlogSchemaResponse]:
        result = await self._blog_dao.get_user_blogs(user_id)
        return [
            BlogSchemaResponse(id=row.id, name=row.name, description=row.description, image=row.image) for row in result
        ]

    async def create_blog_services(self, blog_create: BlogCreateSchema, user_id: int) -> None:
        await self._blog_dao.add_blog(blog_create.name, blog_create.description, blog_create.image, user_id)

    async def update_blog_services(self, blog_id: int, blog_update: BlogUpdateSchema, user_id: int) -> None:
        await self._blog_dao.update_blog(blog_id, blog_update.dict(exclude_unset=True), user_id)

    async def delete_blog_services(self, blog_id: int, user_id: int) -> None:
        await self._blog_dao.delete_blog(blog_id, user_id)

    async def check_true_users_services(self, blog_id: int, user_id: int) -> None:
        if not await self._blog_dao.check_true_users(blog_id, user_id):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Error in request, please check if the path is correct",
            )
