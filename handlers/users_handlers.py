from time import sleep

from aiogram import Router, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.methods import CreateChatInviteLink

from aiogram_dialog import DialogManager, StartMode

from config.config import Config, load_config
from filters.filters import UserValidation
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

user_handlers_router = Router()
config: Config = load_config()


# handler for /start cmd
@user_handlers_router.message(CommandStart(), UserValidation())
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
@user_handlers_router.message(Command(commands=['help']))
async def process_help_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=HelpSG.start_help)


# handler for bot`s description cmd
@user_handlers_router.message(Command(commands=['desc']))
async def process_desc_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=DescSG.start_desc)


# handler for Gargantua`s story cmd
@user_handlers_router.message(Command(commands=['what']))
async def process_what_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=WhatSG.start_what)
    
    
# handler for weight record
@user_handlers_router.message(Command(commands=['weight', 'kg']))
async def process_weight_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=MeasureSG.start_weight)


# handler for /measure cmd
@user_handlers_router.message(Command(commands=['measure', 'cm']))
async def process_measure_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=MeasureSG.start_measure)


# handler for /setup cmd
@user_handlers_router.message(Command(commands=['setup']))
async def process_setup_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=SetupSG.start_setup)


# handler for /account cmd
@user_handlers_router.message(Command(commands=['account']))
async def process_account_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=AccountSG.start_account)

# handler for /report
@user_handlers_router.message(Command(commands=['report']))
async def process_report_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=ReportSG.start_report)
    

# TODO: create another logic for contacting with support/admin
# handler for /support
# allow text message from user and send it to support
@user_handlers_router.message(Command(commands=['support']))
async def process_support_cmd(message: Message, bot: Bot, dialog_manager: DialogManager, config) -> None:
    support = config.tg_bot.support_id[0]
    
    await dialog_manager.start(state=SupportSG.start_support)
    await bot.forward_message(chat_id=support, from_chat_id=message.chat.id, message_id=message.message_id)


# handler for /contacts
@user_handlers_router.message(Command(commands=['contacts']))
async def process_contacts_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=ContactsSG.start_contacts)
    
    
# TODO: make handler for processing messages which starts with '/', but commands not exist or was deleted
# @router.message


@user_handlers_router.message(Command(commands=['test']))
async def process_test_cmd(message: Message, config, bot: Bot) -> None:
    link = await bot.create_chat_invite_link(chat_id=message.chat.id)
    
    await message.answer(f'TEST: {link}')
    # await bot.forward_message(
    #     chat_id=config.tg_bot.support_id,
    #     from_chat_id=message.chat.id,
    #     message_id=message.message_id
    #     )


# @user_handlers_router.message()
# async def send_echo(message: Message):
#     try:
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         await message.reply(text='No no no')
