import time
from decimal import Decimal

from aiogram import types
from loguru import logger

from models.users import User
from telegram.utils import rate_limit
from utils.database import db
from utils.i18n import gettext as _

START_TEXT = '''🎮🌲 <b>BitcoinXBot</b> • безопасный кошелёк-хранилище и процессор платежей с железобетонной безопасностью и безупречным интерфейсом. <b>Закрепи в топе.</b> /info

Ваши фиатные балансы: ≈ {sumBTCBalance:.4f} <b>BTC</b>
🇺🇸 {USD:.4f} <b>USD</b>

Ваша криптовалюта:
🦚 {BTC:.8f} <b>BTC</b>

Заработано: 🌲 {earned:.8f} <b>BTC</b>
Приглашено: {invited} пользователей.'''


async def create_user(msg: types.Message):
    botname = (await msg.bot.me).username
    unixtime = int(time.time())
    user = User(
        userid=msg.from_user.id,
        username=msg.from_user.username,
        signup=unixtime,
        i=0,
        v=0,
        exp='H',
        def_cur='BTC',
        last_use=unixtime,
        lang='ru',
        parent=0,
        invited=0,
        earned=0,
        do=0,
        BalUpdated=unixtime,
        USD=0,
        USDX=0,
        EUR=0,
        EURX=0,
        RUB=0,
        RUBX=0,
        UAH=0,
        UAHX=0,
        BYN=0,
        BYNX=0,
        GEL=0,
        GELX=0,
        UZS=0,
        UZSX=0,
        KZT=0,
        KZTX=0,
        CNY=0,
        CNYX=0,
        BTC=Decimal("0.00010000"),
        BTC_blocked=0,
        UBTC=0,
        UBTC_blocked=0,
        ETH=0,
        ETH_blocked=0,
        BNB=0,
        BNBX=0,
        m_id=0,
        osl=0,
        bot=botname,
        pr=0,
    )
    await user.create()
    return user


def from_none_dict(_d: dict) -> dict:
    return {x: y if y else 0 for (x, y) in _d.items()}


def from_none_list(_l: list) -> list:
    return [x if x else 0 for x in _l]


@rate_limit(1, 'start')
async def bot_start(msg: types.Message):
    user = await User.query.where(User.userid == msg.from_user.id).gino.first()
    if not user:
        user = await create_user(msg)
    sumBTCBalance = sum(from_none_list([
        user.BTC,
        user.BTC_blocked,
    ]), start=Decimal(0))
    await msg.answer(_(START_TEXT).format(
        **from_none_dict({
            "sumBTCBalance": sumBTCBalance,
            "USD": user.USD,
            "BTC": user.BTC,
            "earned": user.earned,
            "invited": user.invited
        })
    ))


async def bot_help(msg: types.Message):
    text = [
        'Список команд: ',
        '/start - Начать диалог',
        '/help - Получить справку'
    ]
    await msg.answer('\n'.join(text))
