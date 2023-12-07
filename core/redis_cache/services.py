from enum import Enum
from typing import Any

from core.redis_cache.enum import RedisExpiration
from core.redis_cache.keys import RedisKeys
from core.services.redis_services import redis_delete, redis_get, redis_set


class RedisCache:
    def __init__(self, enum_: Enum) -> None:
        self.enum_: Enum = enum_
        self.key = RedisKeys(self.enum_).tasks_key

    async def get_value(self) -> Any:
        return await redis_get(key=self.key)

    async def set_value(self, value: Any) -> None:
        await redis_set(self.key, value, getattr(RedisExpiration, self.enum_.name).value)

    async def del_value(self) -> None:
        await redis_delete(self.key)
