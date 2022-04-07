from aiogram import types

from models.rates import Rates
from telegram.utils import rate_limit
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
    await msg.answer(INFO_TEXT)


async def cmd_pass(msg: types.Message):
    pass


async def cmd_faq(msg: types.Message):
    pass


@rate_limit(1, 'start')
async def cmd_rates(msg: types.Message):
    logic_div = lambda n, d: d and n / d or 0
    logic_mult = lambda a, b: a*b if a and b else 0
    rates: Rates = await Rates.query.gino.first()
    RATES_TEXT = f"""🌲 <b>Bitcoin, Ethereum (BitMEX)</b>
<b>BTC</b>/USDT: <code>{rates.BitMEX_BTC_USD:.4f}</code>
<b>ETH</b>/USDT: <code>{rates.BitMEX_ETH_USD:.4f}</code>
<b>BTC</b>/RUB: <code>{logic_mult(rates.USD_RUB, rates.BitMEX_BTC_USD):.2f}</code>
<b>ETH</b>/RUB: <code>{logic_mult(rates.USD_RUB, rates.BitMEX_ETH_USD):.2f}</code>

🌿 <b>Fiat</b>
<b>USD</b>/RUB: <code>{rates.USD_RUB:.2f}</code>
<b>EUR</b>/RUB: <code>{rates.EUR_RUB:.2f}</code>
<b>CNY</b>/USD: <code>{logic_div(rates.CNY_RUB, rates.USD_RUB):.2f}</code>
<b>CNY</b>/RUB: <code>{rates.CNY_RUB:.2f}</code>"""
    # TODO: rates scaling
    await msg.answer(text=RATES_TEXT)


async def cmd_sbp(msg: types.Message):
    pass


async def cmd_atm(msg: types.Message):
    pass


async def cmd_atmusd(msg: types.Message):
    pass


async def cmd_id(msg: types.Message):
    await msg.answer(text=f"<code>{msg.from_user.id}</code> {msg.from_user.mention}")
