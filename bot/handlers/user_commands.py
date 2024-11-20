import logging

from aiogram import Router
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

logger = logging.getLogger(__name__)

# creating router`s object
user_router = Router(name="user router")


# simple /start command
@user_router.message(CommandStart())
async def cmd_start_first(message: Message):
    await message.answer(f"<b>{message.from_user.first_name}</b>, здравствуйте!\n" # type:ignore
                         f"Подробности о работе бота по команде /help")


# TODO: disable this command when FSM is on
# /help command
@user_router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Бот может записывать вес и замеры объемов тела")
    