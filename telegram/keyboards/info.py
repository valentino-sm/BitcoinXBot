from aiogram.types import InlineKeyboardMarkup

from telegram.keyboards.common import cb_start
from telegram.keyboards.inline.consts import InlineConstructor
from utils.async_lru import alru_cache


@alru_cache
async def get_start_button(text: str) -> InlineKeyboardMarkup:
    return InlineConstructor.create_kb([{"text": text, "cb": ({"property": "start", "value": "refresh"}, cb_start)}], schema=[1])