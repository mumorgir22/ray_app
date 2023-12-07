import redis.asyncio as aioredis

from core.config.settings import settings
from core.connection.base_connection import BaseConnection


class RedisConnection(BaseConnection):
    def __init__(self) -> None:
        self.redis_url = settings.redis.redis_url()

    async def connect(self) -> None:
        self.redis = await aioredis.from_url(self.redis_url, decode_responses=True)

    async def disconnect(self) -> None:
        await self.redis.close()


redis_conn = RedisConnection()
