from aiogram import Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.middlewares import BaseMiddleware

from utils import settings
from .throttling import ThrottlingMiddleware


def setup(dp: Dispatcher, i18n: BaseMiddleware = None):
    if settings.debug:
        dp.middleware.setup(LoggingMiddleware("bot"))
    dp.middleware.setup(ThrottlingMiddleware())
    # dp.middleware.setup(ACLMiddleware())

    if i18n:
        dp.middleware.setup(i18n)
