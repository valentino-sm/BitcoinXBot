from typing import Optional

from pydantic import condecimal
from sqlalchemy import Column, Integer, Numeric, String

from utils.database import db


class Rates(db.Model):
    __tablename__ = "rates"

    id: Optional[int] = Column(Integer(), primary_key=True, autoincrement=True, nullable=True)
    txfee: Optional[condecimal(max_digits=16, decimal_places=8)] = Column(Numeric(16, 8))
    satb: Optional[condecimal(max_digits=16, decimal_places=8)] = Column(Numeric(16, 8))
    UB: Optional[condecimal(max_digits=5, decimal_places=2)] = Column(Numeric(5, 2))
    US: Optional[condecimal(max_digits=5, decimal_places=2)] = Column(Numeric(5, 2))
    USD_RUB_buy: Optional[condecimal(max_digits=10, decimal_places=4)] = Column(Numeric(10, 4))
    USD_RUB: Optional[condecimal(max_digits=10, decimal_places=4)] = Column(Numeric(10, 4))
    USD_RUB_sell: Optional[condecimal(max_digits=10, decimal_places=4)] = Column(Numeric(10, 4))
    EUR_RUB: Optional[condecimal(max_digits=10, decimal_places=4)] = Column(Numeric(10, 4))
    CNY_RUB: Optional[condecimal(max_digits=10, decimal_places=4)] = Column(Numeric(10, 4))
    BitMEX_BTC_USD: Optional[condecimal(max_digits=16, decimal_places=4)] = Column(Numeric(16, 4))
    BitMEX_ETH_USD: Optional[condecimal(max_digits=16, decimal_places=4)] = Column(Numeric(16, 4))
    Binance_BTC_USDT: Optional[condecimal(max_digits=16, decimal_places=4)] = Column(Numeric(16, 4))
    Binance_ETH_USDT: Optional[condecimal(max_digits=16, decimal_places=4)] = Column(Numeric(16, 4))
    Kraken_BTC_EUR: Optional[condecimal(max_digits=16, decimal_places=4)] = Column(Numeric(16, 4))
    Kraken_ETH_EUR: Optional[condecimal(max_digits=16, decimal_places=4)] = Column(Numeric(16, 4))
    unixtime: Optional[int] = Column(Integer())
    time: Optional[str] = Column(String(20))
    exch_up: Optional[str] = Column(String(10))
    ZEUS_last: Optional[condecimal(max_digits=15, decimal_places=4)] = Column(Numeric(15, 4))
    Garantex_USDT_RUB_bid: Optional[condecimal(max_digits=8, decimal_places=4)] = Column(Numeric(8, 4))
