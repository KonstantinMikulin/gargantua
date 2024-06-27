import html

from aiogram import Router, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.deep_linking import create_start_link

from filters.filters import AdminIDFilter

admin_router = Router()
admin_router.message.filter(AdminIDFilter())


# TODO: change this logic
# /start cmd for admins
@admin_router.message(CommandStart())
async def process_start_admin(message: Message, config) -> None:
    await message.answer('Hello, admin!!!')


# TODO: change this logic
# /report handler for logs and reports
@admin_router.message(Command(commands=['report']))
async def process_report_admin(message: Message) -> None:
    await message.answer('Here are your logs, captain!')


# TODO: change this logic
# /status cmd for checking bot status
@admin_router.message(Command(commands=['status']))
async def process_status_admin(message: Message) -> None:
    await message.answer('Status is stable, captain!')


# handler to create invite link
@admin_router.message(Command(commands=['link']))
async def create_invite_link(message: Message, bot: Bot) -> None:
    link = await create_start_link(bot, 'score')
    await message.answer(f'Here you go: {html.escape(link)}')


# TODO: make handler for downloading photo
pass
