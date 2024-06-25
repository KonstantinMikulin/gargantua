import logging
from time import sleep

from aiogram import Router, Bot, F, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.methods import CreateChatInviteLink
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile

from aiogram_dialog import DialogManager, StartMode

from config.config import Config, load_config
from filters.filters import UserValidation
from states.users_dialog_states import (
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
# TODO: remove this import
from config.config import USER_DATA

user_router = Router()

logger = logging.getLogger(__name__)


# TODO: remove this handler
# temp handler for testing scoring possibilities
@user_router.message(Command(commands=['score']))
@user_router.message(CommandStart(deep_link=True, magic=F.args == 'score'))
async def process_score_cmd(message: Message) -> None:
    USER_DATA['score'] += 1
    user_name = message.from_user.first_name
    
    await message.answer(f'{user_name}`s score now is {USER_DATA['score']}')


# handler for /start cmd
@user_router.message(CommandStart())
async def process_cmd_start(message: Message, dialog_manager: DialogManager) -> None:
    logger.info('We are in /start handler')
    
    # TODO: uncomment sleep()
    await dialog_manager.start(state=StartSG.start_dialog, mode=StartMode.RESET_STACK)
    # sleep(1)
    await dialog_manager.start(state=StartSG.start_dialog_help)
    # sleep(2)
    await dialog_manager.start(state=StartSG.start_dialog_desc)
    # sleep(3)
    await dialog_manager.start(state=StartSG.create_account_on_start)
    
    # TODO: fix this logic
    # temp solution
    await dialog_manager.reset_stack()
    
    logger.info('We are exiting /start handler')
    
    
# handler for /help cmd
@user_router.message(Command(commands=['help']))
async def process_help_cmd(message: Message, dialog_manager: DialogManager) -> None:
    logger.info('We are in /help handler')
    
    await dialog_manager.start(state=HelpSG.start_help)

    logger.info('We are exiting /help handler')
    

# handler for bot`s description cmd
@user_router.message(Command(commands=['desc']))
async def process_desc_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=DescSG.start_desc)


# handler for Gargantua`s story cmd
@user_router.message(Command(commands=['what']))
async def process_what_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=WhatSG.start_what)
    
    
# handler for weight record
@user_router.message(Command(commands=['weight', 'kg']))
async def process_weight_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=MeasureSG.start_weight)


# handler for /measure cmd
@user_router.message(Command(commands=['measure', 'cm']))
async def process_measure_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=MeasureSG.start_measure)


# handler for /setup cmd
@user_router.message(Command(commands=['setup']))
async def process_setup_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=SetupSG.start_setup)


# handler for /account cmd
@user_router.message(Command(commands=['account']))
async def process_account_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=AccountSG.start_account)

# handler for /report
@user_router.message(Command(commands=['report']))
async def process_report_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=ReportSG.start_report)
    

# TODO: create another logic for contacting with support/admin
# handler for /support
# allow text message from user and send it to support
@user_router.message(Command(commands=['support']))
async def process_support_cmd(message: Message, bot: Bot, dialog_manager: DialogManager, config) -> None:
    support = config.tg_bot.support_id[0]
    
    await dialog_manager.start(state=SupportSG.start_support)
    await bot.forward_message(chat_id=support, from_chat_id=message.chat.id, message_id=message.message_id)


# handler for /contacts
@user_router.message(Command(commands=['contacts']))
async def process_contacts_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=ContactsSG.start_contacts)


@user_router.message(Command('images'))  
async def upload_photo(message: Message) -> None:  
    # Сюда будем помещать file_id отправленных файлов, чтобы потом ими воспользоваться  
    file_ids = []  
  
    # Чтобы продемонстрировать BufferedInputFile, воспользуемся "классическим"  
    # открытием файла через `open()`. Но, вообще говоря, этот способ    # лучше всего подходит для отправки байтов из оперативной памяти    # после проведения каких-либо манипуляций, например, редактированием через Pillow    
    
    # with open("buffer_emulation.jpg", "rb") as image_from_buffer:  
    #     result = await message.answer_photo(  
    #         BufferedInputFile(  
    #             image_from_buffer.read(),  
    #             filename="image from buffer.jpg"  
    #         ),  
    #         caption="Изображение из буфера"  
    #     )  
    #     file_ids.append(result.photo[-1].file_id)  
  
    # Отправка файла из файловой системы  
    image_from_pc = FSInputFile("/mnt/c/Users/user/Pictures/giraffe.jpeg")  
    result = await message.answer_photo(  
        image_from_pc,  
        caption="Изображение из файла на компьютере"  
    )  
    file_ids.append(result.photo[-1].file_id)  
  
    # Отправка файла по ссылке  
    # image_from_url = URLInputFile("https://picsum.photos/seed/groosha/400/300")  
    # result = await message.answer_photo(  
    #     image_from_url,  
    #     caption="Изображение по ссылке"  
    # )  
    # file_ids.append(result.photo[-1].file_id) 
     
    await message.answer("Отправленные файлы:\n"+"\n".join(file_ids))


# @user_handlers_router.message(F.text)
# async def extract_data(message: Message) -> None:
#     print(message)

# @user_handlers_router.message()
# async def send_echo(message: Message):
#     try:
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         await message.reply(text='No no no')
