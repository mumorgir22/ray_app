from apscheduler.schedulers.asyncio import AsyncIOScheduler

from core.weather_api.services import weather_api

scheduler = AsyncIOScheduler()

services = [weather_api]


async def scheduler_service() -> None:
    for service in services:
        scheduler.add_job(service, "interval", seconds=60)  # 1 min for tests
    scheduler.start()


async def schedulers_stop() -> None:
    scheduler.remove_all_jobs()
