from aiogram import Bot
from aiogram.types import BotCommand

commands_dict = {
    '/start': 'Start/re-start bot',
    '/help': 'Show all commands',
    '/desc': 'Bot`s description',
    '/what': 'Who is Gargantua',
    '/weight': 'Record your weight',
    '/measure': 'Record your weight',
    '/setup': 'Setup your bot',
    '/account': 'Setup/view your account',
    '/report': 'Show report',
    '/support': 'Contact support',
    '/contacts': 'Contact us'
}

# TODO: finish it
# function for set bot commands in 'menu' button
async def set_main_menu(bot: Bot):
    main_menu_command = [BotCommand(command=cmd, description=desc) for cmd, desc in commands_dict.items()]
    
    await bot.set_my_commands(main_menu_command)
