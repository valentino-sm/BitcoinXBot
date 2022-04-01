from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart, CommandHelp

from . import common
from .error_handler import error_handler
from ..keyboards.common import cb_start


def register_errors_handler(dp: Dispatcher):
    dp.register_errors_handler(error_handler)


def register_handlers_base(dp: Dispatcher):
    dp.register_message_handler(common.cmd_start, CommandStart())
    dp.register_message_handler(common.cmd_info, CommandHelp())

    dp.register_callback_query_handler(common.cq_change_language, cb_start.filter(property="language", value="change"))
