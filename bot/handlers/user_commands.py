import logging

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from aiogram_dialog import DialogManager, StartMode

from bot.dialogs import GetLastRecordsSG

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


# TODO: change this command to choose all types of records
# simple command to get last weight
@user_router.message(Command("last"))
async def cmd_stats(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=GetLastRecordsSG.choose, mode=StartMode.RESET_STACK)
    