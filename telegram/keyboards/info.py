from aiogram.types import InlineKeyboardMarkup

from telegram.keyboards.common import cb_start
from telegram.keyboards.inline.consts import InlineConstructor
from utils.async_lru import alru_cache


@alru_cache
async def get_start_button(text: str) -> InlineKeyboardMarkup:
    return InlineConstructor.create_kb([{"text": text, "cb": ({"property": "start", "value": "refresh"}, cb_start)}],
                                       schema=[1])


@alru_cache
async def get_sbp_keyboard(btn_link: str, btn_back: str, link: str) -> InlineKeyboardMarkup:
    return InlineConstructor.create_kb([{"text": btn_link, "url": link},
                                        {"text": btn_back, "cb": ({"property": "start", "value": "refresh"}, cb_start)}
                                        ],
                                       schema=[1, 1])
