import orjson
from fastapi import Depends, HTTPException, status

from app.users.dao import UserServiceDAO
from app.users.schemas import UserSchema, UserSchemaResponse, UsersSchemaResponse, WeatherSchema
from core.redis_cache.enum import RedisCacheKey
from core.redis_cache.services import RedisCache


class UserService:
    def __init__(self, user_dao: UserServiceDAO = Depends(UserServiceDAO)) -> None:
        self._user_dao = user_dao

    async def get_users_service(self) -> UsersSchemaResponse:
        items = await self._user_dao.get_users()
        result = UsersSchemaResponse(
            items=[
                UserSchema(
                    id=row.id,
                    username=row.username,
                    hashed_password=row.hashed_password,
                    email=row.email,
                    phone=row.phone,
                    city=row.city,
                )
                for row in items
            ]
        )

        return result

    async def get_user_service(self, user_id: int) -> UserSchemaResponse:
        user_data = await self._user_dao.get_user(user_id)
        if user_data:
            username, email, phone, city = user_data
            if city:
                redis_cache = RedisCache(enum_=RedisCacheKey.CITIES)
                weather_data = await redis_cache.get_value()
                weather_dict = orjson.loads(weather_data)
                city_weather = weather_dict[city]
                weather = WeatherSchema(temperature=city_weather["temperature"], wind_speed=city_weather["wind_speed"])
            else:
                weather = None
            return UserSchemaResponse(username=username, email=email, phone=phone, city=city, weather=weather)
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User don't exists",
            )
