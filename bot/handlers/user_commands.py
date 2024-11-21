import logging

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from aiogram_dialog import DialogManager

from bot.db import get_last_weights

logger = logging.getLogger(__name__)

# creating router`s object
user_router = Router(name="user router")


# simple /start command
@user_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"<b>{message.from_user.first_name}</b>, здравствуйте!\n" # type:ignore
                         f"Подробности о работе бота по команде /help")


# /help command
@user_router.message(Command("help"))
async def cmd_help(message: Message, dialog_manager: DialogManager):
    await message.answer("Бот может записывать вес и замеры объемов тела")


@user_router.message(Command("stats"))
async def cmd_stats(message: Message, session):
    weights = await get_last_weights(session=session, number_of_weights=3)
    
    result = []
    
    for weight in weights:
        result.append(str(weight.weight))
        
    await message.answer(", ".join(result))
