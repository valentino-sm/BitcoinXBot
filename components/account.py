from abc import ABCMeta, abstractmethod
from typing import NamedTuple, Type
from contextvars import ContextVar


class AccountData(NamedTuple):
    userid: int
    username: str
    lang: str


class AccountMeta(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    async def get_me() -> str:
        pass

    @staticmethod
    @abstractmethod
    def get_userid() -> int:
        pass

    @staticmethod
    @abstractmethod
    async def get_data() -> AccountData:
        pass


account_ctx: ContextVar[Type[AccountMeta]] = ContextVar('account_source')
