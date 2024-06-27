import html

from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.deep_linking import create_start_link

admin_router = Router()


# TODO: set filtration for admin cmds
# handler to create invite link
@admin_router.message(Command(commands=['link']))
async def create_invite_link(message: Message, bot: Bot) -> None:
    link = await create_start_link(bot, 'score')
    await message.answer(f'Here you go: {html.escape(link)}')


# TODO: make handler for downloading photo
pass
