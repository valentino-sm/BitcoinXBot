import asyncio
from typing import Union

from aiogram import types, Dispatcher
from aiogram.types import User
from aiogram.utils import exceptions
from loguru import logger

from utils import settings


async def reply(msg: Union[types.Message, types.CallbackQuery] = None, **kwargs) -> types.Message or None:
    r = None
    i = settings.reply_max_tries
    while not isinstance(r, types.Message) and i > 0:
        try:
            if isinstance(msg, types.Message):
                r = await msg.answer(**kwargs)
            elif isinstance(msg, types.CallbackQuery):
                await msg.answer()
                r = await msg.message.answer(**kwargs)
            else:
                logger.warning("None for both Message & CallbackQuery provided")
                await Dispatcher.get_current().bot.send_message(chat_id=User.get_current().id, **kwargs)
        except exceptions.RetryAfter as e:
            logger.error(f"Target [ID:{User.get_current().id}]: Flood limit is exceeded. Sleep {e.timeout} seconds.")
            await asyncio.sleep(e.timeout)
        except exceptions.ChatNotFound as e:
            logger.error(e)
            return
        except exceptions.BotBlocked as e:
            logger.error(e)
            return
        i -= 1
    return r
