from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart, Command

from . import common, info, fiat
from ._error_handler import error_handler
from telegram.keyboards.common import cb_start


def register_errors_handler(dp: Dispatcher):
    dp.register_errors_handler(error_handler)


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(common.cmd_start, CommandStart())
    dp.register_callback_query_handler(common.cmd_start, cb_start.filter(property="start", value="refresh"))
    dp.register_callback_query_handler(common.cq_change_language, cb_start.filter(property="language"))

    dp.register_message_handler(info.cmd_info, Command("info"))
    dp.register_message_handler(info.cmd_rates, Command("rates"))
    dp.register_message_handler(info.cmd_sbp, Command("sbp"))
    dp.register_message_handler(info.cmd_atm, Command("atm"))
    dp.register_message_handler(info.cmd_atmusd, Command("atmusd"))
    dp.register_message_handler(info.cmd_id, Command("id"))

    dp.register_callback_query_handler(fiat.cq_deposit, cb_start.filter(property="fiat", value="deposit"))
    dp.register_callback_query_handler(fiat.cq_withdraw, cb_start.filter(property="fiat", value="withdraw"))
    dp.register_callback_query_handler(fiat.cq_anybank, cb_start.filter(property="fiat", value="anybank"))
