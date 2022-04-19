from typing import Union

from aiogram import types
from aiogram.dispatcher import FSMContext

from services.common import start, StartData
from telegram.keyboards.common import get_start_markup, StartKeyboardText
from telegram.utils import rate_limit, reply
from utils.i18n import i18n
from utils.i18n import gettext as _
from utils.misc import from_none_dict


@rate_limit(1, 'start')
async def cmd_start(msg: Union[types.Message, types.CallbackQuery] = None):
    START_TEXT = _(
        "🎮🌲 <b>BitcoinXBot</b> • безопасный кошелёк-хранилище и процессор платежей с железобетонной безопасностью и безупречным интерфейсом. <b>Закрепи в топе.</b> /info\n"
        "\n"
        "Ваши фиатные балансы: ≈ <code>{sum_fiat_balance:.4f}</code> <b>BTC</b>\n"
        "{assets}"
        "\n"
        "Ваша криптовалюта:\n"
        "🦚 <code>{BTC:.8f}</code> <b>BTC</b>\n"
        "\n"
        "Заработано: 🌲 <code>{earned:.8f}</code> <b>BTC</b>\n"
        "Приглашено: <code>{invited}</code> пользователей.")
    KBD_TEXT = StartKeyboardText(
        fiat_deposit=_("Внести RUB, USD"),
        fiat_withdraw=_("Вывести RUB, USD"),
        btc_deposit=_("📥 Внести BTC"),
        btc_withdraw=_("📤 Вывести BTC"),
        btc_to_ultra=_("Заменить 🦚 BTC → 🥬 УльтраЧистые BTC"),
        ultra_to_btc=_("Перевести 🥬 УльтраЧистые BTC → 🦚 BTC"),
        services=_("🍇 Услуги"),
        settings=_("🎛 Настройки"),
        refresh="♻",
    )

    data: StartData = await start()
    assets = "".join([
        f"🇺🇸 <code>{data.USD:.4f}</code> <b>USD</b>\n" if data.USD else "",
        f"🇷🇺 <code>{data.RUB:.4f}</code> <b>RUB</b>\n" if data.RUB else "",
        f"🇪🇺 <code>{data.EUR:.4f}</code> <b>EUR</b>\n" if data.EUR else "",
        f"🇨🇳 <code>{data.CNY:.4f}</code> <b>CNY</b>\n" if data.CNY else "",
    ])
    answer = {"text": START_TEXT.format(**from_none_dict(data._asdict()), assets=assets),
              "reply_markup": await get_start_markup(KBD_TEXT)}
    await reply(msg=msg, **answer)


@rate_limit(3, 'language')
async def cq_change_language(query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await query.answer()
    _data = await state.get_data()
    if _data["lang"] != callback_data["value"]:
        await i18n.set_user_locale(callback_data["value"])
    await cmd_start(query)
