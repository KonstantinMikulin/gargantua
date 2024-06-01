from aiogram import Bot
from aiogram.types import BotCommand


# TODO: finish it
main_menu_command = [
    BotCommand(
        command='/start',
        description='Start/re-start bot'
    ),
    BotCommand(
        command='/help',
        description='List of bot`s commands'
    ),
    BotCommand(
        command='/'
    )
]


# function for set bot commands in 'menu' button
async def set_main_menu(bot: Bot) -> None:
    