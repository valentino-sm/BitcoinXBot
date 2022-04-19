from aiogram import types
from aiogram.utils import exceptions
from loguru import logger


async def error_handler(update: types.Update, exception: exceptions.TelegramAPIError):
    """
    Exceptions handler. Catches all exceptions within task factory tasks.
    :param dispatcher:
    :param update:
    :param exception:
    :return: stdout logging
    """

    if isinstance(exception, exceptions.MessageNotModified):
        logger.exception('Message is not modified')
        # do something here?
        return True

    if isinstance(exception, exceptions.MessageToDeleteNotFound):
        logger.exception(f'MessageToDeleteNotFound: {exception} \nUpdate: {update}')
        # do something here?
        return True

    if isinstance(exception, exceptions.CantParseEntities):
        # or here
        logger.exception(f'CantParseEntities: {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, exceptions.InvalidQueryID):
        # or here
        logger.exception(f'InvalidQueryID: {exception} \nUpdate: {update}')
        return False

    #  MUST BE THE LAST CONDITION (ЭТО УСЛОВИЕ ВСЕГДА ДОЛЖНО БЫТЬ В КОНЦЕ)
    if isinstance(exception, exceptions.TelegramAPIError):
        logger.exception(f'TelegramAPIError: {exception} \nUpdate: {update}')
        return True

    # At least you have tried.
    logger.exception(f'Update: {update} \n{exception}')
