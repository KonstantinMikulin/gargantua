import html

from aiogram import Router, Bot, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.deep_linking import create_start_link

from aiogram_dialog import DialogManager, StartMode

from config.config import Config, load_config

admin_router = Router()


# handler to create invite link
@admin_router.message(Command(commands=['link']))
async def create_invite_link(message: Message, bot: Bot) -> None:
    link = await create_start_link(bot, 'score')
    await message.answer(f'Here you go: {html.escape(link)}')
