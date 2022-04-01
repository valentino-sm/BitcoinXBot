import random
from dataclasses import dataclass, field
from typing import Any, Tuple

from aiogram.contrib.middlewares.i18n import I18nMiddleware as BaseI18nMiddleware
from loguru import logger


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
        "uk": LanguageData("🇺🇦", "Українська"),
    }

    async def get_user_locale(self, action: str, args: Tuple[Any]) -> str:
        data: dict = args[-1]
        if "chat" in data:
            logger.debug(data["chat"].language)
            return data["chat"].language or self.default
        logger.debug(f"default: {self.default}")
        return random.choice(["ru", "en"])
