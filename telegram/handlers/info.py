from aiogram import types
from aiogram.types import InlineKeyboardMarkup

from components import Rates
from telegram.keyboards.inline.consts import InlineConstructor
from telegram.keyboards.common import get_back_button, cb_start
from telegram.utils import rate_limit, reply
from utils.async_lru import alru_cache
from utils.i18n import gettext as _


async def cmd_info(msg: types.Message):
    INFO_TEXT = _(
        """🦚 <b>Кратко о боте</b>
        
Самый популярный способ использования бота такой:
BTC → UltraClean BTC → RUB

🌲 люди заводят битки (BTC) →
🥬 меняют их на УльтраЧистые битки (UltraClean BTC) →
🍇 выводят на внешние адреса или меняют в USD →
💶 выводят USD при необходимости в <b>рубли (RUB)</b> <i>онлайн</i> в любой банк РФ по Системе Быстрых Платежей (или забирают <i>наличные</i>) через @ColdSig. Например, сейчас комиссия за вывод крипты в рубли - всего <code>3.50%</code>.

💶 Также через @ColdSig можно покупать и продавать крипту в любых объёмах за нал в любое время дня и ночи 24/7. 🌃 Очень удобно и безопасно.

Прочие функции этого бота:

— <b>Кошелёк</b> - безопасный <i>кошелёк-хранилище, биржа и процессор платежей</i> с железобетонной безопасностью и безупречным интерфейсом.

— <b>Переводы КОДАМИ</b> - вы можете перевести любую сумму в <b>RUB, USD, EUR, BTC</b>  любому человеку абсолютно <i>бесплатно</i>и <i>без ограничений</i>.

— <b>Биржа</b> - мгновенное исполнение по рынку.

— <b>VPN</b>: самый быстрый VPN-сервис с оплатой криптой по выгодному курсу.

— По желанию (мы не блокируем) <b>проверка блокировки стейблкоинов</b> (USDT, USDC, GUSD) и адреса Ethereum.

— По желанию (мы не блокируем) <b>AML-проверка адресов Bitcoin</b>."""
    )
    await reply(msg=msg, text=INFO_TEXT, reply_markup=await _get_general_keyboard())


async def cmd_pass(msg: types.Message):
    # TODO: pass
    pass


async def cmd_faq(msg: types.Message):
    pass


@rate_limit(1, 'start')
async def cmd_rates(msg: types.Message):
    rates: Rates = await Rates.query.gino.first()
    RATES_TEXT = f"""🌲 <b>Bitcoin, Ethereum (BitMEX)</b>
<b>BTC</b>/USDT: <code>{rates.BitMEX_BTC_USD:.4f}</code>
<b>ETH</b>/USDT: <code>{rates.BitMEX_ETH_USD:.4f}</code>
<b>BTC</b>/RUB: <code>{rates.BTC_RUB:.2f}</code>
<b>ETH</b>/RUB: <code>{rates.ETH_RUB:.2f}</code>

🌿 <b>Fiat</b>
<b>USD</b>/RUB: <code>{rates.USD_RUB:.2f}</code>
<b>EUR</b>/RUB: <code>{rates.EUR_RUB:.2f}</code>
<b>CNY</b>/USD: <code>{rates.CNY_USD:.2f}</code>
<b>CNY</b>/RUB: <code>{rates.CNY_RUB:.2f}</code>"""
    await reply(msg=msg, text=RATES_TEXT, reply_markup=await _get_general_keyboard())


async def cmd_sbp(msg: types.Message):
    link = "https://help.tinkoff.ru/black/debit-common/sbp-turn-on/"
    SBP_TEXT = _(
        """🌲🥬 Включается возможность получения платежей по <b>Системе быстрых платежей (СБП)</b> в приложении Сбербанк Онлайн <b><a href="{link}">в несколько касаний</a></b>.""") \
        .format(link=link)
    keyboard = await _get_sbp_keyboard(btn_link=_("🥬Включить СБП"), btn_back="🌲 Super!", link=link)
    await reply(msg=msg, text=SBP_TEXT, disable_web_page_preview=True, reply_markup=keyboard)


@alru_cache
async def _get_sbp_keyboard(btn_link: str, btn_back: str, link: str) -> InlineKeyboardMarkup:
    return InlineConstructor.create_kb([{"text": btn_link, "url": link},
                                        {"text": btn_back, "cb": ({"property": "start", "value": "refresh"}, cb_start)}
                                        ],
                                       schema=[1, 1])


async def cmd_atm(msg: types.Message):
    SBPATM_TEXT = _("""🌲🥬 <b>Карта банкоматов Тинькофф</b>

https://www.tinkoff.ru/maps/atm/?partner=tcs""")

    await reply(msg=msg, text=SBPATM_TEXT, disable_web_page_preview=True, reply_markup=await _get_general_keyboard())


async def cmd_atmusd(msg: types.Message):
    ATMUSD_TEXT = _("""🌲🥬 <b>Карта банкоматов Тинькофф</b> (USD)

https://www.tinkoff.ru/maps/atm/?partner=tcs&currency=USD&amount=5000""")
    await reply(msg=msg, text=ATMUSD_TEXT, disable_web_page_preview=True, reply_markup=await _get_general_keyboard())


async def cmd_id(msg: types.Message):
    await reply(msg=msg, text=f"<code>{msg.from_user.id}</code> {msg.from_user.mention}",
                reply_markup=await _get_general_keyboard())


async def _get_general_keyboard() -> InlineKeyboardMarkup:
    return await get_back_button(_("🌲 МЕНЮ"))
