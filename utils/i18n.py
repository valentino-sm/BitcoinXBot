from pathlib import Path

from telegram.middlewares.i18n import I18nMiddleware

i18n = I18nMiddleware(domain="bot", path=Path(__file__).parent.parent / 'locales')

_ = i18n.gettext
