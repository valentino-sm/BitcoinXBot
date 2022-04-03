from contextvars import ContextVar
from typing import Type, Union

from enum import Enum, auto

from components.account_telegram import AccountTelegram


class AccountDataSource(Enum):
    Telegram = auto()
    Web = auto()


ctxDataSource: ContextVar[AccountDataSource] = ContextVar('var')


def current() -> Union[Type[AccountTelegram], None]:
    if ctxDataSource.get() is AccountDataSource.Telegram:
        return AccountTelegram
    elif ctxDataSource.get() is AccountDataSource.Web:
        return None
    return None
