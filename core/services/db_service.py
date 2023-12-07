from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.connection.db_connection import get_session


class BaseDAO:
    def __init__(self, db: AsyncSession = Depends(get_session)) -> None:
        self._db = db
