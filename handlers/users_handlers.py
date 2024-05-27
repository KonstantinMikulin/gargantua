from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from aiogram_dialog import DialogManager, StartMode

from dialogs.users_dialogs import UserSG, WhatSG

router = Router()


@router.message(CommandStart())
async def process_cmd_start(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=UserSG.start_dialog, mode=StartMode.RESET_STACK)


@router.message(Command(commands=['help']))
async def process_help_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=UserSG.help_dialog)


@router.message(Command(commands=['desc']))
async def process_desc_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=UserSG.desc_dialog)


@router.message(Command(commands=['what']))
async def process_what_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=WhatSG.start_what)
