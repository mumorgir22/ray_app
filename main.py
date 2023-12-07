from fastapi import FastAPI

from app.routes import router
from core.connection.redis_connection import redis_conn
from core.services.schedulers_service import scheduler_service, schedulers_stop
from core.weather_api.services import weather_api

app = FastAPI()
services = [redis_conn]
pre_services = [weather_api]


@app.on_event("startup")
async def initialize_connections() -> None:
    for service in services:
        await service.connect()
    await scheduler_service()



@app.on_event("shutdown")
async def close_connection() -> None:
    for service in services:
        await service.disconnect()
    await schedulers_stop()


app.include_router(router)
