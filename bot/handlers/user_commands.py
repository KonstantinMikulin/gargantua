import logging

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

logger = logging.getLogger(__name__)

# creating router`s onject
user_router = Router(name="user router")


# simple /start command
@user_router.message(CommandStart())
async def cmd_admin_start(message: Message, state: FSMContext):
    logger.info("Enter user`s /start handler")

    await state.clear()

    await message.answer("<b>User</b>, you sent /start! Welcome!")

    logger.info("Exit user`s /start handler")
