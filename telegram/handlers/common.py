from aiogram import types, Dispatcher

from services.common import start
from telegram.keyboards.common import get_start_markup
from telegram.utils import rate_limit
from utils.i18n import i18n
from utils.i18n import gettext as _
from utils.misc import from_none_dict


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

    start_data = await start()
    await msg.answer(
        text=START_TEXT.format(**from_none_dict(start_data._asdict())),
        reply_markup=await get_start_markup()
    )


@rate_limit(3, 'language')
async def cq_change_language(query: types.CallbackQuery, callback_data: dict):
    await query.answer()
    _data = await Dispatcher.get_current().current_state().get_data()
    if _data["lang"] != callback_data["value"]:
        await i18n.set_user_locale(callback_data["value"])
    await cmd_start(query.message)


async def cmd_info(msg: types.Message):
    HELP_TEXT = _(
        'Список команд: \n'
        '/start - Начать диалог\n'
        '/info - Получить справку'
    )
    await msg.answer(HELP_TEXT)
