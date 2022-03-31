from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart, CommandHelp

from . import common
from .error_handler import error_handler


def register_errors_handler(dp: Dispatcher):
    dp.register_errors_handler(error_handler)


def register_handlers_base(dp: Dispatcher):
    dp.register_message_handler(common.bot_start, CommandStart())
    dp.register_message_handler(common.bot_help, CommandHelp())
