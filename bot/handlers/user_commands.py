import logging

from aiogram import Router
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.state import default_state

from aiogram_dialog import DialogManager

logger = logging.getLogger(__name__)

# creating router`s object
user_router = Router(name="user router")


# simple /start command
@user_router.message(CommandStart(), StateFilter(default_state))
async def cmd_start_first(message: Message):
    await message.answer(f"<b>{message.from_user.first_name}</b>, здравствуйте!\n" # type:ignore
                         f"Подробности о работе бота по команде /help")


# /help command
@user_router.message(Command("help"), StateFilter(default_state))
async def cmd_help(message: Message, dialog_manager: DialogManager):
    await message.answer("Бот может записывать вес и замеры объемов тела")
    print(dialog_manager.current_context().state)
