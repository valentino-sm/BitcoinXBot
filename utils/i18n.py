from pathlib import Path
from typing import Any

from telegram.middlewares.i18n import I18nMiddleware

i18n = I18nMiddleware(domain="bot", path=Path(__file__).parent.parent / 'locales', default="ru")


def gettext(s: Any) -> str:
    return i18n.gettext(s)

def lazy_gettext(s: Any) -> str:
    return i18n.lazy_gettext()