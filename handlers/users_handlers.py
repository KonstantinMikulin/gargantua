from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from aiogram_dialog import DialogManager, StartMode

from dialogs.users_dialogs import UserSG, WhatSG, MeasureSG

router = Router()


# handler for /start cmd
@router.message(CommandStart())
async def process_cmd_start(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=UserSG.start_dialog, mode=StartMode.RESET_STACK)


# handler for /help cmd
@router.message(Command(commands=['help']))
async def process_help_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=UserSG.help_dialog)


# handler for bot`s description cmd
@router.message(Command(commands=['desc']))
async def process_desc_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=UserSG.desc_dialog)


# handler for Gargantua`s story cmd
@router.message(Command(commands=['what']))
async def process_what_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=WhatSG.start_what)
    
    
# handler for weight record
@router.message(Command(commands=['weight']))
async def process_weight_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=MeasureSG.start_weight)



