from aiogram import types
from aiogram.utils.callback_data import CallbackData

from telegram.keyboards.common import cb_start
from telegram.keyboards.info import get_start_button
from telegram.keyboards.inline.consts import InlineConstructor
from telegram.utils.reply import reply
from utils import settings
from utils.async_lru import alru_cache
from utils.i18n import gettext as _


async def cq_deposit(query: types.CallbackQuery):
    DEPOSIT_TEXT = _(
        """<b>Внесение (ввод средств)</b>
для <b>покупки крипты</b>, совершения <i>обменов, рассчётов и переводов</i>.

💶🥬🍸 <b>Наличными в Москве</b> → @ColdSig
от {min_sum_deposit} руб (или <i>эквивалент</i>)!
🇷🇺 RUB • <code>{deposit_interest}</code>
🇺🇸 USD • <code>{deposit_interest}</code>
🇪🇺 EUR • <code>{deposit_interest}</code>

💳🥬 <b>Онлайн</b> → @ColdSig
по курсу 1 USD = <code>{deposit_rate}</code> руб • <code>0%</code>
<i>переводом</i> от <code>{min_sum_bank}</code> руб.

🎮🥬 <b>Стейблкоинами</b> → @ColdSig
USDT • <code>{deposit_stable}</code>
USDC • <code>{deposit_stable}</code>

🎮🥬 <b>Любой криптой</b>, торгуемой на Binance • <code>{binance}</code> → @ColdSig"""
    )
    keyboard = await get_start_button(_("🌲⚙️МЕНЮ"))
    await reply(msg=query, text=DEPOSIT_TEXT.format(**settings.fiat_config), reply_markup=keyboard)


async def cq_withdraw(query: types.CallbackQuery):
    WITHDRAW_TEXT = _(
        """<b>Снятие (вывод средств)</b>

💶🥬🍸 <b>Наличными в Москве</b> → @ColdSig
от {min_sum_withdraw} руб (или <i>эквивалент</i>)!
🇷🇺 RUB • <code>{withdraw_interest}</code>
🇺🇸 USD • <code>{withdraw_interest}</code>
🇪🇺 EUR • <code>{withdraw_interest}</code>

💳🥬 <b>Онлайн</b> → @ColdSig
в <i>любой</i> <b>банк РФ</b> • от <code>{min_sum_bank}</code> руб. /SBP
1 USD = <code>{withdraw_rate}</code> руб. • <code>0%</code>

🎮🥬 Стейблкоинами → @ColdSig
USDT • <code>{withdraw_stable}</code> + gas
USDC • <code>{withdraw_stable}</code> + gas

🎮🥬 <b>Любой криптой</b>, торгуемой на Binance • <code>{binance}</code> → @ColdSig"""
    )
    keyboard = await get_withdraw_keyboard(_("🌲⚙️МЕНЮ"), _("⚡️🥬💳В любой банк РФ!"))
    await reply(msg=query, text=WITHDRAW_TEXT.format(**settings.fiat_config), reply_markup=keyboard)


async def cq_anybank(query: types.CallbackQuery):
    ANYBANK_TEXT = _(
        """💳🥬 <b>Онлайн</b> → @ColdSig
в <i>любой</i> <b>банк РФ</b> • от <code>{min_sum_bank}</code> руб. /SBP
1 USD = <code>{withdraw_rate}</code> руб. • <code>0%</code>"""
    )
    keyboard = await get_start_button("🔙")
    await reply(msg=query, text=ANYBANK_TEXT.format(**settings.fiat_config), reply_markup=keyboard)


@alru_cache
async def get_withdraw_keyboard(text1: str, text2: str):
    return InlineConstructor.create_kb([{"text": text1, "cb": ({"property": "start", "value": "refresh"}, cb_start)},
                                        {"text": text2, "cb": ({"property": "fiat", "value": "anybank"}, cb_start)}
                                        ],
                                       schema=[1, 1])
