from fastapi import APIRouter

from .telegram import router as telegram_router
# from .web import router as web_router

import models
from utils import settings, database

router = APIRouter()

router.include_router(telegram_router, prefix=settings.prefix_tg)
# router.include_router(web_router)


@router.on_event("startup")
async def on_startup():
    await database.db_init()


@router.on_event("shutdown")
async def on_shutdown():
    await database.db_close()
