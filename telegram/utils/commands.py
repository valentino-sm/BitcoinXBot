from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram import Bot

from utils.i18n import gettext as _


async def register(bot: Bot):
    await bot.set_my_commands(
        commands=[
            BotCommand('info', _('About this bot /// о боте')),
            BotCommand('pass', _('Advanced /// расширенные функции')),
            BotCommand('faq', _('Faq /// ответы на вопросы')),
            BotCommand('rates', _('Rates explanation /// объяснение курсов обмена')),
            BotCommand('sbp', _('Sberbank sbp /// сбербанк сбп')),
            BotCommand('atm', _('Tinkoff atms /// банкоматы тинькофф')),
            BotCommand('atmusd', _('Tinkoff (usd) atms /// банкоматы тинькофф (usd)')),
            BotCommand('start', _('(re)start bot /// перезапустить бот')),
            BotCommand('id', _('Your id /// ваш id')),
        ],
        scope=BotCommandScopeDefault()
    )
