import time
from typing import Optional

from pydantic import condecimal
from sqlalchemy import Column, Integer, BigInteger, String, Numeric

from utils.database import db


class User(db.Model):
    __tablename__ = "main"

    id: Optional[int] = Column(BigInteger(), primary_key=True, autoincrement=True, nullable=True)
    userid: Optional[int] = Column(BigInteger(), index=True)
    username: Optional[str] = Column(String(60))
    signup: Optional[int] = Column(Integer(), default=int(time.time()))
    i: Optional[int] = Column(BigInteger(), default=0)
    v: Optional[int] = Column(Integer(), default=0)
    exp: Optional[str] = Column(String(1), default='H')
    def_cur: Optional[str] = Column(String(3), default='BTC')
    send_am: Optional[condecimal(max_digits=20, decimal_places=8)] = Column(Numeric(20, 8))
    send_as: Optional[str] = Column(String(5))
    send_ac: Optional[int] = Column(BigInteger())
    last_use: Optional[int] = Column(Integer(), default=int(time.time()))
    lang: Optional[str] = Column(String(2), default='en')
    parent: Optional[int] = Column(BigInteger(), default=0)
    invited: Optional[int] = Column(Integer(), default=0)
    earned: Optional[condecimal(max_digits=16, decimal_places=8)] = Column(Numeric(16, 8), default=0)
    do: Optional[str] = Column(String(70), default=0)
    BalUpdated: Optional[int] = Column(Integer(), default=int(time.time()))
    USD: Optional[condecimal(max_digits=20, decimal_places=4)] = Column(Numeric(20, 4), default=0)
    USDX: Optional[condecimal(max_digits=20, decimal_places=4)] = Column(Numeric(20, 4), default=0)
    EUR: Optional[condecimal(max_digits=20, decimal_places=4)] = Column(Numeric(20, 4), default=0)
    EURX: Optional[condecimal(max_digits=20, decimal_places=4)] = Column(Numeric(20, 4), default=0)
    RUB: Optional[condecimal(max_digits=20, decimal_places=4)] = Column(Numeric(20, 4), default=0)
    RUBX: Optional[condecimal(max_digits=20, decimal_places=4)] = Column(Numeric(20, 4), default=0)
    UAH: Optional[condecimal(max_digits=20, decimal_places=4)] = Column(Numeric(20, 4), default=0)
    UAHX: Optional[condecimal(max_digits=20, decimal_places=4)] = Column(Numeric(20, 4), default=0)
    BYN: Optional[condecimal(max_digits=20, decimal_places=4)] = Column(Numeric(20, 4), default=0)
    BYNX: Optional[condecimal(max_digits=20, decimal_places=4)] = Column(Numeric(20, 4), default=0)
    GEL: Optional[condecimal(max_digits=20, decimal_places=4)] = Column(Numeric(20, 4), default=0)
    GELX: Optional[condecimal(max_digits=20, decimal_places=4)] = Column(Numeric(20, 4), default=0)
    UZS: Optional[condecimal(max_digits=20, decimal_places=4)] = Column(Numeric(20, 4), default=0)
    UZSX: Optional[condecimal(max_digits=20, decimal_places=4)] = Column(Numeric(20, 4), default=0)
    KZT: Optional[condecimal(max_digits=20, decimal_places=4)] = Column(Numeric(20, 4), default=0)
    KZTX: Optional[condecimal(max_digits=20, decimal_places=4)] = Column(Numeric(20, 4), default=0)
    CNY: Optional[condecimal(max_digits=20, decimal_places=4)] = Column(Numeric(20, 4), default=0)
    CNYX: Optional[condecimal(max_digits=20, decimal_places=4)] = Column(Numeric(20, 4), default=0)
    BTC: Optional[condecimal(max_digits=16, decimal_places=8)] = Column(Numeric(16, 8), default=0)
    BTC_blocked: Optional[condecimal(max_digits=16, decimal_places=8)] = Column(Numeric(16, 8), default=0)
    UBTC: Optional[condecimal(max_digits=16, decimal_places=8)] = Column(Numeric(16, 8), default=0)
    UBTC_blocked: Optional[condecimal(max_digits=16, decimal_places=8)] = Column(Numeric(16, 8), default=0)
    ETH: Optional[condecimal(max_digits=16, decimal_places=8)] = Column(Numeric(16, 8), default=0)
    ETH_blocked: Optional[condecimal(max_digits=16, decimal_places=8)] = Column(Numeric(16, 8), default=0)
    BNB: Optional[condecimal(max_digits=16, decimal_places=4)] = Column(Numeric(16, 4), default=0)
    BNBX: Optional[condecimal(max_digits=16, decimal_places=4)] = Column(Numeric(16, 4), default=0)
    m_id: Optional[int] = Column(BigInteger(), default=0)
    osl: Optional[int] = Column(Integer(), default=0)
    bot: Optional[str] = Column(String(15))
    pr: Optional[int] = Column(Integer(), default=0)
    comment: Optional[str] = Column(String(10))
    z: Optional[str] = Column(String(1))
    p: Optional[str] = Column(String(1))
