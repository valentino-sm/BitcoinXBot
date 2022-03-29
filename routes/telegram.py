import asyncio
import random
from json import JSONDecodeError
from typing import List

from fastapi import APIRouter, BackgroundTasks, Depends, Request, Response, status, HTTPException
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode, Update

from telegram import filters, middlewares, handlers
from telegram.utils import commands
from utils import settings, i18n

router = APIRouter()
bot = Bot(settings.bot_token, parse_mode=ParseMode.HTML, validate_token=True)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@router.on_event("startup")
async def on_startup():
    middlewares.setup(dp, i18n)
    filters.setup(dp)
    handlers.errors.setup(dp)
    handlers.user.setup(dp)
    await commands.register(bot)
    await bot.delete_webhook()
    await bot.set_webhook(settings.webhook_url)


@router.on_event("shutdown")
async def on_shutdown():
    await storage.close()
    await storage.wait_closed()
    await bot.close()


async def verify_token(token: str):
    if token != settings.bot_token:
        await asyncio.sleep(random.random())  # Additional protection from bruteforce
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


async def proceed_update(updates: List[Update]) -> None:
    Bot.set_current(bot)
    Dispatcher.set_current(dp)
    await dp.process_updates(updates)


@router.post(settings.prefix_webhook + "/{token}", dependencies=[Depends(verify_token)], include_in_schema=False)
async def execute(req: Request, background_tasks: BackgroundTasks) -> Response:
    try:
        updates = [Update(**(await req.json()))]
    except JSONDecodeError:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    background_tasks.add_task(proceed_update, updates)
    return Response(status_code=status.HTTP_200_OK)
