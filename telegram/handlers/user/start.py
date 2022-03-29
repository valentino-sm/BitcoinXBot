from aiogram import types

from models.users import User
from utils.i18n import _


async def bot_start(msg: types.Message):
    await msg.answer(_('''🎮🌲 <b>BitcoinXBot</b> • безопасный кошелёк-хранилище и процессор платежей с железобетонной безопасностью и безупречным интерфейсом. <b>Закрепи в топе.</b> /info

Ваши фиатные балансы: ≈ 0.0000 <b>BTC</b>
🇺🇸 0.0000 <b>USD</b>

Ваша криптовалюта:
🦚 0.00000000 <b>BTC</b>

Заработано: 🌲 0.00000000 <b>BTC</b>
Приглашено: 0 пользователей.'''))
