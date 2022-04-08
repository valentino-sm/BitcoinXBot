from aiogram import Dispatcher, types

from .account import AccountMeta, AccountData
from utils import i18n
from utils.async_lru import alru_cache


class AccountTelegram(AccountMeta):
    @staticmethod
    @alru_cache(maxsize=None)
    async def get_me() -> str:
        return (await Dispatcher.get_current().bot.me).username

    @staticmethod
    def get_userid() -> int:
        return types.User.get_current().id

    @staticmethod
    async def get_data() -> AccountData:
        current_user = types.User.get_current()
        _data = await Dispatcher.get_current().current_state().get_data()
        lang = _data["lang"] if "lang" in _data else i18n.get_default_locale()
        return AccountData(userid=current_user.id, username=current_user.username, lang=lang)
