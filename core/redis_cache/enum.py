from enum import Enum


class RedisCacheKey(str, Enum):
    CITIES = "cities:weather"


class RedisExpiration(int, Enum):
    CITIES = 60 * 60 * 2  # 2 hours
