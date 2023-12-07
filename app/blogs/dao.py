from sqlalchemy import exists, insert, select, update
from sqlalchemy.engine import Row

from core.services.db_service import BaseDAO
from db.models import Blog


class BlogServiceDAO(BaseDAO):
    async def get_user_blogs(self, user_id: int) -> list[Row]:
        query = (
            select(
                Blog.id,
                Blog.name,
                Blog.description,
                Blog.image,
            )
            .where(Blog.user_id == user_id, Blog.is_deleted.is_(False))
            .order_by(Blog.id)
        )
        result = await self._db.execute(query)
        return result.fetchall()

    async def add_blog(self, name: str, description: str | None, image: str | None, user_id: int) -> None:
        query = insert(Blog).values(name=name, description=description, image=image, user_id=user_id)
        await self._db.execute(query)

    async def update_blog(self, blog_id: int, values: dict, user_id: int) -> None:
        query = update(Blog).where(Blog.id == blog_id, Blog.user_id == user_id).values(**values)
        await self._db.execute(query)

    async def delete_blog(self, blog_id: int, user_id: int) -> None:
        query = update(Blog).where(Blog.id == blog_id, Blog.user_id == user_id).values(is_deleted=True)
        await self._db.execute(query)

    async def check_true_users(self, blog_id: int, user_id: int) -> bool:
        query = exists(select(Blog.id).where(Blog.id == blog_id, Blog.user_id == user_id)).select()
        result = await self._db.execute(query)
        return result.scalar_one()
