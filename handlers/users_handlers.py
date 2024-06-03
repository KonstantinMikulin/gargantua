from cgi import print_environ
from time import sleep

from aiogram import Router, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from aiogram_dialog import DialogManager, StartMode

from config.config import Config, load_config
from states.aiogram_dialog_states import (
    StartSG,
    HelpSG,
    DescSG,
    WhatSG,
    MeasureSG,
    SetupSG,
    AccountSG,
    ReportSG,
    SupportSG,
    ContactsSG
)

router = Router()
config: Config = load_config()


# handler for /start cmd
@router.message(CommandStart())
async def process_cmd_start(message: Message, dialog_manager: DialogManager) -> None:
    # TODO: uncomment sleep()
    await dialog_manager.start(state=StartSG.start_dialog, mode=StartMode.RESET_STACK)
    # sleep(1)
    await dialog_manager.start(state=StartSG.start_dialog_help)
    # sleep(2)
    await dialog_manager.start(state=StartSG.start_dialog_desc)
    # sleep(3)
    await dialog_manager.start(state=StartSG.create_account_on_start)


# handler for /help cmd
@router.message(Command(commands=['help']))
async def process_help_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=HelpSG.start_help)


# handler for bot`s description cmd
@router.message(Command(commands=['desc']))
async def process_desc_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=DescSG.start_desc)


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

# handler for /report
@router.message(Command(commands=['report']))
async def process_report_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=ReportSG.start_report)
    

# TODO: clean this handler
# handler for /support
# allow text message from user and send it to support
@router.message(Command(commands=['support']))
async def process_support_cmd(message: Message, bot: Bot, dialog_manager: DialogManager, config) -> None:
    support = config.tg_bot.support_id[0]
    await dialog_manager.start(state=SupportSG.start_support)
    await dialog_manager.switch_to(state=SupportSG.text_imput)
    # await bot.forward_message(chat_id=support, from_chat_id=message.chat.id, message_id=message.message_id)
    # TODO: add logic for sending message to dev


# handler for /contacts
@router.message(Command(commands=['contacts']))
async def process_contacts_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=ContactsSG.start_contacts)
    
    
# TODO: make handler for processing messages whick starts with '/' but commands not exist or was deleted
# @router.message
# pass    
