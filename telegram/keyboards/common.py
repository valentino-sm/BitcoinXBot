from typing import NamedTuple

from aiogram import Dispatcher
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from telegram.keyboards.inline.consts import InlineConstructor
from utils import i18n
from utils.async_lru import alru_cache

cb_start = CallbackData("start", "property", "value")


class StartKeyboardText(NamedTuple):
    fiat_deposit: str
    fiat_withdraw: str
    btc_deposit: str
    btc_withdraw: str
    btc_to_ultra: str
    ultra_to_btc: str
    services: str
    settings: str
    refresh: str

    def __hash__(self):
        return hash(self.settings)


@alru_cache
async def get_start_markup(KBD_TEXT: StartKeyboardText) -> InlineKeyboardMarkup:
    btn_fiat = [{"text": KBD_TEXT.fiat_deposit, "cb": ({"property": "fiat", "value": "deposit"}, cb_start)},
                {"text": KBD_TEXT.fiat_withdraw, "cb": ({"property": "fiat", "value": "withdraw"}, cb_start)}]
    btn_btc = [{"text": KBD_TEXT.btc_deposit, "cb": ({"property": "btc", "value": "deposit"}, cb_start)},
               {"text": KBD_TEXT.btc_withdraw, "cb": ({"property": "btc", "value": "withdraw"}, cb_start)}]
    btn_ultra = [{"text": KBD_TEXT.btc_to_ultra, "cb": ({"property": "ultra", "value": "to"}, cb_start)},
                 {"text": KBD_TEXT.ultra_to_btc, "cb": ({"property": "ultra", "value": "from"}, cb_start)}]
    btn_services = [{"text": KBD_TEXT.services, "cb": ({"property": "start", "value": "services"}, cb_start)}]

    btn_other = [{"text": KBD_TEXT.settings, "cb": ({"property": "start", "value": "settings"}, cb_start)},
                 {"text": KBD_TEXT.refresh, "cb": ({"property": "start", "value": "refresh"}, cb_start)}]

    _data = await Dispatcher.get_current().current_state().get_data()
    btn_lang = [{"text": lang_text.label,
                 "cb": ({"property": "language", "value": lang_code}, cb_start),
                 } for lang_code, lang_text in i18n.AVAILABLE_LANGUAGES.items() if lang_code != _data["lang"]
                ]
    btn_lang = btn_lang[:1]  # noqa Hack, because we only have one language so far ¯\_(ツ)_/¯

    return InlineConstructor.create_kb(
        btn_fiat +
        btn_btc +
        btn_ultra +
        btn_services +
        btn_other +
        btn_lang
        , schema=[2, 2, 1, 1, 1, 3]
    )


@alru_cache
async def get_back_button(text: str) -> InlineKeyboardMarkup:
    return InlineConstructor.create_kb([{"text": text, "cb": ({"property": "start", "value": "refresh"}, cb_start)}],
                                       schema=[1])
