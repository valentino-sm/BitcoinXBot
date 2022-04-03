from decimal import Decimal
from typing import NamedTuple

from components.user import User
from utils.misc import from_none_list


class StartData(NamedTuple):
    sumBTCBalance: Decimal
    BTC: Decimal
    USD: Decimal
    earned: Decimal
    invited: int


async def start() -> StartData:
    user = await User.get()
    sumBTCBalance = sum(from_none_list([
        user.BTC,
        user.BTC_blocked,
    ]), start=Decimal(0))
    return StartData(
        sumBTCBalance=sumBTCBalance,
        BTC=user.BTC,
        USD=user.USD,
        earned=user.earned,
        invited=user.invited,
    )
