from aiogram import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from utils import i18n
from utils.i18n import gettext as _

cb_start = CallbackData("user", "property", "value")


async def get_start_markup() -> InlineKeyboardMarkup:
    # _data = await Dispatcher.get_current().current_state().get_data()
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=_("🇺🇸 English"),
                    callback_data=cb_start.new(property="language", value="change"),
                )
            ],
        ]
    )
