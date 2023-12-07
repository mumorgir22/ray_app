from sqlalchemy import func, select
from sqlalchemy.engine import Row

from core.services.db_service import BaseDAO
from db.models import User


class UserServiceDAO(BaseDAO):
    async def get_users(self) -> list[Row]:
        query = select(User.id, User.username, User.hashed_password, User.email, User.phone, User.city).select_from(
            User
        )
        result = await self._db.execute(query)
        return result.fetchall()

    async def get_user(self, user_id: int) -> Row | None:
        query = select(User.username, User.email, User.phone, User.city).select_from(User).where(User.id == user_id)
        result = await self._db.execute(query)
        return result.fetchone()

    async def get_most_cities(self) -> list[Row]:
        query = select(User.city).select_from(User).group_by(User.city).order_by(func.count(User.city)).limit(20)
        result = await self._db.execute(query)
        return result.fetchall()
