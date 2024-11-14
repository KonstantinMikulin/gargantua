import logging

from aiogram import Router
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

logger = logging.getLogger(__name__)

# creating router`s onject
user_router = Router(name="user router")


# simple /start command
@user_router.message(CommandStart())
async def cmd_start_first(message: Message):
    await message.answer(f"<b>{message.from_user.first_name}</b>, здравствуйте!\n" # type:ignore
                         f"Подробности о работе бота по команде /help")


# /help command
@user_router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Бот может записывать вес и замеры объемов тела")


# FSM /cancel command for default state
@user_router.message(Command(commands="cancel"), StateFilter(default_state))
async def cmd_cancel_default(message: Message):
    await message.answer("Сейчас нечего отменять")


# FSM /cancel if user in some state
@user_router.message(Command(commands="cancel"), ~StateFilter(default_state))
async def cmd_cancel_state(message: Message, state: FSMContext):
    logger.info("Enter 'some state' /cancel command")

    await message.answer("Вы отменили отправку данных")
    # reset state and clear any received data
    await state.clear()
    
    logger.info("Exit 'some state' /cancel command")
