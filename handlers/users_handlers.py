from time import sleep

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from aiogram_dialog import DialogManager, StartMode

from dialogs.users_dialogs import StartSG, WhatSG, MeasureSG, SetupSG, AccountSG

router = Router()


# handler for /start cmd
@router.message(CommandStart())
async def process_cmd_start(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=StartSG.start_dialog, mode=StartMode.RESET_STACK)
    sleep(1)
    await dialog_manager.start(state=StartSG.start_dialog_help)
    sleep(1)
    await dialog_manager.start(state=StartSG.start_dialog_desc)


# handler for /help cmd
@router.message(Command(commands=['help']))
async def process_help_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=StartSG.help_dialog)


# handler for bot`s description cmd
@router.message(Command(commands=['desc']))
async def process_desc_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=StartSG.desc_dialog)


# handler for Gargantua`s story cmd
@router.message(Command(commands=['what']))
async def process_what_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=WhatSG.start_what)
    
    
# handler for weight record
@router.message(Command(commands=['weight', 'kg']))
async def process_weight_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=MeasureSG.start_weight)


# handler for /measure cmd
@router.message(Command(commands=['measure', 'cm']))
async def process_measure_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=MeasureSG.start_measure)


# handler for /setup cmd
@router.message(Command(commands=['setup']))
async def process_setup_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=SetupSG.start_setup)


# handler for /account cmd
@router.message(Command(commands=['account']))
async def process_account_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=AccountSG.start_account)
