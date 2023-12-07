from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.config.settings import settings

Base = declarative_base()

async_engine = create_async_engine(settings.postgres.sqlalchemy_database_url(), isolation_level="AUTOCOMMIT")
async_session = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncGenerator:
    async with async_session() as session:
        yield session


def get_db() -> AsyncSession:
    return async_session()
