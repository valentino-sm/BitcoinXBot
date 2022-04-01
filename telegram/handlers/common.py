import time
from decimal import Decimal

from aiogram import types, Dispatcher
from loguru import logger

from models.users import User
from telegram.keyboards.common import get_start_markup
from telegram.utils import rate_limit
from utils.i18n import i18n
from utils.i18n import gettext as _


async def create_user(msg: types.Message):
    _data = await Dispatcher.get_current().current_state().get_data()
    botname = (await msg.bot.me).username
    unixtime = int(time.time())
    lang = _data["lang"] if "lang" in _data else i18n.default
    user = User(
        userid=msg.from_user.id,
        username=msg.from_user.username,
        signup=unixtime,
        i=0,
        v=0,
        exp='H',
        def_cur='BTC',
        last_use=unixtime,
        lang=lang,
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
async def cmd_start(msg: types.Message):
    START_TEXT = _(
        "🎮🌲 <b>BitcoinXBot</b> • безопасный кошелёк-хранилище и процессор платежей с железобетонной безопасностью и безупречным интерфейсом. <b>Закрепи в топе.</b> /info\n"
        "\n"
        "Ваши фиатные балансы: ≈ {sumBTCBalance:.4f} <b>BTC</b>\n"
        "🇺🇸 {USD:.4f} <b>USD</b>\n"
        "\n"
        "Ваша криптовалюта:\n"
        "🦚 {BTC:.8f} <b>BTC</b>\n"
        "\n"
        "Заработано: 🌲 {earned:.8f} <b>BTC</b>\n"
        "Приглашено: {invited} пользователей.")
    userid = types.User.get_current().id
    user = await User.query.where(User.userid == userid).gino.first()
    if not user:
        user = await create_user(msg)
    sumBTCBalance = sum(from_none_list([
        user.BTC,
        user.BTC_blocked,
    ]), start=Decimal(0))
    await msg.answer(
        text=START_TEXT.format(
            **from_none_dict({
                "sumBTCBalance": sumBTCBalance,
                "USD": user.USD,
                "BTC": user.BTC,
                "earned": user.earned,
                "invited": user.invited
            })),
        reply_markup=await get_start_markup()
    )


@rate_limit(3, 'change_language')
async def cq_change_language(query: types.CallbackQuery, callback_data: dict):
    logger.warning(query)
    logger.warning(callback_data)
    _data = await Dispatcher.get_current().current_state().get_data()
    if _data["lang"] == "ru":
        await i18n.set_user_locale("en")
    else:
        await i18n.set_user_locale("ru")
    await cmd_start(query.message)


async def cmd_info(msg: types.Message):
    HELP_TEXT = _(
        'Список команд: \n'
        '/start - Начать диалог\n'
        '/help - Получить справку'
    )
    await msg.answer(HELP_TEXT)
