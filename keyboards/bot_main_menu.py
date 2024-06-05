from aiogram import Bot
from aiogram.types import BotCommand

from lexicon.lexicon import LEXICON_COMMANDS


# function for set bot commands in 'menu' button
async def set_main_menu(bot: Bot):
    main_menu_command = [BotCommand(command=cmd, description=desc) for cmd, desc in LEXICON_COMMANDS.items()]
    
    await bot.set_my_commands(main_menu_command)
