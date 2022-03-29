from aiogram import Dispatcher
from aiogram.utils import exceptions

from .error_handler import error_handler


def setup(dp: Dispatcher):
    dp.register_errors_handler(error_handler)
