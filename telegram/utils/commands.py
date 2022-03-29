from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram import Bot


async def register(bot: Bot):
    await bot.set_my_commands(
        commands=[
            BotCommand('info', 'О боте')
        ],
        scope=BotCommandScopeDefault()
    )
