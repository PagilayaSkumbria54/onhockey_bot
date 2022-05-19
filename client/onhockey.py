
import asyncio
from aiogram import Bot
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor, exceptions as aiogram_exceptions
from common.func import escape_telegram_char
from server.gino.sql.subscriptions import clear


async def send_escaped_message(self, user_id: int, message: types.message, **kwargs):
    try:
        await self.send_message(user_id, escape_telegram_char(message), **kwargs)
    except aiogram_exceptions.BotBlocked:
        await clear(user_id)
