from aiogram import Bot, Router
from aiogram.filters import CommandStart
from aiogram.types import Message


router = Router()


@router.message(CommandStart())
async def process_cmd_start_admin(message: Message, bot: Bot) -> None:
    await message.answer(text='Bot is ready, admin')
