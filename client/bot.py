import os

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.markdown import link
import markups as keyboard
from common.constants import UserMessage, SubscribesMessage


# Создаём экземпляр бота
onhockey_bot = Onhockey(os.environ['5111619706:AAEUgA1jzuQBf0K2krF81_sKqlD1Xg3SVtw'], parse_mode=types.ParseMode.MARKDOWN_V2)
dispatcher = Dispatcher(onhockey_bot)


# Обработка первого сообщения
@dispatcher.message_handler(commands=['start', 'go'])
async def start_handler(message: types.message):
    await onhockey_bot.send_escaped_message(
        message.from_user.id,
        UserMessage.START
    )

# Доступные команды
@dispatcher.message_handler(commands=['help'])
async def help_handler(message: types.message):
    await onhockey_bot.send_escaped_message(
        message.from_user.id,
        UserMessage.HELP + '\n\n' + UserMessage.START
    )
