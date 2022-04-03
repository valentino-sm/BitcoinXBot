from dataclasses import dataclass, field
from typing import Any, Tuple, Optional

from aiogram import types, Dispatcher
from aiogram.contrib.middlewares.i18n import I18nMiddleware as BaseI18nMiddleware
from babel import Locale

from models.users import User


@dataclass
class LanguageData:
    flag: str
    title: str
    label: str = field(init=False, default=None)

    def __post_init__(self):
        self.label = f"{self.flag} {self.title}"


class I18nMiddleware(BaseI18nMiddleware):
    AVAILABLE_LANGUAGES = {
        "en": LanguageData("🇺🇸", "English"),
        "ru": LanguageData("🇷🇺", "Русский"),
        # "uk": LanguageData("🇺🇦", "Українська"),
    }

    async def get_default_locale(self):
        return str(next(iter(self.AVAILABLE_LANGUAGES)))

    async def setup_new_user_locale(self) -> str:
        """
        Only for updates we don't have locale in Storage
        Get in database first try
        Get from telegram locale second try
        Set to default last
        """
        current_user: Optional[types.User] = types.User.get_current()
        if current_user:
            lang = await User.select('lang').where(User.userid == current_user.id).gino.scalar()
            if lang and lang in self.AVAILABLE_LANGUAGES.keys():
                await self.set_user_locale(lang, to_database=False)
                return lang

        locale: Optional[Locale] = current_user.locale if current_user else None
        if locale and locale.language in self.AVAILABLE_LANGUAGES.keys():
            result = locale.language
        else:
            result = self.get_default_locale()

        await self.set_user_locale(result)

        return result

    async def get_user_locale(self, action: str, args: Tuple[Any]) -> str:
        """
        Parent call this for every update Automatically
        """
        state = Dispatcher.get_current().current_state()
        data = await state.get_data()
        if "lang" not in data:
            data["lang"] = await self.setup_new_user_locale()
        return data["lang"]

    async def set_user_locale(self, locale: str, to_database: bool = True) -> None:
        if locale in self.AVAILABLE_LANGUAGES.keys():
            # ContextVar
            self.ctx_locale.set(locale)
            # Storage
            state = Dispatcher.get_current().current_state()
            await state.update_data({"lang": locale})
            # Database
            if not to_database:
                return
            current_user = types.User.get_current()
            if not current_user:
                return
            await User.update.values(lang=locale).where(User.userid == current_user.id).gino.status()
