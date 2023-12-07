import aiohttp
import orjson

from app.users.dao import UserServiceDAO
from core.config.settings import settings
from core.connection.db_connection import get_db
from core.redis_cache.enum import RedisCacheKey
from core.redis_cache.services import RedisCache


async def _city_url(city: str) -> str | None:
    api_key = settings.weather_api.api_key
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api_key}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            if data and resp.status == 200:
                weather_data = data[-1]
                lat = weather_data["lat"]
                lon = weather_data["lon"]
                weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
                return weather_url
            else:
                return None


async def _fetch_weather(city_url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(city_url) as resp:
            weather = await resp.json()
            temperature = round(weather["main"]["temp"] - 273.15, 2)
            wind_speed = weather["wind"]["speed"]
    return {"temperature": temperature, "wind_speed": wind_speed}


async def _cities_weather(cities: list) -> dict:
    results = {}
    for city in cities:
        city_url = await _city_url(city)
        if city_url and city is not None:
            result = await _fetch_weather(city_url)
            results[city] = result
    return results


async def weather_api() -> dict:
    user_service_dao = UserServiceDAO(db=get_db())
    redis_cache = RedisCache(enum_=RedisCacheKey.CITIES)
    cities = await user_service_dao.get_most_cities()
    cities = [row[0] for row in cities]
    result = await _cities_weather(cities)
    await redis_cache.set_value(orjson.dumps(result))
    return result
