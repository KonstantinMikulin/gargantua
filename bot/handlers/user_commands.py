import logging

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.api.exceptions import NoContextError

from bot.dialogs import MainMenuSG, GetLastRecordsSG

logger = logging.getLogger(__name__)

# creating router`s object
user_router = Router(name="user router")


# simple /start command
@user_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"<b>{message.from_user.first_name}</b>, здравствуйте!\n" # type:ignore
                         f"Подробности о работе бота по команде /help")
    
    
@user_router.message(Command("main"))
async def cmd_main_menu(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=MainMenuSG.main_state, mode=StartMode.RESET_STACK)

# /help command
@user_router.message(Command("help"))
async def cmd_help(message: Message, dialog_manager: DialogManager):
    await message.answer("Бот может записывать вес и замеры объемов тела")


# simple command to get last weight
@user_router.message(Command("last"))
async def cmd_stats(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=GetLastRecordsSG.choose, mode=StartMode.RESET_STACK)
    
    
# show current state
@user_router.message(Command("state"))
async def cmd_state(message: Message, dialog_manager: DialogManager):
    try:
        msg = {dialog_manager.current_context().state.state}
    except NoContextError:
        await message.answer("No current state")
    else:
        await message.answer(str(msg))
        
        
#TODO: remove this handler
# reset aiogram_dialog stack
@user_router.message(Command("cancel"))
async def cmd_cancel(message: Message, dialog_manager: DialogManager):
    await dialog_manager.reset_stack()
    await message.answer(text="Reset stack")
    