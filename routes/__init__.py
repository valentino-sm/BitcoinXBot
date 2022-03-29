from fastapi import APIRouter

from .telegram import router as telegram_router
# from .web import router as web_router
from utils import settings

router = APIRouter()

router.include_router(telegram_router, prefix=settings.prefix_tg)
# router.include_router(web_router)
