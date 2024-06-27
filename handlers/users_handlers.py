import logging

from aiogram import Router, Bot, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, LinkPreviewOptions

from aiogram_dialog import DialogManager, StartMode, ShowMode

from lexicon.lexicon import LEXICON_COMMANDS
from states.users_dialog_states import (
    StartSG,
    HelpSG,
    DescSG,
    MeasureSG,
    SetupSG,
    AccountSG,
    ReportSG,
    SupportSG,
    ContactsSG
)

user_router = Router()

logger = logging.getLogger(__name__)


# TODO: add logic for creating user account
# handler for /start cmd
@user_router.message(CommandStart())
async def process_cmd_start(message: Message, dialog_manager: DialogManager, bot: Bot) -> None:
    logger.info('We are in /start handler')
    
    # deleting message with cmd from user
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    # TODO: add logic if account alredy exist but user restart bot
    await dialog_manager.start(state=StartSG.start_dialog, mode=StartMode.RESET_STACK, show_mode=ShowMode.DELETE_AND_SEND)
    
    logger.info('We are exiting /start handler')
    
    
# handler for /help cmd
@user_router.message(Command(commands=['help']))
async def process_help_cmd(message: Message, dialog_manager: DialogManager, bot: Bot) -> None:
    logger.info('We are in /help handler')
    
    # deleting message with cmd from user
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await dialog_manager.start(state=HelpSG.start_help, show_mode=ShowMode.DELETE_AND_SEND)
    
    logger.info('We are exiting /help handler')
    

# handler for bot`s description cmd
@user_router.message(Command(commands=['desc']))
async def process_desc_cmd(message: Message, dialog_manager: DialogManager, bot: Bot) -> None:
    # deleting message with cmd from user
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await dialog_manager.start(state=DescSG.start_desc, show_mode=ShowMode.DELETE_AND_SEND)


# TODO: add some messages with pics of Gargantua or picture of user himself
# handler for Gargantua`s story cmd
@user_router.message(Command(commands=['what']))
async def process_what_cmd(message: Message, dialog_manager: DialogManager) -> None:
    link_text = 'https://w.wiki/AHxi'
    option_1 = LinkPreviewOptions(
        url='https://w.wiki/AHxi',  
        prefer_small_media=True
    )
    
    await message.answer(f'Behold!\n\n{link_text}', link_preview_options=option_1)
    
    
# handler for weight record
@user_router.message(Command(commands=['weight', 'kg']))
async def process_weight_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=MeasureSG.start_weight, show_mode=ShowMode.DELETE_AND_SEND)


# handler for /measure cmd
@user_router.message(Command(commands=['measure', 'cm']))
async def process_measure_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=MeasureSG.start_measure, show_mode=ShowMode.DELETE_AND_SEND)


# handler for /setup cmd
@user_router.message(Command(commands=['setup']))
async def process_setup_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=SetupSG.start_setup, show_mode=ShowMode.DELETE_AND_SEND)


# handler for /account cmd
@user_router.message(Command(commands=['account']))
async def process_account_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=AccountSG.start_account, show_mode=ShowMode.DELETE_AND_SEND)


# TODO: add some sendChatAction
# handler for /report
@user_router.message(Command(commands=['report']))
async def process_report_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=ReportSG.start_report, show_mode=ShowMode.DELETE_AND_SEND)
    

# TODO: ? add some sendChatAction
# TODO: create another logic for contacting with support/admin
# handler for /support
# allow text message from user and send it to support
@user_router.message(Command(commands=['support']))
async def process_support_cmd(message: Message, bot: Bot, dialog_manager: DialogManager, config) -> None:
    support = config.tg_bot.support_ids[0]
    
    await dialog_manager.start(state=SupportSG.start_support, show_mode=ShowMode.DELETE_AND_SEND)
    await bot.forward_message(chat_id=support, from_chat_id=message.chat.id, message_id=message.message_id)


# handler for /contacts
@user_router.message(Command(commands=['contacts']))
async def process_contacts_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=ContactsSG.start_contacts, show_mode=ShowMode.DELETE_AND_SEND)


@user_router.message(F.text.startswith('/'))
async def process_unknown_cmd(message: Message) -> None:
    if message.text not in LEXICON_COMMANDS:
        await message.answer(text='I don`t know this command')


# handler for anything unknown for bot
@user_router.message()
async def say_what(message: Message) -> None:
    await message.answer(text='I don`t understand you :(')
