import logging

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from aiogram_dialog import DialogManager, StartMode

# TODO: refactor this
from sqlalchemy.ext.asyncio import AsyncSession

from bot.dialogs import MainMenuSG, GetLastRecordsSG

from bot.db import get_weights

logger = logging.getLogger(__name__)

# creating router`s object
user_router = Router(name="user router")


# simple /start command
@user_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"<b>{message.from_user.first_name}</b>, здравствуйте!\n" # type:ignore
                         f"<b>Основное меню</b> по команде /main\n"
                         f"<b>Подробности</b> о работе бота по команде /help"
                         )
    
    
@user_router.message(Command("main"))
async def cmd_main_menu(
    message: Message,
    dialog_manager: DialogManager
    ):
    await dialog_manager.start(
        state=MainMenuSG.main_state,
        mode=StartMode.RESET_STACK
        )

# /help command
@user_router.message(Command("help"))
async def cmd_help(
    message: Message,
    dialog_manager: DialogManager
    ):
    await message.answer(
        "Бот может сохранять вес и замеры объемов тела\n"
        "Основное меню - /main\n"
        "Сохранить вес - /weight\n"
        "Записать объёмы тела - /measure\n"
        "Посмотреть последние сохранённые записи - /last\n"
        )


# simple command to get last weight
@user_router.message(Command("last"))
async def cmd_stats(
    message: Message,
    dialog_manager: DialogManager
    ):
    await dialog_manager.start(
        state=GetLastRecordsSG.choose,
        mode=StartMode.RESET_STACK
        )
    
    
# TODO: change this temp handler
@user_router.message(Command("get"))
async def cmd_get(
    message: Message,
    session: AsyncSession
):
    weights = await get_weights(
        session=session,
        telegram_id=message.from_user.id # type: ignore
    )
    weights_list = []
    for weight in weights:
        weights_list.append(f"{weight.created_at}: {weight.weight}\n")
    msg_text = "".join(weights_list)
    await message.answer(msg_text)
    