from decimal import Decimal
from typing import NamedTuple

from loguru import logger

from components.user import User
from models.users import User as UserModel
from models.rates import Rates
from utils.misc import from_none_list


class StartData(NamedTuple):
    sumBTCBalance: Decimal
    BTC: Decimal
    USD: Decimal
    RUB: Decimal
    EUR: Decimal
    CNY: Decimal
    earned: Decimal
    invited: int


async def sumBTCBalance(user: UserModel, rates: Rates) -> Decimal:
    if not isinstance(user, UserModel):
        return Decimal(0)
    if not isinstance(rates, Rates):
        return user.BTC or Decimal(0)
    logic_mult = lambda a, b: a*b if a and b else 0
    logic_div = lambda n, d: d and n / d or 0
    l1 = [
        user.BTC,
        user.USD,
        user.RUB,
        user.EUR,
        user.CNY
    ]
    l2 = [
        1,
        rates.BitMEX_BTC_USD,
        logic_mult(rates.USD_RUB, rates.BitMEX_BTC_USD),
        logic_mult(rates.EUR_RUB, rates.BitMEX_BTC_USD),
        logic_mult(rates.CNY_RUB, rates.BitMEX_BTC_USD),
    ]
    return sum(logic_div(x, y) for x, y in zip(from_none_list(l1), from_none_list(l2)))


async def start() -> StartData:
    user: UserModel = await User.get_current()
    rates: Rates = await Rates.query.gino.first()

    _sumBTCBalance = await sumBTCBalance(user, rates)
    return StartData(
        sumBTCBalance=_sumBTCBalance,
        BTC=user.BTC,
        USD=user.USD,
        RUB=user.RUB,
        EUR=user.EUR,
        CNY=user.CNY,
        earned=user.earned,
        invited=user.invited,
    )
