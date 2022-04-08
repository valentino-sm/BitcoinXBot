from decimal import Decimal
from typing import NamedTuple

from components.user import User
from components.rates import Rates
from models.users import User as UserModel
from utils.misc import from_none_list, logic_div


class StartData(NamedTuple):
    sum_fiat_balance: Decimal
    BTC: Decimal
    USD: Decimal
    RUB: Decimal
    EUR: Decimal
    CNY: Decimal
    earned: Decimal
    invited: int


async def sum_fiat_balance(user: UserModel, rates: Rates) -> Decimal:
    if not isinstance(user, UserModel):
        return Decimal(0)
    if not isinstance(rates, Rates):
        return user.BTC or Decimal(0)
    l1 = [
        user.USD,
        user.RUB,
        user.EUR,
        user.CNY
    ]
    l2 = [
        rates.BitMEX_BTC_USD,
        rates.BTC_RUB,
        rates.BTC_EUR,
        rates.BTC_CNY,
    ]
    return sum(logic_div(x, y) for x, y in zip(from_none_list(l1), from_none_list(l2)))


async def start() -> StartData:
    user: UserModel = await User.get_current()
    rates: Rates = await Rates.query.gino.first()

    return StartData(
        sum_fiat_balance=await sum_fiat_balance(user, rates),
        BTC=user.BTC,
        USD=user.USD,
        RUB=user.RUB,
        EUR=user.EUR,
        CNY=user.CNY,
        earned=user.earned,
        invited=user.invited,
    )
