import asyncio
import random
from json import JSONDecodeError

from fastapi import APIRouter, BackgroundTasks, Depends, Request, Response, status, HTTPException
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode, Update
from loguru import logger

from components import AccountTelegram
from components.account import account_ctx
from telegram import filters, middlewares, handlers
from telegram.utils import commands
from utils import settings, i18n, ssl

router = APIRouter()
bot = Bot(settings.bot_token, parse_mode=ParseMode.HTML, validate_token=True)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@router.on_event("startup")
async def on_startup():
    middlewares.setup(dp, i18n)
    filters.setup(dp)
    handlers.register_errors_handler(dp)
    handlers.register_handlers_common(dp)
    await commands.register(bot)
    if (await bot.get_webhook_info()).url != settings.webhook_url:
        await bot.set_webhook(settings.webhook_url, certificate=ssl.cert_file)


@router.on_event("shutdown")
async def on_shutdown():
    await storage.close()
    await storage.wait_closed()
    await bot.close()


async def verify_token(token: str):
    if token != settings.bot_token:
        await asyncio.sleep(random.random())  # Additional protection from bruteforce
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


async def proceed_update(update: Update) -> None:
    account_ctx.set(AccountTelegram)
    Bot.set_current(bot)
    Dispatcher.set_current(dp)
    await dp.process_update(update)


@router.post(settings.prefix_webhook + "/{token}", dependencies=[Depends(verify_token)], include_in_schema=False)
async def execute(req: Request, background_tasks: BackgroundTasks) -> Response:
    try:
        update = Update(**(await req.json()))
    except JSONDecodeError:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    background_tasks.add_task(proceed_update, update)
    return Response(status_code=status.HTTP_200_OK)
