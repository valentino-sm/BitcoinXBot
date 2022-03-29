from aiogram import Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.middlewares import BaseMiddleware

from .throttling import ThrottlingMiddleware
from .acl import ACLMiddleware


def setup(dp: Dispatcher, i18n: BaseMiddleware = None):
    dp.middleware.setup(LoggingMiddleware("bot"))
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(ACLMiddleware())

    if i18n:
        dp.middleware.setup(i18n)
