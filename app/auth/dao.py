from sqlalchemy import exists, insert, select
from sqlalchemy.engine import Row

from core.services.db_service import BaseDAO
from db.models import User


class AuthServiceDAO(BaseDAO):
    async def check_users_exist(self, email: str | None, phone: str | None) -> bool:
        if email:
            query = exists(select(User.id).where(User.email == email)).select()
        else:
            query = exists(select(User.id).where(User.phone == phone)).select()
        result = await self._db.execute(query)
        return result.scalar_one()

    async def add_new_user(
        self, username: str, hashed_password: str, email: str | None, phone: str | None, city: str | None
    ) -> int:
        query = (
            insert(User)
            .values(
                username=username,
                hashed_password=hashed_password,
                email=email,
                phone=phone,
                city=city,
            )
            .returning(User.id)
        )
        result = await self._db.execute(query)
        return result.scalar_one()

    async def login_user(self, email: str | None, phone: str | None) -> Row | None:
        select_query = (
            select(
                User.id,
                User.hashed_password,
            )
            .select_from(User)
            .where(User.email == email, User.phone == phone)
        )
        result = await self._db.execute(select_query)
        return result.fetchone()
