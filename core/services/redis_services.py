from typing import Any

from core.connection.redis_connection import redis_conn


async def redis_set(key: str, value: Any, expiration_time: int) -> None:
    await redis_conn.redis.set(key, value, ex=expiration_time)


async def redis_get(key: str) -> Any:
    return await redis_conn.redis.get(key)


async def redis_delete(key: str) -> None:
    await redis_conn.redis.delete(key)
