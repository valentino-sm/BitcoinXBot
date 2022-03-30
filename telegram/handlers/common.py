from aiogram import types
from loguru import logger

from models.users import User
from telegram.utils import rate_limit
from utils.i18n import _


@rate_limit(1, 'help')
async def bot_start(msg: types.Message, user: User):
    logger.info(user.username)
    await msg.answer(_('''🎮🌲 <b>BitcoinXBot</b> • безопасный кошелёк-хранилище и процессор платежей с железобетонной безопасностью и безупречным интерфейсом. <b>Закрепи в топе.</b> /info

Ваши фиатные балансы: ≈ 0.0000 <b>BTC</b>
🇺🇸 0.0000 <b>USD</b>

Ваша криптовалюта:
🦚 0.00000000 <b>BTC</b>

Заработано: 🌲 0.00000000 <b>BTC</b>
Приглашено: 0 пользователей.'''))


async def bot_help(msg: types.Message):
    text = [
        'Список команд: ',
        '/start - Начать диалог',
        '/help - Получить справку'
    ]
    await msg.answer('\n'.join(text))
